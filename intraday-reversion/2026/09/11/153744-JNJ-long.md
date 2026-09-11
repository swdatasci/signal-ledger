---
ticker: JNJ
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-09-11T15:37:44+00:00
O: 268.03
M1_pct: 0.836
entry_ref: 266.64
target: 268.03
trailing_amount: 8.96
D1: up
---

## Signal — opening-reversion long on JNJ

Initial move at open: **0.836%** in up direction from O=$268.03.

Price reverted past open by ~same magnitude — signal band reached at
$266.64. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($268.03). Trailing stop = HWM - $8.96.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
