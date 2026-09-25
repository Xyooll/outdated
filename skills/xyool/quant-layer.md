# Xyool — Independent Quant Layer

## Purpose

The Quant Layer is a **separate analytical system** from Company-Level Xyool, the Opportunity State Engine (OSE), and the Capital Allocation Controller (CAC).

Its purpose is not to replace fundamental reasoning.

Its purpose is to answer:

> **Can established quantitative models provide useful independent information about selection, timing, risk, sizing, regime, or rotation?**

The Quant Layer should initially operate without access to Xyool conclusions so that its incremental value can be measured honestly.

---

## Core Separation Rule

```text
FUNDAMENTAL SYSTEM                         QUANT SYSTEM

Company-Level Xyool                       Quant Data
        ↓                                      ↓
Opportunity State Engine                  Quant Models
        ↓                                      ↓
Capital Allocation Controller             Signal Standardization
                                               ↓
                                          Model Tournament
```

Only after independent testing should the systems be compared or fused.

Do not allow a quant signal to inherit confidence merely because Xyool agrees with it.
Do not allow Xyool to inherit confidence merely because a quant model agrees with it.

Agreement is useful only after each system has earned independent validity.

---

# 1. Quant Layer Objective

The Quant Layer should determine whether quantitative models improve any of the following:

1. **Discovery** — finding candidates before fundamental review.
2. **Selection** — distinguishing stronger from weaker opportunities.
3. **Timing** — identifying when a thesis may begin moving.
4. **Confirmation** — determining whether price/volume behavior supports the thesis.
5. **Risk control** — detecting deterioration or hostile market conditions.
6. **Position sizing** — scaling exposure to volatility and conviction.
7. **Rotation** — determining when capital has a better quantitative destination.
8. **Execution** — improving entry/exit implementation.
9. **Regime awareness** — determining which models currently deserve weight.

The system must measure **economic usefulness**, not merely predictive accuracy.

---

# 2. First Model Library

Use well-known model families with long histories in academic research and professional quantitative investing.

These models should be implemented transparently before adding machine learning or proprietary complexity.

## Q1 — Cross-Sectional Momentum

Core idea:

> Assets that have outperformed peers over an intermediate horizon often continue outperforming for some period.

Canonical measurements may include:
- 12-1 month momentum
- 6-1 month momentum
- 3-month momentum
- residual momentum
- sector-relative momentum

Potential Xyool usefulness:
- discovery
- recognition acceleration
- rotation comparison
- avoiding persistent relative weakness

Do not confuse short-term price spikes with durable momentum.

---

## Q2 — Time-Series Momentum / Trend Following

Core idea:

> An asset's own past direction can contain information about its future directional persistence.

Possible implementations:
- moving-average trend
- breakout systems
- multi-horizon trend
- sign of trailing return
- volatility-scaled trend

Potential Xyool usefulness:
- ignition timing
- trend confirmation
- exit/risk control
- determining whether recognition has begun

---

## Q3 — Value

Core idea:

> Cheap assets relative to fundamental anchors may outperform expensive assets over long horizons.

Possible measurements:
- earnings yield
- FCF yield
- book-to-market where economically appropriate
- EV/EBIT
- EV/EBITDA
- sales yield for early-stage firms only with strong caveats
- industry-relative valuation

Potential Xyool usefulness:
- recognition-gap validation
- avoiding overpayment
- identifying asymmetric entry points

Value must not be used without quality and deterioration controls because cheap assets can remain cheap for valid reasons.

---

## Q4 — Quality / Profitability

Core idea:

> Companies with stronger profitability, balance sheets, cash conversion, and operating quality tend to have superior long-run characteristics.

Possible measurements:
- gross profitability
- ROIC / ROA / ROE where appropriate
- operating margin
- FCF margin
- accruals
- earnings stability
- leverage
- interest coverage
- asset growth discipline

Potential Xyool usefulness:
- confirmation of economic trajectory
- shareholder-capture validation
- filtering weak bottleneck stories
- identifying durable compounders

---

## Q5 — Low Volatility / Defensive

Core idea:

> Lower-volatility and lower-beta assets have historically delivered surprisingly strong risk-adjusted returns in many markets.

Possible measurements:
- realized volatility
- beta
- downside deviation
- maximum drawdown
- idiosyncratic volatility

Potential Xyool usefulness:
- position sizing
- portfolio construction
- capital preservation
- identifying when an attractive thesis carries excessive path risk

This is primarily a risk and allocation model rather than a discovery engine.

---

## Q6 — Short-Term Mean Reversion

Core idea:

