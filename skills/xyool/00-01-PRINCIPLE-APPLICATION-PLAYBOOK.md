# Xyool — Principle Application Playbook

Status: **CANONICAL OPERATIONAL INTERPRETATION / REQUIRED COMPANION TO START-HERE PRIMER**

Purpose: the Start-Here Primer states Xyool's principles. This playbook explains **how to use those principles in live reasoning**.

A principle is not complete merely because a future chat can repeat it. The chat must know:

- **when** the principle applies;
- **what question** the principle forces;
- **what evidence** answers that question;
- **what state can change** because of the evidence;
- **which layer owns the decision**;
- **what output** must be produced;
- **what not to conclude** from the principle alone.

Short form:

> **Principles are operating instructions, not slogans.**

This file does not create a new scoring layer or allocation authority. It teaches correct use of the existing Xyool architecture.

---

# 1. UNIVERSAL PRINCIPLE-USE METHOD

Whenever a Xyool principle becomes relevant, process it through this seven-part pattern:

```text
1. TRIGGER
   Why is this principle relevant now?

2. FORCED QUESTION
   What question must be answered because the principle exists?

3. EVIDENCE
   What facts, filings, prices, customer actions, company disclosures,
   analogs, or state history can answer it?

4. STATE DELTA
   What changed versus the prior Xyool state?

5. AUTHORITY
   Which layer is allowed to act on the answer?

6. OUTPUT
   What field, state, timer, confidence change, or capital comparison
   must be written down?

7. FALSE-POSITIVE GUARD
   What must NOT be inferred from this evidence alone?
```

If a principle is mentioned without these operational consequences when they matter, the principle has not actually been applied.

---

# 2. PRINCIPLES SHOULD CHANGE QUESTIONS BEFORE THEY CHANGE SCORES

Xyool is primarily a question-and-state system.

Correct use:

```text
NEW EVIDENCE
→ principle tells us what to ask
→ answer changes evidence/state/timer/confidence
→ TTC compares updated opportunity
→ capital action may or may not change
```

Incorrect use:

```text
NEW EVIDENCE
→ remember a principle
→ add an arbitrary bonus/penalty
→ rank changes without causal explanation
```

Example:

`Insider sale != bearish signal until classified` does **not** mean add a smaller bearish multiplier.

It means:
1. identify the transaction;
2. determine whether it is discretionary, 10b5-1, tax-driven, option-related, gift/transfer, or other;
3. inspect plan adoption/modification timing where relevant;
4. decide whether the information changes catalyst confidence, downside, shareholder-capture confidence, or nothing;
5. record the classified state.

---

# 3. HOW TO USE QUALITY BEFORE TTC

## Trigger
A company is being added to the Top 50, compared for capital, or promoted because of a catalyst.

## Forced question

> **Should this equity compete for normal capital at all?**

## Evidence
Use company-level Xyool + OSE evidence:
- real demand;
- company control/capture;
- Structural Confirmation;
- Conversion Confirmation;
- runway;
- financing/dilution;
- governance;
- permanent-impairment risk;
- valuation/asymmetry;
- shareholder capture;
- evidence quality.

## State delta
Output one of:

```text
FAIL
WATCH
QUALIFIED
HIGH QUALITY
```

## Authority
Quality owns **eligibility**, not position sizing or catalyst ranking.

## Output
Every ranked name must show Quality state and capital status.

## False-positive guard
A hard date, exciting contract, FDA event, or large possible upside cannot rescue a WATCH/FAIL equity into normal TTC competition.

### Operational example
A biotech has an FDA decision in three days.

Correct use:
- first determine Quality;
- if WATCH, keep it on the event timeline but mark capital-blocked;
- TTC can still study the catalyst for research, but it does not silently compete with qualified names.

Incorrect use:
- rank it first simply because the date is closest.

---

# 4. HOW TO USE EVENT IDENTITY + FRESHNESS

## Trigger
A catalyst date/window or material event is being used in current analysis.

## Forced question

> **Am I discussing the exact same company/program/project/stage/decision-maker/stop-event, and is the information still current?**

