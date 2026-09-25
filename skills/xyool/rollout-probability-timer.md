# Xyool — Rollout Probability Timer (RPT)

Status: **MANDATORY TTC TIMING INTERPRETATION FOR REPEAT / CASCADE EVENTS — PROVISIONAL CALIBRATION**

## Core purpose

The Rollout Probability Timer answers:

> **Given evidence that a deployment, order, site, unit, lot, replenishment cycle, or other economic event can repeat, where are we in the evidence-backed window for the next repeat — and is the conditional probability of a near-term event rising, stable, or falling?**

RPT is not a deterministic countdown. It is a timing interpretation inside TTC.

## Why it exists

A repeat event contains two different pieces of information:

1. **Replication evidence** — the process happened again.
2. **Timing evidence** — the spacing between comparable events may tell us something about when another repeat becomes more likely.

Without an explicit timer, Xyool can correctly recognize a rollout but still underweight its near-term capital relevance.

The failure mode is:

```text
FIRST EVENT
→ SECOND COMPARABLE EVENT
→ Xyool recognizes cascade
→ but treats future timing as static
→ misses that the next-return window is approaching
```

RPT prevents that timing blind spot.

## Relationship to other modules

```text
CASCADE SCORE
Is replication happening?
        ↓
REPEAT-CADENCE QUESTION
What repeats, and what interval(s) have we observed?
        ↓
ROLLOUT PROBABILITY TIMER
Where are we now relative to the next evidence-backed repeat window?
        ↓
TTC
How does this change probability-adjusted return velocity and capital priority?
```

RPT has no independent capital authority.

## Core behavior

For an intact qualified opportunity with a credible repeat mechanism:

```text
PRE-WINDOW
→ repeat thesis exists, but near-term timing advantage is limited

APPROACHING WINDOW
→ expected waiting time falls; near-term event probability may begin to rise

EARLY / MID WINDOW
→ timing support strengthens if the causal process remains intact

LATE WINDOW
→ event can still occur, but absence of expected confirmation becomes increasingly informative

OVERDUE
→ timing support decays; probability/confidence must fall unless new evidence credibly resets the window
```

The correct shape is generally:

> **rise into the supported window, then decay if the repeat fails to appear.**

Time does not create evidence by itself.

## Mandatory question

For every qualifying rollout/repeat candidate ask:

> **Where are we on the Rollout Probability Timer, and what evidence would justify moving the timer forward, backward, or resetting it?**

## Required inputs

```text
Repeatable Unit:
Comparable Event Type: award / order / deployment start / shipment start / acceptance / completion / replenishment / other
Comparable Event Dates:
Observed Interval(s):
Number of Observed Intervals:
Cadence State: None / Emerging / Established / Accelerating / Decelerating / Broken
Cadence Confidence: Low / Medium / High
Same Customer / Program?:
Same Product / Mechanism?:
Qualification Reused?:
Funding Path Reused?:
Remaining Addressable Repeat Units:
Best Evidence Continued Need Exists:
Known Constraints:
Expected Next Repeat Window:
Current Window Position: Pre / Approaching / Early / Mid / Late / Overdue
Last Confirming Evidence Date:
Contradictory Evidence:
Recognition Gap:
Next Trigger:
Invalidation:
```

## Event-anchor consistency rule

RPT intervals must compare the **same kind of economic event** unless there is explicit evidence that one event type causally governs the next.

Do not silently mix:
- award date with completion date;
- order date with shipment date;
- deployment start with customer acceptance;
- acceptance with replenishment;
- authorization with funded task order.

If the first comparable evidence is an award and the second comparable evidence is another award, the observed cadence is **award-to-award** unless a completion/acceptance date is independently established and shown to be the true trigger for the next award.

If multiple event types are observable, keep parallel clocks when useful:

```text
award → award
award → deployment start
deployment start → acceptance
acceptance → repeat award
```

Do not substitute one clock for another merely because it is easier to measure.

### Why this matters

A second order can arrive before the first deployment is publicly reported as complete. In that case, the customer may have gained enough confidence from partial execution, early shipments, or operational progress to expand before full completion.

