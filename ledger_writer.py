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
import re
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



# ---------------------------------------------------------------------------
# open-positions.md -- THE PRODUCER THAT WAS NEVER WRITTEN
# ---------------------------------------------------------------------------
#
# The skeleton commit f519266 (2026-07-19) created open-positions.md with the
# placeholder "(pending first signal)" and shipped this module alongside it.
# This module writes LEDGER_FILE and nothing else; no function anywhere in the
# repo, or in any of the four executors that import it (gov-contracts-trader,
# intraday-reversion, paper-trader, llm-trader), ever touched the position
# book. `_run(["git","add","ledger.md"])` is hardcoded, so even a file written
# by hand would not have been committed.
#
# So the file sat unchanged for five weeks while README.md advertised it, on a
# PUBLIC repo, as "current live paper-trade book". Not stale -- never started.
#
# PAPER ACCOUNTS ONLY, ENFORCED, NOT ASSUMED. This publishes to a public
# repository. Alpaca paper accounts start "PA"; TradeStation sim accounts start
# "SIM". Anything else is refused outright rather than filtered, because the
# failure mode of a filter that silently drops an unrecognised account is
# publishing it.
#
# TWO RULES, AND THE CRUDE ONE IS NOT RETIRED.
# The prefix test is the primary gate: it needs no network, cannot fail open on
# an outage, and is verified against all 8 real live account numbers (measured
# 2026-08-26 -- every one refused, every one of the 6 real sim accounts
# allowed). Its single assumption is a VENDOR FORMAT: that no broker will ever
# issue a live account number beginning "PA" or "SIM". Alpaca live numbers are
# digit strings today, so it holds today. It is still an assumption about
# someone else's namespace, and this repo has been bitten by exactly that
# before -- our vocabulary narrower than the vendor's.
#
# So the DB's own account_type is a CROSS-CHECK on top, not a replacement. If
# trading_accounts says an account is live, it is refused no matter what its
# prefix looks like. The prefix rule stays because a careful classifier that
# replaces a crude one inherits the crude one's blind spots plus its own; kept
# side by side, either can catch what the other misses.
#
# ORDER MATTERS: prefix first, DB second. A DB outage must not turn this into
# "publish anything" -- on any lookup failure the prefix verdict stands alone,
# which is exactly the protection that existed before the cross-check was
# added, so an outage is a return to the prior guarantee and never a weakening.

# No password: this repo is PUBLIC. libpq reads ~/.pgpass. See
# refresh_open_positions.py for the full reasoning.
_PG_URL = os.getenv("PIM_PG_URL",
                    "postgresql://pim_user@10.32.3.27:15433/pim_database")

OPEN_POSITIONS_FILE = LEDGER_ROOT / "open-positions.md"

_PAPER_PREFIXES = ("PA", "SIM")


def _prefix_says_paper(account_number: str) -> bool:
    a = (account_number or "").upper()
    return bool(a) and a.startswith(_PAPER_PREFIXES)


def _db_says_live(account_number: str) -> bool:
    """True only when the DB AFFIRMATIVELY says this account is not sim.

    Unknown is not live: an account absent from trading_accounts, or a DB that
    cannot be reached, returns False so the prefix rule decides alone. This
    function can only ever ADD refusals, never remove one.
    """
    try:
        import psycopg2
        with psycopg2.connect(_PG_URL, connect_timeout=5) as conn:
            with conn.cursor() as c:
                c.execute("SELECT account_type FROM trading_accounts "
                          "WHERE account_number = %s", (account_number,))
                row = c.fetchone()
                return bool(row) and (row[0] or "").lower() != "sim"
    except Exception:
        return False


# The DB `name` embeds the number and the tenants, e.g.
#   "paper1-sim (PA3JEJDWV0EH) — PIM crypto_aitb_1m_wide + QC congress-dpi/..."
# The published table wants the LABEL only: "paper1-sim". Everything from the
# first " (" or " —" onward is detail for operators, not for a public book, and
# the parenthesised number is exactly what we are not publishing.
# WHITESPACE IS REQUIRED before the delimiter. A first attempt used
# [(—-] with a bare hyphen in the class, which turned "paper1-sim" into
# "paper1" -- the hyphen inside the label matched before the separator did.
# Only " (" and " —"/" -" as SEPARATORS end the label.
# Split ONLY on " (" or " —". Not on a hyphen at all.
#  - a bare hyphen in the class turned "paper1-sim" into "paper1": the hyphen
#    INSIDE the label matched before any separator did.
#  - even requiring surrounding spaces, " - " turned "TS SIM - Margin" into
#    "TS SIM", which is lossy and would collide with "TS SIM - Cash" the moment
#    TradeStation accounts are added to this book.
# The parenthesised account number and the em-dash tenant list are the only
# things being stripped, so those are the only two separators recognised.
_LABEL_TAIL = re.compile(r"\s+\(.*$|\s+—.*$")


def account_label(account_number: str) -> str:
    """Short human label for an account, or the number if there is no name.

    FALLING BACK TO THE NUMBER IS DELIBERATE. These are paper accounts, so the
    number is not sensitive -- the gate above is what guarantees that, and it
    is unchanged and still keyed on the NUMBER, never on the label. A label
    lookup is cosmetic, so it must never be able to block or alter publishing:
    if the DB is unreachable the book still publishes, just less readably.
    Making legibility load-bearing on a network call would be trading a real
    property for a nice-to-have.
    """
    try:
        import psycopg2
        with psycopg2.connect(_PG_URL, connect_timeout=5) as conn:
            with conn.cursor() as c:
                c.execute("SELECT name FROM trading_accounts "
                          "WHERE account_number = %s", (account_number,))
                row = c.fetchone()
        if row and row[0]:
            label = _LABEL_TAIL.sub("", row[0]).strip()
            if label:
                return label
    except Exception:
        pass
    return account_number


