---
ticker: CRM
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-10-12T15:58:30+00:00
O: 236.49
M1_pct: 1.865
entry_ref: 233.47
target: 236.49
trailing_amount: 17.64
D1: up
---

## Signal — opening-reversion long on CRM

Initial move at open: **1.865%** in up direction from O=$236.49.

Price reverted past open by ~same magnitude — signal band reached at
$233.47. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($236.49). Trailing stop = HWM - $17.64.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
