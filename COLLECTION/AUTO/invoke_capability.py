#!/usr/bin/env python3
"""Fail-closed local dispatcher for Collection callable capabilities.

Only entries explicitly registered in CALLABLE-REGISTRY.json can be invoked.
No shell is used. Working directories and executable paths are constrained to
the checked-out repository.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "COLLECTION" / "MASTER" / "CALLABLE-REGISTRY.json"


def load() -> dict:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    if data.get("schema_version") != "1.0":
        raise SystemExit("unsupported callable registry schema")
    return data


def find(data: dict, capability_id: str) -> dict:
    for entry in data.get("entries", []):
        if entry.get("capability_id") == capability_id:
            return entry
    raise SystemExit(f"capability not registered: {capability_id}")


def safe_path(value: str) -> Path:
    p = (ROOT / value).resolve()
    if p != ROOT and ROOT not in p.parents:
        raise SystemExit(f"path escapes repository root: {value}")
    return p


def invoke(entry: dict, extra: list[str]) -> int:
    if entry.get("status") not in {"CALLABLE_ON_DEMAND", "PROVEN_CALLABLE"}:
        raise SystemExit(f"capability is not callable: {entry.get('status')}")

    inv = entry.get("invocation")
    if not isinstance(inv, dict) or not isinstance(inv.get("argv"), list) or not inv["argv"]:
        raise SystemExit("callable entry has no argv invocation")

    argv = [str(x) for x in inv["argv"]]
    cwd = safe_path(str(inv.get("cwd", ".")))

    # Never invoke a shell. Resolve repository-local executable/script paths.
    if argv[0] in {"python", "python3"}:
        argv[0] = sys.executable
    elif "/" in argv[0] or argv[0].startswith("."):
        argv[0] = str(safe_path(argv[0]))
    elif os.path.sep in argv[0]:
        raise SystemExit("executable must be python or a repository-local path")

    for i, arg in enumerate(argv):
        if i == 0:
            continue
        if arg.startswith("/") or arg.startswith("./") or arg.startswith("../"):
            safe_path(arg)

    completed = subprocess.run(argv + extra, cwd=cwd, check=False)
    return completed.returncode


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("capability_id", nargs="?")
    parser.add_argument("args", nargs=argparse.REMAINDER)
    parser.add_argument("--list", action="store_true")
    ns = parser.parse_args()

    data = load()
    if ns.list:
        for entry in data.get("entries", []):
            print(f"{entry.get('capability_id')}\t{entry.get('status')}\t{entry.get('name')}")
        return 0
    if not ns.capability_id:
        parser.error("capability_id is required unless --list is used")
    return invoke(find(data, ns.capability_id), ns.args)


if __name__ == "__main__":
    raise SystemExit(main())
