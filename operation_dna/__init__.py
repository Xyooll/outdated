"""Compatibility import shim for the hyphenated source-tree layout."""
from pathlib import Path

_SOURCE = Path(__file__).resolve().parent.parent / "operation-dna" / "operation_dna"
__path__ = [str(_SOURCE)]
