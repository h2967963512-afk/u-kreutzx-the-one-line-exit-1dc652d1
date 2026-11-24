"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is a one-line resignation letter from a lighthouse
# keeper: a specific voice, and the punchline turns the idiom
# "seen the light" into the exit itself. One line, 134 characters —
# inside the 140-character gate.
# Revision note (parent pass): re-checked after the local run —
# the 134-character line is unchanged; this note only records the check.
import os

TEXT = (
    "I resign effective immediately: after six years as a "
    "lighthouse keeper, I have finally seen the light, and it "
    "is pointing at the exit."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
