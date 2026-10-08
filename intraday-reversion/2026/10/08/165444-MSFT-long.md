---
ticker: MSFT
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-10-08T16:54:44+00:00
O: 529.81
M1_pct: 0.698
entry_ref: 525.81
target: 529.81
trailing_amount: 14.8
D1: up
---

## Signal — opening-reversion long on MSFT

Initial move at open: **0.698%** in up direction from O=$529.81.

Price reverted past open by ~same magnitude — signal band reached at
$525.81. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($529.81). Trailing stop = HWM - $14.8.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
