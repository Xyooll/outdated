# Xyool — Mandatory Run Sequence

Status: **CANONICAL STOCK GATE SPECIFICATION / FAIL CLOSED**

Floware execution wrapper:
`domains/stock-market/flows/company-analysis.flow.md`

Meta sequencing controller:
`floware/meta/sequencing.flow.md`

Role:
- this file owns the detailed mandatory stock-analysis gates and domain-required precedence;
- the Flow owns adaptive routing through those gates;
- Sequencing determines readiness, safe parallelism, barriers, and re-entry while preserving these domain gates;
- software does not own the reasoning sequence.


## Purpose

Xyool has accumulated specialized modules that can each be correct while a live analysis is still wrong because a required step was skipped.

This specification exists to prevent **process omission**.

It is executed as Floware: the AI adapts the route to the case while preserving every material gate and fail-closed condition.

> **No final Xyool capital ranking is valid unless every mandatory gate below is explicitly completed, marked not applicable with a reason, or marked blocked.**

A missing step is not neutral. A missing mandatory step means the analysis is **INCOMPLETE / FAIL CLOSED**.

This checklist is a completion/gate contract, not a requirement that every operation be executed serially.

Sequencing may parallelize independent work, for example:
- refreshing independent material characters;
- gathering unrelated source families;
- preparing independent evidence branches.

It may not parallelize across a hard semantic/authority dependency in a way that allows downstream conclusions to finalize early.

This protocol does not create a new scoring layer. It enforces the existing authority chain:

```text
COMPANY-LEVEL XYOOL
→ OSE / FES
→ QUALITY QUALIFIER
→ TTC
→ QUANT EXPRESSION
```

---

## Non-skippable rule

For every stock considered for Top-50 ranking, initiation, increase, reduction, harvest, or rotation, produce a completion ledger:

```text
[ ] 0A. Persistent domain-state load / refresh plan
[ ] 0. Source / freshness lock
[ ] 1. Company + security identity
[ ] 1A. Discovery visibility / breadcrumb intake
[ ] 1B. Corporate entity / subsidiary attribution when applicable
[ ] 2. Quality qualifier + trajectory / unlock / survival
[ ] 3. Material catalyst inventory
[ ] 4. Event-integrity validation
[ ] 5. Dependency graph / causal timer / next-gate mapping
[ ] 6. Insider-activity context
[ ] 7. Catalyst economics / shareholder capture
[ ] 8. Catalyst profitability / repricing burden
[ ] 9. Recognition / price-response evidence
[ ] 9A. Multi-method / market-structure shadow capture
[ ] 10. Downside / invalidation / delay state
[ ] 11. Current-holding / replacement-hurdle comparison when applicable
[ ] 12. Quant expression when executable exposure is being considered
[ ] 13. Final completeness audit
[ ] 14. Deep-analysis memory ingestion when analysis/state materially changes
```

Allowed step states:

```text
PASS
NOT APPLICABLE — reason required
BLOCKED — missing evidence named
FAIL
```

**Blank is prohibited.**

---

## 0A. Persistent domain-state load / refresh plan

For a cataloged stock, before external research:

1. load the persistent stock snapshot and active timers;
2. inspect source cursors / freshness;
3. build a refresh plan;
4. reuse fresh stored evidence;
5. fetch only source families that are missing, stale, due, unknown, or explicitly require independent re-verification.

Canonical state contracts:
- `skills/xyool/domain-state-persistence.md`
- `domains/stock-market/STATE.md`

Runtime read tools where available:
- `domain_state_get`
- `domain_state_dependency`
- `domain_state_refresh_plan`
- `domain_state_due`

If the stock is not cataloged, mark:

```text
NOT APPLICABLE — NEW ENTITY
```

then establish identity/current state and seed the persistent record after the analysis.

Stored state is prior processed evidence, not current authority. A fresh primary-source contradiction must supersede the cached fact through the provenance-preserving update process.

---

## 0. Source / freshness lock

