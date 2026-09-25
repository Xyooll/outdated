# Xyool — SEC Filing Company Memory

Status: **CANONICAL DISCOVERY / MEMORY INGESTION PROCESS — NO INDEPENDENT CAPITAL AUTHORITY**

## Purpose

Xyool should not treat SEC filings as isolated documents that must be reread from scratch.

The SEC layer is an evidence producer:

```text
SEC / EDGAR
→ new filing
→ form-specific extraction
→ normalized evidence events
→ per-stock company memory
→ state-change / confluence detection
→ deep-analysis escalation when material
→ Quality / dependency / timers / TTC
```

The persistent object is the **company/security memory**, not a local archive of every raw filing body.

Raw filing text/XML is a transient parsing input unless an explicit audit requires archival preservation.

Every material extracted fact must retain enough provenance to return to the source:
- accession;
- form;
- filing date;
- source URL/accession;
- extraction method;
- structured fact;
- source snippet where heuristic extraction was used.

---

## 1. Forms covered in v1

### Insider
- Form 3 / 3-A
- Form 4 / 4-A
- Form 5 / 5-A
- Form 144

Form 4 non-derivative transactions receive deterministic XML extraction when XML is available.

Open-market purchase code `P` is classified separately from:
- grants;
- option exercises;
- tax-withholding transactions;
- gifts;
- other transaction codes.

An open-market purchase is a **discovery trigger**, not proof of a thesis.

### Form 4 issuer / reporting-owner identity lock

Before interpreting a Form 4, explicitly distinguish:

```text
ISSUER = whose securities changed ownership?
REPORTING OWNER = who filed / acquired / disposed?
XYOOL SUBJECT = which company/security memory are we updating?
```

If the Xyool subject is the **reporting owner buying another issuer**, do **not** classify the transaction as an insider purchase of the Xyool subject.

Use strategic-owner facts such as:

```text
STRATEGIC_EQUITY_ACCUMULATION
STRATEGIC_EQUITY_STAGE_COMPLETION
STRATEGIC_EQUITY_DISPOSITION
```

Example learned from VWAV:

```text
VisionWave Holdings = reporting owner
SaverOne / SVRE = issuer
Form 4 code P = VisionWave buying SaverOne securities
```

That is a strategic-ownership discovery signal for VWAV, not “a VWAV insider bought VWAV.”

For ADR/ADS structures, never multiply underlying ordinary-share counts by an ADS price without checking the footnotes and current depositary ratio. Prefer the economic ADS units/price disclosed in the filing.

### Corporate events
- 8-K / 8-K-A
- 6-K

### Operating
- 10-Q / 10-Q-A
- 10-K / 10-K-A
- 20-F / 20-F-A

### Financing / shareholder capture
- S-1 / S-1-A
- S-3 / S-3-A
- 424B3
- 424B5

### Ownership
- Schedule 13D / 13D-A
- Schedule 13G / 13G-A
- 13F-HR

### Risk / filing status
- NT 10-Q
- NT 10-K
- Form 25

Coverage can expand without changing the company-memory contract.

---

## 2. Storage rule

Do **not** create one permanent Xyool memory object per filing.

Use:

```text
RAW FILING
→ EXTRACT MATERIAL FACTS
→ APPEND EVIDENCE LEDGER
→ UPDATE COMPACT FILING-MEMORY HEAD
```

Per-stock storage remains:

```text
entities/<entity>.json
evidence/<entity>.jsonl
timers/<entity>.jsonl
analyses/<entity>/...
```

The SEC layer writes primarily to:
- append-only evidence;
- `filing_memory` in the entity snapshot;
- `source_cursors.SEC_EDGAR`;
- discovery fields in `current_state`.

A filing ingestion must not rewrite old evidence bytes.

---

## 3. Compact filing-memory head

Suggested structure:

```text
filing_memory
  schema_version
  recent_filings[]
  latest_by_family{}
  signal_heads{}
  confluence_state
  confluence{}
  deep_analysis_required
  deep_analysis_trigger_reasons[]
  latest_accession
  latest_form
  last_ingested_at
```

The ledger is historical truth.

The snapshot is only the current head.

---

## 4. Discovery signals

V1 recognizes these positive discovery classes:

