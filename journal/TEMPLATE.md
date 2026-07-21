---
ticker: XYZ
direction: long          # long | short
broker: fidelity         # fidelity | alpaca-paper | tradestation | tastytrade
entry_ref: 25.30         # planned entry price at write time
r_risked_usd: 200        # dollar risk if stop hits (entry - stop) * qty
stop: 24.50
target: 27.00
gut_confidence: 7        # 1-10
setup: range-breakout-vol-dryup    # from SETUP_TAXONOMY.md, or a new name (then add it)
emotional_state: calm    # calm | anxious | fomo | revenge | tired | curious
discovery_source: fidelity-scan    # fidelity-scan | hot-list | news | friend | learning | curiosity
---

## Pre-trade thesis

<2-4 sentences on why you expect price to go your direction. Be specific
about the FEATURES you noticed, not the outcome you want. E.g.
"tightening 5-day range on declining volume with sector-relative
strength; suggests accumulation into breakout." Not "I think it'll pop.">

## Ignored warning voice

<What felt off? Any hesitation you're overriding? Write "none" if truly
none — but be honest. This field is the anti-hindsight-bias fix.>

## Alternatives dismissed

<What OTHER interpretation could this price action be? Why are you
dismissing it? Written pre-trade, this catches self-deception.>

## Exit plan

<Why this stop, why this target. R:R ratio. Time-stop if any.>

---

_Populated after outcome via `close.py`:_

- **outcome_r_multiple:** <_e.g. +2.3R, -1.0R, +0.5R (scratch)_>
- **fill_entry:** <_actual entry from broker_>
- **fill_exit:** <_actual exit from broker_>
- **held_hours:** <_wall-clock hours from entry to exit_>
- **post_mortem:** <_1-2 sentences: what actually happened; did the thesis play out; did the warning voice, if any, prove predictive?_>
