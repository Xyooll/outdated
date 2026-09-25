# Xyool Floware Glossary

Status: **CANONICAL TERMINOLOGY**

## Glossary definition policy

Canonical glossary entries are **semantic contracts**, not merely short dictionary definitions.

Their job is to preserve enough meaning that a future reader, Flow, model, or implementation can recover:
- what the concept is;
- what it contains;
- what it does;
- what it does not do;
- how it relates to neighboring concepts;
- what invariants must be preserved;
- what common confusions must be avoided;
- how the concept behaves when composed with the rest of Floware.

Definitions may therefore be as long as necessary.

A concise **Short form** may be included for navigation, recall, or conversation, but it is only a mnemonic. It must never replace, narrow, or override the full canonical definition.

Core rule:

> **Compress for recall, not for authority. Preserve the full meaning in the canonical definition.**

If a shorter explanation omits a material boundary or relationship, the full glossary entry controls.

## Floware

**Floware** is the canonical name and spelling for Xyool's AI-native reasoning and execution architecture.

Floware organizes adaptive intelligence as explicit **Flows**, connects those Flows through governed **Pipes**, composes them into **Pipelines**, and preserves the state, evidence, memory, provenance, authority, timing, learning, goalposts, boundaries, and Meta-level governance required for those compositions to remain reliable over time.

Floware is not merely a collection of prompts, documents, procedures, or software modules.

It is the architecture that specifies:
- what reasoning/work unit is responsible for a job;
- what state/evidence that unit is allowed to consume;
- what output it produces;
- what constraints and gates it must preserve;
- how outputs move safely into other units;
- how multiple units compose toward a larger objective;
- how state/version/provenance continuity survives those compositions;
- how failures, invalidations, re-entry, learning, patching, and audit are handled;
- where deterministic software is required for certainty rather than intelligence.

Its principal native ontology includes:

```text
FLOW
= a goal-directed reasoning / processing unit

PIPE
= a governed connection between Flows

PIPELINE
= a connected graph of Flows and Pipes toward a shared objective / terminal state

PLUMBING
= the collective Pipe structure and connection logic of Floware
```

Floware also includes the supporting structures that make those objects dependable:
- state;
- evidence and provenance;
- memory;
- goalposts;
- authority boundaries;
- domain configuration;
- mapping;
- sequencing;
- patching;
- audit;
- learning;
- correspondence;
- software/hard-limit boundaries.

The older description of Floware as “Flows plus state, evidence, goalposts, learning, routing, and software boundaries” remains conceptually contained inside this definition. The newer ontology makes the previously implicit connection/composition layer explicit through Pipes, Pipelines, and Plumbing.

### Relationship to software

Floware is not synonymous with software.

Canonical law:

> **Use Floware for intelligence. Use software for certainty.**

Floware should express adaptive reasoning, interpretation, composition, and governance first. Deterministic software may implement or enforce hard requirements such as exact arithmetic, persistence, schema validation, transactions, locks, security, scheduling, or physical limits when Floware alone is insufficient.

Software may support Floware, but software must not silently become the architecture.

### Canonical spelling

```text
Floware
```

Do **not** normalize it to `Flowware`.

Speech-to-text may transcribe the spoken word as “Flowware.” When the user is referring to this Xyool architecture, interpret and write it as **Floware** unless the context clearly indicates a different ordinary term.

### Short form — mnemonic only

> **Floware is the architecture in which Flows do the work, Pipes connect the work, and Pipelines compose the work while preserving state and integrity.**

## Flow

A **Flow** is the primary AI-native executable reasoning unit in Xyool.

A Flow defines:
- goal;
- goalpost;
- input state;
- evidence;
- adaptive process;
- gates;
- boundaries;
- fail-closed conditions;
- output state;
- learning hook;
- software/hard-limit boundary.

Short form:

> **A Flow is a goal-directed, state-aware, evidence-bounded path that AI can adapt while preserving its constraints and completion conditions.**

The Flow is the program.

## Meta Flow

A **Meta Flow** is a general Flow whose primary object is the configuration, composition, validation, routing, or governance of other Flows or domain-to-Flow mappings rather than the direct resolution of a domain-native problem.

A Meta Flow can:
- determine which Flow contracts a domain must satisfy;
- map domain-native structures into reusable Floware structures;
- select or bind compatible adapters and supporting Flows;
- detect missing capabilities or invalid mappings;
- validate that a composed Flow preserves canonical invariants;
- route the resulting configuration into execution, memory, audit, learning, and correspondence layers.

