# FLOW — Predictive Astrology

FLOW ID: ASTROLOGY-PREDICTIVE-V1
STATUS: **EXPERIMENTAL / VERIFICATION_PENDING**
DOMAIN: astrology
JOB: convert eligible Astrology-bound Core Story Writer branches into auditable prospective forecasts and evaluate whether they add discrimination beyond relevant non-astrological baselines
AUTHORITY: experimental forecast formation only; no empirical truth claim, high-stakes decision authority, or external-action authority
PARENT GOALPOST: ../../../research/system-tests/astrology-predictive-v1-2026-09-24/GOALPOST.md
UPSTREAM FLOWS: Core Domain Establishment (function readiness), Core Relational Story using Astrology STORY-BINDING.md
DOWNSTREAM FLOWS: Astrology Validation protocol; user-facing delivery through ../DELIVERY.md; Core Learning only after closed/scored outcomes through existing Astrology validation-to-learning Pipe
INBOUND PIPES: ../PLUMBING.md#pipe-astrology-relational-story-predictive
OUTBOUND PIPES: ../PLUMBING.md#pipe-astrology-predictive-validation
SOFTWARE DEPENDENCIES: none for forecast reasoning; existing deterministic astrology calculators may supply verified native timing state

## GOAL

Turn conditional future branches written by the canonical Story Writer under established Astrology rules into finite, falsifiable prospective forecasts, then test whether those forecasts outperform plausible non-astrological baselines.

Core law:

> **Prediction begins only after the claim can clearly lose.**

## GOALPOST

A forecast is valid for prospective testing when:
- subject/date identity is frozen;
- one system/configuration version is identified;
- a small predeclared rule cohort is locked;
- the predicted outcome category is defined independently of astrology;
- start/end and any peak are finite;
- hit, miss, ambiguity, and unavailable conditions are declared;
- confidence is frozen before outcome;
- contradictory signals are recorded;
- relevant null/baseline models are named;
- forecast exposure/blinding status is recorded;
- the record is frozen before the outcome window is scored.

Predictive success is not established by one hit. Evidence requires repeated scored forecasts versus baselines/controls.

## INPUT STATE

Required:
- ../ESTABLISHMENT.md with ASTRO-FN-PREDICTIVE = READY_FOR_CONFIGURATION;
- ../STORY-BINDING.md;
- Core Relational Story output with a frozen Reader current-state basis and Story Writer branch set;
- an experiment-ready frozen rule cohort produced during domain establishment;
- selected predictive-eligible branch ID(s);
- system_id + configuration;
- rule IDs + versions;
- deterministic calculation/timing state;
- subject/date identity;
- target outcome ontology;
- forecast horizon;
- baseline/control plan;
- current validation cohort identity;
- allowed technique set.

For N-of-1 capability studies also load:
- personal baseline measurements when available;
- measurement schedule;
- context covariates allowed by protocol.

## EVIDENCE

Forecast evidence may include:
- verified astrological calculation state;
- source-documented or explicitly hypothetical rules;
- predeclared timing boundaries;
- frozen capability/event definitions.

Validation evidence later includes:
- scheduled prospective measurements;
- externally timestamped events;
- matched control windows;
- personal/calendar/recent-state/context baselines;
- shuffled/placebo signals where used.

Interpretive coherence is not outcome evidence.

## PROCESS

~~~text
RECEIVE ASTROLOGY-BOUND RELATIONAL STORY OUTPUT
→ CONFIRM READER CURRENT-STATE BASIS + WRITER FREEZE/VERSION
→ CONFIRM PREDICTIVE MODE
→ REQUIRE ASTRO-FN-PREDICTIVE = READY_FOR_CONFIGURATION
→ IF NOT READY: RETURN TO CORE DOMAIN ESTABLISHMENT AND STOP
→ REQUIRE FROZEN EXPERIMENT-READY RULE COHORT
→ SELECT ONLY PREDICTIVE-ELIGIBLE STORY WRITER BRANCHES
→ LOCK ONE PRIMARY SYSTEM FOR V1
→ LOCK CONFIGURATION + RULE VERSIONS
→ LOCK ALLOWED TECHNIQUES / SEARCH SPACE
→ MAP SELECTED STORY BRANCH TO ONE PREDEFINED OUTCOME TARGET
→ DEFINE:
     DIRECTION / CATEGORY
     START
     END
     PEAK IF USED
     MAGNITUDE IF USED
     HIT
     MISS
     AMBIGUOUS
     UNAVAILABLE
