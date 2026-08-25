import tempfile
import unittest
from pathlib import Path
from software.runtime.attention import AttentionEngine, AttentionRule, Event
from software.runtime.capability_bus import CapabilityBus, CapabilitySpec
from software.runtime.event_log import EventLog
from software.runtime.executive_loop import ExecutiveLoop
from software.runtime.memory import MemoryStore
from software.runtime.objectives import Objective, ObjectiveRegistry
from software.runtime.plan import Plan, PlanStep

class ExecutiveLoopTests(unittest.TestCase):
    def test_event_to_execution_is_logged(self):
        bus = CapabilityBus()
        bus.register(CapabilitySpec("echo", "echo", lambda value: value))
        attention = AttentionEngine()
        attention.register(AttentionRule("important", "test", lambda e: e.data.get("important", False), priority=5))
        objectives = ObjectiveRegistry()
        objectives.set(Objective("test", "test objective"))
        with tempfile.TemporaryDirectory() as tmp:
            log = EventLog(str(Path(tmp) / "events.jsonl"))
            loop = ExecutiveLoop(bus, MemoryStore(), attention, objectives, log)
            result = loop.process_event(Event("test", "signal", {"important": True}), lambda event, objs: Plan("test", (PlanStep("echo", {"value": "ok"}),)))
            self.assertEqual(result.status, "executed")
            self.assertEqual(result.executed, ("ok",))
            self.assertEqual(log.read()[-1]["event_type"], "executed")

    def test_untriggered_event_does_not_execute(self):
        bus = CapabilityBus()
        bus.register(CapabilitySpec("echo", "echo", lambda: "bad"))
        attention = AttentionEngine()
        attention.register(AttentionRule("important", "test", lambda e: False, priority=5))
        loop = ExecutiveLoop(bus, MemoryStore(), attention)
        result = loop.process_event(Event("test", "signal", {}), lambda *_: Plan("x", (PlanStep("echo"),)))
        self.assertEqual(result.status, "ignored")

if __name__ == "__main__":
    unittest.main()
