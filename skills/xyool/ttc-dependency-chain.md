# Xyool — TTC Dependency Chain / Gating-Node Framework

Status: **CANONICAL PROCESS — GRAPH STRUCTURE REQUIRED FOR MATERIAL MULTI-GATE CATALYSTS; NUMERIC JOINT-PROBABILITY CALIBRATION PROVISIONAL**

## Core purpose

Breadcrumbs, timers, and catalysts should not be interpreted as independent items when the economic outcome requires a sequence of prerequisite events.

For every material multi-gate opportunity, Xyool should represent the causal path as a directed dependency graph:

```text
BREADCRUMB / CURRENT STATE
        ↓
PREREQUISITE GATE(S)
        ↓
ECONOMIC CONVERSION GATE
        ↓
REVENUE / GROSS PROFIT
        ↓
CASH / GAAP PROFITABILITY
        ↓
SHAREHOLDER-CAPTURABLE VALUE
```

Core question:

> **Which unresolved node currently gates the largest economically meaningful downstream path, and what evidence would satisfy or break that dependency?**

This module does not create a new allocator. Quality still owns eligibility. TTC still owns capital priority. Quant remains downstream expression.

---

## 1. Why a graph is required

A flat catalyst list can overstate opportunity by treating sequential events as additive independent catalysts.

Example:

```text
definitive partner agreement
→ acquisition closing
→ manufacturing localization
→ qualification
→ production order
→ revenue
→ gross profit
→ cash breakeven
```

The production order cannot be assigned full value if the upstream acquisition or partner agreement is unresolved.

Likewise, a patent filing, a financing event, and a manufacturing agreement may all occur near each other without belonging to the same economic path.

The graph exists to preserve:
- prerequisite structure;
- serial versus parallel paths;
- the next executable gate;
- terminal economic endpoints;
- failure propagation;
- time-to-economic-impact;
- shareholder-capture dependencies.

---

## 2. Node model

Each material graph node should record, where evidence permits:

```text
node_id
label
node_type
state
satisfied
evidence_status
event_key
timer_ids
expected_window
economic_role
materiality
evidence_ids
invalidation
notes
```

Recommended node types:

```text
BREADCRUMB
AGREEMENT
APPROVAL
FINANCING
ACQUISITION_CLOSE
INTEGRATION
CAPACITY
QUALIFICATION
PROCUREMENT
DEPLOYMENT
REVENUE
GROSS_PROFIT
CASH_BREAKEVEN
GAAP_PROFIT
SHAREHOLDER_CAPTURE
RECOGNITION
```

Node type is descriptive, not a numeric weight.

### Satisfied

Use an explicit `satisfied` boolean for graph mechanics.

A node can be economically unfavorable and still be satisfied as a prerequisite. Example: financing may close but materially damage shareholder capture.

Graph satisfaction does **not** mean the node is bullish.

---

## 3. Edge model

Edges describe causal dependency:

```text
from
to
relationship
required
evidence_ids
notes
```

Recommended relationships:

```text
REQUIRES
UNLOCKS
ENABLES
CONVERTS_TO
FUNDS
QUALIFIES_FOR
DEPLOYS_INTO
TRANSLATES_TO
```

Use `required: true` when the downstream node cannot reasonably occur through the modeled path without the upstream node.

Use `required: false` for supporting or probability-improving evidence that is not a strict prerequisite.

Do not create an edge solely because two events are temporally adjacent.

---

## 4. Frontier / gating nodes

A **frontier gate** is an unresolved node whose required predecessors are satisfied.

This is the graph equivalent of the next actionable causal step.

For a simple serial chain:

```text
A satisfied
→ B unresolved
→ C unresolved
→ D unresolved
```

the frontier gate is `B`.

For parallel prerequisites:

```text
A satisfied ─┐
             ├→ D
B unresolved ┤
C unresolved ┘
```

both `B` and `C` can be frontier gates.

### Primary gating node

