---
ticker: TMO
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-10-16T15:18:02+00:00
O: 692.26
M1_pct: 1.003
entry_ref: 687.86
target: 692.26
trailing_amount: 27.76
D1: up
---

## Signal — opening-reversion long on TMO

Initial move at open: **1.003%** in up direction from O=$692.26.

Price reverted past open by ~same magnitude — signal band reached at
$687.86. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($692.26). Trailing stop = HWM - $27.76.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
