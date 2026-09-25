# Xyool — Quant Model Catalog

## Purpose

This catalog defines the canonical model universe for the **independent Quant Layer**.

The Quant Layer remains separate from Company-Level Xyool, the Opportunity State Engine (OSE), and the Capital Allocation Controller (CAC) during standalone testing.

The objective is not to collect indicators. The objective is to test established quantitative ideas and determine **what job each model is actually useful for**.

Primary jobs:

- DISCOVERY
- SELECTION
- TIMING
- CONFIRMATION
- RISK CONTROL
- POSITION SIZING
- ROTATION
- EXECUTION
- REGIME DETECTION
- PORTFOLIO CONSTRUCTION

Machine learning is explicitly deferred until the canonical model universe has been tested.

---

# 1. Model Classes

Models compete inside the class that matches their economic purpose.

```text
QUANT MODEL UNIVERSE
│
├── A. ALPHA / SECURITY SELECTION
│   ├── Price persistence
│   ├── Reversal
│   ├── Fundamental factors
│   ├── Earnings / event factors
│   ├── Ownership / issuance
│   └── Liquidity / seasonality
│
├── B. STATISTICAL / RELATIVE VALUE
│   ├── Factor residuals
│   ├── Pairs / cointegration
│   ├── PCA residuals
│   └── Cross-sectional residual models
│
├── C. VOLATILITY / REGIME
│   ├── Realized / EWMA volatility
│   ├── GARCH-family forecasts
│   ├── Markov regime switching
│   └── Correlation / dispersion regimes
│
└── D. RISK / PORTFOLIO CONSTRUCTION
    ├── Volatility targeting
    ├── Risk parity / ERC
    ├── Mean-variance
    ├── Black-Litterman
    ├── Hierarchical allocation
    ├── Tail-risk optimization
    └── Kelly sizing
```

Do not rank a risk model against an alpha model using one universal score. A model must first prove usefulness for its intended job.

---

# 2. Tournament 1 — Core Model Universe

Tournament 1 contains established, interpretable models only.

## A. Alpha / Security-Selection Models

### A01 — Cross-Sectional Momentum 12-1

**Canonical idea:** rank securities by return over the prior 12 months excluding the most recent month.

Data:
- adjusted daily or monthly prices
- historical universe membership

Primary jobs:
- discovery
- selection
- rotation

Primary output:
- cross-sectional percentile rank

Failure risks:
- momentum crashes
- regime reversals
- illiquid microcap jumps

---

### A02 — Cross-Sectional Momentum 6-1

Shorter intermediate-horizon momentum benchmark.

Primary jobs:
- selection
- rotation
- confirmation

Keep separate from A01 for robustness testing, but treat both as the same **price-persistence family** when measuring consensus.

---

### A03 — Residual Momentum

Rank momentum after removing broad market and/or factor exposure.

Data:
- security returns
- benchmark/factor returns

Primary jobs:
- selection
- identifying idiosyncratic strength

Useful question:
> Is the company strong, or is the entire factor/sector simply rising?

---

### A04 — Time-Series Momentum

Measure whether an asset's own trailing return is positive or negative over fixed horizons.

Possible canonical horizons:
- 1 month
- 3 months
- 6 months
- 12 months

Primary jobs:
- timing
- confirmation
- risk control

---

### A05 — Moving-Average / Trend Model

Canonical versions:
- close > 200-day moving average
- 50/200 moving-average state
- multi-horizon trend consensus

Primary jobs:
- timing
- ignition confirmation
- risk control

Do not treat multiple moving averages as independent evidence.

---

### A06 — Breakout / Donchian Trend

Canonical versions:
- 20-day breakout
- 55-day breakout
- 100/200-day breakout

Primary jobs:
- ignition detection
- timing

Failure risk:
- false breakouts in low-liquidity securities

---

### A07 — Short-Term Reversal

Canonical measurements:
- 1-day reversal
- 5-day reversal
- market/sector-adjusted reversal

Primary jobs:
- execution
- entry improvement
- anti-chasing

Do not use short-term reversal as a substitute for long-horizon opportunity quality.

---

### A08 — Value Composite

Canonical components where economically appropriate:
- earnings yield
- FCF yield
- EV/EBIT
- EV/EBITDA
- book-to-market
- sales yield with strong quality controls

Primary jobs:
- selection
- recognition-gap validation
- avoiding overpayment

Use industry-relative normalization where required.

---

### A09 — Gross Profitability

Canonical concept:
- gross profits / assets

Primary jobs:
- quality confirmation
- selection

This should remain distinct from valuation.

---

### A10 — Quality Composite

