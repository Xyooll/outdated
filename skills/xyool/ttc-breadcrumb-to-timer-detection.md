# Xyool — TTC Breadcrumb-to-Timer Detection

Status: **MANDATORY TTC RESEARCH / DETECTION PROCESS — PROVISIONAL CALIBRATION — NO INDEPENDENT CAPITAL AUTHORITY**

## Core purpose

TTC should not wait for a fully formed catalyst announcement when meaningful pre-event evidence is already public.

The purpose of Breadcrumb-to-Timer Detection is to improve Xyool's ability to identify weak-but-causal signals early, connect them to the correct economic transition, and arm the appropriate timer before the final order, acceptance, funding, deployment, or revenue event appears.

Core question:

> **What public breadcrumb suggests that a specific economically meaningful transition may already be forming, and what timer should that breadcrumb arm?**

Short form:

> **What breadcrumb is this, what timer does it start, and what would confirm or kill it?**

Breadcrumbs are not catalysts by themselves. They are evidence that a causal clock may be forming.

---

## Breadcrumb discriminator — regular information vs causal breadcrumb

Core distinction:

> **Regular information describes the company or opportunity. A breadcrumb changes the probability, stage, or expected timing of a specific future causal transition.**

Operational shorthand:

> **Verbs beat adjectives.**

Examples of mostly descriptive / regular information:
- large TAM;
- strong technology;
- important customer base;
- management is optimistic;
- market demand is attractive;
- product has many possible applications.

Examples of potentially causal breadcrumb information:
- customer **is testing** the product;
- final product **selection is underway**;
- tooling **has been ordered**;
- funding **was appropriated**;
- qualification **entered its final stage**;
- the customer **expanded to a second site**;
- inventory **is being consumed and replenished**;
- a production line **is being installed**.

The grammatical rule is only a heuristic. A verb does not make evidence causal by itself; it must still pass the tests below.

### Mandatory six-test filter

For any candidate breadcrumb ask:

1. **Transition test — what changes next?**
   Can the information be written as a specific causal transition such as:
   ```text
   testing → acceptance
   acceptance → procurement
   first site → second site
   installed base use → replenishment
   funded capex → usable capacity
   ```
   If no specific transition can be named, the information is usually descriptive rather than a breadcrumb.

2. **Delta test — is this new state information?**
   Does the evidence move the known state forward, backward, or materially change confidence versus the prior information set?
   Repeating the same old claim in a new presentation is not a new breadcrumb.

3. **Agency / commitment test — is someone doing something costly, binding, or operational?**
   Stronger breadcrumbs usually involve observable action by a customer, agency, supplier, regulator, or the company itself: testing, selecting, funding, integrating, ordering, building, hiring for a ramp, deploying, consuming, or accepting.
   Talk without action receives less weight.

4. **Clock test — can a timer be defined?**
   Can Xyool identify:
   - a plausible start event;
   - the stop event;
   - the current stage;
   - what evidence would move the clock forward/backward?
   If not, retain it as WATCHING information rather than an ARMED timer.

5. **Falsifiability test — what would confirm or kill it?**
   A useful breadcrumb should imply a next observable event and an invalidation condition.
   If nothing could disprove the interpretation, it is probably narrative rather than a causal signal.

6. **Economic-link test — does the stop event matter?**
   If the implied transition completes, can it change funded orders, backlog, deployment, revenue, margin, cash, strategic control, or shareholder value?
   Interesting operational detail with no plausible economic consequence should not materially affect TTC.

### Optional seventh test — specificity / comparability

Ask:
- named customer/program or generic?
- same product/mechanism or merely related?
- direct evidence or inference?
- is there a comparable historical transition for calibration?

Higher specificity improves confidence and timer calibration but is not always required to classify a weak breadcrumb.

### Decision rule

```text
DESCRIPTIVE INFORMATION
→ fails Transition and/or Economic-link tests
→ do not create timer

WEAK BREADCRUMB
→ specific transition is plausible but action/evidence is incomplete
→ WATCHING

CAUSAL BREADCRUMB
→ transition + delta + observable action + falsifiable next event
→ ARMED timer

START-EVENT EVIDENCE
→ timer start condition is actually satisfied
→ ACTIVE timer
```

