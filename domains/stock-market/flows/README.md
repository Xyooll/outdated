# Stock / Market Floware

Status: **ACTIVE DOMAIN FLOWARE**

The stock-market domain executes through Floware first.

Primary active flows:

- `company-analysis.flow.md` — full live stock analysis / mandatory gate routing.
- `discovery-visibility.flow.md` — research-visibility gate that unions established Quality candidates with evidence-backed hidden transitions before Quality capital eligibility.
- `story-sourcing.flow.md` — claim-specific source hierarchy and provenance for the parent and every material recursive character.
- `story-memory.flow.md` — persists the finished story and reloads it first so future runs refresh deltas instead of rebuilding.
- `character-memory-reroot.flow.md` — stores material entities as reusable characters and lets any character become a new main research root.
- `quality-credentials.flow.md` — simple upstream screen for company credentials, potential, trajectory, unlock and survival.
- `narrative-thesis.flow.md` — converts mapped evidence/connections into the causal company story and thesis.
- `character-influence.flow.md` — maps every material character, builds qualitative/quantitative profiles and archetype hypotheses, and traces causal paths to shareholder value and price.
- `recursive-character-story.flow.md` — expands material characters into their own nested stories and propagates relevant consequences back to the parent stock.
- `correspondence-rhythm.flow.md` — derives conditional catalyst timing from structurally corresponding processes/protocols.
- `strategy-layer.flow.md` — selects the trading strategy that fits the story, state, horizon, and job.
- `ta-strategy.flow.md` — TA/market-structure strategy family used downstream of thesis/window.
- `payoff-ranking.flow.md` — current frozen development goal.
- `capital-path.flow.md` — represents fixed-horizon payoff as a path through pre-visible material information nodes.
- `recurrent-process.flow.md` — local payoff Flow for continuing operating/economic processes.
- future capital-sizing flow — **NOT OPEN** until payoff-ranking goalpost is achieved.

The stock-domain skill files remain evidence models, methods, taxonomies, and supporting doctrine. They are loaded by flows as needed.

Software is subordinate:
- use it for exact calculations, persistence, market-data interfaces, hard risk limits, or external execution boundaries;
- do not encode new reasoning logic into software unless `floware/core/software-escalation.flow.md` justifies it.

Canonical Flow contract:
`floware/FLOW-CONTRACT.md`


## Relational Story specialization

The stock story architecture is a domain configuration of:

`../../../floware/core/relational-story.flow.md`

Supporting core Flows:
- `../../../floware/core/character-system.flow.md`
- `../../../floware/core/story-reader.flow.md`
- `../../../floware/core/story-writer.flow.md`

Stock-local archetype vocabulary:
- `../CHARACTER-ARCHETYPES.md`

Stock-specific specialization currently supplies:

```text
ROOT
company / security / material company character

CHARACTERS
subsidiaries, customers, partners, JVs, regulators,
financiers, suppliers, insiders, acquisition targets, etc.

CHARACTER PROFILE
quantitative traits + evidence-backed qualitative traits
+ non-exclusive dynamic archetype hypotheses

STORY READER
past → present causal reconstruction

STORY WRITER
evidence-bounded conditional future branches; no invented facts

PROPAGATION TARGET
company economics
→ shareholder capture
→ market recognition / price

SOURCE AUTHORITY
filings, contracts, regulators, counterparties, issuer sources,
then high-quality secondary evidence

RESOURCE HORIZON
max absolute degree = 4
policy reason = RESOURCE_BOUND

ROOT-SPECIFIC OUTPUT
story
→ thesis
→ rhythm / window
→ payoff
→ strategy
```

The stock domain may add stricter rules but may not weaken the core requirements for reusable character identity, relationship continuity, provenance, memory, or audit.
