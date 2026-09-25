# ASTRO-LIB-FULL-CHART-V2

TYPE: OPEN QUESTION / DOMAIN UPDATE
STATUS: **PARTIAL / IN DEVELOPMENT**
SCOPE: Western Tropical whole-chart Story aggregation
LAST REVIEWED: 2026-09-25

## Trigger

The first forecast over-selected a small set of signals and underused the natal house structure.

The requested direction is a fuller chart aggregation including houses and a bounded asteroid layer.

## Proposed architecture

~~~text
NATAL CHART STATE
→ preserve exact degree for every planet / angle / node / asteroid
→ attach local stellar neighborhood where Star Astrology is enabled
→ sign / decan wrappers provide zodiacal context
→ houses establish primary life-area / capture context
→ house rulers / dispositors link chart areas
→ natal aspects establish interaction pattern
→ nodes / bounded asteroid/centaur set add separately weighted modifiers
→ profections / transits / timers activate degree nodes and house networks
→ aggregate by degree + house + ruler + natal target + timing + reinforcement
→ Story Reader / Writer
~~~

## Signal hierarchy candidate

Primary:
- Ascendant / MC / angles;
- Sun, Moon, Mercury, Venus, Mars, Jupiter, Saturn;
- Uranus, Neptune, Pluto where the selected Western system includes them;
- all twelve houses;
- house rulers/dispositors;
- major natal aspects.

Secondary / bounded:
- lunar nodes;
- Chiron;
- Ceres;
- Pallas;
- Juno;
- Vesta;
- selected additional centaurs/asteroids only when preregistered.

## Anti-overfitting rule candidate

Asteroids should not create a primary forecast theme by themselves in v2.

They may:
- reinforce;
- narrow;
- contradict;
- localize

an already-established house/planet/angle story when tightly configured.

The asteroid set and orbs must be frozen before analysis.

## Existing source pointers

- `../../SOURCE-REGISTRY.md#5b-full-chart--asteroid-source-anchors`
- `../../SOURCE-REGISTRY.md`
- `../../RULE-REGISTRY.md`

## Missing work

- establish house-ruler/dispositor rules;
- establish whole-chart aggregation rule;
- freeze asteroid object set;
- freeze asteroid aspect/orb policy;
- establish asteroid meanings with provenance;
- define weighting/priority without opaque master score;
- create `ASTRO.WT.XYOOL_STORY_V2` only after the above is explicit;
- validate whether added objects improve discrimination or merely increase match opportunities.

## Current status

This is a domain-library open question/update record, not an established v2 ruleset.


## Degree-first refinement

The full-chart model now treats exact longitude as the atomic state object.

This does **not** demote houses.

Use:

~~~text
DEGREE
= precise atomic address

HOUSE
= primary life-area / capture wrapper

SIGN / DECAN
= zodiacal context wrappers

STAR FIELD
= astronomical neighborhood around the degree

PLANET / ANGLE / ASTEROID
= occupant / activator

ASPECT / RULERSHIP
= relationship structure
~~~

Canonical research entry:
`star-degree-astrology-v1.md`

Before v2 can be established, the aggregation rules must specify how degree-level information combines with house/ruler/aspect state without double-counting the same underlying longitude.


## Deep Research progress — 2026-09-25

Now specified:
- degree-node graph architecture;
- house-as-capture / degree-as-address distinction;
- ruler/dispositor and aspect edge model;
- epoch-specific stellar-neighborhood layer;
- bounded minor-body tiers;
- v1→v2 immutable migration;
- A→E ablation plan;
- dependency and search-space controls.

Still partial:
- complete house/rulership/planet-condition v2 rule corpus;
- full asteroid semantics and validated orbs;
- narrow outcome mappings for Story Writer;
- prospective incremental validation.

Canonical target:
../../systems/ASTRO.WT.XYOOL_STORY_V2_DEGREE_NODE.yaml
