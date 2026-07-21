---
title: Trader Journal — pre-registered
---

# Trader Journal

Pre-registered public trade log. Every entry is written **before** the trade
is submitted at the broker. The git commit timestamp is the tamper-evident
proof of pre-registration; monthly broker exports prove the fill sequence.

**This is not investment advice.** These are one trader's own trades,
published as a discipline mechanism and a public track record.

## Why this exists

Two problems in retail discretionary trading:

1. **Hindsight bias.** After a win, memory reconstructs the pre-trade state
   as cleaner than it was. After a loss, memory manufactures a "warning
   voice" that may never have existed. Post-hoc journals inherit both
   distortions.
2. **No reverse-engineerable data.** Without a pre-registered record, you
   cannot distinguish real intuition from hindsight, or count which setups
   actually work versus which just feel good.

Pre-registered entries solve both. See Kahneman & Klein (2009),
"Conditions for Intuitive Expertise" — expert intuition is validate-able
only when captured before the outcome arrives.

## Layout

```
journal/
├── README.md                   # this file
├── TEMPLATE.md                 # copy-paste template with all fields
├── SETUP_TAXONOMY.md           # named setup catalog (grows over time)
├── new.py                      # interactive script — writes an entry in <60s
├── close.py                    # attach outcome to an existing entry
├── 2026/                       # entries organized by year/month
│   └── 07/
│       └── 20260721-1447-XYZ-long.md
└── fidelity-exports/           # monthly broker CSVs — proves fill sequence
    └── 2026-07.csv
```

## Workflow

**Before entering a trade:**

```bash
cd ~/caelum/signal-ledger/journal
uv run python new.py
# fills prompts: ticker, direction, r_risked, stop, target,
# gut_confidence, setup name, thesis, ignored warning, emotional state
# writes markdown file + git commit + git push
# under 60 seconds if you know the answers
```

Then submit the actual order at the broker. Git commit timestamp precedes
the broker fill timestamp — auditable proof.

**Monthly** (or before any "prove-it" event):

```bash
# export Fidelity trade history CSV → save as fidelity-exports/YYYY-MM.csv
# git commit + push
uv run python close.py   # walks unsettled entries, attaches outcomes
```

## Schema

All fields in [TEMPLATE.md](./TEMPLATE.md). Required minimum:

- `ticker`, `direction`, `broker`, `r_risked_usd`, `stop`, `gut_confidence` (1-10)
- Pre-trade thesis (2-4 sentences)
- Ignored warning voice (or explicit "none")

Optional but valuable:

- Setup name (from [SETUP_TAXONOMY.md](./SETUP_TAXONOMY.md); grows)
- Alternatives dismissed (why)
- Emotional state (calm / anxious / fomo / revenge / tired)

## Attribution

Author: [@sqwrell](https://github.com/swdatasci) / research@swdatasci.com
