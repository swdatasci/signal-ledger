---
ticker: NVDA
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-20T14:07:41+00:00
O: 218.39
M1_pct: 0.673
entry_ref: 217.57
target: 218.39
trailing_amount: 5.88
D1: up
---

## Signal — opening-reversion long on NVDA

Initial move at open: **0.673%** in up direction from O=$218.39.

Price reverted past open by ~same magnitude — signal band reached at
$217.57. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($218.39). Trailing stop = HWM - $5.88.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
