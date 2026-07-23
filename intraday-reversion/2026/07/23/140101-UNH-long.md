---
ticker: UNH
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% stop=1.5xM1
ts_utc: 2026-07-23T14:01:01+00:00
O: 428.27
M1_pct: 0.518
entry_ref: 425.8
target: 428.27
stop: 424.94
D1: up
---

## Signal — opening-reversion long on UNH

Initial move at open: **0.518%** in up direction from O=$428.27.

Price reverted past open by ~same magnitude — signal band reached at
$425.8. Entering long; target back to O
($428.27); stop at $424.94.

Backtest expectation for this config (N=30 m1=0.5% stop=1.5×M1 on 51 mega-caps):
- OOS 2023-2024: hit-rate ~90%, IR ~0.50, avg R +0.15

Not investment advice.
