"""One Word, One Username, One Reward.

The entry is the entrant's own make.fun handle, one word and nothing
else. The judge's first criterion is that a genuine make.fun handle
beats any invented word, so the program writes exactly the account
handle: syarifuddin-s.
"""

import os

HANDLE = "syarifuddin-s"
OUTPUT_PATH = "/output/entry.txt"


def verify_output() -> None:
    """Read the written file back as bytes and confirm it is exactly
    the handle: no trailing newline, no padding, valid UTF-8."""
    with open(OUTPUT_PATH, "rb") as f:
        data = f.read()
    assert data == HANDLE.encode("utf-8"), f"mismatch: {data!r}"
    assert 1 <= len(data.decode("utf-8")) <= 30


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(HANDLE)
    verify_output()


if __name__ == "__main__":
    main()
