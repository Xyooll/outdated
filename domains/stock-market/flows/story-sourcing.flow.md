# FLOW — Stock Story Sourcing

FLOW ID: `STOCK-STORY-SOURCING-V1`  
STATUS: **ACTIVE / CANONICAL**  
DOMAIN: stock-market  
JOB: build the most accurate stock story from the strongest available evidence for every material character and claim
CORE PARENT FLOW: `../../../floware/core/relational-story.flow.md`  

## GOAL

Source the evidence that becomes the story.

Core law:

> **The quality of the story cannot exceed the quality of the evidence supporting it.**

This applies to:
- the public parent;
- every subsidiary;
- every material investee/JV;
- every material customer, partner, regulator, financier, lender, government, insider, acquisition target, supplier, distributor, exchange, or other character.

## 1. SOURCE THE CLAIM, NOT JUST THE COMPANY

Source strength is claim-specific.

Ask:

```text
WHAT EXACTLY ARE WE CLAIMING?
WHO WOULD KNOW IT DIRECTLY?
WHO HAS LEGAL / OPERATIONAL AUTHORITY OVER IT?
WHAT DOCUMENT CREATES OR RECORDS THE STATE?
IS THERE AN INDEPENDENT COUNTERPARTY SOURCE?
IS THE SOURCE CURRENT?
```

Do not label an entire source universally 'strong' or 'weak'.

A filing may contain:
- audited/reportable financial facts;
- binding contract terms;
- management estimates;
- forward-looking claims;
- third-party statements quoted by management.

Those do not carry equal evidentiary weight.

## 2. PREFERRED SOURCE LADDER

Use the strongest source that directly supports the claim.

### TIER A — STATE-CREATING / AUTHORITATIVE PRIMARY EVIDENCE

Examples:
- executed contracts / amendments / exhibits;
- regulator decisions / official dockets;
- court orders / judgments;
- government procurement awards / obligations;
- exchange/listing notices;
- audited or filed financial statements;
- official ownership filings;
- definitive transaction documents;
- customer purchase/order records when directly disclosed by the customer/authority.

These sources often create, legally establish, or directly record the state.

### TIER B — DIRECT FIRST-PARTY / COUNTERPARTY EVIDENCE

Examples:
- issuer filings and official releases;
- customer releases;
- partner releases;
- regulator/company correspondence;
- official presentations / earnings calls;
- named executive statements;
- official project/program pages.

Useful and often primary, but distinguish verified fact from management characterization or forward-looking language.

### TIER C — HIGH-QUALITY INDEPENDENT SECONDARY EVIDENCE

Examples:
- reputable financial/news reporting;
- specialist trade publications;
- established industry databases;
- analyst/transcript services where original material is unavailable.

Use for discovery, context, corroboration, and gaps.

Do not let secondary interpretation override stronger primary evidence.

### TIER D — DISCOVERY / WEAK CONTEXT

Examples:
- aggregators;
- unsourced reposts;
- promotional sites;
- social posts;
- message boards;
- anonymous claims;
- scraped summaries.

These can generate questions.

They do not close material story states without corroboration.

## 3. TWO-SIDED RELATIONSHIP SOURCING

For a material relationship, seek evidence from both sides where available.

Example:

```text
VWAV says SaverOne relationship exists
+ SaverOne says relationship/ownership exists
+ ownership filing / transaction document confirms terms
→ stronger relationship state
```

For customers:

```text
SUPPLIER SAYS 'CUSTOMER / ROLLOUT'
+ CUSTOMER CONFIRMS DEPLOYMENT / PROCUREMENT
→ stronger commercial story
```

For regulators/governments:

```text
COMPANY SAYS 'APPROVED / INVITED'
+ REGULATOR / AGENCY RECORD
→ stronger gate state
```

Absence of a second-side source is not automatically negative.

Record the evidence asymmetry.

## 3A. RELATIONSHIP-EDGE SOURCING

Source the **relationship itself**, not only the two characters.

For every material edge ask:

```text
WHAT CREATED THIS RELATIONSHIP?
WHAT DOCUMENT / EVENT DEFINES ITS TERMS?
IS IT STILL ACTIVE?
HAS ITS TYPE OR COMMITMENT CHANGED?
DID IT INTRODUCE A NEW CHARACTER?
IS THE RELATIONSHIP CONFIRMED FROM BOTH SIDES WHERE AVAILABLE?
```

Examples of edge evidence:
- executed agreement / amendment;
- acquisition close;
- ownership filing;
- customer purchase/order;
- financing agreement / restructuring;
- regulator order;
- subsidiary formation record;
- termination notice;
- court filing.

A strong source for Character A does not automatically prove A's relationship to Character B.

## 4. SOURCE QUALITY DIMENSIONS

For every material claim assess:

```text
AUTHORITY      — does the source control/record the state?
PROXIMITY      — how close is it to the underlying event?
DIRECTNESS     — fact/document vs interpretation/hearsay?
SPECIFICITY    — exact terms/state vs vague narrative?
FRESHNESS      — current enough for the claim?
INDEPENDENCE   — does corroboration come from another interested party/source?
PROVENANCE     — can we return to the exact evidence?
CONTRADICTION  — does stronger evidence disagree?
```

