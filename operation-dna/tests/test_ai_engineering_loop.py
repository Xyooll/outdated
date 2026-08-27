import unittest

from operation_dna.software.runtime.ai_engineering_loop import AIEngineeringLoop
from operation_dna.software.runtime.ai_provider import LocalStubProvider
from operation_dna.software.runtime.self_build_pipeline import SelfBuildPipeline
from operation_dna.software.runtime.self_build_planner import SelfBuildPlanner
from operation_dna.software.runtime.self_build_agent import SelfBuildAgent
from operation_dna.software.runtime.software_factory import SoftwareFactory
from operation_dna.software.runtime.offline_self_build import OfflineGenerator


class AIEngineeringLoopTests(unittest.TestCase):
    def test_provider_can_plan(self):
        provider = LocalStubProvider()
        plan = provider.plan("build a deterministic probe capability")
        self.assertTrue(plan.name.startswith("capability_"))
        self.assertEqual(plan.goal, "build a deterministic probe capability")

    def test_provider_can_choose_repair(self):
        repair = LocalStubProvider().repair(
            LocalStubProvider().plan("probe"), "syntax error in generated module"
        )
        self.assertEqual(repair.category, "syntax")
        self.assertTrue(repair.instructions)

    def test_loop_runs_through_pipeline(self):
        factory = SoftwareFactory(".")
        planner = SelfBuildPlanner()
        builder = SelfBuildAgent(factory, OfflineGenerator())
        pipeline = SelfBuildPipeline(factory, planner, builder)
        run = AIEngineeringLoop(LocalStubProvider(), pipeline).run("build a deterministic probe capability")
        self.assertEqual(run.goal, "build a deterministic probe capability")
        self.assertTrue(run.plan.requirements)
        self.assertTrue(run.build.build.syntax_ok)


if __name__ == "__main__":
    unittest.main()
