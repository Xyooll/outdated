# Xyool OSE — Cascade Score Extension

Status: **PROVISIONAL OSE HUNTING / STATE VARIABLE — NO INDEPENDENT CAPITAL AUTHORITY**

This file extends `opportunity-state-engine.md` with a customer-adoption cascade state. It is designed to detect when an initial commercial foothold is beginning to propagate across customer sites, units, programs, geographies, or architectures before the full economic effect is visible in trailing financial statements.

## Purpose

Cascade Score answers:

> **Is a validated deployment beginning to replicate into a broader commercial rollout, and how far has that rollout actually progressed?**

It is not a measure of sector demand, valuation, market momentum, or shareholder economics.

The intended causal chain is:

```text
FUNDED / REAL CUSTOMER NEED
        ↓
INITIAL QUALIFICATION / PILOT
        ↓
FIRST MEANINGFUL COMMERCIAL DEPLOYMENT
        ↓
REPEAT DEPLOYMENT / AUTHORIZED EXPANSION
        ↓
REALIZED MULTI-UNIT / MULTI-SITE ROLLOUT
        ↓
CASCADE AT SCALE
        ↓
REVENUE / MARGIN / CASH / PER-SHARE VALUE
```

Cascade Score is most useful in the gap between the first validated deployment and full financial recognition.

## Authority boundary

Cascade Score belongs inside OSE as a **hunting and state-transition variable**.

It may:
- increase research priority;
- strengthen the interpretation of Structural Confirmation when the rollout is causally linked to the company;
- improve the estimate of remaining Potential when replication expands the plausible economic destination;
- identify a transition from isolated validation to repeatable commercialization;
- inform CAC through the full OSE state.

It may not:
- create a position by itself;
- set or mechanically increase a CAC weight;
- promote Conversion Confirmation merely because deployments are increasing;
- override Friction, shareholder-capture failure, dilution, financing risk, or F5 conditions;
- replace Recognition analysis or Quant;
- be treated as a short-term price predictor.

A company can be CS5 and still be a poor equity if conversion economics are weak.

## Cascade Score — CS0 to CS5

- **CS0 — No cascade evidence:** no meaningful commercial deployment chain is visible.
- **CS1 — Qualification / pilot:** testing, qualification, proof-of-concept, trial, or limited pilot exists, but commercial replication is unproven.
- **CS2 — First meaningful commercial deployment:** a real customer has moved beyond pilot/qualification into a meaningful paid deployment, site, unit, program, or architecture.
- **CS3 — Repeat deployment or authorized expansion:** the same customer/program or an independently relevant customer has approved, funded, ordered, or initiated expansion beyond the first deployment. This may still be partly authorized rather than fully realized.
- **CS4 — Material realized rollout underway:** multiple units/sites/programs/geographies are actually deployed or being delivered at material scale, with evidence that replication is occurring rather than merely being permitted.
- **CS5 — Realized cascade at scale:** broad deployment is established and replication has become a major operating reality rather than an isolated project.

Level and velocity must be tracked separately.

### Cascade Velocity

- accelerating ↑↑
- improving ↑
- stable →
- weakening ↓
- collapsing ↓↓

## Authorized vs realized cascade

Do not equate a framework agreement, authorization, maximum quantity, option, or rollout intention with completed deployment.

Every CS3+ state must record:

```text
Cascade Realization: Authorized / Partially Realized / Realized
```

Examples:
- customer authorizes expansion from 10 units to up to 2,000, but capital and production are not yet available → CS3 / Authorized;
- hundreds of units are now deployed under that authorization → CS4 / Partially Realized or Realized;
- the large authorized fleet is actually in service at scale → CS5 / Realized.

This distinction is mandatory because authorized expansion can be economically meaningful while still carrying financing, execution, cancellation, or timing risk.

## Evidence grade — E1 to E3

Cascade evidence quality must be recorded separately from the CS level.

- **E1 — Aggregate evidence:** adoption, deployment, or revenue growth is reported, but the underlying rollout units/sites/customers are not explicitly traceable.
- **E2 — Program/customer explicit, units partly inferred:** a named customer, program, architecture, or rollout is explicit, but exact deployment counts or site progression are incomplete.
- **E3 — Explicit rollout evidence:** units, sites, facilities, lanes, robots, pods, ports, programs, geographies, or equivalent deployment increments are directly disclosed and time-sequenced.

Higher CS with weak evidence quality should carry lower confidence.

## What counts as cascade evidence

Prefer:
1. paid deployments after qualification;
2. repeat orders from the same customer/program;
3. explicit site-to-site or unit-to-unit expansion;
4. funded follow-on contracts;
5. increasing deployed unit counts;
6. customer statements describing rollout or standardization;
7. deliveries across multiple programs/geographies;
8. repeated deployment evidence across quarters;
9. customer architecture adoption that plausibly replicates through additional capacity.

