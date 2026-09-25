# FLOW — Character Memory and Re-Rooting

FLOW ID: `STOCK-CHARACTER-MEMORY-REROOT-V1`  
STATUS: **ACTIVE / CANONICAL**  
DOMAIN: stock-market  
JOB: preserve every material entity as its own reusable character memory and allow any character to become the main research root without rebuilding known state
CORE PARENT FLOW: `../../../floware/core/relational-story.flow.md`
CORE CHARACTER FLOW: `../../../floware/core/character-system.flow.md`  

## GOAL

Separate **who a character is** from **the role it currently plays in another character's story**.

Core law:

> **A subsidiary is a character in its own right. Its role as a subsidiary is one relationship state, not its identity.**

A material entity discovered inside one stock story should retain enough durable memory that it can later be selected as the main character and researched from that saved state.

## 1. CANONICAL CHARACTER VS STORY ROLE

Persist one canonical character identity:

```text
CHARACTER_ID
IDENTITY
ALIASES
PUBLIC / PRIVATE STATUS
SECURITY IDS IF ANY
SOURCE CURSORS
KNOWN RELATIONSHIP EDGES
QUANTITATIVE TRAITS
QUALITATIVE TRAITS
BEHAVIOR SIGNATURE
RESOURCES / CONSTRAINTS / AGENCY
ARCHETYPE HYPOTHESES + CONTRADICTIONS
TRANSFORMATION STATE
LOCAL WEB HEAD
EVIDENCE POINTERS
STORY POINTERS
```

Then allow many contextual story roles:

```text
VWAV STORY:
SaverOne = investee / strategic operating character

SAVERONE STORY:
SaverOne = main character

CEMEX STORY:
SaverOne = supplier / technology partner
```

The character identity is the same object in every story.

### 1A. PROFILE MEMORY

Character Memory also preserves the reusable character profile defined by:
`../../../floware/core/character-system.flow.md`

The profile is not root-relative except where a field is explicitly a story role.

Persist:
- quantitative traits with as-of/evidence;
- qualitative traits with evidence/confidence/contradictions;
- behavior signature;
- resources, constraints and agency;
- zero or more archetype hypotheses;
- transformation history / candidate next forms;
- unclassified or emergent features.

Archetype membership is never required for re-rooting.

## 2. RE-ROOT RULE

When the user selects a nested character as the new main character:

```text
LOAD CANONICAL CHARACTER MEMORY
→ SET CHARACTER AS NEW DEGREE 0
→ RESET RESEARCH DEPTH BUDGET TO 4
→ REUSE ALL KNOWN FACTS / SOURCES / EDGES
→ RECALCULATE DEGREES RELATIVE TO NEW ROOT
→ IDENTIFY NEWLY IN-SCOPE BRANCHES
→ REFRESH STALE / DUE SOURCES
→ EXPAND MISSING LOCAL WEB
→ BUILD NEW ROOT STORY
```

Do **not** inherit the old remaining budget.

Example:

```text
VWAV-rooted story:
SaverOne = absolute D1
remaining budget = 3

RE-ROOT TO SAVERONE:
SaverOne = new D0
remaining budget = 4
```

The previously researched three degrees are reused.
The new fourth degree from SaverOne becomes newly researchable.

## 2A. RESOURCE-BUDGET SEMANTICS

A four-degree horizon is assigned because research capacity is finite.

Re-rooting does not imply that four degrees is intrinsically sufficient for the new character.

It means the current system grants the new root the maximum research budget presently available.

If future capacity expands:

```text
4-degree policy
→ 5 / 6 / adaptive / open-ended policy
```

the same Character Memory should continue outward from saved boundary branches.

## 3. NO DUPLICATE EVIDENCE

Re-rooting must not copy facts into independent disconnected histories.

Use:

```text
CANONICAL EVIDENCE
↕
CANONICAL CHARACTER MEMORY
↕
MULTIPLE STORY VIEWS
```

Story memories should point to canonical character/evidence objects.

A fact about SaverOne discovered while researching VWAV remains SaverOne evidence when SaverOne later becomes the main character.

