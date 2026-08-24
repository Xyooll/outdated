"""Small RSS/Atom adapter using the standard library."""
import urllib.request
import xml.etree.ElementTree as ET


def fetch(url: str, timeout: int = 20) -> list[dict]:
    request = urllib.request.Request(url, headers={"User-Agent": "Xyool-Research/1.0"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        payload = response.read()
    root = ET.fromstring(payload)
    items = []
    for item in root.findall(".//item") + root.findall(".//{http://www.w3.org/2005/Atom}entry"):
        def text(tag: str) -> str:
            node = item.find(tag)
            return (node.text or "").strip() if node is not None else ""
        title = text("title") or text("{http://www.w3.org/2005/Atom}title")
        link = text("link") or text("{http://www.w3.org/2005/Atom}link")
        summary = text("description") or text("summary") or text("{http://www.w3.org/2005/Atom}summary")
        published = text("pubDate") or text("published") or text("{http://www.w3.org/2005/Atom}updated")
        if title:
            items.append({"source": url, "title": title, "url": link, "summary": summary, "published_at": published, "event_type": "rss"})
    return items
