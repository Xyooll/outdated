# Xyool — Floware: AI-Native Adaptive Execution Architecture

Status: **CANONICAL META-ARCHITECTURE**
Date: **2026-09-22**

## Definition

> **Floware is structured, state-aware, goal-directed procedural knowledge designed to be interpreted and executed by AI, with software reserved for deterministic calculations, persistence, interfaces, transactions, security, and hard limits.**

Software remains essential.

Floware is not a replacement for software.

It is a new execution layer for work that is adaptive, contextual, evidence-sensitive, and difficult or wasteful to enumerate as fixed branches.

---

## Repository implementation

Floware is physically implemented under:

- `floware/` — core Flows, contracts, routing, software boundary;
- `domains/<domain>/flows/` — domain Floware.

Canonical repository contracts:
- `floware/README.md`
- `floware/REGISTRY.md`
- `floware/FLOW-CONTRACT.md`
- `floware/REPOSITORY-MAP.md`
- `floware/SOFTWARE-BOUNDARY.md`

Legacy `nodes/` and existing Python remain compatibility/support layers, not the preferred home of new intelligence.

## 1. Software versus Floware

### Software

Software is strongest when the desired behavior should be exact.

Typical properties:

```text
DETERMINISTIC
EXPLICIT INSTRUCTIONS
CALCULATIONS
DATA STRUCTURES
DATABASES
APIs
TRANSACTIONS
SECURITY
PERMISSIONS
HARD LIMITS
LOW-LEVEL CONTROL
```

Software asks:

> **What exact instructions should the machine execute?**

### Floware

Floware is strongest when the desired behavior must adapt to state and context.

Typical properties:

```text
GOAL-DIRECTED
STATE-AWARE
EVIDENCE-SENSITIVE
CONTEXTUAL
ADAPTIVE
REASONING-DRIVEN
SELF-AUDITING
ROUTABLE
LEARNABLE
```

Floware asks:

> **What goal should be achieved, what evidence and constraints govern the process, and how should the path adapt as reality changes?**

---

## 2. The AI-era stack

Canonical conceptual stack:

```text
GOAL
  ↓
FLOWARE
intent / reasoning / planning / adaptation / routing / audit
  ↓
SOFTWARE
deterministic computation / persistence / permissions / hard constraints
  ↓
HARDWARE
physical execution / compute / sensors / actuators
```

Short form:

> **Floware decides what should happen. Software guarantees what must happen. Hardware makes it happen.**

These layers may interact recursively, but their authority should remain explicit.

---

## 3. Why Floware exists

Traditional software attempts to enumerate behavior in advance.

That works well when:
- state space is limited;
- rules are stable;
- exact reproducibility is required;
- errors must be mechanically blocked.

It becomes inefficient when:
- the environment is open-ended;
- evidence changes;
- the correct next action depends on context;
- multiple valid paths can reach the same goal;
- reasoning is more useful than branching;
- maintaining every possible exception creates more complexity than value.

AI allows the executable object to become a **flow of intent + evidence + state + constraints**, rather than only a fixed instruction tree.

---

## 4. The Flow is the program

A canonical Flow contains:

```text
FLOW ID

GOAL
What capability or outcome is being pursued?

GOALPOST
What constitutes sufficient completion?

INPUT STATE
What must be known before execution?

EVIDENCE
What information is authoritative?

PROCESS
What questions/actions should be performed?

GATES
What conditions must be satisfied before proceeding?

ADAPTATION
How may the route change as state changes?

BOUNDARIES
What is outside this Flow's authority?

FAIL-CLOSED CONDITIONS
When must the Flow stop rather than infer?

OUTPUT STATE
What must exist when the Flow finishes?

LEARNING HOOK
What later outcome evaluates whether the Flow worked?

SOFTWARE / HARD LIMITS
Which requirements must not depend on AI discretion?
```

A Flow is therefore closer to:

```text
flow(goal, state, evidence, constraints)
    → adaptive reasoning path
    → actions
    → updated state
    → auditable output
```

