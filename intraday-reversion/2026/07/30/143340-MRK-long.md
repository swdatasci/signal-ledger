---
ticker: MRK
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-07-30T14:33:40+00:00
O: 128.2
M1_pct: 0.757
entry_ref: 127.31
target: 128.2
trailing_amount: 3.88
D1: up
---

## Signal — opening-reversion long on MRK

Initial move at open: **0.757%** in up direction from O=$128.2.

Price reverted past open by ~same magnitude — signal band reached at
$127.31. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($128.2). Trailing stop = HWM - $3.88.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
