"""End-to-end Xyool cognitive loop with attention, memory, budgets and authority gates."""
from dataclasses import dataclass
from typing import Any, Callable
from .attention import AttentionEngine, Event
from .attention_economy import AttentionEconomy, AttentionOpportunity
from .capabilities import CapabilityRegistry
from .event_log import AIEvent, EventLog
from .memory import MemoryItem, MemoryStore
from .production_readiness import KillSwitch, ResourceBudget

@dataclass(frozen=True)
class CycleResult:
    status: str
    reason: str = ""
    output: Any = None
    attention_score: float = 0.0
    cost: float = 0.0

class CognitiveLoop:
    """One deterministic orchestration boundary; adapters/providers are injected."""
    def __init__(self, attention: AttentionEngine, capabilities: CapabilityRegistry,
                 log: EventLog, memory: MemoryStore, budget: ResourceBudget,
                 kill_switch: KillSwitch, economy: AttentionEconomy | None = None):
        self.attention = attention
        self.capabilities = capabilities
        self.log = log
        self.memory = memory
        self.budget = budget
        self.kill_switch = kill_switch
        self.economy = economy or AttentionEconomy()

    def cycle(self, event: Event, reasoner: Callable[[Event, list[MemoryItem], list[dict[str, Any]]], dict[str, Any]]) -> CycleResult:
        self.kill_switch.check()
        signals = self.attention.evaluate(event)
        if not signals:
            self.log.append(AIEvent(event_type="ignored", trigger=event.event_type, context=event.data))
            return CycleResult("ignored", "no attention signal")
        signal = signals[0]
        opportunity = AttentionOpportunity(signal.rule, max(event.importance, signal.priority), 1.0)
        if not self.economy.rank([opportunity], minimum_ratio=0.0):
            return CycleResult("deferred", "attention budget")
        estimated_cost = next((r.estimated_ai_cost for r in self.attention._rules if r.name == signal.rule), 0.0)
        if not self.budget.allow_cost(estimated_cost):
            self.log.append(AIEvent(event_type="deferred", trigger=event.event_type, attention_score=signal.priority, error="AI cost budget exceeded"))
            return CycleResult("deferred", "AI cost budget exceeded", attention_score=signal.priority, cost=estimated_cost)
        context = self.memory.retrieve_relevant(event.event_type, limit=10)
        decision = reasoner(event, context, self.capabilities.describe())
        capability_name = decision.get("capability")
        if not capability_name:
            self.log.append(AIEvent(event_type="planned", trigger=event.event_type, plan=decision, attention_score=signal.priority))
            return CycleResult("planned", "no capability selected", decision, signal.priority, estimated_cost)
        try:
            capability = self.capabilities.get(capability_name)
        except KeyError:
            self.log.append(AIEvent(event_type="rejected", trigger=event.event_type, plan=decision, error="unknown capability"))
            return CycleResult("rejected", "plan references unknown capability", attention_score=signal.priority, cost=estimated_cost)
        if capability.requires_authorization:
            self.log.append(AIEvent(event_type="authorization_required", trigger=event.event_type, plan=decision, capabilities=[capability_name], human_intervention=True))
            return CycleResult("awaiting_authorization", capability_name, attention_score=signal.priority, cost=estimated_cost)
        self.budget.consume(cost=estimated_cost, action=True)
        try:
            output = self.capabilities.invoke(capability_name, **decision.get("arguments", {}))
        except Exception as exc:
            self.log.append(AIEvent(event_type="error", trigger=event.event_type, plan=decision, capabilities=[capability_name], error=str(exc)))
            return CycleResult("error", str(exc), attention_score=signal.priority, cost=estimated_cost)
        self.log.append(AIEvent(event_type="action", trigger=event.event_type, plan=decision, capabilities=[capability_name], actions=[{"capability": capability_name}], result={"value": output}, cost=estimated_cost))
        self.memory.put(MemoryItem("episodic", event.event_type, {"decision": decision, "output": output}, {"tags": [event.source, capability_name], "importance": signal.priority}))
        return CycleResult("executed", capability_name, output, signal.priority, estimated_cost)