Before analysis:
- record analysis date;
- use the Step 0A refresh plan when the entity is cataloged;
- retrieve only the latest filing / issuer evidence needed to refresh stale/due thesis fields;
- search for superseding events, delays, completions, financings, acquisitions, guidance changes, or material adverse updates;
- distinguish current facts from older historical evidence.

Question:
> **What could have changed since the evidence that originally put this company in Xyool?**

A stale source cannot support a current hard-date claim without a freshness check.

---

## 1. Company + security identity

Confirm:
- ticker;
- legal company name;
- exchange / security class where relevant;
- corporate actions / ticker changes where relevant;
- exact program / product / project being discussed.

Never transfer evidence across:
- different drug programs;
- different defense programs;
- different customers;
- different facilities;
- different security classes;
- predecessor / successor entities without explicit linkage.

---

## 1A. Discovery visibility / breadcrumb intake — MUST OCCUR BEFORE QUALITY EXCLUSION

Purpose:
> **Prevent the Quality gate from hiding a stock before Xyool evaluates a credible hidden economic transition.**

Candidate generation must use:

```text
ESTABLISHED-QUALITY SCREEN
        UNION
HIDDEN-TRANSITION BREADCRUMB SCREEN
        ↓
VISIBLE RESEARCH CANDIDATES
```

Apply `skills/xyool/discovery-visibility-gate.md`, `skills/xyool/sec-filing-company-memory.md`, and the breadcrumb six-test filter.

For broad stock discovery, the intake set must include current SEC filing signals where available:
- insider filings;
- corporate-event filings;
- operating filings;
- ownership filings;
- financing/shareholder-capture filings;
- late-filing/listing-risk filings.

A Form 4 or other SEC event can originate a candidate before Quality is known.

A candidate may remain visible even when current Quality is poor if public evidence supports:
- a specific causal transition;
- an economically meaningful stop event;
- a falsifiable path;
- a dependency path toward shareholder value;
- at least plausible survival to the unlock.

Output:

```text
DISCOVERY LANE:
BREADCRUMB:
CAUSAL TRANSITION:
ECONOMIC TERMINAL:
VISIBILITY STATUS:
```

Allowed visibility statuses:

```text
DISCOVERY_VISIBLE
WATCHING
VISIBLE_RISK
REJECT_NON_CAUSAL
```

Rule:

> **Quality may block capital. Quality may not, by itself, block discovery.**

This step has no independent capital authority.

---

## 1B. Corporate entity / subsidiary attribution — CONDITIONAL BUT NON-SKIPPABLE WHEN APPLICABLE

If material evidence originates from a subsidiary, JV, segment, program, customer relationship, or legal entity other than the listed parent:

- identify the exact legal/event entity;
- establish an evidence-backed relationship path to the public parent/security;
- record ownership percentage where known;
- record consolidated vs unconsolidated treatment where known;
- identify the reporting segment/program;
- use the correct economic denominator before assigning parent-company materiality.

Use `agent/corporate_entity_graph.py` / the persistent corporate entity graph where available.

A subsidiary/customer/program headline must not be silently treated as a direct parent-company event.

Allowed result:

```text
DIRECT_PARENT_EVENT
CONSOLIDATED_ENTITY_PATH
PARTIAL_OWNERSHIP_PATH
ATTRIBUTION_PATH_FOUND
UNKNOWN_OR_UNLINKED
NOT APPLICABLE — direct parent/security evidence
```

`UNKNOWN_OR_UNLINKED` blocks hard economic attribution but does not block discovery.

---

## 2. Quality qualifier — MUST OCCUR BEFORE TTC RANKING

Output one:

```text
FAIL
WATCH
QUALIFIED
HIGH QUALITY
```

At minimum test:
- discovery lane / reason the stock remained visible;
- real demand;
- company capture/control;
- structural confirmation;
- conversion confirmation;
- balance sheet / financing durability;
- dilution / governance;
- shareholder capture;
- permanent-impairment risk;
- valuation / asymmetry;
- evidence quality;
- Quality trajectory: IMPROVING / STABLE / DETERIORATING / BINARY-DEPENDENT / UNKNOWN;
- Quality unlock condition;
- Survival to Unlock: PASS / WATCH / FAIL / UNKNOWN;
- post-unlock shareholder-capture question.

