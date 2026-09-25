# FLOW — Software Escalation

FLOW ID: `CORE-SOFTWARE-ESCALATION`  
STATUS: **ACTIVE / CANONICAL**

## GOAL

Prevent unnecessary software from replacing adaptive Floware reasoning.

## TRIGGER

Run this Flow before creating or materially expanding code, scripts, CI, deterministic agents, or executable infrastructure.

## PROCESS

Ask in order:

1. Can the capability be expressed and executed reliably as Floware?
2. Is exact determinism required for correctness or safety?
3. Is structured persistence/integrity required?
4. Is there a hard security, financial, physical, or authorization boundary?
5. Is repeated computation large enough that automation materially reduces total burden?
6. Has an actual failure demonstrated that Floware-only execution is insufficient?
7. Can software be limited to a smaller sub-problem while the intelligence remains Floware?
8. Does expected benefit exceed implementation, testing, CI, maintenance, and failure-surface cost?

## DECISION

```text
FLOWARE_SUFFICIENT
SOFTWARE_SUBCOMPONENT_JUSTIFIED
SOFTWARE_HARD_LIMIT_REQUIRED
DEFER — NEED EVIDENCE
```

## GATE

New software is justified only when the decision is not `FLOWARE_SUFFICIENT`.

## OUTPUT STATE

When software is justified, record:
- exact deterministic responsibility;
- why Floware is insufficient;
- authority boundary;
- minimum software surface;
- removal condition if temporary.

## SOFTWARE / HARD-LIMIT BOUNDARY

This Flow itself requires no software.

> **Software must justify why Floware is insufficient.**
