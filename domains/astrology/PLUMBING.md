# Astrology — Domain Plumbing

Status: **EXPERIMENTAL / VERIFICATION_PENDING**

Parent contracts:
- ../../floware/PIPE-CONTRACT.md
- ../../floware/FLOW-CONTRACT.md
- ../../floware/meta/pipeline-integrity.flow.md

Primary Flow:
- flows/astrology-analysis.flow.md

## PIPE-ASTROLOGY-ENTRY

FROM POINTER:
  CORE-XYOOL-EXECUTION / authorized astrology objective

TO POINTER:
  ASTROLOGY-ANALYSIS / INPUT STATE

SEMANTIC INVARIANTS:
  requested job and user authority preserved
  domain remains EXPERIMENTAL
  high-stakes authority is not created by routing

AUTHORITY:
  routing → interpretive/research analysis only

FAILURE:
  unclear requested system/job/authority = BLOCKED / request domain clarification inside the Flow

---

## PIPE-ASTROLOGY-NATIVE-STATE

FROM POINTERS:
  astrology subject/event inputs
  system/settings identity
  deterministic calculation state
  applicable rule/source registries

TO POINTER:
  ASTROLOGY-ANALYSIS / calculation + interpretation input state

SEMANTIC INVARIANTS:
  system/tradition identity preserved
  input precision/uncertainty preserved
  deterministic calculation kept separate from interpretation
  source/rule provenance preserved
  no silent system mixing

AUTHORITY:
  native domain state → analysis input only

FAILURE:
  missing identity, unresolved calculation conflict, or materially insufficient precision = BLOCKED for affected techniques/claims

---

## PIPE-ASTROLOGY-ANALYSIS-VALIDATION

FROM POINTER:
  ASTROLOGY-ANALYSIS / predictive or efficacy claim package

TO POINTER:
  domains/astrology/VALIDATION.md / applicable frozen validation protocol

GATE:
  predictive/efficacy claim is actually being made

REQUIRED STATE:
  system/settings/version
  frozen claim
  frozen window
  hit definition
  miss definition
  techniques/rules used
  provenance
  uncertainty

SEMANTIC INVARIANTS:
  interpretation ≠ validated prediction
  cross-system agreement ≠ independent evidence by default
  post-outcome reconstruction cannot become preregistered evidence

AUTHORITY:
  analysis claim → validation candidate only

FAILURE:
  missing freeze/provenance = NOT_VALIDATED / BLOCKED, not retrospective repair

---

## PIPE-ASTROLOGY-VALIDATION-LEARNING

FROM POINTER:
  astrology validation / closed outcome record

TO POINTER:
  CORE-LEARNING / outcome evidence

GATE:
  outcome/validation record is closed enough to evaluate a prior claim

SEMANTIC INVARIANTS:
  system/settings/provenance retained
  subjective vs objective outcome class retained
  one hit/miss does not automatically become a general rule
  validation status retained

AUTHORITY:
  evaluated domain evidence → learning input only

FAILURE:
  outcome identity or original claim freeze cannot be recovered = BLOCKED


---

## PIPE-ASTROLOGY-ANALYSIS-RELATIONAL-STORY

FROM POINTER:
  ASTROLOGY-ANALYSIS / established domain-native history, current state, calculated timing state, and rule basis

TO POINTER:
  CORE-RELATIONAL-STORY / Astrology-bound story input using STORY-BINDING.md

GATE:
  requested Reader/Writer scope is established for the selected Astrology system/function
  STORY-BINDING.md applies
  material rule/state/time prerequisites are available

SEMANTIC INVARIANTS:
  Reader cutoff/as-of preserved
  observed history kept separate from astrological interpretation
  rule/system/version identity preserved
  planets/configurations remain state/timer/transition objects unless explicitly mapped otherwise
  predictive Writer authority does not exceed the established Astrology function scope

AUTHORITY:
  Astrology domain state → generic story reconstruction/branching only

FAILURE:
  requested story scope not established, missing transition rules, or unresolved history/state provenance = STORY_PARTIAL / return to Core Domain Establishment as applicable

---

## PIPE-ASTROLOGY-RELATIONAL-STORY-PREDICTIVE

FROM POINTER:
  CORE-RELATIONAL-STORY / Astrology-bound output with frozen Story Reader basis and Story Writer branches

TO POINTER:
  ASTROLOGY-PREDICTIVE-V1 / forecast-wrapper input

GATE:
  ASTRO-FN-PREDICTIVE = READY_FOR_CONFIGURATION
  Writer branch is predictive-eligible under STORY-BINDING.md

SEMANTIC INVARIANTS:
  story ID/version and Reader as-of preserved
  Writer branch ID/version preserved
  branch remains conditional until forecast freeze and outcome validation
  branch-generation rationale/rule basis remains recoverable
  no branch acquires numeric probability unless calibrated

AUTHORITY:
  conditional future branch → prospective forecast candidate only

FAILURE:
  missing Writer freeze/version, invalidated Reader state, or incomplete predictive establishment = BLOCKED

---

## PIPE-ASTROLOGY-PREDICTIVE-VALIDATION

FROM POINTER:
  ASTROLOGY-PREDICTIVE-V1 / frozen forecast record

TO POINTER:
  domains/astrology/VALIDATION.md / prospective timing validation

REQUIRED STATE:
  forecast id
  subject/date id
  system/configuration
  rule IDs/versions
  allowed technique set
  claim/outcome target
  finite window
  hit/miss/ambiguity/unavailable definitions
  confidence
  baseline/control plan
  blinding/forecast-seen state
  freeze evidence

