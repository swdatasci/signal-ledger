---
ticker: CSCO
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-10-08T16:45:56+00:00
O: 116.48
M1_pct: 0.601
entry_ref: 115.82
target: 116.48
trailing_amount: 2.8
D1: up
---

## Signal — opening-reversion long on CSCO

Initial move at open: **0.601%** in up direction from O=$116.48.

Price reverted past open by ~same magnitude — signal band reached at
$115.82. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($116.48). Trailing stop = HWM - $2.8.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
