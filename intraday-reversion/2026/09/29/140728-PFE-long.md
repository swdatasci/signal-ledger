---
ticker: PFE
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-09-29T14:07:28+00:00
O: 28.61
M1_pct: 0.524
entry_ref: 28.47
target: 28.61
trailing_amount: 0.6
D1: up
---

## Signal — opening-reversion long on PFE

Initial move at open: **0.524%** in up direction from O=$28.61.

Price reverted past open by ~same magnitude — signal band reached at
$28.47. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($28.61). Trailing stop = HWM - $0.6.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
