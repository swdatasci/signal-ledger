---
ticker: XOM
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-21T15:12:25+00:00
O: 166.54
M1_pct: 0.877
entry_ref: 165.68
target: 166.54
trailing_amount: 5.84
D1: up
---

## Signal — opening-reversion long on XOM

Initial move at open: **0.877%** in up direction from O=$166.54.

Price reverted past open by ~same magnitude — signal band reached at
$165.68. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($166.54). Trailing stop = HWM - $5.84.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
