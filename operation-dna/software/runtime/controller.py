"""Master closed-loop controller for Operation DNA."""
from dataclasses import dataclass
from typing import Callable, Iterable
from software.research.runner import run_events, RunResult
from software.economics.learning import Forecast, Outcome, evaluate

@dataclass(frozen=True)
class CycleReport:
    cycle_id: str
    research: RunResult
    forecasts: int
    evaluated: int
    state: str

class MasterController:
    """Coordinates sensing, memory and learning; no live-money execution."""
    def __init__(self, db_path: str = "data/operation_dna.db"):
        self.db_path = db_path
        self.forecasts: dict[str, Forecast] = {}
        self.results: list[dict] = []

    def sense(self, fetchers: Iterable[Callable[[], Iterable[dict]]]) -> RunResult:
        from software.research.runner import run_once
        return run_once(fetchers, db_path=self.db_path)

    def ingest(self, events: Iterable[dict]) -> RunResult:
        return run_events(events, db_path=self.db_path)

    def record_forecast(self, forecast: Forecast) -> None:
        if forecast.forecast_id in self.forecasts:
            raise ValueError(f"forecast already exists: {forecast.forecast_id}")
        self.forecasts[forecast.forecast_id] = forecast

    def observe(self, outcome: Outcome) -> dict:
        forecast = self.forecasts.get(outcome.forecast_id)
        if forecast is None:
            raise KeyError(f"unknown forecast: {outcome.forecast_id}")
        result = evaluate(forecast, outcome)
        self.results.append(result)
        return result

    def cycle(self, cycle_id: str, events: Iterable[dict] = ()) -> CycleReport:
        research = self.ingest(events)
        return CycleReport(cycle_id, research, len(self.forecasts), len(self.results), "completed")
