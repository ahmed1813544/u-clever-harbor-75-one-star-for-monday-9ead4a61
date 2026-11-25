"""One Star for Monday - a one-star review of Monday as a restaurant.

Writes a single line of plain text to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when that is set). Fully deterministic:
no network, no randomness, no timestamps - every run writes the same
bytes.
"""

import os

LINE = (
    "The waiter cleared my weekend's table before I sat down, "
    "then Monday served me a week of cold coffee and charged for the alarm."
)


def main():
    # The gate: 1-180 characters, at most 25 words, not only whitespace.
    assert 1 <= len(LINE) <= 180, "line outside the 1-180 character gate"
    assert len(LINE.split()) <= 25, "line over the 25 word cap"
    assert LINE.strip(), "line must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
