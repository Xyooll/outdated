import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock

from software.integrations.alpaca_paper import PaperAccount
from software.runtime.decision_memory import DecisionMemory, DecisionRecord
from software.runtime.evolution_engine import generate_candidates
from software.runtime.paper_risk import RiskGate
from software.runtime.position_ledger import PositionLedger
from software.runtime.production_readiness import KillSwitch, PersistentState, ResourceBudget, RuntimeState
from software.runtime.trade_outcomes import OutcomeStore


class NextStageTests(unittest.TestCase):
    def test_risk_gate_blocks_weak_confidence(self):
        gate = RiskGate(min_confidence=0.8)
        result = gate.check(qty=1, price=10, side="buy", confidence=0.79)
        self.assertFalse(result.approved)

    def test_risk_gate_blocks_position_and_daily_loss(self):
        gate = RiskGate(max_position_qty=2, max_daily_loss=50)
        self.assertFalse(gate.check(qty=1, price=10, side="buy", confidence=0.9, position_qty=2).approved)
        self.assertFalse(gate.check(qty=1, price=10, side="buy", confidence=0.9, realized_pnl=-51).approved)

    def test_position_ledger_applies_fill_and_pnl(self):
        with tempfile.TemporaryDirectory() as tmp:
            ledger = PositionLedger(str(Path(tmp) / "ledger.json"))
            ledger.apply_fill("AAPL", 2, "buy", 10)
            position = ledger.apply_fill("AAPL", 1, "sell", 12)
            self.assertEqual(position.qty, 1)
            self.assertEqual(position.realized_pnl, 2.0)
            restored = PositionLedger(str(Path(tmp) / "ledger.json"))
            self.assertEqual(restored.get_position("AAPL").qty, 1)

    def test_outcome_store_calculates_pnl(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = OutcomeStore(str(Path(tmp) / "outcomes.json"))
            outcome = store.close("t1", "AAPL", "buy", 2, 10, 12, "start")
            self.assertEqual(outcome.pnl, 4.0)
            self.assertEqual(store.summary()["wins"], 1)

    def test_decision_memory_persists_and_summarizes(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = str(Path(tmp) / "decisions.json")
            memory = DecisionMemory(path)
            memory.record(DecisionRecord("1", "s1", "buy", 0.8, 5, True))
            memory.record(DecisionRecord("2", "s1", "buy", 0.7, -2, False))
            summary = memory.summary("s1")
            self.assertEqual(summary["samples"], 2)
            self.assertEqual(summary["total_pnl"], 3)
            self.assertEqual(DecisionMemory(path).summary("s1")["samples"], 2)

    def test_evolution_waits_for_samples(self):
        self.assertEqual(generate_candidates("s1", {"samples": 9}), [])
        candidates = generate_candidates("s1", {"samples": 10, "direction_accuracy": 0.8, "mean_pnl": 2})
        self.assertTrue(candidates)
        self.assertTrue(all(c.requires_validation for c in candidates))


if __name__ == "__main__":
    unittest.main()
