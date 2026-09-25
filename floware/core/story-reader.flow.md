# FLOW — Story Reader

FLOW ID: CORE-STORY-READER
STATUS: **ACTIVE / CANONICAL**
DOMAIN: core
JOB: reconstruct the evidence-backed causal story from past events and relationships into the current state
AUTHORITY: descriptive / explanatory only
PARENT GOALPOST: supplied by Relational Story or calling Flow
UPSTREAM FLOWS: character-system, research, evidence-to-state, relational-story
DOWNSTREAM FLOWS: story-writer, relational-story, domain thesis/output flows, meta audit
SOFTWARE DEPENDENCIES: none by default

## GOAL

Read the story that evidence says has already unfolded.

The Story Reader converts biography-like event history into a causal current-state explanation by distinguishing:
- what happened;
- which characters changed;
- which relationships changed;
- what state transitions occurred;
- what causes are supported;
- what remains unresolved.

Core law:

> **The Reader explains how the current state came to exist. It does not write the future.**

## GOALPOST

The Reader is complete when:
- the current root/state is defined;
- material past transitions are causally ordered;
- character and relationship changes are represented;
- unsupported chronology is not mistaken for causality;
- current conflict/bottleneck is identified;
- unresolved branches and source gaps remain visible.

## INPUT STATE

- root character;
- character profiles;
- relationship graph;
- evidence/history;
- state transitions;
- story memory;
- domain configuration;
- resource horizon.

## EVIDENCE

Use only evidence available up to the reading cutoff/as-of time.

A later outcome may be used only when explicitly performing retrospective evaluation, never to rewrite what was knowable earlier.

## PROCESS

~~~text
SELECT ROOT + AS-OF
→ LOAD PRIOR STORY MEMORY
→ LOAD CHARACTER PROFILES
→ LOAD MATERIAL EVENTS / EDGES / STATE DELTAS
→ ORDER EVENTS TEMPORALLY
→ SEPARATE CHRONOLOGY FROM SUPPORTED CAUSALITY
→ IDENTIFY CHARACTER / RELATIONSHIP TRANSFORMATIONS
→ TRACE CONSEQUENCES TOWARD ROOT
→ IDENTIFY CURRENT CONFLICT / BOTTLENECK
→ IDENTIFY WHAT REMAINS UNRESOLVED
→ COMPRESS INTO CURRENT-STORY EXPLANATION
~~~

## OUTPUT STATE

~~~text
ROOT:
AS OF:
PAST STATE:
MATERIAL TRANSITIONS:
CHARACTER TRANSFORMATIONS:
RELATIONSHIP DELTAS:
SUPPORTED CAUSAL CHAINS:
CURRENT STATE:
CURRENT CONFLICT:
CURRENT BOTTLENECK:
UNRESOLVED QUESTIONS:
SOURCE GAPS:
READER CLOSURE:
~~~

## BIOGRAPHY GUARD

A long sequence of events is not automatically a useful story.

The Reader should compress:
- repeated background events;
- redundant announcements;
- events with no causal path to the current state.

Preserve them in evidence/history, but do not let them dominate the operational story.

## GATES

- as-of time known;
- material evidence has provenance;
- current state does not depend on a future event;
- causal claims distinguish evidence from inference.

## ADAPTATION

For simple domains, the Reader may be very short.

For complex relational domains, it may recurse through local character webs before compression.

## BOUNDARIES

The Reader does not:
- select a preferred future;
- assign future outcomes;
- create fictional events;
- treat archetype as causal proof;
- hide contradictory history.

## FAIL-CLOSED CONDITIONS

Return STORY_READER_PARTIAL / BLOCKED when:
- current state cannot be derived without material missing evidence;
- temporal ordering is corrupted;
- material character/relationship state is stale;
- causal compression would require unsupported assumptions.

## LEARNING HOOK

Reader misses include:
- material past event omitted;
- causal relation falsely inferred;
- character transformation missed;
- stale relationship carried forward;
- biography noise obscured the actual state transition.

## SOFTWARE / HARD-LIMIT BOUNDARY

NONE — FLOWARE SUFFICIENT
