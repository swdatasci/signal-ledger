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
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ledger_writer as L  # noqa: E402

ALPACA = os.getenv("ALPACA_WRAPPER_URL", "http://10.32.3.27:8101")
TS = os.getenv("TS_WRAPPER_URL", "http://10.32.3.27:8102")


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


def main() -> int:
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
        print("  no paper accounts resolvable from env -- refusing to rewrite the "
              "book as empty, because 'no credentials' is not 'no positions'")
        return 1

    rows, failed = [], 0
    for acct, k, s, base in accounts:
        if not L._is_paper(acct):
            print(f"  {acct}: NOT a paper account -- skipped")
            continue
        got = alpaca_positions(acct, k, s, base)
        if got is None:
            failed += 1
            continue
        print(f"  {acct}: {len(got)} position(s)")
        rows.extend(got)

    # A FETCH FAILURE MUST NOT PUBLISH A FLAT BOOK. Writing "(no open positions)"
    # because an API call errored is the same class of bug as the file that was
    # never written: a confident public statement with nothing behind it.
    if failed:
        print(f"  {failed} account(s) failed to report -- NOT rewriting the book")
        return 1

    changed = L.update_open_positions(rows, push=True)
    print(f"  {len(rows)} total position(s); file {'UPDATED' if changed else 'unchanged'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
