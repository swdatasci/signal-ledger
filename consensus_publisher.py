#!/usr/bin/env python3
"""consensus_publisher.py — daily publisher for ai-consensus-daemon output.

Reads the ai_consensus_daily PG table (populated by
~/caelum/news-stream-regime/services/ai_consensus_daemon/daemon.py),
formats yesterday's predictions to markdown, writes to
~/caelum/signal-ledger/consensus/YYYY-MM-DD.md, commits + pushes.

Design notes:
- READS the daemon's output table; does NOT run any LLM calls of its own.
  So no rate-limit exposure, no duplicate data collection.
- Uses the same PG connection string the daemon uses (REGIME_PG_URL env,
  default matches daemon's default).
- No cron — infinite loop, wakes up at 05:00 UTC daily and publishes
  yesterday's day. If already published, no-op. If daemon hasn't written
  yet, wait and retry.
- Runs as a pm2 service: `consensus-publisher`.
- Never touches ai_consensus_daemon's data. Never mutates the DB.

Publishing safeguard: if a day has been already committed (file exists AND
in git history), skip. Never re-writes a published day (that would look
like retroactive edits and break the tamper-evident-timestamp promise).
"""
from __future__ import annotations

import os
import subprocess
import sys
import time
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

try:
    import psycopg2
    import psycopg2.extras
except ImportError:
    print("[fatal] psycopg2 not installed — run: uv pip install psycopg2-binary")
    sys.exit(2)

PG_URL = os.getenv(
    "REGIME_PG_URL",
    "postgresql://pim_user:pim_secure_2025%21@10.32.3.27:15433/pim_database",
)
LEDGER_ROOT = Path("/home/rford/caelum/signal-ledger")
CONSENSUS_DIR = LEDGER_ROOT / "consensus"
PUBLISH_HOUR_UTC = 5   # daemon runs at 04:00 UTC; give it 1h to complete


# --------------------------------------------------------------------------- #
# DB access                                                                    #
# --------------------------------------------------------------------------- #

def fetch_day(conn, day: date) -> list[dict]:
    """Return all ai_consensus_daily rows for the given prediction day."""
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute(
            """
            SELECT day, scope_type, scope_value, model, prompt_style,
                   direction, magnitude, confidence, reasoning,
                   n_articles_in_context, prompt_tokens, completion_tokens,
                   latency_ms, generated_at
            FROM ai_consensus_daily
            WHERE day = %s
            ORDER BY scope_type, scope_value, model, prompt_style
            """,
            (day,),
        )
        return list(cur.fetchall())


def fetch_agreement(conn, day: date) -> list[dict]:
    """Return per-scope aggregate agreement rows for the given day."""
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute(
            """
            SELECT day, scope_type, scope_value,
                   n_naive, n_sophisticated,
                   naive_direction, soph_direction,
                   naive_magnitude, soph_magnitude,
                   naive_consensus_strength, soph_consensus_strength,
                   divergence
            FROM ai_consensus_agreement_daily
            WHERE day = %s
            ORDER BY scope_type, scope_value
            """,
            (day,),
        )
        return list(cur.fetchall())


# --------------------------------------------------------------------------- #
# Markdown formatting                                                          #
# --------------------------------------------------------------------------- #

def _dir_str(d: int) -> str:
    return {-1: "↓", 0: "→", 1: "↑"}.get(d, "?")


