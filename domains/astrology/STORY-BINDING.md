# Astrology — Relational Story Binding

BINDING ID: ASTROLOGY-RELATIONAL-STORY-V1
STATUS: **CANDIDATE / FUNCTIONS_PARTIAL**
DOMAIN: astrology
CORE FLOW: ../../floware/core/relational-story.flow.md
ESTABLISHMENT: ESTABLISHMENT.md

## Purpose

Reuse Xyool's canonical Story Reader → Story Writer architecture for Astrology while keeping all astrological transition rules, timing semantics, source authority, and predictive boundaries domain-local.

Core principle:

> **Astrology does not need a separate story engine. It needs an Astrology grammar for the existing story engine.**

## Root

Default root:
- SUBJECT / NATIVE; or
- EVENT / INSTITUTION / OTHER DECLARED ASTROLOGY SUBJECT for event or mundane work.

The root is the object whose past-to-present state and possible future branches are being read/written.

## Characters and non-character state

Characters may include actual domain-relevant people, relationships, institutions, groups, or other agents when they materially participate in the subject's story.

By default, planets, aspects, transits, dashas, progressions, returns, ingresses, and similar astrological configurations are **not forced into Character semantics**.

They are usually represented as:
- calculated domain state;
- timer / rhythm state;
- transition trigger;
- rule basis;
- conditional constraint.

A domain system may explicitly model a symbolic object as a character only when that representation is useful and does not distort its native meaning.

## Story Reader binding — past → present

The Reader reconstructs the subject's evidence-backed history up to an explicit as-of cutoff.

Inputs may include:
- verified/reported birth or event data;
- selected astrology system/configuration;
- established versioned rules for that system;
- historically calculated timing/configuration states;
- dated real-world events;
- subjective reports explicitly labeled;
- relationship/context state where material;
- prior story memory.

Reader job:

~~~text
PAST REAL-WORLD HISTORY
+ PAST ASTROLOGY STATE UNDER FROZEN RULES
→ order events
→ identify observed state transitions
→ identify which astrology rules would have been active without using later outcome knowledge
→ preserve matches, misses, contradictions, and unknowns
→ CURRENT SUBJECT STORY / STATE
~~~

The Reader may describe correspondence or rule-consistent association.

It must not convert chronology or symbolic correspondence into causal proof.

### History / rule-learning boundary

Historical outcomes may be used for:
- descriptive reconstruction;
- rule discovery in an explicitly labeled discovery cohort;
- failure analysis;
- boundary refinement.

A rule discovered/tuned from a historical case cannot use that same case as fresh confirmation.

## Story Writer binding — present → conditional future

The Writer starts from the Reader's current state.

Inputs:
- Story Reader current state;
- current subject/context state;
- future calculated astrology states/timers;
- established domain transition/timing rules;
- current relationships/constraints;
- unresolved conflicts;
- rule dependencies/contradictions.

Writer job:

~~~text
CURRENT SUBJECT STORY
+ FUTURE ASTROLOGY TIMERS / CONFIGURATIONS
+ ESTABLISHED ASTROLOGY TRANSITION RULES
→ CONDITIONAL FUTURE BRANCHES
→ branch triggers
→ timing windows
→ expected life-area/capability capture
→ observable proof
→ invalidation / counter-story
~~~

The Writer does not itself establish a predictive claim as valid.

Predictive Astrology converts eligible frozen Writer branches into prospective forecast records and routes them to validation.

## Domain transition rules

Every Writer transition must point to a rule that is established for the selected function/scope.

Examples of possible rule families, only when actually established:
- transit activation;
- applying/exact/separating timing;
- return-cycle transitions;
- profection/time-lord transitions;
- dasha/period transitions;
- progression/solar-arc timing;
- ingress/station/eclipsing windows;
- capture/life-area mapping;
- capability translation.

Missing rule family = Domain Establishment gap.

## Relationship semantics

Use actual subject relationships when relevant:
- partner;
- family;
- employer / institution;
- collaborator;
- authority;
- community;
- other domain-relevant actors.

Astrological configuration is usually evidence/state about a proposed transition, not a relationship edge between real-world characters.

## Source authority

For calculated state:
- ephemeris/calculation authority under TIME-STANDARDS.md.

For domain rules:
- source/tradition provenance under RULE-REGISTRY.md and SOURCE-REGISTRY.md.

For observed history/outcomes:
- VALIDATION.md evidence hierarchy.

## Materiality

A historical event or future branch is material when it changes the claimed subject state, relationship, capability, life-area outcome, or validation result enough to affect the current story/forecast objective.

Do not fill the story with every astrological contact or every life event.

## Story Writer authority

Current authority:
**EXPERIMENTAL / CONDITIONAL BRANCH GENERATION ONLY**

Writer output may use:
- could;
- may;
- conditional on;
- branch;
- timing hypothesis.

It may not use deterministic destiny language or calibrated probabilities without evidence.

## Predictive gate

Story Writer may generate Astrology predictive branches only when the selected predictive function/scope is READY_FOR_CONFIGURATION in ESTABLISHMENT.md.

If ASTRO-FN-PREDICTIVE is PARTIAL:
- Reader work may proceed only for otherwise-established historical/interpretive scope;
- predictive Writer branching is blocked for that incomplete scope;
- return to Core Domain Establishment.

## Resource horizon

Use the smallest historical depth and future horizon justified by the requested astrology job.

Preserve older/out-of-horizon pointers rather than treating them as nonexistent.

## Memory

Preserve:
- root/subject identity;
- system/configuration version;
- rule versions;
- historical event/outcome pointers;
- Reader cutoff/current-state version;
- Writer branch version;
- realized/rejected branch outcomes;
- unresolved gaps.

## Audit specializations

Check:
- hindsight leakage;
- silent rule/system changes;
- event-selection bias;
- broad-window overcoverage;
- flexible capture/life-area reinterpretation;
- false causal language;
- missed counter-story;
- branch divergence;
- rule version drift.

## Output

~~~text
ROOT:
SYSTEM / CONFIGURATION:
RULESET / VERSION:
AS-OF:
READER CURRENT STORY:
ACTIVE ASTROLOGY STATE / TIMERS:
FUTURE BRANCHES:
COUNTER-STORY BRANCHES:
OBSERVABLE PROOFS:
INVALIDATIONS:
PREDICTIVE-ELIGIBLE BRANCHES:
ESTABLISHMENT STATUS:
VALIDATION STATUS:
~~~
