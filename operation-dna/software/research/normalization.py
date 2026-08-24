"""Canonical event model shared by RSS, SEC, market, and crypto adapters."""
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import hashlib


@dataclass(frozen=True)
class ResearchEvent:
    source: str
    source_id: str
    title: str
    summary: str
    url: str = ""
    published_at: str = ""
    category: str = "research"
    entity: str = ""
    evidence_score: float = 0.0

    @property
    def event_id(self) -> str:
        raw = f"{self.source}|{self.source_id}|{self.title}|{self.published_at}".encode()
        return hashlib.sha256(raw).hexdigest()[:24]

    def as_dict(self) -> dict:
        value = asdict(self)
        value["event_id"] = self.event_id
        return value


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()
