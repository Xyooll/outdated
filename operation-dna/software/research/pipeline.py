"""Research ingestion pipeline: adapter -> normalized events -> discovery."""
from .adapters import safe_call
from .discovery import discover
from .market_events import stock_bar_events, crypto_market_events


def process_stock_payload(payload: dict) -> dict:
    events = stock_bar_events(payload)
    signals = [signal for event in events for signal in discover(event.as_dict())]
    return {"events": events, "signals": signals}


def process_crypto_payload(payload: list[dict]) -> dict:
    events = crypto_market_events(payload)
    signals = [signal for event in events for signal in discover(event.as_dict())]
    return {"events": events, "signals": signals}


def run(provider: str, loader, *args, **kwargs):
    """Execute a read-only adapter and return structured success/failure data."""
    result = safe_call(provider, loader, *args, **kwargs)
    if not result.success:
        return result
    return result
