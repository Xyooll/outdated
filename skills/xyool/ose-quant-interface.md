# Xyool — OSE ↔ Quant Decision Interface

**Status:** USE / PROVISIONAL  
**Promotion basis:** one fresh five-year contested holdout after an earlier in-sample diagnostic.  
**Not CORE until independently replicated.**

## Purpose

Define authority between Dynamic OSE / Time to Catalyst (TTC) economic evidence and the independent Quant overlay.

The Quant layer supports TTC. It does not own the economic thesis.

```text
XYOOL
  ↓
OSE + QUALITY QUALIFIER
  ↓
TTC DESIRED ECONOMIC ACTION
  ↓
QUANT EXPRESSION MODIFIER
  ↓
EXECUTABLE ACTION
```

## Core rule

> **Quant can challenge immature fundamental evidence. Quant cannot indefinitely veto mature, repeated economic deterioration.**

## First deterioration checkpoint

When OSE records the first independent high-quality deterioration in Conversion Confirmation, shareholder capture, or Conversion Debt, but no F5 override exists:

- TTC may request REVIEW / REDUCE.
- Quant may veto or delay the reduction if trend/price evidence materially contradicts it.
- New capital is blocked until OSE improves.
- The earned core can remain intact because one deterioration event can be temporary noise or an execution shock.

## Second independent deterioration checkpoint

When a second independent high-quality deterioration occurs before recovery:

- OSE/TTC becomes authoritative that economic action is required.
- Quant may reduce the requested magnitude by **at most one step**.
  - Example: TTC 50% reduction → Quant may scale to 25%, but not 0%.
- Quant may delay execution by **at most one monthly checkpoint**.
- Quant cannot completely veto the action.
- If Quant agrees, execute the TTC magnitude normally.

## F5 override

F5 capital-survival, governance, reporting, or shareholder-capture failure overrides Quant immediately.

Examples:
- going-concern risk;
- bankruptcy/restructuring risk to existing equity;
- unresolved severe reporting/governance failure;
- financing terms that destroy per-share capture;
- structural inability to fund required capacity.

## Structural-thesis protection

The rule is symmetric.

Quant cannot create a fundamental sell merely because:
- price crashes;
- momentum turns negative;
- volatility spikes;
- recognition collapses;
- the market enters risk-off mode.

If SC/CC remain strong and OSE does not establish economic deterioration, Quant may:
- cap additions;
- reduce tactical exposure;
- increase cash/risk reserve;
- increase monitoring;

but may not independently invalidate the earned economic core.

## Conversion Debt interaction

Conversion Debt should escalate the maturity of an OSE deterioration state:

```text
CONVERSION DEBT
= duration of weak CC
+ cumulative cash burn
+ remaining capex requirement
+ external financing dependency
+ dilution/debt burden
+ distance to self-funding
```

A high-SC company can still become an equity trap when repeated weak CC makes financing needs progressively destructive.

Two independent Conversion-Debt checkpoints can therefore invoke the second-deterioration authority rule even when Structural Confirmation remains SC4-SC5.

## Runway Lock-In interaction

High RL can prevent a temporary conversion shock from prematurely reaching checkpoint 2 when future economics remain strongly protected by:
- funded backlog;
- take-or-pay contracts;
- long-duration subscriber/charter agreements;
- committed capacity;
- minimum-price/offtake agreements;
- qualification or sole-source locks.

RL does not override destructive financing or F5.

## Required decision trace

Every contested OSE↔Quant decision records:

```text
OSE EVENT:
Checkpoint: 1 / 2 / F5
Structural Confirmation:
Conversion Confirmation:
Runway Lock-In:
Conversion Debt:
Friction:
TTC Desired Action:
TTC Desired Magnitude:
Quant Trend:
Quant Momentum:
Quant Volatility:
Quant Recognition State:
Quant Agreement: YES / NO
Quant Modification:
Maximum Allowed Modification:
Executable Action:
Reason:
Next Review:
```

This prevents hidden authority changes and makes historical replay reproducible.

## Empirical basis

### Prior full-stack diagnostic — ENPH

A previous five-year holdout showed that a hard Quant veto delayed a fundamentally justified ENPH reduction after two major conversion-deterioration checkpoints. A post-test diagnostic suggested the relaxed rule would improve terminal capital, but that diagnostic was not counted as proof because it was learned from the same sample.

### Fresh holdout — Roku

Fresh five-year holdout: 2021-08-31 to 2026-08-31.

Roku produced a genuine contested state:
- checkpoint 1: 2022 conversion deterioration / negative EBITDA / restructuring;
- checkpoint 2: 2023 repeated losses plus additional restructuring and impairment;
- SC remained material;
- price trend had recovered enough that the old Quant rule would veto the reduction.

The economic layer requested a 50% reduction.

- old hard-veto proxy: 0% reduction;
- new interface: 25% reduction;
- the sold tranche was routed to AVGO/HUBB;
- terminal contribution versus leaving that tranche in Roku: approximately **+$272 after modeled costs**.

Full holdout results:
- old hard-Quant-veto system: ~$303,983 from $100k;
- relaxed-veto full system: ~$304,255;
- difference: ~+$272 / +0.09% terminal capital.

The broader relaxed full system also substantially beat static economic allocation and mixed equal-weight buy-and-hold.

## Status rule

The interface is promoted to **USE / PROVISIONAL** because:
- it was frozen before a fresh holdout;
- a real disagreement state occurred;
- it improved terminal capital versus the old hard-veto proxy;
- it preserved the broader architecture's performance.

It remains below CORE because:
- the fresh incremental edge was small;
- only one independent contested holdout has directly tested the exact rule.

A second fresh contested holdout is required for CORE consideration.

## Design principle

> **Fundamental evidence determines what capital should do. TTC determines which qualified opportunity deserves that capital now. Quant determines how efficiently TTC-approved exposure should be expressed, unless fundamental evidence is still immature enough to require independent market confirmation.**