---
ticker: XOM
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-18T14:42:00+00:00
O: 164.35
M1_pct: 0.56
entry_ref: 163.87
target: 164.35
trailing_amount: 3.68
D1: up
---

## Signal — opening-reversion long on XOM

Initial move at open: **0.56%** in up direction from O=$164.35.

Price reverted past open by ~same magnitude — signal band reached at
$163.87. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($164.35). Trailing stop = HWM - $3.68.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
