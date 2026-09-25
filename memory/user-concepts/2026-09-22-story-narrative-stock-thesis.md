# User Concept — Reduce Stock Analysis to Story / Narrative

Date: **2026-09-22**  
Status: **ACTIVE / CORE STOCK-REASONING PHILOSOPHY**

## USER-STATED WORDING

> "I think we need to reduce this to a story/narrative."

> "We have all the information so all we are doing is mapping (wrapper and pointers) it and coming up with a thesis."

> "we know ... VWAV has a lot of connections so we also should understand how those connections ... [influence] VWAV."

> "When we overlook something then that is a miss."

## CONCEPT

The user wants stock analysis to stop at a coherent causal story rather than a collection of disconnected facts and scores.

Once the information exists, Xyool's job is to map:
- entities;
- relationships;
- wrappers;
- pointers;
- dependencies;
- control;
- economics;
- timing

into a thesis.

## ASSISTANT INTERPRETATION

The stock narrative is effectively a human-readable projection of the company graph.

```text
EVIDENCE
→ ENTITY / CONNECTION GRAPH
→ CAUSAL STORY
→ THESIS
→ PAYOFF / INVALIDATION
```

The narrative should reveal what the company is becoming and how value can or cannot reach shareholders.

## MISS DEFINITION

A miss includes any material relationship or connection that existed in the evidence but was not mapped into the thesis.

This means Xyool can miss even when it has technically collected the underlying document.

The failure may be:
- retrieval miss;
- mapping miss;
- relationship miss;
- causal miss;
- interpretation miss.

## SYSTEM CONSEQUENCE

Created:

`domains/stock-market/flows/narrative-thesis.flow.md`

The stock domain should produce a narrative thesis after evidence mapping and before final payoff judgment.

## RELATED CONCEPTS

- Floware
- Wrappers and pointers
- Correspondence
- Direct Resolution
- Question Frontier
- Stock company memory
