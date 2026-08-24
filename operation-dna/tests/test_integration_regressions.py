import unittest
from datetime import datetime, timezone, timedelta

from operation_dna.software.research.normalization import ResearchEvent
from operation_dna.software.research.storage import ResearchStore
from operation_dna.software.research.scheduler import Scheduler, Job
from operation_dna.software.safety.policy import ActionRequest, Policy, evaluate
from operation_dna.software.intelligence.evidence import Evidence, confidence
from operation_dna.software.economics.scanners import scan_trading


class IntegrationRegressionTests(unittest.TestCase):
    def test_canonical_event_can_persist(self):
        event = ResearchEvent("test", "1", "title", "summary", published_at="2026-01-01T00:00:00Z")
        store = ResearchStore(":memory:")
        try:
            store.save(event.as_dict())
            row = store.conn.execute("SELECT id, published_at, event_type FROM events").fetchone()
            self.assertEqual(row[0], event.event_id)
            self.assertEqual(row[1], event.published_at)
            self.assertEqual(row[2], "research")
        finally:
            store.close()

    def test_opportunities_are_upserted_across_source_changes(self):
        store = ResearchStore(":memory:")
        try:
            item = {"type": "opportunity_candidate", "name": "Test", "domain": "business", "score": 0.8, "source_ids": ["s1"]}
            store.save(item)
            store.save({**item, "score": 0.9, "source_ids": ["s2", "s3"]})
            count = store.conn.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
            self.assertEqual(count, 1)
            self.assertEqual(store.top_opportunities(1)[0]["score"], 0.9)
        finally:
            store.close()

    def test_policy_uses_configured_evidence_threshold(self):
        policy = Policy(minimum_evidence_score=0.8, require_capability=False)
        request = ActionRequest(True, 0.7, 0.1, True, True, True)
        allowed, failures = evaluate(policy, request)
        self.assertFalse(allowed)
        self.assertIn("evidence", failures)

    def test_correlated_evidence_does_not_count_twice(self):
        one = Evidence("source-a", "e1", .8, .8, .8, .8)
        duplicate = Evidence("source-a", "e2", .8, .8, .8, .8)
        self.assertEqual(confidence([one, duplicate]), confidence([one]))

    def test_trading_scanner_requires_confluence(self):
        self.assertEqual(scan_trading([{"title": "high volume", "summary": "volume increased"}]), [])
        candidates = scan_trading([{"title": "breakout momentum", "summary": "volume confirmed"}])
        self.assertTrue(candidates)

    def test_scheduler_handles_naive_and_aware_datetimes(self):
        scheduler = Scheduler()
        scheduler.register(Job("research", 5))
        now = datetime.now(timezone.utc)
        self.assertTrue(scheduler.due("research", now.replace(tzinfo=None), now))
        self.assertFalse(scheduler.due("research", now - timedelta(minutes=4), now))


if __name__ == "__main__":
    unittest.main()
