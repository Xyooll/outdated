# FLOW — Intrinsic Degree Foundation

FLOW ID: ASTROLOGY-INTRINSIC-DEGREE-FOUNDATION-V1
STATUS: **EXPERIMENTAL / VERIFICATION_PENDING**
DOMAIN: astrology
JOB: establish versioned intrinsic-meaning candidates for local 30-degree identity and absolute 360-degree identity without collapsing source lineages
AUTHORITY: degree-meaning research/synthesis authority only; no predictive efficacy authority
PARENT GOALPOST: ../../research/system-tests/astrology-predictive-v1-2026-09-24/GOALPOST.md
UPSTREAM FLOWS: Core Domain Establishment, Core Meaning Attribution, Astrology Rule Foundation, Core Domain Library, Research
DOWNSTREAM FLOWS: Core Meaning Attribution, Core Domain Establishment, Astrology Analysis, Core Learning after validation
INBOUND PIPES: ../PLUMBING.md#pipe-astrology-establishment-intrinsic-degree, ../PLUMBING.md#pipe-astrology-meaning-intrinsic-degree
OUTBOUND PIPES: ../PLUMBING.md#pipe-astrology-intrinsic-degree-meaning, ../PLUMBING.md#pipe-astrology-intrinsic-degree-establishment
SOFTWARE DEPENDENCIES: none

## GOAL

Create falsifiable, source-traceable intrinsic degree candidates for two distinct coordinate identities:

~~~text
LOCAL30
position within a sign: 0°00'–29°59'

ABS360
absolute zodiac address: 0°00'–359°59'
~~~

Core law:

> **Local degree meaning and absolute degree meaning are separate hypotheses attached to the same longitude.**

## GOALPOST

A degree-meaning candidate is ready for controlled testing only when:
- coordinate/indexing convention is frozen;
- source lineage is named;
- dependent corpora are identified;
- source-derived and Xyool-created meanings are separated;
- candidate meaning is concise enough to fail;
- conflicts are preserved;
- discovery cases are separated from confirmation cases;
- a null/permutation control exists.

## INPUT STATE

Load:
- ../STAR-DEGREE.md;
- ../library/knowledge/degree-coordinate-duality.md;
- ../library/knowledge/degree-corpus-lineage.md;
- ../SOURCE-REGISTRY.md;
- ../RULE-REGISTRY.md;
- local/absolute degree corpora under ../rules/;
- relevant historical/modern degree sources;
- validation / null / search-space controls.

## EVIDENCE

Source families may include:
- monomoiria / ancient degree rulers;
- Sabian Symbols;
- Charubel;
- La Volasfera / Sepharial;
- Kozminsky;
- Janduz;
- modern local 0–29 Degree Theory;
- future separately identified corpora.

Source agreement is not automatically independent evidence.

## PROCESS

~~~text
RECEIVE DEGREE-MEANING RESEARCH REQUEST
→ FREEZE COORDINATE CONTRACT
→ CHOOSE LOCAL30 or ABS360 or BOTH
→ INVENTORY EXISTING CORPORA
→ NORMALIZE INDEXING
→ BUILD SOURCE-DEPENDENCY GROUPS
→ EXTRACT SEMANTIC PRIMITIVES
→ FOR EACH SOURCE / XYOOL CANDIDATE:
     ROUTE THROUGH CORE-MEANING-ATTRIBUTION
     TYPE = INTRINSIC
     CLAIM MODE = SYMBOLIC / INTERPRETIVE unless stronger authority is independently earned
     PRESERVE SOURCE / AUTHORSHIP
→ PRESERVE CONFLICTS
→ GENERATE SOURCE-DERIVED CANDIDATES
→ IF XYOOL SYNTHESIS:
     LABEL DOMAIN HYPOTHESIS
     RECORD CONTRIBUTING CORPORA
     RECORD DEPENDENCY GROUPS
→ DEFINE NULL / PERMUTATION CONTROL
→ FREEZE CANDIDATE VERSION
→ RETURN TO CORE DOMAIN ESTABLISHMENT
~~~

## LOCAL30 SYNTHESIS

For local degree i in 0..29:

~~~text
LOCAL DEGREE i
→ modern local-degree source candidates
→ compare all 12 absolute zodiac cells sharing local i
→ identify recurring semantic primitives across independent 360 corpora
→ subtract sign-specific language where possible
→ emit XYOOL.LOCAL30 candidate
~~~

Do not infer a universal local meaning merely because one modern system assigns one.

## ABS360 SYNTHESIS

For absolute degree j in 0..359:

