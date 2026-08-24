"""Connect RSS perception to deterministic event storage."""
from .rss import collect
from ..storage.store import MemoryStore


def ingest_feed(store: MemoryStore, url: str, source: str) -> int:
    events = collect(url, source)
    count = 0
    for event in events:
        store.put_event(event)
        count += 1
    return count
