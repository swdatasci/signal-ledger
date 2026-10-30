---
ticker: MRK
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-10-30T14:31:28+00:00
O: 149.55
M1_pct: 1.204
entry_ref: 147.91
target: 149.55
trailing_amount: 7.2
D1: up
---

## Signal — opening-reversion long on MRK

Initial move at open: **1.204%** in up direction from O=$149.55.

Price reverted past open by ~same magnitude — signal band reached at
$147.91. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($149.55). Trailing stop = HWM - $7.2.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