SEMANTIC INVARIANTS:
  frozen forecast cannot be rewritten after outcome
  all eligible forecasts close
  misses remain evidence
  broad window coverage is reported
  baseline comparison is mandatory
  a positive single forecast does not establish predictive validity

AUTHORITY:
  frozen forecast → prospective validation candidate only

FAILURE:
  absent pre-outcome freeze or missing miss/control definition = NOT_VALIDATED / BLOCKED


---

## PIPE-ASTROLOGY-RESEARCH-RULE-FOUNDATION

FROM POINTER:
  CORE-RESEARCH / source-grounded astrology rule evidence

TO POINTER:
  ASTROLOGY-RULE-FOUNDATION-V1 / INPUT STATE

SEMANTIC INVARIANTS:
  source provenance preserved
  source authority does not become efficacy authority
  system/tradition identity preserved
  contradictions remain explicit

AUTHORITY:
  research evidence → rule establishment only

FAILURE:
  source/system identity ambiguous = BLOCKED / PARTIAL

---



---

## PIPE-ASTROLOGY-ESTABLISHMENT-RULE-FOUNDATION

FROM POINTER:
  CORE-DOMAIN-ESTABLISHMENT / Astrology function with MISSING DOMAIN RULE / METHOD

TO POINTER:
  ASTROLOGY-RULE-FOUNDATION-V1 / INPUT STATE

GATE:
  the missing content is Astrology-local rule/method establishment rather than a missing Core primitive

SEMANTIC INVARIANTS:
  target domain function and claimed scope preserved
  Core establishment authority preserved
  source/provenance requirements preserved
  helper may establish rule objects but may not mark the whole function READY_FOR_CONFIGURATION

AUTHORITY:
  Core establishment gap → domain-local rule-foundation work only

FAILURE:
  target function/system/technique ambiguous = PARTIAL / return to Core without readiness change

---

## PIPE-ASTROLOGY-RULE-FOUNDATION-ESTABLISHMENT

FROM POINTER:
  ASTROLOGY-RULE-FOUNDATION-V1 / local ruleset result

TO POINTER:
  CORE-DOMAIN-ESTABLISHMENT / function-readiness re-evaluation

SEMANTIC INVARIANTS:
  rule IDs/versions/provenance preserved
  local ruleset readiness remains distinct from domain-function readiness
  source authority does not become efficacy authority
  unresolved conflicts/blockers preserved

AUTHORITY:
  local rule-foundation result → Core establishment evidence only

FAILURE:
  missing provenance/version/search-space/falsification state = function remains PARTIAL


## PIPE-ASTROLOGY-ESTABLISHMENT-INTRINSIC-DEGREE

FROM POINTER:
  CORE-DOMAIN-ESTABLISHMENT / intrinsic-degree knowledge or rule gap

TO POINTER:
  ASTROLOGY-INTRINSIC-DEGREE-FOUNDATION-V1 / research-synthesis input

GATE:
  requested gap concerns LOCAL30 or ABS360 degree meaning rather than generic star calculation

SEMANTIC INVARIANTS:
  coordinate type preserved
  zero-based index and one-based ordinal preserved
  source lineage/dependency state preserved
  source-derived meaning remains separate from Xyool synthesis
  no efficacy authority created by source consensus

AUTHORITY:
  Core establishment gap → degree-meaning research only

FAILURE:
  unresolved indexing/source lineage = PARTIAL / BLOCKED

---

## PIPE-ASTROLOGY-INTRINSIC-DEGREE-ESTABLISHMENT

FROM POINTER:
  ASTROLOGY-INTRINSIC-DEGREE-FOUNDATION-V1 / frozen meaning candidate or corpus result

TO POINTER:
  CORE-DOMAIN-ESTABLISHMENT / Star Astrology function-readiness re-evaluation

SEMANTIC INVARIANTS:
  candidate IDs/versions preserved
  coordinate type preserved
  contributing/dependent sources preserved
  source consensus does not become validation evidence
  discovery/confirmation separation preserved

AUTHORITY:
  intrinsic-degree result → establishment evidence only

FAILURE:
  unfrozen meaning, unresolved source dependence, or no falsification/null path = function remains PARTIAL

---


## PIPE-ASTROLOGY-INTRINSIC-DEGREE-MEANING

FROM POINTER:
  ASTROLOGY-INTRINSIC-DEGREE-FOUNDATION-V1 / source-derived or Xyool degree-meaning candidate

TO POINTER:
  CORE-MEANING-ATTRIBUTION / INPUT STATE

SEMANTIC INVARIANTS:
  LOCAL30 / ABS360 coordinate identity preserved
  intrinsic meaning type preserved
  source/authorship preserved
  source-lineage dependencies preserved
  source meaning and Xyool synthesis remain distinguishable
  validation status is not upgraded

AUTHORITY:
  Astrology degree-meaning candidate → Core semantic representation only

FAILURE:
  unresolved source/authorship/indexing/claim mode = MEANING_PARTIAL

---

## PIPE-ASTROLOGY-MEANING-INTRINSIC-DEGREE

FROM POINTER:
  CORE-MEANING-ATTRIBUTION / normalized intrinsic meaning object

TO POINTER:
  ASTROLOGY-INTRINSIC-DEGREE-FOUNDATION-V1 / candidate synthesis / freeze state

SEMANTIC INVARIANTS:
  meaning ID/version preserved
  semantic primitives remain linked to native meaning
  intrinsic meaning remains separate from extrinsic chart context
  creative-use status does not become predictive authority

AUTHORITY:
  normalized meaning object → Astrology intrinsic-degree candidate state only

FAILURE:
  meaning type other than INTRINSIC for the degree cell = reject or route to the appropriate extrinsic/composite layer
