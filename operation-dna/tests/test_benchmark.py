import unittest
from software.runtime.sandbox import Sandbox, SimulationEvent
from software.runtime.benchmark import BenchmarkRunner

class BenchmarkTests(unittest.TestCase):
    @staticmethod
    def factory(seed):
        sandbox = Sandbox(seed)
        sandbox.add_source(lambda state, rng: SimulationEvent(state.tick, "test", "reward", {}))
        sandbox.register_handler("reward", lambda state, event: 1.0)
        return sandbox

    def test_reproducible_benchmark(self):
        result = BenchmarkRunner().run(self.factory, self.factory, runs=10, ticks=100)
        self.assertEqual(result.baseline.mean_score, 100.0)
        self.assertEqual(result.candidate.mean_score, 100.0)
        self.assertFalse(result.comparison.candidate_better)

    def test_invalid_configuration(self):
        with self.assertRaises(ValueError):
            BenchmarkRunner().run(self.factory, self.factory, runs=0, ticks=100)

if __name__ == "__main__":
    unittest.main()
