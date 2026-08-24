"""Research ingestion pipeline: adapter -> normalize -> dedupe -> discover -> rank -> persist."""
from .adapters import safe_call
from .discovery import discover
from .market_events import stock_bar_events, crypto_market_events
from ..economics.scanners import scan_business, scan_investments, scan_trading


def _key(event) -> str:
    if hasattr(event, "event_id"):
        return event.event_id
    return str(event.get("event_id") or event.get("id") or f"{event.get('source')}:{event.get('title')}:{event.get('published_at') or event.get('timestamp')}")


def dedupe(events):
    seen, result = set(), []
    for event in events:
        key = _key(event)
        if key not in seen:
            seen.add(key)
            result.append(event)
    return result


def _with_provenance(event: dict) -> dict:
    """Ensure downstream scanners have stable source provenance."""
    value = dict(event)
    source = str(value.get("source", "unknown"))
    source_id = value.get("source_id") or value.get("event_id") or value.get("id")
    value["source_ids"] = [f"{source}:{source_id}"] if source_id else [source]
    if "evidence_score" not in value:
        value["evidence_score"] = 0.0
    return value


def process_stock_payload(payload: dict, persist=None) -> dict:
    return process_events(stock_bar_events(payload), persist)


def process_crypto_payload(payload: list[dict], persist=None) -> dict:
    return process_events(crypto_market_events(payload), persist)


def process_events(events, persist=None) -> dict:
    unique = dedupe(events)
    raw = [_with_provenance(e.as_dict() if hasattr(e, "as_dict") else e) for e in unique]
    signals = [signal for event in raw for signal in discover(event)]
    candidates = []
    for scanner in (scan_business, scan_investments, scan_trading):
        candidates.extend(scanner(raw))
    candidates.sort(key=lambda c: c.risk_adjusted_efficiency, reverse=True)
    if persist:
        for event in raw:
            persist(event)
        for candidate in candidates:
            persist({"type": "opportunity_candidate", "name": candidate.name, "domain": candidate.domain, "thesis": candidate.thesis, "score": candidate.risk_adjusted_efficiency, "evidence_score": candidate.evidence_score, "source_ids": list(candidate.source_ids)})
    return {"ingested": len(events), "unique": len(unique), "signals": signals, "candidates": candidates}


def run(provider: str, loader, *args, **kwargs):
    return safe_call(provider, loader, *args, **kwargs)


if __name__ == "__main__":
    # Safe CI health check: no network calls and no external actions.
    result = process_events([])
    print({"status": "ok", "ingested": result["ingested"], "candidates": len(result["candidates"])})
