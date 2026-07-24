---
ticker: UNH
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-07-24T15:37:12+00:00
O: 421.87
M1_pct: 0.507
entry_ref: 419.98
target: 421.87
trailing_amount: 3.21
D1: up
---

## Signal — opening-reversion long on UNH

Initial move at open: **0.507%** in up direction from O=$421.87.

Price reverted past open by ~same magnitude — signal band reached at
$419.98. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($421.87). Trailing stop = HWM - $3.21.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
