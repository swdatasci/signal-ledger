---
ticker: CSCO
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-04T15:42:13+00:00
O: 120.97
M1_pct: 0.554
entry_ref: 120.47
target: 120.97
trailing_amount: 2.68
D1: up
---

## Signal — opening-reversion long on CSCO

Initial move at open: **0.554%** in up direction from O=$120.97.

Price reverted past open by ~same magnitude — signal band reached at
$120.47. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($120.97). Trailing stop = HWM - $2.68.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
