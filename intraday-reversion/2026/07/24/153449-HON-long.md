---
ticker: HON
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-07-24T15:34:49+00:00
O: 245.19
M1_pct: 0.673
entry_ref: 243.045
target: 245.19
trailing_amount: 2.48
D1: up
---

## Signal — opening-reversion long on HON

Initial move at open: **0.673%** in up direction from O=$245.19.

Price reverted past open by ~same magnitude — signal band reached at
$243.045. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($245.19). Trailing stop = HWM - $2.48.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
