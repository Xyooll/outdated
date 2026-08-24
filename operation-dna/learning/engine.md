# Learning Engine Contract

The learning engine converts experience into tested candidate improvements.

```text
observe → record experience → detect pattern → form hypothesis → generate candidate
→ isolate → evaluate → stress test → safety gate → shadow/limited deployment
→ monitor → promote or rollback → record outcome
```

## Rules

1. Every learning claim must reference evidence.
2. Candidate changes are immutable during an evaluation run.
3. Production and experiment state remain isolated.
4. Baselines are retained for comparison.
5. Promotion requires measurable improvement without unacceptable risk regression.
6. Every promotion has a rollback target.
7. Failed experiments become memory rather than being discarded.
8. The learning engine cannot disable core safety invariants.
9. Changes to credentials, permissions, audit controls, financial hard limits, or recovery mechanisms require explicit authorization.
10. Learning should optimize for robustness and generalization, not merely short-term performance.
