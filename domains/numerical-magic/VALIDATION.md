# Numerical Magic Domain — Validation Protocol

Status: **EXPERIMENTAL / REQUIRED FOR PROMOTION**

The domain contains two fundamentally different things:

```text
DETERMINISTIC COMPONENTS
arithmetic, reduction, carrier lookup, parsing, root-family generation

INTERPRETIVE COMPONENTS
symbolic meanings, intention mappings, glyph meanings, claims about practical effects
```

They must be validated differently.

## 1. Track A — arithmetic correctness

Required invariant tests:

```text
7777 → 28 → 10 → 1
38   → 11 → 2
83   → 11 → 2
738  → 18 → 9
2738 → 20 → 2
99   → 18 → 9
0    → 0
```

Required digital-root identity for all positive integers `n` in a chosen test range:

```text
digital_root(n) == 1 + ((n - 1) mod 9)
```

## 2. Track B — root-family correctness

For root `r`:

```text
r, r+9, r+18, ...
```

Every generated member must reduce to `r`.

Control:

```text
No member generated for root r may reduce to another root.
```

## 3. Track C — carrier mapping correctness

Default Pythagorean carrier profile must satisfy:

```text
AJS=1
BKT=2
CLU=3
DMV=4
ENW=5
FOX=6
GPY=7
HQZ=8
IR=9
```

Known test:

```text
GPGY → 7,7,7,7 → 7777 → 28 → 10 → 1
```

Carrier mapping and glyph meanings must remain separate.

## 4. Track D — order sensitivity

A valid semantic engine must distinguish:

```text
38 = Creation → Manifestation
83 = Manifestation → Creation
```

while preserving their arithmetic equivalence:

```text
38 → 11 → 2
83 → 11 → 2
```

Negative control:

```text
An implementation that reports identical ordered paths for 38 and 83 fails.
```

## 5. Track E — registry determinism

For a fixed `ROOT-REGISTRY.json` version:

```text
same input
+ same carrier profile
+ same registry version
= same parse, same root labels, same provenance
```

Semantic changes require registry version changes.

## 6. Track F — reverse-engineering consistency

When a candidate is constructed from declared roots, decode it again.

Example:

```text
intention tokens: creation, materialization
mapped roots: 3,8
selected order: 3→8
candidate: 38
```

Decode must return the same declared stage sequence.

This tests internal language consistency only; it does not prove real-world efficacy.

## 7. Track G — empirical practice tests

If a practitioner claims that a formula changes external outcomes, use prospective testing.

Freeze before the outcome:

```text
formula
registry version
intention
expected outcome category
measurement method
start date
end date
comparison/control condition
what counts as a hit
what counts as a miss
```

Possible controls:

```text
randomly selected same-root formula
reversed formula
neutral/no-formula condition
matched time window
blinded label condition
```

Track behavioral mediation separately. For example, if `38` helps a person consistently focus on creating and selling art, that psychological or behavioral usefulness is distinct from claiming the number itself caused external income.

## 8. Anti-retrofit rule

After observation, do not:

```text
change the root meaning
change the expected outcome
extend the time window
switch carrier profile
add a new glyph meaning
reinterpret a miss as a hit
```

without first scoring the original hypothesis.

Any change creates a new version/hypothesis.

## 9. Miss loop

```text
MISS
→ verify arithmetic
→ verify profile/version
→ verify frozen interpretation
→ classify whether failure was parser, semantic, intention-map, or outcome-level
→ preserve the failed record
→ change the smallest rule justified by evidence
→ rerun controls
```

## 10. Promotion criteria

The domain may keep deterministic utilities stable while symbolic efficacy remains experimental.

To promote the language architecture itself from EXPERIMENTAL to DOMAIN CANONICAL:

```text
[ ] arithmetic test suite passes
[ ] root-family tests pass
[ ] carrier mapping tests pass
[ ] order-sensitivity tests pass
[ ] registry versioning enforced
[ ] reverse-engineering round trips pass
[ ] worked examples remain reproducible
[ ] negative controls pass
```

To promote any real-world efficacy claim requires a separate evidence standard and should never be inferred merely from the language architecture passing its tests.
