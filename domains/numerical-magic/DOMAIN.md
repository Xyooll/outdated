# Xyool Domain Manifest — Numerical Magic Language

Floware entrypoint:
`domains/numerical-magic/flows/numerical-analysis.flow.md`

New domain reasoning should route through this Flow. Existing deterministic calculation components remain supporting software where exactness requires them.

Status: **EXPERIMENTAL DOMAIN / SYMBOLIC SYSTEM / VALIDATION REQUIRED**

## 1. Domain identity

```text
Domain Name: numerical-magic
Domain Status: EXPERIMENTAL
Primary Objective: construct, parse, compare, and reverse-engineer symbolic numerical formulas for a magic-school language while preserving arithmetic correctness, declared symbolic meanings, provenance, and uncertainty
Decision Maker / User: Xyool operator, designer, practitioner, or researcher
Unit of Decision: numerical formula, reduction chain, letter-carrier expression, symbolic interpretation, or intended construction
```

This domain is a symbolic language system. Arithmetic statements are factual and reproducible; symbolic meanings are declared conventions or hypotheses and must not be presented as scientifically established causal laws.

The domain deliberately separates four layers:

```text
LAYER A — ARITHMETIC
exact digits, sums, reduction chains, digital roots, modular family membership

LAYER B — CARRIER SYSTEM
letter-to-number mappings or other symbol-to-number mappings

LAYER C — SYMBOLIC SEMANTICS
root meanings, ordered-stage meanings, repetition, reversal, grouping, and local glyph meanings

LAYER D — PRACTICE / OUTCOME
how a user applies a formula and what, if anything, is observed afterward
```

A valid arithmetic reduction does not by itself prove that a symbolic interpretation or magical effect is objectively causal.

---

## 2. Core objects / entities

```text
ROOT
DIGIT TOKEN
COMPOUND NUMBER
SEQUENCE
REDUCTION NODE
REDUCTION CHAIN
DIGITAL ROOT
ROOT FAMILY
CARRIER SYMBOL
LETTER CARRIER
GLYPH VARIANT
ORDERED PATH
REVERSED PATH
REPETITION
INTENTION
TARGET
INTERPRETATION
CONSTRUCTION
OBSERVED OUTCOME
VALIDATION RECORD
```

---

## 3. Canonical 1–9 root registry

These meanings are **domain-canonical symbolic definitions**, not universal facts.

```text
1 — Origin / initiation / will / identity
2 — Relation / polarity / receptivity / cooperation
3 — Creation / expression / communication / growth
4 — Structure / foundation / order / stabilization
5 — Change / motion / adaptation / freedom
6 — Harmony / integration / care / responsibility
7 — Knowledge / mystery / analysis / inward mastery
8 — Power / materialization / resources / authority
9 — Completion / culmination / transcendence / release
```

### Zero

`0` is not a tenth root in this system. It is a **modifier** representing field, potential, void, openness, or an unfilled container. It contributes zero arithmetically but may modify a compound symbolically.

Example:

```text
10 → 1 + 0 → 1
```

Arithmetic root: `1`.
Symbolic reading: initiation/origin emerging through or surrounded by potential; optionally, a completed cycle returning to a new beginning.

---

## 4. Observable / reproducible evidence

Directly reproducible domain evidence includes:

```text
input number or symbol string
individual digits
exact arithmetic sum
intermediate reduction values
digital root
root-family membership
letter-carrier mapping under a declared alphabet system
sequence order
reversal relationship
repetition count
machine-generated parse output
```

Symbolic interpretations and outcome claims are separate evidence types.

---

## 5. Latent / uncertain state

```text
whether a symbolic meaning is personally salient
whether a formula has any causal effect beyond interpretation or behavior
which symbolic layer matters most to a practitioner
whether order changes experienced meaning in practice
whether repetition changes anything beyond salience
whether a letter glyph contributes meaning beyond its numeric carrier
whether an observed outcome exceeds chance, expectation, behavior change, or selection effects
```

These may not be silently converted into certainty.

---

## 6. State model

### A. Input state

```text
DECLARED
AMBIGUOUS
MALFORMED
UNSUPPORTED
```

### B. Arithmetic state

```text
PARSED
SUMMED
REDUCED
VERIFIED
FAILED
```

### C. Semantic state

```text
ROOT-ONLY
COMPOUND-INTERPRETED
ORDERED-PATH-INTERPRETED
GLYPH-INTERPRETED
INTENTION-MAPPED
AMBIGUOUS
```

### D. Validation state

```text
CONVENTION
HYPOTHESIS
PROSPECTIVE TEST
OBSERVED MATCH
OBSERVED MISS
AMBIGUOUS RESULT
REJECTED
SUPERSEDED
```

---

## 7. Important transitions

