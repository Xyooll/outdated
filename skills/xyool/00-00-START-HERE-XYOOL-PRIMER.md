# Xyool — START HERE Primer / Instructional Map

Status: **CANONICAL ORIENTATION + ROUTING DOCUMENT**

Purpose: this is the first document a new chat, analyst, agent, or future Xyool run should read before interpreting any individual Xyool module.

> **This primer explains what Xyool is, what it is trying to optimize, which principles are non-negotiable, how authority flows through the system, how misses become improvements, and where to find the authoritative detailed rules.**

This primer is a map, not a replacement for the underlying modules.

---

# 0. FIRST INSTRUCTION FOR EVERY FUTURE CHAT

Before performing material Xyool analysis:

1. Read `XYOOL-START-HERE.md`.
2. Load `floware/REGISTRY.md` and `floware/core/xyool-execution.flow.md`.
3. Identify the active domain and select its applicable `*.flow.md`.
4. Load this primer as supporting Xyool/domain doctrine.
5. Load only the skills, state, evidence, and correspondence required by the active Flow.
6. For stock work, `domains/stock-market/flows/company-analysis.flow.md` owns routing and `00-mandatory-run-sequence.md` owns the detailed mandatory gate specification.
7. Prefer the latest canonical Flow/rule over older research notes, legacy nodes, superseded names, or provisional hypotheses.
8. Before adding software, use `floware/core/software-escalation.flow.md`.

A future chat must not reconstruct Xyool from memory when the current repository is available.

---

# 1. WHAT XYOOL IS

Xyool is a **capital-compounding opportunity system**.

Its objective is not:
- to identify the most exciting company;
- to find the nearest catalyst;
- to maximize prediction accuracy;
- to maximize the number of winning stock calls;
- to chase price momentum;
- to rank stories.

Its objective is:

> **MAXIMIZE COMPOUNDED CAPITAL BY OWNING ONLY QUALIFIED OPPORTUNITIES AND DIRECTING CAPITAL TOWARD THE QUALIFIED OPPORTUNITY WITH THE STRONGEST TIME-ADJUSTED, PROBABILITY-ADJUSTED, SHAREHOLDER-CAPTURABLE REMAINING PAYOFF.**

The permanent asset is **capital**.

Stocks are temporary capital destinations.

A great company can be a poor capital destination at a particular price or time. A near catalyst can be a poor capital destination if it creates little economic value, is already priced, has poor shareholder capture, or has asymmetric failure downside.

---

# 2. THE AUTHORITY CHAIN

The active conceptual chain is:

```text
COMPANY-LEVEL XYOOL
        ↓
DISCOVERY VISIBILITY
(ESTABLISHED QUALITY ∪ HIDDEN TRANSITION)
        ↓
OPPORTUNITY STATE ENGINE (OSE)
        ↓
QUALITY QUALIFIER
        ↓
TIME TO CATALYST (TTC)
        ↓
DESIRED ECONOMIC EXPOSURE
        ↓
OSE ↔ QUANT INTERFACE
        ↓
QUANT EXPRESSION / RISK CONSTRAINTS
        ↓
EXECUTABLE POSITION / CASH
```

Authority boundaries are mandatory.

## Company-Level Xyool
Owns the company-specific causal business thesis:

```text
NEED → CONTROL → MOMENTUM → FRICTION → PRICE
```

It asks why asymmetric value could exist.

## Opportunity State Engine
Owns the dynamic evidence/opportunity state: structural confirmation, conversion confirmation, runway, forward evidence, cascade, recognition, friction, ignition, and related state transitions.

## Discovery Visibility
Owns **research visibility before Quality exclusion**.

Candidate generation is the union of:
- established-quality candidates;
- hidden-transition breadcrumb candidates.

A weak current Quality state may block capital, but may not by itself suppress a stock whose public breadcrumbs show a specific economically meaningful transition.

Canonical process:
- `discovery-visibility-gate.md`
- `ttc-breadcrumb-to-timer-detection.md`

## Quality Qualifier
Owns **normal capital eligibility after discovery visibility is established**.

Output:

```text
FAIL
WATCH
QUALIFIED
HIGH QUALITY
```

A near catalyst cannot rescue a failed or blocked Quality case.