def _is_paper(account_number: str) -> bool:
    if not _prefix_says_paper(account_number):
        return False
    if _db_says_live(account_number):
        print(f"[ledger] {account_number} looks like a paper account by prefix "
              f"but trading_accounts says it is NOT sim. Refusing. If this is "
              f"wrong, the DB row is wrong -- fix the row, not this check.")
        return False
    return True


def render_open_positions(rows: list[dict], as_of: str | None = None) -> str:
    """Markdown for the position book. Pure, so it is testable without a broker."""
    as_of = as_of or _now_utc()
    if not rows:
        return ("# Open Positions\n\n"
                "Alpaca paper-trade book. Regenerated from the BROKER, not from\n"
                "our own logs. TradeStation accounts are not included here.\n"
                f"Last updated: {as_of}\n\n"
                "_(no open positions)_\n")
    head = ("# Open Positions\n\n"
            "Alpaca paper-trade book. Regenerated from the BROKER, not from our\n"
            "own logs -- a book built from what we *think* we sent can drift with\n"
            "the log that produced it and agree while both are wrong.\n\n"
            "Scope: every active, trading-enabled Alpaca paper account, shown\n"
            "by name rather than by account number.\n"
            "TradeStation accounts are NOT covered -- the heading used to say\n"
            "\"current paper-trade book\", which claimed a completeness this\n"
            "producer has never had.\n"
            f"Last updated: {as_of}\n\n"
            "| Account | Symbol | Qty | Avg entry | Last | Unrealized |\n"
            "|---|---|---:|---:|---:|---:|\n")
    body = "".join(
        f"| {account_label(str(r.get('account','?')))} | {r.get('symbol','?')} | {r.get('qty','')} | "
        f"{r.get('avg_entry','')} | {r.get('last','')} | {r.get('unrealized','')} |\n"
        for r in rows)
    return head + body + f"\n{len(rows)} open position(s).\n"


def update_open_positions(rows: list[dict], push: bool = True) -> bool:
    """Rewrite + commit the position book. Returns True if it changed.

    Refuses to publish a non-paper account. Returns False on refusal rather
    than raising, because this is called from executors whose job is trading --
    a bookkeeping failure must never take a trader down.
    """
    live = [r for r in rows if not _is_paper(str(r.get("account", "")))]
    if live:
        print(f"[ledger] REFUSING to publish {len(live)} non-paper account row(s): "
              f"{sorted({str(r.get('account')) for r in live})}. "
              f"open-positions.md is a PUBLIC file.")
        return False
    try:
        new = render_open_positions(rows)
        old = OPEN_POSITIONS_FILE.read_text() if OPEN_POSITIONS_FILE.exists() else ""
        # Compare ignoring the timestamp line, or every run is a commit.
        def _strip(t: str) -> str:
            return "\n".join(l for l in t.splitlines()
                              if not l.startswith("Last updated:"))
        if _strip(new) == _strip(old):
            return False
        OPEN_POSITIONS_FILE.write_text(new)
    except Exception as e:
        print(f"[ledger] open-positions write failed: {e}")
        return False

    _run(["git", "add", "open-positions.md"], LEDGER_ROOT)
    rc, _ = _run(["git", "commit", "-m",
                  f"open-positions: {len(rows)} position(s)"], LEDGER_ROOT)
    if rc == 0 and push:
        _run(["git", "push"], LEDGER_ROOT)
    return True


# ---------------------------------------------------------------------------
# ONE __main__, AT THE END, AND THE LEDGER WRITE IS OPT-IN
# ---------------------------------------------------------------------------
#
# There used to be TWO `if __name__ == "__main__":` blocks -- one mid-file at
# line ~138 and another at ~215. Python runs top to bottom, so a direct
# `python ledger_writer.py` executed BOTH and then fell through into whatever
# was defined after them. The second one called
#
#     record("test", "SIGNAL", "AAPL", "smoke-test event ...")
#
# and `record()` defaults to flush_now=True, push=True. So running this file
# directly APPENDED A FABRICATED SIGNAL to ledger.md, committed it, and pushed
# it to a PUBLIC repository whose README states that every signal here was
# fired by the paper-trader. A fabricated row is indistinguishable from a real
# one to any reader, which makes it an integrity problem rather than clutter.
#
# Verified it never actually fired: no smoke-test row exists in ledger.md and
# no commit ever added one. Latent, not realised.
#
# A mid-file __main__ is also a trap for the next editor -- it reads as the end
# of the module. Appending below it (as the open-positions producer did) is
# invisible at a glance.
#
# The notification smoke test is harmless and stays default. The LEDGER write
# now requires an explicit flag, because a test that publishes to a public
# ledger is not a test.
if __name__ == "__main__":
    import sys as _sys

    if "--write-ledger" in _sys.argv:
        record("test", "SIGNAL", "AAPL",
               "smoke-test event from ledger_writer.py __main__")
        print("[ledger] smoke test WROTE AND PUSHED a row to the public ledger")
    else:
        notify("test", "BUY", "TEST", "smoke test from ledger_writer.__main__",
               is_test=True)
        print("[ledger] test notification sent with [TEST] marker "
              "(no ledger write; pass --write-ledger to publish a row)")