Possible components:
- ROIC / ROA / ROE where appropriate
- operating margin
- FCF margin
- earnings stability
- leverage
- interest coverage
- cash conversion

Primary jobs:
- selection
- failure filtering
- shareholder-capture validation

---

### A11 — Size

Canonical concept:
- market-cap rank / small-minus-large exposure

Primary jobs:
- factor attribution
- discovery context

Size should usually be a control or conditioning variable, not a standalone reason to own a security.

---

### A12 — Investment / Asset Growth

Canonical concept:
- conservative investment / low asset growth versus aggressive asset expansion

Possible measurements:
- total asset growth
- capex growth
- invested-capital growth

Primary jobs:
- selection
- dilution/capital-efficiency context

---

### A13 — Accruals

Canonical concept:
- distinguish accounting earnings from cash-backed earnings

Possible measurements:
- total accruals / assets
- operating accruals
- cash-flow-to-earnings quality

Primary jobs:
- quality confirmation
- failure filtering

---

### A14 — Earnings Surprise

Canonical inputs:
- reported EPS/revenue versus consensus where reliable
- standardized unexpected earnings

Primary jobs:
- event confirmation
- timing
- selection

Publication timestamp must be respected.

---

### A15 — Post-Earnings Announcement Drift (PEAD)

Canonical concept:
- test continued abnormal returns after material earnings surprise.

Primary jobs:
- timing
- confirmation
- rotation

Requires strict event timestamps and realistic next-trade execution.

---

### A16 — Insider Accumulation

Canonical inputs:
- open-market insider purchases
- insider purchase clusters
- insider ownership change

Primary jobs:
- confirmation
- discovery

Weight transaction type and economic size; do not treat grants as purchases.

---

### A17 — Institutional Accumulation

Canonical inputs:
- 13F ownership change
- number of holders
- concentration of new institutional positions

Primary jobs:
- recognition tracking
- confirmation

Lagged filing dates are mandatory; do not use quarter-end holdings before they became public.

---

### A18 — Activist / Beneficial Ownership Signal

Canonical inputs:
- Schedule 13D / 13G changes
- stake size
- activist versus passive classification

Primary jobs:
- event discovery
- recognition/catalyst context

Treat 13D and 13G as economically different signals.

---

### A19 — Net Issuance / Dilution

Canonical measurements:
- change in diluted shares
- net equity issuance
- ATM usage
- convert/warrant overhang where measurable

Primary jobs:
- risk control
- shareholder-capture validation
- selection

A strong business trajectory can still produce weak per-share results if issuance overwhelms growth.

---

### A20 — Liquidity / Amihud Illiquidity

Canonical concept:
- absolute return divided by dollar volume, aggregated over a window

Additional measurements:
- turnover
- median dollar volume
- bid/ask spread where available

Primary jobs:
- execution
- position sizing
- capacity control

---

### A21 — Low Volatility / Low Beta

Canonical measurements:
- realized volatility
- beta
- downside deviation
- idiosyncratic volatility

Primary jobs:
- selection conditioning
- risk control
- sizing

Treat as a risk/return anomaly and risk descriptor, not proof of business quality.

---

### A22 — Seasonality

Canonical tests:
- month-of-year
- day-of-week where justified
- earnings-calendar recurrence
- company-specific seasonal return pattern

Primary jobs:
- timing
- execution

Seasonality must survive multiple subperiods and transaction-cost tests.

---

# 3. Statistical / Relative-Value Models

### S01 — CAPM / Market Residual

Purpose:
- estimate beta
- isolate market-adjusted residual returns

Primary jobs:
- attribution
- residual momentum/reversal
- risk control

---

### S02 — Fama-French 3-Factor Attribution

Factors:
- market
- size
- value

Primary jobs:
- attribution
- residualization
- determining whether observed alpha is merely known factor exposure

---

### S03 — Fama-French 5-Factor Attribution

Factors:
- market
- size
- value
- profitability
- investment

Primary jobs:
- attribution
- model independence testing

---

### S04 — Momentum-Extended Factor Attribution

Add a momentum factor to factor attribution.

Primary jobs:
- residualization
- detecting duplicate momentum exposure

---

### S05 — Pairs / Cointegration

Canonical pipeline:

```text
ECONOMICALLY PLAUSIBLE PAIR
→ STATIONARITY / COINTEGRATION TEST
→ SPREAD MODEL
→ Z-SCORE
→ ENTRY / EXIT
→ STABILITY CHECK
```

Primary jobs:
- relative value
- hedged exposure
- peer dislocation detection

---

### S06 — PCA Residual Statistical Arbitrage

Canonical concept:
- derive common return components
- remove principal-factor exposure
- test residual mean reversion

Primary jobs:
- relative value
- market/sector-neutral dislocation detection