That pattern is stronger cascade evidence than a model that assumes every rollout requires full completion before the next order.

## One-interval rule

One observed interval is **Emerging**, not Established.

With one interval:
- use a widened range rather than an exact date;
- keep confidence low or low-to-medium unless independent rollout evidence is strong;
- do not infer an indefinite periodic sequence;
- do not count future unawarded repeats as backlog/revenue;
- use the timer as a research and TTC timing input, not as a promised event date.

## Nameless example

A small supplier wins a paid installation at one large customer's facility.

Three months later, the same customer orders a second facility using the same product and deployment process. Public disclosures show shipments into the first facility had begun, but do not establish that the first site was fully completed before the second order.

The correct interpretation is:

```text
Repeatable unit: customer facility
Comparable event type: award/order
Observed comparable interval: ~3 months award-to-award
Cadence: Emerging
Next-repeat window: centered near the observed interval but widened materially
Completion-to-repeat cadence: unknown unless completion timing is separately established
```

One month after the second order, the timer is still mostly pre-window.

As the company moves closer to the widened window, TTC may strengthen because expected waiting time is falling.

If another facility is ordered, the rollout evidence strengthens and the timer resets from that new comparable event.

If the widened window passes without a follow-on and there is no credible explanation, cadence confidence falls and TTC timing support decays.

## Counterexample

Two customers place unrelated orders three months apart for different products and under different procurement paths.

Do **not** start a single Rollout Probability Timer merely because the dates resemble a cadence.

The repeated unit, event type, and causal mechanism must actually be comparable.

## What can raise RPT support

RPT timing support can rise when:
- the same customer/program is expanding;
- the same approval/procurement path is reusable;
- qualification has already been cleared;
- addressable repeat units clearly remain;
- rollout capacity/funding remains available;
- customer need remains evident;
- new pre-order signals appear;
- multiple comparable intervals reinforce the cadence;
- intervals shorten without deterioration in evidence quality.

## What can reduce RPT support

Reduce or reset support when:
- repeat units are exhausted;
- the customer pauses or changes architecture;
- funding disappears;
- deployment capacity is constrained;
- the next order requires a new qualification path;
- prior timing was management aspiration rather than actual event spacing;
- the expected window passes without confirmation;
- repeated unexplained window extensions occur;
- recognition has already consumed the remaining economic opportunity.

## Effect on TTC ranking

RPT affects **return velocity**, not company quality.

Conceptually:

```text
credible expected payoff remains intact
+ expected waiting time compresses
+ near-term conditional event probability rises
= TTC can rise
```

Therefore a qualified rollout candidate can move higher in TTC **before** the next order is announced.

But:

```text
HIGHER TTC RANK
≠
AUTOMATIC ROTATION
```

New/unallocated capital can respond more aggressively to RPT changes.

Earned capital in another intact qualified holding still requires the normal higher replacement hurdle.

## Probability interpretation

Do not say that the probability of an eventual repeat rises merely because time passes.

The relevant question is the **conditional probability of a near-term repeat given survival of the causal thesis and current position inside the supported window**.

RPT should distinguish:
- eventual event probability;
- near-term event probability;
- expected waiting time.

Those are not the same thing.

## Window reset governance

When timing changes, record:

```text
Old Window:
New Evidence:
New Window:
Reason for Reset:
Confidence Change:
```

Do not silently move the expected window forward after a miss.

Repeated unexplained resets are negative evidence.

## Validation status

The **Rollout Probability Timer concept and mandatory interpretation are promoted** because repeat timing is part of TTC's core job.

The exact probability curve is **not promoted**.

No universal hazard function, date multiplier, or fixed probability percentage is approved.

Future validation should test:
- event incidence by pre/approaching/early/mid/late/overdue state;
- one-interval versus multi-interval timers;
- same-customer versus cross-customer replication;
- award-to-award versus completion-to-repeat clocks;
- false positives where a second deployment never became a broader rollout;
- whether RPT improves next-dollar allocation after controlling for Quality, recognition, and shareholder capture.
