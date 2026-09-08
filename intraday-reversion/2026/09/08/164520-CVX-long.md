---
ticker: CVX
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-09-08T16:45:20+00:00
O: 211.25
M1_pct: 0.937
entry_ref: 209.87
target: 211.25
trailing_amount: 7.92
D1: up
---

## Signal — opening-reversion long on CVX

Initial move at open: **0.937%** in up direction from O=$211.25.

Price reverted past open by ~same magnitude — signal band reached at
$209.87. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($211.25). Trailing stop = HWM - $7.92.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
