---
ticker: MRK
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-09-02T14:18:08+00:00
O: 151.5
M1_pct: 0.785
entry_ref: 150.43
target: 151.5
trailing_amount: 4.76
D1: up
---

## Signal — opening-reversion long on MRK

Initial move at open: **0.785%** in up direction from O=$151.5.

Price reverted past open by ~same magnitude — signal band reached at
$150.43. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($151.5). Trailing stop = HWM - $4.76.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
