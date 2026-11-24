#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

A robot vacuum's excuse for missing a spot. The program writes the
one-line alibi to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os
import sys

LINE = "I skipped the corner behind the couch. My lidar found a sock, a Lego, and a spider that pays rent. I do not evict tenants."
# 122 characters, verified against the 1-200 gate; no trailing newline in the file.


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"entry must be 1-200 characters, got {len(LINE)}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