than to a conventional fixed function.

---

## 5. Floware is not "just prompting"

A prompt is an instruction surface.

Floware is an architecture.

A valid Flow should have:
- explicit authority;
- persistent state semantics;
- evidence hierarchy;
- goalpost;
- gates;
- stop conditions;
- outputs;
- auditability;
- learning hooks;
- software boundaries.

A large unstructured prompt is not automatically Floware.

---

## 6. Software is still required

Floware must not absorb responsibilities that benefit from determinism.

Prefer software for:
- arithmetic and exact transformations;
- database integrity;
- cryptographic/security boundaries;
- access control;
- financial transaction limits;
- rate/position/torque/temperature limits;
- persistence;
- schemas;
- exact validation;
- anti-lookahead enforcement where mechanical enforcement is practical;
- reproducible bulk computation;
- low-level device control.

Prefer Floware for:
- interpretation;
- research routing;
- causal reasoning;
- hypothesis management;
- adaptive planning;
- evidence synthesis;
- choosing among valid procedures;
- diagnosis;
- correspondence;
- recursive improvement.

Canonical law:

> **Use Floware for intelligence. Use software for certainty.**

---

## 7. Code is not the default implementation

For an AI-native system, a new idea should not automatically become code.

Default decision sequence:

```text
NEW IDEA
   ↓
CAN IT EXIST RELIABLY AS A FLOW?
   ↓
YES → KEEP IT AS FLOWARE
   ↓
DOES A SUB-PART REQUIRE EXACTNESS / SCALE / HARD ENFORCEMENT?
   ↓
YES → IMPLEMENT ONLY THAT PART AS SOFTWARE
```

Promote a Flow component into software when evidence shows at least one of:

1. exact repeatability is necessary;
2. AI discretion creates unacceptable failure risk;
3. the same calculation is repeated frequently;
4. structured persistence is required;
5. automation materially reduces burden;
6. a hard physical/financial/security constraint must be guaranteed;
7. deterministic regression provides clear value.

Do not write software merely because software is familiar.

---

## 8. Flow composition

Flows may call other Flows.

Example:

```text
CAPITAL ALLOCATION FLOW
        ↓
QUALITY FLOW
        ↓
EVENT STATE FLOW
        ↓
TTC FLOW
        ↓
PAYOFF FLOW
        ↓
RECOGNITION FLOW
        ↓
ROTATION FLOW
```

Routing can be state dependent.

Example:

```text
PAYOFF FLOW
   ↓
detect terminal regulatory event
   ↓
REGULATORY PAYOFF FLOW

or

detect procurement dependency
   ↓
PROCUREMENT / CAUSAL-TIMER FLOW
```

The route is adaptive.

The authority boundaries are not.

---

## 9. Floware and robots

Robotics makes the distinction especially visible.

Traditional robotics often resembles:

```text
SENSOR INPUT
→ PREDEFINED SOFTWARE LOGIC
→ FIXED ACTION
```

AI-native robotics can resemble:

```text
GOAL
→ PERCEIVE CURRENT STATE
→ INTERPRET ENVIRONMENT
→ SELECT / ADAPT FLOW
→ ACT
→ OBSERVE RESULT
→ UPDATE STATE
→ CONTINUE TOWARD GOAL
```

Example:

Traditional software might encode:

```text
if object offset = X:
    rotate joint A by Y
    extend actuator by Z
```

Floware can express:

> **Pick up the cup without spilling it.**

The AI may adapt perception, grasp, trajectory, and retry strategy to the actual environment.

Software remains underneath to enforce:
- actuator control;
- collision limits;
- torque limits;
- joint limits;
- emergency stop;
- sensor interfaces;
- timing guarantees;
- authentication.

Robotics therefore fits the same stack:

```text
GOAL
   ↓
FLOWARE
perception / intent / planning / adaptive behavior
   ↓
SOFTWARE
motion control / safety constraints / drivers / deterministic limits
   ↓
HARDWARE
sensors / motors / actuators / physical body
```

