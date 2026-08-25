"""Expected-value-per-cost attention ranking."""
from dataclasses import dataclass

@dataclass(frozen=True)
class AttentionOpportunity:
    name: str
    expected_value: float
    reasoning_cost: float
    urgency: float = 0.0

class AttentionEconomy:
    def rank(self, opportunities: list[AttentionOpportunity], minimum_ratio: float = 0.0) -> list[AttentionOpportunity]:
        def ratio(o): return (o.expected_value + max(0.0, o.urgency)) / max(o.reasoning_cost, 1e-9)
        return sorted((o for o in opportunities if ratio(o) >= minimum_ratio), key=ratio, reverse=True)
