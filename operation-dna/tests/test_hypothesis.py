import unittest
from software.runtime.hypothesis import HypothesisEngine

class HypothesisTests(unittest.TestCase):
    def test_generates_from_underperformance(self):
        engine = HypothesisEngine()
        hs = engine.generate([{"metric": "lookback", "signal": "underperforming", "reason": "drawdown"}], "return")
        self.assertEqual(len(hs), 1)
        self.assertEqual(hs[0].target_metric, "lookback")

    def test_empty_observations(self):
        self.assertEqual(HypothesisEngine().generate([], "profit"), [])

    def test_candidate_creation(self):
        h = HypothesisEngine().generate([{"metric": "threshold", "signal": "underperforming"}], "profit")[0]
        spec = HypothesisEngine().create_candidate(h, lambda _: lambda x: True)
        self.assertIn("Candidate generated", spec.description)

if __name__ == "__main__":
    unittest.main()
