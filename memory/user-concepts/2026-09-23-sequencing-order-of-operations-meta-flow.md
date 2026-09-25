# User Concept — Sequencing / Order-of-Operations Meta Flow

Date: 2026-09-23
Status: **ACTIVE / CORE FLOWARE ARCHITECTURE**

## USER-STATED

Xyool may need something that controls the order of operations.

## ASSISTANT INTERPRETATION

This should be a distinct Meta Flow responsible for logical operational precedence.

It should answer:

> **What is ready now, what must wait, what can run in parallel, and what must be revisited when new evidence invalidates earlier work?**

The operation model should be a dependency-aware partial order, not automatically one rigid list.

Core distinctions:

~~~text
XYOOL EXECUTION
= what work / Flows should run?

SEQUENCING
= what order is dependency-safe and what is READY now?

PATCHING
= what dependent surfaces must change together?

AUDIT
= did the result preserve the governing contracts?
~~~

Sequencing should preserve:
- prerequisites;
- domain gates;
- barriers;
- shared-state mutexes;
- safe parallelism;
- fail-closed states;
- re-entry/versioning when upstream evidence changes.

## SYSTEM CONSEQUENCE

Canonical Meta Flow:
- `floware/meta/sequencing.flow.md`

Core laws:

> **Order follows dependency, not convenience.**

> **Do not serialize independent work, and do not parallelize dependent work.**

Re-entry rule:

> **Re-entry creates a new version of affected work; it does not erase the path that already ran.**

Sequencing is logical order, not calendar scheduling/timing.

## STOCK-DOMAIN CONSEQUENCE

The stock mandatory run sequence remains domain authority.

Sequencing may parallelize independent evidence/character refresh work, but may not bypass:
- discovery before Quality exclusion;
- Quality before normal TTC capital competition;
- causal gate definition before capital priority;
- story/thesis before strategy expression;
- final freshness/character barriers before narrative closure.

## OPEN QUESTION

At larger scale, deterministic DAG validation, locks, transactions, durable execution epochs, and queues may become justified software support. The ordering semantics remain Floware.
