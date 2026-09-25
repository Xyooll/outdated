# FLOW — Astrology Analysis

FLOW ID: ASTROLOGY-ANALYSIS
STATUS: **EXPERIMENTAL / VERIFICATION_PENDING**
DOMAIN: astrology
JOB: system-locked astrological calculation/interpretation and bounded timing-claim analysis
AUTHORITY: interpretive/research only; deterministic calculation state may be reported as calculation, but no empirical/high-stakes/action authority is created
PARENT GOALPOST: ../../../research/system-tests/domain-foundations-v1-2026-09-24/GOALPOST.md
UPSTREAM FLOWS: Core Domain Establishment, Xyool Execution, Domain Configurer; domain-native calculation/system/rule state through Astrology Plumbing
DOWNSTREAM FLOWS: Core Relational Story for history/predictive story work under Astrology binding; domain validation protocol for non-story efficacy claims; Core Learning only after an outcome/validation record exists
INBOUND PIPES: ../PLUMBING.md#pipe-astrology-entry, ../PLUMBING.md#pipe-astrology-native-state
OUTBOUND PIPES: ../PLUMBING.md#pipe-astrology-analysis-relational-story, ../PLUMBING.md#pipe-astrology-analysis-validation
SOFTWARE DEPENDENCIES: existing deterministic astronomical/calendrical/time conversion utilities only where exactness requires them

## GOAL

Execute the requested astrology system(s) while preserving system identity, native rules, calculation provenance, uncertainty, claim type, and empirical validation boundaries.

## GOALPOST

The analysis is complete when:
- requested system/tradition and settings are explicit;
- required inputs and their precision are explicit;
- deterministic calculations are either verified or clearly unavailable;
- interpretation uses only declared rules/sources;
- multi-system outputs remain separable;
- predictive claims have a frozen claim/window/hit/miss definition before outcome use;
- uncertainty and invalidation conditions are explicit;
- no empirical or high-stakes authority is implied beyond evidence.

## INPUT STATE

Load as applicable:
- ../library/INDEX.md
- ../ESTABLISHMENT.md
- ../DOMAIN.md
- ../CONFIGURATION.md
- ../SYSTEM-REGISTRY.md
- ../RULE-REGISTRY.md
- ../RUN-SEQUENCE.md
- ../TIME-STANDARDS.md
- ../VALIDATION.md
- relevant system-specific files;
- subject/event data with precision/uncertainty.

## EVIDENCE

Calculation evidence:
- declared birth/event inputs;
- timezone/calendar conventions;
- ephemeris/calculation output;
- independent calculation cross-checks where material.

Interpretive evidence:
- named tradition/ruleset;
- source provenance;
- domain rules and explicit hypotheses.

Outcome evidence:
- frozen prospective record where predictive;
- timestamped external/subject outcome under the domain validation hierarchy.

A calculated configuration is not evidence that its interpretation is causally true.

## PROCESS

~~~text
IDENTIFY REQUESTED JOB + FUNCTION SCOPE
→ QUERY DOMAIN LIBRARY FIRST FOR EXISTING RULES / BOUNDARIES / VALIDATION LESSONS
→ LOAD ESTABLISHMENT RECORD
→ REQUIRE REQUESTED FUNCTION = READY_FOR_CONFIGURATION
→ IF PARTIAL / BLOCKED: RETURN TO CORE DOMAIN ESTABLISHMENT AND STOP THAT FUNCTION
→ LOCK ASTROLOGY SYSTEM / TRADITION / SETTINGS
→ VALIDATE INPUT PRECISION + TIME/LOCATION ASSUMPTIONS
→ LOAD DECLARED RULESET
→ PRODUCE / LOAD DETERMINISTIC NATIVE CALCULATION STATE
→ CROSS-CHECK MATERIAL CALCULATIONS WHEN REQUIRED
→ INTERPRET EACH SYSTEM NATIVELY
→ IF MULTI-SYSTEM:
      PRESERVE NATIVE OUTPUTS
      MAP TO SHARED CAPABILITY LANGUAGE ONLY IF REQUESTED
      PRESERVE DEPENDENCY / CONTRADICTION
→ CLASSIFY CLAIM:
      CALCULATION
      INTERPRETATION
      TIMING HYPOTHESIS
      PREDICTIVE CLAIM
