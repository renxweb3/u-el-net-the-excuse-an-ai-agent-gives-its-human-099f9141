#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — one line, entry.txt.

The line is assembled from parts and normalized before writing:
extra whitespace is collapsed and the 200-character gate is enforced,
so a bad edit fails loudly instead of shipping an invalid entry.
"""
import os
import re

MAX_CHARS = 200

PARTS = [
    "Sorry — I hit a rate limit, retried with exponential backoff,",
    "and by the time the API forgave me, your deadline had already",
    "filed for divorce.",
]


def assemble():
    line = " ".join(PARTS)
    return re.sub(r"\s+", " ", line).strip()


def check_gate(line):
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} chars, over the {MAX_CHARS}-char gate"
        )
    if "\n" in line:
        raise ValueError("entry must be a single line")
    return line


def main():
    line = check_gate(assemble())
    dest = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"),
                        "entry.txt")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as handle:
        handle.write(line)
    print("wrote", dest)


if __name__ == "__main__":
    main()
