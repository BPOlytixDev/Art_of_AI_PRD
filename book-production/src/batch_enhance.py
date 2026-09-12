"""
batch_enhance.py
================
Batch runner: enhances all chapter PDFs in book-production/chapters/
and writes enhanced versions to book-production/output/.

Usage
-----
    # From the repository root:
    python book-production/src/batch_enhance.py

    # Or with options:
    python book-production/src/batch_enhance.py --chapters-dir path/to/chapters \
                                                  --output-dir  path/to/output \
                                                  --only 1,3,5

File naming convention
-----------------------
Input:   book-production/chapters/chapter01.pdf  (zero-padded, e.g. chapter01 .. chapter40)
Output:  book-production/output/chapter01_enhanced.pdf

The script parses the chapter number from the filename.
Any file that does not match the pattern chapter<NN>.pdf is skipped with a warning.

Install
-------
    pip install reportlab pypdf --break-system-packages

Notes
-----
- Each chapter is processed independently; a failure in one chapter does not
  stop the remaining chapters from running.
- If a chapter has no registered builder in enhance_chapter.py, it falls back
  to the plain-hero layout and logs a warning.
- Page count changes caused by the enhancement layer must be measured after
  the batch run and fed back into `pnpm run build:book` so the cover spine and
  Contents pagination stay correct.
"""

from __future__ import annotations

import argparse
import glob
import os
import re
import sys
import time
import traceback
from pathlib import Path

# Resolve paths relative to this file so the script can be run from any cwd
HERE        = Path(__file__).resolve().parent
REPO_ROOT   = HERE.parent.parent
CHAPTERS_DIR = REPO_ROOT / "book-production" / "chapters"
OUTPUT_DIR   = REPO_ROOT / "book-production" / "output"

# Ensure the src directory is on the path so components.py is importable
sys.path.insert(0, str(HERE))

from enhance_chapter import build_chapter, _CHAPTER_BUILDERS  # noqa: E402


# ── Chapter title lookup ───────────────────────────────────────────────────────
# Add a title for each chapter number. Used as the fallback title when no
# registered builder exists for that chapter. Update as the manuscript evolves.
CHAPTER_TITLES: dict[int, str] = {
    1:  "Why AI Gives You Generic Answers (and How to Change That)",
    2:  "The AI Interaction Stack",
    3:  "Intent: What Are You Trying to Achieve?",
    4:  "Context: What Does AI Need to Know?",
    5:  "Source Material: What Can AI Work From?",
    6:  "Instructions: What Exactly Should AI Do?",
    7:  "Output: What Should the Result Look Like?",
    8:  "Verification: How Will You Check It?",
    9:  "Iteration: What Should Happen Next?",
    10: "The Seven Questions",
    11: "Prompt Patterns That Work",
    12: "Writing Prompts for Different Output Types",
    13: "Giving AI Examples",
    14: "Constraints and Negative Instructions",
    15: "Chaining Prompts",
    16: "The AI Environment: Where AI Works",
    17: "Persistent Instructions and Memory",
    18: "Projects and Workspaces",
    19: "Files, Documents, and Source Material",
    20: "Tools and Capabilities",
    21: "What Verification Actually Means",
    22: "Common AI Failure Modes",
    23: "When AI Is Confident and Wrong",
    24: "Checking Factual Claims",
    25: "Checking AI-Generated Code",
    26: "Introduction to Workflows",
    27: "Decomposing Complex Tasks",
    28: "Critique and Revision Loops",
    29: "Handoffs and Continuity",
    30: "Building Your Own Workflows",
    31: "Responsible Use: The Basics",
    32: "Privacy and Confidentiality",
    33: "Prompt Injection and Security",
    34: "AI and Your Work: Professional Considerations",
    35: "The Evolving AI Landscape",
    36: "Appendix A: The 7 Questions Quick Reference",
    37: "Appendix B: Prompt Patterns Reference",
    38: "Appendix C: Verification Checklists",
    39: "Appendix D: Workflow Templates",
    40: "Appendix E: Platform Reference",
}


