import unittest

from software.economics.learning import Forecast, Outcome, evaluate, calibration
from software.economics.business import BusinessOpportunity, rank
from software.economics.risk import RiskBudget
from software.evolution.promoter import Evaluation, eligible


class EconomicsTests(unittest.TestCase):
    def test_learning(self):
        f = Forecast("f1", "o1", .8, .2, .1, "2026-01-01")
        o = Outcome("f1", .3, .01, "2026-02-01")
        result = evaluate(f, o)
        self.assertTrue(result["direction_correct"])
        self.assertAlmostEqual(result["error"], .1)
        self.assertEqual(calibration([result])["samples"], 1)

    def test_business_ranking(self):
        a = BusinessOpportunity("A", 1, 1, 10, 100, 5)
        b = BusinessOpportunity("B", .5, .5, 100, 50, 30)
        self.assertEqual(rank([b, a])[0].name, "A")

    def test_risk_budget(self):
        budget = RiskBudget(100, 20, 10, 50)
        budget.validate()
        self.assertTrue(budget.can_allocate(10))
        self.assertFalse(budget.can_allocate(21))
        self.assertFalse(budget.can_allocate(10, 45))

    def test_evolution_requires_improvement_and_samples(self):
        self.assertFalse(eligible(Evaluation("v2", .8, .9, 0, 10)))
        self.assertTrue(eligible(Evaluation("v2", .8, .9, 0, 30)))
        self.assertFalse(eligible(Evaluation("v2", .8, .9, 1, 30)))


if __name__ == "__main__":
    unittest.main()
