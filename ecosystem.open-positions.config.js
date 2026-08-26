// Keep open-positions.md current. PM2 cron_restart, never system cron.
//
// Every 30 min, 06:00-14:30 MST weekdays = 09:00-17:30 ET, so it spans the
// pre-open, the session and the close. The box is America/Phoenix (no DST), so
// this drifts one hour against the session between seasons; that is acceptable
// here because the job only READS and republishes -- unlike a collector, a
// mistimed run costs nothing.
//
// WHY SCHEDULED RATHER THAN HOOKED INTO record(). README.md says the book is
// "regenerated after every signal event", which would mean calling this from
// ledger_writer.record(). record() runs inside the traders' hot path, and a
// broker round-trip there would put a bookkeeping call between a signal and its
// order. A stale-by-30-minutes book is a smaller problem than a trader that
// blocks on a positions endpoint.
//
// The script fails CLOSED: a fetch error or missing credentials exits non-zero
// WITHOUT rewriting the file, because "no credentials" is not "no positions"
// and publishing a flat book off an API error is the same defect as the file
// that was never written at all.
//
// LIVENESS. This job had none and could not have had one from the file it
// writes: update_open_positions() skips the write when content is unchanged,
// so open-positions.md's mtime says nothing about whether the job still runs.
// Every run now drops ~/.cache/heartbeats/signal-ledger-open-positions.json
// (see heartbeat.py) carrying the cron above, and pm2-log-triage checks its
// age against the most recent slot this cron should have fired -- so a weekend
// is not staleness and a dead Monday is caught by 07:xx. If this cron string
// changes, HEARTBEAT_CRON in refresh_open_positions.py must change with it or
// the checker will page on a schedule the job no longer keeps.
//
//   pm2 start ecosystem.open-positions.config.js && pm2 save
module.exports = {
  apps: [{
    name: "signal-ledger-open-positions",
    script: "/home/rford/.venv/bin/python",
    args: "refresh_open_positions.py",
    cwd: "/home/rford/caelum/signal-ledger",
    autorestart: false,
    cron_restart: "*/30 6-14 * * 1-5",
    time: true,
  }],
};
