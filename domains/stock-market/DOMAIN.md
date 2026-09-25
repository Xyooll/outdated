# Xyool Domain Manifest — Stock / Market

Status: **ACTIVE DOMAIN / PRIMARY DEVELOPMENT + VALIDATION LAYER**

## Floware execution

Primary domain Floware:
- `domains/stock-market/flows/company-analysis.flow.md`
- `domains/stock-market/flows/payoff-ranking.flow.md`

Current active development Flow:
`STOCK-PAYOFF-RANKING-V1`

Frozen goalpost:
`research/system-tests/stock-payoff-ranking-goalpost-v1-2026-09-22.md`

Canonical domain Plumbing:
- `domains/stock-market/PLUMBING.md`

Stock-market skills remain detailed methods and taxonomies loaded by these Flows. New reasoning should be expressed in domain Floware first. New software requires the core Software Escalation Flow.

## Operation sequencing

Canonical Meta Flow:
`floware/meta/sequencing.flow.md`

Stock-domain order authority:
- `domains/stock-market/flows/company-analysis.flow.md`
- `skills/xyool/00-mandatory-run-sequence.md`

Stock sequencing policy:
- discovery visibility precedes Quality exclusion;
- Quality precedes normal TTC capital competition;
- TTC must identify the actual causal gate before capital priority;
- economics/shareholder capture precedes payoff conclusions;
- thesis/current story precedes strategy expression;
- downstream capital/execution remains authority-gated;
- material character freshness must reach a barrier before final Story Reader/thesis closure;
- independent source/character refresh work may run in parallel when state dependencies allow;
- new evidence that invalidates an earlier result creates a new execution epoch rather than silently overwriting the completed path.

## Character / story configuration

Canonical core:
- `floware/core/character-system.flow.md`
- `floware/core/story-reader.flow.md`
- `floware/core/story-writer.flow.md`
- `floware/core/relational-story.flow.md`

Stock archetype vocabulary:
- `domains/stock-market/CHARACTER-ARCHETYPES.md`

Stock character policy:
- preserve quantitative and qualitative traits separately;
- archetypes are non-exclusive, dynamic hypotheses;
- UNCLASSIFIED / HYBRID / EMERGENT are valid;
- story role is root-relative and is not character identity;
- archetype is not capital authority.

Story Reader authority:
- reconstruct evidence-backed past → present state.

Story Writer authority:
- generate evidence-bounded conditional future branches from current state;
- no invented current facts;
- no calibrated numeric branch probability unless separately earned;
- always preserve material counter-story/failure branches.

## Domain identity

```text
Domain Name: stock-market
Domain Status: ACTIVE
Primary Objective: compound capital
Decision Maker / User: capital allocator / Xyool operator
Unit of Decision: capital allocation / position exposure
Objects / Entities: public companies, securities, catalysts, positions, counterparties, customers, regulators, programs, facilities
Observable Evidence: filings, issuer disclosures, regulator records, prices, volume, contracts, deployments, operating data, insider filings, market data, comparable events
Hidden / Latent State: true conversion probability, causal maturity, future economics, recognition gap, future price response, latent risks
```

## Important transitions

Examples include:

```text
signal → funding
integration → acceptance
acceptance → procurement
procurement → deployment
deployment → revenue / cash
repeat event → rollout / cadence
backlog → realization
submission → regulatory decision
capacity build → commissioning
fundamental change → market recognition
```

## Current decision architecture

Floware wrapper:

```text
GOAL / USER OBJECTIVE
→ STOCK COMPANY-ANALYSIS FLOW
→ relevant domain methods / evidence / state
→ QUALITY
→ TTC / PAYOFF / RECOGNITION
→ auditable output state
→ software only for justified hard limits / exactness
```

Economic authority chain remains:

```text
COMPANY-LEVEL XYOOL
→ OSE / FES
→ QUALITY QUALIFIER
→ BREADCRUMBS / CAUSAL TIMERS / PFS / RPT as TTC evidence
→ TTC + CATALYST PROFITABILITY
→ DESIRED ECONOMIC EXPOSURE
→ OSE ↔ QUANT INTERFACE
→ QUANT EXPRESSION / RISK CAP
→ EVENT EXECUTION POLICY
→ EXECUTABLE POSITION / CASH
```

