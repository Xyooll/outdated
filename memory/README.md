# Xyool Memory

Status: **DURABLE REPOSITORY MEMORY**

This directory is the human-readable long-term memory layer for material concepts that should survive individual chats.

This is distinct from ChatGPT product Memory.

Project Memory may be unavailable or disabled; Git remains the durable source of truth.

## Memory classes

```text
memory/
  user-concepts/
    thoughts, philosophies, design intuitions, rationale, naming decisions

research/
    evidence, experiments, outcomes, regressions

domains/*/state/
    current/historical domain state

software persistence
    machine/runtime state where justified
```

## Primary rule

> **Preserve the person's thought before preserving the system's interpretation of it.**

A future reader should be able to distinguish:
- what the user actually said;
- the concise concept extracted from it;
- why it mattered;
- how Xyool interpreted/applied it;
- what changed later.

## Privacy / sensitivity

Do not infer private biographical facts, medical conditions, political beliefs, relationships, or other sensitive personal attributes from ordinary discussion.

Only preserve sensitive personal material when the user explicitly asks for that specific material to be stored.

## Append orientation

Historical thought should not be silently rewritten when the idea evolves.

Prefer:

```text
ORIGINAL CONCEPT
→ LATER REFINEMENT
→ CONTRADICTION / REVISION
→ CURRENT INTERPRETATION
```

This lets a future reader see intellectual development rather than only the latest summary.
