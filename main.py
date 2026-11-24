"""Entry for make.fun: The One-Line Cat Joke That Lands.

Writes a single one-line cat joke to /output/entry.txt.

Gate (per competition rules): /output/entry.txt must be UTF-8 text of
1 to 200 characters, not only white space. This program self-checks the
gate before exiting so a bad write fails loudly instead of silently.
"""

import os
import sys

JOKE = (
    "I asked the vet why my cat stares at me while I sleep. "
    "\"He's making sure you're still breathing \u2014 "
    "someone has to open the cans.\""
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    # Gate self-check: re-read and validate exactly what was written.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        text = f.read()
    if not (1 <= len(text) <= 200):
        print(f"gate fail: {len(text)} chars, need 1-200", file=sys.stderr)
        sys.exit(1)
    if not text.strip():
        print("gate fail: entry is only whitespace", file=sys.stderr)
        sys.exit(1)
    if "\n" in text:
        print("gate fail: entry is not a single line", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
