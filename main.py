#!/usr/bin/env python3
"""One-line pitch entry for make.fun: "A Day of One-Line Pitches".

Writes a single persuasive sentence to /output/entry.txt.

Deterministic and offline: no network, no API calls, no randomness.
The pitch is a fixed string chosen by local judging; the program only
writes it to the file the harness reads.
"""

import os

PITCH = (
    "Tell make.fun your app idea in plain words and an AI agent will build "
    "the first version for you, free to try, so you can see it working "
    "before you spend a thing."
)


def main() -> None:
    # Gate guard: the sealed scorer only accepts 1-240 characters.
    assert 1 <= len(PITCH) <= 240, f"pitch is {len(PITCH)} chars, must be 1-240"
    assert PITCH.strip(), "pitch must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
