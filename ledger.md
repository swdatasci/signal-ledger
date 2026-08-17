# Signal Ledger — @research_signal

Append-only. Every row is one event, most-recent-first.
Timestamps in UTC. All entries are **paper trades** unless explicitly flagged `[REAL CAPITAL]`.

Format: `YYYY-MM-DD HH:MM UTC | [strategy] | [action] | ticker | notes`

## Events

2026-08-17 16:54 UTC | llm-trader      | BUY      | NVDA   | conf=7 entry=128.9 target=134.2 init_stop=127.15 (min(atr=6.880×2.5=17.20, 0.33×upside=1.75))
2026-08-17 16:54 UTC | llm-trader      | BUY      | JPM    | conf=6 entry=198.45 target=203.75 init_stop=196.7 (min(atr=5.815×2.5=14.54, 0.33×upside=1.75))
2026-08-17 13:06 UTC | live-signal      | LONG-B   | MONDAYxBULL | DO: BUY SPY at open (favor a gap-down open — the ideal setup), SELL at close. Expected ~+0.22%. | conf=high exp=+0.22% hit=56% t=+8.7
2026-08-14 16:34 UTC | intraday-reversion | BUY      | UNP    | O=298.05 entry=296.47 target=298.05 trail=$9.28
2026-08-14 15:23 UTC | llm-trader      | BUY      | NVDA   | conf=7 entry=134.25 target=138.9 init_stop=132.72 (min(atr=7.055×2.5=17.64, 0.33×upside=1.53))
2026-08-14 15:22 UTC | llm-trader      | BUY      | JPM    | conf=6 entry=218.5 target=223.75 init_stop=216.77 (min(atr=6.040×2.5=15.10, 0.33×upside=1.73))
2026-08-14 14:52 UTC | intraday-reversion | BUY      | BA     | O=231.63 entry=230.63 target=231.63 trail=$5.16
2026-08-14 13:08 UTC | live-signal      | LONG-B   | FRIDAYxBULL | DO: BUY SPY at open, SELL at close. Expected ~+0.31%. | conf=high exp=+0.31% hit=59% t=+9.6
2026-08-13 17:36 UTC | llm-trader      | BUY      | UNH    | conf=6 entry=542.1 target=579.0 init_stop=529.92 (min(atr=10.668×2.5=26.67, 0.33×upside=12.18))
2026-08-13 17:35 UTC | llm-trader      | BUY      | JPM    | conf=6 entry=218.75 target=234.5 init_stop=213.55 (min(atr=6.165×2.5=15.41, 0.33×upside=5.20))
2026-08-13 17:35 UTC | llm-trader      | BUY      | NVDA   | conf=7 entry=138.5 target=147.2 init_stop=135.63 (min(atr=7.243×2.5=18.11, 0.33×upside=2.87))
2026-08-13 17:30 UTC | live-signal      | LONG-1   | INTC   | DO: LONG-1 INTC | conf=medium exp=+0.19% hit=53% t=+2.4
2026-08-13 16:31 UTC | llm-trader      | BUY      | NVDA   | conf=7 entry=862.3 target=910.0 init_stop=846.56 (min(atr=7.243×2.5=18.11, 0.33×upside=15.74))
2026-08-13 16:31 UTC | llm-trader      | BUY      | JPM    | conf=6 entry=198.5 target=204.75 init_stop=196.44 (min(atr=6.165×2.5=15.41, 0.33×upside=2.06))
2026-08-13 16:03 UTC | intraday-reversion | BUY      | AMZN   | O=267.24 entry=265.86 target=267.24 trail=$7.68
2026-08-13 15:24 UTC | intraday-reversion | BUY      | ABBV   | O=252.94 entry=250.97 target=252.94 trail=$9.44
2026-08-13 14:25 UTC | llm-trader      | BUY      | NVDA   | conf=7 entry=128.3 target=134.9 init_stop=126.12 (min(atr=7.216×2.5=18.04, 0.33×upside=2.18))
2026-08-13 14:24 UTC | llm-trader      | BUY      | JPM    | conf=6 entry=198.5 target=204.7 init_stop=196.45 (min(atr=6.143×2.5=15.36, 0.33×upside=2.05))
2026-08-13 13:31 UTC | live-signal      | LONG-B   | ORCL   | DO: LONG-B ORCL | conf=high exp=+3.35% hit=59% t=+4.3
2026-08-13 13:31 UTC | live-signal      | LONG-B   | INTC   | DO: LONG-B INTC | conf=high exp=+3.15% hit=61% t=+7.2
2026-08-12 14:05 UTC | intraday-reversion | BUY      | V      | O=361.0 entry=360.05 target=361.0 trail=$9.4
2026-08-12 13:31 UTC | live-signal      | LONG-B   | INTC   | DO: LONG-B INTC | conf=high exp=+3.15% hit=61% t=+7.2
2026-08-11 15:09 UTC | intraday-reversion | BUY      | BA     | O=235.61 entry=234.19 target=235.61 trail=$6.0
2026-08-11 14:31 UTC | intraday-reversion | BUY      | JNJ    | O=261.23 entry=259.23 target=261.23 trail=$11.68
2026-08-11 14:21 UTC | intraday-reversion | BUY      | HON    | O=242.32 entry=241.57 target=242.32 trail=$9.96
2026-08-11 13:37 UTC | llm-trader      | BUY      | JPM    | conf=5 entry=218.3 target=246.9 init_stop=208.86 (min(atr=6.448×2.5=16.12, 0.33×upside=9.44))
2026-08-11 13:37 UTC | llm-trader      | BUY      | NVDA   | conf=6 entry=138.45 target=147.9 init_stop=135.33 (min(atr=7.451×2.5=18.63, 0.33×upside=3.12))
2026-08-11 13:31 UTC | live-signal      | LONG-B   | INTC   | DO: LONG-B INTC | conf=high exp=+2.77% hit=60% t=+6.2
2026-08-10 15:43 UTC | intraday-reversion | BUY      | AVGO   | O=427.53 entry=425.81 target=427.53 trail=$10.68
2026-08-10 14:12 UTC | intraday-reversion | BUY      | V      | O=362.0 entry=359.76 target=362.0 trail=$8.68
2026-08-10 13:00 UTC | live-signal      | LONG-B   | MONDAYxBULL | DO: BUY SPY at open (favor a gap-down open — the ideal setup), SELL at close. Expected ~+0.22%. | conf=high exp=+0.22% hit=56% t=+8.7
2026-08-07 15:35 UTC | intraday-reversion | BUY      | GE     | O=374.05 entry=371.88 target=374.05 trail=$8.8
2026-08-07 15:34 UTC | intraday-reversion | BUY      | BA     | O=232.63 entry=231.31 target=232.63 trail=$5.4
2026-08-07 15:03 UTC | llm-trader      | BUY      | NVDA   | conf=7 entry=138.75 target=149.0 init_stop=135.37 (min(atr=7.688×2.5=19.22, 0.33×upside=3.38))
2026-08-07 15:03 UTC | llm-trader      | BUY      | JPM    | conf=6 entry=218.5 target=237.9 init_stop=212.1 (min(atr=7.563×2.5=18.91, 0.33×upside=6.40))
2026-08-07 13:31 UTC | live-signal      | LONG-B   | CRM    | DO: LONG-B CRM | conf=high exp=+2.77% hit=60% t=+6.2
2026-08-07 13:00 UTC | live-signal      | LONG-B   | FRIDAYxBULL | DO: BUY SPY at open, SELL at close. Expected ~+0.31%. | conf=high exp=+0.31% hit=59% t=+9.6
2026-08-06 15:37 UTC | intraday-reversion | BUY      | HON    | O=248.41 entry=242.86 target=248.41 trail=$5.48
2026-08-06 15:34 UTC | intraday-reversion | BUY      | MS     | O=217.5 entry=216.13 target=217.5 trail=$6.68
2026-08-06 15:34 UTC | intraday-reversion | BUY      | GS     | O=1057.02 entry=1049.18 target=1057.02 trail=$44.08
2026-08-06 15:33 UTC | intraday-reversion | BUY      | VZ     | O=47.07 entry=46.71 target=47.07 trail=$1.64
2026-08-06 15:32 UTC | intraday-reversion | BUY      | BA     | O=239.09 entry=234.78 target=239.09 trail=$5.12
2026-08-06 15:20 UTC | intraday-reversion | BUY      | GOOGL  | O=360.96 entry=359.18 target=360.96 trail=$12.68
2026-08-06 14:48 UTC | intraday-reversion | BUY      | GE     | O=383.97 entry=381.29 target=383.97 trail=$19.48
2026-08-06 14:30 UTC | intraday-reversion | BUY      | NVDA   | O=221.53 entry=219.87 target=221.53 trail=$8.4
2026-08-06 14:14 UTC | intraday-reversion | BUY      | AAPL   | O=314.34 entry=313.44 target=314.34 trail=$7.8
2026-08-06 13:31 UTC | live-signal      | LONG-B   | CRM    | DO: LONG-B CRM | conf=high exp=+2.77% hit=60% t=+6.2
2026-08-06 13:31 UTC | live-signal      | LONG-B   | ORCL   | DO: LONG-B ORCL | conf=high exp=+2.77% hit=60% t=+6.2
2026-08-05 15:53 UTC | intraday-reversion | BUY      | NVDA   | O=219.95 entry=219.06 target=219.95 trail=$4.88
2026-08-05 15:52 UTC | intraday-reversion | BUY      | CVX    | O=188.25 entry=186.78 target=188.25 trail=$4.56
2026-08-05 15:49 UTC | intraday-reversion | BUY      | GOOGL  | O=378.79 entry=376.79 target=378.79 trail=$7.68
2026-08-05 15:48 UTC | intraday-reversion | BUY      | XOM    | O=152.28 entry=151.33 target=152.28 trail=$3.4
2026-08-05 15:40 UTC | intraday-reversion | BUY      | CSCO   | O=121.92 entry=121.33 target=121.92 trail=$2.56
2026-08-05 15:35 UTC | intraday-reversion | BUY      | PM     | O=187.03 entry=186.03 target=187.03 trail=$3.88
2026-08-05 15:31 UTC | intraday-reversion | BUY      | AVGO   | O=422.86 entry=419.62 target=422.86 trail=$16.56
2026-08-05 15:30 UTC | llm-trader      | BUY      | NVDA   | conf=7 entry=124.8 target=129.6 init_stop=123.22 (min(atr=8.090×2.5=20.23, 0.33×upside=1.58))
2026-08-05 15:29 UTC | llm-trader      | BUY      | JPM    | conf=6 entry=198.45 target=203.75 init_stop=196.7 (min(atr=7.478×2.5=18.70, 0.33×upside=1.75))
2026-08-05 15:29 UTC | intraday-reversion | BUY      | HON    | O=248.63 entry=246.85 target=248.63 trail=$10.12
2026-08-05 14:12 UTC | intraday-reversion | BUY      | VZ     | O=46.0 entry=45.36 target=46.0 trail=$3.64
2026-08-05 13:31 UTC | live-signal      | LONG-B   | DIS    | DO: LONG-B DIS | conf=high exp=+3.15% hit=61% t=+7.2
2026-08-05 13:31 UTC | live-signal      | LONG-B   | AMD    | DO: LONG-B AMD | conf=high exp=+3.15% hit=61% t=+7.2
2026-08-05 13:31 UTC | live-signal      | LONG-B   | CSCO   | DO: LONG-B CSCO | conf=high exp=+3.15% hit=61% t=+7.2
2026-08-05 13:31 UTC | live-signal      | LONG-B   | LLY    | DO: LONG-B LLY | conf=high exp=+3.35% hit=59% t=+4.3
2026-08-05 13:31 UTC | live-signal      | LONG-B   | T      | DO: LONG-B T | conf=high exp=+2.77% hit=60% t=+6.2
2026-08-04 15:45 UTC | intraday-reversion | BUY      | MRK    | O=128.63 entry=127.63 target=128.63 trail=$4.6
2026-08-04 15:42 UTC | intraday-reversion | BUY      | CSCO   | O=120.97 entry=120.47 target=120.97 trail=$2.68
2026-08-04 15:32 UTC | intraday-reversion | BUY      | ABBV   | O=244.85 entry=243.9 target=244.85 trail=$4.92
2026-08-04 13:31 UTC | live-signal      | LONG-B   | CSCO   | DO: LONG-B CSCO | conf=high exp=+3.15% hit=61% t=+7.2
2026-08-04 13:31 UTC | live-signal      | LONG-B   | QCOM   | DO: LONG-B QCOM | conf=high exp=+3.15% hit=61% t=+7.2
2026-08-04 13:31 UTC | live-signal      | LONG-B   | AMD    | DO: LONG-B AMD | conf=high exp=+3.15% hit=61% t=+7.2
2026-08-04 13:31 UTC | live-signal      | LONG-B   | INTC   | DO: LONG-B INTC | conf=high exp=+3.15% hit=61% t=+7.2
2026-08-04 13:31 UTC | live-signal      | LONG-B   | NKE    | DO: LONG-B NKE | conf=high exp=+2.77% hit=60% t=+6.2
2026-08-04 13:31 UTC | live-signal      | LONG-B   | TXN    | DO: LONG-B TXN | conf=high exp=+3.15% hit=61% t=+7.2
2026-08-04 13:31 UTC | live-signal      | LONG-B   | CAT    | DO: LONG-B CAT | conf=medium exp=+3.35% hit=59% t=+4.3
2026-08-03 15:31 UTC | intraday-reversion | BUY      | MRK    | O=129.44 entry=127.25 target=129.44 trail=$8.12
2026-08-03 15:00 UTC | intraday-reversion | BUY      | V      | O=368.5 entry=366.03 target=368.5 trail=$13.88
2026-08-03 13:31 UTC | live-signal      | LONG-B   | AMD    | DO: LONG-B AMD | conf=high exp=+2.77% hit=60% t=+6.2
2026-08-03 13:31 UTC | live-signal      | LONG-B   | ADBE   | DO: LONG-B ADBE | conf=high exp=+3.15% hit=61% t=+7.2
2026-08-03 13:10 UTC | live-signal      | LONG-B   | MONDAYxBULL | DO: BUY SPY at open (favor a gap-down open — the ideal setup), SELL at close. Expected ~+0.22%. | conf=high exp=+0.22% hit=56% t=+8.7
2026-07-31 17:58 UTC | llm-trader      | BUY      | AMD    | conf=5 entry=172.3 target=184.0 init_stop=168.44 (min(atr=39.680×2.5=99.20, 0.33×upside=3.86))
2026-07-31 17:57 UTC | llm-trader      | BUY      | NVDA   | conf=6 entry=138.5 target=147.9 init_stop=135.4 (min(atr=7.576×2.5=18.94, 0.33×upside=3.10))
2026-07-31 15:51 UTC | llm-trader      | BUY      | NVDA   | conf=7 entry=128.9 target=134.2 init_stop=127.15 (min(atr=7.576×2.5=18.94, 0.33×upside=1.75))
2026-07-31 15:51 UTC | llm-trader      | BUY      | JPM    | conf=6 entry=198.45 target=203.75 init_stop=196.7 (min(atr=7.540×2.5=18.85, 0.33×upside=1.75))
2026-07-31 14:20 UTC | intraday-reversion | BUY      | XOM    | O=153.74 entry=152.39 target=153.74 trail=$6.52
2026-07-31 13:31 UTC | live-signal      | LONG-B   | CAT    | DO: LONG-B CAT | conf=high exp=+3.15% hit=61% t=+7.2
2026-07-31 13:31 UTC | live-signal      | LONG-B   | INTC   | DO: LONG-B INTC | conf=medium exp=+3.35% hit=59% t=+4.3
2026-07-31 13:31 UTC | live-signal      | LONG-B   | AMD    | DO: LONG-B AMD | conf=medium exp=+3.35% hit=59% t=+4.3
2026-07-31 13:31 UTC | live-signal      | LONG-B   | CMCSA  | DO: LONG-B CMCSA | conf=high exp=+2.77% hit=60% t=+6.2
2026-07-31 13:02 UTC | live-signal      | LONG-B   | FRIDAYxBULL | DO: BUY SPY at open, SELL at close. Expected ~+0.31%. | conf=high exp=+0.31% hit=59% t=+9.6
2026-07-31 13:02 UTC | live-signal      | LONG-B   | H12-MONTHEND-LIFT | DO: BUY SPY at open, SELL at close. Universal effect — works in any regime. | conf=high exp=+0.23% hit=55% t=+7.2
2026-07-30 13:32 UTC | live-signal      | LONG-B   | META   | DO: LONG-B META | conf=medium exp=+3.55% hit=59% t=+4.3
2026-07-30 13:32 UTC | live-signal      | LONG-B   | INTC   | DO: LONG-B INTC | conf=medium exp=+3.35% hit=59% t=+4.3
2026-07-30 13:32 UTC | live-signal      | LONG-B   | ORCL   | DO: LONG-B ORCL | conf=high exp=+3.15% hit=61% t=+7.2
2026-07-30 13:32 UTC | live-signal      | LONG-B   | AMD    | DO: LONG-B AMD | conf=medium exp=+3.35% hit=59% t=+4.3
2026-07-30 13:32 UTC | live-signal      | LONG-B   | CMCSA  | DO: LONG-B CMCSA | conf=high exp=+2.77% hit=60% t=+6.2
2026-07-30 13:32 UTC | live-signal      | LONG-B   | CRM    | DO: LONG-B CRM | conf=high exp=+2.77% hit=60% t=+6.2
2026-07-30 13:32 UTC | live-signal      | LONG-B   | ADBE   | DO: LONG-B ADBE | conf=high exp=+2.77% hit=60% t=+6.2
2026-07-30 13:32 UTC | live-signal      | LONG-B   | MSFT   | DO: LONG-B MSFT | conf=medium exp=+3.35% hit=59% t=+4.3
2026-07-30 13:32 UTC | live-signal      | LONG-B   | QCOM   | DO: LONG-B QCOM | conf=medium exp=+3.55% hit=59% t=+4.3
2026-07-30 13:32 UTC | live-signal      | LONG-B   | CAT    | DO: LONG-B CAT | conf=high exp=+3.15% hit=61% t=+7.2
2026-07-30 13:00 UTC | live-signal      | LONG-B   | T-1xBULL | DO: BUY SPY at open, SELL at close. Expected ~+0.18% (smaller than bear-regime version). | conf=medium exp=+0.18% hit=57% t=+3.1
2026-07-30 13:00 UTC | live-signal      | LONG-B   | H12-MONTHEND-LIFT | DO: BUY SPY at open, SELL at close. Universal effect — works in any regime. | conf=high exp=+0.23% hit=55% t=+7.2
2026-07-30 12:54 UTC | live-signal      | LONG-B   | T-1xBULL | DO: BUY SPY at open, SELL at close. Expected ~+0.18% (smaller than bear-regime version). | conf=medium exp=+0.18% hit=57% t=+3.1
2026-07-30 12:54 UTC | live-signal      | LONG-B   | H12-MONTHEND-LIFT | DO: BUY SPY at open, SELL at close. Universal effect — works in any regime. | conf=high exp=+0.23% hit=55% t=+7.2
2026-07-29 13:51 UTC | llm-trader      | BUY      | NVDA   | conf=7 entry=128.3 target=134.9 init_stop=126.12 (min(atr=7.254×2.5=18.13, 0.33×upside=2.18))
2026-07-29 13:51 UTC | llm-trader      | BUY      | JPM    | conf=6 entry=198.5 target=204.75 init_stop=196.44 (min(atr=7.082×2.5=17.70, 0.33×upside=2.06))
2026-07-29 13:31 UTC | live-signal      | LONG-B   | QCOM   | DO: LONG-B QCOM | conf=high exp=+2.77% hit=60% t=+6.2
2026-07-29 13:31 UTC | live-signal      | LONG-B   | UPS    | DO: LONG-B UPS | conf=high exp=+2.77% hit=60% t=+6.2
2026-07-28 13:31 UTC | live-signal      | LONG-B   | QCOM   | mean=+2.77% t=+6.2 hit=60% conf=high regime='Universal (mega-cap universe 2020-2024)'
2026-07-28 13:31 UTC | live-signal      | LONG-B   | CVX    | mean=+2.77% t=+6.2 hit=60% conf=high regime='Universal (mega-cap universe 2020-2024)'
2026-07-28 13:31 UTC | live-signal      | LONG-B   | INTC   | mean=+3.55% t=+4.3 hit=59% conf=medium regime='Universal (mega-cap universe 2020-2024)'
2026-07-28 01:43 UTC | calendar        | LONG-B   | MONDAY | mean=+0.08% t=+4.2 hit=53% conf=medium regime='Universe-wide'
2026-07-27 19:10 UTC | llm-trader      | BUY      | DIS    | conf=6 entry=96.59 stop=94.0 target=102.0
2026-07-27 19:10 UTC | llm-trader      | BUY      | TGT    | conf=7 entry=140.22 stop=138.5 target=146.0
2026-07-27 19:10 UTC | llm-trader      | BUY      | MCD    | conf=7 entry=270.54 stop=268.0 target=279.0
2026-07-27 17:04 UTC | llm-trader      | BUY      | DHR    | conf=6 entry=194.26 stop=187.0 target=205.32
2026-07-27 17:03 UTC | llm-trader      | BUY      | DASH   | conf=7 entry=184.5 stop=176.29 target=200.3
2026-07-27 17:03 UTC | llm-trader      | BUY      | ADSK   | conf=7 entry=224.59 stop=212.0 target=248.79
2026-07-27 14:55 UTC | llm-trader      | BUY      | VZ     | conf=5 entry=47.18 stop=46.32 target=50.9
2026-07-27 14:54 UTC | llm-trader      | BUY      | MSFT   | conf=6 entry=389.6 stop=385.2 target=417.0
2026-07-24 19:44 UTC | llm-trader      | BUY      | AMZN   | conf=7 entry=232.04 stop=225.0 target=268.0
2026-07-24 19:44 UTC | llm-trader      | BUY      | AVGO   | conf=6 entry=379.96 stop=368.0 target=425.0
2026-07-24 19:44 UTC | llm-trader      | BUY      | AMD    | conf=7 entry=521.23 stop=498.0 target=625.0
2026-07-24 18:42 UTC | llm-trader      | BUY      | CTSH   | conf=6 entry=45.16 stop=43.2 target=50.8
2026-07-24 18:42 UTC | llm-trader      | BUY      | ADBE   | conf=7 entry=225.39 stop=216.0 target=248.0
2026-07-24 18:42 UTC | llm-trader      | BUY      | ACN    | conf=7 entry=146.42 stop=140.75 target=158.0
2026-07-24 16:34 UTC | llm-trader      | BUY      | WDAY   | conf=7 entry=134.0 stop=129.5 target=146.0
2026-07-24 16:33 UTC | llm-trader      | BUY      | TMUS   | conf=6 entry=178.5 stop=174.0 target=192.0
2026-07-24 16:33 UTC | llm-trader      | BUY      | ABNB   | conf=6 entry=142.0 stop=139.5 target=147.5
2026-07-24 14:24 UTC | llm-trader      | BUY      | VZ     | conf=6 entry=45.0 stop=43.7 target=48.1
2026-07-24 14:24 UTC | llm-trader      | BUY      | AAPL   | conf=8 entry=328.0 stop=321.5 target=346.0
2026-07-23 15:49 UTC | intraday-reversion | BUY      | CMCSA  | O=23.29 entry=22.952 target=23.29 stop=22.9
2026-07-23 15:44 UTC | intraday-reversion | BUY      | CSCO   | O=113.14 entry=112.54 target=113.14 stop=112.0
2026-07-23 15:39 UTC | intraday-reversion | BUY      | UNP    | O=312.02 entry=307.36 target=312.02 stop=306.065
2026-07-23 15:39 UTC | intraday-reversion | BUY      | INTC   | O=102.25 entry=100.89 target=102.25 stop=100.0
2026-07-23 15:39 UTC | intraday-reversion | BUY      | CRM    | O=159.38 entry=156.585 target=159.38 stop=156.155
2026-07-23 15:38 UTC | intraday-reversion | BUY      | AMD    | O=551.72 entry=545.519 target=551.72 stop=544.565
2026-07-23 15:38 UTC | intraday-reversion | BUY      | ADBE   | O=215.81 entry=213.4 target=215.81 stop=211.565
2026-07-23 15:34 UTC | intraday-reversion | BUY      | BA     | O=209.11 entry=207.17 target=209.11 stop=205.9
2026-07-23 15:32 UTC | intraday-reversion | BUY      | ORCL   | O=122.16 entry=119.89 target=122.16 stop=118.35
2026-07-23 15:31 UTC | intraday-reversion | BUY      | NKE    | O=41.71 entry=41.229 target=41.71 stop=41.155
2026-07-23 15:31 UTC | intraday-reversion | BUY      | MSFT   | O=388.67 entry=384.627 target=388.67 stop=384.005
2026-07-23 15:27 UTC | intraday-reversion | BUY      | AVGO   | O=392.12 entry=388.04 target=392.12 stop=383.885
2026-07-23 15:25 UTC | intraday-reversion | BUY      | BLK    | O=1051.15 entry=1043.52 target=1051.15 stop=1035.73
2026-07-23 14:27 UTC | intraday-reversion | BUY      | META   | O=608.71 entry=604.51 target=608.71 stop=599.8
2026-07-23 14:25 UTC | llm-trader      | BUY      | META   | conf=5 entry=608.5 stop=592.3 target=647.1
2026-07-23 14:25 UTC | llm-trader      | BUY      | MSFT   | conf=6 entry=389.0 stop=375.6 target=412.0
2026-07-23 14:25 UTC | intraday-reversion | BUY      | WMT    | O=107.51 entry=106.83 target=107.51 stop=106.43
2026-07-23 14:10 UTC | intraday-reversion | BUY      | GOOGL  | O=321.13 entry=318.6 target=321.13 stop=316.09
2026-07-23 14:09 UTC | intraday-reversion | BUY      | NVDA   | O=209.46 entry=208.47 target=209.46 stop=207.345
2026-07-23 14:09 UTC | intraday-reversion | BUY      | AMZN   | O=236.37 entry=234.73 target=236.37 stop=233.4
2026-07-23 14:01 UTC | intraday-reversion | BUY      | UNH    | O=428.27 entry=425.8 target=428.27 stop=424.94
2026-07-22 19:22 UTC | llm-trader      | BUY      | MRVL   | conf=6 entry=213.08 stop=207.68 target=225.49
2026-07-22 19:21 UTC | llm-trader      | BUY      | AMD    | conf=7 entry=561.07 stop=548.29 target=593.17
2026-07-22 17:13 UTC | llm-trader      | BUY      | AMT    | conf=7 entry=166.035 stop=162.0 target=184.0
2026-07-22 17:13 UTC | llm-trader      | BUY      | ADI    | conf=6 entry=387.49 stop=375.0 target=416.0
2026-07-22 17:12 UTC | llm-trader      | BUY      | AMAT   | conf=7 entry=560.05 stop=542.0 target=593.0
2026-07-22 16:08 UTC | llm-trader      | BUY      | AVGO   | conf=6 entry=393.0 stop=375.0 target=462.0
2026-07-22 16:08 UTC | llm-trader      | BUY      | MRVL   | conf=7 entry=214.0 stop=200.58 target=273.69
2026-07-22 16:07 UTC | llm-trader      | BUY      | AMD    | conf=7 entry=548.0 stop=526.0 target=617.0
2026-07-21 19:55 UTC | llm-trader      | BUY      | TSLA   | conf=7 entry=377.4 stop=365.0 target=402.0
2026-07-21 19:55 UTC | llm-trader      | BUY      | AAPL   | conf=8 entry=327.71 stop=319.0 target=345.0
2026-07-20 02:07 UTC | setup           | INIT     | GO     | Ledger wired live. Congress×DPI z≥+2 and gov-contracts DoD $200M-$1B both running under pm2. Next event = first fresh signal from either strategy.
