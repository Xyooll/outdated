# Botanical & Fungal Identity Atlas (MVP)

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
