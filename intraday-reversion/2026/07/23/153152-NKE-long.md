---
ticker: NKE
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% stop=1.5xM1
ts_utc: 2026-07-23T15:31:52+00:00
O: 41.71
M1_pct: 0.887
entry_ref: 41.229
target: 41.71
stop: 41.155
D1: up
---

## Signal — opening-reversion long on NKE

Initial move at open: **0.887%** in up direction from O=$41.71.

Price reverted past open by ~same magnitude — signal band reached at
$41.229. Entering long; target back to O
($41.71); stop at $41.155.

Backtest expectation for this config (N=30 m1=0.5% stop=1.5×M1 on 51 mega-caps):
- OOS 2023-2024: hit-rate ~90%, IR ~0.50, avg R +0.15

Not investment advice.