## Evidence
- issuer filing / press release;
- regulator source where applicable;
- latest earnings/call;
- later extension, delay, withdrawal, completion, acquisition, financing, or superseding event.

## State delta
Classify:

```text
UNRESOLVED
REALIZED
DELAYED
SUPERSEDED
INVALIDATED
```

## Authority
This is an evidence-integrity gate feeding Quality/OSE/TTC.

## Output
Record exact event key and last freshness check.

## False-positive guard
Never transfer evidence from one drug/program/customer/facility/stage to another merely because the ticker is the same.

### Operational example
One drug program fails while another drug at the same company has a pending FDA decision.

Correct use:
- preserve both event keys separately;
- close the failed program's event;
- do not cancel the other program's clock without explicit causal linkage.

---

# 5. HOW TO USE MULTI-GATE CATALYSTS / DEPENDENCY CHAINS

## Trigger
The economic path contains more than one unresolved step or multiple breadcrumbs appear to describe one downstream economic outcome.

## Forced questions

> **What must happen first, what does that unlock, and which unresolved gate currently controls the economically meaningful downstream path?**

and:

> **Which gate is next, which gate changes economics, and which gate is most likely to create shareholder profit?**

## Evidence
Map the causal chain as a directed acyclic graph using `ttc-dependency-chain.md`, e.g.:

```text
TEST
→ ACCEPTANCE
→ PROCUREMENT
→ DEPLOYMENT
→ REVENUE / CASH
```

For each node distinguish:
- satisfied versus unresolved;
- strict prerequisite versus supporting evidence;
- timer / expected window;
- evidence IDs;
- economic role;
- invalidation.

## State delta
Track each gate independently and persist the graph:
- current stage;
- frontier gate(s);
- primary gating node and rationale when justified;
- terminal economic node(s);
- timer;
- probability / confidence;
- materiality;
- recognition consequence;
- profitability transmission;
- shareholder-capture dependency.

Use `domain_state_dependency` where available to validate the persisted DAG and identify the unresolved frontier.

## Authority
Dependency structure, Timers, and FES inform TTC. TTC decides capital priority.

## Output
Where relevant, always distinguish:

```text
NEXT CHRONOLOGICAL EVENT
NEXT ECONOMIC CONVERSION EVENT
NEXT PROFIT-PRODUCING EVENT
PRIMARY GATING NODE
TERMINAL ECONOMIC NODE
```

If a material dependency chain is known but left only in prose, the multi-gate step is incomplete.

## False-positive guard
Do not assign the procurement payoff to SAT/acceptance simply because successful SAT is necessary for procurement. Do not count serial dependency nodes as independent catalysts or mechanically multiply unvalidated point probabilities.

### Operational example
A defense product is currently in SAT.

Correct use:
- SAT may have high P(Hit) and modest P(price move | hit);
- funded procurement may be later but much more material;
- the dependency graph shows procurement as blocked until SAT/acceptance is satisfied;
- TTC should value both without collapsing them.

---

# 6. HOW TO USE CAUSAL TIMERS

## Trigger
Xyool needs to answer when something could convert.

## Forced question

> **What event started the clock, what event stops it, and what evidence tells us how this specific clock normally behaves?**

## Evidence hierarchy
Prefer:
1. same company + same customer/program + same stage transition;
2. same company + same mechanism;
3. same customer/agency + same mechanism;
4. same company historical analog;
5. close industry analog;
6. broad sector benchmark.

## State delta
Record:
- timer type;
- start date;
- expected window;
- window position;
- evidence freshness;
- remaining gates;
- decay/overdue status;
- timing confidence.

## Authority
Timers do not allocate capital. TTC interprets the timer alongside probability, materiality, downside, and recognition.

## Output
Never write only `active now` when a causal stage can be named.

## False-positive guard
Do not assume probability rises forever as time passes. Missed windows can decay.

---

# 7. HOW TO USE BREADCRUMBS / FORWARD EVIDENCE

## Trigger
Public evidence appears before the final catalyst.

## Forced question

