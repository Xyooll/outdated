# Xyool Quant Production Defaults

Status: evidence-tested `USE`, not universal truth.

Evidence report: `research/system-tests/quant-formula-parameter-tournament-report-2026-09-06.md`

Executable implementation: `agent/quant/production.py` (also exported through `agent.quant`).

## Principle

Quant does not own thesis selection or final economic allocation.

```text
XYOOL / OSE / QUALITY QUALIFIER
    ↓
TTC DESIRED ECONOMIC POSITION
    ↓
QUANT
risk sizing + trend/ignition + recognition corroboration
    ↓
EXECUTABLE POSITION
```

Do not collapse these jobs into a universal master score.

## 1. Trend / Ignition Default

Primary production trend signal:

```text
MA10_t = mean(P_t, P_{t-1}, ..., P_{t-9})
Trend_t = +1 if P_t > MA10_t else -1
```

Use MA10 for:
- ignition / add corroboration;
- recognition-state support;
- deterioration corroboration;
- timing confidence.

Status: **USE**.

MA12 is a slower alternative. TSM signals remain secondary corroboration rather than mandatory co-equal gates.

### Authority limit

MA10 cannot:
- create a fundamental thesis;
- break an intact high-SC/high-CC thesis by itself;
- fully veto the second independent high-quality OSE deterioration checkpoint under `ose-quant-interface.md`.

## 2. Expected-Volatility Default

Primary production estimator:

```text
v_t = 0.97 * v_{t-1} + 0.03 * r_t^2
sigma_t = sqrt(12 * v_t)
```

where `r_t` is the monthly return.

Status: **USE**.

Reason:
- slow EWMA 0.94–0.97 forms a robust parameter plateau;
- 0.97 remained competitive on forecast error;
- it had less severe catastrophic underforecasting than RV12 in the fresh test.

Do not treat 0.97 as a magic optimum. Neighboring values remain valid research alternatives.

### Audit estimator

Also calculate:

```text
RV12_t = annualized standard deviation of trailing 12 monthly returns
```

RV12 is an audit / disagreement signal because it had the best average forward-volatility forecast error in both development and fresh samples.

If EWMA97 and RV12 disagree materially, flag `VOL_ESTIMATOR_DISAGREEMENT`; do not silently average them until a hybrid rule is independently tested.

## 3. Risk-Sizing Default

Current risk budget:

```text
target_vol = 0.12
raw_scale = target_vol / sigma_EWMA97
risk_scale = clamp(raw_scale, 0.25, 1.50)
```

Integration constraint conceptually:

```text
executable_position = min(
    TTC_desired_position,
    TTC_desired_position * risk_scale
)
```

Quant therefore may reduce risk expression but may not independently increase a position above TTC's desired economic size.

Status of 12% target: **USE**, not CORE.

10% is a conservative profile. 15% remains a higher-risk research candidate. Target volatility encodes survivability/risk appetite as well as forecast quality, so it should not be optimized merely for terminal return.

## 4. Executable Contract

`agent/quant/production.py` currently implements:
- month-end simple returns from a single price history;
- MA10 trend state and distance;
- EWMA97 annualized volatility;
- RV12 annualized audit volatility;
- 12% target-volatility risk scaling with the frozen 0.25–1.50 clamp;
- desired-position-preserving executable caps;
- a `QuantProductionSignal` output object.

A minimum of 13 month-end prices is required so the production object has 12 monthly returns for the volatility jobs. EWMA initialization is causal: the first 12 observed squared monthly returns seed the recurrence, after which lambda 0.97 updates forward. This seed is implementation plumbing, not a promoted tournament parameter.

### Backward-compatibility note

The current Python implementation still contains some legacy field/parameter names from the retired allocation terminology. Those identifiers are **implementation compatibility aliases only**. Conceptually they mean **TTC desired position / TTC desired vector**. New APIs and documentation should use TTC naming; runtime renaming should be done under ordinary compatibility testing so it does not break the frozen execution stack.

## 5. Rejected / Secondary Defaults

- RV3: REJECT for production sizing; too twitchy/noisy.
- RV6: secondary / research.
- MA6: secondary / research.
- MA12: useful slower alternative, not primary default.
- TSM3: fresh result was competitive but broader sample was noisier; research only.
- TSM6 / TSM12: secondary corroboration.
- Cross-sectional momentum: not promoted for stock-to-stock TTC rotation.

## 6. Output Object

Every production Quant update should expose at least:

```text
Asset:
Timestamp:
Price:
MA10:
Trend: POSITIVE / NEGATIVE
Trend Distance: (Price / MA10) - 1
EWMA97 Volatility:
RV12 Volatility:
Vol Estimator Disagreement:
12% Risk Scale:
TTC Desired Position:
Executable Position Cap:
Recognition / Extension Note:
Quant Confidence:
Data Quality:
```

## 7. Change Control

Do not change these defaults because another exact parameter wins one sample.

Parameter replacement requires:
- a frozen candidate;
- fresh out-of-sample testing;
- neighboring-parameter robustness;
- meaningful improvement in the job-specific metric or risk;
- no damage to the full Xyool/OSE/Quality/TTC system.