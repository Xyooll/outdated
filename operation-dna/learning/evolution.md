# Learning and Safe Evolution

The system learns through controlled experimentation, not unrestricted self-modification.

## Lifecycle
1. Observe
2. Detect a possible improvement
3. Form a hypothesis
4. Generate a candidate change
5. Test in an isolated environment
6. Evaluate against baseline and out-of-sample conditions
7. Shadow/paper deploy where applicable
8. Apply safety gates
9. Limited promotion
10. Monitor
11. Promote, reject, or roll back

Every candidate keeps lineage to its parent version and records evidence, metrics, risks and evaluation results.

Production behavior must remain reversible. A candidate cannot silently alter security boundaries, credentials, hard limits, audit controls, or rollback mechanisms.