> **Does this evidence change the probability, stage, or timing of a specific future economic transition?**

Use the six tests:
- transition;
- delta;
- agency/commitment;
- clock;
- falsifiability;
- economic link.

## Evidence
Prefer observable action:
- testing;
- selecting;
- integrating;
- funding;
- ordering tooling;
- final qualification;
- deploying;
- consuming/replenishing;
- building capacity.

## State delta
Classify:

```text
DESCRIPTIVE
WATCHING
ARMED TIMER
ACTIVE TIMER
```

## Authority
Breadcrumbs/FES alter evidence state and timer readiness; TTC interprets capital consequence.

## Output
Record:
- breadcrumb;
- implied transition;
- timer it arms;
- confirmation trigger;
- invalidation.

## False-positive guard
Management optimism or a large TAM is not a causal breadcrumb by itself.

---

# 8. HOW TO USE REPEAT / CASCADE PRINCIPLES

## Trigger
A material order/deployment/adoption appears to repeat.

## Forced questions

> **Is replication happening?**

and separately:

> **What repeats, and when could it repeat again?**

## Evidence
Check whether repeat events share:
- customer;
- program/product;
- qualification path;
- funding mechanism;
- operational bottleneck;
- economic unit.

## State delta
Cascade can improve while timing confidence remains weak.

Cadence states may be:

```text
NONE
EMERGING
ESTABLISHED
ACCELERATING
DECELERATING
BROKEN
```

## Authority
Cascade describes replication state. Repeat cadence interprets time structure. TTC uses both.

## Output
Write the repeatable unit, observed intervals, comparability, remaining units, expected next window, and confidence.

## False-positive guard
One first→second interval does not establish a guaranteed schedule.

---

# 9. HOW TO USE CATALYST PROFITABILITY

## Trigger
A catalyst is being used to prioritize capital.

## Forced question

> **Even if the catalyst hits, is the stock likely to reprice enough to matter?**

Then ask:

> **How much incremental common-equity value is required for a material reprice from today's basic and fully diluted denominator?**

## Evidence
Estimate transparently:

```text
P(Hit)
P(Material Price Move | Hit)
Conditional Upside Range
Failure / Delay Downside
P(Delay / No-Decision)
Already-Priced State
Surprise State
Economic Materiality
Basic / Fully Diluted Market Cap
25% / 50% / 100% Repricing Burden
Minimum Viable Catalyst
Dynamic Dilution State
Per-Share Capture
Analog Set
```

Use `ttc-repricing-threshold.md` and the deterministic `equity_repricing_burden` tool where available. Do not equate revenue/order dollars directly with equity value.

## State delta
A catalyst may move:
- closer in time but lower in profitability priority;
- higher in P(Hit) but lower in P(move|hit);
- higher in economics but lower in recognition gap;
- higher in upside but also much higher in failure downside.

## Authority
TTC owns the final profitability priority among qualified opportunities.

## Output
Always keep separate:

```text
CHRONOLOGICAL CATALYST ORDER
PROFITABILITY PRIORITY
```

## False-positive guard
Do not treat the nearest date as the best capital opportunity.

---

# 10. HOW TO USE PRICE-REACTION ANALOGS

## Trigger
Xyool needs evidence for P(Material Price Move | Hit) or move magnitude.

## Forced question

> **What happened when this company or a close analog previously delivered economically similar information?**

## Evidence hierarchy
1. same company + same catalyst type;
2. same company + economically similar event;
3. same mechanism/customer/regulator + peer;
4. close event archetype;
5. broad event study.

Record where practical:
- 1D move;
- 5D move;
- 20D move;
- benchmark move;
- surprise level;
- whether economics were comparable.

## State delta
Analogs can raise/lower recognition probability or widen/narrow move ranges.

## Authority
Analogs inform TTC; they do not create a deterministic price target.

## False-positive guard
One prior event is evidence, not a universal coefficient.

---

# 11. HOW TO USE PAYOFF PERSISTENCE

## Trigger
A catalyst realizes or is close enough that post-event economics matter.

## Forced question