> Extreme short-horizon price moves can partially reverse.

Possible measurements:
- 1-day reversal
- 5-day reversal
- distance from short moving average
- RSI-type normalized stretch measures
- residual reversal after market/sector adjustment

Potential Xyool usefulness:
- entry execution
- avoiding chasing
- adding to validated opportunities after temporary dislocations

This model must remain separate from medium-term momentum because the two operate on different horizons.

---

## Q7 — Statistical Arbitrage / Pairs

Core idea:

> Relative price relationships among economically linked securities can temporarily deviate from historical equilibrium.

Possible implementations:
- pairs trading
- cointegration
- sector-neutral residuals
- factor-neutral residual mean reversion

Potential Xyool usefulness:
- relative valuation signals
- peer dislocation detection
- hedged exposure
- identifying company-specific versus industry-wide movement

Pairs models require strict liquidity, borrow, transaction-cost, and stability testing.

---

## Q8 — Volatility Targeting

Core idea:

> Position exposure can be adjusted inversely to realized or forecast volatility to stabilize portfolio risk.

Generic form:

```text
Position Scale ∝ Target Volatility / Expected Volatility
```

Potential Xyool usefulness:
- sizing
- drawdown control
- avoiding oversized positions in unstable small caps
- comparing risk-adjusted opportunity across candidates

Volatility targeting should not determine whether a thesis is true.
It determines how aggressively capital can safely express the thesis.

---

## Q9 — Breadth / Market Regime

Core idea:

> The effectiveness and risk of individual signals depend partly on the condition of the broader market.

Possible measurements:
- percentage of universe above moving averages
- advance/decline breadth
- cross-sectional dispersion
- realized market volatility
- credit spreads where available
- yield-curve state
- liquidity conditions
- correlation regime

Potential Xyool usefulness:
- risk-on/risk-off context
- model weighting
- ignition failure detection
- deciding whether idiosyncratic opportunity can overcome hostile market conditions

---

## Q10 — Risk-Parity / Risk-Budget Allocation

Core idea:

> Allocate portfolio risk deliberately rather than allocating equal dollars to assets with radically different risk.

Possible implementations:
- inverse volatility
- equal risk contribution
- covariance-aware risk budgeting

Potential Xyool usefulness:
- portfolio sizing
- concentration control
- maintaining survivability while pursuing asymmetric opportunities

This is an allocation model, not an alpha model.

---

# 3. Optional Second-Wave Models

Only add these after the first library is functioning and benchmarked:

- earnings momentum / estimate revisions
- post-earnings-announcement drift
- liquidity factors
- asset growth / investment factor
- carry
- seasonality
- insider/issuance signals where reliable data exists
- options-implied signals
- volatility risk premium
- factor residual momentum
- cross-asset macro signals
- machine-learning ensembles

Complexity must be earned through demonstrated incremental value.

---

# 4. Standard Quant Signal Object

Every model must output the same schema so models can be compared directly.

```text
QUANT SIGNAL OBJECT

Model:
Model Family:
Asset:
Timestamp:
Universe:
Lookback:
Holding Horizon:
Raw Signal:
Normalized Signal:
Percentile Rank:
Direction: LONG / NEUTRAL / SHORT
Signal Strength:
Signal Velocity: ↑↑ / ↑ / → / ↓ / ↓↓
Expected Horizon:
Expected Volatility:
Liquidity State:
Regime State:
Confidence:
Data Quality:
Transaction-Cost Estimate:
Failure / Invalidation Condition:
Next Update Trigger:
```

No model may communicate through an undocumented discretionary judgment.

---

# 5. Signal Normalization

Models operate on different units and horizons.

Convert them into comparable forms where possible:

- z-score
- percentile rank
- cross-sectional rank
- volatility-adjusted return
- sector-neutral rank
- market-neutral residual

Preserve both:

1. **Raw Signal** — what the model actually calculated.
2. **Normalized Signal** — a comparable representation.

Never discard the raw signal merely because a normalized score exists.

---

# 6. The Quant Tournament

The Quant Tournament determines **what each model is actually useful for**.

Do not assume every respected model belongs in the final system.

Each model competes independently across multiple jobs.

## Tournament Jobs

```text
DISCOVERY
SELECTION
TIMING
CONFIRMATION
RISK CONTROL
POSITION SIZING
ROTATION
EXECUTION
REGIME DETECTION
```

A model can win one job and lose another.

Example:
- momentum may be strong for selection and rotation
- mean reversion may be weak for long-horizon selection but useful for entry execution
- volatility targeting may have little alpha but materially improve drawdown and compounding

