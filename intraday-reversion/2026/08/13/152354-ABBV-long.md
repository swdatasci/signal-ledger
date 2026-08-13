---
ticker: ABBV
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-13T15:23:54+00:00
O: 252.94
M1_pct: 0.933
entry_ref: 250.97
target: 252.94
trailing_amount: 9.44
D1: up
---

## Signal — opening-reversion long on ABBV

Initial move at open: **0.933%** in up direction from O=$252.94.

Price reverted past open by ~same magnitude — signal band reached at
$250.97. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($252.94). Trailing stop = HWM - $9.44.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
