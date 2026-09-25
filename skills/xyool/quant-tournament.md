# Xyool — Quant Tournament

## Purpose

The Quant Tournament determines **what established quantitative models are actually useful for** before they are allowed to influence Xyool/OSE/CAC.

The tournament is job-specific, point-in-time, cost-aware, and regime-aware.

A model can fail as a standalone alpha model and still survive as a useful risk, sizing, timing, or portfolio-construction model.

---

# 1. Separation Rule

During Tournament 1:

```text
QUANT DATA
   ↓
CANONICAL QUANT MODELS
   ↓
STANDARDIZED SIGNALS
   ↓
TOURNAMENT
   ↓
UTILITY CARDS
```

The tournament does **not** receive Xyool, OSE, or CAC conclusions.

Only after a model earns independent validity do we test whether it improves the fundamental system.

---

# 2. Tournament Leagues

Do not force every model into one leaderboard.

## League A — Alpha / Selection

Questions:
- does the signal rank future returns?
- does top-minus-bottom spread persist?
- does it survive costs?

Typical competitors:
- momentum
- value
- quality
- earnings/event signals
- ownership
- issuance
- liquidity

## League B — Timing / Execution

Questions:
- does it improve entry or exit timing?
- does it reduce chasing?
- does it recognize ignition or deterioration earlier?

Typical competitors:
- trend
- breakout
- short-term reversal
- PEAD

## League C — Statistical / Relative Value

Questions:
- is the residual relationship stable?
- is the spread tradable after costs?
- does the model add information beyond broad factors?

Typical competitors:
- factor residuals
- pairs/cointegration
- PCA residual models

## League D — Volatility / Regime

Questions:
- does the model improve volatility forecasts?
- does it identify hostile or favorable market states?
- does conditioning other models on the regime improve results?

Typical competitors:
- realized volatility
- EWMA
- GARCH
- Markov switching
- breadth
- correlation/dispersion

## League E — Risk / Portfolio Construction

Questions:
- does the allocator improve geometric return?
- does it reduce max drawdown?
- does it reduce concentration and recovery time?

Typical competitors:
- volatility targeting
- inverse volatility
- risk parity / ERC
- minimum variance
- mean-variance
- Black-Litterman
- HRP/HERC/NCO
- CVaR/CDaR
- fractional Kelly

---

# 3. Required Test Universe

Every result must record the exact universe.

Preferred staged universes:

```text
U1 — LIQUID LARGE/MID-CAP US EQUITIES
U2 — BROAD US EQUITIES
U3 — SMALL-CAP / MICROCAP US EQUITIES
U4 — XYOOL-STYLE SMALL-CAP OPPORTUNITY UNIVERSE
U5 — ETFs / CROSS-ASSET BENCHMARKS
```

A model that works in U1 is not assumed to work in U3/U4.

Liquidity and transaction-cost sensitivity become much more important as market capitalization falls.

---

# 4. Tournament Rounds

## Round 0 — Feasibility Gate

A model must have:
- canonical definition
- required data identified
- point-in-time timestamps
- reproducible calculation
- defined universe
- defined rebalance/holding horizon
- transaction-cost model
- known failure modes

Data state must be D3 for the tested universe.

Failure → HOLD FOR DATA / REJECT FROM CURRENT TOURNAMENT.

---

## Round 1 — Canonical Baseline

Test the canonical model with no optimization.

Record:
- CAGR / total return where applicable
- forward-return spread
- information coefficient
- rank IC
- hit rate
- volatility
- max drawdown
- Sharpe
- Sortino
- Calmar
- turnover
- slippage sensitivity
- recovery time

Purpose:
> Establish whether the original idea contains useful signal in our implementation.

---

## Round 2 — Robustness

Test nearby reasonable specifications.

Examples:

```text
Momentum: 12-1 vs 9-1 vs 6-1
Trend: 200D vs 150D vs multi-horizon
Volatility: 20D vs 60D vs EWMA
```

A model is stronger if a **region of parameters** works than if one exact parameter wins.

Fragility flags:
- sign flips under small parameter changes
- performance dominated by one period
- performance dominated by a few securities
- extreme dependence on one rebalance date

---

## Round 3 — Out-of-Sample / Walk-Forward

Preferred process:

```text
DESIGN WINDOW
   ↓
VALIDATION WINDOW
   ↓
LOCK MODEL
   ↓
OUT-OF-SAMPLE WINDOW
   ↓
ROLL FORWARD
```

No parameter may be optimized using future information.

Required result:
- in-sample versus out-of-sample degradation

A model that collapses out of sample is downgraded or rejected.

---

## Round 4 — Regime Survival

Test performance by market state.

Minimum regime matrix:

