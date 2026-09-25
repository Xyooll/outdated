# Xyool — Principle & Question Documentation Standard

Status: **CANONICAL DOCUMENTATION STANDARD**

## Purpose

Xyool principles and mandatory questions must be understandable without reconstructing the conversation or remembering the company that originally exposed the issue.

A rule that contains only a short slogan is too brittle. A future run needs to know:
- what the principle means;
- why it exists;
- what failure mode it prevents;
- when it applies;
- what it is allowed to change;
- what evidence would contradict it.

## Required structure

Every promoted principle, mandatory question, or permanent process check should include, when relevant:

```text
Name
Status / authority
Core principle or question
Why it exists
Failure mode it prevents
When to ask / apply it
What evidence matters
What changes in Xyool if the answer changes
Authority boundary
Nameless example
Counterexample / anti-false-positive example
Validation status
Demotion / invalidation condition
Origin / regression link where useful
```

Not every document needs identical headings, but the substance should be present.

## Explanation rule

Do not add a principle as unexplained wording.

For every promoted principle or question, explain the causal reason it matters.

The explanation should answer:

> **What mistake becomes less likely if Xyool asks this question or applies this principle?**

and:

> **How can the answer alter Quality, OSE/FES, TTC, Quant interpretation, research priority, or capital action?**

## Example rule

Prefer a **nameless example** in canonical skills when the company identity is not needed to understand the causal pattern.

Example:

```text
A supplier receives a first paid deployment at one customer site.
Three months later the same customer orders a second site using the same product and approval path.

Correct lesson:
A repeatable rollout may now exist. Measure the interval, verify the causal process can repeat, and create a widened next-repeat window.

Incorrect lesson:
The customer will place another order exactly three months later.
```

Nameless examples reduce ticker anchoring and make transfer across industries easier.

## When named examples are appropriate

Use named examples in:
- research/system-tests;
- regression artifacts;
- audit trails;
- continuity notes explaining why a rule was introduced;
- cases where the specific contractual/procurement structure is itself material.

Canonical logic should not depend on the identity of the original winner or loser.

A good pattern is:

```text
CANONICAL SKILL
→ nameless explanation + nameless example

RESEARCH / REGRESSION FILE
→ named case + dates + evidence + outcome
```

## Counterexample rule

Whenever a principle could create a false positive, include at least one case where it should **not** apply.

Example:

```text
Two orders occur three months apart, but they came from unrelated customers under different programs.

Do not infer a same-customer rollout cadence merely because the dates happen to match.
```

## Authority rule

Every principle/question must state where it feeds the system.

Examples:
- research-only question;
- OSE state input;
- FES timing input;
- Quality gate input;
- TTC timing/ranking input;
- Quant diagnostic.

A new principle does not silently acquire independent allocation authority.

## Discovery rule

As Xyool discovers a genuinely generalizable principle, record it rather than relying on conversational memory.

Use the Miss-to-Question Learning Loop when the principle came from a process miss.

The standard is:

> **Discover → explain → generalize → give a transferable example → define limits → test → promote at the correct authority level.**

## Anti-bloat rule

Do not turn every observation into a permanent principle.

Promote only when the idea:
- changes a recurring decision or research process;
- is generalizable beyond one case;
- is expressible using pre-outcome evidence;
- has a clear failure mode or boundary;
- adds information rather than duplicating an existing principle.

## Success criterion

A future Xyool run should be able to read the canonical principle and answer:
1. what is being asked;
2. why it is being asked;
3. what evidence would satisfy it;
4. what evidence would refute it;
5. how the answer changes the system;
6. without needing to know which stock originally inspired the rule.