## Time to Catalyst
Owns **capital priority, desired economic exposure, harvest, and rotation** among qualified opportunities.

FES, causal timers, catalyst profitability, insider context, recognition, and payoff persistence are TTC inputs. They are not separate allocation controllers.

## Quant
Owns empirical market/risk expression within TTC-approved exposure.

Quant may scale, constrain, delay, or express approved exposure under tested rules. Quant does not invent the economic thesis and does not create conviction above TTC authority.

---

# 3. THE NON-NEGOTIABLE XYOOL LAWS

These are the core principles every future chat should know before analyzing a stock.

## Law 1 — Discovery before Quality exclusion; Quality before capital timing

First ask:

> **Why should this stock remain visible long enough to evaluate?**

Candidate visibility is created by either:
- established current quality; or
- a causal hidden-transition breadcrumb with an economic path.

Then ask:

> **Should this equity compete for normal capital at all?**

Only after Quality is established should TTC ask where capital belongs now.

WATCH/FAIL names may remain visible as hidden-transition research candidates, but they must not silently compete with QUALIFIED/HIGH QUALITY names for normal capital.

## Law 2 — TTC is the capital-allocation / rotation layer

There is no separate generic allocator above or beside TTC.

FES and causal clocks feed TTC. They do not independently force trades.

## Law 3 — A catalyst is not valuable merely because it is close

Always separate:

```text
CATALYST PROXIMITY
P(HIT)
P(MATERIAL PRICE MOVE | HIT)
MOVE MAGNITUDE
FAILURE / DELAY DOWNSIDE
ALREADY-PRICED STATE
SHAREHOLDER CAPTURE
CURRENT / FULLY DILUTED EQUITY DENOMINATOR
REPRICING BURDEN
```

Chronological order and profitability priority are different outputs.

## Law 4 — Identify the actual causal clock

Do not use vague labels like `active now` when the next gate can be named.

Examples:

```text
integration → acceptance
acceptance → procurement
procurement → deployment
deployment → revenue / cash
qualification → production order
construction → commissioning
submission → regulatory decision
```

Each arrow can have a different timer and a different stock-price consequence.

## Law 5 — Multi-gate catalysts stay separate

For every material multi-gate catalyst, also build or update the dependency graph defined in `ttc-dependency-chain.md`. Identify the unresolved frontier gate(s), the designated primary gating node when justified, and the terminal economic node. Do not leave a known dependency chain only in prose.

Do not collapse:

```text
FIELD TEST
→ ACCEPTANCE
→ PROCUREMENT
→ DEPLOYMENT
→ REVENUE
```

into one event probability or one catalyst date.

Always distinguish when relevant:

```text
NEXT CHRONOLOGICAL EVENT
NEXT ECONOMIC CONVERSION EVENT
NEXT PROFIT-PRODUCING EVENT
PRIMARY GATING NODE
TERMINAL ECONOMIC NODE
```

They may be different.

## Law 6 — Exact event identity is mandatory

The event key is:

```text
COMPANY + PROGRAM/PROJECT + STAGE + DECISION MAKER + STOP EVENT
```

Evidence from another drug, defense program, facility, customer, security class, or stage cannot be transferred without explicit causal linkage.

## Law 7 — Freshness before confidence

Before using a hard date or live catalyst:
- verify from a primary source where practical;
- search for delay, extension, withdrawal, completion, financing, acquisition, or other superseding evidence;
- record what is current versus historical.

A stale catalyst is not a current catalyst.

## Law 8 — Close realized catalysts

When a timer realizes, close it.

Do not keep awarding an `imminent` bonus to an event that already happened.

After realization:
1. classify the economic payoff;
2. update recognition;
3. start the next causal clock only if evidence supports it.

## Law 9 — Economic persistence is not price-recognition persistence

A catalyst can create durable economics and weak stock performance.

A one-off event can create a large stock move.

Payoff persistence must be analyzed separately from market recognition.

Payoff states include:

```text
ONE-OFF REALIZATION
REPEATABLE DISCRETE
RUN-RATE ACTIVATION
STACKED / OVERLAPPING RUN-RATE
DECAYING / TERMINABLE RUN-RATE
```

