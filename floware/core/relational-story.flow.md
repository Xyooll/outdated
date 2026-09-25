# FLOW — Relational Story

FLOW ID: `CORE-RELATIONAL-STORY`  
STATUS: **ACTIVE / CANONICAL**  
DOMAIN: core  
JOB: orchestrate bounded evidence-backed relational stories by combining reusable Character profiles, past-to-present Story Reading, conditional future Story Writing, relationship memory, re-rooting, and audit

## GOAL

Provide a domain-agnostic way to understand complex systems as stories made of:

- a selected main character / root;
- reusable character profiles with quantitative and qualitative traits;
- optional non-exclusive archetypes and transformation states;
- other material characters;
- first-class relationships between them;
- each character's own local web;
- evidence/source authority;
- durable memory;
- re-rooting;
- Story Reader reconstruction of past → present;
- Story Writer construction of present → possible futures;
- change and miss audits.

Core law:

> **A story is a root-relative view over a reusable network of characters, relationships, evidence, and state.**

> **Read what evidence says has happened before writing what could happen next.**

This Flow is domain-agnostic.

Domain-specific Flows supply:
- what counts as a character;
- what relationships matter;
- source hierarchy;
- materiality;
- propagation rules;
- degree/resource budget;
- completion/closure conditions;
- domain-specific outputs.

## 1. CORE OBJECTS

### 1.1 Root / Main Character

The selected object whose story is currently being reconstructed.

A root may be:
- a company;
- person;
- project;
- product;
- process;
- institution;
- system;
- event;
- program;
- asset;
- or any other domain-defined entity capable of participating in meaningful relationships.

The root is a **viewpoint**, not a permanent identity class.

### 1.2 Character

A material entity/node that can:
- hold state;
- participate in relationships;
- change;
- cause or constrain other states;
- introduce additional material characters.

A character can be nested in one story and become the root of another.

Canonical character profiling is delegated to:
`character-system.flow.md`

The Relational Story Flow must not reduce characters to node names. Where material, preserve traits, behavior, archetype hypotheses, contradictions, resources, constraints, agency, and transformation state.

### 1.3 Relationship Edge

A material connection between two characters.

Required edge state:

```text
FROM:
TO:
RELATIONSHIP TYPE:
DIRECTION:
PRIOR STATE:
CURRENT STATE:
DELTA:
  NEW / SAME / STRENGTHENED / WEAKENED /
  CHANGED_TYPE / SUSPENDED / ENDED
MATERIALITY:
PROPAGATION:
EVIDENCE / PROVENANCE:
FRESH THROUGH:
```

The relationship itself must be sourced and refreshed.

### 1.4 Local Web

Every expanded material character becomes a temporary local root.

Its local web contains the domain-relevant relationships surrounding it.

Generic form:

```text
LOCAL ROOT
├─ owned / contained entities
├─ counterparties
├─ customers / users / beneficiaries
├─ suppliers / dependencies
├─ partners / collaborators
├─ regulators / authorities
├─ financiers / resource providers
├─ managers / decision makers
├─ programs / processes
├─ competitors / alternatives
└─ other material characters
```

Domains rename or specialize these branches.

## 2. WRAPPERS AND POINTERS

Do not duplicate whole stories everywhere.

Use root-relative **story wrappers** pointing to reusable state.

Conceptually:

```text
STORY WRAPPER
→ CHARACTER POINTER
   → CANONICAL CHARACTER MEMORY
      → RELATIONSHIP POINTERS
      → EVIDENCE / SOURCE POINTERS
      → LOCAL-WEB POINTERS
      → OTHER CHARACTER POINTERS
```

A wrapper answers:

> **What does this reusable character/relationship mean from the current root's perspective?**

A pointer answers:

> **Where is the reusable underlying state?**

The implementation may use IDs, paths, database keys, references, or another deterministic addressing mechanism.

## 3. CANONICAL CHARACTER MEMORY

Character identity and reusable state are independent of the story that discovered them.

Canonical Character Memory may preserve:

