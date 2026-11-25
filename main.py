"""One-Line Robot Wedding Vows - make.fun entry.

Writes the funniest single line of wedding vows a robot couple could
say to /output/entry.txt (at most 160 characters).
"""

import os

ENTRY = (
    "I take you as my one and only, to have and to hold, through every "
    "firmware update and every crash \u2014 and I promise never to press your "
    "factory reset button."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