```text
INSIDER_OPEN_MARKET_PURCHASE
DEFINITIVE_AGREEMENT
CUSTOMER_EVALUATION
CUSTOMER_QUALIFICATION
CONTRACT_VEHICLE_ACCESS
FUNDED_ORDER
REPEAT_ROLLOUT
CAPACITY_ACTIVATION
STRATEGIC_OWNER_INTENT
STRATEGIC_EQUITY_ACCUMULATION
STRATEGIC_EQUITY_STAGE_COMPLETION
TRANSACTION_CONDITION_PRECEDENT
```

Capture/risk classes include:

```text
INSIDER_OPEN_MARKET_SALE
FINANCING_CAPACITY
GOING_CONCERN
DELISTING_RISK
LATE_FILING
```

These classes determine **research visibility and escalation**, not capital authority.

---

## 5. Extraction authority

### Deterministic extraction

Use deterministic parsing where the filing format supports it.

V1:
- Form 4 XML non-derivative transactions.

A deterministic parser may create high-confidence evidence when the source fields are explicit.

### Heuristic text extraction

Generic filing text may be scanned for causal language such as:
- definitive agreement;
- testing / pilot / evaluation;
- qualification;
- purchase / production / follow-on order;
- second site / repeat rollout;
- commercial production / ready for service;
- ATM / shelf / convertibles / warrants;
- going concern;
- Schedule 13D purpose language;
- listing risk.

Heuristic text matches are:

```text
HEURISTIC_REVIEW_REQUIRED
```

### Contract-award extraction lock

Contract language must fail closed before it enters company memory.

```text
GENERIC CONTRACT AWARD
!=
FUNDED ORDER
```

Required distinctions:

- IDIQ / multiple-award / framework / master agreement / BPA language -> `CONTRACT_VEHICLE_ACCESS` unless a separate funded component is explicit;
- an affirmative received / issued / secured / awarded purchase, production, follow-on, task, or delivery order, or explicit obligated/funded language -> `FUNDED_ORDER`;
- generic `contract award` / `awarded a contract` with no reliable obligation detail -> `CONTRACT_AWARD_REVIEW`;
- future purchase orders, future task orders, eligibility to compete, ceilings, frameworks, or option periods must **not** auto-promote to `FUNDED_ORDER`;
- when vehicle access and an actual order coexist in the same filing, preserve both facts separately.

`CONTRACT_AWARD_REVIEW` and `CONTRACT_VEHICLE_ACCESS` must trigger deep-analysis review when newly ingested. They still have no independent Quality, TTC, or capital authority.

This extraction lock is the intake implementation of the canonical Contract Economic Ladder:

```text
ACCESS / VEHICLE
-> COMPANY-SPECIFIC FUNDED ORDER
-> DELIVERY / BACKLOG
-> REVENUE
-> PROFIT / CASH
```


They may:
- keep a stock visible;
- create a research question;
- trigger a deep analysis.

They may not by themselves:
- promote Quality;
- promote PFS/FES;
- activate a high-confidence timer;
- prove funded economics;
- authorize capital.

---

## 6. Discovery lane update

SEC memory can update:

```text
ESTABLISHED_QUALITY
INSIDER_ORIGIN
HIDDEN_TRANSITION
STRATEGIC_OWNER
BOTH
RISK_ONLY
WATCHING
```

Examples:

```text
Q1 + Form 4 P purchase
→ INSIDER_ORIGIN
→ DISCOVERY_VISIBLE
→ capital still BLOCKED / pending Quality

Q1 + customer qualification breadcrumb
→ HIDDEN_TRANSITION
→ DISCOVERY_VISIBLE

Q4 + funded-order breadcrumb
→ BOTH

S-3 / ATM only
→ RISK_ONLY
→ VISIBLE_RISK
```

Canonical rule:

> **SEC evidence can make a stock visible. It cannot make a blocked stock eligible for normal capital.**

---

## 6A. Recursive character propagation

A company-memory update can matter to another public security when the issuer is a material character in that security's story.

Example:

```text
SAVERONE NEW 6-K / F-3
→ SAVERONE COMPANY MEMORY DELTA
→ VWAV CHARACTER POINTER
→ TEST MATERIALITY TO VWAV
→ UPDATE VWAV NARRATIVE / CAPTURE / TIMERS IF MATERIAL
```

