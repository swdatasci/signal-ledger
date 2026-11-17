---
ticker: BLK
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-11-17T16:00:38+00:00
O: 1195.0
M1_pct: 1.001
entry_ref: 1180.73
target: 1195.0
trailing_amount: 47.84
D1: up
---

## Signal — opening-reversion long on BLK

Initial move at open: **1.001%** in up direction from O=$1195.0.

Price reverted past open by ~same magnitude — signal band reached at
$1180.73. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($1195.0). Trailing stop = HWM - $47.84.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