Authority clarification:
- Quality decides normal capital eligibility.
- TTC owns capital priority / rotation and desired economic exposure.
- Quant is downstream risk/expression authority and may not exceed TTC desired exposure.
- Event Execution translates approved exposure into staged entry, harvest, trailing exit, time stop and evidence-gated re-entry.
- Legacy references to a separate `CAC` allocator in older OSE files are compatibility terminology; do not create a second allocator beside TTC.

Canonical compatibility / precedence map:
- `skills/xyool/stock-module-authority-map.md`

## Outcome / payoff

Primary payoff definition:

> probability-adjusted, shareholder-capturable, realizable capital return through time.

Primary failure / loss definitions include:
- permanent impairment;
- destructive dilution / financing;
- catalyst failure;
- delay / opportunity cost;
- poor shareholder capture;
- over-recognition / valuation compression;
- failed rotation;
- avoidable process misses;
- excessive drawdown or turnover from bad capital process.

## Capture

Capture means the extent to which corporate/operating economics accrue to the common shareholder after considering:
- dilution;
- debt;
- preferreds / warrants;
- capex;
- working capital;
- concentration;
- margin / cash conversion;
- governance;
- valuation already paid.

## Recognition / response

Recognition means how the market price responds to changing economics and uncertainty.

Internal profitability fields include:
- `P(Hit)`;
- `P(Material Price Move | Hit)`;
- conditional upside;
- failure / delay downside;
- already-priced state;
- recognition gap;
- price-response analogs;
- cascade dependencies and incremental gate recognition.

For the default human-facing Top-50 view, these are compressed into:

```text
Happens?
Profit View
```

`Happens?` is the chance of the economically favorable outcome or meaningful value-producing cascade progression during the displayed window.

`Profit View` is the probable stock-price move from the current price across the displayed catalyst/window. For cascade stocks it is cumulative across the modeled cascade window, with dependency and anti-double-counting controls. It is not theoretical best-case upside.

## Timing representation

For live Top-50, catalyst, and timeline work, Xyool must preserve the strongest evidence-supported timing internally and present it simply to the user.

Internal timing evidence hierarchy:

```text
VERIFIED EXACT DATE
→ VERIFIED COMPANY TARGET / DEADLINE
→ COMPANY-GUIDED WINDOW
→ XYOOL-INFERRED WINDOW
```

Human-facing Top-50 rule:

```text
exact verified day -> "Dec 17 EXACT"
exact company target -> "Sep 30 TARGET"
company-guided window -> show the stated window
Xyool-inferred / analog-derived window -> prefix with "~"
```

The default Top-50 table does not manufacture a synthetic single expected day when the exact day is unknown.

Human timing output must now preserve **two views**:

```text
1. SINGLE-DATE TIMERS
   exact event dates + explicit dated targets/deadlines

2. PRE-CATALYST WINDOWS
   evidence-supported active / approaching catalyst intervals
```

Sort each view **time first, Quality second**:

```text
single-date: nearest unresolved date -> Q5 to Q1 within same date
window view: earliest active/approaching window -> Q5 to Q1 within same time bucket
```

This ordering is for monitoring priority, not capital authority. TTC still owns capital priority.

A stock may appear in both views. An exact or target date does not eliminate the pre-catalyst window because economically meaningful events can resolve before the dated stop/deadline.

The pre-catalyst window is a first-class causal timer. It must be based on the same evidence hierarchy, PFS/Hazard where applicable, recognition state, and event/cascade identity. It must not be invented merely to surround a known event after the fact.

A naked `?` should not be used in the human-facing Top-50 timing column. If timing evidence is weak, widen the inferred `~window` until it honestly reflects the uncertainty and retain low timing confidence in the audit record.

Window inference may use, in descending preference:
1. company guidance;
2. contractual/regulatory bounds;
3. current causal stage;
4. same-company history;
5. same customer/process history;
6. close process/regulator/procurement analogs;
7. cross-company event-class analogs;
8. cadence inference;
9. broad event-class priors as a last resort.

Do not confuse timing confidence with catalyst-success probability.
Do not manufacture narrow timing from intuition or a mechanical midpoint.

Authoritative presentation standard:

- `skills/xyool/top50-exact-date-display-standard.md` — legacy filename; canonical human Top-50 display, timing, Q1-Q5 quality compression, cascade presentation, Happens?, and Profit View.

## Pre-funded event / entry treatment

For unscheduled funded orders, repeat procurement and existing-customer scope expansion, separate:

```text
PFS = maturity of the path to the exact funded event
Hazard Heat = proximity of that funded event
```

Do not infer time proximity from a high PFS state alone.

Current controlling files:
- `skills/xyool/pre-funded-event-hunter.md`
- `skills/xyool/pfs-promotion-standard.md`
- `skills/xyool/ttc-event-execution-policy.md`

HOT requires a current pre-outcome timing anchor under `pfs-promotion-standard.md`; price action, time passage, hindsight, or one repeat interval cannot create HOT.

The old universal `1/3 → 1/3 → 1/3` entry sketch is superseded for unscheduled funded events by the PFS × Hazard Heat ladder. Exact percentages remain provisional calibration.

## Cascade treatment

Some stocks should be modeled as linked value-unlocking cascades rather than isolated headlines.

Examples:

```text
SAT → acceptance → procurement → deployment → revenue
capacity activation → utilization → revenue
qualification → shipments → ramp
certification stage → approval → commercial service
```

For these names:
- identify the next chronological gate;
- identify the next economic-conversion gate;
- identify the next profit-producing gate;
- model later gates conditionally on upstream gates;
- update downstream probabilities when upstream gates resolve;
- do not double-count the same economics or recognition at multiple gates;
- display a window spanning the economically relevant cascade segment;
- make Profit View the cumulative probable price move across that segment rather than the reaction to only the first headline.

Cascade length alone is not a positive signal.

## Human-facing Top-50 display

Default format uses two timing sections:

```text
SINGLE-DATE TIMERS
Date | Stock | Q | Timer Type | Catalyst | Happens? | Profit View

PRE-CATALYST WINDOWS
~Window | Stock | Q | Catalyst | Happens? | Profit View
```

Within each section use **time first, Quality second**. Capital rank remains a separate TTC view.

Quality is displayed as `Q1` through `Q5`, with `↑` when explicitly improving. Native Quality state and capital-status detail remain in the audit record.

Do not include `Priced In` or `Stock Cares?` as default columns; those remain internal profitability inputs and should already affect Profit View.

## Persistent domain state / delta fetching

Stock-market live objects should resume from persistent state rather than reconstructing full company history on every run.

Canonical contracts:

- `skills/xyool/domain-state-persistence.md`
- `domains/stock-market/STATE.md`
- `domains/stock-market/state/index.json`

Operational sequence:

```text
LOAD stored stock snapshot
-> inspect active breadcrumbs / timers / unresolved questions
-> inspect source cursors and freshness
-> fetch only missing / stale / due source families
-> append new evidence
-> recompute affected derived state
-> update snapshot + cursors
-> report delta
```

Stored state is a cache with provenance, never authority. Current primary evidence supersedes stale stored state through an append + invalidate/supersede update; history is not silently rewritten.

For current price-sensitive requests, reuse stored causal/economic state, fetch current market data, and recompute recognition / Profit View without re-fetching old company history unless that history is itself stale or incomplete.

---

## Experimental / test-only market sidecars

The following are discoverable from the stock domain but are **not canonical capital logic**:

- `skills/xyool/market-expectations-execution-sidecar.md`
- Quant `V09 — Implied-Volatility Expected-Move Walls`
- `research/system-tests/2026-09-23-iv-wall-execution-sidecar-v1-spec.md`

V09 may test range calibration and execution timing only. It cannot create exposure, bypass Quality/TTC, or treat nominal wall containment as trading win-rate evidence.

---

## Domain-specific evidence

Important stock-market-only or market-heavy evidence includes:
- SEC filings;
- Form 4 / Form 144;
- 10b5-1 plans;
- share count / capital structure;
- price / volume;
- analyst estimate revisions where used;
- market valuation;
- portfolio correlation / volatility;
- transaction and tax friction.

These should not be exported to another domain merely because a correspondence exists at a higher level.

## Source hierarchy