Rule:
> **A near catalyst cannot rescue a failed or blocked Quality case.**

But a failed/blocked current Quality state does **not** erase a candidate that passed Step 1A. It remains visible for hidden-transition research, Quality-unlock tracking, and risk monitoring.

WATCH / FAIL names may remain on a research timeline but cannot silently compete with qualified names for normal TTC capital.

---

## 3. Material catalyst inventory

List **all material unresolved catalysts**, not just the most convenient one.

For each catalyst identify:
- program / project;
- event type;
- current stage;
- next gate;
- whether clocks are sequential or independent;
- whether the prior clock already realized and must be closed.

Do not average parallel catalysts into one vague date.

Output separately:

```text
NEXT CHRONOLOGICAL EVENT
NEXT ECONOMIC CONVERSION EVENT
NEXT PROFIT-PRODUCING EVENT
PRIMARY GATING NODE
TERMINAL ECONOMIC NODE
```

They may be different.

---

## 4. Event-integrity validation

Apply `ttc-catalyst-profitability.md` Event Integrity Lock.

Required event key:

```text
COMPANY + PROGRAM/PROJECT + STAGE + DECISION MAKER + STOP EVENT
```

For hard dates or company-guided windows:
- verify from a primary source;
- search for extension / delay / withdrawal / completion / superseding transaction;
- record last freshness check;
- close realized events immediately.

If exact identity cannot be preserved, **FAIL CLOSED** on the catalyst ranking.

---

## 5. Dependency graph / causal timer / next-gate mapping

Use the actual causal clock, not the headline event.

Examples:

```text
acceptance → procurement
procurement → deployment
deployment → revenue
qualification → production order
construction → commissioning
submission → regulatory decision
```

For any material multi-gate catalyst, apply `ttc-dependency-chain.md` before assigning TTC priority.

Record:
- dependency nodes and required/supporting edges;
- satisfied versus unresolved nodes;
- frontier gate(s);
- primary gating node and rationale when one is designated;
- terminal economic node(s);
- timer type;
- start event / date;
- stop event;
- expected window;
- current window position;
- remaining gates;
- decay / overdue status;
- timing confidence;
- management timing credibility where relevant.

If a material dependency chain is known but left only in prose, mark this step **FAIL / INCOMPLETE**.

Do not label a chain “active now” without identifying which gate is actually next.

---

## 6. Insider-activity context

Apply `ttc-insider-activity.md` for material catalyst windows.

Inspect and classify where available:
- discretionary purchases;
- discretionary sales;
- 10b5-1 executions;
- 10b5-1 adoption / modification / termination dates;
- tax-withholding / sell-to-cover;
- option exercise mechanics;
- gifts / transfers;
- clustered activity.

Rule:
> **Raw insider selling is not interpreted until transaction mechanism and planning date are classified.**

Do not double-count the same economic transaction across Form 4 and Form 144.

---

## 7. Catalyst economics / shareholder capture

Before asking whether price will move, ask whether the event matters economically.

Record:
- decompose economically distinct contract components before assigning state;
- current Contract Economic rung (CE0-CE5) for each material component when the catalyst is contract-like;
- Contract Commitment Quality: PROTECTED / CONDITIONAL / WEAK / UNKNOWN for each material component;
- Optioned Economic Surface separately from Committed Economic Value;
- funded / committed economics;
- optional ceiling / TAM separately;
- whether the ceiling is company-specific or shared and whether future task orders remain competed;
- currently obligated / funded amount where available;
- economics relative to equity value / enterprise value / earnings base;
- per-share capture;
- capex / working-capital requirement;
- dilution / debt / warrants / preferred friction;
- payoff persistence:
  - ONE-OFF REALIZATION
  - REPEATABLE DISCRETE
  - RUN-RATE ACTIVATION
  - STACKED / OVERLAPPING RUN-RATE
  - DECAYING / TERMINABLE RUN-RATE

A catalyst that changes little per share should not rank highly merely because it is close.

---

## 8. Catalyst profitability / repricing burden

