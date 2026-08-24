# Operational DNA Architecture

## Principle
The operation is portable. Infrastructure is replaceable.

## Layers
1. DNA: portable knowledge, schemas, maps, strategies, workflows, deployment definitions.
2. Node: location-specific runtime, services, data stores and configuration.
3. Secrets: separately provisioned credentials and private keys; never committed to Git.
4. Interfaces: Notion, Airtable, Dropbox and other tools are replaceable operational interfaces, not the canonical source.

## Replication
A new node is created by cloning the DNA repository, provisioning the node configuration, applying schemas, rebuilding indexes, restoring approved data, injecting secrets, and starting services.

## Resilience
Maintain geographically separated replicas. A node or provider can fail without destroying the canonical DNA.
