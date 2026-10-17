# Atlas v1.7 — Nested multidimensional profile product contract
Status: **approved product direction / implementation roadmap**, not a claim the features below are deployed.
Source of truth: `botanical-atlas/data/atlas.json` for existing records; `docs/PRODUCT_VISION_CONTRACT.json` for the required product architecture.
Last scoped: 2026-10-17.

## Identity architecture
A botanical or fungal organism has **one verified taxonomic identity hub** with many fully developed, independent profiles. Each top-level category may contain nested tradition-, school-, method- or source-specific subprofiles. **Never replace these with one flattened benefits list.**

```text
Organism identity (taxonomy; synonyms; part; region; lifecycle; citations)
  ├── Medicinal profiles
  │   ├── TCM → native energetics / meridians / diagnostic patterns / historical uses
  │   ├── Ayurveda → rasa / guna / virya / vipaka / dosha / contextual uses
  │   ├── Unani, Siddha, Tibetan, Kampo, regional and named community systems
  │   └── Western biomedicine → preparation-specific experiments and clinical outcomes
  ├── Metaphysical profiles
  │   └── Named tradition/community → symbolism, elements, correspondences,
  │       ritual history, belief-based energetic/emotional interpretations
  ├── Active ingredients / chemistry
  │   └── Compound → occurrence in part/batch → identity/structure →
  │       mechanism or measured bioactivity with source and study limitations
  ├── Preparation and extraction profiles
  │   └── Method → input part/material → output preparation or fraction →
  │       method-specific composition/yield/purity evidence and precautions
  └── Visual library
      └── Organism/parts → medicinal/metaphysical contexts →
          compound diagrams → preparation/extraction illustrations
```

**Relationship rules:** A plant, clove essential oil, aqueous infusion, methanolic extract, and pure eugenol are different materials. A study of isolated eugenol cannot be automatically inherited by clove as human-treatment evidence. A method can produce multiple outputs, and an output can have different constituent composition depending on source material and conditions. Formula interactions are separate from single-material claims. Preserve the existing v1.6 material/formula/interaction records.

## Profile-specific schemas (planned extension, backward-compatible)
- **Identity:** stable organism ID, accepted taxon, synonyms, source, plant/fungal part, region, botanical photo IDs; distinguish authenticated vs uncertain species and lookalikes.
- **Medicinal subprofile:** system ID, named school/community/region/time period, original term + translation, its own conceptual axes, patterns/indications, preparations and material IDs, cautions, contradictions, sources. Biomedical studies have distinct endpoints, populations and evidence tiers.
- **Metaphysical subprofile:** specific tradition (not generic "African" or "Indigenous"), context/time/place, elements/planetary or ritual correspondences **only when applicable**, interpretations, public-knowledge/permissions status, origin and interpretive sources; explicitly label belief/tradition rather than scientific efficacy. Restrict sacred/nonpublic materials.
- **Active ingredient:** exact chemical entity vs family vs mixture, names/identifiers, verified structure, organism/part occurrence and measured concentration with assay and units, tested effects including null findings, biological target/model and adverse effects.
- **Extraction/preparation:** input material/part, method family (e.g., decoction, steam distillation, solvent extraction), technique description, solvent/media category if documented, output material/fraction, measured yield/purity/composition with method/units, traceable source, reproducibility limitations, hazards. Safety-sensitive details may be summarized without risky procedural instructions. Neither historical recipe nor solvent recovery is an established safe personal use.
- **Media:** ID, subject/reference ID (organism, part, compound, profile, method or output), kind (photo, botanical plate, chemical diagram, lab photo, historical artifact, illustration), caption, creator, original URL, license/permission, alt text, verification status, culture/tradition attribution, image type and optional date/location. Never imply an illustration proves the depicted traditional claim.

Use normalized IDs and typed links so a category can have many subprofiles without duplicating the organism. Preserve source disagreements; do not infer correspondence across epistemologies or chemical equivalents from energetic terminology.

## MVP implementation roadmap — *planned*, not yet delivered
1. **Foundation and migration:** add optional versioned `profile_categories`, `profiles`, `profile_sources` and typed cross-links; index existing v1.6 practice claims, folklore, chemistry, materials and formulas non-destructively. Keep old app and research batches readable.
2. **Profile browser:** one organism hub with independent expandable Medicinal, Metaphysical, Active Ingredients, Extraction & Preparation, and Pictures categories. Inside categories, support named subprofiles and visible "not yet researched" states.
3. **Source and evidence cards:** original-language terms and cultural context; separate traditional, metaphysical, in-vitro, animal, human, hypothetical and null-result evidence. Source disagreements and safety warnings visible in context.
4. **Compound-to-extraction links:** connect method/output to part and measured compound occurrence; show where yields/concentrations are unknown. Never infer that an extracted material has a compound's activity or a safe dosage.
5. **Picture galleries:** at least one licensable, source-attributed botanical or fungal image for a representative acceptance organism, correctly labeled chemical diagram and credited preparation image where available; accessible captions, licenses and broken-image fallback. No invented media coverage.
6. **Acceptance walkthrough:** Clove → TCM Ding Xiang and its sourced variations; metaphysical category with distinct tradition subprofiles (or explicit research gaps); eugenol identity/assays; clove bud vs oil/extract distinctions; method-to-material links; attributed images. Include a second fungus acceptance organism to reveal plant-only assumptions.
7. **Build/QA:** data validation, mobile/offline rendering, browse/search/links, performance, regression tests, coverage dashboard. Publish only after checks. No fabricated "all organisms have deep profiles" assertions.

## Full-product stages
- **P1 ontology + migration:** multilingual taxonomy, materials, tradition/community/school nesting, profile versions, media rights registry, provenance/translation history, consent and licensing.
- **P2 deep coverage:** independent profiles by organism × tradition × school × part × source; record conflicting evidence, documented absences and unknowns. No arbitrary completion quota that invents source material.
- **P3 chemistry/extraction depth:** validated constituent inventories, batch variability, measured assay conditions, extraction outputs, quantitative purity/yields when reported, harmful outcomes, null trials, formula-level and drug-interaction boundaries.
- **P4 visual intelligence:** licensed image library of organisms, organs/parts, lookalikes, microscopy, historic texts/artifacts, diagrams, and extraction equipment; accessibility, attribution, image verification and takedown workflow.
- **P5 knowledge graph:** cross-profile comparisons with source-specific explanations, exact relationships and disagreements; never force spiritual concepts into physiology.
- **P6 production quality:** incremental research ingestion; automated QA, human-review exceptions for cultural permission/ambiguous dangerous findings, secure edit history and rollback, offline-first mobile UI, reliable sync only when provisioned, translated terms, evidence drilldown, observability and search quality.
- **P7 ongoing verification:** independent audits of accuracy, citations, taxonomic revisions, image rights, clinical claim downgrades, coverage gaps, accessibility and user feedback.

## Release acceptance and quality bar
An MVP release **passes** when a new organism can be linked to zero or many independent named subprofiles without schema duplication; the prototype clove pathway works end to end; citations and media rights are visible; missing data remain visibly missing; legacy v1.6 entries and the automatic ingestion pipeline remain usable; tests and a mobile/offline smoke test are recorded. A comprehensive full product additionally requires systematic coverage, updated source verification, robust image provenance, negative evidence, conflict handling, community permission rules and audit/rollback.

**Scope freeze:** these five profile families and their nested structure are the approved north star. More categories are allowed through additive versioned extensions, never by deleting a category, collapsing subprofiles, replacing traditional terms with biomedical assertions, or adding fabricated evidence.
