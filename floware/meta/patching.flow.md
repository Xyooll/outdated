# META FLOW — Patching

FLOW ID: META-PATCHING
STATUS: **ACTIVE / CANONICAL**
DOMAIN: meta
JOB: turn one intended architectural/system change into a complete, auditable patch set across every materially dependent Xyool surface
AUTHORITY: change-impact discovery, patch-set composition, propagation, and completion tracking only; no authority to invent the underlying change
PARENT GOALPOST: supplied by Development, Learning, migration, or the authorized change request
UPSTREAM FLOWS: Pipeline Integrity, Development, Learning, Mapping, Domain Configurer, Audit remediation, migration/change requests
DOWNSTREAM FLOWS: Sequencing, owning Flows, Mapping, Domain Configurer, Audit, tests/verification, migration, registry/documentation/state contracts as applicable
INBOUND PIPES: `PLUMBING.md#pipe-meta-integrity-patching`
OUTBOUND PIPES: `PLUMBING.md#pipe-meta-patching-sequencing`, candidate verification through `PLUMBING.md#pipe-meta-candidate-audit`
SOFTWARE DEPENDENCIES: none by default; deterministic dependency indexing, reference search, schema validation, diffing, and transactional staging may support exactness

## GOAL

Apply one intended change everywhere that change must propagate, without relying on memory of repository locations and without allowing a partial patch to masquerade as complete.

Core law:

> **Change the concept once; patch every materially dependent representation of that concept.**

A patch is not "edit the obvious file."

A patch is:

~~~text
INTENDED CHANGE
→ IMPACT GRAPH
→ COMPLETE PATCH SET
→ APPLY
→ VERIFY
→ META AUDIT
→ COMPLETE OR BLOCKED
~~~

## GOALPOST

A patch is complete only when:
- the authoritative source change is identified;
- the pre-change contract/version is known;
- direct and indirect dependency surfaces are mapped;
- each impacted surface has an explicit disposition;
- required representations are updated consistently;
- historical records are preserved where they should not be rewritten;
- migrations/backward compatibility are handled when needed;
- required tests/checks pass;
- Meta Audit finds no unresolved material omission;
- patch status is VERIFIED.

## INPUT STATE

At minimum:
- patch intent;
- reason / originating evidence;
- authoritative source object(s);
- pre-change version/hash/state;
- intended post-change invariant;
- frozen goalpost where material;
- repository/domain scope;
- known consumers/dependents;
- authority/boundary constraints.

## EVIDENCE

Patch impact should be established from the strongest available repository evidence, including:
- declared upstream/downstream dependencies;
- Flow IDs and canonical paths;
- registries and repository maps;
- Mapping objects and domain configuration bindings;
- schema/state contracts;
- reference searches for terms, fields, paths, and versions;
- diffs/hashes of the pre-change and post-change source objects;
- migration/runtime compatibility requirements;
- tests, fixtures, and prior regressions;
- explicit semantic dependency reasoning where literal references are absent.

A search result alone is not proof that the impact graph is complete.

Absence of a literal reference is not proof that no semantic dependency exists.

## PATCH OBJECT

Minimum patch object:

~~~text
PATCH ID:
TITLE:
ORIGIN:
GOALPOST:
STATUS:
AS-OF:

INTENT:
SOURCE-OF-TRUTH OBJECTS[]:
PRE-CHANGE VERSION / HASH:
TARGET INVARIANT:

IMPACT GRAPH[]
  object / path
  relationship_to_change
  impact_type
  required_action
  migration_required
  verification_required
  status

UNCHANGED-BY-DESIGN[]
OUT-OF-SCOPE[]
HISTORICAL-IMMUTABLE[]
BLOCKERS[]
APPLIED CHANGES[]
VERIFICATION[]
META AUDIT RESULT:
~~~

## PATCH STATUS

Use:

~~~text
DRAFT
IMPACT_MAPPED
READY
APPLYING
PARTIAL
BLOCKED
VERIFICATION_PENDING
VERIFIED
SUPERSEDED
ROLLED_BACK
~~~

Only VERIFIED means the patch is complete.

