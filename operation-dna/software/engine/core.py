"""Deterministic event-processing primitives for Operation DNA."""
from dataclasses import dataclass, field
from datetime import datetime, timezone
from hashlib import sha256
from typing import Any


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass(frozen=True)
class Event:
    source: str
    title: str
    url: str
    published_at: str
    summary: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def id(self) -> str:
        raw = f"{self.source}|{self.url}|{self.title}|{self.published_at}".encode()
        return sha256(raw).hexdigest()


@dataclass
class Experience:
    event_id: str
    context: dict[str, Any]
    hypothesis: str | None = None
    decision: str | None = None
    action: str | None = None
    outcome: dict[str, Any] = field(default_factory=dict)
    expected_outcome: dict[str, Any] = field(default_factory=dict)
    lessons: list[str] = field(default_factory=list)
    confidence: float = 0.0
    observed_at: str = field(default_factory=utc_now)


def ingest(events: list[Event], seen_ids: set[str] | None = None) -> list[Event]:
    """Deterministically deduplicate observations and update the supplied seen-id set."""
    seen = seen_ids if seen_ids is not None else set()
    fresh: list[Event] = []
    for event in events:
        if event.id not in seen:
            seen.add(event.id)
            fresh.append(event)
    return fresh


def gate_decision(*, authorized: bool, evidence: bool, valid: bool,
                  risk_ok: bool, permitted: bool, reversible: bool) -> bool:
    """Hard execution gate. All required conditions must pass."""
    return all((authorized, evidence, valid, risk_ok, permitted, reversible))
