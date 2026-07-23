---
ticker: AVGO
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% stop=1.5xM1
ts_utc: 2026-07-23T15:27:06+00:00
O: 392.12
M1_pct: 1.4
entry_ref: 388.04
target: 392.12
stop: 383.885
D1: up
---

## Signal — opening-reversion long on AVGO

Initial move at open: **1.4%** in up direction from O=$392.12.

Price reverted past open by ~same magnitude — signal band reached at
$388.04. Entering long; target back to O
($392.12); stop at $383.885.

Backtest expectation for this config (N=30 m1=0.5% stop=1.5×M1 on 51 mega-caps):
- OOS 2023-2024: hit-rate ~90%, IR ~0.50, avg R +0.15

Not investment advice.