→ IF HISTORY-AWARE STORY OR PREDICTIVE:
      LOAD `../STORY-BINDING.md`
      REQUIRE REQUESTED READER/WRITER SCOPE ESTABLISHED
      ROUTE DOMAIN-NATIVE HISTORY / CURRENT STATE / TIMERS / RULES TO `../../../floware/core/relational-story.flow.md`
→ IF PREDICTIVE:
      REQUIRE ASTRO-FN-PREDICTIVE = READY_FOR_CONFIGURATION
      RELATIONAL STORY OWNS READER → WRITER BRANCH CONSTRUCTION
      PREDICTIVE FLOW LATER OWNS FORECAST FREEZE + BASELINE/CONTROL CONTRACT
→ OUTPUT WITH UNCERTAINTY / INVALIDATION
~~~

## GATES

- requested function/scope is established as READY_FOR_CONFIGURATION;
- system identity lock;
- required input precision;
- calculation/configuration consistency;
- rule provenance;
- no silent cross-system mixing;
- predictive preregistration before outcome review;
- subjective and objective outcomes remain distinct;
- no high-stakes substitution.

## ADAPTATION

Unknown/imprecise birth time restricts time-sensitive techniques rather than automatically blocking the entire domain.

If calculation engines disagree materially, block affected interpretation until resolved.

If systems disagree, preserve the contradiction. Do not average it away.

If synthesis is not requested, return native system outputs separately.

## BOUNDARIES

This Flow does not:
- establish astrology as empirically true;
- convert interpretive confidence into numeric probability without calibration;
- treat cross-system agreement as independent proof;
- change source traditions silently;
- substitute for medical, legal, financial, safety, or other high-stakes evidence;
- authorize external actions.

## FAIL-CLOSED CONDITIONS

Return BLOCKED / UNKNOWN for the affected claim when:
- requested function is PARTIAL/BLOCKED in ../ESTABLISHMENT.md;
- required system identity is missing;
- required input precision is insufficient;
- timezone/calendar conversion is unresolved;
- a material calculation discrepancy remains unresolved;
- a predictive window/hit/miss definition is reconstructed after outcome reveal;
- rule provenance required for the claim is absent.

## OUTPUT STATE

~~~text
REQUESTED JOB:
DOMAIN FUNCTION:
ESTABLISHMENT STATUS:
SYSTEM / TRADITION:
SETTINGS / VERSION:
INPUT PRECISION:
CALCULATION STATE:
CALCULATION PROVENANCE:
INTERPRETIVE CLAIMS:
CLAIM TYPES:
SYNTHESIS / CONTRADICTIONS:
TIMING WINDOW:
PREDICTIVE FREEZE STATUS:
UNCERTAINTY:
INVALIDATION:
VALIDATION STATUS:
NEXT OWNER:
~~~

## LEARNING HOOK

Closed predictions, calculation discrepancies, reproducibility failures, false convergence, and repeated interpretive misses may enter Core Learning only with preserved system/settings/provenance and the applicable validation state.

## SOFTWARE / HARD-LIMIT BOUNDARY

Existing software may support exact astronomical/calendrical/timezone calculation and deterministic cross-checks.

New interpretive, routing, synthesis, confidence, or learning logic belongs in Floware.

## COMPLEXITY RULE

Use only the systems and techniques needed for the requested job. Do not run a multi-system synthesis when one declared system is sufficient.


## Story / predictive-routing boundary

A history-aware or predictive request is story-shaped work and uses `../STORY-BINDING.md` with Core Relational Story.

A predictive request is also a material domain-function update/use request. If `ASTRO-FN-PREDICTIVE` remains PARTIAL in `../ESTABLISHMENT.md`, this Flow returns to Core Domain Establishment before Story Writer may generate predictive branches.

Predictive Astrology consumes eligible Story Writer branches; it is not a parallel future-story engine.


## DOMAIN LIBRARY FIRST

Before new outside research or rule invention, inspect `../library/INDEX.md`.

Use current reusable knowledge when its:
- scope matches;
- canonical pointer resolves;
- status/freshness is sufficient.

Route only real gaps, stale items, conflicts, or new scope to Research / Rule Foundation.

Material new reusable results should be written back through Core Domain Library after canonical domain artifacts are updated.
