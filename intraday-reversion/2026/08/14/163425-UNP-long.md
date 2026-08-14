---
ticker: UNP
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-14T16:34:25+00:00
O: 298.05
M1_pct: 0.778
entry_ref: 296.47
target: 298.05
trailing_amount: 9.28
D1: up
---

## Signal — opening-reversion long on UNP

Initial move at open: **0.778%** in up direction from O=$298.05.

Price reverted past open by ~same magnitude — signal band reached at
$296.47. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($298.05). Trailing stop = HWM - $9.28.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