Prefer, depending on claim:
1. regulators / primary filings;
2. issuer primary disclosures;
3. contractual / customer / agency evidence;
4. directly observable market data;
5. credible third-party evidence;
6. inference, clearly labeled.

Current facts require freshness checks.

## Anti-lookahead

Historical market testing must use only information available at the decision date.

Do not use future prices, filings, contracts, financing, share counts, outcomes, or eventual-winner identity.

## Miss handling

Use the canonical miss-to-question learning loop:

```text
freeze pre-outcome evidence
→ identify what was knowable
→ identify missing question/check
→ generalize
→ positive + negative controls
→ promote only if transferable
```

Timing-window misses and Profit View misses are calibration evidence. If an event lands materially outside its displayed window, or the realized price response falls materially outside the modeled move range, record the miss and inspect which timing, dependency, recognition, or move-size assumption failed.

## Current market-specific canonical modules

Primary current files include:
- `skills/xyool/00-00-START-HERE-XYOOL-PRIMER.md`
- `skills/xyool/00-01-PRINCIPLE-APPLICATION-PLAYBOOK.md`
- `skills/xyool/00-mandatory-run-sequence.md`
- `skills/xyool/xyool.md`
- `skills/xyool/architecture.md`
- `skills/xyool/stock-module-authority-map.md`
- `skills/xyool/opportunity-state-engine.md`
- `skills/xyool/ose-dual-confirmation.md`
- `skills/xyool/ose-sector-demand.md`
- `skills/xyool/ose-forward-evidence-state.md`
- `skills/xyool/ose-cascade-score.md`
- `skills/xyool/ttc-breadcrumb-to-timer-detection.md`
- `skills/xyool/causal-timer-framework.md`
- `skills/xyool/ttc-repeat-cadence-question.md`
- `skills/xyool/rollout-probability-timer.md`
- `skills/xyool/pre-funded-event-hunter.md`
- `skills/xyool/pfs-promotion-standard.md`
- `skills/xyool/time-to-catalyst.md`
- `skills/xyool/ttc-catalyst-profitability.md`
- `skills/xyool/contract-economic-ladder.md`
- `skills/xyool/ttc-event-execution-policy.md`
- `skills/xyool/ttc-evidence-tested-rules.md`
- `skills/xyool/ttc-insider-activity.md`
- `skills/xyool/conversion-debt.md`
- `skills/xyool/top50-exact-date-display-standard.md`
- `skills/xyool/quant-architecture.md`
- `skills/xyool/ose-quant-interface.md`

The current `skills/xyool/` directory must still be scanned for newer canonical modules.

## Principles that may be broader than markets

Candidates for correspondence testing include:
- exact identity before inference;
- source / freshness discipline;
- state-machine delta updates;
- causal gates and timers;
- early breadcrumb detection;
- repeat cadence;
- decay / overdue evidence;
- persistence versus observer response;
- anti-double-counting;
- miss-to-question learning;
- fail-closed handling of material unknowns;
- principle versus calibration distinction;
- positive + negative controls;
- explicit authority boundaries.

These are **correspondence candidates**, not automatically proven universal laws.

## Principles that are explicitly market-local unless redefined and revalidated

Examples:
- capital compounding as objective;
- shareholder capture;
- stock-price recognition;
- Form 4 / Form 144 / 10b5-1 interpretation;
- position sizing;
- earned capital versus new capital;
- harvest / rotation;
- portfolio volatility and correlation rules;
- market-specific Quant models;
- return-velocity calibration;
- event abnormal returns.

## Current calibration status

Market rules have mixed statuses: canonical process, provisional input, supported, rejected, or superseded. Numeric probability bands, universal event-response coefficients, PFS entry-rung percentages, decay constants, and cascade Profit View ranges remain provisional unless a current validation file says otherwise.

## Domain handoff instruction

When current work concerns stocks or public-market capital allocation:

1. load `XYOOL-START-HERE.md`;
2. load this manifest;
3. load `domains/stock-market/flows/README.md`;
4. select the applicable stock Flow;
5. load only the supporting skill/evidence/state needed by that Flow.

Do not begin by selecting Python/software components.

When work moves outside markets, do **not** reuse this manifest as the target-domain specification. Create/load the target domain manifest and construct explicit correspondence mappings.