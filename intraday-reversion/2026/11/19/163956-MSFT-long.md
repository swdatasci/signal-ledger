---
ticker: MSFT
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-11-19T16:39:56+00:00
O: 519.5
M1_pct: 1.346
entry_ref: 514.51
target: 519.5
trailing_amount: 27.96
D1: up
---

## Signal — opening-reversion long on MSFT

Initial move at open: **1.346%** in up direction from O=$519.5.

Price reverted past open by ~same magnitude — signal band reached at
$514.51. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($519.5). Trailing stop = HWM - $27.96.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