Xyool may designate one `primary_gate_id` when evidence supports that it is the most economically consequential unresolved frontier node.

The designation must include a plain-language rationale. It is not automatically chosen by timer proximity or node count.

Prefer the gate that:
- blocks a material economic path;
- has identifiable evidence/timing;
- meaningfully changes probability of downstream conversion;
- is not already economically recognized;
- has shareholder-capturable downstream value.

---

## 5. Critical path

For each economically important terminal node, identify the prerequisite path(s).

Relevant terminal nodes commonly include:

```text
FUNDED ORDER
REVENUE RUN-RATE
GROSS PROFIT
CASH BREAKEVEN
GAAP PROFIT
SHAREHOLDER-CAPTURABLE VALUE
```

The **critical path** is the path whose unresolved gates currently govern the timing or probability of the terminal economic outcome.

Do not assume the shortest chronological path is the highest-value path.

---

## 6. Three event identities must remain separate

For a multi-gate graph always preserve:

```text
NEXT CHRONOLOGICAL EVENT
NEXT ECONOMIC CONVERSION EVENT
NEXT PROFIT-PRODUCING EVENT
```

and add:

```text
PRIMARY GATING NODE
TERMINAL ECONOMIC NODE
```

These can all be different.

---

## 7. Profitability transmission

For every material path ask:

```text
What economics exist if this gate succeeds?
What additional gates remain?
When can revenue begin?
What gross profit could result?
What fixed-cost / cash-burn gap remains?
What dilution / financing is required before shareholders capture it?
```

Useful derived fields:

```text
profitability_gap
profitability_gap_closure
time_to_revenue
time_to_gross_profit
time_to_cash_breakeven
time_to_gaap_profit
ownership_retention / dilution state
```

Do not infer exact values when accounting, margin, capex, or share-count evidence is inadequate.

---

## 8. Joint probability — provisional only

For a purely serial path, the conceptual probability of reaching a downstream node depends on the conditional probabilities of all required unresolved gates.

Conceptually:

```text
P(terminal) = Π P(gate_i | upstream gates satisfied)
```

This is useful for forcing the right question, but **Xyool must not fabricate independence or precise probabilities**.

Rules:
- use conditional probabilities where dependencies are strong;
- do not multiply generic point estimates merely because a formula is available;
- widen uncertainty when evidence is weak;
- preserve correlated failure modes;
- keep universal numeric weights PROVISIONAL until validated.

The graph structure is canonical. Universal joint-probability calibration is not.

---

## 9. Dependency leverage

A gate can matter more than its immediate headline economics if it unlocks a large downstream path.

Record qualitatively:

```text
downstream economic scope
number/type of blocked material nodes
terminal economics unlocked
time compression if satisfied
```

A provisional research metric may examine:

```text
downstream shareholder-capturable value
÷ current equity value
÷ time to expected economic impact
```

but no universal `Catalyst Leverage Ratio` becomes production authority without validation.

---

## 10. Deadline persistence

When a material gate misses an expected date, classify the response:

```text
MISSED + TERMINATED
MISSED + SILENCE
MISSED + EXTENDED
MISSED + EXTENDED + NEW CAPITAL COMMITMENT
MISSED + EXTENDED + MORE SPECIFIC CONTRACTUAL CONDITION
```

A deadline extension is not automatically positive.

However, continued capital commitment, preserved contractual specificity, or repeated counterparty work can provide evidence that the path remains active.

Record it as evidence that changes:
- timer state;
- management timing credibility;
- gate probability;
- or nothing.

Do not silently move the old timer forward.

---

## 11. Counterfactual management behavior

When management abandons one comparable project but continues funding or negotiating another, use the contrast as evidence about selectivity.

Ask:

> **What did management do with similar opportunities it chose not to continue?**

This may improve or weaken confidence in the active path, but it cannot replace third-party evidence or economics.

---

## 12. External counterparty corroboration

A company claim gains credibility when the counterparty independently discloses strategy or actions consistent with the claimed path.

Classify corroboration:

