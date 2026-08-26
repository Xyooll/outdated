"""Convert market API payloads into canonical research events."""
import hashlib
import json

from .normalization import ResearchEvent, now_iso


def stock_bar_events(payload: dict, source: str = "alpaca") -> list[ResearchEvent]:
    events = []
    for symbol, bars in payload.get("bars", {}).items():
        for bar in bars:
            ts = bar.get("t", now_iso())
            events.append(ResearchEvent(
                source=source,
                source_id=f"{symbol}:{ts}",
                title=f"{symbol} market bar",
                summary=f"OHLCV {bar.get('o')} {bar.get('h')} {bar.get('l')} {bar.get('c')} volume {bar.get('v')}",
                published_at=ts,
                category="market_data",
                entity=symbol,
                evidence_score=1.0,
            ))
    return events


def crypto_market_events(payload: list[dict], source: str = "coingecko") -> list[ResearchEvent]:
    """Normalize snapshots while making each materially different snapshot identifiable.

    Wall-clock time is intentionally not used as the identity source: two snapshots can
    legitimately be fetched in the same timestamp resolution. The stable source fields
    plus a canonical payload fingerprint make price/volume/cap changes produce new IDs.
    """
    fetched_at = now_iso()
    events = []
    for row in payload:
        identity = {
            "id": row.get("id", row.get("symbol", "unknown")),
            "symbol": row.get("symbol", ""),
            "current_price": row.get("current_price"),
            "market_cap": row.get("market_cap"),
            "total_volume": row.get("total_volume"),
            "price_change_percentage_24h": row.get("price_change_percentage_24h"),
        }
        fingerprint = hashlib.sha256(
            json.dumps(identity, sort_keys=True, separators=(",", ":"), default=str).encode("utf-8")
        ).hexdigest()[:16]
        events.append(ResearchEvent(
            source=source,
            source_id=f"{identity['id']}:{fingerprint}",
            title=f"Crypto market: {row.get('name', row.get('symbol', 'unknown'))}",
            summary=f"Price {row.get('current_price')} market cap {row.get('market_cap')} 24h volume {row.get('total_volume')}",
            published_at=fetched_at,
            category="crypto_market",
            entity=row.get("symbol", ""),
            evidence_score=0.9,
        ))
    return events
