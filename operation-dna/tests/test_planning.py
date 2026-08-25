import unittest
from software.runtime.capability_bus import CapabilityBus, CapabilitySpec
from software.runtime.plan import Plan, PlanStep, validate_plan, PlanValidationError
from software.runtime.autonomy import Autonomy, require_mode, AutonomyError

class PlanningTests(unittest.TestCase):
    def test_plan_uses_only_known_capabilities(self):
        bus = CapabilityBus()
        bus.register(CapabilitySpec("research", "research", lambda: None))
        plan = Plan("find evidence", (PlanStep("research"),))
        validate_plan(plan, {x["name"] for x in bus.catalog()})

    def test_unknown_capability_rejected(self):
        with self.assertRaises(PlanValidationError):
            validate_plan(Plan("bad", (PlanStep("missing"),)), set())

    def test_autonomy_is_explicit(self):
        require_mode(Autonomy.SIMULATE, Autonomy.SIMULATE)
        with self.assertRaises(AutonomyError):
            require_mode(Autonomy.SIMULATE, Autonomy.CONTROLLED_EXECUTION)

if __name__ == "__main__":
    unittest.main()
