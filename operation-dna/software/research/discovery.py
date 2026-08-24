"""Turn normalized perception events into ranked research opportunity signals.

This layer does not claim that an opportunity is real. It creates candidates for
human/AI validation using transparent, tunable heuristics.
"""
from dataclasses import dataclass
from ..economics.opportunities import OpportunitySignal


@dataclass(frozen=True)
class DiscoveryRule:
    category: str
    keywords: tuple[str, ...]
    base_evidence: float = 0.5


DEFAULT_RULES = (
    DiscoveryRule("business", ("contract", "backlog", "launch", "partnership", "funding"), 0.45),
    DiscoveryRule("infrastructure", ("shortage", "capacity", "bottleneck", "supply chain"), 0.50),
    DiscoveryRule("technology", ("breakthrough", "deployment", "adoption", "production"), 0.40),
)


def discover(event: dict, rules=DEFAULT_RULES) -> list[OpportunitySignal]:
    text = f"{event.get('title', '')} {event.get('summary', '')}".lower()
    results = []
    for rule in rules:
        hits = sum(1 for keyword in rule.keywords if keyword in text)
        if not hits:
            continue
        evidence = min(1.0, rule.base_evidence + 0.1 * hits)
        results.append(OpportunitySignal(
            name=event.get("title", "untitled"),
            category=rule.category,
            evidence_score=evidence,
            expected_upside=0.0,
            capital_required=0.0,
            downside=0.5,
            reversible=True,
            time_to_test_days=30,
        ))
    return results
