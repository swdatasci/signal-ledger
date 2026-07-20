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
from datetime import datetime, timezone
from pathlib import Path

LEDGER_ROOT = Path("/home/rford/caelum/signal-ledger")
LEDGER_FILE = LEDGER_ROOT / "ledger.md"

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


def record(strategy: str, action: str, ticker: str, notes: str = "",
           *, flush_now: bool = True) -> None:
    """Append one event to the ledger.

    - strategy: short strategy tag ("gov-contracts", "congress-dpi")
    - action: SIGNAL | BUY | SELL | STOP | TP | SKIP | ERROR
    - ticker: uppercase symbol
    - notes: freeform, single-line context
    - flush_now: commit + push immediately. Set False when appending many
      rows in a burst; call flush() once at the end.
    """
    ts = _now_utc()
    line = f"{ts} | {strategy:15s} | {action:8s} | {ticker:6s} | {notes}"
    _buffer.append(line)
    if flush_now:
        flush()


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
