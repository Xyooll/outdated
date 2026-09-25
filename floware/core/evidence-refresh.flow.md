# FLOW — Evidence Refresh

FLOW ID: CORE-EVIDENCE-REFRESH
STATUS: CANDIDATE / OPT-IN / INDEPENDENT AUDIT PENDING
DOMAIN: core / domain-neutral
JOB: Evidence Refresh
AUTHORITY: record and route only; existing domain, action, and promotion boundaries apply
PARENT GOALPOST: [Continuity v1](../../research/system-tests/floware-continuity-v1-2026-09-24/GOALPOST.md); individual runs retain their own goalpost
UPSTREAM FLOWS: Checkpoint Resume; Pipeline Integrity
DOWNSTREAM FLOWS: Pipeline Integrity; existing Sequencing/Patching through Pipeline Integrity
INBOUND PIPES: CONT-04, CONT-10 in [continuity Plumbing](../continuity/PLUMBING.md)
OUTBOUND PIPES: CONT-06 in [continuity Plumbing](../continuity/PLUMBING.md)
SOFTWARE DEPENDENCIES: existing authorized storage tools for durable writes; no runtime engine introduced

## GOAL

Determine which recorded conclusions and gates become unusable when their evidence or contracts change.

## GOALPOST

Every material changed input and dependent output has an explicit disposition, including unaffected outputs retained with reasons.

## INPUT STATE

Before/after input versions, current run manifest, consumed-input edges, Pipe wrappers/live state, changed authority or contract scope, active goalpost.

## EVIDENCE

Canonical source revisions, recorded read sets, domain freshness policies, material semantic dependencies and contradictions. Mere absence from a text search is not proof of independence.

## PROCESS

Identify changed roots. Traverse direct and transitive consumed-input dependencies, including merge outputs and audit conclusions. Ask which undeclared semantic dependencies could matter. Mark affected conclusions INVALIDATED in the new candidate view while retaining their historical versions. Preserve unaffected outputs only with an independence rationale. For uncertain dependencies block the uncertain subgraph and identify the missing evidence. Return impact facts to Pipeline Integrity: Sequencing alone owns re-entry epochs/readiness, and Patching handles changed contracts or bindings.

## GATES

Changed-root identity/version known; transitive consumers covered; terminal merge and prior verification invalidated when affected; unchanged outputs not needlessly discarded; invalidation does not automatically produce replacement truth.

## ADAPTATION

A source revision with no material semantic difference may retain output only after recording the compatibility reasoning. Contradictions stay explicit until the owning reasoning Flow resolves them.

## BOUNDARIES

Does not define a second scheduler, change domain truth, rewrite frozen research, or invalidate unrelated branches without evidence.

## FAIL-CLOSED CONDITIONS

Missing read set or unknown semantic dependency prevents claiming selective refresh is complete. Affected downstream action remains blocked until its owning gates are re-established.

## OUTPUT STATE

changed roots; affected closure; retained outputs and reasons; uncertain dependencies; proposed invalidation markers; contract-change flag; remediation owners. Sequencing assigns the epoch.

## LEARNING HOOK

Missed descendants and unnecessary invalidation become regression cases under Learning.

## SOFTWARE / HARD-LIMIT BOUNDARY

NONE — FLOWARE SUFFICIENT for bounded semantic impact assessment. Large exact graph closure or atomic head changes require Software Escalation and deterministic support.

## COMPLEXITY RULE

Reuse existing dependency records and Pipe contracts rather than maintaining an independent graph of contradictory edges.