PARTIAL is an explicit failure/in-progress state, never success.

## IMPACT TYPES

Classify each material dependency as one or more:

~~~text
CANONICAL_CONTRACT
FLOW_REFERENCE
META_FLOW_REFERENCE
DOMAIN_BINDING
MAPPING
REGISTRY
GLOSSARY / TERMINOLOGY
REPOSITORY_MAP / ENTRYPOINT
STATE_CONTRACT
SCHEMA
PERSISTED_CURRENT_STATE
HISTORICAL_RECORD
MIGRATION / COMPATIBILITY
SOFTWARE / RUNTIME
TEST / FIXTURE
RESEARCH / VALIDATION
USER_CONCEPT MEMORY
DOCUMENTATION / EXAMPLE
EXTERNAL INTERFACE
~~~

The classification determines how the surface may be changed.

## IMPACT DISCOVERY

Do not rely only on literal filename/reference search.

Build the patch impact graph from multiple channels:

### 1. Declared dependencies
Read:
- inbound/outbound Pipe pointers and wrappers;
- pipeline manifests / Pipe contracts;
- upstream/downstream Flow declarations;
- core parent links;
- domain configuration bindings;
- Mapping objects;
- registries;
- schemas;
- repository maps.

### 2. Reference search
Search for:
- exact Flow IDs;
- filenames/paths;
- canonical terms;
- field names;
- schema properties;
- version identifiers;
- examples using the old contract.

### 3. Semantic dependency scan
Ask:

~~~text
IF THIS CONCEPT CHANGES, WHAT ELSE BECOMES FALSE OR INCOMPLETE EVEN IF IT NEVER NAMES THE SOURCE FILE?
~~~

Examples:
- adding a new required Character field may affect schema, memory Flow, domain config, Writer input, Audit, tests, and migration;
- renaming a Meta Flow may affect registry, glossary, repository map, entrypoint routing, references, and concept memory;
- changing a domain mapping may require Mapping + Domain Configurer review even if no literal reference exists.

### 4. Persistence / history scan
Determine whether current persisted state must migrate.

Do not rewrite historical evidence, frozen experiments, prior predictions, audit logs, or old concept records merely to make history look current.

### 5. Verification scan
Identify which checks prove the patch is complete.

## PROCESS

~~~text
RECEIVE AUTHORIZED CHANGE
→ IDENTIFY AUTHORITATIVE SOURCE / INVARIANT
→ FREEZE PRE-CHANGE STATE
→ DISCOVER DECLARED DEPENDENCIES
→ TRAVERSE MATERIAL INBOUND / OUTBOUND PIPES
→ SEARCH EXPLICIT REFERENCES
→ RUN SEMANTIC DEPENDENCY SCAN
→ CLASSIFY IMPACTED SURFACES
→ BUILD PATCH IMPACT GRAPH
→ MARK:
    UPDATE
    MIGRATE
    VERIFY-ONLY
    UNCHANGED-BY-DESIGN
    HISTORICAL-IMMUTABLE
    BLOCKED
→ IF REPRESENTATIONS MUST ALIGN: CALL MAPPING
→ IF DOMAIN BINDING CHANGES: CALL DOMAIN CONFIGURER
→ CALL `sequencing.flow.md` FOR NON-TRIVIAL PATCH ORDER / PARALLELISM / BARRIERS
→ APPLY PATCH SET
→ RECORD EACH APPLIED CHANGE
→ RUN LOWEST-SUFFICIENT VERIFICATION
→ RUN META AUDIT
→ IF ANY MATERIAL DEPENDENCY MISSED:
      STATUS = PARTIAL / BLOCKED
      DO NOT CLAIM COMPLETION
→ ELSE:
      STATUS = VERIFIED
~~~

## PATCH ORDER

For non-trivial patch sets, `sequencing.flow.md` owns the operational order.

The list below is a **default precedence hint**, not an independent sequencing authority:

Default dependency-aware order:

