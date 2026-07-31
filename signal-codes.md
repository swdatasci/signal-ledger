---
title: Signal codes — what the notification fields mean
---

# Signal codes

## Which notification is this?

You'll see four distinct Pushover title formats. What produced it tells you what to do with it.

| Title format | Producer | Meaning |
|---|---|---|
| `Signal YYYY-MM-DD: N at ≥high` | `live-signal-producer` (pm2 #62) | Batch of catalog signals firing this slot. See sections below. |
| `[llm-trader] BUY JPM` (or SELL / EXIT etc.) | `llm-trader` → `signal-ledger/ledger_writer.py` | Per-trade decision from the LLM-driven daily-bar trader. Not a catalog signal; a specific ticker action on paper3-sim. |
| `Morning Brief — YYYY-MM-DD` | `morning-brief` (pm2 #58) | Daily briefing digest with a "tap to open" link to the full brief page. |
| `Calendar signals YYYY-MM-DD: N firing` | `daily_calendar_briefing.py` — **LEGACY** | Old format; superseded by `Signal ...`. The pm2 job that produced these was removed. If you see a new one, something is running the old script ad-hoc. |

Everything below applies to the `Signal ...` family from `live-signal-producer`.

## Notification shape (live-signal-producer)

Every Pushover from `live-signal-producer` follows this shape:

```
● CODE [confidence]
  DO THIS: <plain-English action>
  Size: <suggested position size>
  Skip if: <conditions to abort>
  Edge: exp +X.XX% hit XX% (t=+X.X)
```

## What the `Edge:` fields mean

| Field | Meaning |
|---|---|
| `exp` | **Expected return** — historical mean % move over the trade's entry→exit window |
| `hit` | **Hit rate** — % of historical fires that closed in the expected direction |
| `t` | **t-statistic** of the historical mean. Higher = more statistically robust. \|t\|≥3 ≈ p<0.01; \|t\|≥5 is very strong. |

## Confidence tiers

Confidence is derived directly from t-stat, not from hit rate or expected return.

| Tier | Trigger | How to treat it |
|---|---|---|
| `[high]` | \|t\| ≥ 5 | Full size (~3% of account). Act on it if entry window is still open. |
| `[medium]` | 3 ≤ \|t\| < 5 | Half size (~1-2%). Real edge but smaller. |
| `[low]` | \|t\| < 3 | Small size or skip. Weak edge; needs other confirmation. |

## Signal catalog

Grouped by the ET slot the signal fires in.

### Pre-open (09:00 ET) — calendar signals

| Code | Trigger | Play | Edge |
|---|---|---|---|
| `T-1xBEAR` | 2nd-to-last trading day of month + SPY below 200SMA | LONG SPY, open→close | exp +0.74%, hit 64%, t=+11.1 |
| `T-1xBULL` | Same day, SPY above 200SMA | LONG SPY, open→close | exp +0.18%, hit 57%, t=+3.1 |
| `T+3xBEAR` | 3rd trading day of month + bear regime | SHORT SPY (or skip fresh longs) | exp −0.34%, hit 42%, t=−5.0 |
| `POST-OPEXxBULL` | Monday after 3rd-Friday + bull | LONG SPY, open→close | exp +0.46%, hit 63%, t=+8.7 |
| `FRIDAYxBULL` | Non-OpEx Friday + bull | LONG SPY, open→close | exp +0.31%, hit 59%, t=+9.6 |
| `MONDAYxBULL` | Monday + bull (favor gap-down opens) | LONG SPY, open→close | exp +0.22%, hit 56%, t=+8.7 |
| `H12-MONTHEND-LIFT` | Last 2 trading days of month, any regime | LONG SPY, open→close | exp +0.23%, hit 55%, t=+7.2 |

*`H12` is just the internal catalog id (hypothesis #12).* The signal itself is
the month-end pension/401k inflow lift on the last 2 trading days.

### Open (09:31 ET) — gap-driven per-ticker signals

`PEAD-<TICKER>-{UP,DN}-X.X%` — fires when today's open gaps ≥3% vs
yesterday's close on any mega-cap universe ticker. Both up and down gaps
drift UP over the next 20 trading days on this universe.

- `UP` — gap up, `DN` — gap down (both are longs; DN is a mean-revert bounce)
- `X.X%` — the size of the |gap| (e.g., `PEAD-NVDA-DN-4.2%`)
- Exit horizon: **20 trading days** forward; the notification includes a target price

| Sub-band | Edge |
|---|---|
| \|gap\| 3-5% up | exp +3.15%, hit 61%, t=+7.2 |
| \|gap\| 3-5% down | exp +2.77%, hit 61%, t=+6.2 |
| \|gap\| ≥5% up | exp +3.35%, hit 59%, t=+4.3 |
| \|gap\| ≥5% down | exp +3.55%, hit 59%, t=+4.3 |

### Lunch (13:30 ET)

`DOWN-LUNCH-<TICKER>` — fires when a ticker's 11:30→13:30 ET return is
worse than −1%. Play: LONG the ticker at 13:30, exit at 15:30 close.
Marginal edge (exp +0.19%, hit 53%, t=+2.4) — always tagged `[low]`.

### Close (15:30 ET)

`H5b-CLOSE-UPDAYCLOSE` — fires when SPY's 09:30→15:30 ET return is
positive by more than +0.2%. Play: LONG the mega-cap basket 15:30→16:00.
Small edge (exp +0.01%, hit 52%, t=+3.9), medium confidence.

`H5b` is again just the catalog id (hypothesis 5b, "close-updayclose").

## Common `Skip if:` conditions

Baseline skips attached to every signal:
- Pre-market VIX spike (VIX > 25) — regime shift risk
- Major macro release today (FOMC / CPI / NFP)
- Ticker-specific earnings today or tomorrow

PEAD signals add: *"Company-specific news dominated the gap (M&A, lawsuit, etc.)"*

MONDAY signals add: *"SPY pre-market gap > +0.5% (missed the down-open setup)"*

## Where the signals come from

- Producer: `caelum-quantconnect/scripts/live_signal_producer.py`
- Runner: pm2 `live-signal-producer` — fires 4 times per US weekday (09:00, 09:31, 13:30, 15:30 ET)
- Ledger: `ledger.md` in this repo (every fire committed)
- Notifications: Pushover, `[high]`-confidence only by default

Signals are recommendations for a manual Fidelity account. The
signal-producer never talks to a broker — Roderick reads the ledger /
Pushover, applies his own second-gate filter, and executes by hand.
