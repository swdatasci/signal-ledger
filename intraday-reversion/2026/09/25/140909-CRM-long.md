---
ticker: CRM
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-09-25T14:09:09+00:00
O: 237.03
M1_pct: 0.987
entry_ref: 236.26
target: 237.03
trailing_amount: 9.36
D1: up
---

## Signal — opening-reversion long on CRM

Initial move at open: **0.987%** in up direction from O=$237.03.

Price reverted past open by ~same magnitude — signal band reached at
$236.26. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($237.03). Trailing stop = HWM - $9.36.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
