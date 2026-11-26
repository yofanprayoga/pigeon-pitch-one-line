#!/usr/bin/env python3
"""Write one line (<=200 characters): the elevator pitch a city pigeon
gives investors for its startup, to /output/entry.txt.

Entry for make.fun bounty "Pigeon Pitch, One Line"
(u-donrulezz-pigeon-pitch-one-line-af06c6cf).
Pure standard library, no network, deterministic.
"""

import os

# The bounty gate: /output/entry.txt must hold UTF-8 text of 1-200
# characters, not only white space. Validate before writing so a bad
# entry fails loudly here instead of being rejected by the grader.
MAX_CHARS = 200

STORY = (
    "Forty pigeons, one rooftop HQ, zero traffic: we deliver across the "
    "city faster than any courier, and our only fuel is your lunch."
)


def main() -> None:
    story = STORY.strip()
    if not story:
        raise ValueError("entry is empty")
    if len(story) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(story)} chars, over the {MAX_CHARS} limit"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(story + "\n")


if __name__ == "__main__":
    main()
