---
ticker: WMT
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% stop=1.5xM1
ts_utc: 2026-07-23T14:21:37+00:00
O: 107.51
M1_pct: 0.67
entry_ref: 106.84
target: 107.51
stop: 106.43
D1: up
---

## Signal — opening-reversion long on WMT

Initial move at open: **0.67%** in up direction from O=$107.51.

Price reverted past open by ~same magnitude — signal band reached at
$106.84. Entering long; target back to O
($107.51); stop at $106.43.

Backtest expectation for this config (N=30 m1=0.5% stop=1.5×M1 on 51 mega-caps):
- OOS 2023-2024: hit-rate ~90%, IR ~0.50, avg R +0.15

Not investment advice.
