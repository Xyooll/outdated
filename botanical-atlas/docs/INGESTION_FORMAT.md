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

## Medicine, dose, folklore and regulatory extensions (v1.2)

New independently source-attributed collections: `practice_claims`, `dose_guidance`, `folklore`, `regulatory_status`. All records use unique IDs, real `organism_id` and `source_id`, with automated validation and no human draft queue.

- **practice_claims:** `id`, `organism_id`, `system` (e.g. modern biomedicine, TCM, Ayurveda, Unani, European herbalism), `tradition`, `region`, `framework[]` (retain native labels such as wind-heat, five phases, rasayana, mizaj), `condition_or_goal`, `claim_type`, `plant_part`, `preparation`, `evidence_tier`, `source_id`, `limitations`; optional route/original_term.
- **dose_guidance:** `id`, `organism_id`, `tradition`, `part`, `preparation`, `route`, `population`, `intended_use`, `amount_text`, `frequency_text`, `evidence_status`, `upper_limit_status`, `contraindications`, `risks`, `source_id`. Separate clinically studied regimens, traditional/pharmacopoeial ranges, and unknown safe dosages. No field may claim universal guaranteed safety.
- **folklore:** `id`, `organism_id`, `tradition`, `region`, `theme`, `description`, `claim_type`, `evidence_tier`, `source_id`, `limitations`, and `public_knowledge:true`, `clinical_claim:false`. Publicly documented beliefs only. Symbolism is not pharmacology.
- **regulatory_status:** `id`, `organism_id`, `jurisdiction`, `regulator`, `category`, `preparation_scope`, `status_text`, `date_checked`, `source_id`, `limitations`.

Treat modern biomedicine as a named perspective without presenting evidence obtained from empirical trials as equivalent to cultural analogy. A tradition's concepts retain their source vocabulary: TCM Wu Xing five phases (Wood/Fire/Earth/Metal/Water), wind-heat patterns, meridians; Ayurveda's dosha model; Unani temperament/humoral vocabulary. Never infer corresponding biochemical pathways without research. “Five treasures” is not a universal unambiguous canonical label; gather original language/source before encoding it. Respect Indigenous/community knowledge rights. For each organism missing any of these layers, show **not yet cataloged**, not zero benefit or zero risk. The hourly publisher automatically merges these collections in source-backed batches; validation failures abort publication atomically.
