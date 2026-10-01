---
ticker: CRM
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-10-01T14:56:04+00:00
O: 235.19
M1_pct: 1.811
entry_ref: 231.7
target: 235.19
trailing_amount: 17.04
D1: up
---

## Signal — opening-reversion long on CRM

Initial move at open: **1.811%** in up direction from O=$235.19.

Price reverted past open by ~same magnitude — signal band reached at
$231.7. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($235.19). Trailing stop = HWM - $17.04.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
