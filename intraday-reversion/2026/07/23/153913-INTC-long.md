---
ticker: INTC
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% stop=1.5xM1
ts_utc: 2026-07-23T15:39:13+00:00
O: 102.25
M1_pct: 1.467
entry_ref: 100.89
target: 102.25
stop: 100.0
D1: up
---

## Signal — opening-reversion long on INTC

Initial move at open: **1.467%** in up direction from O=$102.25.

Price reverted past open by ~same magnitude — signal band reached at
$100.89. Entering long; target back to O
($102.25); stop at $100.0.

Backtest expectation for this config (N=30 m1=0.5% stop=1.5×M1 on 51 mega-caps):
- OOS 2023-2024: hit-rate ~90%, IR ~0.50, avg R +0.15

Not investment advice.
