---
ticker: GOOGL
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-06T15:19:55+00:00
O: 360.96
M1_pct: 0.878
entry_ref: 359.18
target: 360.96
trailing_amount: 12.68
D1: up
---

## Signal — opening-reversion long on GOOGL

Initial move at open: **0.878%** in up direction from O=$360.96.

Price reverted past open by ~same magnitude — signal band reached at
$359.18. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($360.96). Trailing stop = HWM - $12.68.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
