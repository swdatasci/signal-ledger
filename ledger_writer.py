"""Shared ledger writer for paper-trader executors.

Appends a one-line event to /home/rford/caelum/signal-ledger/ledger.md
and (optionally) commits + pushes so the public repo updates in real time.

Both `paper-trader/executor.py` (Congress×DPI) and
`gov-contracts-trader/executor.py` import this and call `record()` after
every material event: signal-fired, entry-submitted, fill, exit.

Usage:
    from ledger_writer import record
    record("gov-contracts", "SIGNAL", "RTX",
           "DoD award $339M | signal_id=abc123")
    record("gov-contracts", "BUY", "RTX",
           "qty=15 @ $130.50 (paper) | order=xyz789")

Design choices:
- Append-only. Never mutates prior lines.
- Git commit + push is best-effort; if push fails (network, credentials),
  the local file is still updated. Users of the module do not raise on push
  failure — the trade log itself remains the source of truth.
- To avoid a commit per signal in bursts (e.g. batch scans), the module
  accepts a `flush_now=False` on record() and batches until flush() is called.
"""
from __future__ import annotations

import os
import subprocess
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

LEDGER_ROOT = Path("/home/rford/caelum/signal-ledger")
LEDGER_FILE = LEDGER_ROOT / "ledger.md"

# Pushover — credentials from env (set in ~/.bashrc as PUSHOVER_USER_KEY /
# PUSHOVER_API_TOKEN). If either is missing, notifications degrade silently.
PUSHOVER_URL = "https://api.pushover.net/1/messages.json"
PUSHOVER_USER = os.environ.get("PUSHOVER_USER_KEY", "")
PUSHOVER_TOKEN = os.environ.get("PUSHOVER_API_TOKEN", "")

TWITTER_HANDLE = "@research_signal"
LEDGER_PUBLIC_URL = "https://github.com/swdatasci/signal-ledger/blob/main/ledger.md"

# Buffer for batched events (avoid one git commit per signal in a burst)
_buffer: list[str] = []


def _now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def _run(cmd: list[str], cwd: Path, quiet: bool = True) -> tuple[int, str]:
    """Run a shell cmd, return (rc, combined_stdout_stderr)."""
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=30)
        out = (r.stdout or "") + (r.stderr or "")
        if not quiet and r.returncode != 0:
            print(f"[ledger] cmd failed rc={r.returncode}: {' '.join(cmd)}")
            print(f"[ledger] {out}")
        return r.returncode, out
    except Exception as e:
        return 1, f"exception: {e}"


def tweet_intent_url(text: str) -> str:
    """Return a twitter.com/intent/tweet URL that pre-fills the compose window.
    Sanctioned by X — no automation risk. User taps → X opens → user hits Post."""
    return "https://twitter.com/intent/tweet?text=" + urllib.parse.quote(text)


def _format_tweet(strategy: str, action: str, ticker: str, notes: str) -> str:
    """Build a tweet under X's 280-char limit. Includes ledger URL if room."""
    # Distinctive per-strategy prefix so subscribers can pattern-match:
    prefix = {
        "gov-contracts": "[SIGNAL] Gov-contracts",
        "congress-dpi":  "[SIGNAL] Congress×DPI",
    }.get(strategy, f"[SIGNAL] {strategy}")

    core = f"{prefix} {action} {ticker} — {notes}"
    tail = f"\n\nLedger: {LEDGER_PUBLIC_URL}\nNot investment advice."
    # X limit is 280. Reserve room for the tail.
    max_core = 280 - len(tail)
    if len(core) > max_core:
        core = core[:max_core - 3] + "..."
    return core + tail


def _pushover(title: str, message: str, url: str | None = None,
              url_title: str = "Tap to compose tweet", priority: int = 0) -> bool:
    """Send a single pushover notification. Returns True on success. Never raises.

    priority: -2 (silent), -1 (quiet), 0 (default), 1 (high), 2 (emergency)."""
    if not (PUSHOVER_USER and PUSHOVER_TOKEN):
        return False
    data = {
        "token": PUSHOVER_TOKEN,
        "user": PUSHOVER_USER,
        "title": title,
        "message": message,
        "priority": str(priority),
    }
    if url:
        data["url"] = url
        data["url_title"] = url_title
    try:
        encoded = urllib.parse.urlencode(data).encode()
        req = urllib.request.Request(PUSHOVER_URL, data=encoded, method="POST")
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status == 200
    except Exception as e:
        print(f"[ledger] pushover failed: {e}")
        return False