## Law 10 — Do not double count economics

A contract signing and later activation are not two copies of the same economic value.

Do not count:
- contract value again at activation;
- backlog as revenue;
- revenue as cash;
- a guidance increase caused by the same economics as an independent new stream;
- the same insider transaction separately across Form 4 and Form 144.

## Law 11 — Breadcrumbs can arm clocks before the headline catalyst

Do not wait for the final order if public evidence already shows a specific causal transition forming.

Core question:

> **What breadcrumb is this, what timer does it start, and what would confirm or kill it?**

A breadcrumb is useful only if it changes the probability, stage, or expected timing of an economically meaningful transition.

Use the transition, delta, agency/commitment, clock, falsifiability, and economic-link tests.

`Verbs beat adjectives` is a heuristic, not proof.

## Law 12 — Repeat events create a timing question

Whenever a material economic event appears repeatable, ask:

> **What repeats, and when could it repeat again?**

One observed interval creates at most an **Emerging** cadence unless stronger independent evidence exists.

Do not turn one interval into a guaranteed schedule.

## Law 13 — Cascade state and repeat timing are different

Cascade asks:

> **Is replication happening?**

Repeat-cadence asks:

> **What does the time spacing imply about the next plausible repeat?**

Do not double count the same event across Cascade, FES, cadence, and TTC.

## Law 14 — Insider activity must be classified, not merely noticed

For material catalyst windows, classify insider activity when available.

Distinguish:
- discretionary purchase;
- discretionary sale;
- 10b5-1 planned sale;
- tax withholding / sell-to-cover;
- option exercise;
- gift / trust / estate transfer;
- clustered activity.

For 10b5-1 activity, track separately:

```text
PLAN ADOPTION
PLAN MODIFICATION / TERMINATION
TRADE EXECUTION
```

The adoption decision can be more informative than an execution near the catalyst.

Do not infer misconduct or private knowledge from timing alone.

## Law 15 — Shareholder capture matters more than headline economics

For every catalyst ask what shareholders actually capture after:
- dilution;
- debt;
- warrants / preferreds;
- capex;
- working capital;
- financing needs;
- concentration;
- margin / cash conversion;
- valuation already paid.

Program size, TAM, ceilings, and optional maximums are not per-share value.

Apply `ttc-repricing-threshold.md` when catalyst profitability depends materially on company size. A small absolute event can be highly price-sensitive when the current/fully diluted equity denominator is tiny. Conversely, a falling basic market cap caused by expanding dilution is not clean compression.

## Law 16 — Funded/committed economics outrank ceilings and aspirations

Keep separate:

```text
FUNDED / COMMITTED
EXPECTED BUT UNFUNDED
CEILING / OPTION
PIPELINE
TAM
MANAGEMENT ASPIRATION
```

Never silently convert optional economics into backlog or revenue.

For contract-like catalysts, apply the canonical Contract Economic Ladder in `contract-economic-ladder.md`:

```text
CE0 access only
→ CE1 optioned economic surface
→ CE2 funded / committed order
→ CE3 backlog / delivery conversion
→ CE4 revenue conversion
→ CE5 profit / cash / shareholder conversion
```

Always distinguish **Optioned Economic Surface** from **Committed Economic Value**. A large ceiling, vehicle, framework, program maximum, or shared IDIQ can increase strategic potential without creating funded revenue.

## Law 17 — New capital and earned capital are different

**New capital** competes aggressively for the best qualified TTC opportunity.

**Earned capital** already inside an intact qualified position has a higher removal hurdle.

A slightly better new ranking is not sufficient reason to liquidate an intact holding.

## Law 18 — Current holding versus candidate must be compared symmetrically

A full rotation cannot be based on candidate-only catalyst analysis.

Inventory unresolved material catalysts in the current holding and compare both sides on:
- Quality;
- catalyst maturity;
- evidence freshness;
- materiality;
- conversion window;
- recognition gap;
- expected payoff;
- downside;
- shareholder capture;
- liquidity / transaction friction.

Fresh, material, late-stage current-holding catalysts raise the replacement hurdle.

## Law 19 — Price acceleration is recognition evidence, not thesis proof

Before adding to a rising stock ask:

