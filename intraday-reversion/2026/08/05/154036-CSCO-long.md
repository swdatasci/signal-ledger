---
ticker: CSCO
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-05T15:40:36+00:00
O: 121.92
M1_pct: 0.525
entry_ref: 121.33
target: 121.92
trailing_amount: 2.56
D1: up
---

## Signal — opening-reversion long on CSCO

Initial move at open: **0.525%** in up direction from O=$121.92.

Price reverted past open by ~same magnitude — signal band reached at
$121.33. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($121.92). Trailing stop = HWM - $2.56.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
