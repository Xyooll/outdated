# ASTRO-LIB-STAR-DEGREE-V1

TYPE: OPEN QUESTION / USER-DERIVED DOMAIN FRAMEWORK
STATUS: **PARTIAL / RESEARCH**
SCOPE: exact-degree / stellar-field Astrology
LAST REVIEWED: 2026-09-25

## User concept

Treat the exact degree as an information-bearing astrological object in its own right.

Working name:
**Star Astrology**

## Candidate model

~~~text
PLANET / ANGLE / NODE / ASTEROID
→ EXACT DEGREE ADDRESS
→ LOCAL STELLAR NEIGHBORHOOD
→ SIGN / DECAN / HOUSE WRAPPERS
→ RULER / DISPOSITOR CONTEXT
→ ASPECT / PARAN / OTHER GEOMETRY
→ STORY AGGREGATION
~~~

## What is already grounded

Astronomically:
- ecliptic longitude is a precise coordinate;
- tropical zodiac degrees are longitude sectors measured from the equinox;
- fixed-star positions shift relative to tropical degrees mainly through precession;
- star longitude alone is incomplete because latitude/spatial geometry can matter.

Canonical pointers:
- `../../STAR-DEGREE.md`
- `../../SOURCE-REGISTRY.md#5c-star-astrology--degree-field-source-anchors`
- `../../SYSTEM-REGISTRY.md`
- `../../DEPENDENCY-GRAPH.md`

## What remains a hypothesis

- the degree itself has an intrinsic reusable symbolic meaning;
- a degree's stellar neighborhood explains part of that meaning;
- degree-level state adds predictive/descriptive information beyond sign/house/decan/aspect baselines.

## Required rule-foundation work

1. Freeze degree representation:
   - exact longitude;
   - integer-degree cell or another bin only if explicitly needed;
   - coordinate frame and epoch.

2. Freeze stellar-neighborhood rules:
   - star catalogue;
   - inclusion threshold;
   - longitude vs true-angular relationship;
   - latitude handling;
   - magnitude threshold if any;
   - proper-motion/epoch rule.

3. Establish intrinsic-degree meaning method:
   - sourced tradition if one is claimed;
   - otherwise explicit USER-DERIVED / XYOOL HYPOTHESIS;
   - one stable rule identity per meaning/version.

4. Establish combination rules:
   - degree vs star;
   - degree vs sign/decan;
   - degree vs house;
   - degree vs aspect;
   - degree vs asteroid/planet occupancy.

5. Run ablation:
   - categorical chart only;
   - + exact degree;
   - + star field;
   - + both;
   - + asteroids.

## Anti-overfitting constraints

- no adding stars after outcome review;
- no expanding degree/star orb after a miss;
- no treating every nearby star as meaningful;
- no counting degree/sign/decan/house labels as independent evidence when derived from the same longitude;
- no assigning a degree meaning from one case and validating it on that same case.

## Current readiness

~~~text
degree as first-class chart state
→ READY FOR MODELING

stellar-neighborhood calculation
→ PARTIAL

intrinsic degree interpretation
→ PARTIAL / USER-DERIVED

predictive Star Astrology
→ BLOCKED / REQUIRES RULE FOUNDATION + VALIDATION
~~~


## Deep Research progress — 2026-09-25

Now source-grounded:
- epoch/frame-aware degree-state requirement;
- JPL/Swiss/SOFA/Gaia/MPC calculation/source roles;
- Sabian corpus lineage as a distinct modern degree system;
- Ptolemaic fixed-star semantic seed;
- separate longitude vs spherical star-contact hypotheses;
- fixed-star catalogue manifest;
- search-space / dependency / ablation controls.

Still unresolved:
- intrinsic degree efficacy;
- winning star-contact geometry/orb;
- full star semantic corpus;
- predictive outcome translation;
- prospective incremental value.

Canonical new artifacts:
- ../../systems/ASTRO.STAR.DEGREE.XYOOL_V1.yaml
- ../../rules/star_degree_seed_v1.yaml
- ../../catalogs/fixed-stars/manifest.yaml
- ../knowledge/ablation-validation-a-e.md
