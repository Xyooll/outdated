"""RSS ingestion adapter: fetch, normalize, and deduplicate feed items."""
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from hashlib import sha256
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET


@dataclass(frozen=True)
class RSSItem:
    source: str
    title: str
    url: str
    published_at: str | None
    summary: str = ""

    @property
    def id(self) -> str:
        raw = f"{self.source}|{self.url}|{self.title}".encode()
        return sha256(raw).hexdigest()

    def as_event(self) -> dict:
        return {"id": self.id, **asdict(self), "ingested_at": datetime.now(timezone.utc).isoformat()}


def fetch_feed(url: str, timeout: int = 20) -> bytes:
    request = Request(url, headers={"User-Agent": "Operation-DNA/0.1 RSS reader"})
    with urlopen(request, timeout=timeout) as response:
        return response.read()


def parse_feed(xml_bytes: bytes, source: str) -> list[RSSItem]:
    root = ET.fromstring(xml_bytes)
    items = root.findall(".//item")
    if not items:
        # Atom fallback
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        items = root.findall(".//atom:entry", ns)
        return [
            RSSItem(
                source=source,
                title=(item.findtext("atom:title", "", ns) or "").strip(),
                url=(item.find("atom:link", ns).attrib.get("href", "") if item.find("atom:link", ns) is not None else ""),
                published_at=(item.findtext("atom:published", None, ns) or item.findtext("atom:updated", None, ns)),
                summary=(item.findtext("atom:summary", "", ns) or "").strip(),
            ) for item in items
        ]

    return [
        RSSItem(
            source=source,
            title=(item.findtext("title", "") or "").strip(),
            url=(item.findtext("link", "") or "").strip(),
            published_at=(item.findtext("pubDate") or item.findtext("published") or item.findtext("updated")),
            summary=(item.findtext("description", "") or "").strip(),
        ) for item in items
    ]


def collect(url: str, source: str, timeout: int = 20) -> list[dict]:
    """Return normalized event dictionaries; persistence is handled by MemoryStore."""
    return [item.as_event() for item in parse_feed(fetch_feed(url, timeout), source)]
