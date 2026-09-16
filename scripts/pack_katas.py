#!/usr/bin/env python3
"""Pack a lecture's katas into Moodle-ready files.

For a lecture folder like "02_Datentypen", walks each topic subfolder
(e.g. "01_Boolean") and each kata subfolder within it
(e.g. "kata-1-fehler-beheben"):

- If the kata consists of a single .md file, it is copied and renamed to
  "<Topic>_Kata_<n>.md" (e.g. "01_Boolean_Kata_1.md").
- Otherwise, all files in the kata are zipped into
  "<Topic>_Kata_<n>.zip".

Usage:
    python3 scripts/pack_katas.py 02_Datentypen
    python3 scripts/pack_katas.py 02_Datentypen -o dist/02_Datentypen
"""

import argparse
import re
import shutil
import sys
import zipfile
from pathlib import Path

KATA_NUMBER_RE = re.compile(r"kata-(\d+)", re.IGNORECASE)
IGNORED_FILENAMES = {".DS_Store"}


def iter_dirs(path: Path):
    return sorted(
        (p for p in path.iterdir() if p.is_dir() and not p.name.startswith(".")),
        key=lambda p: p.name,
    )


def iter_files(path: Path):
    return sorted(
        (p for p in path.rglob("*") if p.is_file() and p.name not in IGNORED_FILENAMES),
        key=lambda p: p.relative_to(path).as_posix(),
    )


def pack_kata(kata_dir: Path, base_name: str, output_dir: Path) -> str:
    files = iter_files(kata_dir)
    if not files:
        return f"skipped (no files): {kata_dir}"

    if len(files) == 1 and files[0].suffix.lower() == ".md":
        target = output_dir / f"{base_name}.md"
        shutil.copyfile(files[0], target)
        return f"{target.name}  <-  {files[0].relative_to(kata_dir)}"

    target = output_dir / f"{base_name}.zip"
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in files:
            zf.write(f, arcname=f.relative_to(kata_dir).as_posix())
    return f"{target.name}  <-  {len(files)} files"


def pack_lecture(lecture_dir: Path, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    for topic_dir in iter_dirs(lecture_dir):
        for kata_dir in iter_dirs(topic_dir):
            match = KATA_NUMBER_RE.search(kata_dir.name)
            if not match:
                print(f"  ! skipping (no kata number found): {kata_dir}")
                continue

            base_name = f"{topic_dir.name}_Kata_{match.group(1)}"
            result = pack_kata(kata_dir, base_name, output_dir)
            print(f"  {result}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("lecture", help="Relative path to the lecture folder, e.g. 02_Datentypen")
    parser.add_argument(
        "-o", "--output",
        help="Output directory (default: '<lecture>_moodle' next to the lecture folder)",
    )
    args = parser.parse_args()

    lecture_dir = Path(args.lecture)
    if not lecture_dir.is_dir():
        print(f"error: '{lecture_dir}' is not a directory", file=sys.stderr)
        return 1

    output_dir = Path(args.output) if args.output else lecture_dir.parent / f"{lecture_dir.name}_moodle"

    print(f"Packing '{lecture_dir}' -> '{output_dir}'")
    pack_lecture(lecture_dir, output_dir)
    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
