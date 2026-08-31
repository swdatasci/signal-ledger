---
ticker: CVX
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-31T16:07:17+00:00
O: 206.08
M1_pct: 1.135
entry_ref: 204.37
target: 206.08
trailing_amount: 9.36
D1: up
---

## Signal — opening-reversion long on CVX

Initial move at open: **1.135%** in up direction from O=$206.08.

Price reverted past open by ~same magnitude — signal band reached at
$204.37. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($206.08). Trailing stop = HWM - $9.36.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
