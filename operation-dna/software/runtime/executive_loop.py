"""Active AI executive loop primitives.
The AI supplies goals/plans; passive systems execute bounded capabilities and return results.
"""
from dataclasses import dataclass
from typing import Any, Callable
from .plan import Plan, resolve_missing
from .capability_bus import CapabilityBus
from .memory import MemoryStore, MemoryItem

@dataclass(frozen=True)
class CycleResult:
    goal: str
    executed: tuple[Any, ...]
    missing: tuple[str, ...]

class ExecutiveLoop:
    def __init__(self, bus: CapabilityBus, memory: MemoryStore, capability_builder: Callable[[Any], None] | None = None):
        self.bus = bus
        self.memory = memory
        self.capability_builder = capability_builder

    def run_plan(self, plan: Plan) -> CycleResult:
        missing = resolve_missing(plan, {x["name"] for x in self.bus.catalog()})
        if missing:
            if self.capability_builder is None:
                return CycleResult(plan.goal, (), tuple(x.name for x in missing))
            for request in missing:
                self.capability_builder(request)
            return CycleResult(plan.goal, (), tuple(x.name for x in missing))
        outputs = []
        for step in plan.steps:
            outputs.append(self.bus.invoke(step.capability, **step.arguments))
        self.memory.put(MemoryItem("episodic", plan.goal, {"outputs": outputs}, {"steps": len(plan.steps)}))
        return CycleResult(plan.goal, tuple(outputs), ())
