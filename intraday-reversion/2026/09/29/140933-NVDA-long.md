---
ticker: NVDA
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-09-29T14:09:33+00:00
O: 231.02
M1_pct: 0.779
entry_ref: 229.51
target: 231.02
trailing_amount: 7.2
D1: up
---

## Signal — opening-reversion long on NVDA

Initial move at open: **0.779%** in up direction from O=$231.02.

Price reverted past open by ~same magnitude — signal band reached at
$229.51. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($231.02). Trailing stop = HWM - $7.2.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
