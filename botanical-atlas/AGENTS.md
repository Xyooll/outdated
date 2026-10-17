# Botanical Atlas development agent guardrails

Before any Atlas change, read `docs/PRODUCT_VISION_CONTRACT.json`, `docs/PROFILE_ARCHITECTURE_VISION.md`, `docs/FULL_BUILD_STRATEGY.md`, and `docs/INGESTION_FORMAT.md`.

**Non-negotiable:** one organism identity → independent nested Medicinal, Metaphysical, Active Ingredients, Extraction/Preparation and Visual Library profile families. Tradition-specific subprofiles retain native concepts, original names, provenance and contradictions. Never reduce these into a single generic benefits card or frame a spiritual belief as clinical proof.

**Carry forward:** v1.6 medical systems, part-specific medicinal materials, formulas, bioactivity assays, safety, folklore, incoming-batch ingestion, offline app and citation source IDs. Any refactor must migrate them losslessly or provide a documented, tested compatibility layer. Preserve the user-directed automatic publishing workflow (no manual review queue for routine valid public data); block unauthorized sacred/community content and high-risk misinformation.

**Before proposing to merge, supply a change trace:**
1. Which vision-contract invariants and nested profiles does the change advance?
2. Which existing functions and data may regress, and what compatibility/migration tests cover them?
3. Which new claims/images have exact sources, usage rights, uncertainty and safety labels?
4. Which cases were verified in CI and mobile/offline app? Do not call planned features "shipped".
5. Which gaps remain and what evidence would close them?

**Release rules:** run `python -m unittest discover -s tests -v`, `python tools/atlas_pipeline.py validate` and `python tools/atlas_pipeline.py build` from `botanical-atlas/`; preserve the existing GitHub publisher. Review the clove/Ding Xiang/eugenol example and a fungus before calling a nested-profile milestone complete. A syntactically valid page or passing static test is not a real Android usability test.

**Drift tripwires:** reject removal/renaming of the five profile families or this contract without an explicit documented vision change; reject unsourced clinical claims, invented tradition mappings, unsupported extraction outcomes, unauthorized images, unlicensed use or false completion statements. If new concepts do not fit, extend the schema rather than silently rewriting these principles.
