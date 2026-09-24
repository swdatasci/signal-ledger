---
ticker: XOM
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-09-24T16:20:38+00:00
O: 163.09
M1_pct: 0.656
entry_ref: 162.61
target: 163.09
trailing_amount: 4.28
D1: up
---

## Signal — opening-reversion long on XOM

Initial move at open: **0.656%** in up direction from O=$163.09.

Price reverted past open by ~same magnitude — signal band reached at
$162.61. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($163.09). Trailing stop = HWM - $4.28.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
