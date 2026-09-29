---
ticker: TMO
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-09-29T14:11:20+00:00
O: 676.42
M1_pct: 0.708
entry_ref: 673.63
target: 676.42
trailing_amount: 19.16
D1: up
---

## Signal — opening-reversion long on TMO

Initial move at open: **0.708%** in up direction from O=$676.42.

Price reverted past open by ~same magnitude — signal band reached at
$673.63. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($676.42). Trailing stop = HWM - $19.16.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
