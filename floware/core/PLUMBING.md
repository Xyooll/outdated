# Floware Core — Attention Plumbing

Status: **CANDIDATE / VERIFICATION_PENDING**

Parent contracts:
- ../PIPE-CONTRACT.md
- ../FLOW-CONTRACT.md

Purpose: govern the material connections that bring new observations into Xyool and select a bounded active work set before execution.

## PIPE-CORE-OBSERVATION-IN

FROM POINTER:
  external/source adapter, persistent state cursor, due timer, resolved outcome, or explicit user observation

TO POINTER:
  CORE-OBSERVATION-TRIGGER / INPUT STATE

SEMANTIC INVARIANTS:
  source/object identity and prior cursor/state remain explicit
  raw observation does not become domain truth merely by entering the Pipe

AUTHORITY:
  observed data → trigger-evaluation only

FAILURE:
  unresolved identity/provenance = BLOCKED_UNKNOWN

## PIPE-CORE-OBSERVATION-RESOURCE

FROM POINTER:
  CORE-OBSERVATION-TRIGGER / QUEUE or competing trigger candidates

TO POINTER:
  CORE-RESOURCE-ALLOCATION / candidate work

SEMANTIC INVARIANTS:
  trigger materiality/urgency preserved
  queued does not mean authorized external action

AUTHORITY:
  attention candidate only

FAILURE:
  lost trigger provenance/materiality reason = BLOCKED

## PIPE-CORE-OBSERVATION-EXECUTION

FROM POINTER:
  CORE-OBSERVATION-TRIGGER / TRIGGER_NOW

TO POINTER:
  CORE-XYOOL-EXECUTION / authorized objective/context

GATE:
  trigger belongs to an already authorized objective/watch scope, or the user/system authority permits opening the bounded work

SEMANTIC INVARIANTS:
  trigger ≠ substantive conclusion
  trigger ≠ external action authority

FAILURE:
  missing objective/authority boundary = QUEUE/BLOCKED, not silent execution

## PIPE-CORE-EXECUTION-RESOURCE

FROM POINTER:
  CORE-XYOOL-EXECUTION / competing candidate work exceeding simple direct execution

TO POINTER:
  CORE-RESOURCE-ALLOCATION / candidate work

SEMANTIC INVARIANTS:
  original goalpost and hard required gates preserved

AUTHORITY:
  execution routing → work-selection only

FAILURE:
  unclear goal/hard requirements = BLOCKED

## PIPE-CORE-RESOURCE-EXECUTION

FROM POINTER:
  CORE-RESOURCE-ALLOCATION / ACTIVE SET + resource envelopes + deferred set

TO POINTER:
  CORE-XYOOL-EXECUTION / executable selected work

SEMANTIC INVARIANTS:
  deferred work preserved
  selection does not determine dependency order
  selected work retains original authority/gates

AUTHORITY:
  work-selection → execution routing only

FAILURE:
  selection drops mandatory gate or broadens authority = BLOCKED


## PIPE-CORE-EXECUTION-DOMAIN-ESTABLISHMENT

FROM POINTER:
  CORE-XYOOL-EXECUTION / new domain, materially expanded domain, or requested function with unknown establishment readiness

TO POINTER:
  CORE-DOMAIN-ESTABLISHMENT / INPUT STATE

SEMANTIC INVARIANTS:
  user objective and claimed scope preserved
  current authority boundary preserved
  existing established domain scopes are not invalidated merely because a new function is partial
  Core questions do not become local domain answers automatically

AUTHORITY:
  execution routing → domain-establishment analysis only

FAILURE:
  unclear domain/function scope = BLOCKED until scope is bounded

## PIPE-CORE-DOMAIN-ESTABLISHMENT-INTEGRITY

FROM POINTER:
  CORE-DOMAIN-ESTABLISHMENT / READY_FOR_CONFIGURATION output

TO POINTER:
  META-PIPELINE-INTEGRITY / Domain Integration composite

GATE:
  establishment status = READY_FOR_CONFIGURATION for the claimed scope

SEMANTIC INVARIANTS:
  domain-native rules/evidence/function contracts preserved
  establishment readiness ≠ empirical validation
  establishment readiness ≠ configuration validity
  missing local semantics may not be filled by Mapping/Configurer

AUTHORITY:
  established domain scope → Meta integration/configuration only

FAILURE:
  establishment status other than READY_FOR_CONFIGURATION = do not enter Meta configuration for that scope


## PIPE-CORE-DOMAIN-ESTABLISHMENT-LIBRARY

FROM POINTER:
  CORE-DOMAIN-ESTABLISHMENT / domain knowledge or rule coverage check

TO POINTER:
  CORE-DOMAIN-LIBRARY / retrieval query

SEMANTIC INVARIANTS:
  domain, claimed scope, and function preserved
  library lookup precedes classification of a local knowledge/rule gap
  library knowledge retains canonical provenance/status

AUTHORITY:
  establishment question → internal domain-knowledge retrieval only

FAILURE:
  unresolved domain/scope = BLOCKED

