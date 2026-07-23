---
ticker: MSFT
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% stop=1.5xM1
ts_utc: 2026-07-23T15:30:53+00:00
O: 388.67
M1_pct: 0.8
entry_ref: 384.627
target: 388.67
stop: 384.005
D1: up
---

## Signal — opening-reversion long on MSFT

Initial move at open: **0.8%** in up direction from O=$388.67.

Price reverted past open by ~same magnitude — signal band reached at
$384.627. Entering long; target back to O
($388.67); stop at $384.005.

Backtest expectation for this config (N=30 m1=0.5% stop=1.5×M1 on 51 mega-caps):
- OOS 2023-2024: hit-rate ~90%, IR ~0.50, avg R +0.15

Not investment advice.
