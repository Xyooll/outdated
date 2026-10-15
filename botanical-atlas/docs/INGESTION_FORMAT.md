# Automatic Research Batch Format

Place a source-attributed JSON file at `botanical-atlas/incoming/<batch_id>.json` (safe slug, minimum six characters). It is immediately eligible for automated integration, **not** a manual draft-review queue.

Required root keys: `batch_id`, `research_date` (YYYY-MM-DD), `research_reference_url` (HTTPS); plus at least one collection of records. Allowed arrays: `organisms`, `compounds`, `occurrences`, `domain_notes`, `safety`, `cultural_uses`, `sources`, `structures`, `binding`.

Example:
```json
{
  "batch_id": "20261014_global_001",
  "research_date": "2026-10-14",
  "research_reference_url": "https://powo.science.kew.org/",
  "sources": [{"id": "SRC-example-001", "title": "Botanical reference", "organization": "Kew", "url": "https://powo.science.kew.org/"}],
  "organisms": [{"id": "BOT-EXAMPLE", "scientific_name": "Example species", "common_name": "Example only"}],
  "cultural_uses": [{"id": "CUL-EXAMPLE", "organism_id": "BOT-EXAMPLE", "region": "Example", "tradition": "Example only", "part": "Example", "preparation": "Descriptive only", "reported_use": "Example — not an actual medical claim", "claim_kind": "historical_use", "source_id": "SRC-example-001", "verification": "example_only", "limitations": "Not evidence of clinical efficacy"}]
}
```

Each new chemistry occurrence requires `organism_id`, `compound_id`, `source_id`, and `verification` fields. A cultural use requires named region/tradition, plant part/preparation, source, context, limitations and verification. Source URLs must be actual HTTPS links and source metadata must be attributable. A 2D structure must be tied to a specific molecule and source; no invented single structure for a family, extract or mixture. Binding claims require a named assay/model, evidence tier and traceable research links. No health claim may claim clinical confirmation solely on traditional-use evidence. Batch filenames are unique; processed batches are preserved.
