"""Low-capital business opportunity evaluation."""
from dataclasses import dataclass


@dataclass(frozen=True)
class BusinessOpportunity:
    name: str
    demand_score: float
    competition_score: float
    startup_cost: float
    expected_monthly_revenue: float
    time_to_first_dollar_days: int
    reversibility: float = 1.0

    @property
    def attractiveness(self) -> float:
        if self.startup_cost <= 0:
            return 0.0
        revenue_efficiency = self.expected_monthly_revenue / self.startup_cost
        speed = 1.0 / max(1, self.time_to_first_dollar_days)
        return max(0.0, self.demand_score) * max(0.0, self.competition_score) * revenue_efficiency * speed * self.reversibility


def rank(opportunities: list[BusinessOpportunity]) -> list[BusinessOpportunity]:
    return sorted(opportunities, key=lambda item: item.attractiveness, reverse=True)
