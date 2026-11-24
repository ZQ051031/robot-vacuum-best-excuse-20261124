#!/usr/bin/env python3
"""Robot Vacuum's Best Excuse.

Writes one line - the funniest excuse a robot vacuum could give -
to /output/entry.txt. Standard library only, no network access.
"""

import os

ENTRY = "I didn't eat your sock. I was on a top-secret mission under the couch when the cat sat on my power button."

MAX_CHARS = 140


def main():
    if len(ENTRY) > MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} cap")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
