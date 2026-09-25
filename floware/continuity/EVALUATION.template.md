# Evaluation protocol template — version 1

Freeze before observing test responses.

- experiment_id / author / candidate_commit / baseline_commit:
- question / success_gates / failure_gates / stop_budget:
- design: GUIDED / BLINDED / ISOLATED_AB
- task_pool / evidence_snapshot / holdout_custodian:
- executor_access / evaluator_access / contamination_policy:
- model_version / settings / tools / permissions / total_budget:
- treatment: exact Floware instructions supplied
- control: exact ordinary instructions supplied
- repetitions / order_counterbalancing / exclusions:
- frozen_rubric: completion, constraint violations, unsupported claims, unnecessary blocks
- measurement_plan: elapsed time, total tokens including Flow loading, monetary cost
- separation_evidence / independent_auditor:
- immutable_response_locations / failure_retention:
- result: per-case and aggregate, spread/uncertainty, missing measurements
- independent_audit / promotion_decision_owner:

A public fixture and its answers are development material.
A holdout requires a separate custodian and actual restricted executor access.
If no isolated executor is available, ISOLATED_AB = NOT_RUN.
No result is inferred from filling this template.