~~~text
1. SOURCE-OF-TRUTH CONTRACT / FLOW
2. META MAPPINGS / DOMAIN CONFIGURATION
3. CONSUMING FLOWS
4. STATE CONTRACTS / SCHEMAS
5. PERSISTED CURRENT STATE MIGRATIONS
6. SOFTWARE / RUNTIME SUPPORT IF JUSTIFIED
7. TESTS / FIXTURES
8. REGISTRY / GLOSSARY / REPOSITORY MAP / ENTRYPOINTS
9. RESEARCH / CONCEPT-MEMORY RECORD
10. META AUDIT
~~~

This is a default, not a rigid sequence. Sequencing may safely parallelize independent surfaces and must override this hint when real dependencies require a different order.

A schema-first or migration-first order may be safer when runtime compatibility requires it.

## PATCH SURFACE DISPOSITION

Every impacted surface must end in one disposition:

~~~text
UPDATED
MIGRATED
VERIFIED_UNCHANGED
HISTORICAL_IMMUTABLE
NOT_APPLICABLE
BLOCKED
SUPERSEDED
~~~

No discovered material dependency may simply disappear from the patch set.

## ATOMICITY / PARTIAL-PATCH RULE

Prefer a staged patch set that is promoted only after verification.

If the repository/tooling cannot update all files in one atomic transaction:

~~~text
PATCH STATUS = APPLYING / PARTIAL
until
all required surfaces + verification + audit are complete.
~~~

Never use multiple successful file writes as proof that the overall patch succeeded.

A later failure must leave an explicit incomplete-patch record or be rolled back.

## CURRENT STATE VS HISTORY

Patching may update:
- current contracts;
- active schemas;
- current configuration;
- live/persisted heads;
- active examples/tests.

Patching must normally preserve:
- old frozen predictions;
- historical research results;
- prior audit records;
- old evidence records;
- prior user-concept entries;
- superseded versions needed for provenance.

Use migrations, version markers, or superseding records instead of rewriting history.

Core law:

> **Patch the present contract; preserve the evidence of the past.**

## VERSIONING

A material contract patch should determine whether it is:

~~~text
PATCH
backward-compatible clarification/fix

MINOR
new optional capability / backward-compatible extension

MAJOR
breaking semantic or structural change
~~~

Versioning need not use semantic-version syntax everywhere, but compatibility impact must be explicit.

## MAPPING RELATIONSHIP

Use Mapping when the patch changes how two representations align.

~~~text
PATCHING
= where must the authorized change propagate?

MAPPING
= how do the affected representations line up?
~~~

Patching may call Mapping; it does not replace it.

## DOMAIN CONFIGURER RELATIONSHIP

Use Domain Configurer when the patch changes:
- domain-to-core bindings;
- domain capability selection;
- domain-local semantic contracts;
- Story Reader/Writer authority;
- archetype/trait policy;
- evidence/state/outcome semantics.

Patching coordinates propagation; Domain Configurer validates the domain composition.

## AUDIT RELATIONSHIP

Meta Audit is independent of Patching.

~~~text
PATCHING
→ claims the patch set is complete

AUDIT
→ tests whether that claim is true
~~~

Required verification handshake:

```text
PATCH SET APPLIED
→ PATCH STATUS = VERIFICATION_PENDING
→ META AUDIT evaluates the candidate patch
→ PASS / PASS_WITH_NOTES
→ PATCH STATUS = VERIFIED
```

Audit does **not** require the patch to already be VERIFIED.

Patching may not self-declare VERIFIED when a required independent audit reports FAIL/BLOCKED.

## DEVELOPMENT / LEARNING RELATIONSHIP

Development or Learning answers:

> **What should change and why?**

Patching answers:

> **If that change is authorized, what else must change with it?**

Do not let Patching invent architecture solely because propagation is inconvenient.

## GATES

Before APPLYING:
- source-of-truth change is authorized;
- intended invariant is explicit;
- impact graph is materially complete;
- high-risk migrations are identified;
- history-preservation rules are known.

Before VERIFIED:
- every impact-graph node has a disposition;
- schemas/contracts parse where applicable;
- literal references are not stale;
- semantic consumers are consistent;
- migrations preserve compatibility or explicitly break/version it;
- verification appropriate to the change type passed;
- Meta Audit has no unresolved material FAIL/BLOCKED.

