---
ticker: NVDA
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-10-01T15:05:19+00:00
O: 229.98
M1_pct: 0.839
entry_ref: 228.85
target: 229.98
trailing_amount: 7.72
D1: up
---

## Signal — opening-reversion long on NVDA

Initial move at open: **0.839%** in up direction from O=$229.98.

Price reverted past open by ~same magnitude — signal band reached at
$228.85. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($229.98). Trailing stop = HWM - $7.72.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
