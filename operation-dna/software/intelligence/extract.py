"""Domain-neutral deterministic extraction helpers.

LLM/entity-resolution adapters can enrich these records later; this layer only
creates candidate mentions and preserves provenance.
"""
import re
from dataclasses import dataclass
from hashlib import sha256


@dataclass(frozen=True)
class Mention:
    text: str
    kind: str
    start: int
    end: int


def candidate_mentions(text: str) -> list[Mention]:
    """Extract conservative candidate names without pretending they are resolved entities."""
    patterns = {
        "ticker": r"\b[A-Z]{1,5}\b",
        "organization": r"\b(?:[A-Z][A-Za-z0-9&.-]*\s+){1,5}(?:Inc\.?|Corp\.?|Corporation|Company|Co\.?|LLC|Ltd\.?)\b",
    }
    found: list[Mention] = []
    for kind, pattern in patterns.items():
        for match in re.finditer(pattern, text):
            value = match.group(0).strip()
            if kind == "ticker" and len(value) == 1:
                continue
            found.append(Mention(value, kind, match.start(), match.end()))
    return sorted(found, key=lambda x: (x.start, x.end))


def mention_id(mention: Mention) -> str:
    return sha256(f"{mention.kind}|{mention.text}".lower().encode()).hexdigest()
