# Numerical Magic Language — Grammar and Construction Rules

Status: **DOMAIN CANONICAL GRAMMAR v1.0 / SYMBOLIC**

This file defines how numerical expressions are parsed and interpreted inside the `numerical-magic` domain.

## 1. The four simultaneous readings

Every expression is read through four independent channels:

```text
SEQUENCE      — what happens first, second, third, ...
SUM           — the first synthesis of all digits
REDUCTION     — the chain of deeper compounds
ROOT          — the final 1–9 identity
```

Optional fifth channel:

```text
GLYPH         — letter- or symbol-specific nuance when a declared carrier profile is used
```

Never substitute one channel for another.

---

## 2. Canonical root vocabulary

```text
1 ORIGIN        initiate, begin, direct, identify, will
2 RELATION      connect, pair, receive, cooperate, exchange
3 CREATION      create, express, communicate, grow, imagine
4 STRUCTURE     stabilize, order, ground, build, contain
5 CHANGE        move, adapt, alter, liberate, transition
6 HARMONY       integrate, balance, care, reconcile, sustain
7 KNOWLEDGE     know, investigate, analyze, reveal, master inwardly
8 MANIFESTATION materialize, resource, empower, organize, govern
9 COMPLETION    complete, culminate, transcend, release, close
```

These words form the default intention-to-root vocabulary. Synonyms may be added without changing the root's central definition.

---

## 3. Ordered concatenation

A multi-digit number is interpreted left to right as an ordered path.

```text
AB = A → B
ABC = A → B → C
ABCD = A → B → C → D
```

Example:

```text
38
3 → 8
Creation → Manifestation
```

This does **not** mean `3` and `8` become mathematically directional. Direction is symbolic grammar layered over the literal digit order.

---

## 4. Compound synthesis

The first synthesis is the sum of the digits.

```text
38 → 3 + 8 = 11
```

The compound `11` is preserved before further reduction.

```text
38 → 11 → 2
```

Therefore `38` has:

```text
path: Creation → Manifestation
compound: 11
root: Relation
```

---

## 5. Full reduction-chain rule

Repeatedly sum decimal digits until a single non-zero digit remains.

Examples:

```text
7777 → 28 → 10 → 1
738  → 18 → 9
2738 → 20 → 2
9999 → 36 → 9
```

Every node is retained as part of the formula's construction history.

---

## 6. Root-family ladder

For any root `r` from 1 through 9:

```text
F(r,k) = r + 9k,  k = 0,1,2,...
```

Examples:

```text
Root 1: 1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100, ...
Root 2: 2, 11, 20, 29, 38, 47, 56, 65, 74, 83, 92, 101, ...
Root 9: 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, ...
```

Family membership identifies the final root only. The digits still define the path.

---

## 7. Reversal

For a two-stage formula `AB`, the reverse is `BA`.

```text
38 = Creation → Manifestation
83 = Manifestation → Creation
```

Both reduce:

```text
3 + 8 = 11 → 2
8 + 3 = 11 → 2
```

Rule:

> Equal root does not imply equal process.

Use reversal to distinguish **means → end** from **resource → expression**.

---

## 8. Repetition

Repeated digits are interpreted as recursive emphasis on the same root function.

```text
7    Knowledge
77   Knowledge → Knowledge
777  Knowledge → Knowledge → Knowledge
7777 Knowledge → Knowledge → Knowledge → Knowledge
```

The repeated sequence still follows ordinary arithmetic:

```text
77   → 14 → 5
777  → 21 → 3
7777 → 28 → 10 → 1
```

Therefore repetition can produce a final root different from the repeated digit.

Interpretive rule:

> Repetition increases the symbolic weight of the repeated stage while the reduction chain describes the synthesis produced by that repetition.

No claim of objectively increased supernatural force is implied.

---

## 9. Zero modifier

Zero contributes no arithmetic value but may be read as potential, void, field, or container.

```text
10 → Origin + Potential → 1
20 → Relation + Potential → 2
30 → Creation + Potential → 3
```

A zero does not erase the preceding digit and is not treated as a root.

Repeated zeros may be preserved symbolically:

```text
100 = Origin held through two potential/field modifiers
100 → 1
```

---

## 10. Intermediate doubles and triples

Compounds such as `11`, `22`, `33`, etc. are retained but are not automatically exempt from reduction.

Examples:

```text
11 → 2
22 → 4
33 → 6
44 → 8
55 → 10 → 1
66 → 12 → 3
77 → 14 → 5
88 → 16 → 7
99 → 18 → 9
```

The repeated form supplies an additional repetition reading; the final root remains available.

---

## 11. Letter carriers

Default profile: Pythagorean repeating 1–9 assignment.

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

A letter string has two tracks:

```text
GLYPH TRACK   literal letters and any declared glyph meanings
NUMBER TRACK  mapped numeric sequence and reduction
```

