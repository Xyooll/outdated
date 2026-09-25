# META FLOW — Audit

FLOW ID: `META-AUDIT`  
STATUS: **ACTIVE / CANONICAL**  
DOMAIN: meta  
JOB: independently evaluate the integrity, completeness, contract conformance, provenance, and boundary preservation of Flows, mappings, configurations, state transitions, outputs, and learning changes  
AUTHORITY: audit / diagnostic / blocking only; no silent mutation of the audited object  
PARENT GOALPOST: as supplied by the audited context  
UPSTREAM FLOWS: any Flow, Meta Flow, domain Flow, mapping, configuration, state transition, or learning/promotion candidate  
DOWNSTREAM FLOWS: Pipeline Integrity, development, learning, Patching, Sequencing, domain configuration, mapping, execution, or the owning Flow as appropriate  
INBOUND PIPES: `PLUMBING.md#pipe-meta-candidate-audit`  
OUTBOUND PIPES: `PLUMBING.md#pipe-meta-audit-integrity` plus remediation routing to the owning Flow/Meta Flow  
SOFTWARE DEPENDENCIES: none by default; deterministic validators may support exact schema/hash/reference checks

## GOAL

Provide an independent integrity layer that can determine whether a Xyool object or process still satisfies the contracts, evidence, state, authority, and boundaries that govern it.

Core law:

> **The auditor may inspect the contract, but it may not silently redefine the contract it is auditing.**

## GOALPOST

An audit is complete when:
- the governing contract/version is identified;
- the target and relevant evidence/state are frozen for the audit;
- all applicable integrity dimensions are checked;
- findings are classified;
- blockers and unresolved evidence gaps are explicit;
- remediation is routed without the Audit Flow performing hidden repair.

## INPUT STATE

At minimum:
- audit target;
- target type;
- governing Flow/contract/schema/version;
- applicable domain configuration;
- relevant goalpost;
- current and prior state when transition integrity matters;
- evidence/provenance pointers;
- authority and boundary rules.

## AUDIT TARGETS

The Meta Audit may inspect candidate/provisional objects before they reach final status.

For example, a patch in VERIFICATION_PENDING may be audited so that the audit result can determine whether it becomes VERIFIED.

The Meta Audit may inspect:

```text
FLOW
META FLOW
DOMAIN FLOW
DOMAIN CONFIGURATION
MAPPING
RELATIONAL STORY
STATE TRANSITION
EVIDENCE / PROVENANCE GRAPH
MEMORY WRITE
PREDICTION / OUTCOME LINK
LEARNING SIGNAL
PROMOTION / ROLLBACK CANDIDATE
CORRESPONDENCE OBJECT
SOFTWARE ESCALATION DECISION
PATCH SET / PATCH IMPACT GRAPH
SEQUENCE / OPERATION GRAPH
PIPE / PIPELINE / PIPELINE MANIFEST / PLUMBING
```

## PROCESS

```text
SELECT AUDIT TARGET
→ IDENTIFY GOVERNING CONTRACT / VERSION / GOALPOST
→ FREEZE AUDIT VIEW
→ LOAD REQUIRED EVIDENCE / PRIOR STATE / REFERENCES
→ CHECK IDENTITY + VERSION + AUTHORITY
→ CHECK REQUIRED FIELDS / GATES / BOUNDARIES
→ CHECK EVIDENCE + PROVENANCE + FRESHNESS
→ CHECK REFERENCES / POINTERS / RELATIONSHIPS
→ CHECK STATE-TRANSITION CONTINUITY WHEN APPLICABLE
→ CHECK DOMAIN-BOUNDARY / CORE-CONTAMINATION RISK
→ CHECK OUTPUT / OUTCOME / LEARNING CLOSURE
→ CLASSIFY FINDINGS
→ EMIT AUDIT RECORD
→ ROUTE REMEDIATION TO THE OWNING FLOW / META FLOW
```

