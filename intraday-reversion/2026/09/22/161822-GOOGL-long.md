---
ticker: GOOGL
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-09-22T16:18:22+00:00
O: 357.75
M1_pct: 1.795
entry_ref: 353.3
target: 357.75
trailing_amount: 25.68
D1: up
---

## Signal — opening-reversion long on GOOGL

Initial move at open: **1.795%** in up direction from O=$357.75.

Price reverted past open by ~same magnitude — signal band reached at
$353.3. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($357.75). Trailing stop = HWM - $25.68.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