```text
BULL / LOW VOL
BULL / HIGH VOL
BEAR / LOW VOL
BEAR / HIGH VOL
HIGH DISPERSION
LOW DISPERSION
HIGH CORRELATION
LOW CORRELATION
```

Optional macro regimes:
- rising/falling rates
- liquidity expansion/contraction

Record:
- best regime
- weak regime
- failure regime
- whether regime conditioning improves usefulness

---

## Round 5 — Cost / Liquidity Stress

Stress:
- commissions
- spread
- slippage
- delayed execution
- turnover
- minimum dollar volume
- position size / capacity
- borrow availability for short strategies

Small-cap tests should include harsher slippage assumptions than liquid large-cap tests.

A paper alpha that disappears under realistic costs is not useful.

---

## Round 6 — Independence / Redundancy

Measure:
- signal correlation
- return correlation
- rank correlation
- incremental IC
- incremental return after controls
- common factor exposure

Group models by family before consensus.

Example:

```text
12-1 MOMENTUM
6-1 MOMENTUM
MOVING-AVERAGE TREND
BREAKOUT
```

may represent one persistence family rather than four independent votes.

Redundant models can survive as robustness checks, but not receive full independent weight.

---

## Round 7 — Job Utility

Each model is tested for the actual jobs it could perform.

Possible utility scores are maintained separately:

```text
DISCOVERY UTILITY
SELECTION UTILITY
TIMING UTILITY
CONFIRMATION UTILITY
RISK-CONTROL UTILITY
SIZING UTILITY
ROTATION UTILITY
EXECUTION UTILITY
REGIME UTILITY
PORTFOLIO UTILITY
```

Do not average these into one opaque master score.

---

## Round 8 — Fundamental-System Challenge

Only models that survive independent testing reach this round.

Test portfolios/workflows:

1. Quant only
2. Xyool/OSE/CAC only
3. Xyool + Quant agreement filter
4. Xyool + Quant risk overlay
5. Xyool + Quant timing overlay
6. Xyool + Quant rotation confirmation
7. Xyool + independent optimized Quant overlay

Primary question:

> **Does Quant add information or risk control that improves compounded capital beyond Xyool/OSE/CAC alone?**

---

# 5. Standard Tournament Result

```text
TOURNAMENT RESULT

Model ID:
Model:
Class:
Family:
Version:
Universe:
Sample Period:
Out-of-Sample Period:
Rebalance:
Holding Horizon:
Data State:

RETURN METRICS
CAGR:
Total Return:
Average Forward Return:
Median Forward Return:
Top-Bottom Spread:
Hit Rate:

RISK METRICS
Volatility:
Max Drawdown:
Downside Deviation:
Worst Rolling Period:
Recovery Time:

RISK-ADJUSTED
Sharpe:
Sortino:
Calmar:

SIGNAL QUALITY
IC:
Rank IC:
Monotonicity:
Signal Decay:

TRADING REALITY
Turnover:
Estimated Cost:
Slippage Stress:
Capacity:
Liquidity Requirement:

ROBUSTNESS
Parameter Robustness:
Subperiod Robustness:
Regime Robustness:
Out-of-Sample Survival:

INDEPENDENCE
Family Correlation:
Incremental IC:
Incremental Return:

UTILITY
Best Job:
Secondary Jobs:
Weak Jobs:

STATUS:
REJECT / RESEARCH / USE / CORE
```

---

# 6. Promotion Rules

## REJECT

Use when one or more are true:
- no reproducible signal
- fails out of sample
- cost destroys usefulness
- excessive fragility
- unstable economic relationship
- redundant with a stronger simpler model

## RESEARCH

Use when:
- evidence is promising but incomplete
- data is insufficient
- performance is highly regime dependent
- implementation requires additional controls

## USE

Use when:
- robust for at least one defined job
- survives costs
- survives reasonable parameter variation
- has documented failure regime
- provides practical economic utility

## CORE

Use only when:
- strong out-of-sample robustness
- useful across multiple periods/regimes or exceptionally valuable in a clearly identifiable regime
- implementation is simple enough to trust
- failure behavior is understood
- contribution is materially incremental

CORE should be rare.

---

# 7. Tournament Scoreboards

Maintain separate scoreboards rather than one ranking.

```text
ALPHA LEADERBOARD
TIMING LEADERBOARD
RISK LEADERBOARD
REGIME LEADERBOARD
PORTFOLIO LEADERBOARD
```

Example:

```text
MODEL                  ALPHA   TIMING   RISK   PORTFOLIO
12-1 Momentum          High    Med      Low    —
Short Reversal         Low     High     Low    —
GARCH                   —       —      High    —
HRP                     —       —      Med    High
```

