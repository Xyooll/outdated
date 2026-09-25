# User Concept — Pipeline Integrity Composite

Date: 2026-09-24
Status: **ACTIVE / CORE FLOWARE ARCHITECTURE**

## USER-STATED

The priority is whatever ensures the pipeline's integrity.

## ASSISTANT INTERPRETATION

Xyool should expose one top-level Meta integrity front door for material multi-Flow work while preserving the independent primitive Meta contracts underneath it.

The composite should answer:

> **Is the whole pipeline valid end to end, not merely each stage locally?**

Canonical composition:

~~~text
PIPELINE INTEGRITY
├─ Mapping
├─ Domain Configurer
├─ Sequencing
├─ Patching
└─ independent Audit
~~~

Core rules:

> **A pipeline is only as valid as its weakest required handoff.**

> **Pipeline completion requires end-to-end integrity, not merely successful local stages.**

> **No stage may silently change the meaning, authority, version, provenance, or state assumptions of what it receives.**

## SYSTEM CONSEQUENCE

Canonical composite Meta Flow:
- `floware/meta/pipeline-integrity.flow.md`

The five existing Meta Flows remain primitive contracts.

Pipeline Integrity coordinates them only where applicable.

It owns:
- pipeline manifest;
- stage/handoff integrity;
- state/version continuity;
- authority continuity;
- provenance continuity;
- terminal-state integrity;
- final verification handshake.

It does not replace independent Audit.

## COMPOSITE ROUTES

Change management:

~~~text
AUTHORIZED CHANGE
→ Pipeline Integrity
→ Patching
→ Mapping / Domain Configurer as needed
→ Sequencing
→ Apply
→ Audit
→ VERIFIED / BLOCKED
~~~

Domain integration:

~~~text
DOMAIN
→ Pipeline Integrity
→ Mapping
→ Domain Configurer
→ Sequencing
→ Audit
→ VALIDATED DOMAIN PIPELINE
~~~

Ordinary multi-Flow execution:

~~~text
OBJECTIVE
→ Xyool Execution selects Flows
→ Pipeline Integrity
→ Sequencing + handoff/state checks
→ Audit when material
→ terminal output
~~~

## OPEN QUESTION

As pipelines become larger, machine-readable pipeline manifests and deterministic handoff/version validation may become justified software support. The integrity semantics remain Floware.
