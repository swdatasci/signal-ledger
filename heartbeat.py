"""Liveness heartbeat for scheduled jobs in this repo.

WHY THIS EXISTS. `update_open_positions()` deliberately skips the write when
the rendered book is byte-identical ignoring the "Last updated:" line, so the
repo does not take a commit every 30 minutes. That is correct git hygiene and
it is also the reason open-positions.md's mtime is NOT a liveness signal: a
job that died on 2026-08-01 and a book that genuinely has not changed since
2026-08-01 produce the same file with the same timestamp. Nothing on disk
distinguished them.

The other two things that might have noticed also cannot:
  - pm2-log-triage scans ~/.pm2/logs for error lines. A job that stops FIRING
    emits no lines, so there is nothing to scan. It catches a failing run and
    is structurally blind to an absent one.
  - refresh_open_positions.py prints failures to stdout, and "no paper
    accounts resolvable from env" matches none of triage's FLAG_PATTERNS.

So: an artifact written on EVERY run, whatever the outcome, whose freshness is
checked by a separate process. Unconditional is the whole point -- a heartbeat
emitted only on success makes "dead" and "quiet" identical again, which is the
bug we are fixing.

NOT IN THE GIT REPO. signal-ledger is public and a heartbeat is operational
noise with account ids in it. It goes to ~/.cache/heartbeats/, matching the
convention already established by ~/.cache/pm2_log_triage_state.json.

SELF-DESCRIBING SCHEDULE. The file carries its own `cron` and `grace_minutes`
so the checker needs no per-job knowledge. `*/30 6-14 * * 1-5` means a Saturday
gap is not staleness; a checker that hardcoded "older than 30 minutes" would
page every weekend and every night. The schedule travels with the heartbeat
because the job is the only thing that knows it.
"""
from __future__ import annotations

import json
import os
import socket
from datetime import datetime
from pathlib import Path

HEARTBEAT_DIR = Path(os.environ.get(
    "HEARTBEAT_DIR", str(Path.home() / ".cache" / "heartbeats")))


def write(name: str, *, cron: str, grace_minutes: int, ok: bool,
          outcome: str, positions: int | None = None,
          accounts: dict | None = None, error: str | None = None,
          started: datetime | None = None) -> Path | None:
    """Write one heartbeat. Never raises.

    Never raises because this is called from a `finally` -- a heartbeat write
    that threw would mask the real exception it was trying to record, turning
    an observable failure into a confusing one.

    Written atomically (tmp + rename). A checker reading a half-written file
    would report "missing" and page for a job that is in fact alive; a guard
    that cries wolf gets muted, and a muted guard is worse than none.
    """
    try:
        now = datetime.now().astimezone()
        payload = {
            "name": name,
            "cron": cron,
            "grace_minutes": int(grace_minutes),
            "ts": now.isoformat(timespec="seconds"),
            "ts_epoch": now.timestamp(),
            "ok": bool(ok),
            "outcome": outcome,
            "positions": positions,
            "accounts": accounts or {},
            "error": (str(error)[:400] if error else None),
            "pid": os.getpid(),
            "host": socket.gethostname(),
            "duration_s": (round((now - started).total_seconds(), 2)
                           if started else None),
        }
        HEARTBEAT_DIR.mkdir(parents=True, exist_ok=True)
        path = HEARTBEAT_DIR / f"{name}.json"
        tmp = path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        os.replace(tmp, path)
        return path
    except Exception as exc:          # pragma: no cover - defensive
        print(f"[heartbeat] write failed ({type(exc).__name__}: {exc}) -- "
              f"the job itself is unaffected, but liveness is now unobservable")
        return None
