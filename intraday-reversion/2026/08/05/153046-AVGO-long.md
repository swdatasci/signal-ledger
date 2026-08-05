---
ticker: AVGO
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-05T15:30:46+00:00
O: 422.86
M1_pct: 0.979
entry_ref: 419.62
target: 422.86
trailing_amount: 16.56
D1: up
---

## Signal — opening-reversion long on AVGO

Initial move at open: **0.979%** in up direction from O=$422.86.

Price reverted past open by ~same magnitude — signal band reached at
$419.62. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($422.86). Trailing stop = HWM - $16.56.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
