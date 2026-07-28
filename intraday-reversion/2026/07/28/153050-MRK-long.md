---
ticker: MRK
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-07-28T15:30:50+00:00
O: 133.29
M1_pct: 0.855
entry_ref: 132.25
target: 133.29
trailing_amount: 4.56
D1: up
---

## Signal — opening-reversion long on MRK

Initial move at open: **0.855%** in up direction from O=$133.29.

Price reverted past open by ~same magnitude — signal band reached at
$132.25. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($133.29). Trailing stop = HWM - $4.56.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
