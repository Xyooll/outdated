# FLOW — Character System

FLOW ID: CORE-CHARACTER-SYSTEM
STATUS: **ACTIVE / CANONICAL**
DOMAIN: core
JOB: build reusable evidence-backed character profiles without forcing characters into inappropriate categories
AUTHORITY: descriptive / interpretive character modeling only; no domain action authority
PARENT GOALPOST: supplied by the calling Flow
UPSTREAM FLOWS: research, evidence-to-state, relational-story, domain configuration
DOWNSTREAM FLOWS: story-reader, story-writer, relational-story, domain flows, learning, meta audit
SOFTWARE DEPENDENCIES: none by default; persistence/schema validation may be deterministic

## GOAL

Represent a material character as more than an identity node.

The Character System preserves:
- what the character is;
- what roles it plays in different stories;
- quantitative traits;
- qualitative traits;
- behavior patterns;
- resources and constraints;
- agency / dependence;
- candidate archetypes;
- transformation history;
- possible next forms;
- contradictions and unknowns.

Core law:

> **Describe the character from evidence first. Archetypes must fit the character; the character must never be forced to fit an archetype.**

## GOALPOST

A character profile is sufficient when:
- identity is resolved as far as the domain requires;
- contextual role is separated from identity;
- material quantitative and qualitative traits are represented;
- archetype hypotheses are evidence-backed and non-exclusive;
- contradictions are preserved;
- current transformation state and meaningful alternatives are explicit when relevant;
- unknowns remain visible;
- the profile can be reused from another root/story.

## INPUT STATE

- canonical character identity or unresolved identity candidate;
- domain configuration;
- current and historical evidence;
- relationship edges;
- current state;
- behavior/state-transition history;
- quantitative observations when available;
- source authority and freshness;
- current story role(s), if any.

## EVIDENCE

Use the active domain source hierarchy.

Every material qualitative trait or archetype hypothesis should identify:
- supporting observations/evidence;
- contradictions;
- freshness;
- confidence or status.

Do not turn an impression into a permanent character trait without evidence.

## CORE DISTINCTIONS

### Character type

What kind of entity is this?

Examples:
- person;
- company;
- regulator;
- process;
- product;
- institution;
- system.

Character type is ontological.

### Story role

What is this character doing relative to the current root?

Examples:
- customer;
- gatekeeper;
- financier;
- subsidiary;
- adversary;
- beneficiary;
- enabler.

Role is root-relative and can change across stories.

### Trait

What property does the character currently exhibit?

Traits may be quantitative or qualitative.

### Archetype

What recurring structural / behavioral pattern does the character resemble?

Archetype is a hypothesis about pattern, not identity and not a mandatory category.

### Character condition

How well is the current form functioning right now?

Condition is not the archetype.

### Trajectory

How is the character's condition changing through time?

Trajectory is not Quality and is not action authority.

## CHARACTER PROFILE

Minimum reusable form:

~~~text
CHARACTER ID:
IDENTITY / ALIASES:
CHARACTER TYPE:
AS OF:

STORY ROLES[]:
CURRENT STATE:

QUANTITATIVE TRAITS[]:
  trait
  value / range
  unit
  as_of
  evidence

QUALITATIVE TRAITS[]:
  trait
  state / description
  evidence basis
  confidence
  contradictions

BEHAVIOR SIGNATURE:
RESOURCES / CAPABILITIES:
CONSTRAINTS / DEPENDENCIES:
AGENCY:
RELATIONSHIP STYLE:
MATURITY / DEVELOPMENT STATE:
CHARACTER CONDITION:
  EMERGING / PROGRESSING / FUNCTIONING / STALLED /
  REMEDIATING / DEGRADING / TRANSFORMING / UNKNOWN
TRAJECTORY:
  IMPROVING / STABLE / MIXED / DETERIORATING / UNKNOWN

ARCHETYPE HYPOTHESES[]:
  archetype
  status
  supporting traits / evidence
  contradictions
  confidence
  domain registry / definition

TRANSFORMATION STATE:
  current form
  prior forms
  candidate next forms
  failure / degradation forms
  transition evidence

UNKNOWN / UNCLASSIFIED FEATURES:
SOURCE GAPS:
~~~

## QUANTITATIVE VS QUALITATIVE TRAITS

Keep both.

Quantitative traits are measurable:
- size;
- revenue;
- time;
- frequency;
- concentration;
- volatility;
- ownership;
- capacity;
- counts.

Qualitative traits describe evidence-backed structure:
- dependence;
- control;
- maturity;
- relationship style;
- conversion style;
- behavioral consistency;
- agency;
- centralization;
- optionality;
- fragility;
- adaptability.

Do not assign fake numbers merely to make qualitative traits sortable.

If a qualitative trait later earns a validated measurement, preserve the original qualitative observation and add the measurement rather than rewriting history.

## ARCHETYPE RULES

Archetypes describe **form**, not quality.

A valid archetype can exist in:
- a healthy character;
- a stalled character;
- a deteriorating character;
- a Quality-blocked character.

Do not use archetype membership as a proxy for attractiveness, maturity, or capital eligibility.

Archetypes must be:

1. **NON-EXCLUSIVE**
   - one character may express several archetypes at once.

2. **EVIDENCE-BACKED**
   - list evidence and contradictions.