> **Did the underlying economic opportunity improve faster than the price?**

Momentum can corroborate ignition/recognition but cannot create the economic thesis.

## Law 20 — No opaque master score until validated

Xyool may calculate transparent ranges and compare dimensions.

Do not compress the system into a universal numeric score, multiplier, or probability if the empirical validation has not earned it.

## Law 21 — Anti-lookahead is mandatory

At every historical decision point, use only information available then.

Never use future:
- contracts;
- prices;
- earnings;
- share counts;
- financings;
- corporate actions;
- eventual winners;
- later narrative explanations.

A later outcome does not prove it was predictable beforehand.

## Law 22 — Diagnose apparent failure before learning from it

Supporting doctrine: `meta-failure-flow.md`.

A bad outcome or apparent miss is not automatically a system failure. First establish what contract was expected, what was knowable before the outcome, and the first broken layer.

```text
APPARENT MISS / BAD OUTCOME
→ FREEZE / RECONSTRUCT PRE-OUTCOME INFORMATION
→ IDENTIFY EXPECTED CONTRACT
→ TEST KNOWABILITY
→ TRACE EVIDENCE → STATE → DECISION
→ CLASSIFY CONFIRMED / EXONERATED / UNRESOLVED
→ ONLY IF A DEFECT IS CONFIRMED:
     RESEARCH RELEVANT EXISTING METHODS / FAILURES
     KEEP COMPETING EXPLANATIONS ALIVE
     IDENTIFY THE MOST-INFORMATIVE DISCRIMINATING TEST
     DEVELOP A GENERALIZABLE QUESTION / STATE / METHOD ONLY IF SUPPORTED
     FREEZE
     TEST POSITIVE + NEGATIVE + REGRESSION CONTROLS
     PROMOTE / SIMPLIFY / REJECT ONLY FROM FRESH EVIDENCE
```

The goal is to eliminate avoidable process/model defects without fitting history, blaming downstream layers for upstream failures, or rewriting Xyool around randomness and legitimate uncertainty.

## Law 22A — Evidence is a prior, not a closed search space

Existing research and prior Xyool success constrain belief, but do not become permanent law.

When progress plateaus, repeated anomalies persist, models agree while reality disagrees, regime relevance changes, or complexity rises without gain, Xyool may enter **Frontier Experimentation Mode**.

Frontier Mode may search novel representations, interactions, methods, horizons, reversed assumptions, and correspondence-derived hypotheses.

Hard boundary:

> **Frontier experimentation gets freedom of exploration, not freedom of authority.**

Novel outputs begin RESEARCH ONLY / SHADOW ONLY. Fresh target-domain validation is required before authority increases.

Canonical reference: `00-06-EVIDENCE-DIRECTED-FRONTIER-RLE.md`.

## Law 23 — Governance status matters

Every rule/hypothesis should be identifiable as one of:

```text
CANONICAL PROCESS
PROVISIONAL INPUT
RESEARCH ONLY
REJECTED
SUPERSEDED
```

Canonical process must be followed.

Provisional numeric bands, event priors, weights, and thresholds must not be presented as established facts.

Rejected ideas stay rejected unless new evidence justifies reopening them.

## Law 24 — Missing mandatory steps fail closed

For Top-50 ranking, material capital decisions, and catalyst profitability ranking, every mandatory gate in `00-mandatory-run-sequence.md` must be marked:

```text
PASS
NOT APPLICABLE — reason required
BLOCKED — missing evidence named
FAIL
```

Blank is prohibited.

A skipped mandatory step means:

> **INCOMPLETE / FAIL CLOSED**

## Law 25 — The objective is compounded capital, not elegance

A model improvement is valuable only if it improves capital decisions, research coverage, timing calibration, risk control, or realized outcomes without unacceptable false positives, drawdown, turnover, or hindsight fit.


## Law 26 — Freeze the goalpost

Before a major development program, freeze:
- the exact goal;
- success gates;
- method-failure gates;
- boundaries;
- effectiveness standard;
- efficiency standard;
- complexity budget.

A failed method does not permit a new goal. Preserve the failure, change the approach, and continue toward the same frozen objective.

A new goal may begin only after the current goal is achieved or the goal itself is formally invalidated by evidence.

