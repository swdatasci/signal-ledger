#!/usr/bin/env python3
"""Rebuild open-positions.md from the BROKER.

Answers a question that had no answer: nothing ever wrote this file. The
skeleton commit created it 2026-07-19 with "(pending first signal)" and the
producer was never built, so a PUBLIC repo advertised a "current live
paper-trade book" that was empty for five weeks.

FROM THE BROKER, NOT FROM ledger.md. The obvious implementation is to replay
our own append-only log and derive a book from it. That book would then drift
with the log that produced it and the two would agree while both were wrong --
a manual trade, a crash between submit and record, or a fill we never saw would
be invisible in exactly the same way in both. The broker is the only thing that
knows what is actually held.

PAPER ONLY. update_open_positions() refuses non-paper accounts outright; this
script also filters before calling, so the refusal is a backstop rather than
the primary control.

ACCOUNTS COME FROM THE DB, NOT FROM A HARDCODED PAIR OF ENV NAMES
-----------------------------------------------------------------
This enumerated exactly two accounts -- whatever ALPACA_LLM_* and
ALPACA_PAPER_* happened to resolve to in the process env. There is a third
active, trading-enabled, unpaused Alpaca paper account (PA39YLUEFZFU, row 197)
whose credentials live in `trading_accounts` and have no env alias, so it was
never read and never appeared in the book.

MEASURED 2026-08-26: the file reported 13 positions across 2 accounts. The
exit-watcher, which enumerates the same three accounts FROM THE DB
(services/exit-watcher/watcher.py:446-458), reported `positions: 40` on the
same cycle. The 27 it could see and this file could not are all on
PA39YLUEFZFU -- and 12 of them were logging WOULD-FIRE-HORIZON on every cycle.
The account with every overdue exit in it was the one missing from the book.

So the account list is now resolved the way the exit-watcher resolves it: from
`trading_accounts`, filtered to alpaca + is_active + is_trading_enabled +
not paused. Env still supplies credentials when the DB row has none, so nothing
that worked before stops working. `_is_paper` remains the backstop and the DB
query is not trusted to keep live money out on its own.

A note on what this does NOT cover: TradeStation. intraday-reversion holds
positions on SIM1137629M continuously, and no TS account appears here, so the
book's "Current paper-trade book" heading has always meant "the Alpaca part of
it". The heading now says so rather than implying coverage it does not have.
"""
from __future__ import annotations

import json
import os
import sys
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import heartbeat  # noqa: E402
import ledger_writer as L  # noqa: E402

ALPACA = os.getenv("ALPACA_WRAPPER_URL", "http://10.32.3.27:8101")
PAPER_BASE = "https://paper-api.alpaca.markets"
# NO PASSWORD IN THIS DSN. THIS REPO IS PUBLIC.
# libpq reads ~/.pgpass (chmod 600) for the secret, so the credential lives on
# the box and never in the tree, in a commit, or in the process env where a
# `ps`/`pm2 env` dump would show it. The line this file needs:
#   10.32.3.27:15433:pim_database:pim_user:<password>
# PIM_PG_URL still overrides for anyone running this elsewhere.
PG_URL = os.getenv("PIM_PG_URL",
                   "postgresql://pim_user@10.32.3.27:15433/pim_database")
TS = os.getenv("TS_WRAPPER_URL", "http://10.32.3.27:8102")

# Must match ecosystem.open-positions.config.js. The checker reads the cron out
# of the heartbeat rather than being told it, so a Saturday -- when this cron
# does not fire at all -- is not mistaken for a dead job.
HEARTBEAT_NAME = "signal-ledger-open-positions"
HEARTBEAT_CRON = "*/30 6-14 * * 1-5"
# 40 minutes: one full */30 tick plus slack for a slow broker round-trip. Tight
# enough that a dead job is caught within one missed tick, loose enough that a
# single late run does not page.
HEARTBEAT_GRACE_MIN = 40


def _get(url: str, headers: dict, timeout: int = 30):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def alpaca_positions(account_label: str, key: str, secret: str, base: str) -> list[dict]:
    hdr = {"x-alpaca-key-id": key, "x-alpaca-secret-key": secret,
           "x-alpaca-base-url": base}
    try:
        data = _get(f"{ALPACA}/positions", hdr)
    except Exception as exc:
        print(f"  {account_label}: positions fetch failed ({type(exc).__name__}: "
              f"{str(exc)[:70]}) -- SKIPPED, not treated as flat")
        return None                      # None != [] : unknown is not empty
    rows = data if isinstance(data, list) else (data.get("positions") or [])
    out = []
    for p in rows:
        out.append({
            "account": account_label,
            "symbol": p.get("symbol"),
            "qty": p.get("qty"),
            "avg_entry": p.get("avg_entry_price"),
            "last": p.get("current_price"),
            "unrealized": p.get("unrealized_pl"),
        })
    return out


