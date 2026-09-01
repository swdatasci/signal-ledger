#!/usr/bin/env python3
"""Publish CLOSED round trips to the public ledger.

The ledger held 208 BUY rows and zero exits. Every executor calls
ledger_writer.record(action="BUY") when it opens a position, and nothing ever
records the close — because the close is a broker-side event. Both strategies
protect positions with GTC bracket legs, so a target or stop fills at the
exchange with no process of ours running. There was no code path to hook.

So exits are published from the reconcilers' output instead, which is the only
place a fill becomes observable to us. Each strategy's reconcile_outcomes.py
writes parsed/outcomes.csv from the BROKER's own order history; this reads those
and appends anything not already on the ledger.

Consequence worth stating plainly: until this ran, the public ledger could show
what was bought and never what it did. A reader could not compute a win rate, a
return, or a hold time from it, and the repo README's "every entry, fill, and
exit is recorded" was true only of entries.

  --dry-run   print what would be appended, write nothing
  --limit N   publish at most N (default: all unpublished)
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEDGER_FILE = HERE / "ledger.md"

# {ledger strategy tag: outcomes.csv}. The tag must match what that strategy's
# executor already writes on BUY, or entries and exits will not line up for a
# reader pairing them by eye.
SOURCES = {
    "llm-trader": Path("/home/rford/caelum/data-feeds/llm-trader/parsed/outcomes.csv"),
    "intraday-reversion":
        Path("/home/rford/caelum/data-feeds/intraday-reversion/parsed/outcomes.csv"),
}


def already_published() -> set[tuple[str, str]]:
    """{(strategy, exit_order_id)} already on the ledger.

    Keyed on the broker's exit order id, carried in the notes as `xid=`. A
    timestamp key would republish on any reconcile rerun, and the ledger is
    append-only — a duplicate cannot be taken back.
    """
    if not LEDGER_FILE.exists():
        return set()
    out = set()
    for line in LEDGER_FILE.read_text().splitlines():
        m = re.search(r"\|\s*(\S+)\s*\|\s*(?:SELL|STOP|TP)\s*\|.*?xid=([^\s|]+)", line)
        if m:
            out.add((m.group(1), m.group(2)))
    return out


# The reconcilers' vocabulary, mapped to the ledger's. `market` is a plain
# close, not a stop-out and not a target — publishing it as either would
# misreport why a trade ended, which is the field a reader judges the strategy
# on.
ACTION = {"target": "TP", "stop": "STOP", "market": "SELL", "market_exit": "SELL"}


def load(strategy: str, path: Path) -> list[dict]:
    if not path.exists():
        print(f"  {strategy}: no outcomes at {path} — skipped")
        return []
    rows = []
    with path.open() as fh:
        for r in csv.DictReader(fh):
            # Execution noise is a real fill but not a decision: sub-minute
            # round trips at spread-sized losses, 28 of llm-trader's 129. On a
            # PUBLIC ledger they would read as trades the strategy chose.
            if r.get("execution_noise") == "1":
                continue
            if not r.get("exit_order_id") or not r.get("realized_pct"):
                continue
            rows.append({**r, "_strategy": strategy})
    return rows


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    seen = already_published()
    print(f"exits already on the ledger: {len(seen)}")

    fresh = []
    for strat, path in SOURCES.items():
        rows = load(strat, path)
        new = [r for r in rows if (strat, str(r["exit_order_id"])) not in seen]
        print(f"  {strat:20} {len(rows):>4} closed, {len(new):>4} unpublished")
        fresh += new

    fresh.sort(key=lambda r: r.get("exit_ts_et") or "")
    if args.limit:
        fresh = fresh[:args.limit]
    if not fresh:
        print("nothing to publish")
        return 0

    print(f"\npublishing {len(fresh)} exit(s){' (DRY RUN)' if args.dry_run else ''}:")
    if not args.dry_run:
        sys.path.insert(0, str(HERE))
        import ledger_writer  # noqa: PLC0415

    for i, r in enumerate(fresh):
        pct = float(r["realized_pct"])
        action = ACTION.get((r.get("exit_reason") or "").lower(), "SELL")
        notes = (f"{pct:+.2f}% in {float(r['held_hours']):.1f}h "
                 f"entry={r['entry_price']} exit={r['exit_price']} "
                 f"reason={r.get('exit_reason')} xid={r['exit_order_id']}")
        print(f"  {r['exit_ts_et'][:19]} {r['_strategy']:20} {action:5} "
              f"{r['ticker']:6} {pct:+7.2f}%")
        if args.dry_run:
            continue
        # push=False: this is a BACKFILL of closes the broker made days ago, and
        # ledger_writer notifies on every BUY/SELL. Firing ~100 Pushovers for
        # history would burn the operator's monthly quota to say nothing new.
        # flush once at the end rather than committing per row.
        ledger_writer.record(r["_strategy"], action, r["ticker"], notes,
                             flush_now=False, push=False)
    if not args.dry_run:
        ledger_writer.flush()
        print(f"\nappended {len(fresh)} exit(s) to {LEDGER_FILE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
