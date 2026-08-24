"""Conservative entity resolution primitives."""
from dataclasses import dataclass
import re


@dataclass(frozen=True)
class Resolution:
    candidate_id: str
    canonical_id: str | None
    score: float
    status: str
    reasons: list[str]


def normalize_name(name: str) -> str:
    value = name.lower().strip()
    value = re.sub(r"[^a-z0-9\s]", " ", value)
    value = re.sub(r"\b(inc|incorporated|corp|corporation|company|co|llc|ltd)\b", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def similarity(a: str, b: str) -> float:
    """Simple token/Jaccard similarity; intentionally not a final resolver."""
    aa, bb = set(normalize_name(a).split()), set(normalize_name(b).split())
    if not aa or not bb:
        return 0.0
    return len(aa & bb) / len(aa | bb)


def resolve(candidate_id: str, candidate_name: str, canonical_id: str,
            canonical_name: str, threshold: float = 0.85) -> Resolution:
    score = similarity(candidate_name, canonical_name)
    status = "resolved" if score >= threshold else "unresolved"
    reasons = [f"normalized_name_similarity={score:.3f}"]
    return Resolution(candidate_id, canonical_id if status == "resolved" else None, score, status, reasons)