## AUDIT DIMENSIONS

Use only the dimensions relevant to the target.

### System-lineage integrity
- `SYSTEM-LINEAGE.md` is resolvable;
- current integrated state is sourced from `main`;
- the exact `main` commit is recorded when reproducibility matters;
- non-`main` branches are not treated as current merely because they are newer or specialized;
- proposal/mirror/historical status is explicit when a branch is used;
- scoped subordinate lineages are used only inside their declared path/authority;
- unmerged branch deltas that materially affect the audit target are surfaced;
- a branch-local PASS is not represented as integrated-system promotion.

For User Concept Memory specifically:
- current concept history resolves from `lineage/user-concepts`;
- branch-local copies are mirrors/snapshots;
- a frozen consumer records the exact canonical memory commit when material.

### Contract integrity
- required fields present;
- declared upstream/downstream relationships valid;
- boundaries preserved;
- fail-closed rules respected;
- output satisfies the declared contract.

### Mapping integrity
- source and target objects identified;
- preserved invariants explicit;
- transformations explicit;
- information loss named;
- unmapped or incompatible components named;
- no silent domain-specific leakage into a core contract.

### Pipe integrity
- endpoint pointers resolve to the intended canonical objects;
- source/target contracts are compatible or an explicit Mapping governs the transformation;
- wrapper semantics do not redefine canonical endpoint meaning;
- provenance/freshness/version requirements are preserved;
- uncertainty is not silently strengthened;
- authority does not silently increase;
- live Pipe state reflects current compatibility/readiness/invalidation;
- Pipe failure/re-entry behavior is consistent with Sequencing and the pipeline.

### Pipeline integrity
- pipeline objective/terminal state are explicit;
- required stages are identified and have valid terminal status;
- every material Pipe satisfies input/output compatibility;
- semantic meaning is preserved across Pipes or an explicit Mapping exists;
- state/version/as-of continuity is preserved;
- provenance and uncertainty survive required Pipes;
- authority does not silently increase downstream;
- stale/superseded upstream state invalidates affected descendants;
- local stage PASS states are not treated as automatic pipeline PASS;
- final verification handshake is independent.

### Sequencing integrity
- hard prerequisites completed before dependents;
- domain-mandated gates/order preserved;
- independent branches were not incorrectly treated as dependent when material;
- dependent/shared-state operations were not run unsafely in parallel;
- barriers completed before downstream merge/finalization;
- invalidated results were not reused in a newer execution epoch;
- hard dependency graph is cycle-safe or explicitly blocked.

### Patch integrity
- source-of-truth change is identified;
- impact graph includes direct and semantic dependencies;
- every impacted surface has a disposition;
- stale references/semantics are not left active;
- migrations preserve compatibility/provenance or explicitly version the break;
- historical immutable records were not rewritten merely for consistency;
- PARTIAL patches are not represented as complete;
- verification matches the kind of change.

### State integrity
- prior state known where required;
- transition trigger/evidence identified;
- current state does not erase material history;
- stale state is not presented as current;
- invalid transitions are blocked or explained.

### Relational-story / character integrity
- root/main character resolves;
- character identity is separated from root-relative role;
- quantitative and qualitative traits retain provenance;
- archetypes are non-exclusive hypotheses rather than forced categories;
- archetype form is not being used as a proxy for Quality, attractiveness, maturity, or action authority;
- character condition and trajectory are represented separately when material;
- contradictory archetype evidence is preserved;
- character transformation state is updated when material;
- material characters/edges have provenance;
- pointers resolve to canonical memory where required;
- relationship deltas are preserved;
- resource-boundary stops are not misrepresented as reality boundaries;
- material misses/state changes are surfaced;
- Story Reader current state contains no future leakage;
- Story Writer branches begin from the frozen Reader state;
- Writer branches identify triggers, proof and invalidation;
- a preferred narrative did not suppress a material counter-story.