The tournament asks **where a method belongs**, not merely whether it wins overall.

---

# 8. Benchmark Stack

Every strategy must be compared against appropriate simple baselines.

Minimum benchmarks:

```text
BUY & HOLD
EQUAL WEIGHT
MARKET-CAP WEIGHT
EQUAL-WEIGHT REBALANCED
INVERSE VOLATILITY
SIMPLE 12-1 MOMENTUM
SIMPLE 200-DAY TREND
```

Portfolio optimizers must beat simpler risk-aware baselines after costs to justify their complexity.

---

# 9. Anti-Overfit Rules

1. canonical model first
2. few parameters
3. no look-ahead
4. no survivorship bias
5. publication lags respected
6. delisted securities included where possible
7. realistic costs
8. point-in-time universe
9. broad parameter robustness preferred
10. no model enters CORE from in-sample performance alone
11. complexity requires incremental value
12. every model must have a failure-mode document

---

# 10. Model Family Consensus

Consensus is calculated in two stages.

## Stage 1 — Within-Family Consensus

Example:

```text
PRICE PERSISTENCE
  12-1 Momentum
  6-1 Momentum
  Trend
  Breakout
        ↓
PERSISTENCE FAMILY STATE
```

## Stage 2 — Across Independent Families

```text
PERSISTENCE
QUALITY
VALUE
EVENT
OWNERSHIP
REGIME
RISK
        ↓
INDEPENDENT QUANT EVIDENCE
```

This prevents four versions of momentum from masquerading as four independent signals.

---

# 11. Utility Card

Every surviving model receives:

```text
QUANT UTILITY CARD

Model ID:
Model:
Family:
Status: RESEARCH / USE / CORE
Standalone Alpha: Weak / Moderate / Strong
Risk Reduction: Weak / Moderate / Strong
Best Job:
Secondary Jobs:
Weak Jobs:
Best Regime:
Failure Regime:
Signal Horizon:
Turnover:
Capacity:
Cost Sensitivity:
Data Quality:
Independent of Other Quant Families?:
Correlation to Xyool:
Incremental Value to Xyool:
Confidence:
Last Validation Date:
Next Revalidation Trigger:
```

---

# 12. Revalidation

A model that worked historically is not permanently trusted.

Revalidate when:
- enough new observations accumulate
- live performance materially deviates from expected behavior
- market microstructure changes
- costs/liquidity change
- data source changes
- model's known failure regime appears

State flow:

```text
CORE / USE
   ↓
NEW EVIDENCE
   ↓
EXPECTED OR ABNORMAL?
   ↓
MAINTAIN / DOWNGRADE / RESEARCH / REJECT
```

---

# 13. Tournament 1 Starting Order

To minimize infrastructure complexity, implement in waves.

## Wave 1 — Price / Risk Foundation

1. A01 12-1 Momentum
2. A04 Time-Series Momentum
3. A05 Moving-Average Trend
4. A07 Short-Term Reversal
5. A21 Low Volatility
6. V01 Realized Volatility
7. V02 EWMA Volatility
8. P01 Volatility Targeting
9. P02 Inverse Volatility

## Wave 2 — Fundamental Factors

10. A08 Value Composite
11. A09 Gross Profitability
12. A10 Quality Composite
13. A12 Investment / Asset Growth
14. A13 Accruals
15. A19 Net Issuance / Dilution

## Wave 3 — Event / Recognition

16. A14 Earnings Surprise
17. A15 PEAD
18. A16 Insider Accumulation
19. A17 Institutional Accumulation
20. A18 Activist / Beneficial Ownership

## Wave 4 — Statistical / Regime

21. S01 CAPM Residual
22. S03 FF5 Attribution
23. S05 Pairs / Cointegration
24. S06 PCA Residual Stat Arb
25. V03 GARCH(1,1)
26. V06 Markov Regime Switching
27. V07 Breadth Regime
28. V08 Correlation / Dispersion Regime

## Wave 5 — Portfolio Tournament

29. P03 Risk Parity / ERC
30. P04 Minimum Variance
31. P05 Mean-Variance / Max Sharpe
32. P06 Black-Litterman
33. P07 HRP
34. P08 HERC
35. P09 NCO
36. P10 CVaR
37. P11 CDaR
38. P12 Fractional Kelly

This order is implementation order, not expected performance rank.

---

# 14. Final Principle

The Quant Layer wins only if it improves the system's real objective:

> **CAPITAL COMPOUNDING THROUGH OPPORTUNITY ROTATION**

Therefore the final question is not:

> Which quant model has the highest backtest return?

It is:

> **Which quant methods improve discovery, selection, timing, survival, sizing, rotation, or portfolio construction enough to increase robust geometric capital growth after costs?**
