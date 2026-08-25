"""Human-authority control surface primitives."""
from dataclasses import dataclass, field

@dataclass
class ControlState:
    paused: bool = False
    allowed_domains: set[str] = field(default_factory=set)
    blocked_capabilities: set[str] = field(default_factory=set)
    require_human_for_risk: bool = True

class HumanControl:
    def __init__(self): self.state = ControlState()
    def pause(self): self.state.paused = True
    def resume(self): self.state.paused = False
    def allow_domain(self, name): self.state.allowed_domains.add(name)
    def block_capability(self, name): self.state.blocked_capabilities.add(name)
    def authorize(self, capability, risk_class="low") -> bool:
        if self.state.paused or capability in self.state.blocked_capabilities: return False
        return not (self.state.require_human_for_risk and risk_class not in {"low", "none"})