→ NAME RELEVANT BASELINES / CONTROLS
→ RECORD KNOWN CONTRADICTIONS + DEPENDENCIES
→ ASSIGN QUALITATIVE CONFIDENCE BAND
→ RECORD BLINDING / FORECAST-SEEN STATUS
→ FREEZE FORECAST
→ ROUTE TO VALIDATION
→ AFTER WINDOW CLOSE:
     SCORE WITHOUT EDITING ORIGINAL
     COMPARE WITH BASELINES
     RECORD COVERAGE / FALSE POSITIVES / MISSES
→ REPEAT
→ ONLY AFTER ADEQUATE COHORT:
     EVALUATE WHETHER SIGNAL DISCRIMINATES
~~~

## V1 TEST ORDER

Use the complexity ladder:

~~~text
PERSONAL / CALENDAR BASELINE
→ SINGLE ASTROLOGY SYSTEM
→ SINGLE SYSTEM + PERSONALIZATION
→ ONLY IF ADDED VALUE IS SHOWN:
     MULTI-SYSTEM FUSION
     CAPABILITY TRANSLATION EXPANSION
     TUNER COMPRESSION
~~~

Do not begin with fusion.

## FORECAST TYPES

V1 supports:

### Capability/state forecast

Predeclared capability from:
- Focus
- Communication
- Action
- Recovery
- Friction / Impulsiveness
- another explicitly defined capability from CAPABILITY-ONTOLOGY.md

Prefer a sparse primary outcome set.

### External-event forecast

Predeclared event category/subcategory from OUTCOME-TAXONOMY.md.

Common/high-base-rate events require stronger timing/specificity controls.

## NULL / BASELINE REQUIREMENT

Every scored cohort must identify relevant comparators from:

~~~text
N0 unconditional base rate
N1 personal baseline
N2 calendar baseline
N3 recent-state / persistence baseline
N4 context baseline
N5 placebo / shuffled symbolic model
~~~

A forecast that does not outperform an appropriate simple baseline has not shown added predictive information.

## TIMING RULE

Track:
- total observation time;
- total flagged time;
- number of forecast windows;
- event/capability hits inside windows;
- false-positive windows;
- matched/control performance.

Broad calendar coverage is penalized by the existing timing-scoring rules.

Never extend a window because the predicted result did not occur.

## CONFIDENCE

V1 uses:

~~~text
LOW
MEDIUM
HIGH
~~~

No numeric probability is allowed unless a named calibration model already exists for that rule/system/cohort.

After enough forecasts, test whether observed performance is monotonic by band.

## GATES

Before freeze:
- ASTRO-FN-PREDICTIVE is READY_FOR_CONFIGURATION in the domain establishment record;
- branch originates from Core Story Writer under `STORY-BINDING.md`;
- Reader current-state cutoff and Writer branch version are frozen;
- selected rule cohort is experiment-ready and version-locked;
- calculation state valid for claimed technique;
- system/settings identity locked;
- rule versions locked;
- outcome definition independent of astrology;
- finite window;
- miss condition;
- search space declared;
- baseline/control plan declared;
- confidence locked;
- no outcome knowledge used.

Before claiming predictive value:
- all eligible forecasts closed, including misses;
- coverage reported;
- ambiguity rate reported;
- baseline/control comparison completed;
- discovery and confirmation cohorts separated;
- no material lookahead leakage;
- uncertainty/sampling limitations reported.

## ADAPTATION

A miss may generate a new hypothesis only after Failure/Learning analysis. The original forecast and rule version remain unchanged.

If a rule is modified, it enters a new version/cohort.

If a system appears weak, preserve the negative result; do not rescue it by adding systems post hoc.

If one capability is too subjective/noisy, the next cohort may use a stronger behavioral/external endpoint, but prior results remain scored.

## BOUNDARIES

