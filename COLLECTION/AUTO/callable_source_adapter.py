#!/usr/bin/env python3
"""Expose a preserved Collection source as a deterministic local capability descriptor.

This is an adaptation boundary, not an upstream runtime. It proves that a preserved
source can be addressed and inspected on demand without claiming that the upstream
software is installed or executing.
"""
from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCES = ROOT / "COLLECTION" / "SOURCES"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_file")
    ns = parser.parse_args()

    p = (SOURCES / ns.source_file).resolve()
    if p.parent != SOURCES or p.suffix != ".md":
        raise SystemExit("source_file must be a markdown file directly under COLLECTION/SOURCES")
    if not p.is_file():
        raise SystemExit(f"source not preserved: {ns.source_file}")

    text = p.read_text(encoding="utf-8")
    required = ["- Source:", "- Repository:", "- Main revision inspected:", "- License:"]
    missing = [x for x in required if x not in text]
    if missing:
        raise SystemExit(f"source record incomplete: {missing}")

    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
