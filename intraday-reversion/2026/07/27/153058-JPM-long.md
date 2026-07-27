---
ticker: JPM
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-07-27T15:30:58+00:00
O: 357.24
M1_pct: 0.507
entry_ref: 354.887
target: 357.24
trailing_amount: 7.24
D1: up
---

## Signal — opening-reversion long on JPM

Initial move at open: **0.507%** in up direction from O=$357.24.

Price reverted past open by ~same magnitude — signal band reached at
$354.887. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($357.24). Trailing stop = HWM - $7.24.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
