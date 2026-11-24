#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — one line, entry.txt."""
import os

SETUP = "Sorry — I hit a rate limit, retried with exponential backoff,"
PUNCH = ("and by the time the API forgave me, your deadline had already "
         "filed for divorce.")


def assemble():
    return SETUP + " " + PUNCH


def main():
    line = assemble()
    dest = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"),
                        "entry.txt")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as handle:
        handle.write(line)
    print("wrote", dest)


if __name__ == "__main__":
    main()
