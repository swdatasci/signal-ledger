---
ticker: JNJ
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-07-28T15:37:43+00:00
O: 272.52
M1_pct: 0.873
entry_ref: 269.426
target: 272.52
trailing_amount: 9.52
D1: up
---

## Signal — opening-reversion long on JNJ

Initial move at open: **0.873%** in up direction from O=$272.52.

Price reverted past open by ~same magnitude — signal band reached at
$269.426. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($272.52). Trailing stop = HWM - $9.52.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
