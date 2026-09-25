# Use continuity without rebuilding Floware

This is an opt-in candidate extension. Start with the [canonical glossary](../GLOSSARY.md).
Existing [Flow](../FLOW-CONTRACT.md) and [Pipe](../PIPE-CONTRACT.md) contracts remain the reusable authoring templates; no competing definitions are introduced.

1. Use Direct Resolution for a short self-contained task.
2. For material work that must survive interruption, select [Continuity v1](PIPELINE.md).
3. Keep the existing owning Flow and goalpost. Record a material handoff using [Run Record](../core/run-record.flow.md) and its [template](RUN-RECORD.template.md).
4. On interruption, invoke [Checkpoint Resume](../core/checkpoint-resume.flow.md). On changed evidence, invoke [Evidence Refresh](../core/evidence-refresh.flow.md). Existing Pipeline Integrity/Sequencing govern re-entry.
5. For a capability test, select [Evaluation](../core/evaluation.flow.md) with its [protocol template](EVALUATION.template.md).
6. Follow the [non-stock worked example](WORKED-EXAMPLE.md) and inspect the [patch record](../../research/system-tests/floware-continuity-v1-2026-09-24/PATCH-RECORD.md).

Maturity annotations:
SPECIFIED means a contract exists; DEMONSTRATED requires linked observed execution;
REPEATABLY_TESTED requires repeated runs under a frozen protocol;
OPERATIONALLY_VERIFIED requires the relevant real persistence/recovery and audit evidence.
These annotations never replace the canonical Pipeline statuses or existing domain release gates.
This extension is SPECIFIED, with local structural review only. It is not operationally verified.
