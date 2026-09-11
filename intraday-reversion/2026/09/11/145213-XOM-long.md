---
ticker: XOM
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-09-11T14:52:13+00:00
O: 165.07
M1_pct: 0.848
entry_ref: 164.63
target: 165.07
trailing_amount: 5.6
D1: up
---

## Signal — opening-reversion long on XOM

Initial move at open: **0.848%** in up direction from O=$165.07.

Price reverted past open by ~same magnitude — signal band reached at
$164.63. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($165.07). Trailing stop = HWM - $5.6.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
