# signal-ledger

Public real-time algorithmic-trading ledger — swdatasci.
Signals posted from [@research_signal](https://x.com/research_signal).

Every signal our paper-trader fires is timestamped and committed to this repo automatically.
Every entry, fill, and exit is recorded in `ledger.md`. Git commits give tamper-evident timestamps.

## What's here

- **`ledger.md`** — running append-only log of every signal, entry, fill, and exit
- **`open-positions.md`** — current live paper-trade book
- **[Signal codes reference](./signal-codes)** — what the Pushover notification fields (`exp`, `hit`, `t`, confidence tiers) mean, and the full catalog of signal codes
- **`journal/`** — [pre-registered trader journal](./journal/README.md): every trade written BEFORE the broker order, git-committed for tamper-evident sequencing
- **`consensus/`** — [daily 3-LLM consensus predictions](./consensus/) published every morning
### Status of the two strategies — read this before the numbers

**Neither strategy has placed a single order.** Measured 2026-08-10 and
re-verified 2026-08-25 from the live logs: gov-contracts 75 signals, **all**
`skipped:stale`, `entry_order_id` empty on every row; Congress×DPI 1,693
signals, none executed. Nothing in this repo's ledger came from either of them.

- **Gov contracts** — DoD contract awards $200M–$1B to public defense/IT primes,
  T+1 entry, 7d hold.
  - Earlier backtest figures published here were **SPY-hedged α +48%/yr
    (IR 2.23)** and **ITA-hedged α +29%/yr (IR 1.56)**. Those describe an
    all-agency, T+0 configuration. The configuration actually deployed is
    DoD-only at T+1, which measures **IR 0.73, n=78, t ≈ 0.93 —
    indistinguishable from zero.** The published figure overstated the deployed
    strategy by ~2.1x and was selected as the best of a roughly 30-cell grid,
    with 78% of the effect in four tickers and all of it in two Septembers.
  - It also cannot fire. USASpending publishes DoD obligations of this size
    **60–180 days after the award**; realized event→signal lag is **median 385
    days** (min 105, max 719) against a 30-day staleness gate. Every signal is
    born already stale. This is a data-publication limit, not a tuning problem.

- **Congress×DPI z≥+2** — cross of congressional purchase disclosures with
  elevated dark-pool activity.
  - The **IR 0.51–0.60** figure carries a **verified look-ahead**:
    `congress_dpi_alpha.py` computes the z-score over `notify_date ± window`,
    so the entry gate can be satisfied by data up to five days *after* the entry
    price. Live evaluation is backward-only, so live ≠ backtest. The
    unconditional control (DPI alone) is **negative, IR −0.15**, and the z
    threshold was retuned 1.0 → 2.0 after seeing results.
  - At the loose threshold the signal is ~95% SPY beta; commit `e97721a`
    records excess-vs-SPY at **−0.07%**.

Both remain running as paper strategies. No claim on this page should be read
as a validated live result.

## Not investment advice

This is a public research ledger. Nothing here is investment advice, an offer to sell securities,
or personalized guidance. Do your own research. Past performance is not indicative of future results.

Signals published under the publisher's exemption to the Investment Advisers Act §202(a)(11)(D).

## Live status

Both paper-traders run under pm2 with 5-minute poll cadence. First trade will appear in `ledger.md`
when a qualifying signal fires from either strategy.
