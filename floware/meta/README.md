# Floware Meta Flows

Status: **CANONICAL META LAYER**

Meta Flows operate on the structure, configuration, mapping, validation, routing, governance, and integrity of other Flows or domain-to-Flow relationships.

They are still Flows and must satisfy `../FLOW-CONTRACT.md`.

Meta describes architectural level, not superior authority.

Current canonical Meta architecture:

### Composite integrity layer
- `pipeline-integrity.flow.md` — top-level end-to-end integrity coordinator for multi-Flow pipelines.
- `PLUMBING.md` — canonical high-risk Meta Pipes connecting Xyool Execution, the composite, primitive Meta Flows, and independent Audit.

### Primitive Meta Flows

- `mapping.flow.md` — explicit representation-to-representation mapping with invariants, transformations, incompatibilities, and information-loss tracking.
- `domain-configurer.flow.md` — configure a domain to use Floware by binding local semantics to applicable general contracts through explicit mappings.
- `audit.flow.md` — independent integrity and contract-conformance audit.
- `patching.flow.md` — propagate one authorized change across every materially dependent Flow, mapping, domain binding, schema, state contract, test, registry, and compatibility surface.
- `sequencing.flow.md` — determine dependency-safe order, parallelism, barriers, readiness, and re-entry across composed operations.
- `failure.flow.md` — **CANDIDATE / VERIFICATION_PENDING** — classify material failures, assign the correct response owner/disposition, and preserve re-entry/learning evidence without performing the repair.
- `promotion-lifecycle.flow.md` — **CANDIDATE / VERIFICATION_PENDING** — govern candidate promotion, demotion, retirement, supersession, and rollback from earned evidence without replacing Evaluation, Audit, or Patching.

Core rule:

> **A Meta Flow may govern how Flows fit together, but it may not silently import domain-specific semantics or rewrite the contract it is evaluating.**

Canonical domain-integration relationship:

```text
DOMAIN-NATIVE REALITY
→ PIPELINE INTEGRITY
   → MAPPING
   → DOMAIN CONFIGURER
   → SEQUENCING
   → validated Floware bindings
   → AUDIT
→ VERIFIED DOMAIN PIPELINE
```

Mapping, configuration, sequencing, patching, failure classification, lifecycle promotion, and audit are separate primitive jobs. Do not collapse their contracts.

Pipeline Integrity composes them when end-to-end integrity matters.

Canonical change route through Pipeline Integrity:

```text
DEVELOPMENT / LEARNING
→ authorized source change
→ PIPELINE INTEGRITY
→ PATCHING
→ impact graph + patch set
→ SEQUENCING
→ dependency-safe order / parallel branches / barriers
→ Mapping / Domain Configurer when required
→ apply dependent updates
→ AUDIT
→ VERIFIED or BLOCKED
```


## Failure and lifecycle routing

Material failures inside a composed pipeline route through Pipeline Integrity to `failure.flow.md`; the Failure Flow classifies and returns the disposition/owner but does not perform the repair.

When an objective includes changing the lifecycle authority of a candidate/component, Pipeline Integrity may invoke `promotion-lifecycle.flow.md` after the required Evaluation/Audit evidence exists. Promotion may require Patching, but it does not patch itself.
