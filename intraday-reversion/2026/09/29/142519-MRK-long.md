---
ticker: MRK
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-09-29T14:25:19+00:00
O: 148.17
M1_pct: 1.478
entry_ref: 146.79
target: 148.17
trailing_amount: 8.76
D1: up
---

## Signal — opening-reversion long on MRK

Initial move at open: **1.478%** in up direction from O=$148.17.

Price reverted past open by ~same magnitude — signal band reached at
$146.79. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($148.17). Trailing stop = HWM - $8.76.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
