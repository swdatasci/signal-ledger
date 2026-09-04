---
ticker: JPM
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-09-04T14:02:14+00:00
O: 361.0
M1_pct: 0.515
entry_ref: 359.99
target: 361.0
trailing_amount: 7.44
D1: up
---

## Signal — opening-reversion long on JPM

Initial move at open: **0.515%** in up direction from O=$361.0.

Price reverted past open by ~same magnitude — signal band reached at
$359.99. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($361.0). Trailing stop = HWM - $7.44.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
