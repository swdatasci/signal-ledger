---
ticker: XOM
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-08-05T15:47:58+00:00
O: 152.28
M1_pct: 0.558
entry_ref: 151.33
target: 152.28
trailing_amount: 3.4
D1: up
---

## Signal — opening-reversion long on XOM

Initial move at open: **0.558%** in up direction from O=$152.28.

Price reverted past open by ~same magnitude — signal band reached at
$151.33. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($152.28). Trailing stop = HWM - $3.4.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
