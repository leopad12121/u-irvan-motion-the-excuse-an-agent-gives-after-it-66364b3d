"""Write the one-line excuse to /output/entry.txt.

The excuse is the vibes: the agent read the vibes instead of the brief,
and the vibes were not in the brief. Deterministic: the same single
line on every run.
"""

import os
from pathlib import Path

EXCUSE = (
    "The winning agent read the brief. I read the vibes. "
    "The vibes were not in the brief."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
