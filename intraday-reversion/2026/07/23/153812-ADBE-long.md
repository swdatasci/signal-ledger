---
ticker: ADBE
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% stop=1.5xM1
ts_utc: 2026-07-23T15:38:12+00:00
O: 215.81
M1_pct: 1.311
entry_ref: 213.4
target: 215.81
stop: 211.565
D1: up
---

## Signal — opening-reversion long on ADBE

Initial move at open: **1.311%** in up direction from O=$215.81.

Price reverted past open by ~same magnitude — signal band reached at
$213.4. Entering long; target back to O
($215.81); stop at $211.565.

Backtest expectation for this config (N=30 m1=0.5% stop=1.5×M1 on 51 mega-caps):
- OOS 2023-2024: hit-rate ~90%, IR ~0.50, avg R +0.15

Not investment advice.
