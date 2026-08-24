"""Outcome tracking and calibration for opportunity predictions."""
from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class Forecast:
    forecast_id: str
    opportunity_key: str
    predicted_score: float
    predicted_upside: float
    predicted_downside: float
    created_at: str


@dataclass(frozen=True)
class Outcome:
    forecast_id: str
    realized_return: float
    realized_cost: float
    observed_at: str


def evaluate(forecast: Forecast, outcome: Outcome) -> dict:
    error = outcome.realized_return - forecast.predicted_upside
    direction_correct = (forecast.predicted_upside > 0) == (outcome.realized_return > 0)
    return {
        "forecast_id": forecast.forecast_id,
        "opportunity_key": forecast.opportunity_key,
        "error": error,
        "absolute_error": abs(error),
        "direction_correct": direction_correct,
        "realized_return": outcome.realized_return,
        "realized_cost": outcome.realized_cost,
        "evaluated_at": datetime.now(timezone.utc).isoformat(),
    }


def calibration(results: list[dict]) -> dict:
    if not results:
        return {"samples": 0, "direction_accuracy": 0.0, "mean_absolute_error": 0.0}
    return {
        "samples": len(results),
        "direction_accuracy": sum(bool(r["direction_correct"]) for r in results) / len(results),
        "mean_absolute_error": sum(float(r["absolute_error"]) for r in results) / len(results),
    }
