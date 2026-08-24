import tempfile
import unittest
from pathlib import Path
from software.runtime.controller import MasterController
from software.economics.learning import Forecast, Outcome

class ControllerTests(unittest.TestCase):
    def test_closed_loop_ingest_and_learning(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = str(Path(tmp) / "dna.db")
            controller = MasterController(db)
            report = controller.cycle("c1", [{"event_id":"e1","source":"test","title":"Demand signal","published_at":"2026-08-24T12:00:00Z","event_type":"rss"}])
            self.assertEqual(report.state, "completed")
            forecast = Forecast("f1", "business|Demand signal|", .8, .2, .1, "2026-08-24T12:00:00Z")
            controller.record_forecast(forecast)
            result = controller.observe(Outcome("f1", .25, .01, "2026-08-25T12:00:00Z"))
            self.assertTrue(result["direction_correct"])
            self.assertEqual(len(controller.results), 1)

    def test_duplicate_forecast_is_rejected(self):
        controller = MasterController(":memory:")
        f = Forecast("f1", "o1", .5, .1, .1, "2026-08-24T00:00:00Z")
        controller.record_forecast(f)
        with self.assertRaises(ValueError):
            controller.record_forecast(f)

if __name__ == "__main__":
    unittest.main()
