---
ticker: DIS
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-10-13T16:41:04+00:00
O: 109.52
M1_pct: 0.584
entry_ref: 109.12
target: 109.52
trailing_amount: 2.56
D1: up
---

## Signal — opening-reversion long on DIS

Initial move at open: **0.584%** in up direction from O=$109.52.

Price reverted past open by ~same magnitude — signal band reached at
$109.12. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($109.52). Trailing stop = HWM - $2.56.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
