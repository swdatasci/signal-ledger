---
ticker: AMZN
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-13T16:03:24+00:00
O: 267.24
M1_pct: 0.718
entry_ref: 265.86
target: 267.24
trailing_amount: 7.68
D1: up
---

## Signal — opening-reversion long on AMZN

Initial move at open: **0.718%** in up direction from O=$267.24.

Price reverted past open by ~same magnitude — signal band reached at
$265.86. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($267.24). Trailing stop = HWM - $7.68.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
