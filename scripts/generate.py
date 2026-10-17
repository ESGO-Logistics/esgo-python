"""Regenerate src/esgo/_generated from the ESGO OpenAPI spec.

    python scripts/generate.py            # fetch the live spec, then generate
    python scripts/generate.py --offline  # use the openapi.json in the repo

The spec is stored as openapi.json in the repo root, so every change to the
contract shows up as a diff in the pull request. Requires the dev extra
(pip install -e ".[dev]").
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

SPEC_URL = "https://api.es-go.de/v1/openapi.json"
ROOT = Path(__file__).resolve().parent.parent
SPEC_FILE = ROOT / "openapi.json"
TARGET = ROOT / "src" / "esgo" / "_generated"


def fetch_spec() -> None:
    with urllib.request.urlopen(SPEC_URL, timeout=30) as response:
        spec = json.load(response)
    SPEC_FILE.write_text(
        json.dumps(spec, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"Spec fetched: {SPEC_URL} ({len(spec.get('paths', {}))} paths)")


def generate() -> None:
    if TARGET.exists():
        shutil.rmtree(TARGET)
    subprocess.run(
        [
            sys.executable, "-m", "openapi_python_client", "generate",
            "--path", str(SPEC_FILE),
            "--config", str(ROOT / "openapi-python-client.yml"),
            "--meta", "none",
            "--output-path", str(TARGET),
        ],
        check=True,
    )
    print(f"Generated: {TARGET.relative_to(ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--offline", action="store_true", help="do not fetch the live spec")
    args = parser.parse_args()
    if not args.offline:
        fetch_spec()
    generate()


if __name__ == "__main__":
    main()
