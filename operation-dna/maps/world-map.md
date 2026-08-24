# World Node Map

## Node model

Each operational node has:

- `node_id`
- `region`
- `jurisdiction`
- `runtime`
- `data_residency`
- `services`
- `local_sources`
- `local_regulatory_profile`
- `status`

## Initial topology

- `US-01` — United States primary node
- `EU-01` — Europe replication target
- `APAC-01` — Asia-Pacific replication target

These are design targets, not claims that infrastructure is currently deployed.

## Rule

Knowledge and logic are portable. Credentials, private keys, local accounts and jurisdiction-specific secrets remain node-specific.
