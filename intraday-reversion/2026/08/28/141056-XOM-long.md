---
ticker: XOM
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-28T14:10:56+00:00
O: 156.6
M1_pct: 0.524
entry_ref: 155.71
target: 156.6
trailing_amount: 3.28
D1: up
---

## Signal — opening-reversion long on XOM

Initial move at open: **0.524%** in up direction from O=$156.6.

Price reverted past open by ~same magnitude — signal band reached at
$155.71. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($156.6). Trailing stop = HWM - $3.28.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