## 4. LOCAL WEB MEMORY

Each material character retains its own local web head:

```text
CHARACTER
├─ subsidiaries
├─ customers
├─ suppliers
├─ partners / JVs
├─ investees / acquisitions
├─ financing / lenders
├─ regulators / governments
├─ management / insiders
├─ distributors
├─ technologies / programs
└─ courts / exchanges / other decision-makers
```

For every local-web edge preserve:
- relationship type;
- current state;
- prior state;
- relationship delta;
- materiality;
- source authority;
- freshness;
- propagation path.

## 5. SUBSIDIARY RULE

A subsidiary has two simultaneous truths:

```text
RELATIVE TO PARENT:
SUBSIDIARY

RELATIVE TO ITSELF:
MAIN CHARACTER OF ITS OWN STORY
```

Therefore store:
- parent ownership/control edge;
- consolidation/accounting relation;
- the subsidiary's own operations;
- its own subsidiaries;
- its own customers;
- its own financing;
- its own regulators;
- its own partners;
- its own timers and source cursors.

Do not make subsidiary memory dependent on the parent story file.

## 6. DEGREE RECALCULATION

Degrees are **view-relative**, not permanent character attributes.

When the root changes, recompute:

```text
degree_from_current_root
remaining_depth_budget
local_degree
propagation_to_current_root
```

Do not overwrite historical story degrees.

Example:

```text
VWAV ROOT
VWAV D0 → SaverOne D1 → Cemex D2

SAVERONE ROOT
SaverOne D0 → Cemex D1
VWAV may become D1 through the ownership relationship
```

## 7. STORY REUSE

When re-rooting, classify stored information:

```text
REUSE DIRECTLY
- identity
- historical evidence
- relationships still current
- source cursors
- subsidiaries / customers already mapped

REFRESH
- current filings/news
- relationship states
- financing
- timers
- current operating facts

EXPAND
- branches newly inside the four-degree horizon
- branches previously stopped for parent-relative immateriality but now material to new root
```

Parent-relative immateriality does not equal character-relative immateriality.

## 8. CHARACTER PROMOTION

Any material entity may be promoted from nested-only memory to a full research root.

Promotion does not require it to be a public security.

Possible main characters include:
- public companies;
- private subsidiaries;
- acquisition targets;
- JVs;
- customers;
- regulators / agencies where process analysis requires it.

If the goal is stock allocation, a non-public root may not itself be tradeable, but its story can still be researched as the central object.

## 9. MEMORY LAYERS

```text
CANONICAL CHARACTER MEMORY
= reusable identity + character profile + local web + evidence/source state

STORY MEMORY
= one root-relative causal view over characters

STOCK ENTITY MEMORY
= security-specific capital/price/Quality/TTC state
```

Do not collapse these layers.

## 10. MISS RULE

A Re-Root / Character-Memory Miss occurs when:
- a subsidiary is stored only inside its parent's prose;
- a known character must be re-researched because its prior evidence was not attached to its own canonical memory;
- re-rooting duplicates evidence instead of referencing it;
- degrees are treated as permanent instead of recalculated relative to the new root;
- a re-rooted character keeps only the old remaining depth budget rather than receiving four degrees;
- parent-relative materiality suppresses a branch that is material to the newly selected root;
- archetype/qualitative state is stored only in one story instead of reusable Character Memory;
- a stale archetype survives after the character materially transforms.

## OUTPUT

```text
CURRENT ROOT:
CANONICAL CHARACTER ID:
PRIOR STORY ROLES:
REUSED MEMORY:
REFRESHED MEMORY:
NEWLY IN-SCOPE BRANCHES:
NEW DEGREE MAP:
CHARACTER PROFILE STATUS:
ARCHETYPE / TRANSFORMATION DELTAS:
STORY STATUS:
```

## SOFTWARE / HARD-LIMIT BOUNDARY

Floware determines story meaning, materiality, and re-root expansion.

Deterministic persistence is justified for:
- stable character identity;
- edge/evidence pointers;
- source cursors;
- versioning;
- graph reuse;
- root-relative degree recalculation metadata.
