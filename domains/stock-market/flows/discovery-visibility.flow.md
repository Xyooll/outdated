# FLOW — Stock Discovery Visibility

FLOW ID: STOCK-DISCOVERY-VISIBILITY-V1
STATUS: **CANDIDATE / VERIFICATION_PENDING**
DOMAIN: stock-market
JOB: decide whether a security deserves research visibility before Quality capital eligibility is known
AUTHORITY: research visibility and discovery-lane classification only; no normal-capital, sizing, trade, or execution authority
PARENT GOALPOST: ../../../research/system-tests/floware-consolidation-v1-2026-09-24/GOALPOST.md
UPSTREAM FLOWS: Company Analysis, Story Sourcing, Evidence to State, Observation/Trigger where applicable
DOWNSTREAM FLOWS: Quality Credentials, Company Analysis
INBOUND PIPES: ../PLUMBING.md#pipe-stock-evidence-discovery
OUTBOUND PIPES: ../PLUMBING.md#pipe-stock-discovery-quality
SOFTWARE DEPENDENCIES: none; deterministic filing parsing/persistent state may supply evidence but does not decide visibility

## GOAL

Prevent valid high-upside transition evidence from disappearing merely because current Quality is weak, while keeping research visibility strictly separate from capital authority.

Canonical method:
../../../skills/xyool/discovery-visibility-gate.md

Core law:

> **Quality may block capital. Quality may not, by itself, block discovery.**

## GOALPOST

A candidate's discovery state is complete when:
- identity is locked;
- discovery lane is explicit;
- breadcrumb/quality basis is evidenced;
- hidden-transition candidates name the transition and economic terminal;
- falsification/invalidation is explicit;
- survival-to-unlock precheck is stated;
- provenance is retained;
- downstream Quality receives the candidate without any implied capital promotion.

## INPUT STATE

- issuer/security identity;
- current/stored evidence and freshness;
- current Quality if known;
- new breadcrumbs / filings / operating changes;
- transition/dependency clues;
- shareholder-capture/survival evidence where available.

## EVIDENCE

Use the strongest claim-specific evidence available under Story Sourcing.

SEC/company-memory facts may originate discovery, but filing presence alone is not a positive thesis.

## PROCESS

~~~text
LOCK SECURITY / ISSUER IDENTITY
→ BUILD ESTABLISHED-QUALITY CANDIDATE TEST
→ BUILD HIDDEN-TRANSITION BREADCRUMB TEST
→ UNION THE TWO DISCOVERY LANES
→ FOR HIDDEN TRANSITION:
      NAME CAUSAL TRANSITION
      CHECK DELTA / NOVELTY
      CHECK AGENCY / COMMITMENT
      NAME CONFIRMATION + INVALIDATION
      NAME ECONOMIC TERMINAL
      NAME PROVISIONAL DEPENDENCY PATH
      CHECK SURVIVAL TO UNLOCK
→ CLASSIFY DISCOVERY LANE
→ OUTPUT VISIBLE / RISK / REJECT / UNKNOWN
→ PIPE VISIBLE CANDIDATE TO QUALITY
~~~

## DISCOVERY LANES

~~~text
ESTABLISHED_QUALITY
HIDDEN_TRANSITION
BOTH
RISK_ONLY
UNKNOWN
~~~

Additional source-origin tags such as INSIDER_ORIGIN or STRATEGIC_OWNER may be retained without becoming independent lanes/capital signals.

## HIDDEN-TRANSITION GATES

Require:
1. specific state transition;
2. actual delta/new information;
3. observable agency/commitment;
4. falsifiable confirmation/invalidation path;
5. plausible economic link;
6. provisional dependency path;
7. survival-to-unlock precheck.

If the security cannot plausibly capture the economics, preserve the risk/evidence but do not classify hidden upside as capital-eligible.

## GATES

- identity/freshness sufficient for the claim;
- no current-Quality-only prefilter;
- visibility and capital eligibility remain separate;
- evidence provenance survives;
- Survival-to-Unlock FAIL cannot be hidden.

## ADAPTATION

Weak initial breadcrumbs may remain WATCH/UNKNOWN and be revisited by Observation/Trigger when genuinely new evidence arrives.

## BOUNDARIES

Discovery Visibility does not:
- grant normal capital eligibility;
- rank TTC/payoff;
- assign position size;
- convert insider activity directly into a thesis;
- infer hidden transitions from price action alone;
- override Quality.

## FAIL-CLOSED CONDITIONS

Return UNKNOWN/BLOCKED when identity, transition, economic link, or survival evidence is materially ambiguous.

## OUTPUT STATE

~~~text
DISCOVERY VISIBLE:
DISCOVERY LANE:
SOURCE ORIGIN TAGS:
BREADCRUMB:
CAUSAL TRANSITION:
ECONOMIC TERMINAL:
CURRENT QUALITY:
QUALITY TRAJECTORY:
QUALITY UNLOCK CONDITION:
SURVIVAL TO UNLOCK:
CURRENT CAPITAL STATUS:
CONFIRMATION:
INVALIDATION:
NEXT RESEARCH QUESTION:
PROVENANCE:
~~~

## LEARNING HOOK

Missed visible opportunities, noisy false positives, and cases hidden by pre-Quality filtering route to Learning through the stock/domain miss path.

## SOFTWARE / HARD-LIMIT BOUNDARY

NONE — FLOWARE SUFFICIENT

Deterministic SEC extraction or persistent storage may support evidence preparation only.

## COMPLEXITY RULE

Use the minimum discovery evidence needed to decide visibility. Do not run a broad hidden-transition search when the objective is a known security and discovery visibility is already established from fresh evidence.
