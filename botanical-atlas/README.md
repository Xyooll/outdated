# Botanical & Fungal Identity Atlas (MVP 1.2 · plural medical systems)

A growing source-attributed catalog of plants, fungi, individual bioactive compounds, structural chemistry, cultural/ethnobotanical uses, and four-domain effects (bioenergetic/metabolic, physiological, cognitive, affective).

**Location:** public `Xyooll/outdated`, directory `botanical-atlas/`. The Atlas is independent from other software in this repository. **Never commit private health records, credentials, personal notes or restricted cultural knowledge.**

**Open:** [latest standalone Atlas browser](site/index.html). This is an offline snapshot: downloaded files on your phone **do not** synchronize automatically. Download/refresh the newest copy after repository updates.

## Current catalog status (2026-10-15, revision 7)

The canonical source of truth is [data/atlas.json](data/atlas.json), not fixed numbers in this README.

| Record type | Count |
|---|---:|
| Organism identities | 51 |
| Distinct chemical/family identities | 194 |
| Organism-to-compound occurrence records | 233 |
| Effect-domain notes | 204 |
| Safety records | 59 |
| Cultural-use records | 41 |
| Source records | 75 |
| Chemical structure records / links | 181 |
| Experimentally described target-binding records | 7 |
| Locally stored molecule SVG diagrams | 43 |

**Evidence boundaries:** the original 32 organism identities were imported with incomplete verification. Six original citation IDs remain unresolved. Some structure diagrams are drafts, and some structures have registry links rather than locally rendered diagrams. A traditional-use statement does **not** establish clinical efficacy; docking or structural similarity is **not** proof of binding or synergy.

## Earlier research preserved

The [original 32 long-form organism identity profiles and full report](reference/legacy-2026-10-14/) are now archived in GitHub. Their [20 early cross-organism relationship hypotheses](reference/legacy-2026-10-14/03_compound_links.json) are preserved separately. These are historical working notes, **not** silently upgraded to verified clinical claims and not all exposed yet as a queryable combination graph in the app.

## Automatic publishing — no manual review queue

The ChatGPT hourly researcher can submit source-backed JSON batches directly to `botanical-atlas/incoming/<batch_id>.json` on `main`. The GitHub Actions publisher in `.github/workflows/botanical-atlas-publish.yml` validates data integrity, deduplicates, integrates into [data/atlas.json](data/atlas.json), rebuilds HTML and SQLite, archives each accepted batch in [processed/](processed/), and commits. New source records retain evidence classifications; invalid batches halt without overwriting canonical data. Git history provides rollback.

Seven source-to-publish batches have been incorporated through revision 7. The current unattended schedule is *separate* from GitHub Actions and must remain enabled with connector write access; a successful code workflow does not guarantee future hourly research actually runs. [Batch schema](docs/INGESTION_FORMAT.md).

Local testing: `cd botanical-atlas && python -m unittest discover -s tests -v && python tools/atlas_pipeline.py validate && python tools/atlas_pipeline.py build`.

**Research only:** no self-medication, diagnostic, extraction, foraging or chemical synthesis guidance implied by a catalog entry.

## v1.2 — Medical perspectives, dosage, folklore, regulation

The interactive app now offers a **Medicine & meaning** library. Every organism includes dedicated sections for source-attributed medicinal claims in their own tradition (including biomedicine), preparation/population-specific dosing and risk context, publicly documented folklore/metaphysical interpretation, and country/jurisdiction-specific regulation. Absence of researched records is displayed honestly. Initial examples cover TCM five tastes and wind-heat, modern clinical peppermint and ashwagandha research, an EU ginger monograph, and historical rosemary remembrance. These samples are not comprehensive for all organisms. Additional cultural systems can be added with their native terminology and clear provenance. Do not collapse metaphysical associations into biomedical facts or treat historical doses as universally safe.

All source-backed updates are automatically published through the same GitHub Actions pathway; no human draft queue. The file `data/atlas.json` remains the canonical master and its live count takes precedence over the older snapshot table above.

## Research workbench — version 1.3

A new **Research workbench** button opens three interactive analyses within the single-file offline app: (1) a sortable research coverage dashboard for all organisms, with **six explicitly documentation-based fields**; (2) a two- or three-plant side-by-side comparator with preparation-specific medicinal evidence, doses, risk, cultural uses, folklore and chemical inventory; and (3) a cross-organism shared-constituent explorer with an optional strict non-legacy occurrence source filter. All data are derived from the canonical Atlas JSON in the HTML; there is no speculative receptor docking or implied medicinal synergy. Coverage is a documentation metric, not medical quality or effectiveness. Missing citations are highlighted. Automated tests check the offline bundle, Python data integrity, and Node syntax. No new clinical evidence claims or doses are invented by this feature.

## 2026-10-15: assay-level research added

**Study effects** is now visible in the web app and on plant/compound pages. The first eight assays are seven isolated-eugenol studies and one separately studied clove essential-oil result for Giardia, Leishmania and Haemonchus (in vitro only). No established human antiparasitic regimen follows from these findings. Data are source-linked and target/species/life-stage/IC50/EC50-specific. As of catalog revision 13, only one of the 205 distinct chemical identities has individual bioactivity records; the others are NOT proven inactive, they are simply not yet indexed.

To avoid systematic omissions, scheduled research should cross-query synonyms, mechanism and biological activity classes for each *compound*, not just each plant. Include antiparasitic (antiprotozoal and anthelmintic), antifungal, antibacterial, antiviral, analgesic, anti-inflammatory, immune, neurological, metabolic, cardiovascular, dermatological and toxicology activity with study limitations and null/negative evidence. See [coverage gap review](docs/BIOACTIVITY_COVERAGE_GAPS.md).
