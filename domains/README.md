# Xyool Domains

This directory contains Xyool domain definitions, domain Flows, domain state, and specialized adapters where needed.

Xyool's reusable reasoning architecture lives above any single domain. Core Domain Establishment (`floware/core/domain-establishment.flow.md`) first establishes the domain-native foundation and material functions. Only then does the Domain Configurer Meta Flow (`floware/meta/domain-configurer.flow.md`) use explicit Mapping (`floware/meta/mapping.flow.md`) to bind that established scope to applicable Floware contracts. Specialized adapters remain narrower interfaces for native calculations, APIs, formats, or system-specific normalization.

## Floware requirement

Floware is now the primary operating substrate.

Active domains should expose:

```text
domains/<domain>/
  DOMAIN.md
  flows/
    README.md
    <job>.flow.md
  library/            reusable domain knowledge/memory
  STATE.md / state/   when persistent state is required
```

`DOMAIN.md` defines what the domain means.
`library/` preserves reusable source-traceable domain knowledge and points to canonical rules/evidence.
`flows/` defines how AI operates inside the domain.
Skills provide methods used by those Flows.
Software supports only justified deterministic needs.

Before creating a new domain or materially adding a domain function, use:
- `floware/DOMAIN-CONTRACT.md`
- `floware/core/domain-establishment.flow.md`

Only after the claimed scope is `READY_FOR_CONFIGURATION`, use:
- `floware/meta/domain-configurer.flow.md`
- `floware/meta/mapping.flow.md`
- `floware/meta/audit.flow.md` when independent integrity is required.

Before adding domain software, use:
`floware/core/software-escalation.flow.md`

Before creating or modifying a domain, read:

- `skills/xyool/00-03-META-ARCHITECTURE-PRIMER.md`
- `skills/xyool/00-04-DOMAIN-CORRESPONDENCE-HOWTO.md`
- `skills/xyool/00-02-DOMAIN-CORRESPONDENCE-ARCHITECTURE.md`

Current active domain:

- `stock-market/` — active development and validation domain.

Persistent operational domains should also define a `STATE.md` contract and a durable state backend/index. The canonical persistence rules are in `skills/xyool/domain-state-persistence.md`. Live-object work should load stored domain state first and refresh only missing/stale/due evidence.

Registered experimental domains:

- `astrology/` — multi-system astrology adapter with calculation/interpretation separation, mandatory run sequence, controlled validation, system identity registry, rule versioning, capability translation, Tuner compression, and explicit Maya/Dreamspell separation. It remains experimental until its validation suites are executed.
- `numerical-magic/` — symbolic numerical-language adapter with a deterministic arithmetic core, full reduction-chain preservation, ordered-path semantics, root-family ladders, Pythagorean letter carriers, local glyph extensions, reverse-engineering grammar, and explicit separation between symbolic convention and empirical efficacy claims.

Primary astrology Floware:
- `astrology/ESTABLISHMENT.md`
- `astrology/flows/astrology-analysis.flow.md`
- `astrology/CONFIGURATION.md`
- `astrology/PLUMBING.md`

Primary astrology supporting files:

- `astrology/DOMAIN.md`
- `astrology/RUN-SEQUENCE.md`
- `astrology/VALIDATION.md`
- `astrology/SYSTEM-REGISTRY.md`
- `astrology/RULE-REGISTRY.md`
- `astrology/SIGNAL-OUTPUT-MODEL.md`
- `astrology/MAYA.md`

Current astrology system families include Western tropical/traditional, Western sidereal, Jyotish/Vedic, fixed-star/stellar, heliocentric research, traditional/living Maya calendrical systems, and Dreamspell as a separate modern system.

The astrology output architecture preserves the user's earlier capability-optimization and Tuner frameworks as downstream translation/compression layers rather than silently treating them as source-tradition astrology rules.

Primary numerical-magic Floware:
- `numerical-magic/ESTABLISHMENT.md`
- `numerical-magic/flows/numerical-analysis.flow.md`
- `numerical-magic/CONFIGURATION.md`
- `numerical-magic/PLUMBING.md`

Primary numerical-magic supporting files:

- `numerical-magic/DOMAIN.md`
- `numerical-magic/RUN-SEQUENCE.md`
- `numerical-magic/GRAMMAR.md`
- `numerical-magic/ROOT-REGISTRY.json`
- `numerical-magic/engine.py`
- `numerical-magic/VALIDATION.md`
- `numerical-magic/test_engine.py`