~~~text
ABSOLUTE DEGREE j
→ monomoiria ruler
→ independent 360 symbolic corpora
→ dependent-corpus graph
→ epoch-specific stellar field kept separate
→ source-specific meanings
→ candidate shared primitives + conflicts
→ emit XYOOL.ABS360 candidate
~~~

The stellar field is not itself an intrinsic-degree meaning and remains a separate feature family.

## INDEXING GATE

Always preserve:

~~~text
zero_based_index
one_based_ordinal
exact_degree
~~~

0°00'–0°59' is the first ordinal degree in traditions that use ordinal degree symbols.

If a source's indexing convention is ambiguous:
**BLOCK SYNTHESIS FOR THAT SOURCE.**

## GATES

Before candidate creation:
- source identity recoverable;
- coordinate/index convention recoverable;
- no silent source-family merge;
- copyright-safe paraphrase/semantic primitives only where required.

Before testing:
- candidate meaning frozen;
- prediction/description target predefined;
- null permutation available;
- source corpus choice frozen.

## ADAPTATION

If multiple corpora disagree:
- preserve disagreement;
- do not average incompatible meanings into vague prose;
- test corpus-specific and synthesis variants separately.

If a local degree meaning appears to be explained by sign wrappers:
- downgrade local intrinsic claim.

If an absolute degree effect is explained by stellar neighborhood:
- preserve star explanation separately and downgrade intrinsic claim.

## BOUNDARIES

This Flow does not:
- declare any degree meaning empirically true;
- use a subject case to both invent and validate a meaning;
- convert number symbolism into a rule without provenance;
- count dependent corpora as independent confirmation;
- treat exact coordinate calculation as semantic validation.

## FAIL-CLOSED CONDITIONS

Return PARTIAL / BLOCKED when:
- source indexing is unresolved;
- primary/secondary lineage is unclear enough to change meaning;
- candidate becomes too broad to falsify;
- synthesis depends on outcome-aware editing;
- local/absolute coordinate identities are mixed.

## OUTPUT STATE

~~~text
DEGREE MEANING CANDIDATE ID:
COORDINATE TYPE: LOCAL30 / ABS360
INDEX ZERO:
ORDINAL:
EXACT RANGE:
SOURCE CORPORA:
DEPENDENCY GROUPS:
SOURCE-DERIVED PRIMITIVES:
CONFLICTS:
XYOOL SYNTHESIS IF ANY:
STATUS:
NULL CONTROL:
DISCOVERY CASES:
VALIDATION CASES:
~~~

## LEARNING HOOK

Track:
- candidates that fail after controls;
- meanings only supported by dependent source families;
- indexing mistakes;
- local meanings that disappear after sign control;
- absolute meanings that disappear after star-field control.

## SOFTWARE / HARD-LIMIT BOUNDARY

NONE — FLOWARE SUFFICIENT

## COMPLEXITY RULE

Prefer sparse semantic primitives over elaborate prose. A meaning that can describe almost anything is not useful.


## CORE MEANING ATTRIBUTION BINDING

Intrinsic Degree Foundation does not own a separate semantic ontology.

Every degree-meaning candidate must be representable as a Core meaning object under:
`../../../floware/MEANING-CONTRACT.md`
and
`../../../floware/core/meaning-attribution.flow.md`.

For local/absolute intrinsic candidates:

~~~text
MEANING TYPE = INTRINSIC
OBJECT / PATTERN = LOCAL30 degree cell or ABS360 degree cell
SYSTEM / FRAMEWORK = named corpus or Xyool intrinsic-degree synthesis
SOURCE / AUTHORSHIP = tradition / source / user / Xyool
NATIVE MEANING = source-preserved or synthesis wording
SEMANTIC PRIMITIVES = sparse normalized primitives
VALIDATION STATUS = source-only / hypothesis / in-testing / supported / rejected
~~~

Extrinsic Astrology layers remain separate Core meaning objects, for example:

~~~text
HOUSE CONTEXT
SIGN / DECAN / BOUND CONTEXT
RULER / DISPOSITOR RELATION
STELLAR NEIGHBORHOOD INTERPRETATION
ASPECT RELATIONSHIP
TIMING ACTIVATION
~~~

These normally use MEANING TYPE = EXTRINSIC because their meaning depends on relation, placement, or context.

A final chart interpretation may become:

~~~text
INTRINSIC DEGREE MEANING
+ EXTRINSIC HOUSE / SIGN / STAR / RELATION MEANINGS
→ COMPOSITE MEANING
~~~

The composite must preserve its contributing meaning IDs and must not count them as independent evidence merely because multiple labels agree.
