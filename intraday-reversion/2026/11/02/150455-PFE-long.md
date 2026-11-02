---
ticker: PFE
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-11-02T15:04:55+00:00
O: 30.45
M1_pct: 0.624
entry_ref: 30.26
target: 30.45
trailing_amount: 0.76
D1: up
---

## Signal — opening-reversion long on PFE

Initial move at open: **0.624%** in up direction from O=$30.45.

Price reverted past open by ~same magnitude — signal band reached at
$30.26. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($30.45). Trailing stop = HWM - $0.76.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
