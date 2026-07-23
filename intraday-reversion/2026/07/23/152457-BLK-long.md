---
ticker: BLK
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% stop=1.5xM1
ts_utc: 2026-07-23T15:24:57+00:00
O: 1051.15
M1_pct: 0.978
entry_ref: 1043.52
target: 1051.15
stop: 1035.73
D1: up
---

## Signal — opening-reversion long on BLK

Initial move at open: **0.978%** in up direction from O=$1051.15.

Price reverted past open by ~same magnitude — signal band reached at
$1043.52. Entering long; target back to O
($1051.15); stop at $1035.73.

Backtest expectation for this config (N=30 m1=0.5% stop=1.5×M1 on 51 mega-caps):
- OOS 2023-2024: hit-rate ~90%, IR ~0.50, avg R +0.15

Not investment advice.
