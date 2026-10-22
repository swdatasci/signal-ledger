---
ticker: AAPL
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-10-22T14:33:00+00:00
O: 344.88
M1_pct: 0.696
entry_ref: 342.7
target: 344.88
trailing_amount: 9.6
D1: up
---

## Signal — opening-reversion long on AAPL

Initial move at open: **0.696%** in up direction from O=$344.88.

Price reverted past open by ~same magnitude — signal band reached at
$342.7. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($344.88). Trailing stop = HWM - $9.6.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