---

### S07 — Factor-Neutral Cross-Sectional Residual

Neutralize signals against selected factors such as:
- market beta
- sector
- size
- value

Primary jobs:
- independence testing
- cleaner ranking signals

---

# 4. Volatility / Regime Models

### V01 — Realized Volatility

Canonical versions:
- 20-day
- 60-day
- 252-day annualized realized volatility

Primary jobs:
- sizing
- risk control
- regime input

---

### V02 — EWMA Volatility

Canonical concept:
- exponentially weight recent squared returns more heavily.

Primary jobs:
- responsive risk estimation
- volatility targeting

---

### V03 — GARCH(1,1)

Purpose:
- conditional volatility forecasting

Primary jobs:
- position sizing
- tail/risk-state monitoring

Start with GARCH(1,1) before more complex specifications.

---

### V04 — Asymmetric GARCH Family

Candidate specifications:
- EGARCH
- GJR-GARCH

Purpose:
- model asymmetric volatility responses to negative versus positive shocks.

Primary jobs:
- risk forecasting
- stress recognition

---

### V05 — Long-Memory / Multi-Horizon Volatility

Candidate specifications:
- FIGARCH
- HARCH

Status:
- research after GARCH(1,1) benchmark

---

### V06 — Markov Regime Switching

Possible observable states:
- low-volatility bull
- high-volatility bull
- low-volatility bear
- high-volatility bear

Primary jobs:
- regime detection
- model weighting
- risk control

Output should be probabilistic, not merely a hard label.

---

### V07 — Breadth Regime

Possible measurements:
- percentage above 50/200-day moving averages
- advance/decline breadth
- new highs versus new lows

Primary jobs:
- regime detection
- ignition context

---

### V08 — Correlation / Dispersion Regime

Possible measurements:
- average pairwise correlation
- cross-sectional return dispersion
- sector dispersion

Primary jobs:
- regime detection
- determining whether stock selection has room to matter
- portfolio concentration control

---

### V09 — Implied-Volatility Expected-Move Walls

Canonical research baseline:
- freeze a point-in-time annualized implied-volatility input;
- convert a specified central coverage probability into a normal z-score;
- scale by square-root-of-time;
- construct log-symmetric upper/lower expected-move walls.

Primary jobs:
- execution;
- timing;
- volatility/range calibration.

Required data:
- point-in-time options IV;
- underlying OHLCV;
- next-session execution prices;
- corporate-action-safe horizon prices.

Mandatory distinction:

```text
range containment
!=
wall-touch reaction edge
```

This model is **RESEARCH ONLY**. It cannot create exposure or override TTC.
A 90% nominal envelope is not evidence of a 90% trading win rate.

Reference implementation:
- `agent/quant/iv_walls.py`

Frozen test:
- `research/system-tests/2026-09-23-iv-wall-execution-sidecar-v1-spec.md`

---

# 5. Risk / Portfolio Construction Models

### P01 — Volatility Targeting

Canonical form:

```text
Exposure = Target Volatility / Forecast Volatility
```

Apply leverage and maximum-position caps.

Primary jobs:
- sizing
- drawdown control

---

### P02 — Inverse Volatility Allocation

Canonical form:

```text
Weight_i ∝ 1 / Volatility_i
```

Primary jobs:
- simple risk-aware portfolio benchmark

---

### P03 — Equal Risk Contribution / Risk Parity

Goal:
- each asset contributes a deliberate share of portfolio risk.

Primary jobs:
- portfolio construction
- concentration control

---

### P04 — Minimum Variance

Goal:
- minimize forecast portfolio variance subject to constraints.

Primary jobs:
- risk benchmark
- allocation

---

### P05 — Mean-Variance / Maximum Sharpe

Canonical Markowitz-style optimization.

Primary jobs:
- allocation benchmark

Important:
- expected-return estimation error must be stress tested.

---

### P06 — Black-Litterman

Purpose:
- combine equilibrium market information with explicit views and uncertainty.

Primary jobs:
- structured view integration
- portfolio construction

Potential future use:
- translate independent Xyool conviction into probabilistic portfolio views only after independent Quant testing is complete.

---

### P07 — Hierarchical Risk Parity (HRP)

Canonical concept:
- cluster correlated assets
- allocate using hierarchical structure rather than direct covariance inversion.

Primary jobs:
- robust portfolio construction
- correlated-opportunity control

---

### P08 — HERC / Hierarchical Equal Risk Contribution

Purpose:
- hierarchical clustering with cluster-level risk contribution control.

Primary jobs:
- portfolio construction

---

### P09 — Nested Clustered Optimization (NCO)

Purpose:
- reduce estimation error by optimizing within and between clusters.

