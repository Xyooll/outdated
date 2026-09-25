# Xyool — TTC Repeat-Cadence Question

Status: **MANDATORY TTC QUESTION / PROVISIONAL TIMING INPUT — NO INDEPENDENT CAPITAL AUTHORITY**

## Why this exists

The OSE Cascade Score already asks whether a validated deployment is replicating across sites, units, programs, customers, or geographies.

A live OESX review exposed a separate timing gap: Xyool recognized a same-customer repeat facility order but did not force TTC to convert the observed first→second interval into a forward hypothesis for the next comparable event.

The missing question is temporal, not categorical.

## Mandatory question

After every material order, deployment, award, acceptance, replenishment, site expansion, production lot, or other repeatable economic event, TTC must ask:

> **Is this event a one-off, or one unit in a repeatable rollout? If it is repeatable, what is the best evidence-backed interval to the next economically meaningful unit of replication?**

A shorter operational form is:

> **What repeats, and when could it repeat again?**

This question is mandatory whenever Cascade Score is CS2+ or equivalent evidence suggests replication may be possible.

## Purpose

This question converts repeat evidence into a forward TTC clock without pretending that one observed interval is a guaranteed schedule.

The causal chain is:

```text
FIRST REAL DEPLOYMENT / ORDER
        ↓
REPEAT DEPLOYMENT / ORDER
        ↓
IDENTIFY REPEATABLE UNIT
        ↓
MEASURE OBSERVED INTERVAL(S)
        ↓
CHECK WHETHER THE SAME CAUSAL PROCESS CAN REPEAT
        ↓
ESTIMATE NEXT PLAUSIBLE REPEAT WINDOW
        ↓
UPDATE TTC
```

## Required fields

For every material repeat/cascade candidate, record:

```text
Repeatable Unit:
  facility / site / lot / task order / vessel / vehicle / customer / geography /
  replenishment cycle / production tranche / other

First Comparable Event Date:
Latest Comparable Event Date:
Prior Comparable Event Dates:
Observed Interval(s):
Number of Observed Intervals:

Same Customer?: Yes / No
Same Program / Product?: Yes / No
Same Procurement / Approval Mechanism?: Yes / No
Qualification Reused?: Yes / No / Unknown
Funding Path Reused?: Yes / No / Unknown
Operational Bottleneck Reused?: Yes / No / Unknown

Remaining Addressable Repeat Units:
Best Evidence of Continued Need:
Known Constraint on Repetition:

Cadence State:
  None / Emerging / Established / Accelerating / Decelerating / Broken

Cadence Confidence:
  Low / Medium / High

Expected Next Repeat Window:
Window Position:
Next Trigger:
Invalidation:
```

## Timing evidence hierarchy

Use the most specific causal evidence available:

1. same company + same customer + same product/program + same repeat unit;
2. same company + same customer/program, different repeat unit;
3. same company + same procurement/commercial mechanism;
4. same company historical analog;
5. same customer/agency analog;
6. close industry comparison;
7. broad sector cadence only as a fallback.

The more the causal process changes, the less the prior interval should control TTC.

## One-interval rule

One observed first→second interval is useful evidence, but it is **not an established cadence**.

With one interval:
- classify cadence as **Emerging** at most;
- treat the next-event estimate as a **range**, not a date;
- keep Cadence Confidence low unless independent evidence strongly supports a scheduled rollout;
- do not extrapolate a long sequence of future orders;
- do not count unawarded repeat units as backlog or revenue.

Example:

```text
First site: June 8
Second site: September 8
Observed interval: ~3 months

Correct interpretation:
  Emerging repeat cadence.
  Next comparable event plausibly centered near another ~3-month interval,
  with a wider evidence-backed window.

Incorrect interpretation:
  "The company will receive another order exactly December 8."
```

## Multiple-interval rule

When two or more comparable intervals exist, TTC must check:
- median and range of intervals;
- whether intervals are shortening or lengthening;
- whether the same customer/process is responsible;
- whether capacity, funding, approval, seasonality, or customer budgeting changed;
- whether the repeatable unit itself changed in size.

Do not average unlike events merely to manufacture a cadence.

