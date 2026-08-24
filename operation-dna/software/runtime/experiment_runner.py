"""Sandbox-oriented experiment runner.

Only approved local callables are accepted. External execution adapters are
intentionally absent until explicitly configured and authorized.
"""
from dataclasses import dataclass
from typing import Callable, Any


@dataclass(frozen=True)
class ExperimentRun:
    name: str
    status: str
    result: Any = None
    error: str | None = None


def run(name: str, fn: Callable[[], Any], *, enabled: bool = False) -> ExperimentRun:
    if not enabled:
        return ExperimentRun(name, "blocked", error="experiments are disabled")
    try:
        return ExperimentRun(name, "completed", result=fn())
    except Exception as exc:  # deliberate boundary: convert experiment failure to data
        return ExperimentRun(name, "failed", error=str(exc))
