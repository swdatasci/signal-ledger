---
ticker: MRK
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-04T15:45:09+00:00
O: 128.63
M1_pct: 0.894
entry_ref: 127.63
target: 128.63
trailing_amount: 4.6
D1: up
---

## Signal — opening-reversion long on MRK

Initial move at open: **0.894%** in up direction from O=$128.63.

Price reverted past open by ~same magnitude — signal band reached at
$127.63. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($128.63). Trailing stop = HWM - $4.6.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
