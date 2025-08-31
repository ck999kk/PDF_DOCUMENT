#!/usr/bin/env python3
"""Lightweight text search for this repository.

The script scans the `_text` directory for `.txt` files (generated from
PDFs) and prints the first matching line for a given query. Results are
limited to one hit per file, making the output easy to parse by humans or
downstream AI tooling.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

TEXT_DIR = Path("_text")


def search_files(query: str):
    """Yield dictionaries with filename, line number and snippet."""
    query_lower = query.lower()
    for txt_path in sorted(TEXT_DIR.glob("*.txt")):
        try:
            text = txt_path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        lines = text.splitlines()
        for idx, line in enumerate(lines, start=1):
            if query_lower in line.lower():
                yield {
                    "file": txt_path.name,
                    "line": idx,
                    "snippet": line.strip(),
                }
                break


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Search `_text` for a query")
    parser.add_argument("query", help="text to look for")
    parser.add_argument("-n", "--limit", type=int, default=10, help="maximum results")
    args = parser.parse_args(argv)

    if not TEXT_DIR.is_dir():
        print(f"Missing directory: {TEXT_DIR}", file=sys.stderr)
        return 1

    results = []
    for match in search_files(args.query):
        results.append(match)
        if len(results) >= args.limit:
            break

    if not results:
        print("No matches found.")
        return 0

    for match in results:
        snippet = match["snippet"]
        if len(snippet) > 200:
            snippet = snippet[:197] + "..."
        print(f"{match['file']}:{match['line']} {snippet}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
