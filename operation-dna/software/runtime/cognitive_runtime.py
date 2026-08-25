"""Central cognitive orchestration: observe -> attend -> reason -> act -> learn."""
from dataclasses import dataclass
from typing import Any, Callable
from .attention import AttentionEngine, Event
from .capabilities import CapabilityRegistry
from .event_log import AIEvent, EventLog
from .objectives import ObjectiveRegistry

@dataclass(frozen=True)
class CognitiveResult:
    status: str
    reason: str = ""
    output: Any = None

class CognitiveRuntime:
    def __init__(self, attention: AttentionEngine, objectives: ObjectiveRegistry, capabilities: CapabilityRegistry, log: EventLog):
        self.attention, self.objectives, self.capabilities, self.log = attention, objectives, capabilities, log

    def cycle(self, event: Event, reasoner: Callable[[Event, list, list], dict[str, Any]], authorizer: Callable[[str], bool] | None = None) -> CognitiveResult:
        signals = self.attention.evaluate(event)
        if not signals:
            self.log.append(AIEvent(event_type="ignored", trigger=event.event_type))
            return CognitiveResult("ignored", "no attention signal")
        decision = reasoner(event, self.objectives.active(), self.capabilities.describe())
        capability = decision.get("capability")
        if not capability or not self.capabilities.get(capability):
            return CognitiveResult("rejected", "plan references unknown capability")
        cap = self.capabilities.get(capability)
        if cap.requires_authorization and (authorizer is None or not authorizer(capability)):
            self.log.append(AIEvent(event_type="authorization_required", trigger=event.event_type, capabilities=[capability]))
            return CognitiveResult("awaiting_authorization", capability)
        output = self.capabilities.invoke(capability, **decision.get("inputs", {}))
        self.log.append(AIEvent(event_type="action", trigger=event.event_type, actions=[{"capability": capability}], result={"value": output}))
        return CognitiveResult("executed", capability, output)
