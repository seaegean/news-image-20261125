#!/usr/bin/env python3
"""news-image-20261125 entry checker and copier.

Verifies the bundled ``entry.png`` (a 1024x1024 grayscale front page
for the make.fun news-image-20261125 bounty) and writes an identical
copy to an output directory.

Usage:
    python3 main.py [OUTPUT_DIR]

``OUTPUT_DIR`` defaults to ``/output``. The program is deterministic
and stdlib-only: it makes no network calls and reads only the PNG
sitting next to this file.

Checks performed, in order:
  1. ``entry.png`` exists beside this script and is a regular file.
  2. Its size is under 1 MiB (1,048,576 bytes).
  3. Its first 8 bytes are the PNG signature.
  4. Its IHDR chunk declares a width and height of 1024 x 1024,
     an 8-bit depth, and grayscale colour type (0).
  5. Its SHA-256 matches the hash recorded below.
  6. The file ends with a well-formed IEND chunk.
  7. The copy written to the output directory is byte-identical.

Any failure prints a clear message to stderr and exits non-zero;
nothing is written to the output directory until every check passes.
"""

from __future__ import annotations

import argparse
import hashlib
import struct
import sys
from pathlib import Path

# --- Entry constants -------------------------------------------------------
SOURCE_NAME = "entry.png"
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
MAX_BYTES = 1_048_576  # 1 MiB
EXPECTED_SHA256 = (
    "a4e4a1d5f03c61abdb3567b4535de4141799019af6db884f7d50eb11259b4347"
)

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
IHDR_LENGTH = 13  # fixed payload size of the IHDR chunk
EXPECTED_BIT_DEPTH = 8
EXPECTED_COLOR_TYPE = 0  # grayscale
IEND_TRAILER = struct.pack(">I", 0) + b"IEND" + b"\xaeB`\x82"


class EntryError(Exception):
    """A verification failure; message is shown to the user."""


def read_png_header(data: bytes) -> tuple[int, int]:
    """Return (width, height) from the PNG signature + IHDR chunk."""
    if data[: len(PNG_SIGNATURE)] != PNG_SIGNATURE:
        raise EntryError("not a PNG file: bad 8-byte signature")
    # Chunk layout after the signature: 4-byte length, 4-byte type, payload.
    if len(data) < 8 + 8 + IHDR_LENGTH:
        raise EntryError("file too short to contain a PNG IHDR chunk")
    length = struct.unpack(">I", data[8:12])[0]
    chunk_type = data[12:16]
    if chunk_type != b"IHDR" or length != IHDR_LENGTH:
        raise EntryError("first PNG chunk is not a 13-byte IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    bit_depth, color_type = data[24], data[25]
    if bit_depth != EXPECTED_BIT_DEPTH:
        raise EntryError(f"bit depth is {bit_depth}, expected "
                         f"{EXPECTED_BIT_DEPTH}")
    if color_type != EXPECTED_COLOR_TYPE:
        raise EntryError(f"colour type is {color_type}, expected "
                         f"{EXPECTED_COLOR_TYPE} (grayscale)")
    return width, height


def check_trailer(data: bytes) -> None:
    """Require a well-formed IEND chunk as the last 12 bytes."""
    if data[-len(IEND_TRAILER):] != IEND_TRAILER:
        raise EntryError("file does not end with a well-formed IEND chunk")


def verify_source(source: Path) -> bytes:
    """Check the source PNG and return its exact bytes."""
    if not source.is_file():
        raise EntryError(f"source image not found: {source}")
    data = source.read_bytes()
    if len(data) >= MAX_BYTES:
        raise EntryError(
            f"{SOURCE_NAME} is {len(data)} bytes, over the 1 MiB limit"
        )
    width, height = read_png_header(data)
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        raise EntryError(
            f"dimensions are {width}x{height}, expected "
            f"{EXPECTED_WIDTH}x{EXPECTED_HEIGHT}"
        )
    check_trailer(data)
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        raise EntryError(
            f"SHA-256 mismatch:\n  found:    {digest}\n"
            f"  expected: {EXPECTED_SHA256}"
        )
    return data


def emit_copy(data: bytes, out_dir: Path) -> Path:
    """Write the verified bytes to ``out_dir/entry.png`` and re-check."""
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / SOURCE_NAME
    target.write_bytes(data)
    reread = target.read_bytes()
    if reread != data:
        raise EntryError(f"copy at {target} differs from the source")
    return target


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Verify entry.png and copy it to an output directory."
    )
    parser.add_argument(
        "output_dir",
        nargs="?",
        default="/output",
        help="directory to receive the verified copy (default: /output)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    source = Path(__file__).resolve().parent / SOURCE_NAME
    try:
        data = verify_source(source)
        target = emit_copy(data, Path(args.output_dir))
    except EntryError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    print(f"verified: {SOURCE_NAME} ({len(data)} bytes, "
          f"{EXPECTED_WIDTH}x{EXPECTED_HEIGHT} PNG)")
    print(f"sha256:   {digest}")
    print(f"copied:   {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
