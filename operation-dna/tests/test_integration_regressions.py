import sqlite3
import unittest

from operation_dna.software.research.normalization import ResearchEvent
from operation_dna.software.research.storage import ResearchStore
from operation_dna.software.safety.policy import ActionRequest, Policy, evaluate


class IntegrationRegressionTests(unittest.TestCase):
    def test_canonical_event_can_persist(self):
        event = ResearchEvent("test", "1", "title", "summary", published_at="2026-01-01T00:00:00Z")
        with self.subTest("research store"):
            store = ResearchStore(":memory:")
            try:
                store.save(event.as_dict())
                row = store.conn.execute("SELECT event_id, published_at FROM events").fetchone()
                self.assertEqual(row[0], event.event_id)
                self.assertEqual(row[1], event.published_at)
            finally:
                store.close()

    def test_opportunities_are_upserted(self):
        store = ResearchStore(":memory:")
        try:
            item = {
                "type": "opportunity_candidate",
                "name": "Test",
                "domain": "business",
                "score": 0.8,
                "source_ids": ["s1"],
            }
            store.save(item)
            store.save({**item, "score": 0.9})
            count = store.conn.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
            self.assertEqual(count, 1)
            self.assertEqual(store.top_opportunities(1)[0]["score"], 0.9)
        finally:
            store.close()

    def test_policy_uses_configured_evidence_threshold(self):
        policy = Policy(minimum_evidence_score=0.8)
        request = ActionRequest(True, 0.7, 0.1, True, True)
        allowed, failures = evaluate(policy, request)
        self.assertFalse(allowed)
        self.assertIn("evidence", failures)


if __name__ == "__main__":
    unittest.main()