ENV_ALIASES = (
    ("ALPACA_LLM_ACCOUNT_ID", "ALPACA_LLM_API_KEY", "ALPACA_LLM_API_SECRET",
     "ALPACA_LLM_API_URL"),
    ("ALPACA_PAPER_ACCOUNT_ID", "ALPACA_PAPER_API_KEY", "ALPACA_PAPER_API_SECRET",
     "ALPACA_PAPER_API_URL"),
)


def _resolve_accounts() -> tuple[list[tuple[str, str, str, str]], list[str]]:
    """Every active Alpaca paper account, DB first, env as credential fallback.

    Returns (accounts, notes). A note is emitted for anything skipped, because
    an account silently dropped here is a position silently missing from a
    public book -- the exact failure this producer was built to end.

    A DB OUTAGE MUST NOT SHRINK THE BOOK -- AND MUST NOT PUBLISH ONE.
    An earlier version fell back to the two env accounts on DB failure. That
    reads as conservative and is the worst branch available: both env fetches
    SUCCEED, so `failed == 0`, so the book is rewritten, committed and PUSHED
    as a 13-position book -- silently retracting 27 real positions from a
    public record, with the only trace on stdout. That is the same class as the
    fetch failure this file already refuses to publish through, so it gets the
    same answer: raise, publish nothing, leave the book stale and let the
    heartbeat say ok=False. Stale-with-an-alert beats wrong-in-silence.
    It also keeps the file's "Scope: every active..." heading true, which the
    fallback made false for the duration of any outage.
    """
    accounts: list[tuple[str, str, str, str]] = []
    notes: list[str] = []
    seen: set[str] = set()

    env_creds: dict[str, tuple[str, str, str]] = {}
    for acct_env, key_env, sec_env, base_env in ENV_ALIASES:
        acct, k, s = os.getenv(acct_env), os.getenv(key_env), os.getenv(sec_env)
        if acct and k and s:
            env_creds[acct] = (k, s, os.getenv(base_env, PAPER_BASE))

    try:
        rows = _db_paper_accounts()
    except Exception as exc:
        # Truncated: a malformed PIM_PG_URL echoes the DSN back in the error,
        # and that would put a password in the PM2 log.
        raise RuntimeError(
            f"DB account lookup failed ({type(exc).__name__}: "
            f"{str(exc)[:120]}) -- refusing to publish a book built from a "
            f"partial account list") from exc

    db_accounts = {r[0] for r in rows}

    for acct, key, sec, base in rows:
        if acct in seen:
            continue
        if not (key and sec):
            key, sec, base = (*env_creds.get(acct, (None, None, base))[:2], base)
            if not (key and sec):
                notes.append(f"skipping {acct}: no credentials in DB or env")
                continue
        accounts.append((acct, key, sec, base or PAPER_BASE))
        seen.add(acct)

    for acct, (k, s, base) in env_creds.items():
        if acct in seen:
            continue
        if acct in db_accounts:
            continue  # unreachable: in db_accounts implies already in `seen`
        if _db_row_exists(acct):
            # PRESENT IN THE DB BUT EXCLUDED BY THE PREDICATE -- paused,
            # deactivated, or trading-disabled. Honour that. Including it
            # because an env alias happens to exist would make pausing an
            # account out of the book impossible, and would make the "Scope"
            # heading a superset of what it claims.
            notes.append(f"{acct}: in env but its DB row is paused/inactive "
                         f"-- excluded, matching the exit-watcher")
            continue
        notes.append(f"{acct}: in env with no DB row at all -- included")
        accounts.append((acct, k, s, base))
        seen.add(acct)
    return accounts, notes


def _db_row_exists(account_number: str) -> bool:
    """Is there ANY trading_accounts row for this number, predicate aside?

    Distinguishes "the DB deliberately excluded it" from "the DB has never
    heard of it". Only the second is a reason to trust an env alias.
    """
    import psycopg2
    try:
        with psycopg2.connect(PG_URL, connect_timeout=8) as conn:
            with conn.cursor() as c:
                c.execute("SELECT 1 FROM trading_accounts WHERE account_number=%s",
                          (account_number,))
                return c.fetchone() is not None
    except Exception:
        # Unknown is not "absent". If this cannot be answered, keep the account
        # rather than dropping it -- shrinking the book is the worse error.
        return False