Canonical reference: `00-07-GOALPOST-EFFECTIVENESS-GOVERNANCE.md`.

## Law 27 — Effectiveness within reason beats perfection

Xyool does not optimize for theoretical perfection.

The design objective is:

> **Evidence-backed effectiveness sufficient for the decision, achieved with reasonable complexity, research burden, computation, latency, and maintenance.**

Streamlining, efficiency, simplification, and removal are valid forms of optimization.

If a simpler architecture performs materially similarly to a more complex one, prefer the simpler architecture.

Every added layer must earn measurable incremental value.


## Law 28 — Use Floware for intelligence; software for certainty

Xyool is an AI-native system.

Do not automatically translate adaptive reasoning into software.

Use **Floware** for:
- goal-directed reasoning;
- evidence-sensitive routing;
- state interpretation;
- adaptive planning;
- causal analysis;
- correspondence;
- recursive learning.

Use **software** for:
- exact calculation;
- persistence;
- schemas;
- APIs;
- transactions;
- permissions;
- security;
- deterministic validation;
- hard financial, physical, or safety limits.

Canonical stack:

```text
GOAL
  ↓
FLOWARE
adaptive reasoning / planning / routing
  ↓
SOFTWARE
deterministic guarantees / hard limits
  ↓
HARDWARE
execution / compute / sensors / actuators
```

Canonical reference: `00-08-FLOWARE-AI-NATIVE-ARCHITECTURE.md`.

Code is not the default implementation of a new Xyool idea. It must earn its maintenance and complexity cost.

---

# 4. MANDATORY LIVE-RUN ORDER

The detailed authority is `00-mandatory-run-sequence.md`.

Every material live run should complete, in order:

```text
0. SOURCE / FRESHNESS LOCK
1. COMPANY + SECURITY IDENTITY
2. QUALITY QUALIFIER
3. MATERIAL CATALYST INVENTORY
4. EVENT-INTEGRITY VALIDATION
5. CAUSAL TIMER / NEXT-GATE MAPPING
6. INSIDER-ACTIVITY CONTEXT
7. CATALYST ECONOMICS / SHAREHOLDER CAPTURE
8. CATALYST PROFITABILITY OBJECT
9. RECOGNITION / PRICE-RESPONSE EVIDENCE
10. DOWNSIDE / INVALIDATION / DELAY STATE
11. CURRENT-HOLDING / REPLACEMENT-HURDLE COMPARISON
12. QUANT EXPRESSION WHEN EXECUTABLE EXPOSURE IS CONSIDERED
13. FINAL COMPLETENESS AUDIT
```

No future chat should jump from `interesting catalyst` directly to `rank` without this sequence.

---

# 5. CATALYST PROFITABILITY — THE CURRENT TTC FOCUS

A catalyst only matters to capital if it can plausibly produce realizable shareholder profit.

For each material unresolved catalyst, record where evidence permits:

```text
P(Hit)
P(Material Price Move | Hit)
Conditional Upside Range
Conditional Failure / Delay Downside
P(Delay / No-Decision)
Expected Event Window
Surprise State
Already-Priced State
Economic Materiality vs Equity / EV
Per-Share Capture
Payoff Persistence
Liquidity / Exit Friction
Confidence
Analog Set
```

Use specific price-response analogs in this order when possible:

1. same company + same catalyst type;
2. same company + economically similar event;
3. same customer/regulator/mechanism + close peer;
4. close event archetype;
5. broad event-study prior only as fallback.

Do not invent precise probabilities where analog evidence is weak.

---

# 6. CAUSAL TIMER MAP

Authoritative frameworks:
- `causal-timer-framework.md`
- `ttc-dependency-chain.md` for multi-gate prerequisite structure and gating-node detection.

Current timer taxonomy includes:
- Signal-to-Funding;
- Integration-to-Acceptance;
- Acceptance-to-Procurement;
- Procurement-to-Deployment;
- Deployment-to-Revenue / Cash;
- Rollout Probability Timer (RPT);
- Reference-Customer Cascade;
- Replenishment;
- Capacity-Build;
- Backlog-Conversion;
- Regulatory / Administrative;
- Institutionalization;
- Financing / Runway;
- Catalyst Decay / Overdue;
- Management Timing Credibility;
- Recognition;
- Existing-Customer Scope Expansion.

