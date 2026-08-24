# Security Model

## Never commit

- API keys
- OAuth client secrets
- passwords
- private keys
- wallet seed phrases
- exchange credentials
- database passwords
- production environment files

## Separation

Portable DNA contains schemas, logic, maps, documentation, non-secret source definitions and deployment templates. Node secrets are provisioned independently.

## Data handling

Raw evidence and derived intelligence should be classified by sensitivity. Replicas should receive only the data required for their role and jurisdiction.

## Integrity

Use pinned versions/releases for production nodes. Verify repository state and database migrations before deployment.
