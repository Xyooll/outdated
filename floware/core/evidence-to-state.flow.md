# FLOW — Evidence to State

FLOW ID: `CORE-EVIDENCE-STATE`  
STATUS: **ACTIVE / CANONICAL**

## GOAL

Convert evidence into the smallest auditable state representation needed for the current decision.

## PROCESS

```text
IDENTIFY QUESTION
→ IDENTIFY REQUIRED EVIDENCE
→ REUSE FRESH EXISTING EVIDENCE
→ FETCH ONLY MISSING/STALE/MATERIAL EVIDENCE
→ SEPARATE FACT / INFERENCE / UNKNOWN
→ UPDATE STATE DELTA
→ NAME CONTRADICTIONS
→ OUTPUT STATE
```

## GATES

- source identity;
- freshness;
- causal relevance;
- domain attribution;
- contradiction handling.

## ADAPTATION

Evidence requirements expand only when an unresolved uncertainty could materially change the current output.

## FAIL-CLOSED CONDITIONS

Missing material evidence becomes UNKNOWN/BLOCKED, never zero or assumed.

## OUTPUT STATE

- prior state;
- new evidence;
- state delta;
- confidence;
- blockers;
- provenance.

## SOFTWARE / HARD-LIMIT BOUNDARY

Software may be used for exact parsing, persistence, or arithmetic when justified. Reasoning remains Floware.
