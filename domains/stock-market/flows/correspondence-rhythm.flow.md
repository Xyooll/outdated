# FLOW — Stock Correspondence Rhythm

FLOW ID: `STOCK-CORRESPONDENCE-RHYTHM-V1`  
STATUS: **ACTIVE / DEVELOPMENT**  
DOMAIN: stock-market  
JOB: infer the temporal structure of an unresolved catalyst from corresponding completed processes

## GOAL

For a stock whose thesis is waiting on an unresolved catalyst, estimate the **rhythm of the process** that produces that catalyst.

Core law:

> **Do not ask only when the catalyst will happen. Ask what process creates it, where the company is inside that process, and how structurally corresponding processes have moved through the same states.**

## 1. START WITH THE PROCESS, NOT THE STOCK

Identify the causal protocol.

Examples:

```text
PROCUREMENT
RFP / BID / AWARD
GOVERNMENT BUDGET → CONTRACT
REGULATORY REVIEW
CLINICAL TRIAL → DATA → FILING → DECISION
FACILITY QUALIFICATION
CUSTOMER TEST → APPROVAL → PRODUCTION
JV NEGOTIATION → DEFINITIVE AGREEMENT → CLOSE
M&A SIGNING → CONDITIONS → CLOSE
MANUFACTURING VALIDATION → SCALE → DELIVERY
```

The ticker is the object experiencing the process.

The rhythm belongs primarily to the process.

## 2. CURRENT STATE

Map the company onto the process:

```text
PROCESS:
CURRENT STAGE:
PREVIOUS VERIFIED STAGE:
NEXT REQUIRED STAGE:
KNOWN GATES:
KNOWN DATES / WINDOWS:
DEPENDENCIES:
BLOCKERS:
EVIDENCE FRESHNESS:
```

If an exact contractual/statutory date exists, it outranks analog rhythm.

## 3. CORRESPONDENCE SET

Find completed examples with the same important structure.

Prefer correspondence on:

- same protocol;
- same buyer / regulator / agency class;
- similar procurement authority;
- similar gate sequence;
- similar contract size/complexity;
- similar dependency count;
- similar qualification burden;
- similar funding/budget source;
- similar geography/jurisdiction when timing depends on it.

Do not choose analogs merely because the companies look alike.

## 4. EXTRACT THE RHYTHM

For each corresponding process record:

```text
STATE A → STATE B: dwell time
STATE B → STATE C: dwell time
STATE C → terminal event: dwell time

delays
accelerations
restarts
seasonality
budget/calendar effects
approval cadence
```

Then derive:

```text
NORMAL RHYTHM
FAST PATH
SLOW PATH
COMMON DELAY POINT
TERMINAL WINDOW
```

Prefer a range/distribution over a fake exact date.

## 5. RHYTHM IS CONDITIONAL

Rhythm is not prophecy.

It means:

> **Given that this process has reached state X under conditions Y, corresponding processes tend to reach state Z on this kind of cadence.**

A new state can reset the rhythm immediately.

## 6. CORRESPONDENCE BEAM

A **Correspondence Beam** is the structural line connecting the live case to one or more analog processes.

```text
LIVE STATE
   ╲
    ╲ structural correspondence
     ╲
COMPLETED PROCESS ANALOG
     ↓
observed transitions / dwell times
     ↓
RHYTHM FOR LIVE PROCESS
```

A strong beam requires the relationship driving time to be the same.

A weak beam shares superficial similarity but not the timing mechanism.

## 7. STORY INTEGRATION

The rhythm should become part of the stock story.

Example:

```text
CODA has already completed X.
The thesis is waiting on Y.
Y is produced by procurement process P.
Corresponding P processes usually pass through A → B → C.
CODA appears to be at B.
The historical B → C rhythm is approximately [range].
The main delay mechanism is D.
Therefore the catalyst window is better represented as [conditional window],
not an arbitrary date.
```

## 7A. DEDUCTION FORM

The useful output is a conditional deduction:

> **Based on the live process state, known evidence, and the rhythm of corresponding completed processes, event/state X may occur during window Y, unless dependency Z delays or resets the process.**

This is the bridge from correspondence to thesis.

Do not report analog timing without stating:
- why the analog corresponds;
- what stage the live case is in;
- what could break the timing relationship.

## 8. MISS AUDIT

A rhythm miss occurs when Xyool:

- compares the wrong process;
- ignores a known stage transition;
- overlooks a procedural dependency;
- uses stock-price analogs instead of process analogs;
- ignores a calendar/budget/protocol constraint;
- retains an old rhythm after the process state changes;
- mistakes a broad window for an exact prediction.

## 9. OUTPUT

```text
CATALYST:
PROCESS:
CURRENT STAGE:
NEXT GATE:
CORRESPONDENCE BEAM(S):
ANALOG PROCESS SET:
NORMAL RHYTHM:
FAST PATH:
SLOW PATH:
PRIMARY DELAY MECHANISM:
CONDITIONAL CATALYST WINDOW:
WHAT WOULD RESET THE RHYTHM:
CONFIDENCE:
```

## 10. RELATION TO TTC

Correspondence Rhythm informs TTC.

It does not replace TTC.

```text
CORRESPONDENCE RHYTHM
→ better causal timer
→ better event window
→ better holding / opportunity-cost estimate
→ TTC / capital-path state
```

## SOFTWARE / HARD-LIMIT BOUNDARY

`NONE — FLOWARE SUFFICIENT`