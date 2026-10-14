---
ticker: GOOGL
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-10-14T14:23:06+00:00
O: 355.8
M1_pct: 1.012
entry_ref: 353.95
target: 355.8
trailing_amount: 14.4
D1: up
---

## Signal — opening-reversion long on GOOGL

Initial move at open: **1.012%** in up direction from O=$355.8.

Price reverted past open by ~same magnitude — signal band reached at
$353.95. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($355.8). Trailing stop = HWM - $14.4.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
