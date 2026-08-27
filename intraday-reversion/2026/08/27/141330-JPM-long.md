---
ticker: JPM
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-27T14:13:30+00:00
O: 354.68
M1_pct: 0.815
entry_ref: 353.1
target: 354.68
trailing_amount: 11.56
D1: up
---

## Signal — opening-reversion long on JPM

Initial move at open: **0.815%** in up direction from O=$354.68.

Price reverted past open by ~same magnitude — signal band reached at
$353.1. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($354.68). Trailing stop = HWM - $11.56.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
