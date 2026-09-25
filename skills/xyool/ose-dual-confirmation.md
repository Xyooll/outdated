# Xyool OSE — Dual Confirmation + Runway Lock-In Extension

Status: **DUAL CONFIRMATION PROMOTED after fresh five-year mixed-universe holdout. RUNWAY LOCK-IN REQUIRED STATE VARIABLE, VALIDATION CONTINUES. SECTOR DEMAND REQUIRED OSE CONTEXT.**

This file is a mandatory extension of `opportunity-state-engine.md`. Where the legacy OSE uses a single `Confirmation` field, new analyses must preserve the aggregate field for compatibility but also decompose it into Structural Confirmation and Conversion Confirmation.

Sector Demand is also a mandatory OSE context under `ose-sector-demand.md`. It informs Structural Confirmation and Potential when independently evidenced, but it is not an independent capital-action rule and must not be double counted with company-specific demand evidence.

## Why the split exists

A company can control a real bottleneck while failing to convert that control into shareholder economics. The inverse can also occur temporarily: conversion can collapse during an execution shock while the structural bottleneck remains intact.

A single Confirmation ladder confuses these states and can cause both false positives and premature exits.

## Structural Confirmation — SC0-SC5

Question:
> Is the underlying demand/control/bottleneck thesis real and strengthening?

Evidence:
- structural demand,
- independently evidenced Sector Demand where causally relevant,
- bottleneck/control,
- strategic necessity,
- customer dependency,
- qualification/sole-source position,
- replacement difficulty,
- independent customer/industry validation.

Sector Demand may strengthen SC only when it is independently evidenced, directly relevant to the company's served end-market, and paired with credible company control/capture. A strong sector without company control is not high SC.

States:
- SC0 — narrative only / no structural proof
- SC1 — early structural indication
- SC2 — partial proof but replaceable/uncertain
- SC3 — material structural position
- SC4 — strong validated control point
- SC5 — systemically important / unusually difficult to replace

## Conversion Confirmation — CC0-CC5

Question:
> Is the company converting its structural position into shareholder economics?

Evidence chain:
**ORDERS → BOOKINGS → BACKLOG → DEPLOYMENT → REVENUE → MARGIN → EBITDA → OCF → FCF → PER-SHARE VALUE**

Sector Demand does not promote CC by itself. CC remains company-specific economic conversion evidence.

States:
- CC0 — no economic conversion
- CC1 — early/weak conversion; economics unproven
- CC2 — repeated operating evidence but weak/fragile economics
- CC3 — clear revenue/margin/earnings conversion
- CC4 — strong repeated economic conversion and improving cash economics
- CC5 — self-reinforcing conversion with strong cash/per-share evidence

## Runway Lock-In — RL0-RL5

Question:
> How much future economic value is already protected even if the external cycle stops accelerating?

Sources:
- funded backlog,
- take-or-pay agreements,
- long-duration charters,
- contracted capacity,
- qualification/sole-source arrangements,
- committed customer volumes,
- minimum-price agreements,
- long-term offtake.

States:
- RL0 — nothing locked
- RL1 — early visibility
- RL2 — partial backlog/commitments
- RL3 — material protected runway
- RL4 — large multi-year locked economics
- RL5 — exceptionally protected contractual/structural runway

High RL slows Potential and Remaining-Opportunity downgrades caused only by spot-cycle normalization. RL does not protect against fraud, destructive financing, contract cancellation, customer insolvency, or other evidence that the locked economics are not collectible.

Sector Demand and RL remain distinct: Sector Demand measures the external demand regime; RL measures how much company economics survive if that regime stops accelerating.

## Required decision matrix

### High SC / High CC
Earned-core candidate. CAC can allocate based on remaining opportunity, recognition, friction and Quant expression.

### High SC / Low CC
**Real bottleneck, weak conversion.**
- cap new capital,
- increase monitoring,
- diagnose execution vs financing vs temporary cycle,
- do not automatically exit if survival and shareholder capture remain intact,
- repeated CC weakness plus rising Friction can become a shareholder trap even if SC stays high.

### Low SC / High short-term CC
Possible cyclical/nonstrategic earnings state. Do not confuse temporary profits with durable control.

### Low SC / Low CC
Reject/watch. Narrative alone cannot earn core capital.

### Strong Sector Demand / Weak SC
The sector may be attractive while the company is the wrong capture vehicle. Do not promote company opportunity merely because `SD3-SD5` is present.

### Cooling Sector Demand / High SC + High RL
Do not automatically downgrade earned capital. Determine whether locked runway, share gains, company-specific conversion, or bottleneck migration offsets sector cooling.