### Counterfactual / double-counting test

For multiple pieces of evidence ask:

> **If this item were removed, would our causal-state or timer conclusion actually change?**

If no, it is likely corroboration or duplicate description rather than a separate breadcrumb.

This prevents one underlying fact from being counted repeatedly through a press release, earnings call, guidance update, and analyst recap.

---

## Architecture

```text
PUBLIC EVIDENCE
      ↓
DISCOVERY VISIBILITY
      ↓
BREADCRUMB DETECTION
      ↓
CAUSAL INTERPRETATION
      ↓
TIMER CANDIDATE
      ↓
EVIDENCE / COMPARABILITY CHECK
      ↓
ARMED / ACTIVE TIMER
      ↓
FES + TTC UPDATE
      ↓
REALIZED / FAILED / STALE / SUPERSEDED
```

Authority remains:

```text
DISCOVERY VISIBILITY
→ research visibility only

QUALITY
→ normal capital eligibility

BREADCRUMBS / DEPENDENCY GRAPH / TIMERS / FES
→ causal timing evidence

TTC
→ capital priority

QUANT
→ downstream expression only
```

When a breadcrumb belongs to a material multi-gate path, also apply `ttc-dependency-chain.md`:

```text
BREADCRUMB
→ NODE / EDGE UPDATE
→ FRONTIER / GATING NODE
→ TIMER
→ DOWNSTREAM ECONOMIC PATH
```

The breadcrumb must not be counted as an independent catalyst if it merely advances or corroborates a node in an existing dependency chain.

---

## Pre-Quality discovery use

Breadcrumb Detection is not limited to stocks that already pass Quality.

During candidate search, use it as one side of the discovery union:

```text
ESTABLISHED-QUALITY CANDIDATES
        UNION
HIDDEN-TRANSITION BREADCRUMB CANDIDATES
```

A Q1/Q2/WATCH/FAIL company may therefore remain visible if the breadcrumb passes the causal/economic tests and creates a credible Quality-unlock question.

Required handoff to Quality:

```text
DISCOVERY LANE
CURRENT QUALITY
QUALITY TRAJECTORY
QUALITY UNLOCK CONDITION
SURVIVAL TO UNLOCK
POST-UNLOCK SHAREHOLDER CAPTURE
```

The breadcrumb does not promote Quality by itself.

Canonical visibility contract:
- `skills/xyool/discovery-visibility-gate.md`

---

## Why this exists

Recent Xyool misses showed two different timing blind spots:

1. a repeat event was recognized after it happened, but the spacing between repeats was not carried forward into a next-event timer;
2. an existing customer was publicly testing/selecting an adjacent product scope, but Xyool did not arm a scope-expansion timer before the later funded commitment.

The failure mode is not lack of information. It is failure to convert available information into an explicit causal clock.

This process is intended to eliminate avoidable misses where:
- the evidence was public;
- the causal transition was inferable;
- but Xyool did not ask the question that would have created the timer.

---

## Breadcrumb classes

### 1. Customer-Evaluation Breadcrumb
Examples:
- testing;
- final product selection;
- field trial;
- pilot;
- integration work;
- qualification activity;
- engineering validation.

Likely timers:
- Integration-to-Acceptance;
- Acceptance-to-Procurement;
- Existing-Customer Scope Expansion.

### 2. Customer-Scope Breadcrumb
Examples:
- current customer evaluating an adjacent product/service;
- management says relationship scope is expanding;
- new category/site/application under discussion;
- existing contract plus active adjacent testing.

Likely timer:
- Existing-Customer Scope Expansion Timer.

### 3. Repeat / Rollout Breadcrumb
Examples:
- second site;
- second lot;
- follow-on task order;
- repeat deployment;
- another geography/unit using the same process.

Likely timers:
- Repeat-Cadence;
- Rollout Probability Timer;
- Reference-Customer Cascade Timer.

### 4. Funding Breadcrumb
Examples:
- appropriation;
- budget line;
- customer-funded development;
- board approval;
- committed capex;
- contract definitization progress.

