import unittest
from software.runtime.capability_bus import CapabilityBus, CapabilitySpec
from software.runtime.plan import Plan, PlanStep, validate_plan, resolve_missing, resolve_or_build, PlanValidationError
from software.runtime.autonomy import Autonomy, require_mode, AutonomyError

class PlanningTests(unittest.TestCase):
    def test_plan_uses_known_capabilities(self):
        bus = CapabilityBus()
        bus.register(CapabilitySpec("research", "research", lambda: None))
        plan = Plan("find evidence", (PlanStep("research"),))
        validate_plan(plan)
        self.assertEqual(resolve_missing(plan, {x["name"] for x in bus.catalog()}), [])

    def test_missing_capability_becomes_build_request(self):
        plan = Plan("find evidence", (PlanStep("new_research_tool", purpose="Need a better research capability"),))
        requests = resolve_missing(plan, set())
        self.assertEqual(requests[0].name, "new_research_tool")
        self.assertEqual(requests[0].purpose, "Need a better research capability")

    def test_missing_capability_can_be_sent_to_builder(self):
        plan = Plan("create capability", (PlanStep("generated_tool"),))
        built = []
        _, requests = resolve_or_build(plan, set(), lambda request: built.append(request.name))
        self.assertEqual(built, ["generated_tool"])
        self.assertEqual(len(requests), 1)

    def test_empty_plan_rejected(self):
        with self.assertRaises(PlanValidationError):
            validate_plan(Plan("", ()))

    def test_autonomy_is_explicit(self):
        require_mode(Autonomy.SIMULATE, Autonomy.SIMULATE)
        with self.assertRaises(AutonomyError):
            require_mode(Autonomy.SIMULATE, Autonomy.CONTROLLED_EXECUTION)

if __name__ == "__main__":
    unittest.main()
