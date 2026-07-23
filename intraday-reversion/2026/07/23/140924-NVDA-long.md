---
ticker: NVDA
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% stop=1.5xM1
ts_utc: 2026-07-23T14:09:24+00:00
O: 209.46
M1_pct: 0.673
entry_ref: 208.47
target: 209.46
stop: 207.345
D1: up
---

## Signal — opening-reversion long on NVDA

Initial move at open: **0.673%** in up direction from O=$209.46.

Price reverted past open by ~same magnitude — signal band reached at
$208.47. Entering long; target back to O
($209.46); stop at $207.345.

Backtest expectation for this config (N=30 m1=0.5% stop=1.5×M1 on 51 mega-caps):
- OOS 2023-2024: hit-rate ~90%, IR ~0.50, avg R +0.15

Not investment advice.
