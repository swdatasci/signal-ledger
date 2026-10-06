---
ticker: PFE
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-10-06T14:21:34+00:00
O: 27.48
M1_pct: 0.837
entry_ref: 27.29
target: 27.48
trailing_amount: 0.92
D1: up
---

## Signal — opening-reversion long on PFE

Initial move at open: **0.837%** in up direction from O=$27.48.

Price reverted past open by ~same magnitude — signal band reached at
$27.29. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($27.48). Trailing stop = HWM - $0.92.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
