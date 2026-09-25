# FLOW — Story Writer

FLOW ID: CORE-STORY-WRITER
STATUS: **ACTIVE / CANONICAL**
DOMAIN: core
JOB: construct auditable conditional future story branches from the current state without inventing facts
AUTHORITY: hypothesis generation / scenario construction only; no action authority
PARENT GOALPOST: supplied by Relational Story or calling Flow
UPSTREAM FLOWS: story-reader, character-system, relational-story, domain timing/state flows, novelty-enhancer when creative mode is explicitly enabled
DOWNSTREAM FLOWS: domain thesis/strategy flows, learning, meta audit
SOFTWARE DEPENDENCIES: none by default

## GOAL

Write plausible future stories that could unfold from the current evidence-backed state.

The Writer uses:
- character profiles;
- archetypes and contradictions;
- current character condition and trajectory;
- resources and constraints;
- relationships;
- active processes / timers;
- unresolved conflicts;
- known transition rules;
- domain-local causal mechanics.

It produces branches, not fiction and not a single deterministic narrative.

Core law:

> **The Writer may extend the current state through explicit conditional transitions. It may not invent evidence.**

## GOALPOST

A Story Writer output is sufficient when:
- at least the materially distinct future paths are represented;
- every branch starts from the current Reader state;
- each transition names its prerequisites/triggers;
- involved characters and their expected roles are explicit;
- observable proof and invalidation are defined;
- counter-story / failure paths are included where material;
- no branch is presented as fact;
- numeric probabilities are omitted unless calibrated evidence supports them.

## INPUT STATE

- Story Reader output;
- current character profiles;
- archetype hypotheses and contradictions;
- relationship graph;
- current conflict/bottleneck;
- active timers/processes;
- domain transition rules;
- resource and authority boundaries.

## EVIDENCE

A future branch must be grounded in one or more of:
- current verified state;
- existing relationship/dependency structure;
- domain-valid transition rules;
- active process/timer evidence;
- evidence-backed character traits/archetypes;
- supported correspondence where the target domain has earned it.

Archetype resemblance alone is not evidence for a branch.

Clearly separate:
- observed current facts;
- inferred transition structure;
- conditional future hypotheses.

## BRANCH OBJECT

~~~text
BRANCH ID:
BRANCH LABEL:
STATUS: HYPOTHESIS / ARMED / WEAKENED / CLOSED / REALIZED / REJECTED

START STATE:
DRIVING CHARACTERS:
RELEVANT ARCHETYPES / TRAITS:
CHARACTER CONDITION / TRAJECTORY:
TRIGGER / PREREQUISITES:
TRANSITION SEQUENCE:
KEY RELATIONSHIP CHANGES:
EXPECTED CHARACTER TRANSFORMATIONS:
OBSERVABLE PROOF:
CONDITIONAL WINDOW / RHYTHM:
INVALIDATION:
DOWNSTREAM CONSEQUENCE:
CONFIDENCE: ordered / qualitative unless calibrated
DEPENDENCIES:
SOURCE / RULE BASIS:
~~~

## BRANCH FAMILIES

Do not force these when irrelevant, but consider:

- CONTINUATION — current process continues;
- CONVERSION — unresolved capability converts into realized outcome;
- DELAY / STALL — current path persists without required conversion;
- FAILURE / BREAK — material gate fails or relationship ends;
- TRANSFORMATION — a character changes form/archetype;
- PARALLEL PATH — another existing branch becomes dominant;
- ADVERSARIAL / COUNTER-STORY — evidence-backed path that challenges the preferred thesis;
- EMERGENT — new character/process enters after a defined trigger.

## PROCESS

~~~text
LOAD STORY READER CURRENT STATE
→ LOAD CHARACTER PROFILES
→ IDENTIFY CURRENT CONFLICT / BOTTLENECK
→ LIST ARMED / POSSIBLE TRANSITIONS
→ GENERATE DISTINCT BRANCHES
→ FOR EACH BRANCH:
    identify trigger / prerequisites
    identify characters / traits / archetypes
    trace relationship + state transitions
    identify observable proof
    define invalidation / stop
    define consequence