Short form:

> **A Meta Flow operates on the structure and use of Flows so that domain-specific reality can enter Floware without contaminating its general contracts.**

A Meta Flow is still a Flow and must satisfy the normal Flow contract.

Meta status describes **architectural level**, not importance or authority.

A Meta Flow must not silently import domain-specific semantics into a core contract. Domain-specific meaning remains in the domain or its configuration.

Example:

```text
DOMAIN
→ DOMAIN CONFIGURER META FLOW
→ VALIDATED DOMAIN-TO-FLOWARE MAPPING
→ CORE / GENERAL FLOWS
→ DOMAIN EXECUTION
```

The **Domain Configurer** is a Meta Flow.

Canonical primitive Meta Flows currently include **Mapping**, **Domain Configurer**, **Sequencing**, **Patching**, and **Audit**. The canonical composite integrity layer is **Pipeline Integrity**.

## Pipe

A **Pipe** is a first-class governed connection between one Flow and another Flow, or between compatible stages inside a composed Floware structure.

Its purpose is not merely to transport output.

A Pipe defines the conditions under which something produced or established upstream may safely become something consumed, interpreted, authorized, or acted upon downstream.

Conceptually:

```text
UPSTREAM FLOW
      ↓
     PIPE
      ↓
DOWNSTREAM FLOW
```

A valid Pipe preserves every material property required by the downstream contract.

Depending on the connection, that can include:
- identity;
- state;
- evidence;
- provenance/source lineage;
- semantic meaning;
- units/scales;
- time/as-of state;
- version;
- uncertainty/confidence;
- authority/permission;
- readiness;
- gate status;
- invalidation state;
- transformation/mapping;
- failure behavior;
- re-entry conditions.

A Pipe may transport information, but it may also constrain or propagate **control**.

For example, a Pipe may communicate:

```text
DATA / STATE
EVIDENCE / PROVENANCE
AUTHORITY
READINESS
BLOCKED / FAIL
INVALIDATION
VERSION CHANGE
CONTROL / GATE STATE
```

Those are not automatically different architectural objects. They are different properties or jobs of a Pipe unless repeated evidence later justifies specialized Pipe classes.

### Canonical representation — Pointers + Wrapper + live state

A Pipe should normally be represented as:

```text
PIPE
=
ENDPOINT POINTERS
+
CONNECTION WRAPPER
+
LIVE PIPE STATE
```

The **Pointers** identify the canonical endpoints without copying them.

The **Wrapper** contains the relationship-specific rules that govern how those endpoints may connect.

The **live Pipe state** records current compatibility/readiness/version/invalidation information without redefining the durable relationship.

This reuses the same architectural idea already present in Relational Story: pointers reference reusable canonical state, while wrappers preserve the context-specific meaning/rules around that state.

A Pointer alone is not a Pipe.

A Wrapper alone is not a Pipe.

The Pipe is the governed connection formed by the endpoint references plus the relationship contract and, when needed, its current operational state.

Canonical contract:
`PIPE-CONTRACT.md`

### Pipe contract

A material Pipe should be understandable in terms of:

```text
PIPE ID
FROM FLOW / STAGE
TO FLOW / STAGE

SOURCE OUTPUT / STATE
TARGET INPUT / STATE

REQUIRED MAPPING / TRANSFORMATION
SEMANTIC INVARIANTS
PROVENANCE REQUIREMENTS
FRESHNESS / AS-OF REQUIREMENTS
VERSION REQUIREMENTS
UNCERTAINTY PRESERVATION
AUTHORITY IN / AUTHORITY OUT
GATE / CONDITION
LOSS / COMPRESSION
FAILURE BEHAVIOR
INVALIDATION / RE-ENTRY BEHAVIOR
AUDIT STATUS
```

Not every Pipe needs every field explicitly materialized. The contract should preserve whatever is materially necessary for that connection.

### Pipe integrity

Two individually correct Flows do not guarantee a correct Pipe.

Example:

```text
Story Writer output:
confidence = HIGH

Payoff input:
P(Hit) = numeric probability
```

A Pipe that silently converts:

```text
HIGH → 0.80
```

without an earned Mapping/calibration is invalid even if both endpoint Flows are individually valid.

Therefore:

> **Flow correctness does not imply Pipe correctness.**

A Pipe is valid only when the downstream interpretation remains justified by the upstream meaning and the governing Mapping/domain contracts.

### Mapping relationship

**Mapping** answers how two representations correspond.