Do not promote CS based only on:
- TAM;
- unsigned pipeline;
- non-binding MOUs;
- maximum contract values without funded orders;
- management claims of large future opportunity;
- one isolated deployment with no replication evidence;
- stock-price appreciation;
- analyst enthusiasm.

## Relationship to Sector Demand

Sector Demand and Cascade Score are different.

- Sector Demand asks whether the external end-market demand regime is strengthening across independent participants.
- Cascade Score asks whether this company is moving from one deployment into repeatable customer adoption.

A company can have:
- high SD and low CS: excellent sector, company rollout not yet proven;
- low/moderate SD and high CS: company is gaining share or executing unusually well inside a less explosive sector;
- high SD and high CS: external demand and company-specific replication are reinforcing each other.

Do not double count the same customer deployment as independent sector breadth.

## Relationship to Structural Confirmation

Cascade Score can strengthen SC when a rollout demonstrates that the company controls something customers repeatedly need.

But replication alone does not prove a durable bottleneck. A commodity product can also roll out quickly.

High CS should strengthen SC most when repeat adoption is connected to:
- qualification barriers;
- sole/limited-source status;
- embedded architecture;
- switching costs;
- scarce capacity;
- regulatory/mission-critical qualification;
- proprietary supply-chain access;
- recurring service/control rights.

## Relationship to Conversion Confirmation

CS does **not** promote CC mechanically.

CC still requires company-specific economic conversion:

```text
ORDERS → BOOKINGS → BACKLOG → DEPLOYMENT → REVENUE → MARGIN → EBITDA → OCF → FCF → PER-SHARE VALUE
```

High CS plus weak CC can identify a business with real adoption but poor shareholder economics.

This is a required anti-trap rule.

## Relationship to Recognition

Cascade Score is most valuable before the market has fully recognized the economic consequence of replication.

The desired hunting configuration is generally:

```text
CS2 → CS3 with ↑ / ↑↑ velocity
+ E2/E3 evidence
+ high remaining Potential
+ credible SC
+ improving CC
+ manageable Friction
+ incomplete Recognition
```

Do not wait mechanically for CS4. By CS4/CS5 the rollout may already be well recognized.

Conversely, do not increase merely because a CS3 event coincides with a price breakout. Recognition and remaining opportunity must still be evaluated separately.

## Required state fields

For every material cascade candidate record:

```text
Cascade Score: CS0-CS5
Cascade Velocity: ↑↑ / ↑ / → / ↓ / ↓↓
Cascade Evidence Grade: E1 / E2 / E3
Cascade Realization: Authorized / Partially Realized / Realized
Cascade Confidence: Low / Medium / High
Cascade Unit: facility / lane / pod / robot / port / program / architecture / other
Initial Deployment:
Latest Deployment / Expansion:
Best Evidence:
Weakest Link:
Next Trigger:
Invalidation:
```

## Event update rule

```text
OLD CASCADE STATE
        ↓
NEW CUSTOMER / PROGRAM EVIDENCE
        ↓
IS IT PAID / FUNDED / REAL?
        ↓
IS THIS FIRST DEPLOYMENT, REPEAT, AUTHORIZATION, OR REALIZED ROLLOUT?
        ↓
EVIDENCE GRADE?
        ↓
LEVEL + VELOCITY UPDATE
        ↓
IMPACT ON POTENTIAL / SC / CC / RL / FRICTION / RECOGNITION?
        ↓
NEW OSE STATE
        ↓
CAC INTERPRETATION
```

## Cross-stock calibration result

The initial broader test across OESX, CVU, CRDO, SOUN, SERV, and CHPT supports provisional use of CS as an OSE hunting variable.

Key findings:
- explicit facility/unit progression is the cleanest form of cascade evidence;
- aggregate deployment growth can still be useful but requires a lower evidence grade;
- authorized expansion must be separated from realized deployment;
- real cascade can precede large repricing;
- real cascade can also coexist with severe financing or conversion failure;
- therefore CS is informative but not sufficient for capital allocation.

See:
- `research/system-tests/2026-09-09-cascade-score-cross-stock-test.md`

## Validation status

**Provisional PASS for state/hunting usefulness.**

Not yet validated as an automatic capital rule.

Future validation should be point-in-time and ask:
- Does CS2→CS3 identify subsequent large commercial expansions earlier than trailing revenue growth alone?
- Does E2/E3 outperform E1 in precision?
- Does separating Authorized from Realized reduce false positives?
- Does adding CS improve discovery/selection after controlling for SC, CC, Sector Demand, Friction, and Recognition?
- Does CS improve next-dollar allocation when interpreted through CAC, without causing excessive chasing or financing-trap exposure?

Until that evidence exists, Cascade Score remains a **provisional OSE hunting/state extension, not independent allocation authority**.