Likely timers:
- Signal-to-Funding;
- Acceptance-to-Procurement;
- Capacity-Build.

### 5. Capacity / Supply Breadcrumb
Examples:
- equipment ordered;
- facility construction;
- staffing for ramp;
- tooling installed;
- supplier qualification;
- incremental feedstock/offtake secured.

Likely timers:
- Capacity-Build;
- Procurement-to-Deployment;
- Backlog-Conversion.

### 6. Installed-Base Consumption Breadcrumb
Examples:
- spares usage;
- warehouse depletion;
- maintenance intensity;
- fleet utilization;
- consumables demand;
- refurbishment/repair volume.

Likely timer:
- Replenishment Timer.

### 7. Institutionalization Breadcrumb
Examples:
- training equipment;
- curriculum use;
- doctrine/specification language;
- standard workflow insertion;
- dedicated school/academy use.

Likely timer:
- Institutionalization Timer.

### 8. Management-Timing Breadcrumb
Examples:
- "imminent";
- "near term";
- "this quarter";
- "by year end";
- stated acceptance/procurement timing.

Likely overlay:
- Management Timing Credibility Timer.

Management language alone must not create a high-confidence economic timer.

### 9. Financial-Translation Breadcrumb
Examples:
- guidance increase after operating evidence;
- backlog conversion reflected in expected revenue;
- margin guidance improves after mix shift;
- cash-flow outlook improves after deployment.

Likely timers:
- Deployment-to-Revenue/Cash;
- Backlog-Conversion;
- Recognition Timer.

Do not double count financial translation as independent evidence when it is merely the accounting consequence of the same underlying order.

### 10. Capital-Structure Breadcrumb
Examples:
- shrinking liquidity;
- increasing revolver usage;
- expensive bridge financing;
- convertibles;
- covenant amendments;
- ATM use.

Likely timer:
- Financing / Runway Timer.

This usually affects Quality/shareholder capture rather than positive TTC promotion.

---

## Mandatory breadcrumb scan

For every earnings call, 10-Q/10-K, investor presentation, material press release, contract notice, and relevant customer/agency disclosure, scan for:

```text
CUSTOMER
- new customer?
- existing customer expanding scope?
- testing / pilot / final selection?
- repeat site / unit / order?

PRODUCT / PROGRAM
- integration?
- acceptance / qualification?
- funded transition?
- production readiness?

PROCUREMENT / FUNDING
- authorization?
- obligation?
- definitization?
- funded minimum?
- delivery schedule?

CAPACITY / SUPPLY
- equipment / facility / staffing / feedstock?
- bottleneck removed or forming?

INSTALLED BASE
- consumption / spares / repair / replenishment?

INSTITUTIONALIZATION
- training / curriculum / standardization / doctrine?

FINANCIAL TRANSLATION
- backlog → revenue?
- order → guidance?
- revenue → margin/cash?

TIMING LANGUAGE
- explicit window?
- management timing credibility?

NEGATIVE BREADCRUMBS
- delay?
- failed test?
- lost customer?
- financing need?
- order cancellation?
```

A scan is incomplete until each material breadcrumb is either linked to a timer and, when applicable, a dependency-graph node/edge, or explicitly rejected as non-causal/noise.

---

## Breadcrumb evidence packet

Every material breadcrumb should record:

```text
Breadcrumb:
Source:
Source Date:
Customer / Program:
Breadcrumb Class:
Direct or Inferred:
Evidence Quality: FE1-FE4 or equivalent
Economic Relevance: Low / Medium / High

Causal Transition Suggested:
Dependency Node ID:
Required Upstream Node(s):
Downstream Economic Node:
Candidate Timer Type:
Proposed Start Event:
Proposed Start Date:
Expected Stop Event:
Historical / Comparable Timing Evidence:

State:
  WATCHING / ARMED / ACTIVE / REALIZED / FAILED / STALE / SUPERSEDED

Promotion Trigger:
Demotion Trigger:
Invalidation:
Double-Counting Risk:
Next Research Question:
```

---

## Timer-state progression

### WATCHING
Interesting language/evidence exists but the causal transition is not specific enough.

### ARMED
A specific causal transition is identifiable and a timer can be defined, but evidence is still early or incomplete.

