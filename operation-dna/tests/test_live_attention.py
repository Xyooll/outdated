import unittest
from software.integrations.shadow import ShadowObservation
from software.integrations.live_attention import observation_to_event, decide

class LiveAttentionTests(unittest.TestCase):
    def test_ordinary_trade_does_not_wake_ai(self):
        obs = ShadowObservation("alpaca", "market.signal", {"symbol":"BTC/USD","price":100,"size":10,"timestamp":"2026-08-26T00:00:00Z"})
        result = decide(obs)
        self.assertFalse(result.wake_ai)

    def test_large_trade_wakes_ai(self):
        obs = ShadowObservation("alpaca", "market.signal", {"symbol":"BTC/USD","price":100,"size":10000,"timestamp":"2026-08-26T00:00:00Z"})
        result = decide(obs)
        self.assertTrue(result.wake_ai)
        self.assertIn("large_market_trade", result.reasons)

    def test_observation_normalizes_to_event(self):
        obs = ShadowObservation("alpaca", "market.signal", {"symbol":"BTC/USD","price":100,"size":10})
        event = observation_to_event(obs)
        self.assertEqual(event.source, "alpaca")
        self.assertEqual(event.event_type, "market.signal")

if __name__ == "__main__":
    unittest.main()