> **Does the economic payoff end with the event, repeat discretely, or activate an ongoing economic stream?**

## Evidence
Classify:

```text
ONE-OFF REALIZATION
REPEATABLE DISCRETE
RUN-RATE ACTIVATION
STACKED / OVERLAPPING RUN-RATE
DECAYING / TERMINABLE RUN-RATE
```

Then evaluate:
- run rate;
- duration;
- margin/cash conversion;
- renewal/replenishment;
- concentration/termination risk;
- how much is already recognized.

## State delta
Realization can close one timer while creating a durable economic state and a new timer.

## Authority
Payoff persistence informs remaining opportunity and TTC.

## Output
Close the realized timer, record activated economics, update recognition, then identify next unresolved clock.

## False-positive guard
Persistent economics do not guarantee persistent stock-price appreciation.

---

# 12. HOW TO USE INSIDER ACTIVITY / 10b5-1

## Trigger
Material catalyst window or notable insider filing.

## Forced question

> **What caused the transaction, and how informative is it after classification?**

## Evidence
Classify:
- discretionary purchase;
- discretionary sale;
- 10b5-1 planned sale;
- tax withholding / sell-to-cover;
- option exercise;
- gift/transfer;
- clustered activity.

For 10b5-1 separately track:

```text
PLAN ADOPTION
PLAN MODIFICATION / TERMINATION
EXECUTION
```

## State delta
Possible states:

```text
POSITIVE
NEUTRAL / MECHANICAL
LOW-INFORMATION PLANNED SELLING
CAUTION
MATERIAL NEGATIVE CONTEXT
UNKNOWN / INCOMPLETE
```

## Authority
Insider context can change confidence/downside/research priority. It does not independently force a trade.

## Output
Record transaction class and whether it changes any TTC assumption.

## False-positive guard
A planned execution immediately before a catalyst is not equivalent to a discretionary sale made immediately before a catalyst.

---

# 13. HOW TO USE SHAREHOLDER CAPTURE

## Trigger
Headline economics look large.

## Forced question

> **How much of the economics can common shareholders actually capture per share?**

## Evidence
Separate:
- funded/committed economics;
- ceilings/options;
- capex;
- working capital;
- debt;
- dilution;
- warrants/preferreds;
- margins;
- concentration;
- financing needs;
- existing valuation;
- current and fully diluted equity denominator;
- enterprise value / creditor claims;
- repricing burden for material percentage moves;
- reverse-split/listing pressure when relevant.

## State delta
A large contract can improve company economics while shareholder capture remains weak.

## Authority
Quality owns eligibility consequences; TTC uses remaining per-share economics for priority.

## Output
Write company economics and per-share capture separately.

## False-positive guard
TAM, program size, or contract ceiling is not shareholder value.

---

# 14. HOW TO USE RECOGNITION

## Trigger
Economics improve or price moves materially.

## Forced question

> **Has the market already recognized the economic change, under-recognized it, or moved ahead of it?**

## Evidence
Use:
- price reaction to new facts;
- estimate revisions;
- volume/relative strength;
- valuation change;
- analyst/institutional recognition;
- economics versus price change.

## State delta
Recognition gap may widen or compress even when business fundamentals are unchanged.

## Authority
Recognition informs TTC remaining opportunity. Price alone does not create Quality.

## Output
State whether price moved faster/slower than economics and how much recognition gap plausibly remains.

## False-positive guard
Price acceleration is evidence about recognition, not proof that the thesis improved.

---

# 15. HOW TO USE NEW CAPITAL VS EARNED CAPITAL

## Trigger
Deciding whether to add new cash or sell one holding to fund another.

## Forced questions

For new capital:
> **What is the best qualified TTC destination now?**

For earned capital:
> **Has the existing position lost enough relative merit to clear the higher removal hurdle?**

## Evidence
Compare both current holding and candidate on:
- Quality;
- unresolved catalysts;
- FES/timer maturity;
- probability;
- materiality;
- recognition gap;
- downside;
- remaining opportunity;
- shareholder capture;
- liquidity/friction.

