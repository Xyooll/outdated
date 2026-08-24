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
        if not job.name.strip():
            raise ValueError("job name is required")
        if job.interval_minutes < 5:
            raise ValueError("minimum interval is 5 minutes")
        self.jobs[job.name] = job

    def due(self, job_name: str, last_run: datetime | None, now: datetime | None = None) -> bool:
        if job_name not in self.jobs:
            raise KeyError(f"unknown job: {job_name}")
        job = self.jobs[job_name]
        if not job.enabled:
            return False
        now = now or datetime.now(timezone.utc)
        if now.tzinfo is None:
            now = now.replace(tzinfo=timezone.utc)
        if last_run is None:
            return True
        if last_run.tzinfo is None:
            last_run = last_run.replace(tzinfo=timezone.utc)
        return (now - last_run).total_seconds() >= job.interval_minutes * 60
