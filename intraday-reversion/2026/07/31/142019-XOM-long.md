---
ticker: XOM
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-07-31T14:20:19+00:00
O: 153.74
M1_pct: 1.06
entry_ref: 152.39
target: 153.74
trailing_amount: 6.52
D1: up
---

## Signal — opening-reversion long on XOM

Initial move at open: **1.06%** in up direction from O=$153.74.

Price reverted past open by ~same magnitude — signal band reached at
$152.39. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($153.74). Trailing stop = HWM - $6.52.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
