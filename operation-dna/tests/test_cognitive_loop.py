import tempfile
import unittest
from pathlib import Path
from software.runtime.attention import AttentionEngine, AttentionRule, Event
from software.runtime.capabilities import Capability, CapabilityRegistry
from software.runtime.event_log import EventLog
from software.runtime.memory import MemoryStore
from software.runtime.production_readiness import KillSwitch, ResourceBudget
from software.runtime.loop import CognitiveLoop

class CognitiveLoopTests(unittest.TestCase):
    def make_loop(self, d):
        attention = AttentionEngine()
        attention.register(AttentionRule("market-change", "market", lambda e: e.data.get("price_change", 0) > 1, priority=2, estimated_ai_cost=.1))
        registry = CapabilityRegistry()
        registry.register(Capability("record_signal", "record a simulated signal", lambda symbol=None: {"symbol": symbol}, requires_authorization=False))
        return CognitiveLoop(attention, registry, EventLog(str(Path(d)/"events.jsonl")), MemoryStore(str(Path(d)/"memory.jsonl")), ResourceBudget(max_cost=1, max_actions=5), KillSwitch())

    def test_full_cycle(self):
        with tempfile.TemporaryDirectory() as d:
            loop = self.make_loop(d)
            event = Event("market", "price", {"price_change": 2, "symbol": "TEST"}, importance=1)
            result = loop.cycle(event, lambda e, m, c: {"capability": "record_signal", "arguments": {"symbol": e.data["symbol"]}})
            self.assertEqual(result.status, "executed")
            self.assertEqual(loop.log.read()[-1]["event_type"], "action")
            self.assertEqual(loop.memory.retrieve_relevant("price")[0].content["output"]["symbol"], "TEST")

    def test_unknown_capability_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            loop = self.make_loop(d)
            event = Event("market", "price", {"price_change": 2})
            result = loop.cycle(event, lambda e, m, c: {"capability": "does_not_exist"})
            self.assertEqual(result.status, "rejected")

    def test_kill_switch_blocks_cycle(self):
        with tempfile.TemporaryDirectory() as d:
            loop = self.make_loop(d); loop.kill_switch.stop()
            with self.assertRaises(RuntimeError):
                loop.cycle(Event("market", "price", {"price_change": 2}), lambda *_: {})

if __name__ == "__main__": unittest.main()