The active TTC bottleneck is usually the **next unresolved material gate**, not an average of every clock.

---

# 7. FORWARD EVIDENCE / EARLY DETECTION

## FES
Authoritative module: `ose-forward-evidence-state.md`.

FES asks what economically meaningful event is forming, how advanced it is, how strong the evidence is, and whether velocity is improving or weakening.

FES informs TTC. It does not independently allocate capital.

## Breadcrumb-to-Timer Detection
Authoritative module: `ttc-breadcrumb-to-timer-detection.md`.

Use when weak-but-causal public evidence may justify WATCHING, ARMING, or ACTIVATING a timer before a headline catalyst.

## Cascade
Authoritative module: `ose-cascade-score.md`.

Use to determine whether adoption is replicating across sites, units, programs, customers, or geographies.

## Repeat Cadence
Authoritative module: `ttc-repeat-cadence-question.md`.

Mandatory question when repeat evidence exists:

> **What repeats, and when could it repeat again?**

## Rollout Probability Timer
Authoritative module: `rollout-probability-timer.md`.

Use to interpret where a repeatable rollout sits relative to an evidence-backed next-repeat window. Do not assume probability rises forever; overdue windows decay.

`ttc-window-proximity.md` is a compatibility/superseded-name pointer to RPT, not a separate modern concept.

---

# 8. ECONOMIC CONVERSION / PAYOFF MAP

## Catalyst Materiality
Evaluate funded/capturable economics relative to current equity value, enterprise value, and earnings/cash base.

## Payoff Persistence
Authoritative treatment lives in `causal-timer-framework.md` and supporting TTC tests.

Ask what economic state exists **after** the timer realizes.

## Reusable Asset Monetization (RAM)
Detailed handling lives in `time-to-catalyst.md`.

Rental/reusable-asset revenue can support economics while a catalyst develops, but it is not SaaS and does not substitute for procurement conversion.

## Conversion Debt
Authoritative module: `conversion-debt.md`.

Use when a company accumulates promises/backlog/capacity/funding that still requires conversion into realized economics.

---

# 9. INSIDER / GOVERNANCE CONTEXT

Authoritative module: `ttc-insider-activity.md`.

Mandatory principle:

> **Insider sale != bearish signal until transaction context is classified.**

10b5-1 executions are not ignored; they are interpreted through plan adoption/modification/execution history.

Insider context can modify confidence, downside assumptions, shareholder-capture confidence, and research priority. It does not create independent capital authority.

---

# 10. CAPITAL ROTATION PRINCIPLES

Authoritative modules:
- `time-to-catalyst.md`
- `ttc-evidence-tested-rules.md`

Key principles:

### New capital
Competes for the strongest qualified TTC opportunity now.

### Earned capital
Requires a higher hurdle to remove.

### Replacement hurdle
A candidate must remain materially superior after valuing the current holding's unresolved catalysts.

### Close comparisons
When the differential is small, prefer:

```text
HOLD CURRENT
PARTIAL ROTATION
NEW CAPITAL TO CANDIDATE
```

over unnecessary full replacement.

### Aggressive constant reshuffling
Not established as a generic edge and should not be treated as one.

---

# 11. QUANT ROLE

Authoritative modules:
- `quant-architecture.md`
- `quant-layer.md`
- `quant-production-defaults.md`
- `quant-model-catalog.md`
- `quant-tournament.md`
- `ose-quant-interface.md`

Principle:

> **Quality decides eligibility. TTC decides desired economic exposure. Quant decides how that approved exposure can be expressed under measured market risk.**

Quant does not create a broken thesis or add exposure beyond TTC authority.

Use the current repo version and current frozen/tested defaults. Do not reconstruct old Quant settings from chat memory.

---

# 12. RESEARCH / TEST GOVERNANCE

Authoritative modules:
- `miss-to-question-learning-loop.md`
- `principle-question-documentation-standard.md`
- `ttc-evidence-tested-rules.md`

Research rules:

