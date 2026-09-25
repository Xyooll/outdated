# Floware Registry

Status: **CANONICAL ROUTING INDEX**

## Core flows

| Flow | Status | Purpose |
|---|---|---|
| `core/xyool-execution.flow.md` | ACTIVE | Top-level Floware execution loop |
| `core/conversation.flow.md` | ACTIVE | Low-orchestration conversation |
| `core/research.flow.md` | ACTIVE | Evidence-efficient research |
| `core/development.flow.md` | ACTIVE | Floware-first capability development |
| `core/execution.flow.md` | ACTIVE | Authorized operational execution |
| `core/goalpost.flow.md` | ACTIVE | Freeze/maintain/close goals without drift |
| `core/evidence-to-state.flow.md` | ACTIVE | Convert evidence into auditable state |
| `core/domain-establishment.flow.md` | CANDIDATE / VERIFICATION_PENDING | Establish domain-native foundation and per-function readiness before Meta configuration |
| `core/domain-library.flow.md` | CANDIDATE / VERIFICATION_PENDING | Reuse and maintain source-traceable domain knowledge before repeating external research |
| `core/observation-trigger.flow.md` | CANDIDATE / VERIFICATION_PENDING | Decide whether a new observation, due condition, or resolved outcome should be ignored, recorded, queued, or trigger Xyool work |
| `core/resource-allocation.flow.md` | CANDIDATE / VERIFICATION_PENDING | Select the bounded active work set under finite attention/resources before Sequencing governs operational order |
| `core/direct-resolution.flow.md` | ACTIVE | Find the simplest workable answer before escalating proof |
| `core/question-frontier.flow.md` | ACTIVE | Improve weak questions until workable result or real bottleneck |
| `core/software-escalation.flow.md` | ACTIVE | Decide whether software is actually necessary |
| `core/learning.flow.md` | ACTIVE | Outcome → audit → lesson → flow improvement |
| `core/user-concept-memory.flow.md` | ACTIVE | Preserve user-originated concepts, rationale, and intellectual continuity |
| `core/correspondence.flow.md` | ACTIVE | Transfer structure across domains without forced mappings |
| `core/meaning-attribution.flow.md` | CANDIDATE / VERIFICATION_PENDING | Represent intrinsic/extrinsic/composite meaning with provenance and claim-mode boundaries |
| `core/novelty-enhancer.flow.md` | CANDIDATE / VERIFICATION_PENDING | Generate structurally novel creative/development candidates without altering evidence authority |
| `core/character-system.flow.md` | ACTIVE | Build reusable evidence-backed character profiles with quantitative/qualitative traits, non-exclusive archetypes, behavior signatures, and transformations |
| `core/story-reader.flow.md` | ACTIVE | Reconstruct past-to-present causal story state from evidence without writing the future |
| `core/story-writer.flow.md` | ACTIVE | Generate auditable conditional future story branches from current state without inventing facts |
| `core/relational-story.flow.md` | ACTIVE | Orchestrate reusable root-relative character/relationship stories with memory, Reader/Writer separation, re-rooting, bounded expansion, and audit |
| `core/code-to-flow.flow.md` | RESEARCH / ACTIVE | Translate programming semantics into Floware correspondences |

## Meta flows

| Flow | Status | Purpose |
|---|---|---|
| `meta/pipeline-integrity.flow.md` | ACTIVE / CANONICAL COMPOSITE | Coordinate end-to-end integrity across multi-Flow pipelines; current candidate extension also routes material Failure classification and lifecycle Promotion when applicable |

### Primitive Meta Flows

| Flow | Status | Purpose |
|---|---|---|
| `meta/mapping.flow.md` | ACTIVE | Map source and target representations explicitly while preserving invariants and exposing transformation, loss, ambiguity, and incompatibility |
| `meta/domain-configurer.flow.md` | ACTIVE | Configure a domain to use Floware by binding local semantics and specialized adapters to general contracts through explicit mappings |
| `meta/audit.flow.md` | ACTIVE | Independently audit Flow, pipeline/handoff, mapping, configuration, sequencing, patch, state, provenance, boundary, and learning integrity without silently rewriting the audited contract |
| `meta/patching.flow.md` | ACTIVE | Turn one authorized change into a complete dependency-aware patch set and prevent partial updates from being declared complete |
| `meta/sequencing.flow.md` | ACTIVE | Control dependency-safe order of operations, parallel readiness, barriers, re-entry, and fail-closed sequencing across composed Flows |
| `meta/failure.flow.md` | CANDIDATE / VERIFICATION_PENDING | Classify material failures, assign the correct response owner/disposition, and preserve re-entry/learning evidence without repairing the target |
| `meta/promotion-lifecycle.flow.md` | CANDIDATE / VERIFICATION_PENDING | Govern evidence-backed promotion, demotion, retirement, supersession, and rollback without replacing Evaluation, Audit, or Patching |

## Active domain flows

### stock-market

