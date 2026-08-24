import tempfile
from pathlib import Path
from operation_dna.software.engine.core import Event, ingest, gate_decision
from operation_dna.software.engine.learning import Evaluation, eligible_for_promotion

def test_event_deduplication():
    e = Event("s", "title", "https://x", "2026-01-01")
    assert len(ingest([e, e], set())) == 1

def test_gate_requires_all_controls():
    assert gate_decision(authorized=True, evidence=True, valid=True, risk_ok=True, permitted=True, reversible=True)
    assert not gate_decision(authorized=True, evidence=False, valid=True, risk_ok=True, permitted=True, reversible=True)

def test_learning_requires_robust_improvement():
    assert eligible_for_promotion(Evaluation(1, 2, False, True), True)
    assert not eligible_for_promotion(Evaluation(1, 2, True, True), True)
