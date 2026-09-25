# FLOW — Stock Capital Path

FLOW ID: `STOCK-CAPITAL-PATH-V1`  
STATUS: **ACTIVE / DEVELOPMENT**  
DOMAIN: stock-market  
JOB: fixed-horizon payoff path  
AUTHORITY: development / shadow only  
PARENT FLOW: `payoff-ranking.flow.md`

## GOAL

Represent the capital outcome horizon as a sequence of **pre-visible material information nodes** rather than attributing the entire horizon to the event that opened the position.

Core law:

> **Capital accounting follows the whole path. Capital forecasting must therefore model the information path that was visible at entry.**

## INPUT STATE

- event-local payoff state;
- frozen entry date;
- intended capital horizon;
- unresolved catalyst/dependency state known at entry;
- scheduled/guided future events known at entry;
- shareholder-capture state;
- downside/repricing state;
- Recognition context.

## PROCESS

```text
FREEZE ENTRY INFORMATION
→ INVENTORY MATERIAL NODES INSIDE HORIZON
→ CLASSIFY RELATION TO ENTRY EVENT
→ CLASSIFY INFORMATION TYPE
→ CLASSIFY TIMING VISIBILITY
→ ESTIMATE COMPANY-RELATIVE MATERIALITY
→ APPLY DOUBLE-COUNT GUARD
→ IDENTIFY DOMINANT CAPITAL-PATH NODE(S)
→ APPLY RECOGNITION TO THE RELEVANT NODE/PATH
→ BUILD CAPITAL-PATH STATE
→ ORDER ONLY WHERE EVIDENCE DISCRIMINATES
```

## 1. HORIZON NODE INVENTORY

A node belongs in the capital path only if, at entry, public evidence already made the node or its causal path visible.

Do not add a later event merely because it eventually happened.

Allowed visibility:

```text
HARD_DATE
COMPANY_GUIDED_WINDOW
CAUSALLY_ARMED / UNSCHEDULED
LATENT — visible path but weak timing
UNKNOWN
```

A node that was not knowable at entry may explain a later outcome, but it cannot be used as a predictive feature in reconstruction.

## 2. NODE RELATION TO THE ENTRY EVENT

Classify each material future node:

### SAME_CHAIN_REALIZATION

The node mostly realizes economics already created by the entry event.

Examples:
- product availability after approval;
- first shipment/sale after an already approved launch;
- ordinary deployment after funded procurement.

Guardrail:
Do not count the same economics twice.

### RECURRENT_REMEASUREMENT

The node remeasures an ongoing process rather than merely realizing the prior event.

Examples:
- next earnings report for a recurring operating engine;
- next order/cadence observation;
- next utilization/adoption update.

This is new information, but the causal process is continuous.

### ADJACENT_SAME_FRANCHISE

The node provides genuinely new evidence but remains tied to the same asset/franchise.

Examples:
- new indication data;
- combination data;
- additional clinical readout for the same core asset.

### PARALLEL_INDEPENDENT

The node belongs to another program, product, customer, contract, or causal path whose outcome can materially alter shareholder payoff independently of the entry event.

Examples:
- another drug's Phase 3 result;
- a distinct partnership milestone;
- a different regulatory decision.

### UNKNOWN_RELATION

Do not force a relation when evidence is insufficient.

## 3. INFORMATION TYPE

Classify what can change:

```text
REALIZATION
NEW_EVIDENCE
BINARY_DECISION
CASH / CONTRACT MILESTONE
FUNDING / FINANCING
GUIDANCE / EARNINGS
OTHER MATERIAL STATE
```

Serial realization generally contains less incremental information than a genuinely independent binary decision or new clinical/economic evidence, but no universal weight is assumed.

## 4. PATH REGIME

After node inventory, classify the capital path:

```text
INDEPENDENT_NODE_DOMINANT
RECURRENT_PROCESS
SAME_CHAIN_REALIZATION
ENTRY_EVENT_DECAY / NO_DOMINANT_VISIBLE_NODE
MIXED
UNKNOWN
```

This is a routing state, not a score.

### INDEPENDENT_NODE_DOMINANT
A distinct material node inside the horizon can change the payoff distribution independently of the entry event.

### RECURRENT_PROCESS
The capital path is primarily continued observation of an ongoing operating/economic process.

Canonical subflow:
`recurrent-process.flow.md`

### SAME_CHAIN_REALIZATION
The path primarily realizes economics already created by the entry event.

### ENTRY_EVENT_DECAY / NO_DOMINANT_VISIBLE_NODE
No sufficiently material pre-visible node inside the horizon displaces the entry-event state. Capital behavior may be dominated by recognition, valuation/repricing, uncertainty decay, or unforeseeable new information.

### MIXED
Multiple regimes materially overlap.

## 5. DOMINANT CAPITAL-PATH NODE

Ask:

> **Which unresolved node, known at entry, has the greatest plausible ability to change shareholder payoff during this horizon?**

This is the **Dominant Capital-Path Node (DCPN)**.

The DCPN may be:
- the entry event's downstream realization;
- an adjacent franchise event;
- a parallel independent event.

If a later independent node materially dominates the horizon, the capital forecast should not continue pretending the original event is the sole causal object.

## 6. RECOGNITION ATTACHMENT

Recognition is not a free-floating stock penalty.

Ask:

> **Recognition of what?**

Attach Recognition context to:
- the entry event;
- the DCPN;
- or the path as a whole when evidence cannot separate them.

A highly recognized entry event does not imply that an independent upcoming program milestone is equally recognized.

Likewise, an underrecognized entry event does not imply every downstream event retains headroom.

## 7. DOUBLE-COUNT GUARD

Do not count:
- approval and launch as two copies of the same value;
- first sale and already-modeled commercialization as independent economics;
- contract signing and funded realization as separate full values;
- multiple data presentations of substantially the same information as independent catalysts.

The question is:

> **What new uncertainty or economics does this node add beyond what prior nodes already created?**

## 8. SELECTIVE ORDERING / ABSTENTION

Do not force a full order when the path state does not discriminate.

Allowed result:

```text
A > B
A ~ B — INSUFFICIENT DISCRIMINATION
BLOCKED
```

Development scoring must report abstentions separately rather than treating false precision as intelligence.

A later version may define a frozen abstention scoring rule before validation.

## 9. OUTPUT STATE

For each opportunity:

```text
ENTRY EVENT:
CAPITAL HORIZON:
VISIBLE MATERIAL NODES:
  - node
  - relation
  - information type
  - timing visibility
  - materiality
  - shareholder capture
  - Recognition context
PATH REGIME:
DOMINANT CAPITAL-PATH NODE:
DOUBLE-COUNT NOTES:
CAPITAL-PATH STATE:
DOWNSIDE / INVALIDATION:
ORDERING CONFIDENCE:
BLOCKERS:
```

## 10. LEARNING HOOK

When capital outcome and event attribution diverge:

1. identify the first later material event;
2. ask whether its path was visible at entry;
3. if visible, audit whether the Capital-Path Flow represented it;
4. if not visible, classify it as unforeseeable/new information rather than retrofitting the model.

## 11. SOFTWARE / HARD-LIMIT BOUNDARY

`NONE — FLOWARE SUFFICIENT`

Exact return arithmetic may use existing deterministic tooling when needed, but capital-path reasoning remains Floware.
