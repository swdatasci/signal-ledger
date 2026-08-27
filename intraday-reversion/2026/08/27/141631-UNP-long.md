---
ticker: UNP
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-27T14:16:31+00:00
O: 308.0
M1_pct: 0.565
entry_ref: 306.73
target: 308.0
trailing_amount: 6.96
D1: up
---

## Signal — opening-reversion long on UNP

Initial move at open: **0.565%** in up direction from O=$308.0.

Price reverted past open by ~same magnitude — signal band reached at
$306.73. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($308.0). Trailing stop = HWM - $6.96.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
