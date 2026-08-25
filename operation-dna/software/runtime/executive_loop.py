"""Integrated event-driven executive loop.
The AI is active; passive systems sense, expose capabilities, and return results.
"""
from dataclasses import dataclass
from typing import Any, Callable
from .attention import AttentionEngine, Event
from .event_log import AIEvent, EventLog
from .objectives import ObjectiveRegistry
from .plan import Plan, resolve_missing, validate_plan
from .capability_bus import CapabilityBus
from .memory import MemoryStore, MemoryItem

@dataclass(frozen=True)
class CycleResult:
    status: str
    goal: str = ""
    executed: tuple[Any, ...] = ()
    missing: tuple[str, ...] = ()

class ExecutiveLoop:
    def __init__(self, bus: CapabilityBus, memory: MemoryStore, attention: AttentionEngine | None = None, objectives: ObjectiveRegistry | None = None, event_log: EventLog | None = None, capability_builder: Callable[[Any], None] | None = None):
        self.bus = bus
        self.memory = memory
        self.attention = attention
        self.objectives = objectives or ObjectiveRegistry()
        self.event_log = event_log
        self.capability_builder = capability_builder

    def run_plan(self, plan: Plan) -> CycleResult:
        validate_plan(plan)
        missing = resolve_missing(plan, {x["name"] for x in self.bus.catalog()})
        if missing:
            if self.capability_builder is not None:
                for request in missing:
                    self.capability_builder(request)
            if self.event_log:
                self.event_log.append(AIEvent(event_type="capability_gap", objective=plan.goal, capabilities=[x.name for x in missing]))
            return CycleResult("capability_gap", plan.goal, (), tuple(x.name for x in missing))
        outputs = tuple(self.bus.invoke(step.capability, **step.arguments) for step in plan.steps)
        self.memory.put(MemoryItem("episodic", plan.goal, {"outputs": outputs}, {"steps": len(plan.steps)}))
        if self.event_log:
            self.event_log.append(AIEvent(event_type="executed", objective=plan.goal, plan={"steps": len(plan.steps)}, result={"outputs": outputs}))
        return CycleResult("executed", plan.goal, outputs, ())

    def process_event(self, event: Event, planner: Callable[[Event, list], Plan]) -> CycleResult:
        """Wake the AI only when attention rules fire, then plan and execute/build."""
        if self.attention is not None and not self.attention.evaluate(event):
            if self.event_log:
                self.event_log.append(AIEvent(event_type="ignored_event", trigger=event.event_type, attention_score=event.importance))
            return CycleResult("ignored")
        plan = planner(event, self.objectives.active())
        return self.run_plan(plan)
