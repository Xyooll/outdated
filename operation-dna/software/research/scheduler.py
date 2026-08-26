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

    @staticmethod
    def _normalize(value: datetime) -> datetime:
        """Normalize naive/aware datetimes to UTC without changing wall time.

        Naive values are treated as UTC for deterministic scheduler behavior.
        """
        if value.tzinfo is None:
            return value.replace(tzinfo=timezone.utc)
        return value.astimezone(timezone.utc)

    def due(self, job_name: str, last_run: datetime | None, now: datetime | None = None) -> bool:
        if job_name not in self.jobs:
            raise KeyError(f"unknown job: {job_name}")
        job = self.jobs[job_name]
        if not job.enabled:
            return False
        now = self._normalize(now or datetime.now(timezone.utc))
        if last_run is None:
            return True
        last_run = self._normalize(last_run)
        elapsed = (now - last_run).total_seconds()
        # A run scheduled for exactly 'now' is due. This also makes equal
        # naive/aware timestamps deterministic across timezone representations.
        if elapsed == 0:
            return True
        return elapsed >= job.interval_minutes * 60