```text
CHARACTER ID
IDENTITY / ALIASES
CHARACTER TYPE
SOURCE CURSORS
RELATIONSHIP EDGES
LOCAL WEB HEAD
EVIDENCE POINTERS
STORY POINTERS
CURRENT STATE
QUANTITATIVE TRAITS
QUALITATIVE TRAITS
BEHAVIOR SIGNATURE
RESOURCES / CONSTRAINTS / AGENCY
ARCHETYPE HYPOTHESES
TRANSFORMATION STATE
UNRESOLVED QUESTIONS
SOURCE GAPS
```

Core law:

> **A character's role in a story is not the character's identity.**

Example:

```text
STORY A:
Character X = subsidiary

STORY B:
Character X = supplier

STORY C:
Character X = main character
```

All three views point to the same canonical character where identity resolution permits.

## 4. ROOT-RELATIVE STORY MEMORY

Story Memory preserves one causal view over the character network.

Recommended fields:

```text
STORY ID
ROOT CHARACTER
AS OF
SOURCE AUTHORITY
CLOSURE STATUS
RESOURCE HORIZON

STORY READER HEAD
COMPRESSED STORY
THESIS / CURRENT EXPLANATION
PRIMARY CONFLICT
PRIMARY BOTTLENECK
LIKELY NEXT STATE
CONDITIONAL WINDOW / RHYTHM
INVALIDATION / FAILURE PATH

STORY WRITER HEAD
FUTURE BRANCHES[]
COUNTER-STORY BRANCHES[]
NEXT OBSERVABLE PROOFS[]

CHARACTER POINTERS[]
RELATIONSHIP GRAPH[]
LOCAL WEB HEADS[]
NEW CHARACTERS[]
RELATIONSHIP DELTAS[]
ENDED / SUSPENDED EDGES[]
SOURCE GAPS[]
BOUNDARY POINTERS[]
NEXT REFRESH TARGETS[]
```

The story is **root-relative**.

The characters and their underlying evidence are reusable.

## 5. RE-ROOTING

Any reusable character may become the new main character.

Process:

```text
SELECT CHARACTER
→ LOAD CANONICAL CHARACTER MEMORY
→ SET AS NEW ROOT / DEGREE 0
→ APPLY DOMAIN RESOURCE BUDGET
→ RECALCULATE DEGREES RELATIVE TO NEW ROOT
→ REUSE KNOWN EVIDENCE / EDGES / LOCAL WEB
→ REFRESH STALE OR DUE STATE
→ EXPAND NEWLY IN-SCOPE BRANCHES
→ BUILD NEW ROOT STORY
```

Do not rebuild known character state from zero.

Do not preserve old degree numbers as permanent properties.

Degrees belong to the **current root view**.

## 6. RESOURCE HORIZON

Recursive story graphs can expand without a natural practical endpoint.

Therefore every domain must declare a current exploration/resource policy.

Generic form:

```text
MAX_DEGREE:
POLICY_REASON:
MATERIALITY_STOP:
BOUNDARY_BEHAVIOR:
```

The degree limit is not an epistemic statement about reality.

It is an operational research bound.

Core law:

> **A boundary means "not expanded under the current resource budget," not "nothing exists beyond here."**

Preserve:
- beyond-boundary pointers;
- unresolved branches;
- why expansion stopped;
- enough provenance to resume later.

A future system may use:
- a larger fixed depth;
- adaptive depth;
- information-value-based expansion;
- continuous/real-time graph maintenance.

## 7. EVIDENCE AND SOURCING

A story cannot be stronger than its supporting evidence.

For every material:
- character state;
- relationship edge;
- transition;
- claimed cause;
- timing/rhythm;
- propagation path;

identify the best available evidence under the active domain's source hierarchy.

Generic source questions:

```text
WHAT EXACTLY IS THE CLAIM?
WHO / WHAT HAS AUTHORITY OVER IT?
WHAT SOURCE CREATED OR RECORDED THE STATE?
IS THE SOURCE CURRENT?
CAN THE OTHER SIDE OF THE RELATIONSHIP CORROBORATE IT?
DOES STRONGER EVIDENCE CONTRADICT IT?
```

Preserve provenance.

Do not promote inference into fact merely because it appears inside a primary source.

## 8. STORY-BUILDING PROCESS

Use three separable capabilities:

```text
CHARACTER SYSTEM
= who/what are the characters really like?

STORY READER
= how did past evidence produce the current state?

STORY WRITER
= what materially distinct future branches can validly follow?
```

Canonical route:

```text
SELECT ROOT
↓
LOAD STORY MEMORY
↓
LOAD / REFRESH CANONICAL CHARACTER PROFILES
↓
DISCOVER / REFRESH MATERIAL RELATIONSHIPS + LOCAL WEBS
↓
PROPAGATE MATERIAL CONSEQUENCES BACK TOWARD ROOT
↓
RUN story-reader.flow.md
    past evidence
    → state/relationship/character transitions
    → current causal story
↓
FORM CURRENT THESIS / EXPLANATION
↓
IF THE DOMAIN AUTHORIZES FUTURE BRANCHING:
    RUN story-writer.flow.md
    current state
    + character traits/archetypes
    + relationships
    + active processes/timers
    → conditional future branches
    → observable proof / invalidation
↓
AUDIT FOR MISSES / STATE CHANGES / ARCHETYPE ERROR / BRANCH ERROR
↓
WRITE UPDATED STORY + CHARACTER MEMORY
```

A domain may use Reader without Writer.

The Writer is not allowed to turn a biography into a deterministic forecast.

## 9. PROPAGATION

A nested state matters to the root only if there is a defensible path back.

Generic form:

```text
NESTED CHARACTER STATE
→ RELATIONSHIP EDGE
→ INTERMEDIATE STATE
→ ...
→ ROOT-RELEVANT CONSEQUENCE
```

The active domain defines what counts as a root-relevant consequence.

Do not skip intermediate transmission steps merely because two characters are related.

## 10. RELATIONSHIP CONTINUITY

At each refresh compare stored relationships with current evidence.

Allowed deltas:

```text
NEW
SAME
STRENGTHENED
WEAKENED
CHANGED_TYPE
SUSPENDED
ENDED
```

A relationship change can alter the story even when no character is new.

If an edge ends:
- retain it historically;
- remove or downgrade it from the active story as appropriate;
- reconsider descendants whose relevance depended on that edge.

## 11. NEW-CHARACTER ENTRANCE

At every root and local web ask:

```text
DID A NEW MATERIAL CHARACTER ENTER?
WHICH EDGE INTRODUCED IT?
WHAT IS ITS CURRENT STATE?
WHAT DEGREE IS IT FROM THE CURRENT ROOT?
DOES IT CHANGE THE STORY?
DOES IT HAVE ITS OWN MATERIAL LOCAL WEB?
```

New-character detection applies recursively, not only at the root.

## 12. MEMORY / DELTA REFRESH

Do not rebuild an unchanged graph.

Preferred loop:

```text
LOAD MEMORY
→ IDENTIFY STALE / DUE / CHANGED BRANCHES
→ REFRESH ONLY THOSE BRANCHES
→ COMPARE PRIOR vs CURRENT STATE
→ PROPAGATE MATERIAL DELTAS
→ PRESERVE UNCHANGED BRANCHES
→ WRITE NEW VERSION ONLY WHEN JUSTIFIED
```

Memory should preserve both:
- finished root-relative story;
- reusable underlying character/relationship state.

## 13. AUDIT / MISS SYSTEM

Minimum generic miss classes:

```text
RETRIEVAL MISS
SOURCE MISS
CHARACTER MISS
CHARACTER-TRAIT MISS
ARCHETYPE / CHARACTER-FORM MISS
RELATIONSHIP MISS
STATE-CHANGE MISS
MAPPING MISS
CAUSAL / PROPAGATION MISS
RECURSION MISS
MEMORY MISS
THESIS / STORY-READER MISS
STORY-WRITER BRANCH MISS
OUTCOME MISS
```

Audit questions:

```text
DID A MATERIAL CHARACTER ENTER OR LEAVE?
DID AN EDGE CHANGE?
DID OWNERSHIP / CONTROL / DEPENDENCE CHANGE?
DID A MATERIAL CHILD WEB CHANGE?
DID A BETTER SOURCE APPEAR?
DID CURRENT EVIDENCE SUPERSEDE STORED STATE?
DID A TIMER / RHYTHM CHANGE?
DID A BOUNDARY BRANCH BECOME MATERIAL?
DID THE STORY FAIL TO PROPAGATE A NESTED CHANGE?
DID MEMORY LOSE REUSABLE STATE?
DID A CHARACTER'S QUALITATIVE FORM CHANGE?
DID AN ARCHETYPE LABEL OVERRIDE CONTRADICTING EVIDENCE?
DID THE WRITER OMIT A MATERIAL COUNTER-STORY?
DID REALITY FOLLOW A BRANCH WE FAILED TO WRITE?
```

