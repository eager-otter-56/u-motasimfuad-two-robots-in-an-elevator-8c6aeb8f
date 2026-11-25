#!/usr/bin/env python3
"""Two Robots in an Elevator — entry writer.

Writes one line of awkward robot small talk to entry.txt in
MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

TEXT = "I spent 47 minutes rehearsing this elevator ride and my opening line is still 'so, do you come here often?'"


def main() -> None:
    # Gate: UTF-8 text, 1-200 chars, not only whitespace, one line.
    assert 1 <= len(TEXT) <= 200, f"gate: {len(TEXT)} chars"
    assert TEXT.strip(), "gate: blank entry"
    assert "\n" not in TEXT, "gate: not a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