```text
raw expression → parsed tokens
parsed tokens → ordered symbolic path
ordered digits → arithmetic sum
sum → next reduction node
reduction node → final digital root
intention → candidate root target
root target → candidate compound family
candidate compound → selected ordered construction
letter string → numeric carrier sequence
prospective symbolic hypothesis → observed match / miss / ambiguous
```

---

## 8. Domain laws

### Law 1 — Preserve the whole reduction chain
Never collapse a number directly to its digital root when intermediate compounds are available.

Example:

```text
7777 → 28 → 10 → 1
```

All four states are retained.

### Law 2 — Root is identity; compound is construction
The digital root describes the deepest canonical root. The unreduced compound describes how that root is constructed.

### Law 3 — Order matters symbolically
`38` and `83` share the same arithmetic sum and root but are different ordered paths.

```text
38 = 3 → 8
83 = 8 → 3
```

### Law 4 — Arithmetic does not depend on interpretation
Changing a symbolic meaning never changes the mathematical reduction.

### Law 5 — Symbolic meanings must declare provenance
Each meaning should be tagged as one of:

```text
DOMAIN CANONICAL
INHERITED NUMEROLOGY CONVENTION
LOCAL GLYPH EXTENSION
USER-DEFINED
EXPERIMENTAL
```

### Law 6 — Repetition amplifies symbolic weight, not mathematical truth
Repeated digits increase salience and recursive emphasis in the symbolic grammar. This does not establish greater empirical power.

### Law 7 — Reverse paths are related but not identical
`AB` and `BA` have equal digit sums but different process direction.

### Law 8 — Same root does not mean same formula
Every member of a root family shares a digital root while retaining its own construction history.

### Law 9 — Zero modifies; it does not replace the 1–9 roots
Zero may alter a reading while remaining arithmetically neutral.

### Law 10 — No hidden master-number exception
Intermediate compounds such as `11`, `22`, and `33` are preserved as meaningful nodes but are still reduced unless a declared alternate profile explicitly stops reduction.

### Law 11 — Carrier and meaning are separate
A letter may carry a number because of a declared mapping. Any additional letter-specific symbolic meaning is a separate layer.

### Law 12 — Construction should be reversible
Given a target intention, the system should be able to search candidate formulas; given a formula, it should be able to explain its path back to the same declared rules.

---

## 9. Root-family ladder

For root `r` in `1..9`, the canonical arithmetic family is:

```text
r, r+9, r+18, r+27, ...
```

Equivalently, positive integers whose digital root is `r` belong to the same root family.

Example for root `9`:

```text
9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, ...
```

Members share the root `9` but not the same ordered construction.

---

## 10. Pythagorean letter carrier profile

The default letter carrier profile is the repeating 1–9 alphabet mapping:

```text
1: A J S
2: B K T
3: C L U
4: D M V
5: E N W
6: F O X
7: G P Y
8: H Q Z
9: I R
```

This profile is used only when explicitly selected.

Example:

```text
G P Y → 7 7 7 → 21 → 3
```

### Local 7-glyph extension

The current experimental local semantics for the three `7` carriers are:

```text
G — Gnosis / investigation / discovery
P — Projection / application / directed power
Y — Choice / branching / transcendence
```

These are **LOCAL GLYPH EXTENSIONS**, not standard Pythagorean numerology meanings.

Thus:

```text
GPGY
→ 7-7-7-7
→ 28
→ 10
→ 1
```

while the glyph path can additionally be read as:

```text
Gnosis → Projection → Gnosis → Choice
```

---

## 11. Construction model

A complete formula has up to five simultaneous descriptions:

```text
1. SURFACE FORM        the literal number or glyph string
2. ORDERED PATH        the stage-by-stage root meanings
3. COMPOUND SUM        the first arithmetic synthesis
4. REDUCTION CHAIN     every subsequent reduction node
5. FINAL ROOT          the deepest 1–9 identity
```

Example:

```text
38
Surface: 38
Ordered path: Creation → Materialization
Compound sum: 11
Reduction chain: 38 → 11 → 2
Final root: Relation
```

Interpretive short form:

> creative expression directed into material manifestation, resolving toward relation/exchange.

---

## 12. Reverse engineering from intention

The canonical reverse-engineering procedure is:

```text
INTENTION
→ identify desired primary root(s)
→ choose desired final root
→ search candidate compounds in that root family
→ evaluate digit order as process
→ evaluate intermediate compounds
→ optionally select a carrier/glyph representation
→ record the formula and rationale
→ if testing in practice, freeze the expected outcome before observation
```

Example intention:

```text
make money through art
```

Candidate path:

```text
3 = creation / art / expression
8 = materialization / resources
38 = creation → materialization
38 → 11 → 2
```

The final `2` may be interpreted as exchange, audience, partnership, or relationship, but that is a symbolic reading, not a guarantee of income.

---

## 13. Actions

Permitted domain actions include:

```text
parse
sum
reduce
verify
interpret
compare
reverse
mirror
generate root family
generate candidate compounds
map letters to numbers
map intention to candidate roots
record a prospective symbolic hypothesis
record outcome
revise a local semantic definition
reject a mapping
```

