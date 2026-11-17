---
ticker: CVX
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-11-17T17:59:00+00:00
O: 217.58
M1_pct: 0.896
entry_ref: 216.04
target: 217.58
trailing_amount: 7.8
D1: up
---

## Signal — opening-reversion long on CVX

Initial move at open: **0.896%** in up direction from O=$217.58.

Price reverted past open by ~same magnitude — signal band reached at
$216.04. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($217.58). Trailing stop = HWM - $7.8.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
