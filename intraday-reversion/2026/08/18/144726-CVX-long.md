---
ticker: CVX
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-18T14:47:26+00:00
O: 205.03
M1_pct: 0.58
entry_ref: 204.09
target: 205.03
trailing_amount: 4.76
D1: up
---

## Signal — opening-reversion long on CVX

Initial move at open: **0.58%** in up direction from O=$205.03.

Price reverted past open by ~same magnitude — signal band reached at
$204.09. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($205.03). Trailing stop = HWM - $4.76.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
