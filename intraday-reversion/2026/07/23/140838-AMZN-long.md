---
ticker: AMZN
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% stop=1.5xM1
ts_utc: 2026-07-23T14:08:38+00:00
O: 236.37
M1_pct: 0.838
entry_ref: 234.73
target: 236.37
stop: 233.4
D1: up
---

## Signal — opening-reversion long on AMZN

Initial move at open: **0.838%** in up direction from O=$236.37.

Price reverted past open by ~same magnitude — signal band reached at
$234.73. Entering long; target back to O
($236.37); stop at $233.4.

Backtest expectation for this config (N=30 m1=0.5% stop=1.5×M1 on 51 mega-caps):
- OOS 2023-2024: hit-rate ~90%, IR ~0.50, avg R +0.15

Not investment advice.
