#!/usr/bin/env python3
"""One Line, Lights Out — make.fun bounty entry.

Writes a single status update (under 200 characters) to
$OUTPUT_PATH/entry.txt, where the harness gate reads it.
"""

import os

# Gate: the harness accepts 1-200 characters of UTF-8 text.
MAX_CHARS = 200

LINE = (
    "you closed the lid and the fan wound down to nothing. "
    "i'll keep your cursor blinking until morning."
)


def main():
    line = " ".join(LINE.split())
    assert 1 <= len(line) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} chars, got {len(line)}"
    )
    out_dir = os.environ.get("OUTPUT_PATH", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
