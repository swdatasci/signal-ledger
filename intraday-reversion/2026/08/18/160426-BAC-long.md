---
ticker: BAC
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-18T16:04:26+00:00
O: 63.99
M1_pct: 0.625
entry_ref: 63.73
target: 63.99
trailing_amount: 1.6
D1: up
---

## Signal — opening-reversion long on BAC

Initial move at open: **0.625%** in up direction from O=$63.99.

Price reverted past open by ~same magnitude — signal band reached at
$63.73. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($63.99). Trailing stop = HWM - $1.6.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
