---
ticker: CRM
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% stop=1.5xM1
ts_utc: 2026-07-23T15:38:57+00:00
O: 159.38
M1_pct: 1.349
entry_ref: 156.585
target: 159.38
stop: 156.155
D1: up
---

## Signal — opening-reversion long on CRM

Initial move at open: **1.349%** in up direction from O=$159.38.

Price reverted past open by ~same magnitude — signal band reached at
$156.585. Entering long; target back to O
($159.38); stop at $156.155.

Backtest expectation for this config (N=30 m1=0.5% stop=1.5×M1 on 51 mega-caps):
- OOS 2023-2024: hit-rate ~90%, IR ~0.50, avg R +0.15

Not investment advice.
