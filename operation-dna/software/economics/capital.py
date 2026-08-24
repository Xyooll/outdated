"""Capital-allocation primitives shared by business and trading applications."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Opportunity:
    name: str
    capital_required: float
    expected_value: float
    downside: float
    reversible: bool
    evidence_score: float

    @property
    def expected_return_ratio(self) -> float:
        if self.capital_required <= 0:
            return 0.0
        return self.expected_value / self.capital_required


def score(opportunity: Opportunity) -> float:
    """Rank opportunity quality; this is a prioritization signal, not authorization."""
    risk_factor = max(0.0, 1.0 - min(1.0, opportunity.downside))
    reversibility = 1.0 if opportunity.reversible else 0.5
    return opportunity.expected_return_ratio * opportunity.evidence_score * risk_factor * reversibility


def rank(opportunities: list[Opportunity]) -> list[Opportunity]:
    return sorted(opportunities, key=score, reverse=True)
