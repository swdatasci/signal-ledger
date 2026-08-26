---
ticker: BLK
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-26T14:41:50+00:00
O: 1175.71
M1_pct: 0.536
entry_ref: 1172.35
target: 1175.71
trailing_amount: 25.2
D1: up
---

## Signal — opening-reversion long on BLK

Initial move at open: **0.536%** in up direction from O=$1175.71.

Price reverted past open by ~same magnitude — signal band reached at
$1172.35. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($1175.71). Trailing stop = HWM - $25.2.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
