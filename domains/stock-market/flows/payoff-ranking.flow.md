# FLOW — Stock Payoff Ranking

FLOW ID: `STOCK-PAYOFF-RANKING-V1`  
STATUS: **ACTIVE / FROZEN DEVELOPMENT GOAL**  
DOMAIN: stock-market  
JOB: payoff-ranking  
AUTHORITY: development / shadow only  
PARENT GOALPOST: `research/system-tests/stock-payoff-ranking-goalpost-v1-2026-09-22.md`

## GOAL

Finish an effective, evidence-based payoff-ranking architecture that ranks Quality-eligible opportunities by expected shareholder payoff well enough to support a later capital-allocation stage.

The goal is fixed until ACHIEVED or formally INVALIDATED.

## SUCCESS STANDARD

Use the frozen goalpost file.

Key gates include:
- beat B1 and B2 on the consumed development/regression library;
- avoid dependence on one/two extreme cases;
- no major tested cohort below 50% pairwise ordering;
- materially improve magnitude usefulness, with >=50% interval coverage target without uselessly wide ranges;
- justify every retained layer;
- only then run the frozen untouched validation campaign.

Perfection is not required.

## INPUT STATE

For each case/opportunity:
- Quality eligibility;
- economic/causal state;
- event identity;
- event-local uncertainty removal/materiality;
- recognition context;
- next-event/TTC/dependency state;
- valuation/shareholder-capture context;
- known consumed outcome when in development mode.

## FLOW ARCHITECTURE

```text
QUALITY CREDENTIALS / ELIGIBILITY
      ↓
NARRATIVE THESIS / CONNECTION MAP
      ↓
EVENT-LOCAL PAYOFF FLOW
      ↓
ARCHETYPE-CONDITIONED RECOGNITION / MARKET CONTEXT
      ↓
NEXT-EVENT / TTC / DEPENDENCY FLOW
      ↓
CAPITAL-PATH PAYOFF
      ↓
RELATIVE PAYOFF RANK
      ↓
MAGNITUDE / ROBUSTNESS AUDIT
```

## PROCESS

### A. Event-local payoff

Ask:
- What actually changed?
- How material is it to this company?
- What uncertainty was removed?
- What economics are capturable by common shareholders?
- What remains unresolved before the next material state?

Output:
`EVENT_LOCAL_PAYOFF_STATE`

### B. Recognition / context

Treat recognition as descriptive/contextual unless an archetype-local mapping has earned direction.

Do not assume:
- high recognition = bad;
- weak TA = underrecognized;
- strong TA = continuation;
- strong TA = exhaustion.

Output:
`RECOGNITION_CONTEXT`

### C. Capital path

Canonical subflow:
`capital-path.flow.md`

Do not treat the capital horizon as a longer attribution window for the entry event.

Build:
- the pre-visible material-node inventory inside the horizon;
- relation of each node to the entry event;
- information type;
- timing visibility;
- company-relative materiality;
- shareholder capture;
- node/path-specific Recognition;
- Dominant Capital-Path Node (DCPN) when evidence supports one.

Ask:
- What material information states were already visible at entry?
- Which are same-chain realizations versus genuinely independent nodes?
- Which node can most alter shareholder payoff inside the horizon?
- What economics would be double-counted if multiple nodes were added?
- What should remain unordered because evidence does not discriminate?

Output:
`CAPITAL_PATH_STATE`

### D. Rank

Compare eligible opportunities on:
- expected payoff distribution;
- downside;
- timing;
- future-state uncertainty;
- recognition burden only where locally justified;
- opportunity cost.

Do not compress into a universal master score unless evidence earns it.

Selective ordering is allowed during development. Do not force pairwise precision where the Flow is materially non-discriminating; report abstentions separately.

## ADAPTATION

Different archetypes may use different local mappings while sharing the same Flow structure.

Correspondence transfers the question/structure, not the sign/weight/threshold.

## REGRESSION SET

Use the frozen hard cases:
HOOD, IOT, AFRM, SE, IONS, ARWR, CAVA, CRSP, VKTX, ALT, DUOL, SWTX.

## METHOD FAILURE

When an approach fails:
```text
PRESERVE FAILURE
→ DIAGNOSE
→ SIMPLIFY / REDESIGN FLOW
→ SAME GOALPOST
```

Do not change the goal.

## BOUNDARIES

Until this goal is achieved:
- no production sizing;
- no leverage optimization;
- no execution optimization except outcome-definition necessities;
- no routine fresh-stock consumption;
- no new universal master score;
- no unrelated research branch taking over the goal.

## OUTPUT STATE

For each candidate:
- event-local payoff state/range;
- recognition/context state;
- next-event/TTC state;
- capital-path payoff state/range;
- downside/invalidation;
- relative payoff rank;
- confidence;
- blockers;
- explanation of rank.

For the program:
- current success-gate status;
- method failures;
- regression status;
- whether untouched validation is authorized yet.

## LEARNING HOOK

Use consumed cases for development.
Use untouched cases only after development gates are met.

All material misses route to:
`floware/core/learning.flow.md`

## SOFTWARE / HARD-LIMIT BOUNDARY

Default:
`NONE — FLOWARE SUFFICIENT FOR REASONING ARCHITECTURE`

Software may be introduced only if `floware/core/software-escalation.flow.md` finds a justified exact-computation, persistence, or hard-limit need.

The current focus is the Flow itself.


## DEVELOPMENT SPEED

For each unresolved payoff question:

1. run `floware/core/direct-resolution.flow.md`;
2. attempt the simplest structural answer from existing consumed evidence;
3. attack it with the cheapest material contradiction;
4. use the answer provisionally if it is workable;
5. escalate to a broader consumed regression only when needed;
6. use a new tournament/cohort only when cheaper evidence cannot discriminate.

Do not make every payoff question pay tournament-level proof cost.


## Narrative requirement

Before final payoff ranking, load:

`narrative-thesis.flow.md`

The payoff model should understand the causal story it is ranking.

Do not let a score hide an unmapped relationship, dependency, or shareholder-capture break.


## Quality boundary

Payoff ranking begins after the Quality credentials screen:

`quality-credentials.flow.md`

Do not make payoff ranking redo the Quality job.

Quality determines whether the opportunity deserves normal capital competition. Payoff ranking compares the qualified opportunities.
