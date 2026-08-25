import unittest
from software.runtime.sandbox import Sandbox, SimulationEvent

class SandboxTests(unittest.TestCase):
    def test_deterministic_source(self):
        def source(state, rng):
            return SimulationEvent(state.tick, "market", "tick", {"move": rng.random()})
        a, b = Sandbox(7), Sandbox(7)
        a.add_source(source); b.add_source(source)
        self.assertEqual(a.step()[0].data, b.step()[0].data)

    def test_handler_changes_score(self):
        sandbox = Sandbox()
        sandbox.add_source(lambda state, rng: SimulationEvent(state.tick, "test", "reward", {}))
        sandbox.register_handler("reward", lambda state, event: 2.5)
        result = sandbox.run(10)
        self.assertEqual(result.events, 10)
        self.assertEqual(result.score, 25.0)

    def test_invalid_ticks_rejected(self):
        with self.assertRaises(ValueError):
            Sandbox().run(0)

if __name__ == "__main__":
    unittest.main()
