import unittest

from software.integrations.shadow import ShadowRegistry, StaticProvider

class ShadowIntegrationTests(unittest.TestCase):
    def test_shadow_observation_has_no_side_effects(self):
        registry = ShadowRegistry()
        registry.register(StaticProvider("market", "market.signal", {"symbol": "TEST", "price": 101}))
        observations = registry.observe_all()
        self.assertEqual(len(observations), 1)
        self.assertEqual(observations[0].provider, "market")
        self.assertFalse(observations[0].side_effects)

    def test_providers_are_deterministic_and_sorted(self):
        registry = ShadowRegistry()
        registry.register(StaticProvider("z", "z.event", {"v": 2}))
        registry.register(StaticProvider("a", "a.event", {"v": 1}))
        first = registry.observe_all()
        second = registry.observe_all()
        self.assertEqual(first, second)
        self.assertEqual([x.provider for x in first], ["a", "z"])

    def test_duplicate_provider_rejected(self):
        registry = ShadowRegistry()
        registry.register(StaticProvider("market", "market.signal", {}))
        with self.assertRaises(ValueError):
            registry.register(StaticProvider("market", "market.signal", {}))

if __name__ == "__main__":
    unittest.main()