The physical world is too variable to enumerate every useful behavior in advance.

Floware lets the robot pursue goals adaptively while software preserves the non-negotiable boundaries.

---

## 10. Floware and Xyool

Much of Xyool already behaves as proto-Floware:

- Mandatory Run Sequence;
- Quality;
- OSE / FES;
- TTC;
- Recognition;
- Correspondence;
- RLE;
- Goalpost Governance;
- evidence-directed experimentation.

These should not automatically be treated as documentation waiting to become Python.

Where they are sufficiently structured, they are themselves the executable reasoning architecture.

The AI should:
1. load the relevant Flow;
2. load current state;
3. gather only required evidence;
4. route through the applicable gates;
5. adapt within declared boundaries;
6. produce the required output state;
7. persist material learning;
8. invoke software only where software adds justified certainty or efficiency.

---

## 11. Goalposts prevent Floware drift

Adaptive systems can wander.

Therefore Floware inherits:

`00-07-GOALPOST-EFFECTIVENESS-GOVERNANCE.md`

Every major Flow should know:
- what it is trying to finish;
- what counts as sufficient effectiveness;
- what is out of scope;
- when a method failed;
- when the Flow may stop;
- when the next goal may begin.

Floware without goalposts risks becoming endless reasoning.

Goalposts without Floware risk becoming rigid procedure.

Together:

```text
GOALPOST
    ↓
FLOWARE
adaptive path
    ↓
EVIDENCE
constrains belief
    ↓
SOFTWARE HARD LIMITS
constrain unsafe/invalid action
    ↓
OUTCOME
    ↓
LEARNING
```

---

## 12. Recursive Flow evolution

A Flow may improve through outcomes:

```text
FLOW
 ↓
EXECUTION
 ↓
OUTCOME
 ↓
AUDIT
 ↓
FAILURE / SUCCESS CLASSIFICATION
 ↓
EVIDENCE
 ↓
FLOW IMPROVEMENT
 ↓
REGRESSION
 ↓
UPDATED FLOW
```

But updates must obey:
- frozen goalposts;
- evidence hierarchy;
- anti-lookahead;
- development vs holdout separation;
- domain correspondence boundaries;
- effectiveness-within-reason;
- complexity tax.

Recursive learning may improve the Flow.

It may not rewrite authority merely because a new story sounds coherent.

---

## 13. Evidence-based Flow optimization

A better Flow is not necessarily a larger Flow.

Improve by:
- deleting redundant stages;
- combining duplicate evidence checks;
- reducing unnecessary research;
- improving routing;
- clarifying authority;
- improving state definitions;
- adding a hard software guard only where needed;
- replacing software branches with adaptive reasoning where safe;
- replacing vague reasoning with software where exactness matters.

Optimization target:

> **Maximum useful goal achievement per justified unit of complexity, research, computation, latency, and maintenance.**

This follows the Xyool standard:

> **Effectiveness within reason, not perfection.**

---

## 14. Flowware design test

Before implementing a new Xyool capability ask:

```text
1. What is the goal?
2. What is the frozen goalpost?
3. What state must be understood?
4. What evidence is authoritative?
5. What parts require adaptive reasoning?
6. What parts require deterministic enforcement?
7. What can fail closed?
8. What should the output state contain?
9. How will later evidence evaluate the Flow?
10. Is code actually necessary?
```

If question 10 has no evidence-backed answer, do not default to code.

---

## 15. Core laws

> **Use Floware for intelligence. Use software for certainty.**

> **The flow itself can be the program.**

> **Software specifies exact behavior; Floware specifies intent, state, evidence, constraints, and adaptive process.**

> **Do not encode adaptive reasoning into software unless determinism, scale, or hard enforcement earns the cost.**

> **Robots and AI-native systems can use Floware above software: adaptive goal pursuit above deterministic safety/control.**

> **Floware does not remove software. It gives software a clearer job.**
