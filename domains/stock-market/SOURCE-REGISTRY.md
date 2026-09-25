# Xyool Stock Market — Source Registry

Status: **ACTIVE SUPPORTING REGISTRY / DISCOVERY + PROVENANCE**

As of: **2026-09-24**

Governing source-authority Flow:
- `flows/story-sourcing.flow.md`

Operational feed catalog:
- `sources/rss.yaml`

## Purpose

Maintain a durable catalog of high-quality stock-market source surfaces without turning feed availability into evidence authority.

This registry supports discovery, freshness, delta fetching, source cursors, and provenance. It does **not** replace claim-specific source selection in Stock Story Sourcing.

Core rule:

> **RSS detects change. The strongest claim-specific evidence determines state.**

## RSS / feed boundary

Default path:

```text
RSS / ATOM ITEM
→ IDENTIFY CHARACTER / SECURITY / RELATIONSHIP / EVENT
→ DEDUPLICATE AGAINST SOURCE CURSOR + EVIDENCE
→ RESOLVE THE CANONICAL LINKED RECORD
→ CLASSIFY CLAIM TYPE + SOURCE AUTHORITY
→ CHECK COUNTERPARTY / SECOND-SIDE EVIDENCE WHEN MATERIAL
→ APPEND EVIDENCE
→ INVALIDATE / REFRESH AFFECTED STORY BRANCHES
→ RECOMPUTE ONLY AFFECTED DERIVED STATE
```

A feed item may itself come from an authoritative publisher, but material state should still preserve the underlying record or canonical linked page when practical.

Examples:
- SEC filing feed → preserve accession / filing record.
- FDA MedWatch feed → preserve the FDA safety alert.
- Nasdaq halt feed → preserve halt/resumption fields.
- GlobeNewswire item → treat as issuer-originated distribution; resolve issuer filing/IR/counterparty evidence before it closes a material state.

## Source classes

The registry uses the same claim-specific hierarchy as `story-sourcing.flow.md`:

```text
TIER_A
state-creating / authoritative primary evidence

TIER_B
direct first-party / counterparty evidence

TIER_C
high-quality independent secondary evidence

TIER_D
discovery / weak context
```

The tier applies to the claim the source directly supports. It is not a universal rating of the publisher.

## Feed roles

```text
AUTHORITATIVE_SIGNAL
Publisher directly records or controls the event/state.

PRIMARY_DISCOVERY
Direct first-party or agency disclosure useful for early detection.

ISSUER_DISTRIBUTION
Company-originated release distributed by a wire service.
Not independent corroboration.

SECONDARY_DISCOVERY
Credible reporting/context that should route to stronger evidence.

DYNAMIC_FEED
Feed endpoint must be generated from issuer/form/search parameters.
```

## Required source record fields

```yaml
source_id:
provider:
source_tier:
feed_role:
feed_format:
feed_url:
landing_url:
status:
priority:
claim_scope:
entity_mapping:
confirmation_rule:
poll_floor_seconds:
verified_on:
limitations:
```

Do not invent a poll rate where the publisher has not stated one.

## Current collection order

1. Regulators / primary filings.
2. Exchanges / market-state notices.
3. Government agencies that create regulatory, procurement, grant, safety, or program state.
4. Per-company investor-relations feeds for tracked entities.
5. Issuer-distribution wires for breadth and early discovery.
6. High-quality independent secondary feeds for discovery/corroboration gaps.
7. Aggregators/social only when they generate a material question that stronger sources can test.

## Initial RSS families

The machine-readable first batch is in `sources/rss.yaml`.

It begins with:
- SEC / EDGAR;
- Nasdaq trade halts;
- FDA MedWatch;
- DOJ Antitrust;
- FTC competition feed discovery;
- Grants.gov;
- NIH funding opportunities;
- NASA news releases;
- GlobeNewswire event-specific issuer-distribution feeds.

## Company IR feed policy

Per-company investor-relations RSS/Atom feeds should be discovered and stored against the canonical company/CIK entity rather than added as anonymous global feeds.

Preferred mapping:

```text
ISSUER ID / CIK
→ official IR domain
→ newsroom / filing / event RSS or Atom endpoint
→ source cursor
→ character-local freshness
```

Do not treat a third-party mirror as the issuer's official feed.

## Dedupe / identity

Preferred dedupe keys, in order:

```text
native stable event ID / accession / notice ID
→ canonical item URL
→ feed GUID
→ normalized provider + title + published_at hash
```

Entity resolution should prefer stable identifiers (CIK, exchange symbol + venue, agency notice IDs) before fuzzy company-name matching.

## Failure handling

A source-monitoring miss includes:
- a high-priority feed existed but was not registered;
- a registered feed changed/broke and the failure was silent;
- a feed item could not map to a material tracked character;
- duplicate items created duplicate evidence/state transitions;
- issuer-distribution copy was mistaken for independent corroboration;
- a feed item triggered state promotion without resolving stronger available evidence;
- the cursor advanced before the item/evidence was durably recorded.

Feed failures should be auditable inputs to the normal miss/learning path.

## Software boundary

Feed polling, XML parsing, conditional GET, dedupe, cursor persistence, retry/backoff, schema validation, and high-volume entity matching are valid candidates for deterministic software **after** the source contract is stable.

Source authority, materiality, claim interpretation, relationship meaning, and state promotion remain Floware reasoning responsibilities.