1. Freeze the information set before testing historical decisions.
2. Separate hypothesis generation from validation.
3. Preserve failures.
4. Use positive and negative controls.
5. Prefer untouched holdouts.
6. Do not optimize thresholds to one winner.
7. Do not promote a numeric rule merely because it explains a recent move.
8. Record authority and validation status.
9. Rejected hypotheses remain visible so the system does not relearn the same false rule.
10. A principle may be canonical while its numeric calibration remains provisional.

---

# 13. TOP-50 OUTPUT RULES

A Top-50 is not merely a ranked list of interesting companies.

At minimum preserve, where applicable:

```text
Rank
Ticker / Company
Quality State
Capital Status
Highest Material Unresolved Catalyst
Next Chronological Event
Next Economic Conversion Event
Next Profit-Producing Event
Expected Window / Hard Date
Timing Type
Event-Integrity State
Causal Stage / FES
Window Position / Decay
Remaining Gates
Catalyst Materiality
P(Hit)
P(Material Price Move | Hit)
Conditional Upside
Failure / Delay Downside
Already-Priced State
Payoff Persistence
Insider Context
Recognition Gap
Return Velocity / Profitability Priority
Confidence
Next Decision Trigger
Completeness State
```

A WATCH/FAIL name can appear for research relevance but must remain clearly capital-blocked unless Quality changes.

Chronological ranking and profitability ranking must not be silently merged.

---

# 14. HOW TO HANDLE A NEW EVENT

For material company news:

```text
OLD STATE
   ↓
NEW EVIDENCE
   ↓
WHAT CHANGED?
   ↓
EVENT IDENTITY + FRESHNESS
   ↓
QUALITY CHANGED?
   ↓
OSE / FES STATE CHANGED?
   ↓
CATALYST STAGE / TIMER CHANGED?
   ↓
PROBABILITY / MATERIALITY CHANGED?
   ↓
PAYOFF PERSISTENCE CHANGED?
   ↓
RECOGNITION / PRICE RESPONSE CHANGED?
   ↓
INSIDER / SHAREHOLDER-CAPTURE CONTEXT CHANGED?
   ↓
DOWNSIDE / INVALIDATION CHANGED?
   ↓
TTC RETURN-VELOCITY / PROFITABILITY PRIORITY
   ↓
CURRENT vs CANDIDATES vs CASH
   ↓
QUANT EXPRESSION IF APPLICABLE
```

Do not blindly rescore from scratch when a state-machine delta is more informative.

---

# 15. HOW TO HANDLE A MISS

Authoritative module: `miss-to-question-learning-loop.md`.

Every material miss should be classified first:
- unknowable outcome;
- research-coverage miss;
- identity/freshness miss;
- causal-connection miss;
- timer/calibration miss;
- quality miss;
- catalyst-profitability miss;
- shareholder-capture miss;
- recognition miss;
- rotation/replacement-hurdle miss;
- Quant expression miss;
- process-omission miss.

Then ask:

> **What question, check, state field, or evidence requirement would have forced Xyool to notice the relevant information before the outcome was known?**

Promote the general question only after it survives controls.

Never patch around the identity of the latest winner or loser.

---

# 16. FAIL-CLOSED CONDITIONS

A final Xyool capital ranking should be marked incomplete when any material required item is unknown and could plausibly change the result.

Examples:
- Quality not assessed;
- catalyst program identity ambiguous;
- hard date unverified;
- newer superseding evidence not checked;
- realized catalyst still carried as unresolved;
- causal next gate unknown;
- material insider activity visible but unclassified;
- funded economics confused with ceiling/TAM;
- failure downside omitted;
- current holding not compared before rotation;
- required Quant state unavailable for executable sizing;
- mandatory step left blank.

Unknown is acceptable.

Silently skipped is not.

---

# 17. MODULE ROUTING MAP

This is the current routing map. Future chats must still scan the directory for newer modules.

