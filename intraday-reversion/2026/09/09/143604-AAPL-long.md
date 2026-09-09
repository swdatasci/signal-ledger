---
ticker: AAPL
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-09-09T14:36:04+00:00
O: 315.49
M1_pct: 0.662
entry_ref: 313.84
target: 315.49
trailing_amount: 8.36
D1: up
---

## Signal — opening-reversion long on AAPL

Initial move at open: **0.662%** in up direction from O=$315.49.

Price reverted past open by ~same magnitude — signal band reached at
$313.84. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($315.49). Trailing stop = HWM - $8.36.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