def _db_paper_accounts() -> list[tuple[str, str, str, str]]:
    """Alpaca accounts the system considers live-for-trading, from the DB.

    Same predicate as services/exit-watcher/watcher.py:446-458 on purpose: the
    watcher managing a position that the book does not list is the divergence
    being removed, and two different account predicates would reintroduce it.
    """
    import psycopg2  # local import: a DB outage must not stop the module loading
    with psycopg2.connect(PG_URL, connect_timeout=8) as conn:
        with conn.cursor() as c:
            c.execute("""
                SELECT account_number,
                       credentials->>'api_key',
                       credentials->>'api_secret',
                       COALESCE(credentials->>'base_url', %s)
                FROM trading_accounts
                WHERE trading_provider = 'alpaca'
                  AND is_active = true
                  AND is_trading_enabled = true
                  AND paused = false
                ORDER BY id
            """, (PAPER_BASE,))
            return [tuple(r) for r in c.fetchall()]


def _run(hb: dict) -> int:
    """Do the work; record what happened into `hb` for the heartbeat.

    Split out of main() so that main() can write the heartbeat in a `finally`.
    Every return below is a return through that finally, including the paths
    that fail closed -- a heartbeat only written on success would leave the two
    silent failure modes ("no credentials" and "fetch failed") looking exactly
    like a job that was never scheduled, which is the defect being closed.
    """
    try:
        accounts, skipped = _resolve_accounts()
    except RuntimeError as exc:
        # A NAMED OUTCOME, not a traceback. This path is reachable on any DB
        # blip and it must land in the heartbeat as its own thing -- a crash
        # and "the DB was briefly unreachable" call for different responses,
        # and the checker cannot tell them apart from an mtime.
        print(f"  {exc}")
        hb.update(outcome="db-lookup-failed", ok=False, error=str(exc))
        return 1
    for note in skipped:
        print(f"  {note}")

    if not accounts:
        msg = ("no paper accounts resolvable -- refusing to rewrite the "
               "book as empty, because 'no credentials' is not 'no positions'")
        print(f"  {msg}")
        # This message matches NONE of pm2_log_triage.py's FLAG_PATTERNS, so
        # before the heartbeat existed this failure was invisible to every
        # monitor on the box. It is carried in the heartbeat's error field.
        hb.update(outcome="no-credentials", ok=False, error=msg)
        return 1

    rows, failed = [], 0
    per_account: dict[str, object] = {}
    for acct, k, s, base in accounts:
        if not L._is_paper(acct):
            print(f"  {acct}: NOT a paper account -- skipped")
            per_account[acct] = "non-paper-refused"
            continue
        got = alpaca_positions(acct, k, s, base)
        if got is None:
            failed += 1
            per_account[acct] = "fetch-failed"
            continue
        print(f"  {acct}: {len(got)} position(s)")
        per_account[acct] = len(got)
        rows.extend(got)
    hb["accounts"] = per_account

    # A FETCH FAILURE MUST NOT PUBLISH A FLAT BOOK. Writing "(no open positions)"
    # because an API call errored is the same class of bug as the file that was
    # never written: a confident public statement with nothing behind it.
    if failed:
        msg = f"{failed} account(s) failed to report -- NOT rewriting the book"
        print(f"  {msg}")
        hb.update(outcome="fetch-failed", ok=False, error=msg,
                  positions=len(rows))
        return 1

    changed = L.update_open_positions(rows, push=True)
    print(f"  {len(rows)} total position(s); file {'UPDATED' if changed else 'unchanged'}")
    # "unchanged" is a SUCCESSFUL run. Distinguishing it from "never ran" is the
    # entire reason this heartbeat exists: update_open_positions() skips the
    # write when content matches, so open-positions.md's mtime cannot tell them
    # apart and a week of flat markets looks identical to a week of downtime.
    hb.update(outcome="updated" if changed else "unchanged", ok=True,
              positions=len(rows))
    return 0


def main() -> int:
    started = datetime.now().astimezone()
    hb: dict = {"outcome": "crashed", "ok": False, "error": None,
                "positions": None, "accounts": {}}
    try:
        return _run(hb)
    except BaseException as exc:
        # An unhandled exception must still leave a heartbeat, or a crash looks
        # like a job that was never scheduled. Re-raised after recording.
        hb.update(outcome="crashed", ok=False,
                  error=f"{type(exc).__name__}: {exc}")
        raise
    finally:
        heartbeat.write(
            HEARTBEAT_NAME, cron=HEARTBEAT_CRON,
            grace_minutes=HEARTBEAT_GRACE_MIN, started=started,
            ok=hb["ok"], outcome=hb["outcome"], positions=hb["positions"],
            accounts=hb["accounts"], error=hb["error"])


if __name__ == "__main__":
    sys.exit(main())