---

# 7. Tournament Metrics

Do not rank models by one metric.

Track at minimum:

## Return
- CAGR
- total return
- average forward return after signal
- median forward return
- hit rate

## Risk
- maximum drawdown
- volatility
- downside deviation
- tail loss
- worst rolling period

## Risk-Adjusted
- Sharpe ratio
- Sortino ratio
- Calmar ratio

## Signal Quality
- information coefficient
- rank information coefficient
- top-minus-bottom spread
- monotonicity across signal buckets
- signal decay

## Trading Reality
- turnover
- liquidity requirement
- slippage sensitivity
- transaction-cost sensitivity
- capacity

## Compounding Utility
- capital growth
- drawdown recovery time
- geometric return
- probability of large permanent impairment

The master criterion remains:

> **Does this model improve compounded capital growth after realistic costs and risk?**

---

# 8. Point-in-Time Testing Rules

All tests must prevent false performance.

Required:

1. no look-ahead bias
2. no survivorship bias
3. point-in-time fundamentals
4. historical universe membership where possible
5. delisted securities included where possible
6. realistic publication delays
7. transaction costs
8. slippage
9. liquidity constraints
10. borrow constraints for short models
11. corporate actions handled correctly
12. parameter choices fixed before out-of-sample evaluation

Research and production periods must be separated.

---

# 9. Walk-Forward Validation

Preferred structure:

```text
TRAIN / DESIGN PERIOD
        ↓
VALIDATION PERIOD
        ↓
LOCK MODEL
        ↓
OUT-OF-SAMPLE TEST
        ↓
ROLL FORWARD
```

Do not continuously optimize parameters on the same period used to report performance.

A simple robust model should beat an overfit complex model.

---

# 10. Regime Matrix

Every model should be tested by environment rather than only across the full sample.

Possible regimes:

```text
BULL / LOW VOLATILITY
BULL / HIGH VOLATILITY
BEAR / LOW VOLATILITY
BEAR / HIGH VOLATILITY
HIGH DISPERSION
LOW DISPERSION
RISING RATES
FALLING RATES
LIQUIDITY EXPANSION
LIQUIDITY CONTRACTION
```

For every model record:

```text
Model:
Best Regimes:
Weak Regimes:
Failure Regimes:
Current Regime Fit:
```

The future ensemble should change **model weight**, not retroactively change model history.

---

# 11. Independence Testing

The Quant Layer is most valuable when it adds information Xyool does not already contain.

Measure:

- correlation among quant signals
- correlation between quant signals and Xyool states
- incremental information coefficient
- incremental return after controlling for existing signals
- change in drawdown
- change in turnover
- change in geometric return

Ask:

> **Does this signal add new information, or merely describe the same phenomenon in another language?**

Redundant models should receive lower weight even if individually profitable.

---

# 12. Quant Consensus Is Not Truth

Multiple models agreeing can increase confidence only if they are sufficiently independent.

For example:

```text
12-1 MOMENTUM
6-1 MOMENTUM
3-MONTH MOMENTUM
MOVING-AVERAGE TREND
```

may look like four confirmations while actually representing one underlying price-trend phenomenon.

Group signals by economic family before calculating consensus.

---

# 13. Quant Family Structure

```text
PRICE PERSISTENCE
  ├─ Cross-Sectional Momentum
  └─ Time-Series Momentum

VALUATION
  └─ Value

BUSINESS QUALITY
  └─ Quality / Profitability

PRICE REVERSAL
  ├─ Short-Term Mean Reversion
  └─ Statistical Arbitrage

RISK
  ├─ Low Volatility
  ├─ Volatility Targeting
  └─ Risk-Parity / Risk Budget

MARKET STATE
  └─ Breadth / Regime
```

Consensus should first be calculated **within family**, then across independent families.

---

# 14. Quant Utility Card

After testing, each model receives a practical role card.

```text
QUANT UTILITY CARD

Model:
Family:
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
Correlation to Xyool:
Incremental Value:
Confidence:
Status: REJECT / RESEARCH / USE / CORE
```

A model does not need standalone alpha to be useful.

Example:

> A volatility model that reduces catastrophic drawdowns may improve geometric compounding even if it contributes no directional prediction.

---

# 15. Initial Integration Experiments

Do not immediately merge all models into one score.

Test specific hypotheses.

## Experiment A — Quant as Discovery Filter

```text
QUANT SCREEN
   ↓
XYOOL ANALYSIS
```

Question:
> Does the quant screen increase the hit rate of companies entering Xyool review?

---

## Experiment B — Quant as Ignition Detector