### ACTIVE
The start event is sufficiently evidenced and the clock is running.

### REALIZED
The stop event occurred. Close the timer and identify the next timer.

### FAILED
The causal path broke.

### STALE
Expected window passed without adequate confirmation.

### SUPERSEDED
A newer event changed the relevant causal clock.

Rule:

> **Do not leave realized timers running, and do not silently move stale windows forward.**

---

## Nameless example

A company already provides maintenance services to a large retailer.

Management later says the same retailer is testing an adjacent product category and is in final product selection. No purchase order exists yet.

Correct treatment:

```text
Breadcrumb: adjacent product testing + final selection
Class: Existing-customer scope
Timer: Existing-Customer Scope Expansion
State: ARMED
Stop Event: funded adjacent-scope order
```

If the order arrives, the timer closes REALIZED and a Procurement-to-Deployment or Backlog-Conversion Timer may begin.

Incorrect treatment:
- count the future order as backlog;
- assume management optimism guarantees an award;
- ignore the evidence until the order is announced.

---

## Counterexample

Management says there is a "large pipeline" and many customers are interested, but no named customer, testing, selection, funding, qualification, or procurement evidence exists.

Do not arm a high-confidence timer.

At most classify as WATCHING / weak breadcrumb until a causal transition becomes observable.

---

## Breadcrumb confluence

Multiple breadcrumbs can strengthen a timer when they reduce different uncertainties.

Example:

```text
customer testing
+ final product selection
+ management near-term timing
+ reusable existing contract relationship
```

This is stronger than any one item alone.

But do not mechanically count four breadcrumbs as four independent catalysts.

Ask:

> **Do these breadcrumbs independently reduce different uncertainties, or are they multiple descriptions of the same underlying fact?**

This distinction is mandatory to avoid double counting.

---

## Relationship to timer confluence

Breadcrumb detection occurs before timer confluence analysis.

```text
BREADCRUMBS
→ detect / arm individual timers

TIMERS
→ identify serial or parallel causal clocks

TIMER CONFLUENCE
→ assess whether multiple distinct clocks reinforce probability, materiality, or return velocity

TTC
→ rank qualified capital destinations
```

Timer count alone does not raise TTC.

Independent or sequentially compressing timers can matter more than duplicated evidence around one event.

---

## Research priority rule

When an ARMED timer could materially change TTC ranking, Xyool should proactively search for:
- same-company historical interval;
- same-customer precedent;
- same procurement/approval mechanism;
- comparable customer behavior;
- evidence that the remaining gate is reusable rather than starting over;
- hidden negative constraints.

The goal is to convert an ARMED timer into ACTIVE, reject it, or calibrate its window before the final headline where possible.

---

## Anti-false-positive rules

Do not promote a breadcrumb merely because:
- stock price moved;
- management uses promotional language;
- TAM is large;
- an analyst speculates;
- an option/ceiling exists;
- two unrelated events happen near each other;
- the same fact appears in multiple sources;
- a customer is unnamed and no causal activity is observable;
- a historical winner makes a similar phrase look meaningful in hindsight.

Every breadcrumb must point to a specific causal transition.

---

## Effect on TTC

Breadcrumbs may affect TTC only through structured causal evidence.

They can improve:
- research priority;
- FES stage/velocity;
- probability estimate;
- timer confidence;
- expected window;
- recognition-gap analysis;
- return velocity;
- ranking among qualified opportunities.

They cannot independently:
- create Quality;
- create funded economics;
- count future orders as revenue/backlog;
- override shareholder-capture failure;
- force a trade.

---

## Validation status

The mandatory breadcrumb scan and Breadcrumb → Timer conversion process are promoted as a **process requirement** because recent misses involved public pre-outcome evidence that was not converted into explicit timers.

Specific breadcrumb predictive weights, numeric probability boosts, and universal timing formulas are **not promoted**.

Future validation should measure:
- which breadcrumb classes most often precede real timer completion;
- false-positive rates by evidence quality;
- incremental value of breadcrumb confluence;
- whether ARMED timers improve TTC rankings before headline realization;
- whether detection gains survive negative controls and untouched holdouts.
