---
ticker: BLK
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-09-02T15:22:47+00:00
O: 1128.79
M1_pct: 0.712
entry_ref: 1123.43
target: 1128.79
trailing_amount: 32.16
D1: up
---

## Signal — opening-reversion long on BLK

Initial move at open: **0.712%** in up direction from O=$1128.79.

Price reverted past open by ~same magnitude — signal band reached at
$1123.43. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($1128.79). Trailing stop = HWM - $32.16.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
