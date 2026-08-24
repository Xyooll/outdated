"""Simple dependency-free scheduler for perception jobs."""
import time
from dataclasses import dataclass
from typing import Callable

@dataclass(frozen=True)
class Job:
    name: str
    interval_seconds: int
    handler: Callable[[], None]
    last_run: float = 0.0

class Scheduler:
    def __init__(self):
        self.jobs: list[Job] = []

    def add(self, name: str, interval_seconds: int, handler: Callable[[], None]) -> None:
        self.jobs.append(Job(name, interval_seconds, handler))

    def run_once(self) -> list[str]:
        now = time.time()
        ran = []
        updated = []
        for job in self.jobs:
            if now - job.last_run >= job.interval_seconds:
                job.handler()
                ran.append(job.name)
                updated.append(Job(job.name, job.interval_seconds, job.handler, now))
            else:
                updated.append(job)
        self.jobs = updated
        return ran