| Flow | Status | Purpose |
|---|---|---|
| `domains/stock-market/flows/company-analysis.flow.md` | ACTIVE | Floware wrapper for mandatory stock analysis |
| `domains/stock-market/flows/discovery-visibility.flow.md` | CANDIDATE / VERIFICATION_PENDING | Preserve research visibility for established-quality and hidden-transition candidates before Quality capital eligibility |
| `domains/stock-market/flows/story-sourcing.flow.md` | ACTIVE | Source parent and recursive stock characters using claim-specific evidence authority |
| `domains/stock-market/flows/story-memory.flow.md` | ACTIVE | Persist completed stock stories and resume future runs from delta refreshes |
| `domains/stock-market/flows/character-memory-reroot.flow.md` | ACTIVE | Persist reusable character-local webs and re-root any material entity as the main research character |
| `domains/stock-market/flows/quality-credentials.flow.md` | ACTIVE | Screen stock credentials, potential, unlock and survival before deeper thesis work |
| `domains/stock-market/flows/character-influence.flow.md` | ACTIVE | Map material characters and their causal transmission to shareholder value / price |
| `domains/stock-market/flows/recursive-character-story.flow.md` | ACTIVE | Recursively expand material characters and propagate nested consequences to the parent stock |
| `domains/stock-market/flows/narrative-thesis.flow.md` | ACTIVE | Map company connections into a causal story/thesis and miss audit |
| `domains/stock-market/flows/correspondence-rhythm.flow.md` | ACTIVE DEVELOPMENT | Derive catalyst rhythm from structurally corresponding processes |
| `domains/stock-market/flows/strategy-layer.flow.md` | ACTIVE DEVELOPMENT | Select strategy by story, state, horizon and trading job |
| `domains/stock-market/flows/ta-strategy.flow.md` | ACTIVE RESEARCH | TA/market-structure strategy family downstream of thesis/window |
| `domains/stock-market/flows/payoff-ranking.flow.md` | ACTIVE GOAL | Current frozen payoff-ranking development program |
| `domains/stock-market/flows/capital-path.flow.md` | ACTIVE DEVELOPMENT | Fixed-horizon path through pre-visible material information nodes |
| `domains/stock-market/flows/recurrent-process.flow.md` | ACTIVE DEVELOPMENT | Reason about continuing operating/economic processes inside the capital path |

## Authority

The registry routes execution. It does not grant capital, transaction, or external-action authority.

## Registration rule

A new major capability should be registered as a Flow before software is created for it.

If software becomes necessary, the corresponding Flow must state why in its Software / Hard-Limit Boundary.

## Repository contracts

- `REPOSITORY-MAP.md` — directory authority and precedence.
- `SOFTWARE-BOUNDARY.md` — software exception policy.
- `MIGRATION.md` — incremental migration without a big-bang rewrite.
- `FLOW-CONTRACT.md` — required structure for new Flows.
- `DOMAIN-CONTRACT.md` — required native-domain/function establishment contract before configuration.
- `DOMAIN-LIBRARY-CONTRACT.md` — durable domain-knowledge reuse/provenance contract.
- `MEANING-CONTRACT.md` — intrinsic/extrinsic/composite meaning representation and authority contract.
- `PIPE-CONTRACT.md` — required semantic contract for material first-class Pipes and Plumbing.
- `core/PLUMBING.md` — candidate core attention/trigger/resource Pipes.
- `meta/PLUMBING.md` — canonical high-risk Meta Pipes.


### experimental domains

| Domain | Flow | Status |
|---|---|---|
| astrology | `domains/astrology/flows/rule-foundation.flow.md` | EXPERIMENTAL / DOMAIN-LOCAL ESTABLISHMENT HELPER |
| astrology | `domains/astrology/flows/intrinsic-degree-foundation.flow.md` | EXPERIMENTAL / DEGREE-MEANING ESTABLISHMENT HELPER |
| astrology | `domains/astrology/flows/astrology-analysis.flow.md` | EXPERIMENTAL / FUNCTIONS_PARTIAL / CONFIGURATION VERIFICATION_PENDING |
| astrology | `domains/astrology/flows/predictive-astrology.flow.md` | EXPERIMENTAL / BLOCKED UNTIL ASTRO-FN-PREDICTIVE READY_FOR_CONFIGURATION |
| numerical-magic | `domains/numerical-magic/flows/numerical-analysis.flow.md` | EXPERIMENTAL / CURRENT SCOPE READY_FOR_CONFIGURATION / CONFIGURATION VERIFICATION_PENDING |

Experimental status limits claim authority, not Floware routing.

## Opt-in continuity candidates

Status: CANDIDATE / SPECIFIED / INDEPENDENT AUDIT PENDING. These entries grant no new authority and do not change default execution.

| Flow | Purpose |
|---|---|
| [Run Record](core/run-record.flow.md) | Capture evidence-linked checkpoints and verify storage receipts. |
| [Checkpoint Resume](core/checkpoint-resume.flow.md) | Reconcile checkpoint, current inputs and authority before re-entry. |
| [Evidence Refresh](core/evidence-refresh.flow.md) | Identify affected and retained outputs for existing Sequencing. |
| [Evaluation](core/evaluation.flow.md) | Govern frozen guided, blinded or isolated comparison experiments. |

Composition: [Continuity v1](continuity/PIPELINE.md). Connections: [Continuity Plumbing](continuity/PLUMBING.md).
