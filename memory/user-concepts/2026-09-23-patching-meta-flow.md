# User Concept — Patching Meta Flow

Date: 2026-09-23
Status: **ACTIVE / CORE FLOWARE ARCHITECTURE**

## USER-STATED

Xyool may need a Patching Meta Flow so that when an update is made, the system knows how and what to update.

The intended concept is:

> **Apply one update and update all of the right dependent places without missing any.**

## ASSISTANT INTERPRETATION

A patch should not mean editing one obvious file.

It should mean:

~~~text
AUTHORIZED SOURCE CHANGE
→ DISCOVER IMPACT / DEPENDENCIES
→ BUILD PATCH SET
→ UPDATE / MIGRATE / VERIFY EACH MATERIAL SURFACE
→ META AUDIT
→ COMPLETE ONLY WHEN NOTHING MATERIAL IS MISSED
~~~

Patching is distinct from:
- Development / Learning — decides what should change and why;
- Mapping — determines how representations line up;
- Domain Configurer — validates domain composition;
- Audit — independently checks whether the patch is complete.

## SYSTEM CONSEQUENCE

Canonical Meta Flow:
- `floware/meta/patching.flow.md`

Patching now owns:
- change-impact discovery;
- explicit impact graphs;
- dependency-aware patch sets;
- partial-patch detection;
- migration / compatibility disposition;
- preservation of historical immutable records;
- routing to Mapping / Domain Configurer where needed;
- verification and independent Meta Audit before VERIFIED status.

Core laws:

> **Change the concept once; patch every materially dependent representation.**

> **Patch the present contract; preserve the evidence of the past.**

## RELATED CONCEPTS

- Floware as an AI-native layer above software
- Meta Flow
- Mapping
- Domain Configurer
- Audit
- recursive learning / governed promotion
- relational story master-contract integrity

## OPEN QUESTION

As Xyool grows, deterministic dependency indexing may become justified to support Patching at scale. The reasoning contract should remain Floware even if software later supports exact reference/dependency discovery.
