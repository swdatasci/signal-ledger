---
ticker: XOM
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-09-08T16:56:02+00:00
O: 160.61
M1_pct: 1.557
entry_ref: 158.89
target: 160.61
trailing_amount: 10.0
D1: up
---

## Signal — opening-reversion long on XOM

Initial move at open: **1.557%** in up direction from O=$160.61.

Price reverted past open by ~same magnitude — signal band reached at
$158.89. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($160.61). Trailing stop = HWM - $10.0.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
