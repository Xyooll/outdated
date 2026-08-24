"""Capital and experiment risk controls."""
from dataclasses import dataclass


@dataclass(frozen=True)
class RiskBudget:
    capital: float
    max_single_experiment: float
    max_single_trade: float
    max_total_exposure: float

    def validate(self) -> None:
        if min(self.capital, self.max_single_experiment, self.max_single_trade, self.max_total_exposure) < 0:
            raise ValueError("risk budget values cannot be negative")
        if self.max_single_experiment > self.capital:
            raise ValueError("experiment limit exceeds capital")
        if self.max_single_trade > self.capital:
            raise ValueError("trade limit exceeds capital")
        if self.max_total_exposure > self.capital:
            raise ValueError("exposure limit exceeds capital")

    def can_allocate(self, amount: float, current_exposure: float = 0.0, trade: bool = False) -> bool:
        limit = self.max_single_trade if trade else self.max_single_experiment
        return amount >= 0 and amount <= limit and current_exposure + amount <= self.max_total_exposure
