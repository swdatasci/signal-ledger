---
ticker: UNH
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-07-29T14:44:30+00:00
O: 428.26
M1_pct: 0.799
entry_ref: 425.5
target: 428.26
trailing_amount: 13.68
D1: up
---

## Signal — opening-reversion long on UNH

Initial move at open: **0.799%** in up direction from O=$428.26.

Price reverted past open by ~same magnitude — signal band reached at
$425.5. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($428.26). Trailing stop = HWM - $13.68.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
