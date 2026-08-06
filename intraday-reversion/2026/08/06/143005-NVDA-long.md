---
ticker: NVDA
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-06T14:30:05+00:00
O: 221.53
M1_pct: 0.948
entry_ref: 219.87
target: 221.53
trailing_amount: 8.4
D1: up
---

## Signal — opening-reversion long on NVDA

Initial move at open: **0.948%** in up direction from O=$221.53.

Price reverted past open by ~same magnitude — signal band reached at
$219.87. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($221.53). Trailing stop = HWM - $8.4.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
