# Xyool Emergency Recovery Backup

Backup date: **2026-09-25**

Source repository: `Xyooll/Xyool`  
Source canonical branch: `main`  
Source canonical commit: `4137f4ee45b5ebb928c83361e98d1d54a6aceef8`  
Source full tree: `4137f4ee45b5ebb928c83361e98d1d54a6aceef8`

## What this branch is

This branch is an **independent critical-recovery snapshot** stored in the separate private repository `Xyooll/outdated`.

The files in this branch were copied into new Git objects in `outdated`; they do not depend on the source repository remaining available.

## Included

Copied: **297 files / 1991531 bytes**

Included:
- root system/control contracts;
- complete `floware/`;
- complete `memory/` mirror, including User Concept Memory;
- complete text `skills/` library;
- complete `correspondence/`;
- domain architecture, configurations, rules, libraries and flows;
- stock-state schemas and state README.

## Intentionally not included in this first layer

Omitted: **856 files / 9505077 bytes**

Major omissions:
- generated / historical `research/` results;
- bulky stock instance state under `domains/stock-market/state/` except schemas/README;
- runtime/software implementation directories such as `agent/`, `tests/`, `scripts/`, `data/`;
- GitHub workflow files;
- legacy nodes/docs not required by this critical layer;
- one binary skill PDF: `skills/xyool/adversarial-self-targeting-ai-defensive-research.pdf`.

The complete source tree inventory is stored in `FULL-SOURCE-TREE-MANIFEST.json` so omissions are explicit rather than silent.

## Recovery priority

If the primary Xyool repository is lost:

1. restore this branch into a new repository;
2. begin with `SYSTEM-LINEAGE.md` and `XYOOL-START-HERE.md`;
3. treat `memory/user-concepts/` here as the latest integrated mirror captured at the source commit;
4. reconstruct omitted generated state/research from any additional archives if available;
5. do not mistake this backup branch for a live writable canonical lineage until recovery is intentionally promoted.

## Old contents of the `outdated` repository

The pre-backup `outdated/main` state was preserved before this operation at:

`archive/pre-xyool-backup-2026-09-25`

No old repository history was destroyed.
