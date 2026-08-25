import unittest
from software.runtime.attention import AttentionEngine, AttentionRule, Event

class AttentionTests(unittest.TestCase):
    def test_irrelevant_event_does_not_wake_ai(self):
        engine = AttentionEngine()
        engine.register(AttentionRule("large_move", "market", lambda e: e.data.get("move", 0) >= 3, priority=5))
        self.assertEqual(engine.evaluate(Event("market", "tick", {"move": 1})), [])

    def test_trigger_wakes_ai(self):
        engine = AttentionEngine()
        engine.register(AttentionRule("large_move", "market", lambda e: e.data.get("move", 0) >= 3, priority=5))
        signals = engine.evaluate(Event("market", "tick", {"move": 4}))
        self.assertEqual(len(signals), 1)
        self.assertTrue(signals[0].wake_ai)

    def test_priority_orders_attention(self):
        engine = AttentionEngine()
        engine.register(AttentionRule("low", "rss", lambda e: True, priority=1))
        engine.register(AttentionRule("high", "rss", lambda e: True, priority=9))
        signals = engine.evaluate(Event("rss", "article", {}))
        self.assertEqual([s.rule for s in signals], ["high", "low"])

if __name__ == "__main__":
    unittest.main()
