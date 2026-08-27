import unittest

from software.runtime.market_features import FeatureEngine
from software.runtime.signal_engine import SignalEngine
from software.runtime.strategy_engine import StrategyEngine


class StrategyEngineTests(unittest.TestCase):
    def test_features_are_deterministic(self):
        engine = FeatureEngine()
        values = [100, 101, 102, 103, 104, 105]
        result = None
        for value in values:
            result = engine.update(value, value - 0.1, value + 0.1, 10)
        self.assertAlmostEqual(result.return_5, 0.05)
        self.assertGreater(result.trend, 0)
        self.assertGreaterEqual(result.spread, 0)

    def test_signal_enters_on_confluence(self):
        engine = FeatureEngine()
        result = None
        for value in [100, 101, 102, 103, 104, 105]:
            result = engine.update(value)
        signal = SignalEngine().evaluate(result)
        self.assertEqual(signal.action, "buy")
        self.assertGreater(signal.confidence, 0.5)

    def test_signal_exits_existing_position(self):
        engine = FeatureEngine()
        result = None
        for value in [105, 104, 103, 102, 101, 100]:
            result = engine.update(value)
        signal = SignalEngine().evaluate(result, position_qty=1)
        self.assertEqual(signal.action, "sell")

    def test_strategy_engine_ranks_results(self):
        engine = FeatureEngine()
        result = None
        for value in [100, 101, 102, 103, 104, 105]:
            result = engine.update(value)
        strategies = StrategyEngine()
        results = strategies.evaluate(result)
        self.assertEqual(len(results), 5)
        self.assertTrue(all(r.signal.action in {"buy", "sell", "hold"} for r in results))

    def test_strategy_stats(self):
        strategies = StrategyEngine()
        strategies.record("fast", 2.0)
        strategies.record("fast", -1.0)
        row = next(r for r in strategies.leaderboard() if r["strategy"] == "fast")
        self.assertEqual(row["samples"], 2)
        self.assertEqual(row["wins"], 0) if "wins" in row else None
        self.assertEqual(row["total_pnl"], 1.0)
        self.assertEqual(row["win_rate"], 0.5)


if __name__ == "__main__":
    unittest.main()
