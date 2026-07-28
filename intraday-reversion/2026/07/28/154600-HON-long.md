---
ticker: HON
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-07-28T15:46:00+00:00
O: 249.66
M1_pct: 0.537
entry_ref: 248.61
target: 249.66
trailing_amount: 5.36
D1: up
---

## Signal — opening-reversion long on HON

Initial move at open: **0.537%** in up direction from O=$249.66.

Price reverted past open by ~same magnitude — signal band reached at
$248.61. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($249.66). Trailing stop = HWM - $5.36.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
