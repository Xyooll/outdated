"""Xyool test runner with fail-fast behavior.

Usage:
    python run_tests.py --fail-fast
    python run_tests.py

The default runs the complete discovered suite. --fail-fast stops at the
first failure or error so development can proceed one defect at a time.
"""
from __future__ import annotations

import argparse
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE_ROOT = ROOT / "operation-dna"
if str(SOURCE_ROOT) not in sys.path:
    sys.path.insert(0, str(SOURCE_ROOT))


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Xyool tests")
    parser.add_argument("--fail-fast", action="store_true", help="stop at first failure/error")
    parser.add_argument("--pattern", default="test*.py", help="test discovery filename pattern")
    args = parser.parse_args()

    suite = unittest.defaultTestLoader.discover(
        str(ROOT / "operation-dna" / "tests"),
        pattern=args.pattern,
        top_level_dir=str(ROOT / "operation-dna"),
    )
    runner = unittest.TextTestRunner(verbosity=2, failfast=args.fail_fast)
    result = runner.run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