```text
XYOOL HIGH-POTENTIAL COMPANY
       +
TREND / MOMENTUM / BREADTH
       ↓
IGNITION CONFIRMATION
```

Question:
> Can price-based models improve timing without causing the system to chase?

---

## Experiment C — Quant as Risk Overlay

```text
CAC DESIRED POSITION
       ↓
VOLATILITY / REGIME / LIQUIDITY
       ↓
RISK-ADJUSTED POSITION
```

Question:
> Can quant risk models preserve more capital through adverse regimes?

---

## Experiment D — Quant as Rotation Confirmation

```text
CURRENT HOLDING vs CANDIDATE
       ↓
CAC OPPORTUNITY DIFFERENTIAL
       +
RELATIVE MOMENTUM / TREND
       ↓
ROTATION CONFIDENCE
```

Question:
> Does relative price behavior reduce premature rotations or identify deterioration earlier?

---

## Experiment E — Fundamental + Quant Orthogonality

Compare four portfolios:

1. Quant only
2. Xyool/OSE/CAC only
3. Xyool + agreeing quant signals only
4. Xyool + independent optimized quant overlay

Question:

> **Does combining genuinely independent evidence improve geometric return and reduce drawdowns?**

---

# 16. Anti-Overfitting Rules

1. Start with canonical model definitions.
2. Use few parameters.
3. Prefer broad parameter robustness to a single optimal setting.
4. Penalize turnover.
5. Penalize model complexity.
6. Require out-of-sample survival.
7. Require cross-regime testing.
8. Require economic rationale.
9. Do not add indicators merely because backtests improve.
10. Every model must have a documented failure mode.

A model that works only at one exact parameter is probably fragile.

---

# 17. Quant Layer State Flow

```text
RAW MARKET / FUNDAMENTAL DATA
          ↓
POINT-IN-TIME DATASET
          ↓
INDIVIDUAL QUANT MODELS
          ↓
RAW SIGNALS
          ↓
NORMALIZED SIGNALS
          ↓
FAMILY AGGREGATION
          ↓
REGIME CONTEXT
          ↓
MODEL TOURNAMENT
          ↓
UTILITY CARDS
          ↓
INTEGRATION EXPERIMENTS
```

The Quant Layer produces **signals and measured utility**.

It does not initially produce the final capital-allocation decision.

---

# 18. Event Update Rule

For each new data point:

```text
OLD QUANT STATE
   ↓
NEW DATA
   ↓
WHICH MODEL CHANGED?
   ↓
SIGNAL MAGNITUDE?
   ↓
SIGNAL VELOCITY?
   ↓
REGIME CHANGE?
   ↓
MODEL CONFIDENCE CHANGE?
   ↓
NEW QUANT STATE
```

This mirrors Xyool's stateful philosophy without contaminating the two systems.

---

# 19. Initial Build Order

Implement in this order:

```text
1. Data Contract
2. Cross-Sectional Momentum
3. Time-Series Momentum
4. Value
5. Quality / Profitability
6. Low Volatility
7. Short-Term Mean Reversion
8. Volatility Targeting
9. Breadth / Regime
10. Risk-Budget Allocation
11. Statistical Arbitrage / Pairs
12. Tournament Harness
13. Walk-Forward Testing
14. Quant Utility Cards
15. Xyool Integration Experiments
```

The first implementation should remain interpretable and reproducible.

---

# 20. Primary Quant Research Questions

The Quant Layer exists to answer these questions empirically:

1. Which established quant models remain useful in the universes Xyool cares about?
2. Which models survive realistic transaction costs and liquidity constraints?
3. Which models work specifically in small and asymmetric equities?
4. Which models improve discovery?
5. Which models improve ignition/timing?
6. Which models reduce drawdowns?
7. Which models improve position sizing?
8. Which models improve rotation decisions?
9. Which signals are redundant with Xyool?
10. Which signals are genuinely orthogonal?
11. Which model combinations improve geometric capital growth?
12. In which regimes should each model be trusted, reduced, or ignored?

---

# 21. Final Success Criterion

The Quant Layer is successful only if it produces **measurable incremental utility**.

The eventual benchmark should compare:

```text
BUY / HOLD BASELINES
        vs
QUANT ONLY
        vs
XYOOL + OSE + CAC
        vs
XYOOL + OSE + CAC + QUANT OVERLAY
```

Primary question:

> **Does the Quant Layer increase compounded capital growth, improve timing or selection, or reduce destructive drawdowns after realistic implementation costs?**

If a model does not improve one of those outcomes, it does not earn a permanent role in the system.