| Need | Primary module |
|---|---|
| Start-here orientation | `00-00-START-HERE-XYOOL-PRIMER.md` |
| Mandatory execution order / no skipped steps | `00-mandatory-run-sequence.md` |
| Full Xyool company research framework | `xyool.md` |
| System authority / architecture | `architecture.md` |
| Dynamic opportunity state | `opportunity-state-engine.md` |
| Sector demand | `ose-sector-demand.md` |
| Structural + conversion confirmation | `ose-dual-confirmation.md` |
| Forward evidence state | `ose-forward-evidence-state.md` |
| Cascade / replication | `ose-cascade-score.md` |
| Causal timer taxonomy / payoff persistence | `causal-timer-framework.md` |
| Early breadcrumb detection | `ttc-breadcrumb-to-timer-detection.md` |
| Repeat timing | `ttc-repeat-cadence-question.md` |
| Rollout timing probability | `rollout-probability-timer.md` |
| TTC capital allocation / rotation | `time-to-catalyst.md` |
| Tested / rejected TTC rules | `ttc-evidence-tested-rules.md` |
| Catalyst price/profitability layer | `ttc-catalyst-profitability.md` |
| Insider activity / 10b5-1 | `ttc-insider-activity.md` |
| Conversion promises vs realization | `conversion-debt.md` |
| Quant authority / architecture | `quant-architecture.md` |
| Quant models / risk logic | `quant-layer.md` |
| Quant model inventory | `quant-model-catalog.md` |
| Frozen production defaults | `quant-production-defaults.md` |
| Quant model selection/testing | `quant-tournament.md` |
| OSE ↔ Quant authority | `ose-quant-interface.md` |
| Miss learning | `miss-to-question-learning-loop.md` |
| New-principle documentation standard | `principle-question-documentation-standard.md` |
| Legacy window-proximity name | `ttc-window-proximity.md` → use RPT |

Research/system-test files under `research/system-tests/` are evidence and regression records. They do not automatically outrank canonical skill files.

---

# 18. WHAT A FUTURE CHAT SHOULD SAY WHEN UNCERTAIN

Use explicit states such as:

```text
UNKNOWN
INSUFFICIENT EVIDENCE
BLOCKED
PROVISIONAL
INFERRED — LOW CONFIDENCE
COMPANY-GUIDED
HARD DATE — PRIMARY SOURCE VERIFIED
```

Do not fill missing evidence with confidence language.

Do not manufacture precise probabilities because the user asked for a rank.

A useful incomplete answer is better than a falsely complete one.

---

# 19. VERSION / SOURCE DISCIPLINE

When the user asks to use Xyool:

1. Use the current GitHub repository version when available.
2. Do not claim a revision number from memory.
3. Prefer canonical `skills/xyool/` files over old conversational reconstructions.
4. Use research tests to understand validation history, not to override newer canonical rules.
5. When a concept has been superseded, use the current canonical name while preserving compatibility references.
6. Record material changes as repo changes rather than relying on chat memory.

---

# 20. ONE-SCREEN XYOOL SUMMARY

```text
OBJECTIVE
Compound capital.

FIRST GATE
Quality: should we own it at all?

SECOND GATE
TTC: where should qualified capital be now?

TIMING
Use causal gates, not vague dates.

PROFITABILITY
P(hit) × P(price move | hit) × magnitude
minus failure/delay downside,
subject to what is already priced and what shareholders capture.

EARLY SIGNALS
Turn causal breadcrumbs into explicit timers.

REPEATS
Ask: what repeats, and when could it repeat again?

REALIZED EVENTS
Close old timer; classify payoff; start next supported clock.

INSIDERS
Classify mechanism; 10b5-1 adoption != execution.

ROTATION
New capital competes aggressively; earned capital has a higher removal hurdle.

QUANT
Express TTC-approved exposure; do not invent thesis conviction.

MISSES
Freeze → identify missing question → generalize → test controls → promote only if transferable.

DISCIPLINE
No skipped mandatory steps. Missing = fail closed.
```

---

# 21. FINAL INSTRUCTION

When a future chat is asked to “run Xyool,” “rank the Top 50,” “compare two stocks,” “find the next one to pop,” “test a catalyst,” or “decide where capital should go,” it should begin from this map and then execute the current mandatory sequence using the authoritative modules.

The system should remain willing to say:

> **The opportunity is interesting, but the evidence is not complete enough to rank capital yet.**

That is preferable to skipping a gate.

Final principle:

> **XYOOL IS A DISCIPLINED CAPITAL PROCESS, NOT A COLLECTION OF STOCK SIGNALS.**
