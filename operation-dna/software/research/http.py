"""Small dependency-free JSON HTTP client for public research APIs."""
import json
import urllib.request
import urllib.error


def get_json(url: str, headers: dict[str, str] | None = None, timeout: int = 20):
    request = urllib.request.Request(url, headers=headers or {"User-Agent": "OperationDNA/1.0 research-client"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"HTTP {exc.code} from {url}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Network error from {url}: {exc.reason}") from exc
