# Biological activity audit — initial gap review (October 15, 2026)

## Canonical coverage after first parasitology batch

- 65 organisms: 45 plants, 20 fungi
- 205 named chemical identities, 244 organism–compound occurrence links
- 192 structure records (some incomplete/draft; this is **not** 192 fully validated atom/bond depictions)
- 129 source records
- **8 assay-level bioactivity records**, of which 7 concern isolated eugenol and one concerns **clove essential oil**.
- **1 of 205 compounds** has indexed compound-specific assay activity; **204 unindexed** is a literature/search coverage gap, NOT 204 biologically inert compounds.
- 16 source-attributed medicinal perspective claims; 6 dosage context records; 54 cultural-use records; 2 folklore records; 7 target-binding records. The catalog is not close to comprehensive.

## Missing dimensions, prioritized

1. **Effect × target × evidence grid**: antiparasitic subdivided into protozoa, nematodes, cestodes and trematodes; microbial pathogen species and life stages. Antibacterial, antifungal, antiviral, analgesic, anti-inflammatory, antioxidant/oxidative stress, metabolic, immunomodulatory, cardiovascular, CNS/affective, reproductive, wound/skin, cancer/cytotoxic and adverse/poisoning activity; preserve negative/null results.
2. **Test material attribution**: species identity, organ/part, plant chemotype, extraction solvent/temperature, concentrations and purity; whole herb, essential oil, standardized extract and isolated molecule are distinct.
3. **Real mechanism confidence**: direct assays, protein-target binding vs phenotypic changes vs pathway associations vs unvalidated molecular docking; avoid invented molecular targets.
4. **Pharmacokinetics and relevance**: absorption, oral bioavailability, metabolism, achievable exposure, chemical instability, dose-response curves, host-cell selectivity and clinically studied formulations. In vitro IC50 is NOT a human dose.
5. **Clinical reality**: human trials, comparators, randomization/blinding, effect sizes, contradictory/null outcomes, trial participants/indication, regulatory notices, adverse events, interactions, pregnancy/age/organ impairment. Neither food ingestion nor folkloric use establishes clinical effect.
6. **Coverage, sources and taxonomy**: original six missing source IDs in imported legacy occurrence records, synonym conflicts and authentication, incomplete 2D drawing verification, worldwide cultural systems including TCM wind-heat, Ayurveda, Unani, ethnomycology, spiritual/folklore material attributed ethically.
7. **Interaction/synergy and harms**: combined molecule A+B effects must be independently studied; never infer clinical synergy from overlapping pathways. Include competing effects, metabolism interactions and contamination.
8. **Unattended quality assurance**: source authenticity/dead-link detection, study-to-claim attribution, robust deduplication, units normalization, reproducible automated ingestion, provenance and rollback, recurring schedule health. The downloaded offline app is a snapshot and does not automatically synchronize with GitHub.

## Confirmed index example

- Isolated eugenol vs *Giardia lamblia* trophozoites: cultured-cell growth IC50 101 µg/mL.
- *Syzygium aromaticum* essential oil (mixture), separately tested: cultured Giardia growth IC50 134 µg/mL.
- Isolated eugenol vs *Leishmania mexicana mexicana* promastigotes: in vitro IC50 2.72 µg/mL; lipid droplet alterations associated experimentally, exact protein target uncertain.
- Isolated eugenol vs *Leishmania major* promastigotes and amastigotes: two separate stage-specific results.
- Isolated eugenol vs *Haemonchus contortus* eggs, larvae and adult motility: three separate assays in the veterinary context. Docking to HcPMT is a hypothesis, not direct measured binding.

Primary references are included in the Atlas sources and each `bioactivities` item. **Nothing here proves that eating clove or swallowing clove oil treats parasites.** NIH LiverTox documents serious eugenol/clove oil toxicity from overdoses.

## Implementation next

Continue adding new plants and fungi while simultaneously making activity research a required question for each new compound. The publishing mechanism can store zero-source/null findings distinctly from unsearched targets. Measure **fraction of compound identities with at least one explicitly sourced activity**, and **fraction of organisms with validated parts, compounds, safety, indigenous/cultural context and regulatory status**, rather than treating a growing organism count as proof of database completeness.
