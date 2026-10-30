---
ticker: JNJ
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-10-30T14:03:44+00:00
O: 280.0
M1_pct: 0.721
entry_ref: 278.38
target: 280.0
trailing_amount: 8.08
D1: up
---

## Signal — opening-reversion long on JNJ

Initial move at open: **0.721%** in up direction from O=$280.0.

Price reverted past open by ~same magnitude — signal band reached at
$278.38. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($280.0). Trailing stop = HWM - $8.08.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
