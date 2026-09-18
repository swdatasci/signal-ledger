---
ticker: AMD
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-09-18T14:46:32+00:00
O: 547.6
M1_pct: 0.687
entry_ref: 544.82
target: 547.6
trailing_amount: 15.04
D1: up
---

## Signal — opening-reversion long on AMD

Initial move at open: **0.687%** in up direction from O=$547.6.

Price reverted past open by ~same magnitude — signal band reached at
$544.82. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($547.6). Trailing stop = HWM - $15.04.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
