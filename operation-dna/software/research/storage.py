"""Compatibility facade over the canonical Operation DNA MemoryStore."""
from ..storage.store import MemoryStore
from ..storage.migrations import SCHEMA


class ResearchStore:
    """Legacy research API backed by the shared memory database."""
    def __init__(self, path: str = "data/operation_dna.db"):
        self.store = MemoryStore(path)
        self.store.db.executescript(SCHEMA)
        self.store.db.commit()

    @property
    def conn(self):
        return self.store.db

    def save(self, item: dict) -> None:
        if item.get("type") == "opportunity_candidate":
            self.store.put_opportunity(item)
        else:
            self.store.put_event(item)

    def top_opportunities(self, limit: int = 25) -> list[dict]:
        return self.store.top_opportunities(limit)

    def close(self) -> None:
        self.store.close()
