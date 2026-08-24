"""Continuous research ingestion loop backed by canonical memory."""
from dataclasses import dataclass
from typing import Callable, Iterable
from .pipeline import process_events
from .storage import ResearchStore


@dataclass(frozen=True)
class RunResult:
    fetched: int
    ingested: int
    unique: int
    candidates: int
    top: list[dict]


def run_events(events: Iterable[dict], db_path: str = "data/operation_dna.db") -> RunResult:
    store = ResearchStore(db_path)
    try:
        result = process_events(list(events), persist=store.save)
        return RunResult(
            fetched=result["ingested"],
            ingested=result["ingested"],
            unique=result["unique"],
            candidates=len(result["candidates"]),
            top=store.top_opportunities(25),
        )
    finally:
        store.close()


def run_once(fetchers: Iterable[Callable[[], Iterable[dict]]], db_path: str = "data/operation_dna.db") -> RunResult:
    raw: list[dict] = []
    for fetch in fetchers:
        try:
            raw.extend(list(fetch()))
        except Exception:
            # One unavailable source must not stop all other research sources.
            continue
    return run_events(raw, db_path=db_path)
