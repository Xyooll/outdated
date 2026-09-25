# FLOW — Observation / Trigger

FLOW ID: CORE-OBSERVATION-TRIGGER
STATUS: **CANDIDATE / VERIFICATION_PENDING**
DOMAIN: core
JOB: decide whether a newly observed change, due condition, or resolved outcome should be ignored, recorded, queued, or trigger Xyool work
AUTHORITY: attention-entry routing only; no authority to decide domain truth, action, capital, or external execution
PARENT GOALPOST: ../../research/system-tests/floware-consolidation-v1-2026-09-24/GOALPOST.md
UPSTREAM FLOWS: external/source adapters, persistent domain state, Run Record/continuity, user-authorized observation context
DOWNSTREAM FLOWS: Resource Allocation, Xyool Execution, Evidence to State, applicable domain Flow
INBOUND PIPES: PLUMBING.md#pipe-core-observation-in
OUTBOUND PIPES: PLUMBING.md#pipe-core-observation-resource, PLUMBING.md#pipe-core-observation-execution
SOFTWARE DEPENDENCIES: none for reasoning; future scheduler/feed adapters may invoke this Flow

## GOAL

Recognize material change without forcing Xyool to continuously re-research everything.

Core law:

> **Observe broadly only when justified; trigger narrowly on material change.**

## GOALPOST

An observation is resolved when Xyool can state:
- what changed or became due;
- compared with what prior state/cursor;
- whether the change is new;
- whether it is material to any active object/goal;
- which object/Flow could be affected;
- whether immediate work, queued work, record-only, or no action is appropriate;
- what evidence/freshness remains unknown.

## INPUT STATE

Examples:
- new source item/version/hash;
- timer/deadline becoming due;
- resolved outcome;
- changed permission/availability;
- changed state/evidence head;
- explicit user observation;
- previous cursor/state;
- active goals/watch objects where available.

## EVIDENCE

Use source identity, timestamps/versions, prior cursors, current state, active goalposts, and domain materiality contracts.

Observation may identify a candidate change before full Research proves its meaning.

## PROCESS

~~~text
RECEIVE OBSERVATION
→ LOCK SOURCE / OBJECT IDENTITY
→ COMPARE WITH PRIOR CURSOR / STATE
→ DUPLICATE?
    YES → RECORD/IGNORE
→ NAME DELTA
→ IDENTIFY POSSIBLY AFFECTED GOAL / OBJECT / FLOW
→ CHECK MATERIALITY + CONSEQUENCE OF DELAY
→ CLASSIFY:
    IGNORE
    RECORD_ONLY
    QUEUE
    TRIGGER_NOW
    BLOCKED_UNKNOWN
→ IF MULTIPLE TRIGGERS COMPETE:
    ROUTE TO RESOURCE ALLOCATION
→ IF IMMEDIATE MATERIAL TRIGGER:
    ROUTE TO XYOOL EXECUTION
→ FULL DOMAIN INTERPRETATION REMAINS WITH THE OWNING FLOW
~~~

## TRIGGER CLASSES

Generic triggers may include:
- new evidence/source;
- stale/due refresh;
- deadline/timer;
- resolved outcome;
- external state change;
- authority/permission change;
- dependency completion/failure;
- user-requested watch object.

Do not create domain conclusions from trigger class alone.

## GATES

- stable object/source identity;
- novelty/delta check;
- materiality reason;
- destination owner;
- no authority increase.

## ADAPTATION

If materiality cannot be decided cheaply, queue a bounded Research/Direct Resolution task rather than escalating the whole system.

If several observations collapse to one underlying state change, deduplicate while preserving provenance.

## BOUNDARIES

This Flow does not:
- continuously poll by itself;
- decide the substantive domain answer;
- execute external actions;
- promote candidates;
- allocate final resources when multiple jobs compete;
- invent urgency from price/noise/volume or analogous domain signals.

## FAIL-CLOSED CONDITIONS

Return BLOCKED_UNKNOWN when identity, prior state, or materiality cannot be established and acting could cause material waste or consequence.

## OUTPUT STATE

~~~text
OBSERVATION ID:
SOURCE / OBJECT:
PRIOR CURSOR / STATE:
CURRENT CURSOR / STATE:
DELTA:
NOVELTY:
MATERIALITY:
AFFECTED GOAL / OBJECT / FLOW:
DISPOSITION:
URGENCY / CONSEQUENCE OF DELAY:
PROVENANCE:
NEXT OWNER:
~~~

## LEARNING HOOK

Missed triggers, noisy false triggers, and repeatedly wasted wake-ups become Learning evidence for materiality/attention rules.

## SOFTWARE / HARD-LIMIT BOUNDARY

NONE — FLOWARE SUFFICIENT FOR TRIGGER REASONING

Continuous wake-up, polling, RSS/feed ingestion, timers, or durable queues require software/infrastructure only when later justified by Software Escalation.

## COMPLEXITY RULE

Deduplicate and perform the cheapest materiality check first. Do not turn every source item, timer tick, or unchanged cursor into a Xyool task.