3. **DYNAMIC**
   - archetypes may strengthen, weaken, transform, or be rejected as state changes.

4. **DOMAIN-LOCAL BY DEFAULT**
   - a stock archetype is not automatically a universal archetype.

5. **OPEN-WORLD**
   - UNCLASSIFIED, HYBRID, and EMERGENT are valid states.
   - new archetypes may be proposed when evidence repeatedly fails to fit existing definitions.

6. **NON-AUTHORITATIVE**
   - archetype membership does not by itself authorize a decision.

7. **ANTI-FUNNEL**
   - do not discard material evidence because it conflicts with the nearest archetype.

8. **COMPOSITION BEFORE PROLIFERATION**
   - prefer multiple existing archetypes plus raw traits over inventing a new catch-all label.
   - promote a new archetype only when a recurring structural pattern appears across materially different characters and changes downstream reasoning.

Allowed archetype status:

~~~text
CANDIDATE
PROVISIONAL
SUPPORTED_FOR_SCOPE
WEAKENED
REJECTED
SUPERSEDED
UNCLASSIFIED
EMERGENT
~~~

## BEHAVIOR SIGNATURE

Where the domain supports it, summarize recurring behavior:

~~~text
WHAT DOES THIS CHARACTER REPEATEDLY DO?
WHAT DOES IT AVOID?
HOW DOES IT RESPOND TO CONSTRAINT?
HOW DOES IT ACQUIRE / DISTRIBUTE RESOURCES?
DOES IT CONVERT OPTIONALITY INTO REALIZED OUTCOMES?
HOW STABLE IS THE PATTERN?
WHAT EVIDENCE CONTRADICTS THE PATTERN?
~~~

Do not anthropomorphize non-human characters. For systems/institutions, behavior means observed process/state tendency.

## TRANSFORMATION

Characters can change archetype/state.

Generic form:

~~~text
CURRENT FORM
→ transition evidence
→ CANDIDATE NEXT FORM

or

CURRENT FORM
→ failed transition / constraint
→ DEGRADATION FORM
~~~

A transformation is part of the story and should not be hidden by a static label.

## PROCESS

~~~text
RESOLVE CHARACTER
→ LOAD CANONICAL MEMORY
→ LOAD CURRENT / HISTORICAL EVIDENCE
→ SEPARATE IDENTITY FROM CURRENT STORY ROLE
→ EXTRACT QUANTITATIVE TRAITS
→ EXTRACT QUALITATIVE TRAITS
→ SUMMARIZE BEHAVIOR SIGNATURE
→ IDENTIFY RESOURCES / CONSTRAINTS / AGENCY
→ CLASSIFY CURRENT CONDITION + TRAJECTORY
→ PROPOSE ZERO OR MORE ARCHETYPE HYPOTHESES
→ SEARCH FOR CONTRADICTING EVIDENCE
→ MARK UNCLASSIFIED / EMERGENT FEATURES
→ IDENTIFY CURRENT / POSSIBLE TRANSFORMATIONS
→ WRITE / UPDATE CHARACTER PROFILE
→ ROUTE MATERIAL CHANGES TO STORY READER / WRITER
~~~

## GATES

Before using an archetype downstream:
- definition must be known;
- supporting evidence must exist;
- contradictory evidence must be represented;
- archetype may not replace the raw traits;
- domain/local calibration status must be explicit.

## ADAPTATION

Some domains may not need archetypes.

Some characters may be too sparse, novel, or unstable to classify.

In those cases:
- preserve traits;
- use UNCLASSIFIED / EMERGENT;
- continue reasoning without an archetype.

## BOUNDARIES

This Flow does not:
- force exhaustive taxonomies;
- infer private motives without evidence;
- convert all traits to numbers;
- treat archetype similarity as causal proof;
- erase contradictions;
- make domain decisions solely from character labels.

## FAIL-CLOSED CONDITIONS

Return PROFILE_PARTIAL / UNCLASSIFIED when:
- evidence is too sparse;
- identity is unresolved;
- archetype definitions conflict with evidence;
- qualitative claims cannot be sourced;
- the character changes too quickly for a stable profile.

Do not invent a neat archetype to satisfy the schema.

## OUTPUT STATE

~~~text
CHARACTER PROFILE STATUS:
CHARACTER ID:
TYPE:
ROLES:
QUANTITATIVE TRAITS:
QUALITATIVE TRAITS:
BEHAVIOR SIGNATURE:
RESOURCES:
CONSTRAINTS:
AGENCY:
ARCHETYPE HYPOTHESES:
CHARACTER CONDITION:
TRAJECTORY:
TRANSFORMATION STATE:
CONTRADICTIONS:
UNCLASSIFIED FEATURES:
NEXT EVIDENCE:
~~~

## LEARNING HOOK

When later behavior/outcomes diverge from the expected character pattern, ask:
- was the archetype wrong?
- was a qualitative trait wrong?
- did the character transform?
- did the relationship context change?
- was evidence missing?

Preserve failed archetype hypotheses; do not rewrite them away.

## SOFTWARE / HARD-LIMIT BOUNDARY

NONE — FLOWARE SUFFICIENT

Software may support persistence, schema validation, stable IDs, provenance links, and large-scale trait indexing.
