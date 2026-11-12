---
ticker: DIS
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-11-12T17:07:35+00:00
O: 119.53
M1_pct: 0.761
entry_ref: 118.95
target: 119.53
trailing_amount: 3.64
D1: up
---

## Signal — opening-reversion long on DIS

Initial move at open: **0.761%** in up direction from O=$119.53.

Price reverted past open by ~same magnitude — signal band reached at
$118.95. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($119.53). Trailing stop = HWM - $3.64.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
