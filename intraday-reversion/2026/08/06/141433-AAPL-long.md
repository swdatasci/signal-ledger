---
ticker: AAPL
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-06T14:14:33+00:00
O: 314.34
M1_pct: 0.62
entry_ref: 313.44
target: 314.34
trailing_amount: 7.8
D1: up
---

## Signal — opening-reversion long on AAPL

Initial move at open: **0.62%** in up direction from O=$314.34.

Price reverted past open by ~same magnitude — signal band reached at
$313.44. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($314.34). Trailing stop = HWM - $7.8.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