## State delta
A candidate can become the best place for new cash without justifying a full sale of an intact holding.

## Authority
TTC owns desired rotation. Quant expresses it downstream.

## Output
Choose among:

```text
HOLD CURRENT
NEW CAPITAL TO CANDIDATE
PARTIAL ROTATION
FULL ROTATION
CASH
```

with explicit replacement-hurdle reasoning.

## False-positive guard
A slightly higher current rank is not sufficient to liquidate earned capital.

---

# 16. HOW TO USE QUANT

## Trigger
TTC has already decided desired economic exposure and the question becomes executable risk expression.

## Forced question

> **How should approved exposure be expressed under measured volatility, correlation, concentration, trend, liquidity, and tested risk rules?**

## Evidence
Use the current repo's Quant models/defaults, not remembered parameters.

## State delta
Quant may reduce, constrain, delay, or alter expression according to tested authority rules.

## Authority
Quant cannot invent fundamental conviction or increase exposure beyond TTC authority.

## Output
Show TTC desired exposure and Quant-adjusted executable exposure separately when material.

## False-positive guard
A strong technical signal cannot rescue failed Quality or create a catalyst thesis.

---

# 17. HOW TO USE THE MISS-TO-QUESTION LOOP

## Trigger
Xyool materially misses:
- a winner;
- a risk;
- a catalyst;
- timing;
- price response;
- shareholder capture;
- rotation;
- process coverage.

## Step 1 — classify the miss

Examples:

```text
UNKNOWABLE OUTCOME
RESEARCH-COVERAGE MISS
IDENTITY / FRESHNESS MISS
CAUSAL-CONNECTION MISS
TIMER / CALIBRATION MISS
QUALITY MISS
CATALYST-PROFITABILITY MISS
SHAREHOLDER-CAPTURE MISS
RECOGNITION MISS
ROTATION MISS
QUANT EXPRESSION MISS
PROCESS-OMISSION MISS
```

## Step 2 — freeze the pre-outcome information set
Do not use facts learned after the result.

## Step 3 — identify the missing question
Ask:

> **What question/check/state field would have forced Xyool to notice the relevant public information before the outcome?**

## Step 4 — generalize
Remove the company/ticker identity from the proposed rule.

Bad:
> Always penalize RARE when an insider sells.

Good:
> For every material catalyst, classify insider activity by mechanism and planning date before interpreting it.

## Step 5 — run controls
Test:
- the missed case using only pre-outcome information;
- positive controls where the principle should help;
- negative controls where the principle should remain neutral.

## Step 6 — govern the result
Classify as:

```text
CANONICAL PROCESS
PROVISIONAL INPUT
RESEARCH ONLY
REJECTED
```

## Step 7 — close the miss
Every material miss must end as one of:

```text
A. NEW GENERALIZABLE QUESTION / CHECK ADDED
B. EXISTING RULE WAS SUFFICIENT BUT EXECUTION SKIPPED IT
C. OUTCOME WAS GENUINELY UNKNOWABLE / NOT ACTIONABLE
D. PROPOSED FIX FAILED CONTROLS — NO CHANGE
```

A miss is not considered processed merely because it was discussed.

## Authority
Miss handling changes the system only through the appropriate existing layer. It does not create a free-floating score.

## False-positive guard
Do not optimize the system to select the latest winner after the fact.

---

# 18. HOW TO PROCESS A NEW STOCK FROM ZERO

Use this sequence:

```text
1. Fresh sources / identity
2. Build company causal thesis: NEED → CONTROL → MOMENTUM → FRICTION → PRICE
3. Build OSE state
4. Quality qualifier
5. If WATCH/FAIL: research only unless Quality changes
6. Inventory unresolved material catalysts
7. Validate exact event identity / freshness
8. Map causal timers + FES/breadcrumbs
9. Evaluate economics / shareholder capture
10. Classify payoff persistence where relevant
11. Inspect insider context for material catalyst windows
12. Build catalyst profitability object + repricing-burden lens
13. Evaluate recognition / price-response analogs
14. Define downside / invalidation / delay
15. TTC profitability priority among qualified alternatives
16. Quant expression only if executable exposure is being considered
17. Completeness audit
```