A **Pipe** operationalizes a governed connection between endpoints.

Mapping may define part of a Pipe's transformation contract, but Mapping is not itself the Pipe.

### Authority rule

A Pipe may preserve or reduce authority according to contract, but it may not silently increase authority.

For example:

```text
ANALYSIS AUTHORITY
→ Pipe
→ EXECUTION AUTHORITY
```

is invalid unless an explicit downstream authority contract grants the transition.

### Short form — mnemonic only

> **Flows do the work. Pipes connect the Flows while preserving the meaning and constraints required for the connection to remain valid.**

## Pointer

A **Pointer** is a reference to canonical reusable state or a canonical architectural object.

A Pointer answers:

> **Where is the underlying thing?**

A Pointer may identify:
- a Flow;
- a Flow input/output;
- state;
- evidence;
- memory;
- a Character;
- a relationship;
- a Mapping;
- a schema/contract;
- another Pipe;
- another canonical object.

Pointers prevent duplication and allow multiple contexts to refer to the same underlying object.

A Pointer does not itself define how the referenced object should be interpreted or used.

That is the role of the surrounding contract or Wrapper.

## Wrapper

A **Wrapper** is a context-specific contract around one or more referenced canonical objects.

A Wrapper answers:

> **What does this referenced object/relationship mean here, and what rules govern its use in this context?**

A Wrapper may preserve:
- role/context;
- transformation;
- allowed interpretation;
- materiality;
- authority;
- gate conditions;
- provenance requirements;
- failure behavior;
- invalidation/re-entry behavior.

A Wrapper must not redefine the underlying canonical object.

In Pipes:

```text
POINTERS
= where the source/target are

WRAPPER
= how the relationship between them is governed
```

This is the same general architectural pattern used by Relational Story wrappers around reusable Character/relationship state.

## Pipeline

A **Pipeline** is a goal-directed composition of Flows connected by Pipes, with explicit entry conditions, dependency/order constraints, gates/barriers, state/version continuity, and terminal conditions.

A Pipeline is not required to be a single straight line.

It may be:
- linear;
- branching;
- converging;
- conditional;
- partially parallel;
- recursively re-entered through a new execution epoch;
- composed of core, Meta, and domain Flows.

Generic form:

```text
ENTRY
  ↓
FLOW A
 ├─PIPE→ FLOW B ─┐
 └─PIPE→ FLOW C ─┤
                 ↓
               FLOW D
                 ↓
              TERMINAL
```

A Pipeline exists to achieve an objective that is larger than the job of any one participating Flow.

Its integrity depends on:
- the correctness of required Flows;
- the correctness of required Pipes;
- valid ordering/prerequisites;
- valid barriers and merges;
- preserved state/version/provenance;
- preserved authority;
- valid failure/invalidation/re-entry behavior;
- satisfaction of terminal conditions.

Therefore:

> **Pipeline integrity is not the sum of local PASS states.**

A Pipeline can fail even when every local Flow reports PASS if a Pipe, ordering relation, state version, or authority transition is invalid.

### Pipeline identity

A material Pipeline should be capable of expressing:

```text
PIPELINE ID / VERSION
OBJECTIVE / GOALPOST
ENTRY CONDITIONS
FLOWS / STAGES
PIPES
SEQUENCING / DEPENDENCIES
STATE / VERSION HEAD
AUTHORITY BOUNDARY
FAILURE / RE-ENTRY RULES
TERMINAL CONDITIONS
AUDIT / INTEGRITY STATUS
```

### Pipeline vs workflow

Within Floware, **Pipeline** names the connected Flow/Pipe structure.

Do not use “workflow” as a synonym for a Floware Pipeline when that would collapse the distinction between AI-native adaptive architecture and conventional automation.

### Short form — mnemonic only

> **Pipeline = a goal-directed graph of Flows connected by Pipes under shared entry, sequencing, integrity, and terminal conditions.**

## Plumbing

**Plumbing** is the collective connection structure formed by Pipes inside Floware.

If Flows are the units that perform reasoning/work, Plumbing is the architecture that determines how those units are connected well enough to behave as a coherent larger system.

Plumbing includes:
- topology — which Flows connect to which;
- Pipe contracts;
- endpoint compatibility;
- Mapping/transformation requirements;
- sequencing dependencies;
- gates and barriers;
- branching and merge behavior;
- shared-state coordination;
- state/version continuity;
- evidence/provenance continuity;
- uncertainty preservation;
- authority continuity;
- failure propagation;
- invalidation;
- re-entry;
- rollback/recovery where applicable.

