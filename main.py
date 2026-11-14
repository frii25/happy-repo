"""ai-happy-01 entry: write the happy image to /output/entry.png.

The image is an original flat illustration: a small round robot
handing a steaming cup of cocoa to a sleepy cat wrapped in a blanket,
the steam curling into a glowing heart under a warm sunrise.
Deterministic: the same bytes are written on every run.
"""
import os
import shutil
import sys


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Self-check: valid PNG magic and inside the 1 MiB limit.
    with open(dst, "rb") as f:
        head = f.read(8)
    if head != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a PNG")
    if os.path.getsize(dst) > 1048576:
        raise SystemExit("entry.png exceeds 1 MiB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
