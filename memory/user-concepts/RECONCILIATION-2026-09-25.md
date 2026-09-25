# User Concept Lineage Reconciliation — 2026-09-25

Status: **COMPLETE / MIGRATION PROVENANCE**

## Purpose

Before canonicalization, User Concept Memory had diverged across feature branches.

This record preserves the one-time reconciliation that established `lineage/user-concepts` as the canonical history.

## Reconciliation basis

The canonical lineage branch was created from `feature/domain-establishment-v1`, because that branch contained the broadest known superset of the then-current thought ledger.

The canonical `feature/rle-level-a` ledger was verified to be a subset of that history.

One additional valid concept existed only on `feature/astrology-predictive-v1` and was imported explicitly before canonicalization was declared complete.

## Recovered branch-local concepts

| Concept file | Source branch | Source blob SHA |
|---|---|---|
| `2026-09-24-future-build-notes.md` | `feature/domain-establishment-v1` | `fe59081f9872d24539fa9c32d92f8671fc24dec9` |
| `2026-09-25-domain-libraries-build-self-sufficiency.md` | `feature/domain-establishment-v1` | `df4bda3ca343e20f65285859b5aa06bc36195c15` |
| `2026-09-25-meaning-attribution-and-novelty-enhancer.md` | `feature/domain-establishment-v1` | `57af2bd13aabba400fbc76a4725fac9498e28f9e` |
| `2026-09-25-processor-executioner-agent-loop.md` | `feature/domain-establishment-v1` | `39870e42f1cb1078f1bea2961f83b8546a4fbe05` |
| `2026-09-25-event-model-rss-html-control-layer.md` | `feature/domain-establishment-v1` | `0e5091221d05715cc9f49c255a7cfae50d3658c3` |
| `2026-09-25-star-astrology-degree-as-atomic-unit.md` | `feature/astrology-predictive-v1` | `3d895718268f945f6e2e665e7cef8a2454cd46b0` |

## Canonicalization changes

After recovery:
- `lineage/user-concepts` became the sole current User Concept Memory authority;
- the canonical ledger was updated to include all reconciled concepts;
- the Star Astrology concept was imported into the lineage;
- the canonical-lineage architecture concept was added;
- `LINEAGE.md` defined read/write/reconciliation rules;
- working branches with known drift were marked non-authoritative mirrors.

## Historical rule

These source branches remain valid provenance for the fact that the concepts were first captured there.

They are not competing current ledgers.

Future branch-local memory divergence is a reconciliation event and must not be silently treated as a second lineage.
