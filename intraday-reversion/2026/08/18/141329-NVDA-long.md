---
ticker: NVDA
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-18T14:13:29+00:00
O: 220.37
M1_pct: 0.576
entry_ref: 219.05
target: 220.37
trailing_amount: 5.08
D1: up
---

## Signal — opening-reversion long on NVDA

Initial move at open: **0.576%** in up direction from O=$220.37.

Price reverted past open by ~same magnitude — signal band reached at
$219.05. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($220.37). Trailing stop = HWM - $5.08.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
