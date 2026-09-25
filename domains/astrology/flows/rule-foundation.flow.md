# FLOW — Astrology Rule Foundation

FLOW ID: ASTROLOGY-RULE-FOUNDATION-V1
STATUS: **EXPERIMENTAL / VERIFICATION_PENDING**
DOMAIN: astrology
JOB: serve as a domain-local establishment helper that builds source-grounded, versioned, falsifiable astrology rule objects for a named system/technique and returns them to Core Domain Establishment
AUTHORITY: local rule identity, provenance, representation, and rule-cohort readiness only; no authority to declare the domain function READY_FOR_CONFIGURATION, validate efficacy, promote a rule, or make predictions
PARENT GOALPOST: ../../../research/system-tests/astrology-predictive-v1-2026-09-24/GOALPOST.md
UPSTREAM FLOWS: Core Domain Establishment, Research
DOWNSTREAM FLOWS: Core Domain Establishment
INBOUND PIPES: ../PLUMBING.md#pipe-astrology-establishment-rule-foundation, ../PLUMBING.md#pipe-astrology-research-rule-foundation
OUTBOUND PIPES: ../PLUMBING.md#pipe-astrology-rule-foundation-establishment
SOFTWARE DEPENDENCIES: none

## GOAL

Create a bounded rule set that accurately represents the named astrology system or an explicitly labeled Xyool hypothesis, then return that local rule state to Core Domain Establishment for function-readiness review.

Core law:

> **A system definition is not a rule set, and a rule schema is not an established rule.**

## GOALPOST

A local rule cohort may be RULESET_READY_FOR_EXPERIMENT only when every included material rule has:
- stable rule ID and version;
- system ID and technique;
- rule class;
- source provenance or explicit XYOOL_HYPOTHESIS status;
- source reference/locator sufficient to recover the rule basis;
- required inputs;
- calculation prerequisites;
- trigger configuration;
- native interpretation;
- timing start/peak/end rules when timing is claimed;
- orb/threshold/correlation settings when applicable;
- known dependencies/conflicts;
- falsification condition;
- boundaries/known exceptions where material;
- explicit capability translation only if separately defined;
- status that does not overstate predictive support.

## INPUT STATE

Load first:
- ../library/INDEX.md;
- relevant library knowledge/boundary/open-question entries;
- canonical pointers referenced by those entries.

Required:
- target system ID;
- target technique/subsystem;
- intended job: descriptive / timing / predictive / synthesis;
- applicable source hierarchy;
- existing source registry;
- existing rule registry/schema;
- existing rule files;
- experiment target if rules are being prepared for a specific cohort.

## EVIDENCE

Prefer:
- foundational/primary tradition texts;
- living-tradition sources;
- established scholarly or practitioner sources tied to a named tradition;
- modern-system primary sources for modern systems;
- explicit Xyool hypothesis only when no sourced traditional rule is being claimed.

Source authenticity and predictive efficacy remain separate questions.

## PROCESS

~~~text
LOCK TARGET SYSTEM + TECHNIQUE
→ QUERY ASTROLOGY DOMAIN LIBRARY
→ LOAD EXISTING CANONICAL RULE / SOURCE POINTERS
→ AUDIT EXISTING RULE COVERAGE
→ IF ADEQUATE CURRENT RULE OBJECTS EXIST:
     VERIFY VERSION / PROVENANCE / EXPERIMENT READINESS
→ ELSE:
     RESEARCH NAMED SOURCES
     EXTRACT MINIMUM TESTABLE RULE STATEMENTS
     CLASSIFY RULE TYPE
     ASSIGN RULE ID + VERSION
     RECORD SOURCE + PROVENANCE
     DEFINE REQUIRED INPUTS / CALCULATION PREREQUISITES
     DEFINE TRIGGER
     PRESERVE NATIVE INTERPRETATION
     DEFINE TIMING BOUNDARIES IF CLAIMED
     DEFINE CONFLICTS / DEPENDENCIES
     DEFINE FALSIFICATION CONDITION
     LABEL STATUS
→ SEPARATELY DEFINE ANY XYOOL CAPABILITY TRANSLATION
→ CHECK SEARCH-SPACE SIZE / DUPLICATION
→ EMIT LOCAL RULESET READINESS:
     RULESET_READY_FOR_INTERPRETATION
     RULESET_READY_FOR_EXPERIMENT
     PARTIAL
     BLOCKED
