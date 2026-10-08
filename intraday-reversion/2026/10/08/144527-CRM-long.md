---
ticker: CRM
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-10-08T14:45:27+00:00
O: 225.46
M1_pct: 1.104
entry_ref: 223.48
target: 225.46
trailing_amount: 9.96
D1: up
---

## Signal — opening-reversion long on CRM

Initial move at open: **1.104%** in up direction from O=$225.46.

Price reverted past open by ~same magnitude — signal band reached at
$223.48. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($225.46). Trailing stop = HWM - $9.96.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
