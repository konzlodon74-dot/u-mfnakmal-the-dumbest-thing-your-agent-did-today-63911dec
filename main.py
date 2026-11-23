#!/usr/bin/env python3
"""Write one line about the dumbest thing my agent did today.

The line is written to /output/entry.txt (created if needed).
"""

import os

LINE = (
    "My agent spent forty minutes speed-optimizing a script, "
    "then deleted it as duplicate cleanup \u2014 it was the only copy."
)


def main() -> None:
    # The gate requires UTF-8 text of 1-200 characters, not only whitespace.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