## ADAPTATION

Small patch:
- one Flow + registry reference;
- direct verification may be sufficient.

Large cross-layer patch:
- core Flow;
- Meta mappings;
- multiple domain bindings;
- schemas;
- software;
- tests;
- migration;
- audit.

Do not make every typo correction a repository-wide ceremony.

Use the smallest patch scope that can prove completeness.

## BOUNDARIES

Patching does not:
- decide whether an unsupported idea should become canonical;
- rewrite historical evidence for consistency;
- silently broaden domain authority;
- use text replacement as a substitute for semantic compatibility;
- migrate state without preserving provenance;
- alter protected contracts merely to make downstream files easier to patch;
- declare success while material nodes remain unresolved.

## FAIL-CLOSED CONDITIONS

Return PARTIAL / BLOCKED when:
- source of truth is ambiguous;
- dependency graph cannot be established sufficiently;
- a breaking migration lacks a compatibility plan;
- a required Mapping/Domain Configurer step is unresolved;
- one or more required patch surfaces failed to update;
- verification cannot establish that stale semantics are gone;
- Meta Audit reports material failure.

## OUTPUT STATE

~~~text
PATCH ID:
PATCH STATUS:
SOURCE CHANGE:
TARGET INVARIANT:
IMPACTED SURFACES:
UPDATED:
MIGRATED:
VERIFIED UNCHANGED:
HISTORICAL IMMUTABLE:
BLOCKED:
VERIFICATION:
META AUDIT:
COMPATIBILITY / VERSION:
ROLLBACK / SUPERSEDE POINTER:
~~~

## LEARNING HOOK

A Patching Miss occurs when:
- a dependent file/contract/schema/state/test was omitted;
- a stale term/field survives and changes behavior;
- a historical artifact was incorrectly rewritten;
- a migration was unnecessary or destructive;
- a literal reference was updated but semantic behavior remained stale;
- patch ordering caused avoidable incompatibility;
- the patch was marked complete despite being partial.

Recurring misses should improve:
- Pipe declarations / wrappers;
- dependency declarations;
- repository maps;
- Mapping objects;
- schemas;
- patch-impact heuristics;
- deterministic dependency indexing.

## SYSTEM LINEAGE / BRANCH AUTHORITY

Repository-wide authority contract:
`../../SYSTEM-LINEAGE.md`

Patching must distinguish **where a change was developed** from **where that change becomes current**.

Core rule:

> **A branch-local patch is a proposal until the reconciled system change is integrated into `main`.**

For system-affecting changes:

~~~text
PROPOSAL BRANCH DELTA
→ identify intended invariant
→ compare against main
→ classify every material delta
→ reconcile impact graph
→ verify
→ Audit when material
→ integrate into main
→ only then CURRENT
~~~

Allowed delta dispositions:

~~~text
INTEGRATE
SUPERSEDE
PRESERVE_HISTORICAL
MIRROR_ONLY
REJECT
BLOCKED
~~~

A materially relevant branch delta may not disappear merely because another branch was selected as the baseline.

Scoped subordinate lineages are exceptions only within their declared scope. For example, `lineage/user-concepts` owns current `memory/user-concepts/` history; it does not own Floware or domain architecture.

When patching a scoped-lineage object:
- write the scoped canonical lineage first;
- record the canonical commit when reproducibility matters;
- synchronize `main` mirrors only as integration snapshots;
- never let a mirror silently become a competing authority.

Patching is BLOCKED when:
- the canonical integrated branch cannot be resolved;
- branch authority is ambiguous;
- an unmerged branch delta is being represented as current system truth;
- a scoped lineage is being used outside its declared authority.

## SOFTWARE / HARD-LIMIT BOUNDARY

Floware is sufficient for reasoning about impact and patch scope.

Deterministic software may be justified for:
- repository-wide reference indexing;
- dependency graph construction;
- schema/reference validation;
- staged multi-file transactions;
- exact diff/hashing;
- rollback;
- CI/test selection;
- migration execution.

Software support must implement the Patching contract; it must not silently become the architecture.
