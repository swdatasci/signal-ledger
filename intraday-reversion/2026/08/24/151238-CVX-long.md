---
ticker: CVX
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-24T15:12:38+00:00
O: 203.67
M1_pct: 0.8
entry_ref: 202.48
target: 203.67
trailing_amount: 6.52
D1: up
---

## Signal — opening-reversion long on CVX

Initial move at open: **0.8%** in up direction from O=$203.67.

Price reverted past open by ~same magnitude — signal band reached at
$202.48. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($203.67). Trailing stop = HWM - $6.52.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
