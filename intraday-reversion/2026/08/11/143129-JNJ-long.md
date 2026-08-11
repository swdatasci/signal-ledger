---
ticker: JNJ
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-11T14:31:29+00:00
O: 261.23
M1_pct: 1.118
entry_ref: 259.23
target: 261.23
trailing_amount: 11.68
D1: up
---

## Signal — opening-reversion long on JNJ

Initial move at open: **1.118%** in up direction from O=$261.23.

Price reverted past open by ~same magnitude — signal band reached at
$259.23. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($261.23). Trailing stop = HWM - $11.68.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