If repeated intervals shorten while evidence quality remains high, classify cadence as **Accelerating**.

If intervals lengthen or expected repeats fail without explanation, classify as **Decelerating** or **Broken** and lower TTC probability/velocity accordingly.

## Relationship to Cascade Score

Cascade Score answers:

> **Is replication happening?**

Repeat-Cadence asks:

> **Given that replication may be happening, what does the time spacing imply about the next plausible replication event?**

Therefore:

```text
CASCADE SCORE
replication state / breadth
        ↓
REPEAT-CADENCE QUESTION
time structure of replication
        ↓
TTC
capital-priority interpretation
```

Do not double count the same repeat event as separate independent evidence in Cascade Score, FES, and TTC. Cascade establishes replication; cadence interprets its timing; TTC makes the capital decision.

## Relationship to FES

A repeat event may:
- increase FES velocity;
- improve confidence that a path is repeatable;
- create a new expected conversion/repeat window;
- identify the next funded/order/fielding trigger.

But a predicted repeat does not itself promote FES.

Only actual evidence can promote the state.

## Relationship to TTC ranking

A repeat cadence can materially improve TTC when all of the following are true:
- the equity passes Quality;
- the repeat events are economically meaningful;
- evidence shows the same causal process can continue;
- remaining addressable units/sites/orders exist;
- the next repeat window is reasonably near;
- recognition has not already consumed the economics;
- shareholder capture remains acceptable.

A high-quality repeat cadence should increase expected return velocity relative to an otherwise similar opportunity with no visible replication clock.

It does **not** automatically outrank a larger, more probable, or less-recognized catalyst elsewhere.

## Anti-false-positive rules

Do not infer a repeat cadence from:
- two unrelated customers buying at different times;
- one contract plus management discussion of pipeline;
- option ceilings or maximum quantities;
- framework authorization without funded repeat orders;
- seasonality mistaken for customer rollout;
- stock-price moves;
- analyst estimates;
- a single renewal where no remaining replication units exist;
- acquisitions creating artificial revenue repetition.

A repeat cadence must be tied to a plausible repeated economic unit and a causal reason the process can recur.

## OESX regression lesson

The OESX case exposed the gap:

```text
First hyperscaler facility
→ second facility from the same customer roughly three months later
```

Xyool correctly recognized the second event as stronger cascade evidence, but the live ranking underweighted it because TTC did not explicitly ask whether the first→second interval created a forward third-facility clock.

The corrected interpretation is:
- repeat unit: hyperscaler facility deployment;
- same customer: yes;
- repeat evidence: direct and paid;
- observed intervals: one;
- cadence state: Emerging;
- cadence confidence: Low-to-Medium depending on corroborating rollout evidence;
- next repeat window: centered on the observed interval but widened substantially because N=1;
- TTC implication: stronger near-term return-velocity case than a static recognition-only reading implied.

This is a process correction, not proof that a third OESX facility must arrive on schedule.

## Mandatory event-update insertion

Every TTC event update now includes:

```text
NEW MATERIAL EVENT
      ↓
DOES IT REVEAL A REPEATABLE UNIT?
      ↓
HAS A COMPARABLE EVENT OCCURRED BEFORE?
      ↓
IF YES: MEASURE INTERVAL(S)
      ↓
IS THE CAUSAL PROCESS REUSABLE?
      ↓
SET / UPDATE NEXT REPEAT WINDOW
      ↓
UPDATE CADENCE STATE + CONFIDENCE
      ↓
RECALCULATE TTC RETURN VELOCITY
```

## Validation requirement

The question itself is mandatory because failing to ask it creates a systematic blind spot.

The **numeric predictive value of observed cadence remains provisional** and must be tested across both successful and failed cascades.

Future validation should measure:
- probability of another repeat after CS3 / first repeat;
- error of next-event windows by evidence hierarchy;
- one-interval vs multi-interval precision;
- accelerating vs decelerating cadence outcomes;
- false positives where first repeat never became a rollout;
- whether cadence-aware TTC improves capital decisions after controlling for recognition and quality.

Do not promote a mechanical cadence formula until it survives point-in-time holdouts.