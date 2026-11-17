---
ticker: UNP
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-11-17T15:05:12+00:00
O: 301.18
M1_pct: 0.704
entry_ref: 298.58
target: 301.18
trailing_amount: 8.48
D1: up
---

## Signal — opening-reversion long on UNP

Initial move at open: **0.704%** in up direction from O=$301.18.

Price reverted past open by ~same magnitude — signal band reached at
$298.58. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($301.18). Trailing stop = HWM - $8.48.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