Mandatory TTC profitability fields:

```text
P(Hit):
P(Material Price Move | Hit):
Conditional Upside Range:
Conditional Failure / Delay Downside:
P(Delay / No-Decision):
Already-Priced State:
Surprise State:
Expected Event Window:
Confidence:
Analog Set:
Basic Market Cap:
Fully Diluted Market Cap / Range:
Enterprise Value:
25% / 50% / 100% Repricing Burden:
Minimum Viable Catalyst:
Dynamic Dilution State:
Reverse-Split / Listing Timer when relevant:
```

Apply `ttc-repricing-threshold.md`. Use the deterministic `equity_repricing_burden` tool where available for denominator arithmetic.

Use ranges unless precision is empirically earned.

Do not substitute `P(Hit)` for `P(price move | hit)`.

---

## 9. Recognition / price-response evidence

Ask:
- has a similar event moved this stock before?
- what was the 1D / 5D / 20D reaction where data are available?
- was the prior event expected or surprising?
- how much of the current catalyst is already recognized?
- is price response strengthening, weakening, or being absorbed?

Use the hierarchy:
1. same company + same event type;
2. same company + similar economics;
3. same mechanism/customer/regulator + close peer;
4. close event archetype;
5. broad prior only if necessary.

One analog is evidence, not a universal coefficient.

---

## 9A. Multi-method / market-structure shadow capture

Interpretation order:

> **TA / market structure should normally be interpreted after the causal story, thesis, and event/process window are known.**

TA can refine recognition, timing, contradiction detection, and execution. It does not originate the fundamental catalyst thesis.


Status: **EXPERIMENTAL / SHADOW-ONLY.**

For fresh stock analyses, freeze available non-headline state alongside the canonical analysis:

- price / market structure;
- expectations / revisions;
- ownership;
- entity-network evidence;
- fundamental inflection;
- regime / factor state;
- liquidity / microstructure;
- statistical peer/residual evidence.

Use `skills/xyool/multi-method-discovery-market-structure.md`.

At minimum, where sufficient OHLCV exists, market structure should record the available subset of:

```text
SMA20 / SMA50 / SMA200 relation
20-session breakout / breakdown
distance from 52-week high
RSI14
ATR14 %
relative volume20
anchored VWAP / distance from anchor when meaningful
structure state
```

Important:
- these fields do not override Quality or current production authority;
- correlated indicators must not be counted as independent votes;
- missing sidecar data is `BLOCKED` or `UNKNOWN`, not bearish;
- Fibonacci levels, if recorded, are experimental geometry only and carry zero authority;
- Recognition V1 remains frozen; this sidecar is analyzed separately until fresh validation earns a successor version.

The anti-headline test is mandatory for discovery research:

> **Could this stock have become research-visible from a non-catalyst family even if no new headline had appeared?**

---

## 10. Downside / invalidation / delay state

Every candidate must state:
- failure condition;
- delay condition;
- stale / overdue condition;
- financing / runway risk;
- permanent-impairment path;
- what evidence would lower P(Hit), P(move|hit), or payoff magnitude;
- what would invalidate the thesis entirely.

A ranking without downside is incomplete.

---

## 11. Current holding / replacement hurdle

Required before any full thesis-to-thesis rotation.

Compare both current holding and candidate on:
- Quality;
- unresolved catalysts;
- causal stage;
- event probability;
- event materiality;
- window position;
- recognition gap;
- profitability priority;
- downside;
- shareholder capture;
- liquidity / taxes / friction;
- confidence.

Fresh late-stage current catalysts raise the removal hurdle.

Candidate-only analysis cannot authorize a full rotation.

---

## 12. Quant expression

Only after TTC determines desired economic exposure:
- confirm market-data readiness;
- apply approved Quant risk / concentration / execution constraints;
- Quant may reduce / delay / express risk according to tested authority;
- Quant may not create a thesis or increase exposure above TTC desired exposure.

If Quant data are unavailable, label execution state accordingly rather than pretending Quant passed.

---

## 13. Final completeness audit

Before publishing a Top-50 rank, catalyst timeline, profitability rank, or capital action, ask:

