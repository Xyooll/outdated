"""Decompose engineering goals and plan independent capabilities in parallel."""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from typing import Iterable

from .ai_provider import AIProvider, EngineeringPlan


@dataclass(frozen=True)
class CapabilityTask:
    goal: str
    index: int


@dataclass(frozen=True)
class OrchestrationPlan:
    goal: str
    tasks: tuple[CapabilityTask, ...]
    plans: tuple[EngineeringPlan, ...]


class CapabilityOrchestrator:
    """Fast planner: independent subgoals are planned concurrently.

    It deliberately parallelizes reasoning/planning, not filesystem mutation.
    Actual builds can therefore remain isolated and deterministic.
    """

    def __init__(self, provider: AIProvider, max_workers: int = 4):
        if max_workers < 1:
            raise ValueError("max_workers must be >= 1")
        self.provider = provider
        self.max_workers = max_workers

    def decompose(self, goal: str) -> tuple[CapabilityTask, ...]:
        if not goal or not goal.strip():
            raise ValueError("goal is required")
        text = goal.strip()
        parts = [p.strip() for p in text.replace(" and ", "|").split("|") if p.strip()]
        if len(parts) == 1:
            return (CapabilityTask(text, 0),)
        return tuple(CapabilityTask(part, i) for i, part in enumerate(parts))

    def plan(self, goal: str) -> OrchestrationPlan:
        tasks = self.decompose(goal)
        with ThreadPoolExecutor(max_workers=min(self.max_workers, len(tasks))) as pool:
            plans = tuple(pool.map(lambda task: self.provider.plan(task.goal), tasks))
        return OrchestrationPlan(goal, tasks, plans)
