"""Persistent research runner backed by the canonical memory database."""
from .pipeline import process_events
from .storage import ResearchStore


def run_events(events, db_path="data/operation_dna.db"):
    store = ResearchStore(db_path)
    try:
        result = process_events(events, persist=store.save)
        return {
            "ingested": result["ingested"],
            "unique": result["unique"],
            "candidate_count": len(result["candidates"]),
            "top": store.top_opportunities(25),
        }
    finally:
        store.close()
