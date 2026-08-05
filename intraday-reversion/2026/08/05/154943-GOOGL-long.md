---
ticker: GOOGL
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-05T15:49:43+00:00
O: 378.79
M1_pct: 0.507
entry_ref: 376.79
target: 378.79
trailing_amount: 7.68
D1: up
---

## Signal — opening-reversion long on GOOGL

Initial move at open: **0.507%** in up direction from O=$378.79.

Price reverted past open by ~same magnitude — signal band reached at
$376.79. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($378.79). Trailing stop = HWM - $7.68.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
