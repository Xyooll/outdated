# Replication and Backup Contract

A node is reconstructible from versioned DNA plus separately provisioned configuration and secrets.

## Required backup classes

- source/DNA: Git repository
- schema: versioned SQL
- memory: encrypted database backups
- audit: append-only logs with retention policy
- configuration: non-secret node manifests
- secrets: external secret manager; never committed

## Clone procedure

1. Provision a new runtime.
2. Clone the repository at a known release.
3. Apply the database schema.
4. Restore authorized memory snapshots if needed.
5. Install node-local configuration.
6. Provision secrets independently.
7. Run integrity checks.
8. Start in read-only/shadow mode.
9. Validate health.
10. Enable application capabilities deliberately.

A clone must not automatically inherit credentials or privileged execution rights from another node.