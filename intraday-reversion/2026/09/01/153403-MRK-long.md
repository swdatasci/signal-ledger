---
ticker: MRK
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-09-01T15:34:03+00:00
O: 150.23
M1_pct: 0.965
entry_ref: 149.26
target: 150.23
trailing_amount: 5.8
D1: up
---

## Signal — opening-reversion long on MRK

Initial move at open: **0.965%** in up direction from O=$150.23.

Price reverted past open by ~same magnitude — signal band reached at
$149.26. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($150.23). Trailing stop = HWM - $5.8.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
