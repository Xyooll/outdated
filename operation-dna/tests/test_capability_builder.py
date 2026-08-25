import unittest
from software.runtime.hypothesis import Hypothesis, CandidateSpec
from software.runtime.capability_builder import CapabilityBuilder

class CapabilityBuilderTests(unittest.TestCase):
    def spec(self):
        h = Hypothesis("test candidate", "score", "increase", "test", {})
        return CandidateSpec(h, lambda x: x, "test")

    def test_passes_gates_but_does_not_auto_promote(self):
        builder = CapabilityBuilder(lambda _: True, lambda _: True)
        result = builder.build(self.spec())
        self.assertTrue(result.eligible_for_promotion)
        self.assertFalse(builder.promote(result, lambda _: False))

    def test_failed_test_cannot_promote(self):
        builder = CapabilityBuilder(lambda _: False, lambda _: True)
        result = builder.build(self.spec())
        self.assertFalse(result.eligible_for_promotion)
        self.assertFalse(builder.promote(result, lambda _: True))

    def test_sandbox_failure_cannot_promote(self):
        builder = CapabilityBuilder(lambda _: True, lambda _: False)
        result = builder.build(self.spec())
        self.assertFalse(result.eligible_for_promotion)

if __name__ == "__main__":
    unittest.main()
