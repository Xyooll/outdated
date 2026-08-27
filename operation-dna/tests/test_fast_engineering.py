import tempfile
import unittest
from pathlib import Path

from operation_dna.software.runtime.ai_provider import LocalStubProvider
from operation_dna.software.runtime.autonomous_engineer import AutonomousEngineer
from operation_dna.software.runtime.build_memory import BuildMemory
from operation_dna.software.runtime.capability_orchestrator import CapabilityOrchestrator
from operation_dna.software.runtime.offline_self_build import OfflineGenerator
from operation_dna.software.runtime.self_build_agent import BuildRequest, SelfBuildAgent
from operation_dna.software.runtime.software_factory import SoftwareFactory


class FastEngineeringTests(unittest.TestCase):
    def test_orchestrator_plans_independent_goals(self):
        result = CapabilityOrchestrator(LocalStubProvider(), max_workers=2).plan(
            "build a probe and build a validator"
        )
        self.assertEqual(len(result.tasks), 2)
        self.assertEqual(len(result.plans), 2)
        self.assertEqual(result.tasks[0].index, 0)
        self.assertEqual(result.tasks[1].index, 1)

    def test_autonomous_engineer_validates_without_promotion(self):
        with tempfile.TemporaryDirectory() as tmp:
            factory = SoftwareFactory(str(Path(tmp) / "stage"))
            agent = SelfBuildAgent(factory, OfflineGenerator(), max_iterations=2)
            engineer = AutonomousEngineer(
                LocalStubProvider(), agent,
                BuildMemory(str(Path(tmp) / "memory.jsonl")),
                max_repairs=1,
            )
            outcome = engineer.build(BuildRequest("probe", "build a deterministic probe"))
            self.assertTrue(outcome.resolved)
            self.assertFalse(outcome.result.promoted)
            self.assertEqual(outcome.attempts, 1)

    def test_empty_goal_is_rejected(self):
        with self.assertRaises(ValueError):
            CapabilityOrchestrator(LocalStubProvider()).plan("")


if __name__ == "__main__":
    unittest.main()
