import tempfile
import unittest
from pathlib import Path

from operation_dna.software.runtime.offline_self_build import OfflineGenerator
from operation_dna.software.runtime.self_build_pipeline import SelfBuildPipeline
from operation_dna.software.runtime.self_build_planner import SelfBuildPlanner
from operation_dna.software.runtime.self_build_agent import AutonomousSelfBuildAgent
from operation_dna.software.runtime.software_factory import SoftwareFactory

class SelfBuildPipelineTests(unittest.TestCase):
    def test_offline_pipeline_builds_candidate_without_api(self):
        with tempfile.TemporaryDirectory() as tmp:
            factory = SoftwareFactory(staging_root=tmp)
            planner = SelfBuildPlanner()
            builder = AutonomousSelfBuildAgent(factory, OfflineGenerator(), max_iterations=1)
            result = SelfBuildPipeline(factory, planner, builder).run("build a deterministic probe capability")
            self.assertTrue(result.build.build.syntax_ok)
            self.assertTrue(result.build.build.tests_ok)
            self.assertFalse(result.build.promoted)
            self.assertEqual(result.plan.reason, "no matching capability; new capability required")

    def test_planner_rejects_empty_goal(self):
        with self.assertRaises(ValueError):
            SelfBuildPlanner().plan("")

if __name__ == "__main__":
    unittest.main()
