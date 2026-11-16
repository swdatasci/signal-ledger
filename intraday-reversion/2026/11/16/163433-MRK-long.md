---
ticker: MRK
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-11-16T16:34:33+00:00
O: 147.9
M1_pct: 0.899
entry_ref: 146.99
target: 147.9
trailing_amount: 5.32
D1: up
---

## Signal — opening-reversion long on MRK

Initial move at open: **0.899%** in up direction from O=$147.9.

Price reverted past open by ~same magnitude — signal band reached at
$146.99. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($147.9). Trailing stop = HWM - $5.32.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
