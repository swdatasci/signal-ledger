---
ticker: MSFT
direction: long
strategy: intraday-reversion
config: N=30 m1=0.5% trailing=1.5xM1 target=O trend-filter=on market-gate=on parent-30m-cancel=on
ts_utc: 2026-11-02T17:11:25+00:00
O: 523.9
M1_pct: 0.874
entry_ref: 521.09
target: 523.9
trailing_amount: 18.32
D1: up
---

## Signal — opening-reversion long on MSFT

Initial move at open: **0.874%** in up direction from O=$523.9.

Price reverted past open by ~same magnitude — signal band reached at
$521.09. Trend filter passed (price > 50-day MA > 200-day MA).
Market-context gate passed (SPY not down > 1%).

Entering long. Target = O ($523.9). Trailing stop = HWM - $18.32.
Winners ride multi-day if trailing stop keeps trailing up; parent order
cancels itself if unfilled within 30 minutes.

Not investment advice.
