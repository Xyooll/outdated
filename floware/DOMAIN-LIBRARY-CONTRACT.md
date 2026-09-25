# Xyool Domain Library Contract

Status: **CANDIDATE / VERIFICATION_PENDING**

Purpose: define durable, reusable domain knowledge that lets Xyool begin from accumulated internal knowledge before repeating external research.

Core law:

> **External evidence bootstraps the domain; the Domain Library preserves what Xyool has established, learned, rejected, and still does not know.**

The Domain Library is not a replacement for provenance, freshness checks, validation, or outside evidence.

## 1. Role

A domain library is the durable reusable knowledge layer for one domain.

It should let a future run answer:
- What does Xyool already know about this domain?
- Which rules/methods already exist?
- Where did they come from?
- Which parts have been validated, rejected, or superseded?
- What examples and failure boundaries already exist?
- What remains unknown or stale?
- What outside research is actually still necessary?

## 2. Repository shape

Preferred shape:

~~~text
domains/<domain>/library/
  README.md
  INDEX.md
  knowledge/
  cases/
  boundaries/
  open-questions/
~~~

The library may point to existing canonical domain artifacts instead of duplicating them.

Examples:
- rule objects remain canonical in a domain rule registry/rules directory;
- source records remain canonical in source registries;
- validation results remain canonical in research/validation artifacts;
- live state remains in domain state;
- user-originated philosophy remains in user-concept memory.

The Domain Library indexes and distills these into reusable domain knowledge.

## 3. Knowledge object contract

Each reusable knowledge object should expose, when applicable:

~~~text
KNOWLEDGE ID:
DOMAIN:
TYPE:
STATUS:
VERSION:
SCOPE:
SUMMARY:
CANONICAL POINTERS:
SOURCE / PROVENANCE:
FRESHNESS CLASS:
LAST REVIEWED:
VALIDATION STATUS:
KNOWN DEPENDENCIES:
KNOWN CONFLICTS:
KNOWN BOUNDARIES:
FAILURE / MISS NOTES:
SUPERSEDES:
SUPERSEDED BY:
OPEN QUESTIONS:
~~~

## 4. Knowledge types

Common types:

~~~text
DOMAIN FACT
RULE / METHOD POINTER
ONTOLOGY / VOCABULARY
STATE-MODEL KNOWLEDGE
TIMING / TRANSITION KNOWLEDGE
VALIDATION LESSON
FAILURE BOUNDARY
WORKED CASE
NEGATIVE / CONTROL CASE
SOURCE SYNTHESIS
CORRESPONDENCE HYPOTHESIS
MEANING OBJECT
SYMBOLIC CORPUS
CREATIVE HEURISTIC
OPEN QUESTION
~~~

## 5. Status ladder

Use statuses that preserve what has actually been earned:

~~~text
IMPORTED / UNREVIEWED
SOURCE-GROUNDED
DOMAIN-ESTABLISHED
IN TESTING
VALIDATED_FOR_SCOPE
SUPPORTED_WITH_BOUNDARIES
REJECTED
SUPERSEDED
STALE / REFRESH_REQUIRED
UNKNOWN
~~~

These statuses do not replace a domain's native rule-status vocabulary. The library may point to canonical rule status instead.

## 6. Reuse-first research rule

Correct order:

~~~text
DOMAIN QUESTION
→ QUERY DOMAIN LIBRARY
→ LOAD RELEVANT CANONICAL POINTERS
→ CHECK SCOPE + FRESHNESS + VALIDATION
→ SUFFICIENT?
    YES → USE INTERNAL KNOWLEDGE WITH PROVENANCE
    NO
      ↓
   RESEARCH ONLY MATERIAL GAPS
      ↓
   UPDATE / ADD CANONICAL DOMAIN ARTIFACTS
      ↓
   DISTILL REUSABLE LIBRARY KNOWLEDGE
~~~

Do not browse externally merely because an outside source exists if the same stable rule is already captured, current, and sufficient.

Do browse/refresh when:
- the fact is time-sensitive;
- provenance is weak;
- sources conflict;
- the question exceeds stored scope;
- validation status changed;
- a canonical rule/source was superseded;
- consequence warrants independent verification.

## 7. Provenance preservation

Internal reuse must never erase external origin.

Every source-derived knowledge object should retain pointers to:
- source record;
- canonical rule/method object;
- relevant research artifact;
- version/edition/date where material.

Xyool may become less dependent on repeated retrieval while remaining fully traceable to the evidence that bootstrapped the knowledge.

## 8. Distillation rule

Store reusable understanding, not copied source text.

Prefer:
- concise rule representation;
- structured method;
- boundary;
- dependency;
- contradiction;
- validation lesson;
- failure mode;
- source pointer.

Do not turn the Domain Library into an uncontrolled archive of external content.

## 9. Learning write-back

Learning should update the library when a result is reusable.

Examples:

~~~text
confirmed failure boundary
→ add/update boundary object

rule survives prospective test
→ update validation pointer/status

rule fails control
→ record rejection/boundary

new correspondence works in target domain
→ add tested local correspondence pointer
~~~

One incident must not silently become permanent domain knowledge.

## 10. Self-sufficiency metric

Useful domain maturity can be described by decreasing unnecessary external work, not by eliminating external sources.

Track conceptually:
- repeat questions answered from library;
- percentage of required rule/method coverage already internalized;
- external lookups avoided because knowledge is stable/current;
- stale/conflicted items requiring refresh;
- validation-backed vs source-only knowledge;
- unresolved open questions.

Self-sufficiency means **better starting state**, not isolation from new evidence.

## 11. Domain establishment integration

Domain Establishment must query the Domain Library before declaring a local knowledge/rule gap.

A missing item is classified only after:

~~~text
CHECK LIBRARY
→ CHECK CANONICAL POINTERS
→ CHECK FRESHNESS / SCOPE
→ ONLY THEN CLASSIFY MISSING DOMAIN KNOWLEDGE / RULE / SOURCE
~~~

Newly established domain knowledge should be indexed into the library before the establishment/update cycle closes.

## 12. Privacy

Domain libraries store reusable domain knowledge, not private user dossiers.

User-specific records belong only in explicitly authorized private/domain state surfaces.

Do not write sensitive personal data into a general domain library merely because it was used in an experiment.

## 13. Software boundary

Floware and repository artifacts are sufficient initially.

Future software may provide indexing/search/deduplication at scale only after Software Escalation proves the need.


## 14. Meaning-rich domains

When a domain stores symbolic, occult, metaphysical, ritual, narrative, or other meaning-bearing knowledge, use:
- `MEANING-CONTRACT.md`;
- `core/meaning-attribution.flow.md`.

The library should preserve:
- intrinsic/extrinsic/composite meaning type;
- system/tradition/framework;
- source/authorship;
- native meaning;
- semantic primitives;
- context/relationship conditions;
- validation status;
- creative-use status.

A meaning object may be reusable for creative work even when not empirically validated. The library must not conflate those authorities.

## 15. Creative heuristics

A domain library may preserve reusable creative heuristics or novelty lessons such as:
- productive correspondence jumps;
- useful inversions;
- effective ontology swaps;
- failed/noisy novelty operators.

These are creative-process knowledge, not domain facts.
