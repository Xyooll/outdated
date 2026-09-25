# Run record template — version 1

Copy into the authorized run store under a unique run/checkpoint ID.
Replace placeholders with observed values; templates are not live state.

- record_id / run_id / pipeline_id / pipeline_version:
- objective / frozen_goalpost_ref:
- repository_commit / Flow_and_Pipe_contract_revisions:
- execution_epoch / expected_parent_record / checkpoint_time:
- source_as_of / observed_at / written_at:
- domain_binding_ref / canonical_state_head:
- current_authority_scope / authority_evidence_ref:
- stages: id, status, input_refs_and_versions, output_ref_and_version, read_set, blockers
- dependencies: producer, consumer, Pipe_id, required_fields, semantic_reason
- Pipes: use the live state fields in [Plumbing](PLUMBING.md)
- invalidated_outputs / retained_outputs_and_reasons:
- pending_external_effects: action_id, attempt_id, receipt_ref, observed_outcome, reconciliation_needed
- pipeline_status / independent_audit_ref_or_pending:
- budget / used_resources_or_NOT_MEASURED:
- storage_receipt: destination, persisted_revision, readback_match, collision_check, concurrency_guarantee
- remaining_work / next_owner:

Storage receipt may be recorded in a subsequent receipt record to avoid a self-referential content hash.
Never place credentials or secrets in records.
