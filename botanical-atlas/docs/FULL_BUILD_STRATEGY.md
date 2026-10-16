# Botanical Identity Atlas: MVP plus Full-Product Development Strategy (medical systems overhaul)
Date: 2026-10-16 | Scope: Xyooll/outdated/botanical-atlas

## Product invariant
Each plant/fungus is ONE taxonomically controlled organism identity connected to MANY source-specific traditional/biomedical perspectives. A single species can have multiple region-, school-, text-, part-, extraction- and historically contingent medicinal claims. Cross-system labels are searchable but NEVER assigned scientific equivalence automatically. Research captures both medicinal, ritual/folklore and experimentally observed results with separate evidence labels.

## MVP v1.5 deliverables — built
- Canonical `medical_systems` vocabulary registry with 10 frameworks and provenance URL: TCM, Ayurveda, Siddha, Unani/Tibb, Persian/Islamic medicine, African regional medicine, publicly shared Indigenous accounts, European herbals, Western biomedicine, Himalayan/Tibetan. These are adaptable framework *templates*, not claims of completeness or homogeneity.
- Native conceptual axes per tradition. TCM: warm/cold nature, acrid/sweet/etc. flavors, Spleen/Stomach/Lung/Kidney and other channels, five phases only where a source actually gives an attribution, pattern indications, actions, contraindications and textual disagreements. Ayurveda: rasa/guna/virya/vipaka/dosha/prabhava/dhatu. Unani: mizaj/akhlat/afaal/darajat. All name their own source-specific vocabulary.
- New `Medical systems` tab listing native concepts and linked sourced claims, alongside `Medicinal claims`. Individual claims may contain `framework_details` using the system's own keys; user sees them within the claim card, with warnings when a study or a framework is not biomedical evidence.
- Automated publisher accepts new systems and deep profiles. Deep profiles must include medical-system ID, original-language term, cited source, multi-attribute native concepts, indication, exact part/preparation, evidence level and limitations. Existing shallow claims stay labeled; do not invent detailed attributes.
- Ding Xiang (丁香, Caryophylli Flos) from the Chinese Pharmacopoeia is the first end-to-end acceptance example; verify the next batch's actual Actions publication before claiming complete.

## Full-product development stages
### F1 — Global materia medica ontology and multilingual references
Normalize organism synonyms across taxonomic authorities, local names and part-used identities. Version a medical-system registry by tradition, school, region, terminology standard, original language/script, transliteration, translated definition, doctrinal concepts and permission status. Represent unique sources (including contradictory schools) and precise page/monograph evidence with structured provenance and stable citations. **Do not** encode one worldview as normative for all.

### F2 — Deep medicinal-system profiles for all appropriate taxa
For each documented organism × tradition × source, independently research original name and identity, nature/energetics, flavor, constitution/tissue affinities, diagnostic pattern, therapeutic actions, ritual/folklore distinctions, indications, preparation, part, route, co-formulation and substitutions, contraindications, duration/amount where actually specified, interactions, clinical-evidence contrast and uncertainties. DO NOT invent a correspondence for a label such as “five treasures” without a source. Build completeness dashboards separately for each *system*, not a universal checklist which unfairly penalizes different traditions. Require named community permission for nonpublic Indigenous material.

### F3 — Clinical/biological evidence and safety graph
Join exact plant part/preparation to chemical occurrence with analytical method and amount, pure-molecule structure to human/animal/cell/antiparasitic experiments (and null results), target species and life stage, dose-response, PK/PD and selectivity, adverse events and case reports. Western biomedical clinical trial evidence has its own distinct method/endpoint metadata. For traditional amounts: “monograph reference” ≠ universally safe dose. Flag pregnancy, liver/renal toxicity, age, anticoagulants, fungal contamination, poisonous lookalikes and source disagreements. Organism-level causality cannot be deduced from isolated-compound activity.

### F4 — Formula, compatibility and cross-tradition comparison
Separate organism, medicinal material, formulation, extraction process, ratio, route, coadministered drugs, documented historical incompatibilities, and studied modern interactions. Keep folklore/metaphysical meaning and Wu Xing framework as belief systems with original context; never claim empirical proof from analogy. Compare traditions through source-constrained translation, not false equivalence (“Kidney Yang” is not renal physiology).

### F5 — Product and quality
Offline searchable responsive app, hosted updating version, filters by system/pattern/evidence/region/parts, side-by-side dossier, original-language support, citation drilldown, audit history/rollback, saved local notes kept private, batch provenance, automatic CI prepublication checks, negative study finding capture, link rot monitor, localization and accessibility audits. No user health records/secret cultural knowledge stored in public GitHub.

## Coverage metrics
- Taxa count + fungi ratio (discovery progress only)
- For each tradition: % eligible taxa with ≥1 sourced claim, % claims with original script and source, % with native framework attributes, % with contraindication and preparation details, % conflicting perspectives noted.
- For each compound: verified molecular identity, occurrence by species/part, method-specific bioactivity assays, preclinical vs human evidence, harms/negative findings.
- For each historically sourced dose: presence of product, route, age group, condition, unit, source and clear non-prescriptive label.
- Data QA: invalid refs = 0, false human treatment claims = 0, no forbidden automatic review queue, reproducible CI/website build, searchable app passes mobile acceptance.

## Current limitation and next release gates
MVP is not a completed global pharmacopeia. 65 organisms and 32 medicinal-claim records existed at baseline; most organism/tradition pairs still have no deep profile. Prioritize coverage without fabricating native theory assignments. The preexisting HTML downloaded to a phone remains an offline snapshot; use hosted page for current versions. A passing Python/JS CI does not prove physical Android UI tests have run.

### Completed v1.6 foundations (first milestone)
- Typed medicinal-material identities with organism, part, preparation and processing; prohibit one herb species from silently standing in for essential oil, rhizome, tincture or isolated molecule.
- Explicit multi-ingredient formula and ingredient tables with source references and required ≥2 authenticated ingredients, plus typed pairwise interaction evidence that distinguishes hypothesized bioavailability effects from demonstrated clinical efficacy.
- New responsive offline application tabs 'Medicinal materials' and 'Formulas & interactions'; links back to plant dossiers, original sources and each ingredient; search across formula constituents.
- Validation and regression tests block malformed ingredients, missing sources, unsupported clinical or synergistic assertions, and universally safe-dose implications.
- Verified first formula example intended: Trikatu (dried ginger rhizome, black pepper fruit, long pepper fruit), linked to the 1992 Journal of Ethnopharmacology review; source-backed historical composition is NOT proof of efficacy, and its hypothesized bioavailability effects cannot substitute for pharmacokinetic clinical trials. Actual publication must be confirmed separately.

Still incomplete: full global formula corpus, genuinely measured herbal combination interactions, batch-specific processing quantities, source-verification automation, original-language licensing and community permissions, user accessibility/mobile interaction tests, clinically validated safety and effectiveness.
