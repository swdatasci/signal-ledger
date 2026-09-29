---
ticker: ABBV
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-09-29T14:30:21+00:00
O: 265.45
M1_pct: 1.311
entry_ref: 262.89
target: 265.45
trailing_amount: 13.92
D1: up
---

## Signal — opening-reversion long on ABBV

Initial move at open: **1.311%** in up direction from O=$265.45.

Price reverted past open by ~same magnitude — signal band reached at
$262.89. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($265.45). Trailing stop = HWM - $13.92.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
