# AI Consensus — passive observation ledger

Published daily by an automated pipeline.
**This is a research ledger. NOT a tradeable signal, NOT investment advice.**

## What this is

Every day at 04:00 UTC, an internal service (`ai-consensus-daemon`) pulls the last 24 hours of financial-news headlines per tradable scope (e.g. `SPY`, `QQQ`, `XLF`, `BTC`), then asks **three LLMs** (currently Claude, GPT, Gemini) to predict tomorrow's direction using **two different prompt styles** each:

- **naive** — "will this go up or down tomorrow?" with just raw headlines
- **sophisticated** — reasoning-chain prompt that explicitly considers counter-evidence

That produces **6 predictions per scope per day** (3 models × 2 styles).

Each morning after the daemon runs, this ledger publishes the full transcripts.

## Why publish it publicly, before we know if it works

Two reasons:

1. **Tamper-evident timestamps.** Git commits prove when each prediction was made — nobody (including us) can retroactively edit an entry once it's committed. That's the honest way to evaluate a signal.
2. **Build in public.** The methodology is transparent. If it works, subscribers see the whole runway. If it doesn't, they see us kill it honestly.

## Phase status

**Phase 1: passive observation.** We collect predictions daily and record actual outcomes. No trading yet. Runs 30-60 days until enough forward data exists.

**Phase 2 (unlocks ~Aug-Sep 2026): backtest the contrarian rule.** Hypothesis: when 3 LLMs all agree strongly, the crowd is priced in → fade. We measure this against actual price outcomes.

**Phase 3 (only if Phase 2 shows edge):** paper-trade the rule on Alpaca, hourly cadence, with an arbiter LLM using debate structure. Publish trades to the parent `ledger.md` alongside the signal-service's existing signals.

## Not investment advice

Signals published under the publisher's exemption to the Investment Advisers Act §202(a)(11)(D).
Do your own research. Past predictions are not indicative of future accuracy.

## File format

`YYYY-MM-DD.md` — one file per prediction day. Contains the aggregate agreement table plus per-model reasoning transcripts.
