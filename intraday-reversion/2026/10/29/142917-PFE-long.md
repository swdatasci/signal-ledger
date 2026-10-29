---
ticker: PFE
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-10-29T14:29:17+00:00
O: 29.93
M1_pct: 0.835
entry_ref: 29.78
target: 29.93
trailing_amount: 1.0
D1: up
---

## Signal — opening-reversion long on PFE

Initial move at open: **0.835%** in up direction from O=$29.93.

Price reverted past open by ~same magnitude — signal band reached at
$29.78. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($29.93). Trailing stop = HWM - $1.0.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