Plumbing is broader than any single Pipe but narrower than Floware as a whole.

Conceptually:

```text
FLOWARE
├─ Flows        = work/reasoning units
├─ Plumbing     = connection structure
│   └─ Pipes    = individual governed connections
├─ Pipelines    = goal-directed compositions of Flows + Pipes
├─ State / Evidence / Memory
└─ Meta governance / Learning / Boundaries
```

Good Plumbing allows Floware to preserve meaning and integrity as work moves across multiple Flows.

Bad Plumbing can make individually valid Flows produce an invalid system.

Examples of Plumbing failures include:
- connecting semantically incompatible outputs/inputs;
- losing provenance between stages;
- using stale state/version downstream;
- widening authority without permission;
- creating hidden cycles/deadlocks;
- merging branches before required barriers complete;
- failing to propagate invalidation;
- patching one endpoint without updating affected Pipes.

### Relationship to Pipeline Integrity

Pipeline Integrity evaluates the end-to-end composition.

Plumbing is the connection structure being evaluated.

Pipeline Integrity therefore asks not only:

```text
Are the Flows valid?
```

but also:

```text
Is the Plumbing valid?
Are the Pipes valid?
Does the connected Pipeline preserve its contracts end to end?
```

### Short form — mnemonic only

> **Plumbing is the governed connection structure that lets Flows function together without losing meaning, state, provenance, authority, or integrity.**

## Pipeline Integrity

**Pipeline Integrity** is the composite Meta Flow that coordinates end-to-end integrity across a multi-Flow pipeline.

Short form:

> **Pipeline Integrity asks whether the whole pipeline is valid, not merely whether each stage passed locally.**

It coordinates Mapping, Domain Configurer, Sequencing, Patching, and independent Audit as applicable.

Canonical Flow:
`meta/pipeline-integrity.flow.md`

Core rule:

> **A pipeline is only as valid as its weakest required Pipe.**

A local PASS does not automatically become a pipeline PASS.

## Mapping

**Mapping** is the explicit process of aligning a source representation with a target representation while preserving named invariants and exposing transformations, ambiguity, incompatibility, unmapped components, and information loss.

Short form:

> **Mapping asks: how does representation A line up with representation B?**

Mapping does not establish causal or empirical transfer. That is the job of Correspondence when knowledge is moving across domains.

Canonical Mapping Meta Flow:
`meta/mapping.flow.md`

## Domain Configurer

The **Domain Configurer** is the Meta Flow that determines how a domain uses Floware. It selects applicable general contracts, consumes explicit mappings, binds domain-local semantics, identifies specialized adapters and hard-limit support, exposes missing capabilities, and produces an auditable domain configuration.

Short form:

> **The Domain Configurer makes a domain fit Floware without making Floware become that domain.**

Canonical Domain Configurer Meta Flow:
`meta/domain-configurer.flow.md`

A specialized adapter may translate a particular native system, API, calculation, or format. The Domain Configurer governs the domain-level composition and must not be replaced conceptually by one monolithic "Domain Adapter."

## Sequencing

**Sequencing** is the Meta Flow that determines the dependency-safe order of operations across composed Flows.

Short form:

> **Sequencing asks: what is ready now, what must wait, and what can run in parallel?**

Sequencing uses prerequisites, gates, state dependencies, authority constraints, barriers, and shared-state conflicts to build a partial order rather than blindly enforcing one rigid list.

Canonical Sequencing Meta Flow:
`meta/sequencing.flow.md`

Core rules:

> **Order follows dependency, not convenience.**

> **Do not serialize independent work, and do not parallelize dependent work.**

Sequencing does not choose the goal or decide domain truth. Xyool Execution selects/routs work; Sequencing controls operational precedence.

## Patching

**Patching** is the Meta Flow that propagates one authorized change across every materially dependent representation of that change.

Short form:

> **Patching asks: if this changes here, what else must change with it?**

Patching builds an impact graph, assigns every affected surface a disposition, applies the complete patch set, and refuses to call a multi-surface update complete while material dependencies remain unresolved.

Canonical Patching Meta Flow:
`meta/patching.flow.md`

Core rules:

> **Change the concept once; patch every materially dependent representation.**

> **Patch the present contract; preserve the evidence of the past.**

Patching does not decide whether the underlying architectural idea is good. Development/Learning supplies the authorized change. Mapping handles representation alignment. Domain Configurer handles domain composition. Audit independently checks completeness.

## Audit

