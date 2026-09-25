# User Concept — Source Infrastructure Waits for Autonomy

Date: **2026-09-24**  
Status: **ACTIVE / FUTURE AUTONOMY ARCHITECTURE**

## USER-STATED WORDING

> "Right now we don't really have an input for these but we will build it later."

> "Yeah, one we make xyool autonomous then we make use of it"

## CONCEPT

Xyool may define and catalog useful information sources before it has an autonomous input/ingestion mechanism for them.

The RSS/source registry should therefore be preserved now as future-ready source infrastructure, without forcing an artificial ingestion path into the current architecture.

When Xyool becomes autonomous, the source registry can become one of the system's active external-input surfaces.

## ASSISTANT INTERPRETATION

The intended progression is:

```text
NOW
SOURCE DISCOVERY + SOURCE AUTHORITY + REGISTRY
→ preserve the sources and their meaning

LATER
AUTONOMOUS INPUT / MONITORING CAPABILITY
→ consume registered sources
→ detect changes
→ map them to characters / relationships / events
→ validate evidence
→ update state
→ trigger affected Flows
```

The autonomy layer should consume the existing source contracts rather than redefining source authority.

This means "having a source" and "having an autonomous input for that source" are separate architectural concerns.

## SYSTEM CONSEQUENCE

Current RSS/source work remains a **passive source registry/specification** until Xyool has an autonomous input/monitoring capability.

Do not build or imply an always-on polling/ingestion system merely because the registry exists.

When autonomous input is developed, reconnect to:

- `domains/stock-market/SOURCE-REGISTRY.md`
- `domains/stock-market/sources/rss.yaml`
- `domains/stock-market/flows/story-sourcing.flow.md`

and create the appropriate governed Pipe from autonomous external sensing into evidence/state handling.

## RELATED CONCEPTS

- Source Quality Builds the Story
- Floware as an AI-native layer above software
- Pipes / Pointers / Wrappers
- Persistent state / delta fetching
- Future autonomous Xyool
