"""Development bootstrap for the source-tree layout.

When Python is launched from the repository root, automatically expose the
hyphenated ``operation-dna`` source directory so local unittest discovery can
import the ``software`` package without requiring a manually configured
PYTHONPATH. Installed/package deployments do not depend on this file.
"""
from pathlib import Path
import sys

SOURCE_ROOT = Path(__file__).resolve().parent / "operation-dna"
if SOURCE_ROOT.is_dir() and str(SOURCE_ROOT) not in sys.path:
    sys.path.insert(0, str(SOURCE_ROOT))
