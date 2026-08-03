---
ticker: MRK
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-03T15:30:52+00:00
O: 129.44
M1_pct: 1.568
entry_ref: 127.25
target: 129.44
trailing_amount: 8.12
D1: up
---

## Signal — opening-reversion long on MRK

Initial move at open: **1.568%** in up direction from O=$129.44.

Price reverted past open by ~same magnitude — signal band reached at
$127.25. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($129.44). Trailing stop = HWM - $8.12.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