def format_day(day: date, rows: list[dict], agreement: list[dict]) -> str:
    if not rows:
        return None  # nothing to publish

    total_tokens = sum(
        (r.get("prompt_tokens") or 0) + (r.get("completion_tokens") or 0)
        for r in rows
    )
    scopes = sorted({(r["scope_type"], r["scope_value"]) for r in rows})
    models = sorted({r["model"] for r in rows})

    lines = []
    lines.append(f"# AI Consensus — {day.isoformat()}")
    lines.append("")
    lines.append(f"_Published from `ai_consensus_daily` PG table_")
    lines.append(f"_Rows: {len(rows)}, scopes: {len(scopes)}, models: {len(models)}, "
                 f"total tokens: {total_tokens:,}_")
    lines.append("")
    lines.append("**Research phase — not a tradeable signal, not investment advice.** "
                 "See `README.md` in this directory for methodology.")
    lines.append("")

    # Aggregate table
    lines.append("## Aggregate agreement per scope")
    lines.append("")
    if agreement:
        lines.append("| Scope | N naive | N soph | Naive dir | Soph dir | "
                     "Naive strength | Soph strength | Divergence |")
        lines.append("|---|---|---|---|---|---|---|---|")
        for a in agreement:
            scope = f"{a['scope_type']}/{a['scope_value']}"
            lines.append(
                f"| {scope} | {a['n_naive']} | {a['n_sophisticated']} | "
                f"{a['naive_direction']:+.2f} | {a['soph_direction']:+.2f} | "
                f"{a['naive_consensus_strength']:.2f} | {a['soph_consensus_strength']:.2f} | "
                f"{a['divergence']:+.2f} |"
            )
        lines.append("")
        lines.append("_Divergence > 0 → naive panel more bullish than sophisticated; "
                     "|divergence| > 0.5 = notable style disagreement._")
    else:
        lines.append("_(no aggregate view available — materialized view may need refresh)_")
    lines.append("")

    # Per-scope, per-model reasoning
    lines.append("## Per-model reasoning")
    lines.append("")
    grouped = defaultdict(list)
    for r in rows:
        key = (r["scope_type"], r["scope_value"])
        grouped[key].append(r)

    for scope_key in sorted(grouped.keys()):
        st, sv = scope_key
        lines.append(f"### {st}/{sv}")
        lines.append("")
        for r in grouped[scope_key]:
            arrow = _dir_str(r["direction"])
            reasoning = (r.get("reasoning") or "").strip().replace("\n", " ")
            if len(reasoning) > 400:
                reasoning = reasoning[:397] + "..."
            lines.append(
                f"- **{r['model']}** _({r['prompt_style']})_: "
                f"**{arrow}** dir={r['direction']:+d}, "
                f"mag={r['magnitude']:.2f}, conf={r['confidence']:.2f} "
                f"— {reasoning or '_(no reasoning provided)_'}"
            )
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(f"_Committed at {datetime.now(timezone.utc).isoformat(timespec='seconds')} "
                 f"by `consensus_publisher.py`._")

    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# Git plumbing                                                                 #
# --------------------------------------------------------------------------- #

def _run(cmd: list[str], cwd: Path) -> tuple[int, str]:
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=30)
        return r.returncode, (r.stdout or "") + (r.stderr or "")
    except Exception as e:
        return 1, f"exception: {e}"


def _refresh_index() -> None:
    """Regenerate consensus/index.md with links to newest 30 days."""
    idx_path = CONSENSUS_DIR / "index.md"
    days = sorted(
        [p.stem for p in CONSENSUS_DIR.glob("20*.md")],
        reverse=True,
    )[:30]
    if not days:
        return
    links = "\n".join(f"- [{d}](./{d})" for d in days)
    idx = (
        "---\ntitle: AI Consensus — index\n---\n\n"
        "# AI Consensus — daily predictions\n\n"
        "Passive observation ledger. See [README](./README) for methodology.\n"
        "**Research phase — not a tradeable signal, not investment advice.**\n\n"
        "Each entry: 3 LLMs (Claude, GPT, Gemini) × 2 prompt styles (naive, "
        "sophisticated) × N tradable scopes, published the morning after collection.\n\n"
        "## Recent days\n\n"
        f"{links}\n\n"
        "## Source of truth\n\n"
        "Repo (tamper-evident git commits): "
        "[github.com/swdatasci/signal-ledger/tree/main/consensus]"
        "(https://github.com/swdatasci/signal-ledger/tree/main/consensus)\n\n"
        "Every entry has an anchored commit — nobody (including us) can edit "
        "a past prediction without leaving a git-history trail.\n"
    )
    idx_path.write_text(idx)


