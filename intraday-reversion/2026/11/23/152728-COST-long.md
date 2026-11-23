---
ticker: COST
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-11-23T15:27:28+00:00
O: 1090.52
M1_pct: 0.685
entry_ref: 1086.39
target: 1090.52
trailing_amount: 29.88
D1: up
---

## Signal — opening-reversion long on COST

Initial move at open: **0.685%** in up direction from O=$1090.52.

Price reverted past open by ~same magnitude — signal band reached at
$1086.39. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($1090.52). Trailing stop = HWM - $29.88.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
