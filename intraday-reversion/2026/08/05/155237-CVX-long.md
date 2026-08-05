---
ticker: CVX
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-05T15:52:37+00:00
O: 188.25
M1_pct: 0.606
entry_ref: 186.78
target: 188.25
trailing_amount: 4.56
D1: up
---

## Signal — opening-reversion long on CVX

Initial move at open: **0.606%** in up direction from O=$188.25.

Price reverted past open by ~same magnitude — signal band reached at
$186.78. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($188.25). Trailing stop = HWM - $4.56.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