Primary jobs:
- portfolio construction
- covariance instability control

---

### P10 — CVaR Optimization

Goal:
- optimize expected return subject to conditional value-at-risk / expected shortfall.

Primary jobs:
- tail-risk control
- allocation

---

### P11 — CDaR / Drawdown Optimization

Goal:
- explicitly control conditional drawdown risk.

Primary jobs:
- survivability
- geometric-compounding protection

---

### P12 — Kelly / Fractional Kelly

Canonical concept:
- size exposure according to estimated edge relative to uncertainty.

Default research preference:
- fractional Kelly, especially half-Kelly or lower

Primary jobs:
- sizing
- capital growth optimization

Never apply unconstrained Kelly to unstable estimates or highly skewed small-cap opportunities.

---

# 6. Deferred Model Families

Do **not** include these in Tournament 1 until the canonical competitors have a working benchmark:

- random forests
- gradient boosting
- neural networks
- LSTM forecasting
- transformers
- reinforcement learning
- genetic optimization
- opaque proprietary composites

Machine learning may later be tested for:

1. signal combination
2. nonlinear interactions
3. regime-conditioned weighting
4. probability calibration

But it must compete against the transparent canonical baseline.

---

# 7. Optional Data-Dependent Models

These are allowed when trustworthy historical data is available:

## Options
- implied volatility level
- IV minus realized volatility
- skew
- term structure
- put/call surface measures
- delta/gamma exposure proxies

## Microstructure
- order-flow imbalance
- trade imbalance
- bid/ask pressure
- spread dynamics

## Cross-Asset / Carry
- FX carry
- futures term-structure carry
- crypto funding / basis
- commodity curve signals

They are not required for Tournament 1 because point-in-time historical data quality may be the binding constraint.

---

# 8. Data Availability Classes

Every model receives one of four data states:

```text
D0 — DATA UNAVAILABLE
D1 — LIVE / CURRENT ONLY
D2 — HISTORICAL BUT INCOMPLETE
D3 — POINT-IN-TIME BACKTEST READY
```

A model cannot enter the final tournament until it reaches **D3** for the intended test universe.

Current expected feasibility:

```text
PRICE / OHLCV                     D3-capable
BASIC FUNDAMENTALS                D2→D3 depending historical timestamps
SEC FILINGS / OWNERSHIP           D2→D3 depending coverage window
EARNINGS EVENTS                   D2→D3
OPTIONS IV / GREEKS               D1→D2 unless historical surface data is added
MICROSTRUCTURE                    D1→D2 unless deep history is added
```

---

# 9. Canonical-First Rule

For every model:

1. implement the well-known canonical version first
2. lock the definition
3. establish baseline performance
4. test nearby parameter robustness
5. only then test modifications

Example:

```text
12-1 MOMENTUM
    ↓
BASELINE
    ↓
6-1 / 9-1 / SECTOR-NEUTRAL VARIANTS
    ↓
ROBUSTNESS COMPARISON
```

Do not search hundreds of parameters for the best historical result.

---

# 10. Family Independence

Signals must be grouped by underlying economic mechanism.

```text
PRICE PERSISTENCE
  A01 A02 A03 A04 A05 A06

REVERSAL
  A07 S05 S06

VALUATION
  A08

BUSINESS QUALITY
  A09 A10 A12 A13

EVENT / RECOGNITION
  A14 A15 A16 A17 A18

SHAREHOLDER FRICTION
  A19

LIQUIDITY / RISK
  A20 A21

VOLATILITY / REGIME
  V01–V08

PORTFOLIO CONSTRUCTION
  P01–P12
```

Several correlated members of one family do not constitute several independent confirmations.

---

# 11. Required Model Record

Every implemented model must have:

```text
MODEL ID:
NAME:
CLASS:
FAMILY:
CANONICAL DEFINITION:
DATA REQUIRED:
DATA STATE: D0 / D1 / D2 / D3
LOOKBACK:
EXPECTED HORIZON:
PRIMARY JOB:
SECONDARY JOBS:
RAW OUTPUT:
NORMALIZATION:
KNOWN FAILURE MODES:
TRANSACTION-COST SENSITIVITY:
LIQUIDITY REQUIREMENT:
PARAMETERS LOCKED?:
IMPLEMENTED?:
BACKTESTED?:
OUT-OF-SAMPLE?:
TOURNAMENT STATUS:
```

---

# 12. Tournament 1 Principle

The purpose of Tournament 1 is not to discover the prettiest backtest.

It is to answer:

> **Which established quantitative methods provide robust, independent, economically useful information for Xyool's capital-compounding objective?**

The survivor set should be smaller than the starting universe.
