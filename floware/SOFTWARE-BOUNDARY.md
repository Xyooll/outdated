# Software Boundary

Status: **CANONICAL / SOFTWARE-EXCEPTION POLICY**

Xyool is Floware-first.

Existing software remains available, but software is no longer the default implementation path.

## Default

```text
NEW CAPABILITY
→ DESIGN FLOW
→ RUN FLOW
→ EVALUATE EFFECTIVENESS
→ SOFTWARE ONLY IF A SPECIFIC NEED IS PROVEN
```

## Software is justified for

- exact arithmetic or transformation where approximation is unacceptable;
- structured persistence and integrity;
- security/authentication/permissions;
- external transactions;
- physical or financial hard limits;
- repeated bulk computation where automation materially reduces burden;
- deterministic validation that prevents an evidenced failure mode;
- interfaces/drivers/APIs that AI reasoning cannot substitute for.

## Software is not justified merely because

- the rule can be coded;
- code feels more formal;
- a Markdown flow looks less technical;
- a one-time calculation could be automated;
- a behavior might someday need enforcement;
- software already exists nearby.

## Existing directories

```text
agent/
scripts/
tests/
main.py
```

are **supporting software assets**.

They are not the primary location of Xyool intelligence.

Do not expand them unless `core/software-escalation.flow.md` supports the need.

## Migration posture

Do not rewrite working software merely to make the repository look Floware-native.

Instead:
1. stop unnecessary software growth;
2. move reasoning authority into Flows;
3. keep proven hard-limit software;
4. retire software only when the Flow no longer depends on it and removal is safe.

> **Software must justify why Floware is insufficient.**
