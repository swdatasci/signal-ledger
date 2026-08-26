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


def _run(hb: dict) -> int:
    """Do the work; record what happened into `hb` for the heartbeat.

    Split out of main() so that main() can write the heartbeat in a `finally`.
    Every return below is a return through that finally, including the paths
    that fail closed -- a heartbeat only written on success would leave the two
    silent failure modes ("no credentials" and "fetch failed") looking exactly
    like a job that was never scheduled, which is the defect being closed.
    """
    accounts = []
    for label_env, key_env, sec_env, base_env in (
        ("ALPACA_LLM_ACCOUNT_ID", "ALPACA_LLM_API_KEY", "ALPACA_LLM_API_SECRET",
         "ALPACA_LLM_API_URL"),
        ("ALPACA_PAPER_ACCOUNT_ID", "ALPACA_PAPER_API_KEY", "ALPACA_PAPER_API_SECRET",
         "ALPACA_PAPER_API_URL"),
    ):
        acct, k, s = os.getenv(label_env), os.getenv(key_env), os.getenv(sec_env)
        base = os.getenv(base_env, "https://paper-api.alpaca.markets")
        if acct and k and s:
            accounts.append((acct, k, s, base))
        else:
            missing = [n for n, v in ((label_env, acct), (key_env, k), (sec_env, s)) if not v]
            print(f"  skipping {label_env}: missing {missing}")

    if not accounts:
        msg = ("no paper accounts resolvable from env -- refusing to rewrite the "
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
