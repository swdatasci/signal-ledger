---
ticker: BAC
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-09-11T14:17:37+00:00
O: 63.11
M1_pct: 1.141
entry_ref: 62.65
target: 63.11
trailing_amount: 2.88
D1: up
---

## Signal — opening-reversion long on BAC

Initial move at open: **1.141%** in up direction from O=$63.11.

Price reverted past open by ~same magnitude — signal band reached at
$62.65. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($63.11). Trailing stop = HWM - $2.88.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
