---
ticker: AMD
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-09-25T14:20:00+00:00
O: 634.0
M1_pct: 0.789
entry_ref: 631.43
target: 634.0
trailing_amount: 20.0
D1: up
---

## Signal — opening-reversion long on AMD

Initial move at open: **0.789%** in up direction from O=$634.0.

Price reverted past open by ~same magnitude — signal band reached at
$631.43. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($634.0). Trailing stop = HWM - $20.0.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
