---
ticker: MRK
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-11-02T15:06:37+00:00
O: 148.82
M1_pct: 0.974
entry_ref: 147.88
target: 148.82
trailing_amount: 5.8
D1: up
---

## Signal — opening-reversion long on MRK

Initial move at open: **0.974%** in up direction from O=$148.82.

Price reverted past open by ~same magnitude — signal band reached at
$147.88. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($148.82). Trailing stop = HWM - $5.8.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
