---
ticker: BAC
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-09-10T14:08:03+00:00
O: 62.65
M1_pct: 0.575
entry_ref: 62.43
target: 62.65
trailing_amount: 1.44
D1: up
---

## Signal — opening-reversion long on BAC

Initial move at open: **0.575%** in up direction from O=$62.65.

Price reverted past open by ~same magnitude — signal band reached at
$62.43. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($62.65). Trailing stop = HWM - $1.44.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
