"""Route reasoning work between local and remote AI providers by cost/complexity."""
from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class ModelPolicy:
    local_max_complexity: float = 0.35
    remote_budget: float = 1.0

class ModelRouter:
    def __init__(self, local_provider: Any, remote_provider: Any | None = None, policy: ModelPolicy | None = None):
        self.local = local_provider
        self.remote = remote_provider
        self.policy = policy or ModelPolicy()

    def reason(self, prompt: str, context: list[dict[str, Any]], complexity: float = 0.0, estimated_remote_cost: float = 0.0) -> dict[str, Any]:
        if complexity <= self.policy.local_max_complexity or self.remote is None or estimated_remote_cost > self.policy.remote_budget:
            result = self.local.reason(prompt, context)
            result.setdefault("provider", "local")
            return result
        result = self.remote.reason(prompt, context)
        result.setdefault("provider", "remote")
        return result
