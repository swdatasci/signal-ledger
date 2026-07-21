# Signal Ledger — @sqwrell

Append-only. Every row is one event, most-recent-first.
Timestamps in UTC. All entries are **paper trades** unless explicitly flagged `[REAL CAPITAL]`.

Format: `YYYY-MM-DD HH:MM UTC | [strategy] | [action] | ticker | notes`

## Events

2026-07-21 19:55 UTC | llm-trader      | BUY      | TSLA   | conf=7 entry=377.4 stop=365.0 target=402.0
2026-07-21 19:55 UTC | llm-trader      | BUY      | AAPL   | conf=8 entry=327.71 stop=319.0 target=345.0
2026-07-20 02:07 UTC | setup           | INIT     | GO     | Ledger wired live. Congress×DPI z≥+2 and gov-contracts DoD $200M-$1B both running under pm2. Next event = first fresh signal from either strategy.