→ ADD COUNTER-STORY / FAILURE PATHS
→ REMOVE DUPLICATE OR PURELY FICTIONAL BRANCHES
→ ORDER ONLY WHEN EVIDENCE DISCRIMINATES
→ FREEZE WRITER OUTPUT FOR LATER COMPARISON
~~~

## ARCHETYPE USE

Archetypes may shape which branches deserve consideration, but cannot create a transition by themselves.

The same archetype can produce different branches under different conditions.

Example:

```text
SCALE-UP OPERATOR + PROGRESSING / IMPROVING
→ utilization / throughput / mature-operator branch may be armed

SCALE-UP OPERATOR + STALLED / DETERIORATING
→ remediation / stranded-capacity / financing-dominance branches become more material
```

Use form + condition + trajectory together.

Example:

~~~text
SUPPORTED pattern:
capital-dependent platform assembler

may suggest examining:
- acquisition / integration branch;
- financing-dominance branch;
- conversion-to-operator branch.

But each branch still requires domain evidence, actual relationships, and transition prerequisites.
~~~

If archetype and current evidence disagree, evidence wins.

## FUTURE-WRITING DISCIPLINE

Use language such as:
- could;
- may;
- conditional on;
- branch;
- scenario;
- next-state candidate.

Do not convert a coherent branch into certainty.

Do not generate dozens of low-value branches. Prefer materially distinct paths.

## GATES

Before a branch is promoted from HYPOTHESIS to ARMED:
- its prerequisite state exists;
- the transition is valid in the domain;
- observable proof can be named;
- the branch is not supported only by archetype resemblance.

## ADAPTATION

Some domains are generative/creative and may intentionally use a wider Writer.

Other domains, such as finance or science, require evidence-bounded scenario writing.

The Domain Configurer must define the Writer authority appropriate to the domain.

## BOUNDARIES

The Writer does not:
- invent current facts;
- imply branch realization without evidence;
- assign calibrated probability without calibration;
- rewrite the Reader history;
- use archetype labels as destiny;
- hide a counter-story because it is inconvenient.

## FAIL-CLOSED CONDITIONS

Return WRITER_PARTIAL / NO_VALID_BRANCH when:
- current state is unreliable;
- no valid transition rules are known;
- branches require fictional facts;
- archetype evidence is too weak to support the proposed path;
- material dependencies are missing.

## OUTPUT STATE

~~~text
WRITER STATUS:
CURRENT STATE BASIS:
PRIMARY FUTURE BRANCHES[]:
COUNTER-STORY BRANCHES[]:
UNORDERED BRANCHES[]:
NEXT OBSERVABLE PROOFS:
BRANCHES REQUIRING NEW EVIDENCE:
FREEZE / VERSION ID:
~~~

## LEARNING HOOK

When reality advances:
- identify which branch, if any, reality followed;
- identify the first divergence from each active branch;
- distinguish branch miss from timing miss;
- update character traits/archetypes only when evidence warrants;
- preserve branches that failed.

Writer learning is:

~~~text
WRITTEN BRANCH
→ OBSERVED REALITY
→ FIRST DIVERGENCE
→ CHARACTER / RELATIONSHIP / TRANSITION MISS
→ UPDATE
~~~

## SOFTWARE / HARD-LIMIT BOUNDARY

NONE — FLOWARE SUFFICIENT

Software may support branch persistence, versioning, timestamps, and deterministic comparison of frozen branch states.


## CREATIVE NOVELTY MODE

Some domains intentionally write fiction, design worlds, invent metaphors, explore occult/symbolic systems, or otherwise permit creative invention.

When creative authority is explicit:
- `novelty-enhancer.flow.md` may supply structurally novel candidate material;
- `meaning-attribution.flow.md` may supply symbolic/intrinsic/extrinsic meaning objects;
- invented material must remain distinguishable from Reader evidence;
- novelty may expand branch diversity but cannot independently move a branch to ARMED in an evidence-bounded predictive domain.

Creative Writer:

~~~text
READER / SEED STATE
+ MEANING OBJECTS
+ OPTIONAL NOVELTY CANDIDATES
→ CREATIVE BRANCHES
~~~

Evidence-bounded Writer:

~~~text
READER VERIFIED STATE
+ DOMAIN TRANSITION RULES
→ CONDITIONAL BRANCHES

NOVELTY
→ hypotheses/questions only
~~~