An **Audit** is an independent integrity evaluation of a Flow, Meta Flow, mapping, domain configuration, state transition, evidence/provenance chain, output, or learning change against the governing contract and evidence.

Short form:

> **Audit asks whether the system preserved what it said it would preserve.**

A local Flow may self-check during execution. A **Meta Audit** evaluates the object from outside its own execution path when independence or cross-layer integrity matters.

Canonical Meta Audit:
`meta/audit.flow.md`

Core rule:

> **The auditor may inspect the contract, but it may not silently redefine the contract it is auditing.**

Audit may PASS, WARN, FAIL, or BLOCK. It does not silently repair the audited object; remediation belongs to the responsible Flow or Meta Flow.

## Character

A **Character** is a reusable state-bearing entity that can participate in relationships, change over time, and appear in multiple root-relative stories.

Character identity is separate from its story role.

## Archetype

An **Archetype** is an evidence-backed hypothesis that a character expresses a recurring structural or behavioral pattern.

Archetypes are non-exclusive, dynamic, domain-local by default, and optional. A character may remain UNCLASSIFIED or EMERGENT.

Core rule:

> **The archetype must fit the evidence; the evidence must never be forced to fit the archetype.**

Canonical Character System:
`core/character-system.flow.md`

## Story Reader

The **Story Reader** reconstructs how past evidence, character changes, relationship changes, and state transitions produced the current state.

Short form:

> **Reader: past → present.**

Canonical Flow:
`core/story-reader.flow.md`

## Story Writer

The **Story Writer** constructs conditional future branches from the evidence-backed current state.

It generates hypotheses, not facts.

Short form:

> **Writer: present → possible futures.**

Canonical Flow:
`core/story-writer.flow.md`

## Workflow

Within Xyool, avoid **workflow** when referring to an AI-native reasoning process.

Use **Flow** instead.

Reserve **workflow** for conventional automation systems where the term is native or useful, for example:
- GitHub Actions workflows;
- third-party workflow engines;
- external automation products.

Naming rule:

```text
AI-NATIVE ADAPTIVE PROCESS → FLOW
CONVENTIONAL AUTOMATION PIPELINE → WORKFLOW
```

Do not mechanically rename third-party product/API terms when doing so would reduce clarity.

## User Concept

A **User Concept** is a material idea, belief, hypothesis, philosophy, design intuition, naming choice, rationale, or worldview expressed by the user that may matter to future understanding.

User Concepts are preserved separately from Xyool's derived interpretation.

## Thought Ledger

The **Thought Ledger** is the append-oriented, human-readable history of User Concepts.

Its purpose is not only operational memory.

It should also make it possible for a future reader to understand:
- what the user believed;
- why the user believed it;
- how the idea developed;
- how it influenced Xyool;
- what was still uncertain;
- what later evidence changed.

## Memory distinction

```text
USER CONCEPT MEMORY
= human ideas / rationale / philosophy / intent

DOMAIN STATE
= current modeled state of an external domain

RESEARCH MEMORY
= experiments / evidence / outcomes / failures

SOFTWARE MEMORY
= application/session persistence
```

Do not collapse these into one layer.


## Correspondence Beam

A **Correspondence Beam** is a structural line connecting a live object/process to one or more analogs that share the mechanism relevant to the current question.

For timing questions:

```text
LIVE PROCESS STATE
→ STRUCTURAL CORRESPONDENCE
→ COMPLETED ANALOG PROCESS
→ OBSERVED TRANSITION TIMING
→ LIVE RHYTHM ESTIMATE
```

A strong beam shares the causal mechanism that determines the outcome or timing.

A weak beam shares only superficial resemblance.

## Rhythm

**Rhythm** is the observed cadence of state transitions inside a process.

In the stock domain, rhythm is usually expressed as:
- dwell time between process states;
- common delay points;
- fast/normal/slow paths;
- calendar or budget cadence;
- conditional event windows.

Rhythm is conditional evidence, not a deterministic forecast.


## Canonical System Lineage

The **Canonical System Lineage** is the single integrated Git lineage that answers:

> **What is Xyool now?**

Canonical branch:
`main`

A newer or more specialized branch does not become system authority merely by containing later work.

Branch-local changes remain proposals until reconciled into `main`.

Scoped subordinate lineages may exist only when `SYSTEM-LINEAGE.md` explicitly names their bounded authority. The current example is `lineage/user-concepts`, authoritative only for `memory/user-concepts/`.

Core rule:

> **Branches may diverge in work. Authority may not diverge in meaning.**
