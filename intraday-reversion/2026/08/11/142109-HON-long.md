---
ticker: HON
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-11T14:21:09+00:00
O: 242.32
M1_pct: 1.028
entry_ref: 241.57
target: 242.32
trailing_amount: 9.96
D1: up
---

## Signal — opening-reversion long on HON

Initial move at open: **1.028%** in up direction from O=$242.32.

Price reverted past open by ~same magnitude — signal band reached at
$241.57. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($242.32). Trailing stop = HWM - $9.96.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
