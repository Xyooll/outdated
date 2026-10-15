# Botanical & Fungal Identity Atlas (MVP)

A growing source-attributed catalog of plants, fungi, individual bioactive compounds, structural chemistry, cultural/ethnobotanical uses, and four-domain effects (bioenergetic/metabolic, physiological, cognitive, and affective).

**Repository:** public `Xyooll/outdated`, directory `botanical-atlas/`. The scientific Atlas is independent from the other software in this repository. **Do not commit personal health records, private notes, credentials, or restricted cultural knowledge.**

**Open:** [standalone offline Atlas](site/index.html). This is a snapshot. Downloaded HTML files do **not** synchronize automatically; fetch the latest repository copy to see updates.

**Baseline:** 32 organisms, 168 compound/family identities, 205 occurrences, 22 sourced cultural use entries, 43 offline 2D chemical drawings. Most inherited chemistry claims still require stronger citation verification. Drawings labeled draft must not be treated as structurally confirmed, and structural similarity is not binding proof.

## Auto updates (no human approval)

The hourly researcher can commit one structured and source-cited batch to `botanical-atlas/incoming/<batch_id>.json` on `main`. The repository-root workflow `.github/workflows/botanical-atlas-publish.yml` automatically tests and integrates source-checked batches, deduplicates identities, rebuilds HTML and SQLite, archives accepted batches, then commits. Invalid batches fail and do not overwrite canonical entries. Git history provides rollback.

Use [batch specification](docs/INGESTION_FORMAT.md) for new records and check GitHub **Actions** for each verified publish. A successful workflow does not independently prove medical efficacy or that every species is correctly identified. Regional tradition, laboratory findings, randomized clinical evidence and hypotheses must remain distinguishable.

To test locally: `cd botanical-atlas && python -m unittest discover -s tests -v && python tools/atlas_pipeline.py validate && python tools/atlas_pipeline.py build`.
