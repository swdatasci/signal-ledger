---
ticker: AVGO
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-10T15:43:40+00:00
O: 427.53
M1_pct: 0.625
entry_ref: 425.81
target: 427.53
trailing_amount: 10.68
D1: up
---

## Signal — opening-reversion long on AVGO

Initial move at open: **0.625%** in up direction from O=$427.53.

Price reverted past open by ~same magnitude — signal band reached at
$425.81. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($427.53). Trailing stop = HWM - $10.68.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
