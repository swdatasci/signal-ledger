---
ticker: COST
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-07-28T15:48:28+00:00
O: 980.52
M1_pct: 0.717
entry_ref: 973.72
target: 980.52
trailing_amount: 28.12
D1: up
---

## Signal — opening-reversion long on COST

Initial move at open: **0.717%** in up direction from O=$980.52.

Price reverted past open by ~same magnitude — signal band reached at
$973.72. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($980.52). Trailing stop = HWM - $28.12.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