Example:

```text
GPGY
Glyph track: G → P → G → Y
Number track: 7 → 7 → 7 → 7
Reduction: 7777 → 28 → 10 → 1
```

Local experimental meanings currently defined only for the 7-carrier triad:

```text
G = Gnosis / investigation / discovery
P = Projection / application / directed power
Y = Choice / branching / transcendence
```

Do not invent letter-specific meanings for other carriers without registering them as a new local extension.

---

## 12. Construction from intention

Use this compiler-like procedure.

### Step 1 — Extract semantic verbs/nouns

Example intention:

```text
make money by being an artist
```

Extract:

```text
art / create / express
money / material result / resource
```

### Step 2 — Map concepts to roots

```text
art / create / expression → 3
money / materialization / resources → 8
```

### Step 3 — Determine process order

```text
create first, materialize second → 38
```

### Step 4 — Compute full reduction

```text
38 → 11 → 2
```

### Step 5 — Interpret the result layer

```text
2 → relation / exchange / audience / partnership
```

### Step 6 — Preserve alternatives

```text
83 = resources/power directed into creation
```

It is not interchangeable with `38` even though both reduce to `2`.

---

## 13. Three-stage and four-stage formulas

Example:

```text
738
7 Knowledge
3 Creation
8 Manifestation
```

Read:

```text
Knowledge → Creation → Manifestation
738 → 18 → 9
```

Possible symbolic paraphrase:

> understand or discover, express what is known creatively, bring it into material form, resolving toward completion.

Four-stage example:

```text
2738
2 Relation
7 Knowledge
3 Creation
8 Manifestation
2738 → 20 → 2
```

Path:

```text
Connect → Know → Create → Materialize
```

Root:

```text
2 Relation
```

---

## 14. Closed-circuit formulas

A formula is called **root-returning** when its final root equals its first digit.

Example:

```text
2738 starts with 2 and reduces to 2
```

This may be symbolically classified as a closed or returning circuit:

```text
2 → 7 → 3 → 8 → 20 → 2
```

This is a local grammar property, not a claim of physical closure or conserved energy.

---

## 15. Destination-targeted construction

If the desired final root is known, search within its root family and then select the compound whose digit path best matches the intended process.

Example target root:

```text
9 = Completion
```

Two-digit candidates include:

```text
18  Origin → Manifestation → Completion
27  Relation → Knowledge → Completion
36  Creation → Harmony → Completion
45  Structure → Change → Completion
54  Change → Structure → Completion
63  Harmony → Creation → Completion
72  Knowledge → Relation → Completion
81  Manifestation → Origin → Completion
90  Completion → Potential → Completion
99  Completion → Completion → Completion
```

This is the basis of reverse engineering.

---

## 16. Construction constraints

A candidate formula should satisfy as many of these as possible:

```text
1. correct arithmetic
2. desired roots present
3. desired stage order preserved
4. final root intentional rather than accidental where possible
5. intermediate compounds examined
6. no hidden semantic overrides
7. carrier profile declared if letters are used
8. shortest formula preferred when two formulas encode the same intended path equally well
```

The shortest-form preference keeps the language readable and reduces arbitrary degrees of freedom.

---

## 17. Comparison protocol

When comparing formulas, do not ask only whether they share a root.

Compare:

```text
surface digits
length
ordered path
repetition pattern
first synthesis
full reduction chain
final root
zero modifiers
carrier/glyph layer
intention match
```

Example:

```text
38 and 83
same length: yes
same digits: yes
same order: no
same first sum: yes
same root: yes
same process meaning: no
```

---

## 18. Canonical notation

Human-readable notation:

```text
38 :: 3→8 :: 11→2
```

Meaning:

```text
surface :: ordered path :: reduction after surface
```

Expanded notation:

```text
38 :: Creation→Manifestation :: 38→11→2 :: ROOT=Relation
```

Glyph notation:

```text
GPGY :: 7→7→7→7 :: 7777→28→10→1
```

---

## 19. Versioning rule

Any change to the following requires a version change in `ROOT-REGISTRY.json`:

```text
root names
root meanings
zero meaning
carrier mapping
glyph-specific meanings
semantic provenance
```

Arithmetic algorithms do not change with symbolic registry versions.

---

## 20. One-screen compiler model

```text
INTENTION
   ↓
SEMANTIC TOKENS
   ↓
ROOT MAPPING
   ↓
ORDERED DIGIT PATH
   ↓
CANDIDATE NUMBER
   ↓
SUM / REDUCTION CHAIN
   ↓
FINAL ROOT
   ↓
OPTIONAL LETTER/GLYPH CARRIER
   ↓
FROZEN INTERPRETATION
   ↓
OPTIONAL PROSPECTIVE TEST
```

Core rule:

> **Digits describe the path, compounds describe synthesis, the reduction chain preserves history, and the final root describes the deepest canonical identity.**
