# User Concept — Better Questions Instead of Better Loops

Date: **2026-09-22**  
Status: **ACTIVE / CORE REASONING PHILOSOPHY**

## USER-STATED WORDING

> "if we get one crappy question ... that leads to a crappy answer ... why don't we ask a better question that leads to a better answer?"

> "if it just leads to crappy results, we ask another question"

> "continuously do that until we find a question that actually gives us a result that is workable"

> "That way we can stop having to loop."

> "We just keep asking the questions until we reach a bottleneck."

## CONCEPT

The user proposes that recursive reasoning should optimize **the question itself**, not merely the answer.

If a question produces weak, non-discriminating, or unusable results, Xyool should:
1. diagnose why the question failed;
2. formulate a materially better question;
3. ask/test it;
4. repeat until the result becomes workable;
5. stop when a real bottleneck is reached.

## RATIONALE — USER-STATED / DIRECTLY SUPPORTED

A bad question can trap the system in repeated poor answers.

Changing models, features, or implementation does not help if the underlying question remains malformed.

The user sees better questioning as a way to avoid loops.

## ASSISTANT INTERPRETATION

This creates a **Question Frontier**:

```text
GOAL
→ QUESTION
→ RESULT
→ QUESTION QUALITY AUDIT
→ BETTER QUESTION
→ RESULT
→ ...
→ WORKABLE RESULT or BOTTLENECK
```

The important distinction is between:
- reformulating intelligently;
- endlessly rewording the same question.

A new question should change the target, unit, causal boundary, time scale, comparison, or evidence requirement in a meaningful way.

## SYSTEM CONSEQUENCE

Created:
`floware/core/question-frontier.flow.md`

The Question Frontier becomes a reusable core Flow for:
- development;
- research;
- recursive learning;
- domain analysis.

## OPEN QUESTIONS

- Should Xyool maintain a reusable library of high-value questions by domain?
- How should question information value be estimated without a numeric score?
- Should bottleneck types become first-class state across all domains?
- Can successful question transformations themselves be transferred by correspondence?
