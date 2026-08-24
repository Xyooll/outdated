"""Research ingestion pipeline: adapter -> normalize -> dedupe -> discover -> rank -> persist."""
from .adapters import safe_call
from .discovery import discover
from .market_events import stock_bar_events, crypto_market_events
from ..economics.scanners import scan_business, scan_investments, scan_trading


def _key(event) -> str:
    if hasattr(event, "event_id"):
        return event.event_id
    return str(event.get("event_id") or event.get("id") or f"{event.get('source')}:{event.get('title')}:{event.get('timestamp')}")


def dedupe(events):
    seen, result = set(), []
    for event in events:
        key = _key(event)
        if key not in seen:
            seen.add(key)
            result.append(event)
    return result


def process_stock_payload(payload: dict) -> dict:
    events = stock_bar_events(payload)
    return process_events(events)


def process_crypto_payload(payload: list[dict]) -> dict:
    events = crypto_market_events(payload)
    return process_events(events)


def process_events(events, persist=None) -> dict:
    unique = dedupe(events)
    raw = [e.as_dict() if hasattr(e, "as_dict") else e for e in unique]
    signals = [signal for event in raw for signal in discover(event)]
    candidates = []
    for scanner in (scan_business, scan_investments, scan_trading):
        candidates.extend(scanner(raw))
    candidates.sort(key=lambda c: c.risk_adjusted_efficiency, reverse=True)
    if persist:
        for event in raw:
            persist(event)
        for candidate in candidates:
            persist({"type": "opportunity_candidate", "name": candidate.name, "domain": candidate.domain, "score": candidate.risk_adjusted_efficiency, "source_ids": list(candidate.source_ids)})
    return {"ingested": len(events), "unique": len(unique), "signals": signals, "candidates": candidates}


def run(provider: str, loader, *args, **kwargs):
    """Execute a read-only adapter and return structured success/failure data."""
    return safe_call(provider, loader, *args, **kwargs)
