# Xyool Conversion Debt

Status: **RESEARCH / TRACKING ONLY**

Evidence report: `research/system-tests/conversion-debt-validation-report-2026-09-06.md`

## Purpose

Conversion Debt describes the accumulating shareholder burden when a company retains a real structural opportunity but repeatedly fails to convert that opportunity into self-funding economics.

It is useful as an OSE state variable.

It is **not currently authorized as an automatic sell trigger**.

## State Inputs

Track:
- Structural Confirmation (SC)
- Conversion Confirmation (CC)
- Runway Lock-In (RL)
- gross / unit margin direction
- operating profit / EBITDA direction
- OCF / FCF direction
- net debt / liquidity runway
- dilution / external financing dependence
- remaining capex to CFIT
- time spent materially below self-funding
- repair trajectory

## What Current Testing Established

1. Conversion Debt can provide useful early warning before F5. Enviva generated approximately three months of lead versus the later going-concern/F5 state and about seven months versus Chapter 11.
2. Nominal backlog or take-or-pay contracts can be misleading. Locked revenue is not necessarily locked economic value.
3. High capex alone is not Conversion Debt. HII and Albemarle were important negative controls.
4. The frozen automatic 50% trigger produced false positives in Emergent BioSolutions and Spirit AeroSystems.
5. Quant scaling reduced the Spirit false-positive damage but did not solve the underlying state-classification problem.

Therefore:

```text
TRACK Conversion Debt
DO NOT automatically REDUCE from Conversion Debt alone
```

Until a new trigger is independently validated, capital actions must continue to come from the existing OSE/CAC evidence and friction rules.

## Research Candidates — Not Production Rules

### Economic Runway Lock-In

Research candidate:

```text
ERL = nominal locked runway
      × margin quality
      × contract enforceability / funding certainty
      × cash-conversion quality
```

Motivation: Enviva had extremely high nominal contracted backlog but destructive contract economics.

### Deterioration Breadth

Research candidate:

```text
DB = number of independently worsening core metrics
```

Potential core metrics:
- gross / unit margin
- EBITDA / operating income
- OCF / FCF
- net debt / liquidity runway
- dilution / external capital requirement
- remaining capex to CFIT

The prior 'one worsening metric is enough' rule is rejected.

### Repair Trajectory

Explicitly track whether the company is repairing:
- cost structure
- asset sales
- debt maturity profile
- customer funding / support
- capex burden
- working capital
- unit economics
- cash conversion

Weak absolute CC with an improving repair trajectory must not be treated identically to accelerating Conversion Debt.

## Guardrail

Do not let Conversion Debt become a generic detector for:
- losing stocks,
- volatile stocks,
- pre-revenue companies,
- all high-capex companies,
- all externally financed companies.

Company-Level Xyool remains responsible for proving the structural opportunity first.
