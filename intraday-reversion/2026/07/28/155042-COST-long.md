---
ticker: COST
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-07-28T15:50:42+00:00
O: 981.78
M1_pct: 0.588
entry_ref: 974.279
target: 981.78
trailing_amount: 23.08
D1: up
---

## Signal — opening-reversion long on COST

Initial move at open: **0.588%** in up direction from O=$981.78.

Price reverted past open by ~same magnitude — signal band reached at
$974.279. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($981.78). Trailing stop = HWM - $23.08.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
