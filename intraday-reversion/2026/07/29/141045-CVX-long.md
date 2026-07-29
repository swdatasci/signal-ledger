---
ticker: CVX
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-07-29T14:10:45+00:00
O: 192.5
M1_pct: 0.551
entry_ref: 191.6
target: 192.5
trailing_amount: 4.24
D1: up
---

## Signal — opening-reversion long on CVX

Initial move at open: **0.551%** in up direction from O=$192.5.

Price reverted past open by ~same magnitude — signal band reached at
$191.6. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($192.5). Trailing stop = HWM - $4.24.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
