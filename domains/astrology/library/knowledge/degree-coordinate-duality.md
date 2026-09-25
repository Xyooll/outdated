# ASTRO-LIB-DEGREE-COORDINATE-DUALITY

TYPE: STATE MODEL / ONTOLOGY
STATUS: **DOMAIN-ESTABLISHED FOR REPRESENTATION**
SCOPE: Star Astrology / all degree-level work
LAST REVIEWED: 2026-09-25

## Two degree identities

Every tropical/sidereal longitude has two degree identities that must be preserved separately.

### Local sign degree

~~~text
local_degree_exact = longitude mod 30
range = [0°, 30°)

local_index_zero = floor(local_degree_exact)
range = 0..29

local_ordinal = local_index_zero + 1
range = 1..30
~~~

Question:

> What does this position within any 30° sign mean?

This supports local-degree systems such as modern 0–29 Degree Theory and any future Xyool local-cycle hypothesis.

### Absolute zodiac degree

~~~text
absolute_degree_exact = longitude mod 360
range = [0°, 360°)

absolute_index_zero = floor(absolute_degree_exact)
range = 0..359

absolute_ordinal = absolute_index_zero + 1
range = 1..360
~~~

Question:

> What does this unique address around the complete zodiac mean?

This supports:
- monomoiria degree lords;
- Sabian Symbols;
- Charubel / La Volasfera;
- Kozminsky;
- Janduz;
- future Xyool 360-cell intrinsic meanings.

## Example

~~~text
11°14' Scorpio

local_degree_exact = 11°14'
local_index_zero = 11
local_ordinal = 12

absolute_degree_exact ≈ 221°14'
absolute_index_zero = 221
absolute_ordinal = 222
~~~

The local and absolute identities are both real properties of the same coordinate.

Do not overwrite one with the other.

## Ordinal indexing warning

Many degree-symbol traditions are ordinal:

~~~text
0°00'–0°59' = first degree
1°00'–1°59' = second degree
...
29°00'–29°59' = thirtieth degree
~~~

Always store both zero-based index and one-based ordinal to prevent off-by-one errors.

## Interpretation layers

~~~text
LOCAL30 INTRINSIC CANDIDATE
+
ABS360 INTRINSIC CANDIDATE
+
STELLAR NEIGHBORHOOD
+
SIGN / DECAN / BOUND
+
HOUSE / RULER
+
OBJECT / ASPECT / TIMING
→ full degree-node state
~~~

Local and absolute meanings are not automatically independent because both derive from the same longitude. Validation must use feature-family ablation.
