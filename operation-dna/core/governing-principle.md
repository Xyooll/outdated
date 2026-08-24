# Governing Principle: General Adaptive Operating System

Operation DNA is domain-independent. Trading, business building, research, product creation, marketing, finance, and operations are applications of the same adaptive architecture.

## Core loop

```text
Perceive → Understand → Hypothesize → Test → Act → Observe → Learn → Evolve
```

## Functional architecture

- **Mind:** AI reasoning, interpretation, hypothesis formation, planning, strategy.
- **Subconscious:** deterministic code, routines, calculations, validation, monitoring and execution.
- **Memory:** sensory, working, semantic, episodic and procedural experience.
- **Safety/Homeostasis:** protected invariants, permissions, limits, auditability, recovery and rollback.
- **Learning:** controlled experimentation, evaluation, promotion and rejection.
- **Evolution:** versioned behavioral improvement with lineage and reversible deployment.
- **Applications:** domain-specific implementations built on the common core.

## Applications

- `applications/trading/`
- `applications/business/`
- `applications/research/`
- `applications/product/`
- `applications/marketing/`
- `applications/finance/`
- `applications/operations/`

Applications may define domain-specific rules, but they must not bypass core safety, memory, provenance, or evolution controls.

## Architectural rule

The system is the organism; applications are organs. Infrastructure, plugins, AI providers, databases and geographic nodes are replaceable components.

The portable DNA must be sufficient to reconstruct the operating architecture in a new environment, with local configuration and separately provisioned secrets.