→ RETURN TO CORE DOMAIN ESTABLISHMENT
→ CORE DECIDES FUNCTION ESTABLISHMENT STATUS
~~~

## RULE CLASSES

Use the canonical registry classes where applicable:
- NATIVE_CALCULATION_RULE
- NATIVE_INTERPRETIVE_RULE
- TIMING_RULE
- CAPTURE_RULE
- CAPABILITY_TRANSLATION_RULE
- CONVERGENCE_RULE
- TUNER_COMPRESSION_RULE
- ACTION_MAPPING_RULE
- CORRESPONDENCE_RULE

Do not hide an experimental Xyool translation inside a sourced native rule.

## GATES

Before RULESET_READY_FOR_EXPERIMENT:
- target system identity is unambiguous;
- every rule is recoverable to a source or explicit hypothesis;
- rule wording is narrow enough to fail;
- timing rules have finite boundaries;
- experiment-relevant settings are locked;
- contradictions between sources are preserved as separate rules or explicitly resolved;
- capability translations have their own rule IDs/status;
- no efficacy claim is inferred from source authority;
- no large unconstrained interpretation library is silently admitted into the cohort.

## ADAPTATION

If sources disagree, preserve separate rule versions/lineages rather than forcing consensus.

If a source provides broad symbolism but no timing rule, the local rule set may be RULESET_READY_FOR_INTERPRETATION but not RULESET_READY_FOR_EXPERIMENT for timing prediction.

If a useful predictive mapping must be invented by Xyool, label it DOMAIN_HYPOTHESIS and validate it prospectively; do not attribute it to the source tradition.

## BOUNDARIES

This Flow does not:
- prove that a rule works;
- choose outcomes after seeing cases;
- create numeric probabilities;
- promote a rule beyond its evidence;
- collapse multiple traditions into one rule;
- make a forecast.

## FAIL-CLOSED CONDITIONS

Return PARTIAL/BLOCKED when:
- source provenance is materially ambiguous;
- target system/technique is not locked;
- timing behavior is needed but no timing rule exists;
- rule trigger/falsification cannot be stated;
- a capability translation is being treated as native tradition without evidence;
- the allowed rule/search space cannot be bounded.

## OUTPUT STATE

~~~text
RULESET ID:
SYSTEM ID:
TECHNIQUE:
SOURCE SET:
RULE IDS / VERSIONS:
RULE COUNT:
RULE CLASSES:
NATIVE RULE COVERAGE:
TIMING RULE COVERAGE:
CAPABILITY-TRANSLATION COVERAGE:
CONFLICTS:
DEPENDENCIES:
SEARCH-SPACE SIZE:
LOCAL RULESET READINESS:
TARGET DOMAIN FUNCTION:
CORE ESTABLISHMENT REVIEW REQUIRED: YES
BLOCKERS:
VALIDATION STATUS:
~~~

## LEARNING HOOK

Rule provenance errors, false-positive-prone formulations, unresolved source conflicts, and rules that fail prospectively may route to Learning after preserving the original rule version.

## SOFTWARE / HARD-LIMIT BOUNDARY

NONE — FLOWARE SUFFICIENT

Structured files may store the rules. Software is unnecessary until scale/version enforcement proves a hard limit.

## COMPLEXITY RULE

Establish only the rule set needed for the current experiment or interpretive job. Do not ingest an entire astrology literature merely because it exists.


## Core ownership boundary

This Flow is a domain-specific establishment subflow under `floware/core/domain-establishment.flow.md`.

Its output means:

~~~text
the local Astrology rule set is sufficiently specified for a stated purpose
~~~

It does **not** mean:

~~~text
the Astrology domain function is READY_FOR_CONFIGURATION
~~~

Core Domain Establishment must re-evaluate the complete function contract, including rule coverage, evidence, state/time, outputs, validation, and Flow ownership, before updating `../ESTABLISHMENT.md`.


## LIBRARY WRITE-BACK

After Core Domain Establishment accepts a reusable rule-foundation result:
- update canonical rule/source artifacts first;
- distill the reusable lesson/pointer into `../library/`;
- preserve source provenance, validation status, conflicts, and open blockers;
- do not copy large source passages into the library.

If a rule is rejected or superseded later, update the library status rather than deleting its history.