```text
DISCOVERY VISIBILITY / BREADCRUMB INTAKE COMPLETE?
QUALITY + TRAJECTORY + UNLOCK + SURVIVAL COMPLETE?
ALL MATERIAL CATALYSTS INVENTORIED?
EVENT IDENTITY VERIFIED?
LATEST DATE/WINDOW VERIFIED?
REALIZED EVENTS CLOSED?
NEXT CAUSAL GATE IDENTIFIED?
MATERIAL DEPENDENCY GRAPH / GATING NODE VERIFIED?
INSIDER ACTIVITY CHECKED / CLASSIFIED?
ECONOMIC MATERIALITY ESTIMATED?
CONTRACT COMPONENTS DECOMPOSED + CE RUNG / COMMITMENT QUALITY / OPTIONED VS COMMITTED VALUE CHECKED WHEN APPLICABLE?
CURRENT / FD EQUITY DENOMINATOR + REPRICING BURDEN CHECKED?
P(HIT) SEPARATE FROM P(MOVE|HIT)?
UPSIDE AND FAILURE DOWNSIDE SHOWN?
ALREADY-PRICED / RECOGNITION CHECKED?
CURRENT HOLDING COMPARED IF ROTATING?
QUANT STATUS EXPLICIT IF EXECUTABLE?
SOURCE / CONFIDENCE / BLOCKERS SHOWN?
```

If any required item is blank:

```text
FINAL STATUS = INCOMPLETE / FAIL CLOSED
```

Do **not** fill missing evidence with assumption merely to complete a ranking.

---

## 14. Deep-analysis memory ingestion

Required when a run produces a full/deep analysis or materially changes:
- thesis architecture;
- dependency graph / primary gate;
- shareholder-capture state;
- repricing interpretation;
- material timers;
- Quality / TTC rationale.

Use:
- `skills/xyool/stock-analysis-memory-ingestion.md`
- `stock_analysis_memory_plan`
- `stock_analysis_memory_ingest`
- `stock_analysis_memory_audit`

Required process:

```text
preserve full finished analysis artifact
→ enumerate material conclusions
→ assign persistence dispositions
→ plan / validate
→ ingest
→ audit zero unmapped material conclusions
```

For a tiny factual refresh with no material analytical change:

```text
NOT APPLICABLE — DELTA STATE UPDATE ONLY
```

A deep analysis that is only summarized into current state, without a lossless archive and extraction audit, is incomplete as durable Xyool memory.

---

## Top-50 output requirement

A Top-50 table should carry at least:

```text
Rank
Ticker
Discovery Lane
Quality State
Quality Trajectory
Quality Unlock Condition
Survival to Unlock
Capital Eligibility
Next Chronological Event
Next Profit-Producing Event
Primary Gating Node
Terminal Economic Node
Timing Type
Expected Window
Event-Integrity Status
P(Hit)
P(Material Move | Hit)
Conditional Upside
Repricing Sensitivity / Burden
Failure / Delay Downside
Already-Priced State
Insider Context State
Profitability Priority
Confidence
Completeness Status
```

A name may remain in the research Top 50 with WATCH / BLOCKED status, but it must be visibly separated from capital-eligible names.

---

## Miss handling

If a later review discovers a step was skipped:
1. classify it as a **process omission**;
2. freeze the pre-outcome information set;
3. apply `miss-to-question-learning-loop.md`;
4. identify the minimum generalizable missing question;
5. test positive and negative controls;
6. update this run sequence only if the requirement is transferable;
7. do not rewrite the old result as though the step had originally been performed.

Rule:
> **A discovered omission becomes a permanent checklist item only when the generalized question is prospectively answerable and transferable.**

---

## Authority boundary

This protocol enforces completion. It does not create independent BUY / SELL / ROTATE authority.

Authority remains:

```text
QUALITY → eligibility
TTC → capital priority / desired exposure
QUANT → tested risk/execution expression
```

## Permanent interpretation

> **Xyool may be uncertain. Xyool may be blocked. Xyool may say evidence is missing. Xyool may not silently skip a required step and still call the output complete.**
