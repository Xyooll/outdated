"""Feed registry and research-source policy."""
from dataclasses import dataclass


@dataclass(frozen=True)
class ResearchFeed:
    id: str
    name: str
    url: str
    category: str
    geography: str
    trust_tier: str = "unverified"
    enabled: bool = False


def enabled_feeds(feeds: list[ResearchFeed]) -> list[ResearchFeed]:
    return [feed for feed in feeds if feed.enabled and feed.url]


def validate_feed(feed: ResearchFeed) -> None:
    if not feed.id or not feed.name or not feed.url:
        raise ValueError("feed requires id, name, and url")
    if feed.trust_tier not in {"unverified", "community", "primary", "institutional"}:
        raise ValueError("invalid trust tier")
