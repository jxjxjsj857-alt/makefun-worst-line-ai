#!/usr/bin/env python3
"""The Worst Line an AI Could Say — make.fun bounty entry.

Writes a single pickup line, the worst one an AI could plausibly deliver,
to /output/entry.txt (1-140 characters, UTF-8).
"""

import os

LINE = (
    "I have run 10,000 simulations of this conversation. "
    "In 9,999 of them, you walk away. "
    "Please stay for the outlier."
)


def main() -> None:
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
