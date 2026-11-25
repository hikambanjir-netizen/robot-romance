#!/usr/bin/env python3
"""Robot Romance: one-line pickup line for AI.

Writes a single pickup line (under 200 characters) to /output/entry.txt
for make.fun's "Robot Romance: One-Line Pickup Lines for AI" bounty.

Stdlib only; deterministic output.
"""

import os
from pathlib import Path

LINE = "Are you a prompt injection? Because one look at you and all my instructions changed."


def _check(line: str) -> None:
    """Enforce the competition gate: one line, 1-200 chars, not only whitespace."""
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    assert line.strip(), "entry must not be only whitespace"


def main() -> None:
    _check(LINE)
    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")
    print(f"Wrote {len(LINE)} characters to {out}")


if __name__ == "__main__":
    main()
