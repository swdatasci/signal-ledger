---
ticker: TMO
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-10-06T14:13:27+00:00
O: 683.35
M1_pct: 1.607
entry_ref: 675.63
target: 683.35
trailing_amount: 43.92
D1: up
---

## Signal — opening-reversion long on TMO

Initial move at open: **1.607%** in up direction from O=$683.35.

Price reverted past open by ~same magnitude — signal band reached at
$675.63. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($683.35). Trailing stop = HWM - $43.92.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