## Trap logic

### Narrative / technology trap
Typical state:
`SC0-SC3 + CC0-CC1 + RL0-RL1 + elevated F`

Rule:
- no core allocation,
- technical milestones alone do not equal economic conversion,
- price momentum does not promote CC.

### Real-bottleneck shareholder trap
Typical state:
`SC4-SC5 + persistent CC0-CC2 + F4-F5`

Rule:
- structural importance is not enough,
- repeated negative FCF, huge capital requirements, dilution/debt dependency, governance failure or inability to reach self-funding progressively lowers shareholder capture,
- F5 can override SC5 and force exit.

A strong Sector Demand state does not cure this trap.

## Conversion-Debt Watch

Not yet a promoted exit rule, but OSE must record the ingredients needed to test it:

```text
CONVERSION DEBT
= duration of weak CC
+ cumulative cash burn
+ remaining capex requirement
+ external financing dependency
+ dilution/debt burden
+ distance to self-funding
```

Repeated CC weakness should become more serious with time. A business cannot remain indefinitely in `SC5 / CC1` without the financing burden changing the equity thesis.

Do not turn this into an automatic threshold until it survives a fresh holdout.

## Hard Friction Override

F5 governance/reporting/capital-survival/shareholder-capture failure can override strong SC and RL.

Examples include:
- unresolved reporting failure,
- going-concern risk,
- bankruptcy/restructuring that materially impairs old equity,
- financing terms that destroy per-share capture,
- structural inability to fund required capacity.

## CAC implications

### New capital
Prefer high Remaining Opportunity with:
- causally relevant Sector Demand that is stable/improving where applicable,
- SC4+,
- CC improving or CC4+,
- manageable F,
- adequate RL where relevant,
- Quant add permission.

Sector Demand remains context, not a mechanical sizing input.

### Earned capital
Do not remove merely because CC dips for one period if:
- SC remains high,
- survival is strong,
- shareholder capture is intact,
- RL protects future economics.

Do not remove merely because Sector Demand decelerates if locked/company-specific economics remain superior.

Material reductions require persistent conversion failure, structural deterioration, severe friction, remaining-opportunity compression, or a clearly superior replacement hurdle.

## Updated state card

```text
OPPORTUNITY STATE CARD

Company:
Price:
Position:
Potential: P0-P5
Sector Demand: SD0-SD5
Sector Demand Velocity: ↑↑ / ↑ / → / ↓ / ↓↓
Sector Demand Breadth: Narrow / Mixed / Broad
Sector Demand Funding: Unfunded / Partial / Funded / Locked
Sector Demand Duration: Short / Medium / Multi-year / Structural
Structural Confirmation: SC0-SC5
Conversion Confirmation: CC0-CC5
Runway Lock-In: RL0-RL5
SC Velocity: ↑↑ / ↑ / → / ↓ / ↓↓
CC Velocity: ↑↑ / ↑ / → / ↓ / ↓↓
Aggregate Confirmation: C0-C5   # compatibility only
Fundamental Velocity:
Ignition: I0-I5
Recognition: R0-R7
Recognition Gap:
Shareholder Capture:
Friction: F0-F5
Conversion Debt: Low / Medium / High / Extreme
Remaining Opportunity:
Time to Catalyst:
Time to Maturity:
Permanent Impairment Risk:
Confidence:
Best Evidence:
Weakest Link:
Next Trigger:
Invalidation:
CAC Action:
```

## Evidence basis for promotion

Fresh five-year mixed-universe replay, 2020-12-31 to 2025-12-31:
- Dual-Confirmation dynamic system: ~$570.5k from $100k
- initial CAC + hold: ~$534.3k
- all-candidate equal-weight B&H: ~$367.0k
- investability-filtered equal-weight B&H: ~$406.4k
- old single-Confirmation VRT-exit proxy: ~$522.7k

The decisive refinement test was Vertiv: SC remained high during the 2022 conversion collapse. Preserving the core instead of applying the old 50% reduction added roughly $47.8k of terminal value in the otherwise identical replay.

The same mixed holdout also demonstrated why high SC cannot override persistent CC/Friction failure: WOLF remained strategically relevant in silicon carbide but became a shareholder-capital trap, while PLUG and QS never established the economic conversion required for core status.

Runway Lock-In was directionally supported, particularly by LNG and the distinction between spot-cycle changes and protected contracted economics, but should continue to accumulate independent holdout evidence.

Sector Demand is newly required OSE context as of the current revision. No independent capital-action rule for Sector Demand has yet been validated; its presence in the state card must not be misrepresented as a tested sizing rule.
