---
ticker: CMCSA
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% stop=1.5xM1
ts_utc: 2026-07-23T15:49:50+00:00
O: 23.29
M1_pct: 1.116
entry_ref: 22.952
target: 23.29
stop: 22.9
D1: up
---

## Signal — opening-reversion long on CMCSA

Initial move at open: **1.116%** in up direction from O=$23.29.

Price reverted past open by ~same magnitude — signal band reached at
$22.952. Entering long; target back to O
($23.29); stop at $22.9.

Backtest expectation for this config (N=30 m1=0.5% stop=1.5×M1 on 51 mega-caps):
- OOS 2023-2024: hit-rate ~90%, IR ~0.50, avg R +0.15

Not investment advice.
