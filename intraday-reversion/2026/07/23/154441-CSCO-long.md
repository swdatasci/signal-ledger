---
ticker: CSCO
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% stop=1.5xM1
ts_utc: 2026-07-23T15:44:41+00:00
O: 113.14
M1_pct: 0.672
entry_ref: 112.54
target: 113.14
stop: 112.0
D1: up
---

## Signal — opening-reversion long on CSCO

Initial move at open: **0.672%** in up direction from O=$113.14.

Price reverted past open by ~same magnitude — signal band reached at
$112.54. Entering long; target back to O
($113.14); stop at $112.0.

Backtest expectation for this config (N=30 m1=0.5% stop=1.5×M1 on 51 mega-caps):
- OOS 2023-2024: hit-rate ~90%, IR ~0.50, avg R +0.15

Not investment advice.
