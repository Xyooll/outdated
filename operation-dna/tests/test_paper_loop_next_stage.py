"""Tests for reconciliation and continuous paper loop plumbing."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock

from software.runtime.paper_reconciliation import reconcile_positions
from software.runtime.trade_outcome_tracker import TradeOutcomeTracker


class PaperLoopNextStageTests(unittest.TestCase):
    def test_reconciliation_detects_mismatch(self):
        class Position:
            symbol = "AAPL"
            qty = 0.1
        ledger = Mock()
        ledger.positions = {"AAPL": Position()}
        broker = Mock()
        broker._request.return_value = [{"symbol": "AAPL", "qty": "0.2"}]
        result = reconcile_positions(broker, ledger)
        self.assertFalse(result["in_sync"])
        self.assertEqual(result["discrepancies"][0]["broker_qty"], 0.2)

    def test_reconciliation_accepts_match(self):
        class Position:
            symbol = "AAPL"
            qty = 0.1
        ledger = Mock()
        ledger.positions = {"AAPL": Position()}
        broker = Mock()
        broker._request.return_value = [{"symbol": "AAPL", "qty": "0.1"}]
        self.assertTrue(reconcile_positions(broker, ledger)["in_sync"])

    def test_outcome_tracker_records_pnl(self):
        with tempfile.TemporaryDirectory() as tmp:
            tracker = TradeOutcomeTracker(str(Path(tmp) / "outcomes.jsonl"))
            tracker.record(client_order_id="x", symbol="AAPL", side="buy", qty=0.1,
                           entry_price=100, exit_price=110, reason="take_profit")
            self.assertEqual(tracker.summary()["total_pnl"], 1.0)
            self.assertEqual(tracker.summary()["wins"], 1)


if __name__ == "__main__":
    unittest.main()
