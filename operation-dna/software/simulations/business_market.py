"""Synthetic opportunity marketplace for safe business strategy evaluation."""
from dataclasses import dataclass
import random
from typing import Callable

@dataclass(frozen=True)
class Opportunity:
    value: float
    difficulty: float
    fit: float
    competition: float

@dataclass(frozen=True)
class BusinessResult:
    revenue: float
    costs: float
    profit: float
    opportunities_taken: int

class SyntheticBusinessMarket:
    def __init__(self, seed: int = 42):
        self.rng = random.Random(seed)

    def opportunities(self, count: int = 1000):
        for _ in range(count):
            yield Opportunity(
                value=self.rng.uniform(20, 500),
                difficulty=self.rng.random(),
                fit=self.rng.random(),
                competition=self.rng.random(),
            )


def run_business_strategy(strategy: Callable[[Opportunity], bool], seed: int = 42, opportunities: int = 1000) -> BusinessResult:
    market = SyntheticBusinessMarket(seed)
    revenue = costs = 0.0
    taken = 0
    for opportunity in market.opportunities(opportunities):
        if not strategy(opportunity):
            continue
        taken += 1
        delivery_cost = opportunity.value * (0.15 + 0.45 * opportunity.difficulty)
        revenue += opportunity.value
        costs += delivery_cost
    return BusinessResult(revenue, costs, revenue - costs, taken)


def fit_baseline(opportunity: Opportunity) -> bool:
    return opportunity.fit >= 0.65 and opportunity.competition <= 0.60
