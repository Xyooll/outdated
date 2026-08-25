import tempfile
import unittest
from pathlib import Path
from software.runtime.event_log import AIEvent, EventLog

class EventLogTests(unittest.TestCase):
    def test_append_and_read(self):
        with tempfile.TemporaryDirectory() as tmp:
            log = EventLog(str(Path(tmp) / "events.jsonl"))
            log.append(AIEvent(event_type="attention", objective="trade", trigger="volatility", confidence=.8))
            events = log.read()
            self.assertEqual(len(events), 1)
            self.assertEqual(events[0]["event_type"], "attention")
            self.assertEqual(events[0]["objective"], "trade")
            self.assertEqual(events[0]["confidence"], .8)
            self.assertTrue(events[0]["timestamp"])

    def test_recent_limit(self):
        with tempfile.TemporaryDirectory() as tmp:
            log = EventLog(str(Path(tmp) / "events.jsonl"))
            for i in range(3):
                log.append(AIEvent(event_type=f"event_{i}"))
            self.assertEqual(len(log.read(2)), 2)

if __name__ == "__main__":
    unittest.main()
