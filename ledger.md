# Signal Ledger — @research_signal

Append-only. Every row is one event, most-recent-first.
Timestamps in UTC. All entries are **paper trades** unless explicitly flagged `[REAL CAPITAL]`.

Format: `YYYY-MM-DD HH:MM UTC | [strategy] | [action] | ticker | notes`

## Events

2026-07-24 14:24 UTC | llm-trader      | BUY      | AAPL   | conf=8 entry=328.0 stop=321.5 target=346.0
2026-07-23 15:49 UTC | intraday-reversion | BUY      | CMCSA  | O=23.29 entry=22.952 target=23.29 stop=22.9
2026-07-23 15:44 UTC | intraday-reversion | BUY      | CSCO   | O=113.14 entry=112.54 target=113.14 stop=112.0
2026-07-23 15:39 UTC | intraday-reversion | BUY      | UNP    | O=312.02 entry=307.36 target=312.02 stop=306.065
2026-07-23 15:39 UTC | intraday-reversion | BUY      | INTC   | O=102.25 entry=100.89 target=102.25 stop=100.0
2026-07-23 15:39 UTC | intraday-reversion | BUY      | CRM    | O=159.38 entry=156.585 target=159.38 stop=156.155
2026-07-23 15:38 UTC | intraday-reversion | BUY      | AMD    | O=551.72 entry=545.519 target=551.72 stop=544.565
2026-07-23 15:38 UTC | intraday-reversion | BUY      | ADBE   | O=215.81 entry=213.4 target=215.81 stop=211.565
2026-07-23 15:34 UTC | intraday-reversion | BUY      | BA     | O=209.11 entry=207.17 target=209.11 stop=205.9
2026-07-23 15:32 UTC | intraday-reversion | BUY      | ORCL   | O=122.16 entry=119.89 target=122.16 stop=118.35
2026-07-23 15:31 UTC | intraday-reversion | BUY      | NKE    | O=41.71 entry=41.229 target=41.71 stop=41.155
2026-07-23 15:31 UTC | intraday-reversion | BUY      | MSFT   | O=388.67 entry=384.627 target=388.67 stop=384.005
2026-07-23 15:27 UTC | intraday-reversion | BUY      | AVGO   | O=392.12 entry=388.04 target=392.12 stop=383.885
2026-07-23 15:25 UTC | intraday-reversion | BUY      | BLK    | O=1051.15 entry=1043.52 target=1051.15 stop=1035.73
2026-07-23 14:27 UTC | intraday-reversion | BUY      | META   | O=608.71 entry=604.51 target=608.71 stop=599.8
2026-07-23 14:25 UTC | llm-trader      | BUY      | META   | conf=5 entry=608.5 stop=592.3 target=647.1
2026-07-23 14:25 UTC | llm-trader      | BUY      | MSFT   | conf=6 entry=389.0 stop=375.6 target=412.0
2026-07-23 14:25 UTC | intraday-reversion | BUY      | WMT    | O=107.51 entry=106.83 target=107.51 stop=106.43
2026-07-23 14:10 UTC | intraday-reversion | BUY      | GOOGL  | O=321.13 entry=318.6 target=321.13 stop=316.09
2026-07-23 14:09 UTC | intraday-reversion | BUY      | NVDA   | O=209.46 entry=208.47 target=209.46 stop=207.345
2026-07-23 14:09 UTC | intraday-reversion | BUY      | AMZN   | O=236.37 entry=234.73 target=236.37 stop=233.4
2026-07-23 14:01 UTC | intraday-reversion | BUY      | UNH    | O=428.27 entry=425.8 target=428.27 stop=424.94
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
