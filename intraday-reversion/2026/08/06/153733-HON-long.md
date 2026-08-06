---
ticker: HON
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-06T15:37:33+00:00
O: 248.41
M1_pct: 0.552
entry_ref: 242.86
target: 248.41
trailing_amount: 5.48
D1: up
---

## Signal — opening-reversion long on HON

Initial move at open: **0.552%** in up direction from O=$248.41.

Price reverted past open by ~same magnitude — signal band reached at
$242.86. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($248.41). Trailing stop = HWM - $5.48.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
