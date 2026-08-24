"""Environment-driven feed registry.

Credentials and URLs are configuration, never source-controlled secrets.
"""
import os


def configured_feeds() -> list[str]:
    raw = os.getenv("XYOOL_FEEDS", "")
    return [item.strip() for item in raw.split(",") if item.strip()]


def require_any_feed() -> list[str]:
    feeds = configured_feeds()
    if not feeds:
        raise RuntimeError("No research feeds configured; set XYOOL_FEEDS")
    return feeds
