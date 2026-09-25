# Xyool Astrology Domain

Status: **EXPERIMENTAL**

This directory is the operational entry point for Xyool's astrology domain.

## Read order

1. `library/INDEX.md` — reusable internal domain knowledge and canonical pointers
   - `library/SOURCE-INDEX.md`
   - `library/RULE-INDEX.md`
   - `library/VALIDATION-INDEX.md`
2. `DOMAIN.md` — domain contract and laws
3. `SYSTEM-REGISTRY.md` — system identities and provenance boundaries
4. `RULE-REGISTRY.md` — versioned rule schema
5. `RUN-SEQUENCE.md` — mandatory analysis procedure
6. `SIGNAL-OUTPUT-MODEL.md` — capability optimization, atomic windows, convergence, Tuner
7. `VALIDATION.md` — controls, prospective testing, calibration, ablation
8. `MAYA.md` — traditional/living Maya calendrical and Dreamspell separation when relevant
9. `STAR-DEGREE.md` — user-derived degree-as-atomic-address / stellar-field research framework

## Core architecture

```text
INPUTS
→ SYSTEM IDENTITY
→ CALCULATION / CALENDAR CONVERSION
→ SYSTEM-NATIVE INTERPRETATION
→ VERSIONED RULE OBJECTS
→ OPTIONAL CAPABILITY TRANSLATION
→ CROSS-SYSTEM CONVERGENCE / CONTRADICTION
→ ATOMIC TIME WINDOWS
→ OPTIONAL TUNER COMPRESSION
→ PROSPECTIVE OUTCOME / FEEDBACK
→ VALIDATION / MISS LEARNING
```

## Current system namespaces

```text
ASTRO.WT.MODERN
ASTRO.WT.TRAD
ASTRO.WT.XYOOL_STORY_V1
ASTRO.WT.XYOOL_STORY_V2_DEGREE_NODE
ASTRO.WS
ASTRO.JYO
ASTRO.STAR
ASTRO.HELIO
MAYA.TRAD
DREAMSPELL.ARGUELLES
```

Adjacent systems may contribute to higher-level synthesis only when explicitly named:

```text
ADJ.WUXING
ADJ.HD
ADJ.AYURVEDA
```

They are not silently reclassified as astrology.

## Prior user frameworks preserved

### Capability Optimization

```text
Mental Capacity
Focus
Action
Opportunity
Communication
Creation
Investigation
Connection
Recovery
Friction / Impulsiveness
```

The objective is practical capability mapping rather than good/bad labeling.

### Atomic timing

Every material boundary creates a new interval. No broad phase smoothing when the active signal set changes.

### Tuner

```text
Energy
Direction
Stability
Intensity
Clarity
```

Optional goals:

```text
High Performance
Recovery
Transformation
```

Optional controllable levers:

```text
Breath
Body
Fuel
Attention
```

### Full-resolution sky research

Fixed stars, parans, and heliocentric/3D concepts are preserved as testable research layers rather than silently treated as validated astrology.

## Maya integrity

`MAYA.TRAD` and `DREAMSPELL.ARGUELLES` are separate systems.

Traditional/living Maya calendar material is preserved with its own provenance and calculation identity. Dreamspell is preserved as a modern system with its own implementation rules.

Never blend them under one generic "Mayan" signal.

## Validation rule

```text
TEST EACH SYSTEM ALONE
→ TEST TRANSLATION
→ TEST CONVERGENCE
→ RUN ABLATIONS
→ PROMOTE ONLY WHAT ADDS OUT-OF-SAMPLE / PROSPECTIVE INFORMATION
```

The domain remains EXPERIMENTAL until these tests are executed.

## Domain knowledge memory

Astrology now uses `library/INDEX.md` as the first reusable-knowledge surface.

The library:
- points to established rules, sources, validation methods, and failure boundaries;
- records partial/open domain updates;
- lets future work reuse stable knowledge before broad external research;
- preserves original provenance and validation status.

External research remains required for new, stale, conflicted, or current information.
