---
ticker: JNJ
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-09-29T14:27:11+00:00
O: 269.11
M1_pct: 1.033
entry_ref: 266.05
target: 269.11
trailing_amount: 11.12
D1: up
---

## Signal — opening-reversion long on JNJ

Initial move at open: **1.033%** in up direction from O=$269.11.

Price reverted past open by ~same magnitude — signal band reached at
$266.05. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($269.11). Trailing stop = HWM - $11.12.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
