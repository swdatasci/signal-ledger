"""Interactive pre-trade journal entry.

Fills a markdown template from prompts, writes it under
journal/YYYY/MM/, commits + pushes.  Under 60 seconds to fill if you
know the answers.

Usage:  cd ~/caelum/signal-ledger && uv run python journal/new.py
"""
from __future__ import annotations

import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
JOURNAL = REPO / "journal"


def ask(prompt: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    val = input(f"{prompt}{suffix}: ").strip()
    return val or default


def ask_int(prompt: str, lo: int, hi: int) -> int:
    while True:
        raw = input(f"{prompt} ({lo}-{hi}): ").strip()
        try:
            n = int(raw)
        except ValueError:
            print(f"  not an integer, try again")
            continue
        if not (lo <= n <= hi):
            print(f"  out of range {lo}-{hi}, try again")
            continue
        return n


def ask_multiline(prompt: str, min_chars: int = 20) -> str:
    print(f"{prompt} (end with a single '.' on a line):")
    lines: list[str] = []
    while True:
        line = input()
        if line.strip() == ".":
            break
        lines.append(line)
    body = "\n".join(lines).strip()
    if len(body) < min_chars:
        print(f"  too short ({len(body)} < {min_chars}); rewriting.")
        return ask_multiline(prompt, min_chars)
    return body


def main() -> int:
    print("=== pre-trade journal entry ===")
    print("all fields git-committed BEFORE you place the broker order.")
    print()

    ticker = ask("ticker").upper()
    if not ticker:
        print("ticker required, abort"); return 1

    direction = ask("direction (long/short)", "long").lower()
    if direction not in {"long", "short"}:
        print("direction must be long or short, abort"); return 1

    broker = ask("broker (fidelity/alpaca-paper/tradestation/tastytrade)", "fidelity")
    entry_ref = ask("entry_ref (planned price now)")
    stop = ask("stop price")
    target = ask("target price (blank = none)")
    r_risked = ask("r_risked $ (dollar loss if stop hits)")

    gut = ask_int("gut confidence", 1, 10)
    setup = ask("setup slug (see SETUP_TAXONOMY.md; use 'new:<slug>' to add)")
    emotional_state = ask("emotional state (calm/anxious/fomo/revenge/tired/curious)", "calm")
    discovery_source = ask("discovery source (fidelity-scan/hot-list/news/friend/learning/curiosity)", "fidelity-scan")

    thesis = ask_multiline("pre-trade thesis (2-4 sentences, specific FEATURES not desired outcome)", min_chars=30)
    warning = ask_multiline("ignored warning voice (or type 'none' then .)", min_chars=4)
    alternatives = ask_multiline("alternatives dismissed (why not the other read?)", min_chars=10)
    exit_plan = ask_multiline("exit plan (why this stop/target, R:R, time stop if any)", min_chars=15)

    now = datetime.now(timezone.utc)
    stamp = now.strftime("%Y%m%d-%H%M%S")
    year = now.strftime("%Y")
    month = now.strftime("%m")

    out_dir = JOURNAL / year / month
    out_dir.mkdir(parents=True, exist_ok=True)
    fname = f"{stamp}-{ticker}-{direction}.md"
    path = out_dir / fname

    if setup.startswith("new:"):
        new_slug = setup[4:].strip()
        setup = new_slug
        print(f"NOTE: remember to add '{new_slug}' to SETUP_TAXONOMY.md")

    content = f"""---
ticker: {ticker}
direction: {direction}
broker: {broker}
entry_ref: {entry_ref}
r_risked_usd: {r_risked}
stop: {stop}
target: {target}
gut_confidence: {gut}
setup: {setup}
emotional_state: {emotional_state}
discovery_source: {discovery_source}
utc_written: {now.isoformat(timespec="seconds")}
---

## Pre-trade thesis

{thesis}

## Ignored warning voice

{warning}

## Alternatives dismissed

{alternatives}

## Exit plan

{exit_plan}

---

_populated after outcome via `close.py`:_

- **outcome_r_multiple:**
- **fill_entry:**
- **fill_exit:**
- **held_hours:**
- **post_mortem:**
"""
    path.write_text(content)
    print(f"\nwrote {path.relative_to(REPO)}")

    rel = str(path.relative_to(REPO))
    msg = f"journal: {ticker} {direction} @ {stamp} (gut={gut}, r=${r_risked})"
    r1 = subprocess.run(["git", "add", rel], cwd=REPO)
    r2 = subprocess.run(["git", "commit", "-m", msg], cwd=REPO)
    r3 = subprocess.run(["git", "push"], cwd=REPO)
    if r1.returncode or r2.returncode or r3.returncode:
        print("!! git add/commit/push had a nonzero exit — check status manually")
        return 2
    print("\ncommitted + pushed. broker order can go in now.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