def publish_file(day: date, content: str) -> bool:
    """Write + commit + push. Returns True on new-commit success."""
    CONSENSUS_DIR.mkdir(parents=True, exist_ok=True)
    fpath = CONSENSUS_DIR / f"{day.isoformat()}.md"
    if fpath.exists():
        # Never rewrite a published day — protects tamper-evident timestamps
        print(f"[skip] {fpath.name} already exists — not rewriting")
        return False
    fpath.write_text(content)
    _refresh_index()
    rel_new = str(fpath.relative_to(LEDGER_ROOT))
    rel_idx = str((CONSENSUS_DIR / "index.md").relative_to(LEDGER_ROOT))
    rc, out = _run(["git", "add", rel_new, rel_idx], LEDGER_ROOT)
    if rc != 0:
        print(f"[git] add failed: {out}")
        return False
    rc, out = _run(
        ["git", "commit", "-m", f"consensus: publish {day.isoformat()}"],
        LEDGER_ROOT,
    )
    if rc != 0:
        print(f"[git] commit failed: {out}")
        return False
    rc, out = _run(["git", "push", "origin", "HEAD"], LEDGER_ROOT)
    if rc != 0:
        print(f"[git] push failed (committed locally): {out}")
    print(f"[publish] {fpath.name}")
    return True


# --------------------------------------------------------------------------- #
# Main loop                                                                    #
# --------------------------------------------------------------------------- #

def try_publish(target_day: date) -> str:
    """One-shot: attempt to publish target_day. Returns status string."""
    try:
        conn = psycopg2.connect(PG_URL, connect_timeout=15)
    except Exception as e:
        return f"db_error: {e}"

    try:
        rows = fetch_day(conn, target_day)
        agreement = fetch_agreement(conn, target_day)
    except Exception as e:
        conn.close()
        return f"query_error: {e}"
    conn.close()

    if not rows:
        return f"no_data_for_{target_day.isoformat()}"

    content = format_day(target_day, rows, agreement)
    if content is None:
        return "empty_content"

    ok = publish_file(target_day, content)
    return "published" if ok else "already_published"


def _sleep_until_next_publish(now_utc: datetime) -> None:
    target = now_utc.replace(hour=PUBLISH_HOUR_UTC, minute=0, second=0, microsecond=0)
    if now_utc >= target:
        target = target + timedelta(days=1)
    secs = (target - now_utc).total_seconds()
    print(f"[loop] sleeping {int(secs)}s until next publish at {target.isoformat()}")
    time.sleep(secs)


def loop() -> int:
    print("=" * 64)
    print(f"consensus_publisher  |  {datetime.now(timezone.utc).isoformat(timespec='seconds')}")
    print(f"PG: {PG_URL.split('@')[-1] if '@' in PG_URL else PG_URL}")
    print(f"target dir: {CONSENSUS_DIR}")
    print("=" * 64)

    # First: try to publish anything that already exists but hasn't been
    # published (backfill window: last 7 days).
    today = datetime.now(timezone.utc).date()
    for offset in range(1, 8):
        d = today - timedelta(days=offset)
        r = try_publish(d)
        print(f"[backfill] {d}: {r}")

    while True:
        try:
            _sleep_until_next_publish(datetime.now(timezone.utc))
            # Publish yesterday's day (daemon ran at 04:00 UTC for D-1 predictions)
            target_day = datetime.now(timezone.utc).date() - timedelta(days=1)
            print(f"\n[loop] publishing {target_day}")
            for attempt in range(3):
                status = try_publish(target_day)
                print(f"[loop] attempt {attempt+1}: {status}")
                if status == "published" or status == "already_published":
                    break
                if status.startswith("no_data"):
                    # Daemon may not have finished yet — wait 10min and retry
                    print("[loop] daemon output missing, retry in 600s")
                    time.sleep(600)
                    continue
                # DB error or other — wait 60s and retry
                time.sleep(60)
        except KeyboardInterrupt:
            print("\n[loop] interrupted")
            return 0
        except Exception as e:
            print(f"[loop] pass error (continuing): {type(e).__name__}: {e}")
            time.sleep(60)


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(description="Publish ai_consensus_daily to signal-ledger")
    ap.add_argument("--once", type=str, default=None,
                    help="Publish a single YYYY-MM-DD and exit (skip loop)")
    ap.add_argument("--backfill-days", type=int, default=None,
                    help="Publish last N days (unpublished only) and exit")
    args = ap.parse_args()

    if args.once:
        d = date.fromisoformat(args.once)
        print(try_publish(d))
        return 0
    if args.backfill_days:
        today = datetime.now(timezone.utc).date()
        for offset in range(1, args.backfill_days + 1):
            d = today - timedelta(days=offset)
            print(f"{d}: {try_publish(d)}")
        return 0

    return loop()


if __name__ == "__main__":
    sys.exit(main())