```text
NONE
ONE-SIDED
PARTIAL INDEPENDENT
DIRECT COUNTERPARTY
MULTI-PARTY
```

Check:
- partner investor materials;
- customer procurement documents;
- regulator records;
- exchange filings;
- supplier disclosures.

Counterparty corroboration changes evidence quality, not event identity.

---

## 13. Hidden architecture inference

Xyool may infer a plausible link across breadcrumbs when several facts jointly imply an operational design.

Required output:

```text
INFERRED LINK
supporting evidence_ids
confidence
alternative explanations
falsification event
```

Never store an inference as a confirmed fact.

Example pattern:

```text
capital allocated for facility outside current geography
+ named manufacturing partner in another geography
+ partner independently states localization strategy
→ inferred localization architecture
```

---

## 14. Volume quality

Unusual volume should be mapped to the graph rather than treated as a catalyst by itself.

Classify:

```text
INFORMATION_VOLUME
NARRATIVE_VOLUME
CAPITAL_STRUCTURE_VOLUME
POSITIONING_VOLUME
MIXED / UNKNOWN
```

Volume can change Recognition or research priority.

It does not satisfy an economic dependency node unless the underlying event itself is verified.

---

## 15. Failure propagation

If a required upstream node fails:

```text
FAILED REQUIRED NODE
→ mark dependent path BLOCKED / INVALIDATED
→ close or demote affected timers
→ remove unsupported downstream probability
→ preserve independent parallel paths
```

Do not invalidate unrelated branches.

If a node is superseded by a new mechanism, create a new edge/path rather than rewriting historical evidence.

---

## 16. Persistent-state contract

For stock entities, persist:

```text
dependency_graph:
  graph_version
  as_of
  primary_gate_id
  terminal_node_ids
  nodes[]
  edges[]
  analyst_rationale
```

Derived runtime analysis may calculate:

```text
frontier_gate_ids
blocked_node_ids
satisfied_node_ids
unsatisfied_node_ids
downstream_node_counts
cycle_status
```

The graph should remain compact. Detailed source text belongs in the evidence ledger.

---

## 17. Mandatory workflow

When a material multi-gate catalyst exists:

```text
1. Identify exact event identities.
2. Convert breadcrumbs into candidate nodes.
3. Identify strict versus supporting dependencies.
4. Build/update the DAG.
5. Mark satisfied versus unresolved nodes from evidence.
6. Identify frontier gate(s).
7. Designate primary gate only with rationale.
8. Identify next chronological, economic-conversion, and profit-producing events.
9. Trace profitability and shareholder-capture transmission.
10. Map each active gate to timer(s).
11. Apply recognition, dilution, failure, and delay state.
12. Report the state change.
```

A material multi-gate catalyst analysis is incomplete if the dependency chain is known but left only in prose.

---

## 18. What this framework must not do

Do not:
- count every node as an independent catalyst;
- award more TTC value merely because a graph has more nodes;
- multiply unvalidated probabilities mechanically;
- infer a signed agreement from strategic fit;
- treat partner strategy as proof of a specific transaction;
- confuse a satisfied financing node with good shareholder capture;
- treat volume as node completion;
- promote a blocked Quality name because its dependency chain is exciting.

---

## 19. Required validation

Prospectively record:
- graph as known before outcome;
- frontier gates;
- primary gate rationale;
- actual gate completion/failure;
- time between nodes;
- price response at each node;
- revenue/gross-profit realization;
- dilution/share-count change;
- whether graph use changed TTC priority versus flat-catalyst treatment.

Validation targets:
1. fewer double-counted catalysts;
2. earlier identification of economically decisive gates;
3. better time-to-economic-impact estimates;
4. fewer false positives from narrative catalysts;
5. improved profitability ranking without excessive turnover or hindsight fit.

---

## Core rule

> **Do not ask only “What catalysts exist?” Ask “What must happen first, what does that unlock, and how does the chain transmit into shareholder-capturable profit?”**
