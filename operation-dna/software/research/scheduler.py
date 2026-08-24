"""Minimal scheduler contract. Production deployment can map jobs to cron/systemd/GitHub Actions."""
from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass(frozen=True)
class Job:
    name: str
    interval_minutes: int
    enabled: bool = True

class Scheduler:
    def __init__(self):
        self.jobs: dict[str, Job] = {}

    def register(self, job: Job):
        if job.interval_minutes < 5:
            raise ValueError("minimum interval is 5 minutes")
        self.jobs[job.name] = job

    def due(self, job_name: str, last_run: datetime | None, now: datetime | None = None) -> bool:
        job = self.jobs[job_name]
        if not job.enabled:
            return False
        now = now or datetime.now(timezone.utc)
        return last_run is None or (now - last_run).total_seconds() >= job.interval_minutes * 60