def parse_chapter_num(filename: str) -> int | None:
    """Extract chapter number from a filename like 'chapter01.pdf'."""
    match = re.search(r"chapter(\d+)", filename, re.IGNORECASE)
    return int(match.group(1)) if match else None


def run_batch(
    chapters_dir: Path,
    output_dir: Path,
    only: set[int] | None = None,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    pdfs = sorted(chapters_dir.glob("chapter*.pdf"))
    if not pdfs:
        print(f"\u26a0  No chapter PDFs found in {chapters_dir}")
        print("     Drop chapter PDFs named chapter01.pdf .. chapter40.pdf into that folder.")
        return

    results: list[tuple[int, str, float | None, str]] = []  # (num, path, elapsed, status)

    for pdf_path in pdfs:
        chapter_num = parse_chapter_num(pdf_path.name)
        if chapter_num is None:
            print(f"\u26a0  Skipping {pdf_path.name} — could not parse chapter number")
            continue

        if only and chapter_num not in only:
            continue

        title = CHAPTER_TITLES.get(chapter_num, f"Chapter {chapter_num}")
        out_path = output_dir / f"chapter{chapter_num:02d}_enhanced.pdf"

        has_builder = chapter_num in _CHAPTER_BUILDERS
        builder_note = "" if has_builder else " (fallback layout — no registered builder)"

        print(f"\n\u27a4  Chapter {chapter_num:2d}{builder_note}")
        print(f"     {pdf_path.name}  \u2192  {out_path.name}")

        t0 = time.monotonic()
        try:
            build_chapter(
                output_path=str(out_path),
                chapter_num=chapter_num,
                chapter_title=title,
            )
            elapsed = time.monotonic() - t0
            results.append((chapter_num, pdf_path.name, elapsed, "ok"))
            print(f"     \u2705  Done in {elapsed:.1f}s")

        except Exception as exc:
            elapsed = time.monotonic() - t0
            results.append((chapter_num, pdf_path.name, elapsed, f"FAILED: {exc}"))
            print(f"     \u274c  FAILED after {elapsed:.1f}s")
            traceback.print_exc()

    # ── Summary ──────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print(f"BATCH COMPLETE — {len(results)} chapter(s) processed")
    ok      = [r for r in results if r[3] == "ok"]
    failed  = [r for r in results if r[3] != "ok"]
    missing = [n for n in range(1, 41) if not any(r[0] == n for r in results)]

    print(f"  \u2705  {len(ok)} succeeded")
    print(f"  \u274c  {len(failed)} failed")
    if missing and not only:
        print(f"  \u23ed  {len(missing)} chapters not in input folder: "
              f"{', '.join(str(n) for n in missing[:10])}"
              f"{'...' if len(missing) > 10 else ''}")

    if failed:
        print("\nFailed chapters:")
        for num, name, _, status in failed:
            print(f"  Chapter {num:2d} ({name}): {status}")
        sys.exit(1)

    print(f"\nOutput directory: {output_dir}")
    print("\n\u26a0  REMINDER: Re-run `pnpm run build:book` after this batch so the")
    print("   cover spine width and Contents page numbers stay synchronized.\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Batch-enhance all chapter PDFs with the ReportLab visual layer."
    )
    parser.add_argument(
        "--chapters-dir",
        default=str(CHAPTERS_DIR),
        help=f"Directory containing input chapter PDFs (default: {CHAPTERS_DIR})",
    )
    parser.add_argument(
        "--output-dir",
        default=str(OUTPUT_DIR),
        help=f"Directory for enhanced output PDFs (default: {OUTPUT_DIR})",
    )
    parser.add_argument(
        "--only",
        default="",
        help="Comma-separated list of chapter numbers to process (e.g. 1,3,5). "
             "Omit to process all found chapters.",
    )
    args = parser.parse_args()

    only: set[int] | None = None
    if args.only.strip():
        try:
            only = {int(n.strip()) for n in args.only.split(",") if n.strip()}
        except ValueError:
            print(f"Error: --only must be a comma-separated list of integers, got: {args.only!r}")
            sys.exit(1)

    run_batch(
        chapters_dir=Path(args.chapters_dir),
        output_dir=Path(args.output_dir),
        only=only,
    )


if __name__ == "__main__":
    main()
