---
ticker: META
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% stop=1.5xM1
ts_utc: 2026-07-23T14:26:41+00:00
O: 608.71
M1_pct: 0.976
entry_ref: 604.51
target: 608.71
stop: 599.8
D1: up
---

## Signal — opening-reversion long on META

Initial move at open: **0.976%** in up direction from O=$608.71.

Price reverted past open by ~same magnitude — signal band reached at
$604.51. Entering long; target back to O
($608.71); stop at $599.8.

Backtest expectation for this config (N=30 m1=0.5% stop=1.5×M1 on 51 mega-caps):
- OOS 2023-2024: hit-rate ~90%, IR ~0.50, avg R +0.15

Not investment advice.
