"""Unified adapter facade for read-only research ingestion."""
from dataclasses import dataclass
from typing import Callable, Any


@dataclass(frozen=True)
class AdapterResult:
    provider: str
    success: bool
    payload: Any = None
    error: str | None = None


def safe_call(provider: str, fn: Callable[..., Any], *args, **kwargs) -> AdapterResult:
    try:
        return AdapterResult(provider, True, fn(*args, **kwargs))
    except Exception as exc:
        return AdapterResult(provider, False, error=str(exc))
