---
ticker: HON
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-07-28T14:50:06+00:00
O: 249.8
M1_pct: 0.881
entry_ref: 247.4
target: 249.8
trailing_amount: 8.8
D1: up
---

## Signal — opening-reversion long on HON

Initial move at open: **0.881%** in up direction from O=$249.8.

Price reverted past open by ~same magnitude — signal band reached at
$247.4. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($249.8). Trailing stop = HWM - $8.8.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
