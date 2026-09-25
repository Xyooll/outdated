# FLOW — Domain Library

FLOW ID: CORE-DOMAIN-LIBRARY
STATUS: **CANDIDATE / VERIFICATION_PENDING**
DOMAIN: core
JOB: retrieve, curate, distill, and maintain reusable domain knowledge so Xyool starts from accumulated internal knowledge before repeating external research
AUTHORITY: domain-knowledge memory/index authority only; no authority to manufacture facts, validate efficacy, overwrite canonical rules, or suppress required external refresh
PARENT GOALPOST: ../../research/system-tests/domain-establishment-v1-2026-09-24/GOALPOST.md
UPSTREAM FLOWS: Domain Establishment, Research, Learning, Evaluation/Validation outputs, domain Flows
DOWNSTREAM FLOWS: Domain Establishment, Research, domain Flows, Learning
INBOUND PIPES: PLUMBING.md#pipe-core-domain-establishment-library, PLUMBING.md#pipe-core-research-library
OUTBOUND PIPES: PLUMBING.md#pipe-core-library-domain-establishment, PLUMBING.md#pipe-core-library-research
SOFTWARE DEPENDENCIES: none

## GOAL

Reduce repeated domain research by preserving reusable, source-traceable, validation-aware knowledge and exposing it before outside retrieval is attempted.

Core law:

> **Remember what was earned; refresh what can change; research only what is still missing.**

## GOALPOST

A library interaction is complete when:
- relevant stored knowledge/canonical pointers were checked;
- scope/freshness/validation status were assessed;
- sufficient internal knowledge was returned, or material gaps were named;
- any reusable new result was written back without erasing provenance/history;
- rejected/superseded/stale knowledge was not silently reused.

## INPUT STATE

Load:
- domain identity;
- requested function/question;
- domain library INDEX.md if present;
- relevant knowledge objects/pointers;
- rule/source registries;
- validation/failure history;
- freshness requirements;
- current establishment/update scope.

## EVIDENCE

Library knowledge derives from canonical domain artifacts and their provenance.

Acceptable bases include:
- established rule/method objects;
- source registries;
- domain ontology/state contracts;
- validation/evaluation records;
- failure/learning records;
- frozen cases/controls;
- correspondence results validated in the target domain.

Library repetition itself is not evidence.

## PROCESS

~~~text
RECEIVE DOMAIN QUESTION / KNOWLEDGE UPDATE
→ LOAD DOMAIN LIBRARY INDEX
→ FIND RELEVANT KNOWLEDGE OBJECTS + CANONICAL POINTERS
→ CHECK:
     SCOPE
     VERSION
     FRESHNESS
     VALIDATION STATUS
     CONFLICT / SUPERSESSION
→ IF SUFFICIENT:
     RETURN REUSABLE KNOWLEDGE + PROVENANCE
→ ELSE:
     EMIT MATERIAL GAP SET
     ROUTE GAP TO RESEARCH / DOMAIN ESTABLISHMENT
→ WHEN NEW REUSABLE KNOWLEDGE RETURNS:
     DISTILL MINIMUM REUSABLE OBJECT
     LINK CANONICAL ARTIFACTS
     PRESERVE PROVENANCE
     LABEL STATUS
     APPEND / SUPERSEDE WITHOUT ERASING HISTORY
     UPDATE INDEX
~~~

## GATES

Before reuse:
- domain/scope match;
- canonical pointer resolves;
- knowledge is not superseded/rejected;
- freshness is adequate for the claim;
- validation status is not overstated;
- dependencies/boundaries are preserved.

Before write-back:
- result is materially reusable;
- source/canonical provenance exists when required;
- authorship/status are clear;
- one example is not promoted into a general law;
- private user data is excluded unless explicitly authorized for that storage surface.

## ADAPTATION

If stable source-grounded knowledge is repeatedly requested, prefer the stored object and source pointer over re-retrieval.

If a claim is dynamic, retain the reusable method/background knowledge but refresh the changing state.

If sources conflict, store the conflict and competing pointers rather than flattening them.

If validation changes, update the library status/pointer while preserving prior history.

## BOUNDARIES

The Domain Library does not:
- replace Research when evidence is stale/missing/contested;
- replace canonical rule/source registries;
- declare predictive/causal validity;
- store every raw source document;
- convert private user records into general domain memory;
- erase rejected/superseded history.

## FAIL-CLOSED CONDITIONS

Return GAP / REFRESH_REQUIRED / CONFLICTED when:
- no canonical pointer exists;
- freshness is insufficient;
- scope mismatch is material;
- knowledge was superseded/rejected;
- provenance cannot be recovered;
- validation status is ambiguous for the requested authority.

## OUTPUT STATE

~~~text
DOMAIN:
QUESTION / FUNCTION:
LIBRARY HIT STATUS:
KNOWLEDGE IDS:
CANONICAL POINTERS:
SCOPE:
FRESHNESS:
VALIDATION STATUS:
CONFLICTS / BOUNDARIES:
MATERIAL GAPS:
EXTERNAL RESEARCH REQUIRED:
WRITE-BACK REQUIRED:
~~~

## LEARNING HOOK

Track repeated misses where:
- knowledge existed but was not retrieved;
- stale knowledge was reused;
- the same external research was unnecessarily repeated;
- a library object overstated validation;
- useful failure/validation lessons were not written back.

Those are domain-memory failures and may improve indexing/contract structure.

## SOFTWARE / HARD-LIMIT BOUNDARY

NONE — FLOWARE SUFFICIENT

Search/index software is deferred until repository-scale retrieval becomes a demonstrated bottleneck.

## COMPLEXITY RULE

Store the smallest reusable knowledge object that prevents meaningful relearning. Do not duplicate entire source documents or canonical domain files.
