"""Internet research skill for the Xyool orchestrator."""
from __future__ import annotations

from dataclasses import dataclass
import re
from urllib.parse import quote
import requests

@dataclass(frozen=True)
class WebResult:
    query: str
    title: str
    url: str
    snippet: str

class WebSkill:
    """Searches the public web through a simple HTTP backend."""
    def __init__(self, endpoint: str = "https://www.google.com/search", timeout: int = 15):
        self.endpoint = endpoint
        self.timeout = timeout

    def __call__(self, query: str = "", **_: object) -> str:
        if not query.strip():
            return "WEB_ERROR: empty query"
        try:
            r = requests.get(self.endpoint, params={"q": query}, headers={"User-Agent": "Xyool/1.0"}, timeout=self.timeout)
            r.raise_for_status()
            text = re.sub(r"<[^>]+>", " ", r.text)
            text = re.sub(r"\s+", " ", text).strip()
            return f"WEB_SEARCH query={query!r} results={text[:12000]}"
        except requests.RequestException as exc:
            return f"WEB_ERROR {type(exc).__name__}: {exc}"
