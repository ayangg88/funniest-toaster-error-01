#!/usr/bin/env python3
"""The Funniest Toaster Error Message.

A kitchen toaster keeps a lifetime slice counter. When the count passes the
warranty, it stops pretending everything is fine and tells its owner, in the
flattest voice it has, that the warranty is already gone.

Writes the single error line to /output/entry.txt.
"""

import os

# Lifetime odometer reading, and the slice the warranty ran out on.
SLICES_TOASTED = 4096
WARRANTY_ENDS_AT = 4095

MESSAGE = (
    f"I have toasted {SLICES_TOASTED:,} slices. "
    f"My warranty ended at {WARRANTY_ENDS_AT:,}."
)

MAX_CHARS = 120


def build_message() -> str:
    return MESSAGE.strip()


def main() -> None:
    text = build_message()
    assert text and not text.isspace(), "entry must not be blank"
    assert len(text) <= MAX_CHARS, "entry must be at most 120 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == text, "entry file does not match the message"
    print(text)


if __name__ == "__main__":
    main()