Do not duplicate the underlying filing as if VWAV filed it.

Preserve the source issuer and provenance, then propagate only the relevant consequence through the evidence-backed relationship.

Rule:

> **A material character's filing is part of the parent's story when the filing changes a state that can economically or causally reach the parent.**

This is mandatory for current story-building, not an optional research sidecar.

## 7. Cross-filing confluence

Do not treat filings independently once they belong to the same company memory.

Current categorical states:

```text
NONE
SINGLE_SIGNAL
INSIDER_PLUS_TRANSITION
MULTI_SOURCE_CONFLUENCE
TRANSITION_WITH_CAPTURE_RISK
RISK_ONLY
```

Examples:

```text
FORM 4 OPEN-MARKET PURCHASE
+
8-K DEFINITIVE AGREEMENT
→ INSIDER_PLUS_TRANSITION
```

```text
10-Q CUSTOMER QUALIFICATION
+
S-3 ATM / WARRANT CAPACITY
→ TRANSITION_WITH_CAPTURE_RISK
```

No numeric confluence score is promoted.

Confluence is a research-priority state only.

---

## 8. Deep-analysis escalation

Routine SEC ingestion should stay compact.

Escalate to a native deep analysis when new evidence includes:
- hidden causal transition;
- open-market insider purchase;
- strategic-owner intent;
- positive transition intersecting financing/shareholder-capture risk;
- another material state change requiring dependency/Quality/TTC recomputation.

Set:

```text
filing_memory.deep_analysis_required = true
```

and record reasons.

The flag remains pending until a downstream deep analysis explicitly clears/replaces it.

The deep analysis then uses the existing lossless memory process:

```text
stock_analysis_memory_plan
→ ingest
→ audit
```

---

## 9. New-stock auto-cataloging

A previously unknown stock may enter Xyool from an SEC discovery event.

Example:

```text
Form 4 P purchase
→ resolve ticker/CIK/security
→ create L1 discovery entity
→ append Form 4 evidence
→ INSIDER_ORIGIN
→ Quality = UNASSESSED
→ capital = BLOCKED_PENDING_QUALITY
→ deep analysis required
```

This is intentional.

A stock does not need to pass Quality before Xyool is allowed to remember it.

---

## 10. SEC cursor / delta rule

For each cataloged stock persist:

```text
source_cursors.SEC_EDGAR
  CIK
  latest_accession_processed
  latest_filing_date_processed
  forms_of_interest
  last_checked_at
  status
```

On the next scan:
1. read the cursor;
2. request recent SEC submissions;
3. stop when the stored accession is reached;
4. process only newer forms of interest;
5. ingest oldest-to-newest.

Do not refetch/reprocess the full filing history on every scan.

### Historical/backfill rule

A historical filing can be ingested after newer evidence already exists.

When that happens:

- append the historical normalized evidence;
- record it as historical/backfill ingestion in `filing_memory`;
- do **not** move `source_cursors.SEC_EDGAR` backward;
- do **not** overwrite a newer `latest_sec_accession` index head;
- do not relabel the old filing as the company's latest current filing.

Freshness authority and historical evidence completeness are separate concerns.

---

## 11. Current implementation

Code:
- `agent/sec_edgar.py`
- `agent/sec_filing_intake.py`
- `agent/sec_company_memory.py`

Runtime tools:
- `sec_company_memory_plan`
- `sec_company_memory_ingest`
- `sec_company_memory_get`

CLI:
- `scripts/ingest_sec_company_memory.py`

The EDGAR client requires a descriptive user agent supplied by the operator.

---

## 12. Capital-authority boundary

Authority remains:

```text
SEC RADAR / COMPANY MEMORY
→ discovery visibility + evidence

QUALITY
→ normal capital eligibility

TTC
→ capital priority / desired exposure

QUANT
→ downstream expression
```

Form 4 buying does not override dilution.

An 8-K agreement does not prove closing.

A 13D does not prove a transaction.

A shelf does not prove issuance.

A filing event is evidence. Xyool must still trace the causal and shareholder-capture path.

---

## Core rule

> **Remember the company, not the paperwork. Preserve source provenance, append the evidence, update only the state that actually changed, and escalate material changes into the existing Xyool decision stack.**
