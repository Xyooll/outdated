# Xyool Astrology — Delivery Contract

Status: **EXPERIMENTAL DOMAIN CANONICAL / USER-FACING PRESENTATION LAYER**

Purpose: keep internal astrology reasoning rich while making the default user-facing forecast concise, scannable, and useful.

Core law:

> **Reason deeply; deliver shallowly by default.**

Internal model complexity must not leak into the default answer unless it materially changes the conclusion.

## 1. Progressive disclosure

Use three delivery depths:

### QUICK

Use when the user wants the forecast itself.

Structure:
1. one-line overall theme;
2. continuous horizon coverage in compact segments;
3. one sentence per segment;
4. visually emphasize only the strongest 3–5 turning points;
4. strongest testable prediction;
5. one-line confidence/status.

### STANDARD — default

Use when the user asks for a normal reading/forecast.

Structure:
1. headline;
2. continuous timeline with no omitted intervals;
3. 2–3 strongest predictions called out separately;
4. what would count as a hit/miss;
5. short 'why this is showing up' section with no more than 2 primary drivers per prediction;
6. confidence/status.

### AUDIT / DEEP

Use only when requested or when the task is explicitly validation/research/audit.

May include:
- exact degrees;
- LOCAL30 / ABS360 identities;
- houses/rulers/dispositors;
- fixed-star contacts;
- asteroid nodes;
- aspect/orb details;
- dependency graph;
- rule IDs;
- model A/B/C/D/E comparison;
- nulls and scoring logic.

## 2. Default forecast hierarchy

Present in this order:

OVERALL STORY
→ WHEN
→ WHAT MAY HAPPEN
→ WHAT TO WATCH
→ CONFIDENCE / TEST STATUS

Do not present the calculation chain before the forecast conclusion.

## 3. Forecast window object

User-facing minimum:

~~~text
DATE / WINDOW
THEME
PREDICTION
WHAT COUNTS AS A HIT
~~~

Optional internal fields remain available but hidden by default.

## 3A. Continuous coverage rule

A requested forecast horizon must be fully partitioned.

~~~text
HORIZON START
→ interval 1
→ interval 2
→ interval 3
→ ...
→ HORIZON END
~~~

Every interval receives a state.

Possible states include:
- BUILDING;
- PEAK / HIGH-ACTIVATION;
- SEPARATING;
- TRANSITION;
- INTEGRATION;
- LOW-SIGNAL / BACKGROUND-DOMINANT;
- CONFLICTED;
- INSUFFICIENTLY DISTINCT.

LOW-SIGNAL is still data. It means the active model produces less concentrated or less differentiated signal, not that "nothing is happening."

Do not label an interval a control or gap merely because no major signal is present. Control windows belong to the validation layer, not the user-facing forecast.

## 4. Compression rules

For default delivery:
- cover the full requested horizon continuously;
- do not leave unlabeled time gaps;
- compress adjacent intervals only when their active signal set and dominant story are materially equivalent;
- show the strongest 3–5 turning points prominently while still preserving lower-intensity intervals;
- max 3 primary predictions called out as strongest;
- lower-intensity intervals remain in the timeline;
- max 2 technical drivers per prediction;
- avoid repeating the same house/degree/star explanation in multiple sections;
- translate technical astrology into plain-language event/state terms first;
- put jargon in parentheses only when useful;
- do not list every active transit, asteroid, or star;
- do not narrate the entire reasoning graph.

## 5. Evidence selection

Rank candidate signals internally, then expose only the signals that materially change the forecast.

Preferred hierarchy:
1. strongest timing activation;
2. strongest house/capture relevance;
3. strongest ruler/aspect reinforcement;
4. degree/star/minor-body modifiers only if they sharpen or distinguish the prediction.

Asteroids and fixed stars should usually be modifiers in STANDARD mode, not separate sections.

## 6. Technical detail budget

STANDARD mode allows at most:
- 2 exact degree references;
- 2 house/ruler references;
- 1 stellar or asteroid modifier per primary prediction;
- 1 short note on intrinsic/extrinsic meaning when it changes interpretation.

If more detail is needed, switch to AUDIT / DEEP rather than making STANDARD longer.

## 7. Confidence language

Default user-facing confidence should be one line:

~~~text
Status: experimental / calculated but not validated
Confidence: low / medium / higher relative to this experimental model
~~~

Do not dump the full confidence vector unless requested.

## 8. Validation-friendly delivery

A forecast can remain concise and still be falsifiable.

Default:
~~~text
Prediction:
Window:
Hit if:
Miss if:
~~~

Technical rule IDs and null-model details stay in the frozen forecast record, not the default prose.

## 9. Comparison to prior forecast

When rerunning after model upgrades, summarize only material differences:

~~~text
WHAT CHANGED
- stronger/weaker timing;
- different life area;
- narrower/broader window;
- new degree/star layer materially changed the claim;
- no meaningful change.
~~~

Do not repeat the entire original forecast.

## 10. Delivery anti-patterns

Avoid:
- explaining every astrological component before stating the forecast;
- turning one prediction into several paragraphs of symbolic decomposition;
- listing all degree clusters;
- listing all asteroid contacts;
- repeating caveats after every paragraph;
- mixing validation methodology into ordinary forecast prose;
- using technical richness as a proxy for usefulness.

## 11. Default STANDARD template

~~~text
# Forecast

Overall: <one-sentence story>

| Window | What to watch | Strength |
| --- | --- | --- |
| <date> | <plain-language prediction> | <band> |

## Strongest calls
1. <prediction>
2. <prediction>
3. <prediction>

## What would count
- Hit: <observable outcome>
- Miss: <observable non-outcome>

## Why
- <driver 1>
- <driver 2>

Status: experimental / not yet validated.
~~~

## 12. User control

If the user asks:
- 'why?' → expand one prediction;
- 'show the astrology' → show the technical drivers;
- 'audit it' → show rule IDs, degrees, dependencies, and scoring;
- 'just tell me the forecast' → QUICK mode.

Final rule:

> **The user should understand the forecast before they understand the machinery.**