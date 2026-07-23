# signal-ledger

Public real-time algorithmic-trading ledger — swdatasci.
Signals posted from [@research_signal](https://x.com/research_signal).

Every signal our paper-trader fires is timestamped and committed to this repo automatically.
Every entry, fill, and exit is recorded in `ledger.md`. Git commits give tamper-evident timestamps.

## What's here

- **`ledger.md`** — running append-only log of every signal, entry, fill, and exit
- **`open-positions.md`** — current live paper-trade book
- **`journal/`** — [pre-registered trader journal](./journal/README.md): every trade written BEFORE the broker order, git-committed for tamper-evident sequencing
- **`consensus/`** — [daily 3-LLM consensus predictions](./consensus/) published every morning
- Signals fire from two strategies:
  - **Gov contracts** — DoD contract awards $200M-$1B to public defense/IT primes, T+1 entry, 7d hold. Backtest: SPY-hedged α +48%/yr (IR 2.23) or ITA-hedged α +29%/yr (IR 1.56).
  - **Congress×DPI z≥+2** — high-conviction cross of congressional purchase disclosures with elevated dark-pool activity. Backtest: IR 0.51-0.60.

## Not investment advice

This is a public research ledger. Nothing here is investment advice, an offer to sell securities,
or personalized guidance. Do your own research. Past performance is not indicative of future results.

Signals published under the publisher's exemption to the Investment Advisers Act §202(a)(11)(D).

## Live status

Both paper-traders run under pm2 with 5-minute poll cadence. First trade will appear in `ledger.md`
when a qualifying signal fires from either strategy.