The numerical-magic domain treats arithmetic, carrier mappings, symbolic semantics, and real-world outcome claims as separate layers. Internal language consistency does not establish external causality.

Future domains belong under:

`domains/<domain-name>/`

Each new or materially expanded domain should first be established through the Core Domain Establishment Flow. Meta Domain Configurer only binds scopes that are `READY_FOR_CONFIGURATION`. Each new ACTIVE domain should contain at minimum:
- `DOMAIN.md`;
- `flows/README.md`;
- at least one registered primary Flow.

Each domain manifest must declare at minimum:

- objective;
- decision unit;
- entities;
- observable evidence;
- latent / hidden state;
- state transitions;
- gates;
- timers;
- actions;
- outcome/payoff definition;
- failure/loss definition;
- capture definition;
- recognition/response definition;
- source hierarchy;
- freshness standard;
- invalidation standard;
- validation method;
- anti-lookahead discipline;
- miss-handling method;
- domain-specific rules;
- imported principles and their correspondence status;
- calibrations that are explicitly local to the domain;
- persistent-state contract / backend when the domain maintains live objects;
- source freshness / cursor policy for delta fetching.

## Domain readiness

A new domain should not be marked ACTIVE until it has, at minimum:

```text
[ ] objective defined
[ ] claimed scope/functions inventoried
[ ] each required function has a native function contract
[ ] actual native rule/method coverage exists for each claimed function
[ ] reusable established knowledge is indexed in domain library
[ ] primary Flow(s) defined
[ ] Flow authority / boundaries defined
[ ] software boundary declared
[ ] entities defined
[ ] evidence hierarchy defined
[ ] state model defined
[ ] transition model defined
[ ] gates/timers defined where relevant
[ ] action authority defined
[ ] success/failure defined
[ ] freshness/invalidation rules defined
[ ] miss loop defined
[ ] imported principles labeled by validation status
[ ] local calibrations separated from core principles
[ ] at least one worked example
[ ] at least one negative/control example
[ ] Domain Establishment status is READY_FOR_CONFIGURATION for the claimed active scope
```

Until then use a status such as:

```text
DRAFT
EXPERIMENTAL
BLOCKED
```

Do not assume a principle validated in one domain is automatically valid in another.

Do not import numeric thresholds, timing windows, scores, or action rules from a source domain unless separately validated in the target domain.

See:

- `skills/xyool/00-03-META-ARCHITECTURE-PRIMER.md`
- `skills/xyool/00-04-DOMAIN-CORRESPONDENCE-HOWTO.md`
- `skills/xyool/00-02-DOMAIN-CORRESPONDENCE-ARCHITECTURE.md`
- `correspondence/README.md`

## Floware references

- `floware/README.md`
- `floware/FLOW-CONTRACT.md`
- `floware/REGISTRY.md`
- `floware/REPOSITORY-MAP.md`


## Domain knowledge reuse

Before broad external research, use:
- `floware/DOMAIN-LIBRARY-CONTRACT.md`
- `floware/core/domain-library.flow.md`

Preferred loop:

~~~text
existing domain library
→ relevant canonical rules / sources / validation / failure boundaries
→ identify only missing or stale knowledge
→ external research
→ establish/update canonical domain artifacts
→ distill reusable result back into library
~~~

A mature domain should require less repeated external research, while still refreshing dynamic facts and retaining original provenance.


## Experimental-domain configuration rule

For an experimental domain, a structurally complete Floware configuration does not imply empirical validation.

Keep separate:

~~~text
FLOWARE CONFIGURATION VALIDITY
≠
DOMAIN THEORY / PREDICTIVE EFFICACY
~~~

Architecture may become VALIDATED_FOR_SCOPE while the domain itself remains EXPERIMENTAL.

## Current establishment snapshot

- Astrology: **FUNCTIONS_PARTIAL**. Sourced Maya/Dreamspell interpretation and validation methodology are established; Western/Jyotish/stellar/predictive functions require further establishment.
- Numerical Magic: **READY_FOR_CONFIGURATION for the current arithmetic/symbolic/construction scope**; empirical efficacy remains outside that ready scope.
