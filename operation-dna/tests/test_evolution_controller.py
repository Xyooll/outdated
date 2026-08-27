import tempfile
import unittest
from pathlib import Path

from operation_dna.software.runtime.evolution_controller import EvolutionController
from operation_dna.software.runtime.strategy_engine import StrategyEngine


class EvolutionControllerTests(unittest.TestCase):
    def test_waits_for_evidence(self):
        with tempfile.TemporaryDirectory() as td:
            controller = EvolutionController(StrategyEngine(), str(Path(td) / "evolution.json"))
            run = controller.evolve("baseline", minimum_samples=3)
            self.assertFalse(run.promoted)
            self.assertIsNone(run.winner)
            self.assertIn("insufficient", run.reason)

    def test_generates_candidate_after_evidence(self):
        with tempfile.TemporaryDirectory() as td:
            controller = EvolutionController(StrategyEngine(), str(Path(td) / "evolution.json"))
            for pnl in [1.0, -0.5, 0.5, -0.25, 0.75]:
                controller.learn("baseline", pnl)
            run = controller.evolve("baseline", minimum_samples=5)
            self.assertTrue(run.candidates)
            self.assertIsNotNone(run.winner)
            self.assertFalse(run.promoted)
            self.assertIn("validation", run.reason)

    def test_promotion_requires_explicit_authority(self):
        with tempfile.TemporaryDirectory() as td:
            controller = EvolutionController(StrategyEngine(), str(Path(td) / "evolution.json"))
            for _ in range(5):
                controller.learn("baseline", 1.0)
            denied = controller.evolve("baseline", minimum_samples=5, promote=True)
            self.assertFalse(denied.promoted)
            self.assertIn("authority", denied.reason)
            approved = controller.evolve("baseline", minimum_samples=5, promote=True,
                                         authority=lambda candidate: True)
            self.assertTrue(approved.promoted)

    def test_history_persists(self):
        with tempfile.TemporaryDirectory() as td:
            path = str(Path(td) / "evolution.json")
            controller = EvolutionController(StrategyEngine(), path)
            for _ in range(5):
                controller.learn("baseline", -1.0)
            controller.evolve("baseline", minimum_samples=5)
            restored = EvolutionController(StrategyEngine(), path)
            self.assertEqual(restored.generation, 1)
            self.assertEqual(len(restored.history), 1)


if __name__ == "__main__":
    unittest.main()