---

## 14. Success / payoff definition

The domain has separate success layers:

```text
ARITHMETIC SUCCESS
all sums and reduction chains are correct

LANGUAGE SUCCESS
the same expression receives the same interpretation under the same declared rules

CONSTRUCTION SUCCESS
reverse engineering produces candidate formulas that transparently encode the intended symbolic path

REPRODUCIBILITY SUCCESS
another operator can reconstruct the same parse and reduction from the same settings

EMPIRICAL SUCCESS
only if separately tested: predeclared outcome hypotheses discriminate beyond relevant controls or base rates
```

---

## 15. Failure / loss definition

```text
wrong arithmetic
skipped reduction node
silent change of root meaning
silent change of letter mapping
confusing a root with a compound construction
claiming AB and BA are identical because their sums match
post-hoc reinterpretation after seeing an outcome
claiming empirical causality from symbolic consistency alone
failing to distinguish inherited conventions from local inventions
using an ambiguous formula without declaring how it is parsed
```

---

## 16. Source hierarchy

### Arithmetic

1. direct calculation;
2. independent machine verification.

### Carrier mapping

1. explicitly declared mapping table;
2. documented tradition-specific mapping;
3. local experimental mapping.

### Symbolic meaning

1. domain-canonical root registry;
2. explicitly named inherited numerology convention;
3. local glyph extension;
4. user-defined meaning;
5. free-form intuition.

### Outcome claims

1. prospective frozen record;
2. timestamped external outcome;
3. contemporaneous user report;
4. retrospective report;
5. narrative reconstruction.

---

## 17. Invalidation conditions

A formula or interpretation is blocked or invalidated when:

```text
arithmetic is wrong
input string is malformed
carrier profile is unknown
symbolic profile is unspecified where multiple profiles conflict
required digit order is missing
an interpretation contradicts the declared root registry without being labeled as an override
outcome criteria were changed after observation
```

---

## 18. Validation architecture

### Track A — arithmetic correctness
Test known reductions and root-family membership.

### Track B — parser reproducibility
Same input + same profile must return the same parse.

### Track C — semantic determinism
Same formula + same symbolic registry must generate the same ordered root sequence and provenance labels.

### Track D — reverse-engineering consistency
A generated candidate must decode back into the intention components it was selected to represent.

### Track E — empirical practice testing
If users test real-world effects, predictions must be frozen prospectively with controls and explicit miss conditions.

See `VALIDATION.md`.

---

## 19. Anti-lookahead discipline

For any claimed real-world effect:

```text
FREEZE FORMULA
→ FREEZE INTENTION
→ FREEZE EXPECTED OUTCOME
→ FREEZE TIME WINDOW
→ OBSERVE
→ SCORE MATCH / MISS / AMBIGUOUS
→ REVISE ONLY AFTER SCORING
```

Changing the formula or interpretation after seeing the result creates a new hypothesis and does not rescue the old one.

---

## 20. Miss handling

```text
MISS / AMBIGUOUS
→ verify arithmetic
→ verify carrier profile
→ verify semantic profile
→ check whether the expected outcome was specific enough
→ identify the smallest failed assumption
→ preserve the miss
→ revise only the local rule that the evidence actually challenges
```

Miss categories:

```text
ARITHMETIC MISS
PARSER MISS
CARRIER MISS
SEMANTIC-CONFLICT MISS
ORDER MISS
INTENTION-MAPPING MISS
OUTCOME MISS
BASE-RATE / FALSE-POSITIVE MISS
RETROFIT MISS
UNKNOWABLE
```

---

## 21. Imported Xyool principles

The following Xyool core principles are implemented directly:

```text
identity before inference
evidence/source separation
state and transition tracking
explicit uncertainty
invalidation
anti-lookahead
miss-to-question learning
positive and negative controls
principle vs local calibration separation
reproducibility
```

No stock-market calibration, timing window, or action rule is imported.

---

## 22. Explicitly local calibrations

```text
1–9 symbolic definitions
zero modifier meaning
letter carrier profile
G/P/Y glyph extensions
repetition semantics
reversal semantics
compound-reading style
intention-to-root vocabulary
whether any alternate profile preserves selected compounds without final reduction
```

All may evolve, but changes must be versioned.

---

## 23. Readiness status

```text
[x] objective defined
[x] entities defined
[x] evidence hierarchy defined
[x] state model defined
[x] transition model defined
[x] actions defined
[x] success/failure defined
[x] freshness/invalidation logic defined
[x] miss loop defined
[x] local calibrations separated
[x] worked examples provided
[x] negative/control logic defined
[ ] empirical efficacy validated
```

Therefore the domain remains:

```text
EXPERIMENTAL
```

Arithmetic and parsing components may be treated as deterministic utilities; symbolic and efficacy claims remain convention- or hypothesis-level unless separately tested.
