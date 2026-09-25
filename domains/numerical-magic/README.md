# Xyool Numerical Magic Language

Status: **EXPERIMENTAL**

This domain implements a deterministic numerical grammar plus an explicitly symbolic interpretation layer.

## Start here

1. `DOMAIN.md` — domain contract, root meanings, evidence boundaries, and domain laws.
2. `GRAMMAR.md` — complete construction and reverse-engineering grammar.
3. `LETTER-NUMBER-PROTOCOL.md` — canonical dual-value letter logic: alphabet ordinal + reduced root, ring-preserving letter selection, and ordinal substructure.
4. `ROOT-REGISTRY.json` — machine-readable root/carrier/glyph/letter definitions.
5. `RUN-SEQUENCE.md` — canonical decode and reverse-engineering procedure.
6. `engine.py` — deterministic parser, reducer, root-family generator, and dual-channel letter engine.
7. `VALIDATION.md` — arithmetic, semantic, reverse-engineering, and optional empirical validation protocol.
8. `test_engine.py` — executable regression tests for the deterministic core.

## Core model

```text
SURFACE FORM
→ ORDERED PATH
→ COMPOUND SUM
→ FULL REDUCTION CHAIN
→ FINAL ROOT
```

Example:

```text
38
→ Creation → Manifestation
→ 11
→ 2
→ Relation
```

## Dual-value letter model

Every A-Z letter preserves two linked numbers:

```text
LETTER
→ ALPHABET ORDINAL
→ ORDINAL REDUCTION CHAIN
→ ROOT FAMILY
```

Examples:

```text
W = 23 → 5
P = 16 → 7
Y = 25 → 7
V = 22 → 4
S = 19 → 10 → 1
```

The root digit determines which letters are eligible to encode a numerical ring. The ordinal pathway distinguishes candidates inside the same root family.

Example root family:

```text
5 → E = 5, N = 14→5, W = 23→5
```

The ordinal channel adds nested numerical information but does not replace the canonical reduction chain of the ring.

Example with the local G/P/Y glyph extension:

```text
GPGY
Root channel:    7 → 7 → 7 → 7
Ring reduction:  7777 → 28 → 10 → 1
Ordinal channel: 7 + 16 + 7 + 25 = 55 → 10 → 1
Glyph channel:   Gnosis → Projection → Gnosis → Choice
```

## Root map

```text
1 Origin
2 Relation
3 Creation
4 Structure
5 Change
6 Harmony
7 Knowledge
8 Manifestation
9 Completion
0 Potential (modifier, not root)
```

## CLI examples

From the repository root:

```bash
python domains/numerical-magic/engine.py number 7777
python domains/numerical-magic/engine.py number 38
python domains/numerical-magic/engine.py text GPGY
python domains/numerical-magic/engine.py letter W
python domains/numerical-magic/engine.py letter-options 57444
python domains/numerical-magic/engine.py family 9 --count 12
python domains/numerical-magic/engine.py candidates 2 --digits 2
```

Run deterministic tests:

```bash
python domains/numerical-magic/test_engine.py
```

## Important boundary

The arithmetic, alphabet ordinal, digital-root, and carrier lookup layers are deterministic. The symbolic root meanings, ordinal-compound interpretations, glyph meanings, and any claimed magical efficacy are conventions or hypotheses unless separately validated. Internal consistency is not evidence of external causality.
