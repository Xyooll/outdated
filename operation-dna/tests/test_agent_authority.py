import unittest
from operation_dna.software.runtime.agent_authority import Authority, allowed, promotion_requires_authority


class AgentAuthorityTests(unittest.TestCase):
    def test_levels_are_ordered(self):
        self.assertLess(Authority.BUILD, Authority.VALIDATE)
        self.assertLess(Authority.VALIDATE, Authority.PROMOTE)

    def test_promotion_is_explicit(self):
        self.assertFalse(promotion_requires_authority(Authority.VALIDATE))
        self.assertTrue(promotion_requires_authority(Authority.PROMOTE))

    def test_required_level(self):
        self.assertTrue(allowed(Authority.REPAIR, Authority.BUILD))
        self.assertFalse(allowed(Authority.BUILD, Authority.REPAIR))


if __name__ == "__main__":
    unittest.main()
