---
ticker: ABBV
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-04T15:32:19+00:00
O: 244.85
M1_pct: 0.502
entry_ref: 243.9
target: 244.85
trailing_amount: 4.92
D1: up
---

## Signal — opening-reversion long on ABBV

Initial move at open: **0.502%** in up direction from O=$244.85.

Price reverted past open by ~same magnitude — signal band reached at
$243.9. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($244.85). Trailing stop = HWM - $4.92.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
