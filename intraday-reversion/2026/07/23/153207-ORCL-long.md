---
ticker: ORCL
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% stop=1.5xM1
ts_utc: 2026-07-23T15:32:07+00:00
O: 122.16
M1_pct: 2.079
entry_ref: 119.89
target: 122.16
stop: 118.35
D1: up
---

## Signal — opening-reversion long on ORCL

Initial move at open: **2.079%** in up direction from O=$122.16.

Price reverted past open by ~same magnitude — signal band reached at
$119.89. Entering long; target back to O
($122.16); stop at $118.35.

Backtest expectation for this config (N=30 m1=0.5% stop=1.5×M1 on 51 mega-caps):
- OOS 2023-2024: hit-rate ~90%, IR ~0.50, avg R +0.15

Not investment advice.
