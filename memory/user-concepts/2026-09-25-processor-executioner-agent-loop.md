# Processor / Executioner Agent Loop

DATE: 2026-09-25
STATUS: **ACTIVE / FUTURE AUTONOMY ARCHITECTURE CONCEPT**

## USER IDEA

ChatGPT acts as the Processor while an agent acts as the Executioner.

The user begins by talking with ChatGPT. The conversational reasoning result can be compiled into a bounded prompt/job capsule. That output alerts/wakes the execution agent. The execution agent performs the work, writes durable state/results to Git, returns a compact receipt, and alerts the Processor. The Processor interprets the result, talks with the user, and may issue the next bounded job.

## CORE LOOP

~~~text
USER
→ CHATGPT / PROCESSOR
→ XYOOL CORE
→ JOB CAPSULE / COMPILED PROMPT
→ JOB_READY EVENT
→ EXECUTION AGENT / EXECUTIONER
→ GIT / DURABLE STATE
→ EXECUTION RECEIPT
→ JOB_COMPLETE / JOB_BLOCKED EVENT
→ CHATGPT / PROCESSOR
→ USER
→ repeat
~~~

## ROLE SPLIT

### ChatGPT / Processor

- conversation and intent recognition;
- reasoning and question refinement;
- goalpost/Flow/domain selection;
- context compilation;
- interpretation of execution results;
- deciding whether another job is warranted;
- explaining the result to the user.

### Xyool Core

- routing/orchestration;
- authority boundaries;
- Resource Allocation;
- Sequencing;
- Observation/Trigger;
- Failure handling;
- deciding which agent/Flow/context is required.

### Execution Agent / Executioner

- receives bounded work;
- loads only required Git pointers/context;
- researches/calculates/edits/tests/calls tools;
- writes results/evidence/state;
- returns a compact execution receipt;
- may request follow-up work but should not self-authorize an endless recursive mission.

### Git

- durable cognitive state;
- Floware contracts;
- domain rules/libraries;
- run artifacts;
- evidence/provenance;
- learned state;
- job/receipt pointers where appropriate.

## CONTEXT-CAPSULE PRINCIPLE

The agent should not receive the whole conversation or repository by default.

Compile the minimum sufficient context:

~~~text
JOB ID
GOAL
GOALPOST
AUTHORITY
FLOW
DOMAIN
REQUIRED GIT POINTERS
CURRENT STATE
INPUT EVIDENCE
DO
DO NOT
EXPECTED OUTPUT
FAILURE CONDITIONS
~~~

Token savings come from context isolation and pointer-based retrieval, not merely from adding more agents.

## EVENT MODEL

Candidate event types:

- JOB_READY;
- JOB_COMPLETE;
- JOB_BLOCKED;
- NEW_EVIDENCE;
- FAILURE_DETECTED;
- OUTCOME_RESOLVED;
- TIMER_DUE;
- SOURCE_CHANGED;
- AUDIT_REQUIRED.

These should correspond to Observation/Trigger, Resource Allocation, Sequencing, Failure, Learning, and other existing Flows rather than creating a second reasoning architecture.

## EXECUTION RECEIPT

A compact return object may include:

~~~text
JOB ID
STATUS
COMMITS / ARTIFACT POINTERS
CHANGED SURFACES
RESULT SUMMARY
FAILURES / BLOCKERS
NEW QUESTIONS
LOCAL CHECKS
FOLLOW-UP REQUESTS
~~~

The Processor should inspect full Git artifacts only when needed.

## IMPORTANT ARCHITECTURAL PRINCIPLE

> **The agent does not need to remember Xyool. Xyool remembers Xyool.**

The agent may be disposable/stateless. Durable intelligence resides in Git, Floware, Domain Libraries, and Core orchestration.

## AUTHORITY RULE

The Executioner may propose follow-up work but should normally not decide its own next mission.

Preferred:

~~~text
EXECUTIONER
→ REQUEST / RECEIPT
→ PROCESSOR / CORE
→ AUTHORIZE NEXT JOB IF WARRANTED
~~~

Not:

~~~text
EXECUTIONER
→ unrestricted self-spawning loop
~~~

## RELATION TO EXISTING FUTURE BUILD ITEMS

This concept refines:
- Autonomous Flow runner;
- durable work queue / event bus;
- programmatic tool orchestration;
- multi-agent / parallel-worker runtime;
- run-record/checkpoint persistence;
- Git-aware development support.

## BUILD BOUNDARY

CONCEPT ONLY / DO NOT IMPLEMENT YET.

Before implementation:
- prove the single-context/token-cost bottleneck;
- define Agent Contract;
- define Job Capsule contract;
- define Execution Receipt contract;
- define event semantics;
- verify how much existing parked runtime can be reused;
- pass Software Escalation.

## WORKING NAMES

- Agent Context Runtime;
- Agent Capsule Architecture;
- Processor–Executioner Loop;
- Xyool Agent Runtime.

No canonical name chosen yet.

## USER INTERACTION / INTERRUPTIBILITY

The Processor–Executioner loop must remain user-interactive while execution is in flight.

Core principle:

> **Autonomy must not remove conversational control.**

The user should be able to:
- ask what is happening;
- inspect current job state;
- add context or constraints;
- redirect the objective;
- pause or cancel pending work;
- approve/reject suggested follow-up jobs;
- request a partial result;
- reprioritize competing jobs;
- continue normal conversation without waiting for the Executioner to finish unrelated work.

Candidate interaction model:

~~~text
USER
↕
CHATGPT / PROCESSOR
↕
XYOOL CORE
↕
ACTIVE JOB STATE
↕
EXECUTIONER
~~~

The Processor remains the user's live interface even while an Executioner is active.

User input during execution becomes a new event, for example:

~~~text
USER_UPDATE
USER_REDIRECT
USER_PAUSE
USER_CANCEL
USER_APPROVAL
USER_PRIORITY_CHANGE
USER_CONTEXT_APPEND
~~~

Core then determines whether the input:
- updates the active Job Capsule;
- queues a follow-up;
- invalidates/restarts work;
- pauses/cancels execution;
- changes resource allocation;
- requires no execution change.

Do not silently mutate an in-flight job when doing so would compromise reproducibility. Material changes should create a new job version/epoch or explicit supersession record.

## INTERACTION PRIORITY

Explicit user direction outranks autonomous continuation unless:
- the requested action is outside authority/safety bounds;
- a transaction already crossed an irreversible external boundary that cannot be undone.

The Executioner should surface state through compact receipts/checkpoints so the Processor can answer user questions without loading the entire execution trace.

## EXPERIENCE TARGET

The desired experience is:

~~~text
USER talks normally
→ Processor responds normally
→ execution may continue through bounded jobs
→ user can interrupt or redirect at any point
→ Core reconciles the new instruction
→ Processor stays conversational
~~~

The system should feel like one continuous collaboration, not a batch job queue that takes control away from the user.
