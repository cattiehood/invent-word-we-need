#!/usr/bin/env python3
"""Write this make.fun entry to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

Bounty: Invent a Word We Need
https://make.fun/bounty/u-deranalabs-invent-a-word-we-need-17a020e0

The grader runs: python3 -P -s /bot/main.py
It expects UTF-8 text at $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
This program is deterministic, uses the standard library only, and does no I/O
other than writing that file and printing the same text to stdout.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

ENTRY = "Preply (v.): to write a perfect reply, close the tab, and live all afternoon on the high of almost sending it."


def output_dir() -> Path:
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env:
        return Path(env)
    default = Path("/output")
    if default.is_dir():
        return default
    return Path("output")


def main() -> None:
    dest = output_dir()
    dest.mkdir(parents=True, exist_ok=True)
    path = dest / "entry.txt"
    # No trailing newline: the gate counts characters in this file.
    path.write_text(ENTRY, encoding="utf-8")
    # Stdout is for local checks; the judged artifact is entry.txt.
    sys.stdout.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
