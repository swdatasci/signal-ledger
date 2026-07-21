"""Attach outcomes to open journal entries.

Walks journal/YYYY/MM/*.md looking for entries where outcome_r_multiple
is still blank, prompts for the outcome fields, rewrites the entry,
commits + pushes.

Usage:  cd ~/caelum/signal-ledger && uv run python journal/close.py
        # to close a specific entry:
        uv run python journal/close.py journal/2026/07/20260721-1447-XYZ-long.md
"""
from __future__ import annotations

import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
JOURNAL = REPO / "journal"


def unsettled_entries() -> list[Path]:
    out = []
    for md in sorted(JOURNAL.rglob("*.md")):
        if md.name in {"README.md", "TEMPLATE.md", "SETUP_TAXONOMY.md"}:
            continue
        text = md.read_text()
        if re.search(r"\*\*outcome_r_multiple:\*\*\s*$", text, re.MULTILINE):
            out.append(md)
    return out


def ask(p: str, default: str = "") -> str:
    s = f" [{default}]" if default else ""
    v = input(f"{p}{s}: ").strip()
    return v or default


def close_one(path: Path) -> bool:
    print(f"\n=== closing {path.relative_to(REPO)} ===")
    text = path.read_text()
    # Extract ticker for prompts
    tk = re.search(r"^ticker:\s*(\S+)", text, re.MULTILINE)
    ticker = tk.group(1) if tk else "?"
    print(f"ticker: {ticker}")

    r_mult = ask("outcome R-multiple (e.g. +2.3, -1.0, +0.5, 0)")
    fill_entry = ask("actual entry fill (blank if none — trade was cancelled)")
    fill_exit = ask("actual exit fill (blank if still open — abort close)")
    if not fill_exit:
        print("no exit fill given; aborting close for this entry")
        return False
    held_hours = ask("hours held (approx ok)")
    print("post-mortem (1-2 sentences; end with '.'):")
    lines = []
    while True:
        line = input()
        if line.strip() == ".":
            break
        lines.append(line)
    pm = "\n".join(lines).strip()
    if not pm:
        pm = "(none written)"

    replacements = {
        r"(\*\*outcome_r_multiple:\*\*)\s*$": rf"\1 {r_mult}",
        r"(\*\*fill_entry:\*\*)\s*$": rf"\1 {fill_entry}",
        r"(\*\*fill_exit:\*\*)\s*$": rf"\1 {fill_exit}",
        r"(\*\*held_hours:\*\*)\s*$": rf"\1 {held_hours}",
        r"(\*\*post_mortem:\*\*)\s*$": rf"\1 {pm}",
    }
    for pat, rep in replacements.items():
        text = re.sub(pat, rep, text, count=1, flags=re.MULTILINE)

    path.write_text(text)
    return True


def main(argv: list[str]) -> int:
    if len(argv) > 1:
        target = REPO / argv[1]
        if not target.exists():
            print(f"not found: {target}"); return 1
        candidates = [target]
    else:
        candidates = unsettled_entries()
        if not candidates:
            print("no unsettled entries")
            return 0
        print(f"{len(candidates)} unsettled entries:")
        for i, c in enumerate(candidates):
            print(f"  {i}: {c.relative_to(REPO)}")
        idx_raw = input("index to close (or 'all' to walk them): ").strip()
        if idx_raw == "all":
            pass
        else:
            try:
                candidates = [candidates[int(idx_raw)]]
            except (ValueError, IndexError):
                print("invalid index"); return 1

    updated: list[Path] = []
    for c in candidates:
        if close_one(c):
            updated.append(c)

    if not updated:
        print("nothing updated"); return 0

    rels = [str(u.relative_to(REPO)) for u in updated]
    msg = f"journal: close {len(updated)} entries"
    subprocess.run(["git", "add"] + rels, cwd=REPO, check=False)
    subprocess.run(["git", "commit", "-m", msg], cwd=REPO, check=False)
    subprocess.run(["git", "push"], cwd=REPO, check=False)
    print(f"\ncommitted + pushed close for {len(updated)} entries.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
