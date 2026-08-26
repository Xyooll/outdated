import os
import tempfile
import unittest
from pathlib import Path

from software.integrations.alpaca_paper import PaperAccount
from software.runtime.paper_execution_controller import AuditLog, PaperExecutionController
from software.runtime.production_readiness import KillSwitch, PersistentState, ResourceBudget, RuntimeState


class FakeBroker:
    def __init__(self, blocked=False):
        self.calls = []
        self._account = PaperAccount("paper", "ACTIVE", 100000.0, 400000.0, blocked)

    def account(self):
        self.calls.append(("account",))
        return self._account

    def submit_market_order(self, symbol, qty, side, client_order_id=None):
        self.calls.append(("order", symbol, qty, side, client_order_id))
        return {"id": "paper-order", "status": "accepted"}


class PaperExecutionControllerTests(unittest.TestCase):
    def setUp(self):
        self.old_opt_in = os.environ.get("XYOOL_PAPER_EXECUTE")
        os.environ["XYOOL_PAPER_EXECUTE"] = "YES"

    def tearDown(self):
        if self.old_opt_in is None:
            os.environ.pop("XYOOL_PAPER_EXECUTE", None)
        else:
            os.environ["XYOOL_PAPER_EXECUTE"] = self.old_opt_in

    def make_controller(self, tmp, **kwargs):
        return PaperExecutionController(
            broker=kwargs.pop("broker", FakeBroker()),
            budget=kwargs.pop("budget", ResourceBudget(max_actions=10)),
            kill_switch=kwargs.pop("kill_switch", KillSwitch()),
            state=PersistentState(str(Path(tmp) / "state.json")),
            audit=AuditLog(str(Path(tmp) / "audit.jsonl")),
            execution_enabled=kwargs.pop("execution_enabled", True),
            max_notional=kwargs.pop("max_notional", 100.0),
        )

    def test_success_passes_all_gates_and_audits(self):
        with tempfile.TemporaryDirectory() as tmp:
            broker = FakeBroker()
            result = self.make_controller(tmp, broker=broker).execute_market_order("aapl", 2, "buy", 25)
            self.assertEqual(result.status, "accepted")
            self.assertEqual(broker.calls[1][1:4], ("AAPL", 2, "buy"))
            lines = Path(tmp, "audit.jsonl").read_text(encoding="utf-8").splitlines()
            self.assertEqual(len(lines), 2)
            self.assertIn("paper_order_authorized", lines[0])
            self.assertIn("paper_order_submitted", lines[1])

    def test_disabled_by_default(self):
        with tempfile.TemporaryDirectory() as tmp:
            broker = FakeBroker()
            with self.assertRaisesRegex(RuntimeError, "disabled"):
                self.make_controller(tmp, broker=broker, execution_enabled=False).execute_market_order("AAPL", 1, "buy", 10)
            self.assertEqual(broker.calls, [])

    def test_kill_switch_blocks_before_broker(self):
        with tempfile.TemporaryDirectory() as tmp:
            broker = FakeBroker(); kill = KillSwitch(); kill.stop()
            with self.assertRaisesRegex(RuntimeError, "kill switch"):
                self.make_controller(tmp, broker=broker, kill_switch=kill).execute_market_order("AAPL", 1, "buy", 10)
            self.assertEqual(broker.calls, [])

    def test_pause_blocks_before_broker(self):
        with tempfile.TemporaryDirectory() as tmp:
            broker = FakeBroker(); state = PersistentState(str(Path(tmp) / "state.json"))
            state.save(RuntimeState(paused=True))
            controller = PaperExecutionController(broker=broker, state=state, audit=AuditLog(str(Path(tmp) / "audit.jsonl")), execution_enabled=True)
            with self.assertRaisesRegex(RuntimeError, "paused"):
                controller.execute_market_order("AAPL", 1, "buy", 10)
            self.assertEqual(broker.calls, [])

    def test_notional_limit_blocks_before_broker_and_budget(self):
        with tempfile.TemporaryDirectory() as tmp:
            broker = FakeBroker(); budget = ResourceBudget(max_actions=1)
            controller = self.make_controller(tmp, broker=broker, budget=budget, max_notional=50)
            with self.assertRaisesRegex(RuntimeError, "notional"):
                controller.execute_market_order("AAPL", 3, "buy", 20)
            self.assertEqual(broker.calls, [])
            self.assertEqual(budget.actions, 0)

    def test_budget_blocks_before_order(self):
        with tempfile.TemporaryDirectory() as tmp:
            broker = FakeBroker(); budget = ResourceBudget(max_actions=0)
            controller = self.make_controller(tmp, broker=broker, budget=budget)
            with self.assertRaisesRegex(RuntimeError, "action budget"):
                controller.execute_market_order("AAPL", 1, "buy", 10)
            self.assertEqual(len(broker.calls), 1)  # account eligibility is checked first

    def test_paper_opt_in_is_required(self):
        with tempfile.TemporaryDirectory() as tmp:
            os.environ.pop("XYOOL_PAPER_EXECUTE", None)
            broker = FakeBroker()
            with self.assertRaisesRegex(RuntimeError, "XYOOL_PAPER_EXECUTE"):
                self.make_controller(tmp, broker=broker).execute_market_order("AAPL", 1, "buy", 10)
            self.assertEqual(broker.calls, [])

    def test_blocked_account_cannot_execute(self):
        with tempfile.TemporaryDirectory() as tmp:
            broker = FakeBroker(blocked=True)
            with self.assertRaisesRegex(RuntimeError, "eligible"):
                self.make_controller(tmp, broker=broker).execute_market_order("AAPL", 1, "buy", 10)
            self.assertEqual(len(broker.calls), 1)


if __name__ == "__main__":
    unittest.main()
