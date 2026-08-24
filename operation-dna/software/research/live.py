"""Live RSS research entrypoint.

Configured feeds are read from XYOOL_FEEDS as a comma-separated list. Each
source is isolated so one outage cannot stop the research cycle.
"""
import os
from .rss import fetch
from .runner import run_once


def main() -> int:
    urls = [u.strip() for u in os.getenv("XYOOL_FEEDS", "").split(",") if u.strip()]
    if not urls:
        print("No XYOOL_FEEDS configured; nothing to ingest.")
        return 0
    result = run_once((lambda url=url: fetch(url) for url in urls))
    print({
        "fetched": result.fetched,
        "ingested": result.ingested,
        "unique": result.unique,
        "candidates": result.candidates,
        "top": result.top[:10],
    })
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
