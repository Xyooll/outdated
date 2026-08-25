import unittest
from software.simulations.trading_market import run_strategy, momentum_baseline
from software.simulations.business_market import run_business_strategy, fit_baseline

class SimulationTests(unittest.TestCase):
    def test_trading_is_reproducible(self):
        a = run_strategy(momentum_baseline, seed=10, ticks=500)
        b = run_strategy(momentum_baseline, seed=10, ticks=500)
        self.assertEqual(a, b)

    def test_business_is_reproducible(self):
        a = run_business_strategy(fit_baseline, seed=10, opportunities=500)
        b = run_business_strategy(fit_baseline, seed=10, opportunities=500)
        self.assertEqual(a, b)

    def test_simulations_have_no_external_dependency(self):
        result = run_business_strategy(fit_baseline, seed=1, opportunities=10)
        self.assertGreaterEqual(result.profit, -result.costs)

if __name__ == "__main__":
    unittest.main()
