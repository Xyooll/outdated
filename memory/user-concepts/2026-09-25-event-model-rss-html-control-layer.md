# Event Model + RSS Adapters + HTML Control Layer

DATE: 2026-09-25
STATUS: **ACTIVE / FUTURE AUTONOMY + SOFTWARE ARCHITECTURE CONCEPT**

## USER IDEA

HTML may be useful later for events and RSS, but the architecture should avoid making HTML or RSS the system itself.

## CORE PRINCIPLE

> **Events are the data model. RSS is one event source. HTML is the visualization/control layer.**

## EVENT-FIRST ARCHITECTURE

~~~text
RSS / ATOM / APIs / FILINGS / WEBHOOKS / EMAIL / TIMERS / USER INPUT / AGENT EVENTS
→ SOURCE-SPECIFIC ADAPTERS
→ NORMALIZED EVENT OBJECTS
→ EVENT QUEUE / STORE
→ XYOOL CORE
→ OBSERVATION / TRIGGER
→ DOMAIN / FLOW ROUTING
→ RESEARCH / EXECUTION / LEARNING
~~~

RSS should therefore be implemented as one adapter, not as the canonical system.

## NORMALIZED EVENT OBJECT

Candidate common envelope:

~~~yaml
event_id:
event_type:
source_type:
source_id:
published_at:
observed_at:
title:
canonical_url:
content_pointer:
domain_candidates:
priority:
dedupe_key:
provenance:
status:
~~~

Source-specific fields may extend the envelope.

Examples:
- RSS item → source_type: rss;
- SEC filing → source_type: edgar;
- agent completion → source_type: xyool_agent;
- timer → source_type: scheduler;
- user redirect → source_type: user.

## HTML ROLE

HTML/CSS/JavaScript should be a human-facing presentation and control surface over Xyool state, not a reasoning authority.

Potential views:
- event feed;
- source quality;
- domain routing;
- queued / ignored / researching / completed status;
- current job state;
- failures;
- provenance;
- event history;
- unread / processed state;
- priority;
- links to source and Git artifacts.

Potential event detail panel:

~~~text
SOURCE
RAW EVENT
NORMALIZED EVENT
WHY IT MATTERS
FLOW ROUTE
CURRENT JOB
EXECUTION RECEIPT
GIT POINTERS
~~~

## HUMAN-IN-THE-LOOP CONTROLS

A future HTML dashboard may expose controls such as:

~~~text
IGNORE
RESEARCH
PRIORITIZE
PAUSE
OPEN SOURCE
SEND TO DOMAIN
ASK PROCESSOR
~~~

These controls should emit explicit user events into Core rather than directly bypassing Floware.

## EARLY IMPLEMENTATION SHAPE

Prefer a lightweight progression.

Early:

~~~text
RSS / SOURCE
→ PARSER / ADAPTER
→ JSON EVENT
→ GIT OR LOCAL STATE
→ XYOOL CORE
→ SIMPLE HTML VIEWER
~~~

Later, if justified by scale/concurrency:

~~~text
RSS / APIs / WEBHOOKS
→ EVENT ADAPTERS
→ SQLITE / POSTGRES / EVENT QUEUE
→ XYOOL CORE
→ WEB UI
~~~

Do not introduce a database or large frontend framework until the current storage/UI layer hits a demonstrated limit.

## PROCESSOR–EXECUTIONER INTEGRATION

Events become wake signals for the future Processor–Executioner runtime:

~~~text
EVENT
→ OBSERVATION / TRIGGER
→ PROCESSOR / CORE RELEVANCE DECISION
→ JOB CAPSULE
→ EXECUTIONER
→ GIT / STATE
→ JOB_COMPLETE EVENT
→ PROCESSOR
~~~

This keeps external source events and internal execution events on one shared event abstraction.

## BOUNDARY

HTML may present Xyool and emit user-control events, but it must not become the source of truth for reasoning, authority, or memory.

Canonical durable state remains in Floware/Git/domain state until a later storage migration is justified.

## BUILD STATUS

CONCEPT ONLY / DO NOT IMPLEMENT YET.

Before build:
- define canonical Event Contract;
- define adapter boundary;
- define deduplication/idempotency semantics;
- define event lifecycle/status vocabulary;
- define queue/store requirements;
- define UI control-to-event mapping;
- prove the need through autonomous source intake;
- route implementation through Software Escalation.