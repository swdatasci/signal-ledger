---
ticker: GOOGL
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% stop=1.5xM1
ts_utc: 2026-07-23T14:10:48+00:00
O: 321.13
M1_pct: 1.046
entry_ref: 318.6
target: 321.13
stop: 316.09
D1: up
---

## Signal — opening-reversion long on GOOGL

Initial move at open: **1.046%** in up direction from O=$321.13.

Price reverted past open by ~same magnitude — signal band reached at
$318.6. Entering long; target back to O
($321.13); stop at $316.09.

Backtest expectation for this config (N=30 m1=0.5% stop=1.5×M1 on 51 mega-caps):
- OOS 2023-2024: hit-rate ~90%, IR ~0.50, avg R +0.15

Not investment advice.
