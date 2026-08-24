import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from software.research.normalization import ResearchEvent
from software.research.market_events import stock_bar_events, crypto_market_events
from software.economics.scanners import scan_business


class ResearchPipelineTests(unittest.TestCase):
    def test_event_ids_are_stable(self):
        event = ResearchEvent("test", "1", "title", "summary")
        self.assertEqual(event.event_id, event.event_id)

    def test_stock_payload_normalizes(self):
        events = stock_bar_events({"bars": {"ABC": [{"t": "2026-01-01T00:00:00Z", "o": 1, "h": 2, "l": 0.5, "c": 1.5, "v": 100}]}})
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0].entity, "ABC")

    def test_crypto_payload_normalizes(self):
        events = crypto_market_events([{"id": "bitcoin", "name": "Bitcoin", "symbol": "btc", "current_price": 1}])
        self.assertEqual(events[0].source, "coingecko")

    def test_business_scanner_detects_signal(self):
        candidates = scan_business([{"title": "New contract", "summary": "customer backlog"}])
        self.assertEqual(candidates[0].domain, "business")


if __name__ == "__main__":
    unittest.main()
