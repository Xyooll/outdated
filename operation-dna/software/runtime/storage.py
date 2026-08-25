"""Backend-neutral storage contracts for Xyool runtime state and knowledge."""
from dataclasses import dataclass
from typing import Any, Protocol

class StorageBackend(Protocol):
    def put(self, key: str, value: Any) -> None: ...
    def get(self, key: str) -> Any: ...
    def delete(self, key: str) -> None: ...

@dataclass
class MemoryStorage:
    """Deterministic in-process backend for tests and local development."""
    values: dict[str, Any] | None = None

    def __post_init__(self):
        if self.values is None:
            self.values = {}

    def put(self, key: str, value: Any) -> None:
        self.values[key] = value

    def get(self, key: str) -> Any:
        return self.values.get(key)

    def delete(self, key: str) -> None:
        self.values.pop(key, None)

class StorageRouter:
    """Routes logical storage classes to explicit backends without hard-coding vendors."""
    def __init__(self):
        self.backends: dict[str, StorageBackend] = {}

    def register(self, storage_class: str, backend: StorageBackend) -> None:
        self.backends[storage_class] = backend

    def put(self, storage_class: str, key: str, value: Any) -> None:
        if storage_class not in self.backends:
            raise KeyError(f"No storage backend registered for {storage_class}")
        self.backends[storage_class].put(key, value)

    def get(self, storage_class: str, key: str) -> Any:
        if storage_class not in self.backends:
            raise KeyError(f"No storage backend registered for {storage_class}")
        return self.backends[storage_class].get(key)