This Flow does not:
- establish astrology as true;
- guarantee events;
- advise medical/legal/financial/safety actions from astrology;
- change the prediction after seeing the result;
- count a retrospective fit as prospective evidence;
- combine systems merely to rescue misses;
- generate precise probabilities without calibration.

## FAIL-CLOSED CONDITIONS

Return NOT_VALID_FOR_PROSPECTIVE_TEST when:
- ASTRO-FN-PREDICTIVE is not READY_FOR_CONFIGURATION;
- selected system lacks an experiment-ready established rule cohort;
- system/rule identity is not frozen;
- calculation prerequisite is unresolved;
- the claim has no finite miss condition;
- outcome category is defined from the astrology interpretation itself;
- the forecast window is chosen after outcome review;
- required baseline/control plan is absent;
- too many undeclared techniques were searched to identify the prediction.

## OUTPUT STATE

~~~text
FORECAST ID:
STORY ID / VERSION:
READER AS-OF:
WRITER BRANCH ID / VERSION:
COHORT:
SUBJECT / DATE ID:
CREATED AT:
SYSTEM ID:
CONFIGURATION:
RULE IDS / VERSIONS:
ALLOWED TECHNIQUES:
CLAIM:
OUTCOME TYPE:
CATEGORY / CAPABILITY:
DIRECTION:
CAPTURE AREA:
WINDOW START:
WINDOW END:
PEAK:
MAGNITUDE:
CONFIDENCE:
HIT:
MISS:
AMBIGUOUS:
UNAVAILABLE:
KNOWN CONTRADICTIONS:
KNOWN DEPENDENCIES:
BASELINES / CONTROLS:
BLINDING LEVEL:
FORECAST SEEN:
FREEZE STATUS:
VALIDATION STATUS:
~~~

## LEARNING HOOK

After scoring, material misses, false positives, calibration failures, and control failures route through the existing Astrology validation → Core Learning path.

Learning may propose a new rule/version or narrower boundary. It may not rewrite the scored forecast.

## SOFTWARE / HARD-LIMIT BOUNDARY

NONE — FLOWARE SUFFICIENT FOR V1 FORECAST REASONING

Existing deterministic calculation software may supply exact positions/windows. Automated ledgers, hashing, prompts, schedulers, and scoring utilities remain deferred until the Flow proves the need.

## COMPLEXITY RULE

Start with one system, a small frozen rule cohort, and a sparse outcome set. Add fusion, more techniques, narrower atomic windows, or calibrated probabilities only when the simpler model has demonstrated incremental value.


## STORY WRITER BOUNDARY

Core Story Writer owns conditional future branch construction.

Predictive Astrology owns:
- deciding which established Writer branches are eligible to become forecast records;
- freezing claim/window/hit/miss/control state;
- routing those frozen records to prospective validation;
- later scoring against baselines.

Do not duplicate branch-generation logic inside this Flow.

If the Writer cannot produce a valid branch because transition rules are missing, return to Core Domain Establishment rather than improvising an Astrology prediction.


## DELIVERY BOUNDARY

The frozen forecast record may be technically dense.

User-facing delivery is governed by `../DELIVERY.md`.

Default:
- use STANDARD mode;
- state the forecast before the machinery;
- expose at most 3 primary predictions and 5 windows;
- technical degrees/houses/stars/asteroids are supporting evidence, not the main narrative;
- include concise hit/miss conditions;
- keep full rule IDs, dependencies, nulls, and scoring in the internal/audit record.

If the user asks for:
- "just the forecast" → QUICK;
- normal forecast → STANDARD;
- "why / show the astrology" → expand only the requested prediction;
- "audit / deep" → AUDIT / DEEP.

Delivery compression may remove presentation detail but must never change the underlying frozen claim, window, confidence, or scoring definition.


## CONTINUOUS COVERAGE RULE

A user-facing forecast over a declared horizon must not contain unlabeled gaps.

Predictive formation may still promote only some branches as primary calls, but the presentation layer must characterize every interval using the active/fading/building/background state available from the full Story/Signal model.

Correct separation:

~~~text
PRIMARY FORECAST CALLS
= strongest falsifiable claims

CONTINUOUS TIMELINE
= full horizon state, including low-signal/background intervals

VALIDATION CONTROLS
= separately designated comparison intervals
~~~

Do not equate "not a primary call" with "no useful data."