## PIPE-CORE-LIBRARY-DOMAIN-ESTABLISHMENT

FROM POINTER:
  CORE-DOMAIN-LIBRARY / reusable knowledge + material gap set

TO POINTER:
  CORE-DOMAIN-ESTABLISHMENT / function-readiness analysis

SEMANTIC INVARIANTS:
  source/validation/freshness status preserved
  a library hit does not automatically make a function READY_FOR_CONFIGURATION
  gaps remain explicit

AUTHORITY:
  reusable domain knowledge → establishment evidence only

FAILURE:
  stale/conflicted/superseded object = REFRESH_REQUIRED, not silent reuse

## PIPE-CORE-RESEARCH-LIBRARY

FROM POINTER:
  CORE-RESEARCH / reusable evidence-backed result suitable for domain memory

TO POINTER:
  CORE-DOMAIN-LIBRARY / write-back candidate

SEMANTIC INVARIANTS:
  source provenance retained
  fact/inference/unknown distinctions retained
  raw external content is not copied wholesale by default

AUTHORITY:
  research result → candidate reusable domain knowledge only

FAILURE:
  missing provenance/scope = do not persist as established knowledge

## PIPE-CORE-LIBRARY-RESEARCH

FROM POINTER:
  CORE-DOMAIN-LIBRARY / library hit or material gap set

TO POINTER:
  CORE-RESEARCH / existing knowledge context + unresolved external evidence gaps

SEMANTIC INVARIANTS:
  stable internal knowledge reused
  stale/dynamic items still require refresh
  library status does not override research evidence requirements

AUTHORITY:
  knowledge context/gap definition → bounded research only

FAILURE:
  unclear freshness/validation = research must treat as unresolved


## PIPE-CORE-DOMAIN-ESTABLISHMENT-MEANING

FROM POINTER:
  CORE-DOMAIN-ESTABLISHMENT / meaning-dependent domain function or unresolved semantic model

TO POINTER:
  CORE-MEANING-ATTRIBUTION / INPUT STATE

GATE:
  claimed domain function materially depends on intrinsic, extrinsic, composite, symbolic, ritual, metaphysical, narrative, or creative meaning

SEMANTIC INVARIANTS:
  domain/system identity preserved
  source/authorship preserved
  meaning claim mode preserved
  meaning does not become empirical fact through routing

AUTHORITY:
  domain establishment question → semantic modeling only

FAILURE:
  unresolved object/system/source/claim-mode identity = MEANING_PARTIAL / BLOCKED

## PIPE-CORE-MEANING-LIBRARY

FROM POINTER:
  CORE-MEANING-ATTRIBUTION / reusable meaning object

TO POINTER:
  CORE-DOMAIN-LIBRARY / meaning knowledge write-back candidate

SEMANTIC INVARIANTS:
  intrinsic/extrinsic/composite type preserved
  source/authorship and framework preserved
  semantic primitives remain linked to native meaning
  validation status and creative-use status preserved

AUTHORITY:
  reusable meaning representation → domain knowledge candidate only

FAILURE:
  missing provenance or ambiguous authorship = do not persist as established meaning

## PIPE-CORE-CORRESPONDENCE-NOVELTY

FROM POINTER:
  CORE-CORRESPONDENCE / abstract invariant or remote structural counterpart

TO POINTER:
  CORE-NOVELTY-ENHANCER / creative divergence input

GATE:
  creative/generative authority explicitly allows remote recombination

SEMANTIC INVARIANTS:
  source correspondence remains traceable
  imported structure does not import source-domain truth/thresholds
  invention remains labeled

AUTHORITY:
  structural analogy → creative candidate generation only

FAILURE:
  correspondence cannot be abstracted without importing invalid source-domain assumptions = BLOCKED

## PIPE-CORE-NOVELTY-STORY-WRITER

FROM POINTER:
  CORE-NOVELTY-ENHANCER / creative candidate set

TO POINTER:
  CORE-STORY-WRITER / optional creative branch input

GATE:
  Writer is operating under a creative/generative domain configuration

SEMANTIC INVARIANTS:
  invented elements remain marked
  evidence-backed Reader state remains unchanged
  novelty does not arm a branch without domain-valid transition support

AUTHORITY:
  novel creative material → candidate branch generation only

FAILURE:
  invented element would contaminate evidence-bounded Reader state = BLOCKED

## PIPE-CORE-NOVELTY-DEVELOPMENT

FROM POINTER:
  CORE-NOVELTY-ENHANCER / structurally novel candidate

TO POINTER:
  CORE-DEVELOPMENT / optional challenger or design candidate

GATE:
  current development goal benefits from divergent ideation after baseline/direct answer exists

SEMANTIC INVARIANTS:
  frozen goalpost preserved
  hard constraints preserved
  candidate remains unverified until ordinary Development/Evaluation gates pass

AUTHORITY:
  creative divergence → development candidate only

FAILURE:
  novelty changes mandatory requirements or authority boundary = REJECT CANDIDATE