The output is not valid if mandatory fields are silently skipped.

---

# 19. HOW TO PROCESS NEW COMPANY NEWS

Do not blindly rebuild the whole company.

Use delta reasoning:

```text
OLD STATE
→ NEW FACT
→ WHICH PRINCIPLE DOES THIS TRIGGER?
→ WHICH RUNG / TIMER / FIELD CHANGES?
→ WHAT DOES NOT CHANGE?
→ DOES QUALITY CHANGE?
→ DOES TTC PRIORITY CHANGE?
→ DOES CAPITAL ACTION CHANGE?
```

Example:
A new contract arrives.

Do not stop at `contract = positive`.
Ask:
- funded or ceiling?
- new customer or repeat?
- same repeatable unit?
- economics relative to EV?
- margin/capex/working-capital burden?
- already expected?
- what prior timer closes?
- what next timer begins?
- how did similar contracts move the stock?
- does Quality change, TTC change, or merely confirmation improve?

---

# 20. HOW TO COMPARE TWO STOCKS

Never compare only the candidate.

Build a symmetric table:

```text
QUALITY
UNRESOLVED CATALYSTS
NEXT CHRONOLOGICAL EVENT
NEXT PROFIT-PRODUCING EVENT
FES / TIMER STAGE
EXPECTED WINDOW
P(HIT)
P(MOVE | HIT)
MATERIALITY
SHAREHOLDER CAPTURE
FAILURE DOWNSIDE
ALREADY PRICED
PAYOFF PERSISTENCE
RECOGNITION GAP
INSIDER CONTEXT
REMAINING OPPORTUNITY
LIQUIDITY / FRICTION
CONFIDENCE
```

Then answer two separate questions:

```text
WHERE SHOULD NEW CAPITAL GO?
SHOULD EARNED CAPITAL BE REMOVED FROM THE CURRENT HOLDING?
```

Those answers can differ.

---

# 21. HOW TO BUILD / UPDATE THE TOP 50

The Top 50 is an opportunity set, not a proximity list.

For every name:
1. run mandatory completeness gates;
2. preserve Quality/capital status;
3. inventory material catalysts;
4. separate chronology from profitability;
5. close realized catalysts;
6. update price recognition;
7. update payoff persistence;
8. preserve blocked/watch names as blocked;
9. mark unknown fields rather than fabricate precision;
10. rank normal capital only among eligible opportunities.

A Top-50 row should allow a future chat to answer:

> **Why is this company here, what must happen next, how likely is that event, what could the stock do if it happens, what can go wrong, and why does the opportunity deserve this capital priority now?**

If the row cannot answer those questions, it is incomplete.

---

# 22. HOW TO KNOW WHETHER A PRINCIPLE ACTUALLY MATTERED

After applying a principle, explicitly state one of:

```text
NO STATE CHANGE
CONFIDENCE CHANGE ONLY
RESEARCH PRIORITY CHANGE
FES / TIMER CHANGE
QUALITY CHANGE
TTC PRIORITY CHANGE
CAPITAL ACTION CHANGE
QUANT EXPRESSION CHANGE
```

This prevents principles from becoming ceremonial checkboxes.

A principle can be correctly applied and produce **no action change**.

That is not failure. The purpose is correct interpretation, not forced activity.

---

# 23. REQUIRED FUTURE-CHAT BEHAVIOR

A future chat using Xyool should be able to explain not only:

> **What is the rule?**

but also:

> **Why did this rule trigger here? What evidence did we inspect? What state changed? Which layer owns the consequence? What did we explicitly avoid inferring?**

If it cannot answer those questions, it has not demonstrated operational understanding of Xyool.

Final operational principle:

> **USE EACH PRINCIPLE TO FORCE THE RIGHT QUESTION, ROUTE THE ANSWER TO THE RIGHT STATE, AND LET ONLY THE AUTHORIZED LAYER CHANGE CAPITAL.**
