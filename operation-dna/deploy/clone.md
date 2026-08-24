# Clone Protocol

1. Clone the repository.
2. Select a node profile from `nodes/`.
3. Provision a clean runtime.
4. Apply `schemas/sqlite.sql` to create the derived index.
5. Load canonical Markdown/YAML records into the index.
6. Rebuild search and relationship indexes.
7. Inject secrets from an external secret manager or environment.
8. Configure local data sources and geographic rules.
9. Start collectors, automation and services.
10. Run integrity checks against the DNA version and schema version.
11. Register the node and begin synchronization.

A clone must never copy secrets from the repository. It should receive credentials independently.
