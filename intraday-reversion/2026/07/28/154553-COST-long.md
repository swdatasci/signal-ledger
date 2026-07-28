---
ticker: COST
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-07-28T15:45:53+00:00
O: 981.0
M1_pct: 0.668
entry_ref: 974.09
target: 981.0
trailing_amount: 26.2
D1: up
---

## Signal — opening-reversion long on COST

Initial move at open: **0.668%** in up direction from O=$981.0.

Price reverted past open by ~same magnitude — signal band reached at
$974.09. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($981.0). Trailing stop = HWM - $26.2.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
