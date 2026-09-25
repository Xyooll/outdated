# FLOW — Code to Flow Translation

FLOW ID: `CORE-CODE-TO-FLOW`  
STATUS: **RESEARCH / ACTIVE**  
DOMAIN: core  
JOB: translate programming semantics into Floware structure

## GOAL

Translate a program, programming construct, or programming language into an equivalent Flow representation where possible, while explicitly preserving semantics that still require deterministic software.

## PROCESS

```text
IDENTIFY SOURCE LANGUAGE
→ IDENTIFY CONSTRUCT / PROGRAM GOAL
→ PARSE SEMANTIC ROLE
→ EXTRACT STATE / TRANSITIONS / REFERENCES / CONSTRAINTS
→ MAP TO FLOW ATTRIBUTES
→ IDENTIFY SOFTWARE-ONLY SEMANTICS
→ BUILD FLOW REPRESENTATION
→ TEST BEHAVIORAL EQUIVALENCE
→ RECORD AMBIGUOUS / FAILED MAPPINGS
→ REFINE GLOSSARY
```

## GATES

A translation is not complete merely because the Flow reads naturally.

Check whether the source depends on:
- memory layout;
- pointer aliasing;
- lifetime/resource semantics;
- exact timing;
- concurrency ordering;
- binary compatibility;
- hardware registers;
- cryptographic guarantees;
- deterministic precision.

If any matter materially, preserve them as software/hard-limit boundaries.

## OUTPUT STATE

- source construct/program;
- semantic decomposition;
- Flow correspondence;
- software-only semantics;
- behavioral-equivalence status;
- failed/ambiguous mappings;
- glossary updates.

## SUPPORTING REFERENCES

- `../CODE-TO-FLOW-CORRESPONDENCE.md`
- `../LANGUAGE-CORRESPONDENCE-GLOSSARY.md`
- `correspondence.flow.md`

## SOFTWARE / HARD-LIMIT BOUNDARY

Software may be required to parse/execute source code or verify exact behavioral equivalence.

The translation logic itself remains Floware.
