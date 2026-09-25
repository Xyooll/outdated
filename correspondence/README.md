# Xyool Correspondence

This directory stores explicit cross-domain knowledge-transfer maps.

Before creating or using a correspondence, read:

- `skills/xyool/00-03-META-ARCHITECTURE-PRIMER.md`
- `skills/xyool/00-04-DOMAIN-CORRESPONDENCE-HOWTO.md`
- `skills/xyool/00-02-DOMAIN-CORRESPONDENCE-ARCHITECTURE.md`

Correspondence is the controlled process of asking whether a causal, temporal, evidentiary, or learning principle from one domain has a structurally valid counterpart in another.

It is **not** permission to copy domain-specific scores, thresholds, objectives, calibrations, or actions.

## Required workflow

```text
SOURCE-DOMAIN OBSERVATION / PRINCIPLE
→ VERIFY SOURCE STATUS
→ REMOVE DOMAIN-SPECIFIC NOUNS
→ IDENTIFY ABSTRACT INVARIANT
→ TEST WHETHER THE INVARIANT DEPENDS ON SOURCE-DOMAIN MECHANICS
→ PROPOSE TARGET-DOMAIN STRUCTURAL MATCH
→ IDENTIFY IMPORTANT DIFFERENCES
→ STATE WHAT TRANSFERS
→ STATE WHAT DOES NOT TRANSFER
→ DEFINE TARGET-DOMAIN FALSIFICATION / TEST
→ RUN TARGET-DOMAIN EVIDENCE / CONTROLS
→ ASSIGN VALIDATION STATUS
→ FEED RESULT BACK INTO THE ABSTRACTION IF WARRANTED
```

## Required file fields

Each correspondence file should include:

```text
Source Domain:
Source Principle / Pattern:
Source Validation Status:
Source Evidence:
Source Failure Modes:

Abstract Invariant:

Target Domain:
Target Objects / States:
Proposed Mapping:

Structural Match:
Important Differences:
Transferred Components:
Non-Transferred Components:
Target-Domain Test:
Target-Domain Evidence:
Negative / Control Case:
False-Positive / Failure Modes:
Status:
Next Evidence Needed:
Source-Principle Feedback:
```

## Status values

```text
HYPOTHESIS
PROVISIONAL
SUPPORTED
REJECTED
SUPERSEDED
```

## Core rule

> **Correspondence generates a testable mapping; target-domain evidence earns the rule.**

Operational shorthand:

> **Transfer questions, structures, and tested causal relationships before transferring conclusions.**

## Anti-transfer rules

Do not automatically transfer:
- numeric thresholds;
- probability bands;
- timing windows;
- scoring weights;
- market objectives;
- capital actions;
- market-data features;
- regulatory or filing-specific evidence assumptions;
- source-domain actor semantics;
- causal mechanisms that merely look similar on the surface.

If an abstract principle transfers but calibration does not, use:

```text
RETAIN STRUCTURE
RESET CALIBRATION
RE-ESTIMATE LOCALLY
```

## Correspondence stress test

Before treating a mapping as more than analogy, ask:

```text
1. Is the same causal relationship present?
2. Are the relevant actors analogous in function, not merely name?
3. Does the same state transition exist?
4. Is the gate structurally necessary in both domains?
5. Does timing carry comparable information?
6. Are important confounders and differences named?
7. Can the target mapping fail in a measurable way?
8. Is there target-domain evidence rather than only source-domain success?
```

## Bidirectional learning

A correspondence can refine the source-domain principle too.

If a target domain reveals that the supposed invariant was actually source-specific, update or narrow the abstraction rather than forcing the target to fit.

Target-domain outcomes may:

```text
strengthen the abstraction
reveal boundary conditions
narrow the abstraction
reject only the mapping
generate a new core candidate
```

Preserve rejected mappings so Xyool does not repeatedly relearn the same false analogy.

Use `correspondence/TEMPLATE.md` for new mappings.

See `skills/xyool/00-02-DOMAIN-CORRESPONDENCE-ARCHITECTURE.md` for the canonical specification and `skills/xyool/00-04-DOMAIN-CORRESPONDENCE-HOWTO.md` for the operating procedure.
