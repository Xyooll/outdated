import unittest
from software.runtime.evaluation import Evaluator, EvaluationMetrics

class EvaluationTests(unittest.TestCase):
    def test_candidate_wins_without_more_errors(self):
        evaluator = Evaluator()
        baseline = EvaluationMetrics(10.0, 5.0, 15.0, 0.1, 3)
        candidate = EvaluationMetrics(12.0, 7.0, 17.0, 0.1, 3)
        result = evaluator.compare(baseline, candidate)
        self.assertTrue(result.candidate_better)
        self.assertEqual(result.improvement, 2.0)

    def test_candidate_with_higher_errors_is_rejected(self):
        evaluator = Evaluator()
        baseline = EvaluationMetrics(10.0, 5.0, 15.0, 0.1, 3)
        candidate = EvaluationMetrics(12.0, 7.0, 17.0, 0.2, 3)
        self.assertFalse(evaluator.compare(baseline, candidate).candidate_better)

if __name__ == "__main__":
    unittest.main()
