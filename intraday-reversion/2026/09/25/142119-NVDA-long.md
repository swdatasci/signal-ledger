---
ticker: NVDA
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-09-25T14:21:19+00:00
O: 225.11
M1_pct: 0.813
entry_ref: 223.72
target: 225.11
trailing_amount: 7.32
D1: up
---

## Signal — opening-reversion long on NVDA

Initial move at open: **0.813%** in up direction from O=$225.11.

Price reverted past open by ~same magnitude — signal band reached at
$223.72. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($225.11). Trailing stop = HWM - $7.32.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