Do not compress these into a fake universal numeric score unless evidence earns it.

## 5. FACT / CLAIM TYPE

Classify material evidence:

```text
LEGAL / CONTRACTUAL FACT
REGULATORY / GOVERNMENT STATE
REPORTED FINANCIAL FACT
OWNERSHIP / CAPITAL-STRUCTURE FACT
OPERATING FACT
COUNTERPARTY-CONFIRMED FACT
MANAGEMENT CLAIM
FORWARD GUIDANCE / INTENT
THIRD-PARTY CLAIM
SECONDARY INTERPRETATION
INFERENCE
UNKNOWN
```

Primary-source location does not convert a management claim into an externally verified fact.

## 6. CHARACTER SOURCE PACKET

Every material character should have:

```text
CHARACTER:
LATEST PRIMARY FILINGS / REPORTS:
LATEST ISSUER / OFFICIAL NEWS:
COUNTERPARTY SOURCES:
REGULATOR / GOVERNMENT SOURCES:
OWNERSHIP / FINANCING SOURCES:
OPERATING / FINANCIAL SOURCES:
MATERIAL CLAIMS:
RELATIONSHIP EDGES:
BEST SOURCE PER CLAIM / EDGE:
CONTRADICTIONS:
SOURCE GAPS:
FRESH THROUGH:
```

## 6A. FOUR-DEGREE SOURCE COVERAGE

Source coverage follows the same character boundary as recursive story-building.

```text
DEGREE 0 — main stock; 4 degrees remaining
DEGREE 1 — direct material characters; 3 remaining
DEGREE 2 — material characters of Degree 1; 2 remaining
DEGREE 3 — material characters of Degree 2; 1 remaining
DEGREE 4 — material characters of Degree 3; boundary
```

For every material character encountered through Degree 4:
- build the required source packet;
- use the strongest claim-specific evidence available;
- record freshness and contradictions;
- propagate material consequences upward.

Materiality can stop sourcing earlier.

Normal source expansion does not open full Degree-5 character packets.

If a Degree-4 claim depends on evidence beyond the boundary, record:

`BEYOND-DEGREE-4 DEPENDENCY — NOT FULLY EXPANDED`

This preserves the boundary without pretending the dependency does not exist.

## 7. STORY CONSTRUCTION

Build the story only after the material claim-source map exists.

```text
SOURCES
→ VERIFIED / ATTRIBUTED CLAIMS
→ CHARACTER STATES
→ RELATIONSHIPS
→ CAUSAL STORY
→ THESIS
```

Every important sentence in the story should be traceable to evidence.

## 8. CONTRADICTION RULE

When sources conflict:

1. preserve both claims;
2. prefer stronger/more direct/more current authority for the state;
3. explain the contradiction;
4. do not average incompatible facts;
5. leave UNKNOWN/BLOCKED when the conflict cannot be resolved.

Example:

```text
COMPANY PRESS RELEASE
vs
EXECUTED CONTRACT
→ contract controls contract terms
```

```text
OLD FILING
vs
NEW REGULATORY ORDER
→ new order controls current state
```

## 9. SOURCE-QUALITY MISS

A sourcing miss occurs when:

- stronger available evidence was not checked;
- a material claim relied on a weak source when primary evidence was accessible;
- only one side of a material relationship was checked despite accessible counterparty evidence;
- a management assertion was treated as verified fact;
- stale evidence supported a current-state claim;
- contradictory stronger evidence was missed;
- a subsidiary/material character was not sourced independently of the parent;
- provenance was lost.

Canonical rule:

> **If better available evidence could materially change the story and Xyool failed to seek or incorporate it, that is a sourcing miss.**

## 10. STORY AUTHORITY

Final story state:

```text
SOURCE-SUPPORTED
SOURCE-PARTIAL — MATERIAL GAPS NAMED
SOURCE-BLOCKED — MATERIAL CLAIM CANNOT BE VERIFIED
```

A narrative can be useful while partial, but it may not present unsupported certainty.

## 10A. DISCOVERY SOURCE REGISTRY

Supporting registry:
- `../SOURCE-REGISTRY.md`
- `../sources/rss.yaml`

The registry provides known discovery surfaces, feed endpoints, cursor targets, and provenance metadata. It does not change the claim-specific source ladder in this Flow.

Canonical feed rule:

> **RSS detects change. The strongest claim-specific evidence determines state.**

For a material feed item:
1. map it to the correct character / security / relationship / event;
2. deduplicate it against the relevant source cursor and evidence;
3. resolve the canonical linked record;
4. apply this Flow's claim-specific authority and contradiction rules;
5. update only affected story branches and derived state.

Issuer-distribution wires are first-party discovery surfaces, not independent counterparty confirmation.

## 11. SOFTWARE / HARD-LIMIT BOUNDARY

`NONE — FLOWARE SUFFICIENT FOR SOURCE SELECTION / REASONING`

Software/tools may support retrieval, parsing, source cursors, exact filing extraction, and provenance persistence.