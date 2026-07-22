# Signal Ledger — @sqwrell

Append-only. Every row is one event, most-recent-first.
Timestamps in UTC. All entries are **paper trades** unless explicitly flagged `[REAL CAPITAL]`.

Format: `YYYY-MM-DD HH:MM UTC | [strategy] | [action] | ticker | notes`

## Events

2026-07-22 19:22 UTC | llm-trader      | BUY      | MRVL   | conf=6 entry=213.08 stop=207.68 target=225.49
2026-07-22 19:21 UTC | llm-trader      | BUY      | AMD    | conf=7 entry=561.07 stop=548.29 target=593.17
2026-07-22 17:13 UTC | llm-trader      | BUY      | AMT    | conf=7 entry=166.035 stop=162.0 target=184.0
2026-07-22 17:13 UTC | llm-trader      | BUY      | ADI    | conf=6 entry=387.49 stop=375.0 target=416.0
2026-07-22 17:12 UTC | llm-trader      | BUY      | AMAT   | conf=7 entry=560.05 stop=542.0 target=593.0
2026-07-22 16:08 UTC | llm-trader      | BUY      | AVGO   | conf=6 entry=393.0 stop=375.0 target=462.0
2026-07-22 16:08 UTC | llm-trader      | BUY      | MRVL   | conf=7 entry=214.0 stop=200.58 target=273.69
2026-07-22 16:07 UTC | llm-trader      | BUY      | AMD    | conf=7 entry=548.0 stop=526.0 target=617.0
2026-07-21 19:55 UTC | llm-trader      | BUY      | TSLA   | conf=7 entry=377.4 stop=365.0 target=402.0
2026-07-21 19:55 UTC | llm-trader      | BUY      | AAPL   | conf=8 entry=327.71 stop=319.0 target=345.0
2026-07-20 02:07 UTC | setup           | INIT     | GO     | Ledger wired live. Congress×DPI z≥+2 and gov-contracts DoD $200M-$1B both running under pm2. Next event = first fresh signal from either strategy.
