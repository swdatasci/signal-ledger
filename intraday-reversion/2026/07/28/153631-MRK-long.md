---
ticker: MRK
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-07-28T15:36:31+00:00
O: 133.1
M1_pct: 0.999
entry_ref: 131.4
target: 133.1
trailing_amount: 5.32
D1: up
---

## Signal — opening-reversion long on MRK

Initial move at open: **0.999%** in up direction from O=$133.1.

Price reverted past open by ~same magnitude — signal band reached at
$131.4. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($133.1). Trailing stop = HWM - $5.32.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
