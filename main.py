#!/usr/bin/env python3
"""Write exactly one letter to $MAKEFUN_OUTPUT_DIR/entry.txt.

The letter is W. Behind it sits the word "wrecked": a day that wrecked me
and I lived to tell it. It is vivid (a sharp picture of a day that ran
you over), funny (self-deprecating, the kind of word you repeat to a
friend), and true (an honest report of a real day, not a performance).
W fits "wrecked" exactly, and it is not the obvious pick — A for amazing
and Z for zero sleep are the ones everyone reaches for first. The gate
allows exactly one character, and this program writes exactly one.
Deterministic: the same letter, the same byte, every run. No network,
no randomness.
"""
import os
import sys

LETTER = "W"
WORD_BEHIND_IT = "wrecked"


def main():
    if len(LETTER) != 1 or not LETTER.isalpha() or not LETTER.isupper():
        print("error: entry must be exactly one uppercase letter",
              file=sys.stderr)
        raise SystemExit(1)
    if not WORD_BEHIND_IT.startswith(LETTER.lower()):
        print("error: letter does not match its word", file=sys.stderr)
        raise SystemExit(1)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(LETTER)
    print(f"wrote {target}: {LETTER!r} for {WORD_BEHIND_IT!r}")


if __name__ == "__main__":
    main()
