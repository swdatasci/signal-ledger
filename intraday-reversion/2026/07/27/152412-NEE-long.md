---
ticker: NEE
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-07-27T15:24:12+00:00
O: 89.66
M1_pct: 0.558
entry_ref: 89.13
target: 89.66
trailing_amount: 2.0
D1: up
---

## Signal — opening-reversion long on NEE

Initial move at open: **0.558%** in up direction from O=$89.66.

Price reverted past open by ~same magnitude — signal band reached at
$89.13. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($89.66). Trailing stop = HWM - $2.0.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
