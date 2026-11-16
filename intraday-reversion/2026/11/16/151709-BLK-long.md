---
ticker: BLK
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-11-16T15:17:09+00:00
O: 1212.05
M1_pct: 0.61
entry_ref: 1206.45
target: 1212.05
trailing_amount: 29.56
D1: up
---

## Signal — opening-reversion long on BLK

Initial move at open: **0.61%** in up direction from O=$1212.05.

Price reverted past open by ~same magnitude — signal band reached at
$1206.45. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($1212.05). Trailing stop = HWM - $29.56.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
