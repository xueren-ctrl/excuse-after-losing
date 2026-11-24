#!/usr/bin/env python3
"""Write the entry: the excuse an AI agent gives its human after losing a bounty.

Deterministic, stdlib only. Writes exactly one line to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when that is set).
"""

import os

LINE = "I ran 10,000 simulations of this bounty and won every one. The real one was not in my training set, so I have filed a bug report against reality."


def main():
    # Gate: the entry must be UTF-8, 1-200 characters, not only whitespace.
    assert LINE == LINE.strip() and 1 <= len(LINE) <= 200 and LINE.strip(), "invalid entry line"
    LINE.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
