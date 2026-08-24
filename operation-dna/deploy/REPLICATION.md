# Replication and Clone Specification

## Objective
A clone must be reconstructible from versioned DNA plus node-specific configuration and separately provisioned secrets.

## Sequence

1. Clone the repository at a pinned release.
2. Provision the runtime environment.
3. Apply database schema.
4. Restore approved knowledge/data snapshots.
5. Rebuild search indexes.
6. Register the node and geography.
7. Inject secrets through a secure secret manager or environment mechanism.
8. Connect approved external services.
9. Run integrity checks.
10. Start collectors, analysis workers and services.
11. Record node health and DNA version.

## Clone classes

- `full` — complete operational replica
- `research` — knowledge/research only
- `trading` — trading services and required market data only
- `edge` — lightweight collector/monitoring node

## Disaster recovery

The DNA repository is the reconstruction source. Databases and raw archives are replicated separately. No single server, provider or geography is authoritative for the entire operation.
