import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock

from software.integrations.alpaca_paper import PaperAccount
from software.runtime.paper_execution_controller import AuditLog, PaperExecutionController
from software.runtime.production_readiness import KillSwitch, PersistentState, ResourceBudget, RuntimeState


class PaperExecutionControllerTests(unittest.TestCase):
    def setUp(self):
        self.previous = os.environ.get("XYOOL_PAPER_EXECUTE")
        os.environ["XYOOL_PAPER_EXECUTE"] = "YES"

    def tearDown(self):
        if self.previous is None:
            os.environ.pop("XYOOL_PAPER_EXECUTE", None)
        else:
            os.environ["XYOOL_PAPER_EXECUTE"] = self.previous

    def controller(self, broker=None, **kwargs):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        state = PersistentState(str(root / "state.json"))
        audit = AuditLog(str(root / "execution.jsonl"))
        broker = broker or Mock()
        broker.account.return_value = PaperAccount("acct", "ACTIVE", 100000.0, 400000.0, False)
        broker.submit_market_order.return_value = {"id": "order-1", "status": "accepted"}
        return PaperExecutionController(
            broker=broker,
            budget=ResourceBudget(max_cost=1.0, max_actions=1, max_experiments=10),
            state=state,
            audit=audit,
            **kwargs,
        ), broker, state, audit

    def test_disabled_by_default(self):
        c, broker, _, _ = self.controller(execution_enabled=False)
        with self.assertRaisesRegex(RuntimeError, "disabled"):
            c.execute_market_order("AAPL", 1, "buy", 25)
        broker.account.assert_not_called()

    def test_requires_environment_opt_in(self):
        os.environ["XYOOL_PAPER_EXECUTE"] = "NO"
        c, broker, _, _ = self.controller(execution_enabled=True)
        with self.assertRaisesRegex(RuntimeError, "XYOOL_PAPER_EXECUTE"):
            c.execute_market_order("AAPL", 1, "buy", 25)
        broker.account.assert_not_called()

    def test_kill_switch_and_pause_block_before_broker(self):
        c, broker, state, _ = self.controller(execution_enabled=True)
        c.kill_switch.stop()
        with self.assertRaisesRegex(RuntimeError, "kill switch"):
            c.execute_market_order("AAPL", 1, "buy", 25)
        c.kill_switch.reset()
        state.save(RuntimeState(paused=True))
        with self.assertRaisesRegex(RuntimeError, "paused"):
            c.execute_market_order("AAPL", 1, "buy", 25)
        broker.account.assert_not_called()

    def test_notional_and_account_gates(self):
        c, broker, _, _ = self.controller(execution_enabled=True, max_notional=100)
        with self.assertRaisesRegex(RuntimeError, "exceeds limit"):
            c.execute_market_order("AAPL", 5, "buy", 25)
        broker.account.return_value = PaperAccount("acct", "ACTIVE", 100000.0, 400000.0, True)
        with self.assertRaisesRegex(RuntimeError, "not eligible"):
            c.execute_market_order("AAPL", 1, "buy", 25)
        broker.submit_market_order.assert_not_called()

    def test_success_audits_and_consumes_action_budget(self):
        c, broker, _, audit = self.controller(execution_enabled=True)
        result = c.execute_market_order("AAPL", 1, "buy", 25)
        self.assertEqual(result.status, "accepted")
        self.assertEqual(c.budget.actions, 1)
        broker.submit_market_order.assert_called_once()
        lines = audit.path.read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(lines), 2)
        self.assertIn("paper_order_authorized", lines[0])
        self.assertIn("paper_order_submitted", lines[1])

    def test_broker_failure_is_audited(self):
        c, broker, _, audit = self.controller(execution_enabled=True)
        broker.submit_market_order.side_effect = RuntimeError("broker failure")
        with self.assertRaisesRegex(RuntimeError, "broker failure"):
            c.execute_market_order("AAPL", 1, "buy", 25)
        lines = audit.path.read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(lines), 2)
        self.assertIn("paper_order_authorized", lines[0])
        self.assertIn("paper_order_failed", lines[1])


if __name__ == "__main__":
    unittest.main()