### Evidence integrity
- source authority matches the claim;
- provenance is recoverable;
- freshness is sufficient;
- contradiction handling is explicit;
- inference is not promoted into fact.

### Learning integrity
- outcome links back to the original prediction/decision;
- pre-outcome evidence is preserved;
- evaluator/goalpost was not rewritten to rescue the candidate;
- development and validation evidence are not silently mixed;
- promotion status matches evidence.

### Authority integrity
- analysis does not become action authority;
- domain-local calibration does not become universal authority;
- correspondence confidence does not leak across domains;
- software support does not silently override canonical Floware.

## FINDING STATES

```text
PASS
PASS_WITH_NOTES
WARN
FAIL
BLOCKED
NOT_APPLICABLE
```

A FAIL means the audited object violates a known governing requirement.

A BLOCKED result means the audit cannot establish integrity because required evidence, version identity, provenance, or state is unavailable.

## LOCAL SELF-AUDIT VS META AUDIT

A Flow may contain its own self-checks.

Those remain useful for fast local integrity.

The Meta Audit is different:

```text
LOCAL SELF-AUDIT
= the Flow checking its own declared conditions during execution

META AUDIT
= an independent Flow evaluating whether the Flow, mapping,
  configuration, transition, or result preserved the governing contract
```

Do not remove local checks merely because Meta Audit exists.

Use Meta Audit when independence, cross-layer integrity, release/promotion confidence, or architectural consistency matters.

## GATES

Before returning PASS:
- governing contract/version must be known;
- material evidence/provenance must be available;
- target must not have changed during the audit without disclosure;
- applicable domain configuration must be identified;
- unresolved material contradictions must be named.

## ADAPTATION

The audit route depends on target type.

Examples:

```text
DOMAIN CONFIGURATION
→ emphasize mapping + domain-boundary + contract integrity

RELATIONAL STORY
→ emphasize identity + relationship + provenance + state continuity

LEARNING PROMOTION
→ emphasize frozen evaluator + outcome linkage + validation separation

SOFTWARE ESCALATION
→ emphasize necessity + authority + Floware/software boundary
```

## BOUNDARIES

The Meta Audit does not:
- rewrite the audited contract;
- repair the target silently;
- change a frozen goalpost;
- invent missing evidence;
- grant domain or action authority;
- promote a candidate merely because it is internally coherent.

Repairs must be routed to the owning Flow, Patching Meta Flow, Domain Configurer, Mapping Meta Flow, Development Flow, Learning Flow, or other responsible layer.

## FAIL-CLOSED CONDITIONS

Return BLOCKED rather than PASS when:
- a current-system claim cannot establish canonical `main` identity;
- the audited target is being sourced from an unmerged proposal branch without explicit proposal scope;
- a subordinate canonical lineage is being used outside its declared scope;
- the governing contract/version cannot be identified;
- required provenance cannot be recovered;
- the audit target is materially incomplete;
- the target changed during audit and the delta cannot be reconciled;
- the evaluator and candidate cannot be separated where independence is required.

## OUTPUT STATE

```text
AUDIT ID:
TARGET:
TARGET TYPE:
GOVERNING CONTRACT / VERSION:
DOMAIN / CONFIGURATION:
GOALPOST:
AS-OF:
FINDING:
CHECKS PERFORMED:
PASSED:
WARNINGS:
FAILURES:
BLOCKERS:
PROVENANCE:
REMEDIATION OWNER:
RE-AUDIT CONDITION:
```

## LEARNING HOOK

Audit failures and recurring warnings may feed:
`../core/learning.flow.md`

The learning system may improve the responsible Flow only after preserving the failed audit evidence and governing goalpost.

## SOFTWARE / HARD-LIMIT BOUNDARY

`NONE — FLOWARE SUFFICIENT BY DEFAULT`

Use deterministic software only when exact schema validation, hashing, reference resolution, immutable logging, or scale justifies it.
