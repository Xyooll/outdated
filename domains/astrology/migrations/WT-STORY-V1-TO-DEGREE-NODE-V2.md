# Western Story v1 → Degree-Node v2 Migration

STATUS: **CANDIDATE / DOMAIN UPDATE**

Do not mutate ASTRO.WT.XYOOL_STORY_V1 in place.

Target: ASTRO.WT.XYOOL_STORY_V2_DEGREE_NODE.

## Mapping

| V1 concept | V2 representation |
| --- | --- |
| natal planet | object attached to exact degree node |
| sign | categorical wrapper derived from degree node |
| whole-sign house | life-area/capture edge |
| house ruler | governance edge to ruler degree node |
| dispositor | governance edge from object/sign to ruler node |
| major aspect | typed edge between exact degree nodes |
| applying/exact/separating | dynamic edge state |
| transit | future degree node creating time-varying edge to natal node |
| annual profection | time-lord activation on house/sign/ruler network |
| fixed star | stellar-neighborhood edge, not a text label on the degree |
| asteroid | optional object node admitted only by frozen manifest |
| Story Reader | historical rule activations mapped to dated outcomes |
| Story Writer | future graph activations converted to conditional branches |
| Predictive Astrology | frozen forecast wrapper around eligible branches |

## Preservation

V1 examples/results remain addressable under V1.

Migration must not retroactively make V1 forecasts appear to have used stars, degree symbolism, or asteroids.

## Validation

Before V2 becomes READY_FOR_CONFIGURATION:
- deterministic v1 state must reproduce through v2 where features overlap;
- new degree/star/minor-body layers must remain separately ablatable;
- dependency lineage must prevent wrapper double counting;
- search-space policy must be frozen.