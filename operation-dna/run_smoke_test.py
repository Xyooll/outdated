"""Run a dependency-light end-to-end Xyool smoke test from the operation-dna directory."""
import tempfile
from pathlib import Path
from software.runtime.attention import AttentionEngine, AttentionRule, Event
from software.runtime.capabilities import Capability, CapabilityRegistry
from software.runtime.event_log import EventLog
from software.runtime.memory import MemoryStore
from software.runtime.production_readiness import KillSwitch, ResourceBudget
from software.runtime.loop import CognitiveLoop

def main():
    with tempfile.TemporaryDirectory() as d:
        attention = AttentionEngine()
        attention.register(AttentionRule("signal", "synthetic", lambda e: e.data.get("trigger", False), priority=2, estimated_ai_cost=.1))
        caps = CapabilityRegistry()
        caps.register(Capability("record", "record a synthetic result", lambda value=None: {"value": value}, requires_authorization=False))
        loop = CognitiveLoop(attention, caps, EventLog(str(Path(d)/"events.jsonl")), MemoryStore(str(Path(d)/"memory.jsonl")), ResourceBudget(max_cost=1, max_actions=5), KillSwitch())
        result = loop.cycle(Event("synthetic", "test", {"trigger": True, "value": 42}, importance=1), lambda e, m, c: {"capability": "record", "arguments": {"value": e.data["value"]}})
        assert result.status == "executed", result
        assert loop.log.read()[-1]["event_type"] == "action"
        print("XYOOL SMOKE TEST: PASS")
        print(f"status={result.status} output={result.output}")

if __name__ == "__main__":
    main()
