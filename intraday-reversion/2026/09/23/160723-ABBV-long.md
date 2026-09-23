---
ticker: ABBV
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-09-23T16:07:23+00:00
O: 266.0
M1_pct: 0.906
entry_ref: 264.7
target: 266.0
trailing_amount: 9.64
D1: up
---

## Signal — opening-reversion long on ABBV

Initial move at open: **0.906%** in up direction from O=$266.0.

Price reverted past open by ~same magnitude — signal band reached at
$264.7. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($266.0). Trailing stop = HWM - $9.64.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