def notify(strategy: str, action: str, ticker: str, notes: str = "",
           *, is_test: bool = False) -> None:
    """Fire-and-forget push notification with pre-composed tweet intent URL.
    User taps notification → X compose opens pre-filled → user hits Post.
    Never raises.

    is_test=True marks the notification as [TEST] so it can't be confused with
    a real trade. Real trades should always pass is_test=False (the default)."""
    tweet_text = _format_tweet(strategy, action, ticker, notes)
    intent = tweet_intent_url(tweet_text)
    test_prefix = "[TEST] " if is_test else ""
    test_note = " (SMOKE TEST — do not post)" if is_test else ""
    _pushover(
        title=f"{test_prefix}[{strategy}] {action} {ticker}",
        message=f"{notes}{test_note}\n\nTap to compose tweet →",
        url=intent if not is_test else None,  # no tap-URL on tests
        url_title=f"Compose from {TWITTER_HANDLE}",
        priority=1 if not is_test else 0,     # lower priority for tests
    )


if __name__ == "__main__":
    # Any direct invocation of this module is a test by definition.
    notify("test", "BUY", "TEST", "smoke test from ledger_writer.__main__",
           is_test=True)
    print("[ledger] test notification sent with [TEST] marker")


def record(strategy: str, action: str, ticker: str, notes: str = "",
           *, flush_now: bool = True, push: bool = True) -> None:
    """Append one event to the ledger.

    - strategy: short strategy tag ("gov-contracts", "congress-dpi")
    - action: SIGNAL | BUY | SELL | STOP | TP | SKIP | ERROR
    - ticker: uppercase symbol
    - notes: freeform, single-line context
    - flush_now: commit + push immediately. Set False when appending many
      rows in a burst; call flush() once at the end.
    - push: send pushover notification with pre-composed tweet intent URL.
      Only fires for BUY/SELL (skip SIGNAL/SKIP/ERROR to avoid notification
      spam during dedup passes). Set explicitly True/False to override.
    """
    ts = _now_utc()
    line = f"{ts} | {strategy:15s} | {action:8s} | {ticker:6s} | {notes}"
    _buffer.append(line)
    if flush_now:
        flush()
    # Pushover only for trade events (BUY/SELL). Everything else is bookkeeping.
    if push and action.upper() in ("BUY", "SELL"):
        notify(strategy, action, ticker, notes)


def flush() -> None:
    """Persist buffered lines + commit + push."""
    if not _buffer:
        return
    if not LEDGER_FILE.parent.exists():
        # Ledger dir missing — degrade gracefully
        _buffer.clear()
        return

    lines = list(_buffer)
    _buffer.clear()

    # Append lines to ledger.md — insert AFTER the "## Events" header so
    # newest events remain on top (chronological within one flush is fine).
    try:
        content = LEDGER_FILE.read_text() if LEDGER_FILE.exists() else ""
    except Exception:
        content = ""

    marker = "## Events\n"
    if marker in content:
        head, tail = content.split(marker, 1)
        # Strip the "_(no events yet — ...)_" placeholder if present
        tail_stripped = tail.lstrip()
        if tail_stripped.startswith("_(no events yet"):
            end = tail_stripped.find("\n")
            tail_stripped = tail_stripped[end + 1:] if end >= 0 else ""
        new_content = head + marker + "\n" + "\n".join(lines) + "\n" + tail_stripped
    else:
        new_content = (content or "# Signal Ledger\n\n## Events\n\n") + "\n".join(lines) + "\n"

    try:
        LEDGER_FILE.write_text(new_content)
    except Exception as e:
        print(f"[ledger] write failed: {e}")
        return

    # Commit + push (best-effort — never raise)
    msg = lines[0][:80] if len(lines) == 1 else f"{len(lines)} events"
    _run(["git", "add", "ledger.md"], LEDGER_ROOT)
    rc, out = _run(["git", "commit", "-m", f"ledger: {msg}"], LEDGER_ROOT)
    if rc == 0:
        # Non-blocking push; if network is down we've still committed locally
        _run(["git", "push", "origin", "HEAD"], LEDGER_ROOT)


if __name__ == "__main__":
    # Smoke test
    record("test", "SIGNAL", "AAPL", "smoke-test event from ledger_writer.py __main__")
    print("[ledger] smoke test complete — check ledger.md")
