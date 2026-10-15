# Botanical Identity Atlas — MVP + full-build strategy

## Delivered MVP v1.2

Searchable offline application, 2D compound diagrams where authenticated, source-linked organisms, chemical occurrences, global cultural uses, separate systems of medicine, preparation-aware dosage and safety, folklore/metaphysical beliefs, regulator entries, four effect domains, notes, JSON/SQLite exports and unattended GitHub publishing. Every research update must retain stable IDs, provenance, revision and rollback in Git; schema and evidence gates are automated, with **no manual drafts-for-review step**.

## Full-build stages

1. **Coverage:** systematic profiles for every existing organism across clinically studied actions, cross-border historical uses, native theoretical categories and publicly sourced folklore. Track missing coverage openly. Include traditional practice identity, part, formulation and region.
2. **Clinical & safety depth:** trial outcome and effect size, human adverse event signals, contraindications, interactions, age, pregnancy/lactation, duration, contamination risks, preparation-specific monographs, dose ranges and no-safe-dose-known flags. Never infer personal safety from ranges.
3. **Molecular intelligence:** source-verified structures and stereochemistry, binding assay vs docking annotations, absorption/metabolism, mechanistic evidence grades, interaction/conflict graph; no inferred miracle compounds.
4. **Interoperability:** reusable controlled vocabularies (medical systems and original-language constructs), source provenance snapshots, diff browsing, native multilingual search, citations, ethical Indigenous knowledge permissions, region-specific regulation.
5. **Delivery & reliability:** optional authenticated hosted frontend and offline cache updates, schema migrations, tests, accessibility and performance budgets, source-link monitoring, hourly job health metrics and recovery notifications. The public outdated repository does not protect confidential data. Avoid private notes in public commits.

## Release acceptance gates

- UI actually displays each collection on desktop and mobile; no blank or overlapping panels.
- Source/reference and taxonomy integrity automated; unsafe or uncited claims rejected atomically.
- Human/animal/in-vitro/traditional/folklore distinctions remain visible everywhere.
- A measured dose is tied to product, part, preparation, route, population, indication, duration and source; absent data is plainly marked.
- CI builds searchable HTML and SQLite, and archived processed batches demonstrate repeated unattended updates.
- An offline downloaded copy requires refreshing to receive newly published records unless a separate sync client exists.
