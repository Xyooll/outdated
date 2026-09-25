# Numerical Magic — Domain Plumbing

Status: **EXPERIMENTAL / VERIFICATION_PENDING**

Parent contracts:
- ../../floware/PIPE-CONTRACT.md
- ../../floware/FLOW-CONTRACT.md
- ../../floware/meta/pipeline-integrity.flow.md

Primary Flow:
- flows/numerical-analysis.flow.md

## PIPE-NUMERICAL-MAGIC-ENTRY

FROM POINTER:
  CORE-XYOOL-EXECUTION / authorized numerical-magic objective

TO POINTER:
  NUMERICAL-MAGIC-ANALYSIS / INPUT STATE

SEMANTIC INVARIANTS:
  requested job preserved
  domain remains EXPERIMENTAL
  symbolic analysis creates no external-action authority

AUTHORITY:
  routing → arithmetic/symbolic research only

FAILURE:
  unclear grammar/job/authority = BLOCKED / UNKNOWN

---

## PIPE-NUMERICAL-MAGIC-NATIVE-STATE

FROM POINTERS:
  literal formula/string/intention
  grammar + version
  root registry
  carrier mapping/profile
  deterministic parse/arithmetic state where used

TO POINTER:
  NUMERICAL-MAGIC-ANALYSIS / deterministic + symbolic input state

SEMANTIC INVARIANTS:
  literal input preserved
  mapping/version preserved
  full reduction chain recoverable
  order/reversal/repetition preserved
  inherited convention distinguished from local extension

AUTHORITY:
  native state → analysis input only

FAILURE:
  ambiguous undeclared grammar/mapping or unreproducible arithmetic = BLOCKED for affected layer

---

## PIPE-NUMERICAL-MAGIC-ANALYSIS-VALIDATION

FROM POINTER:
  NUMERICAL-MAGIC-ANALYSIS / empirical efficacy claim package

TO POINTER:
  domains/numerical-magic/VALIDATION.md / applicable frozen validation protocol

GATE:
  a real-world efficacy claim is being tested

REQUIRED STATE:
  grammar/version
  exact formula/parse
  symbolic interpretation/construction
  frozen expected outcome
  window
  hit definition
  miss definition
  provenance

SEMANTIC INVARIANTS:
  arithmetic correctness ≠ empirical efficacy
  symbolic consistency ≠ empirical efficacy
  post-hoc interpretation cannot become a prospective prediction

AUTHORITY:
  symbolic/empirical hypothesis → validation candidate only

FAILURE:
  missing prospective freeze/provenance = NOT_VALIDATED / BLOCKED

---

## PIPE-NUMERICAL-MAGIC-VALIDATION-LEARNING

FROM POINTER:
  numerical-magic validation / closed outcome record

TO POINTER:
  CORE-LEARNING / outcome evidence

GATE:
  outcome is linked to a frozen prior claim

SEMANTIC INVARIANTS:
  grammar/version/formula identity retained
  one outcome does not prove or disprove the whole symbolic language
  arithmetic/parser defects separated from efficacy misses

AUTHORITY:
  evaluated domain evidence → learning input only

FAILURE:
  prior frozen claim cannot be recovered = BLOCKED