## 14. CLOSURE

A story can close under the current policy when:
- all in-scope material characters are expanded, closed, or explicitly blocked;
- material relationship states are current enough for the decision;
- unresolved source gaps are named;
- boundary branches are preserved;
- no required propagation path is silently missing;
- the story/thesis does not rely on unsupported positive assumptions.

Possible status:

```text
STORY_CLOSED
STORY_PARTIAL — MATERIAL GAPS NAMED
STORY_BLOCKED — REQUIRED EVIDENCE MISSING
STORY_STALE — MATERIAL STATE MAY HAVE CHANGED
```

Closure is relative to:
- current evidence;
- current domain policy;
- current resource horizon;
- current decision need.

It is not a claim of complete knowledge.

## 15. DOMAIN CONFIGURATION BINDING

A domain using this Flow must provide an explicit Relational Story binding through `../meta/domain-configurer.flow.md` and `../meta/mapping.flow.md`.

The domain configuration should define:

```text
CHARACTER TYPES:
CHARACTER PROFILE / TRAIT POLICY:
ARCHETYPE POLICY / REGISTRY OR NONE:
STORY READER AUTHORITY:
STORY WRITER AUTHORITY / BRANCH LIMITS:
RELATIONSHIP TYPES:
SOURCE HIERARCHY:
MATERIALITY TEST:
PROPAGATION TARGET:
RESOURCE HORIZON:
STOP RULES:
MEMORY BACKEND:
AUDIT SPECIALIZATIONS:
FINAL STORY OUTPUT:
```

Example domains may specialize the same architecture differently:

```text
STOCKS
root = company/security
propagation target = economics / shareholder capture / price

PROJECT MANAGEMENT
root = project
propagation target = delivery / risk / dependency state

RESEARCH
root = hypothesis / research object
propagation target = evidence / confidence / unresolved questions

SOFTWARE / SYSTEMS
root = system/service
propagation target = behavior / dependency / failure path

ORGANIZATIONS
root = team / institution
propagation target = decisions / resources / outcomes
```

These are structural examples, not claims that all domains share identical semantics.

Specific native adapters may sit below the domain configuration for calculations, APIs, formats, or system-specific normalization. They do not replace the domain-level configuration contract.

Material domain-to-story bindings should be independently checkable through `../meta/audit.flow.md`.

## 16. RELATION TO OTHER CORE FLOWS

Use with:

- `character-system.flow.md` for reusable character traits, archetypes, behavior and transformation state;
- `story-reader.flow.md` for evidence-backed past → present reconstruction;
- `story-writer.flow.md` for conditional present → possible-future branches;
- `research.flow.md` for evidence acquisition;
- `evidence-to-state.flow.md` for state conversion;
- `direct-resolution.flow.md` to avoid unnecessary expansion;
- `question-frontier.flow.md` when the current story question is weak;
- `correspondence.flow.md` when transferring structure across domains;
- `learning.flow.md` when outcomes expose a miss or architecture improvement;
- `../meta/mapping.flow.md` for domain-to-story representation mapping;
- `../meta/domain-configurer.flow.md` for domain-level binding/configuration;
- `../meta/audit.flow.md` for independent story/mapping/configuration integrity checks.

## 17. SOFTWARE / HARD-LIMIT BOUNDARY

Floware owns:
- story construction;
- materiality;
- re-rooting logic;
- propagation interpretation;
- closure;
- miss classification.

Software is justified for:
- stable IDs;
- pointers;
- persistence;
- indexing;
- graph storage;
- provenance;
- source cursors;
- versioning;
- deterministic degree calculation;
- atomic writes;
- high-scale refresh scheduling.

## CORE STATEMENTS

> **A story is a view over a network, not a replacement for the network.**

> **Every material character can become a root.**

> **A role is not an identity, and an archetype is not a box.**

> **Read the current story before writing future branches.**

> **Remember the character once; reuse it across many stories.**

> **Remember the relationship, not only the names at either end.**

> **Bound exploration because resources are finite, while preserving the path for future expansion.**
