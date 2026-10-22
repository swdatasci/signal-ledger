---
ticker: TMO
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-10-22T14:12:34+00:00
O: 691.7
M1_pct: 1.663
entry_ref: 684.25
target: 691.7
trailing_amount: 46.0
D1: up
---

## Signal — opening-reversion long on TMO

Initial move at open: **1.663%** in up direction from O=$691.7.

Price reverted past open by ~same magnitude — signal band reached at
$684.25. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($691.7). Trailing stop = HWM - $46.0.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
