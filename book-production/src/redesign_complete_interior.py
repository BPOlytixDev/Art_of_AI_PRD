"""Pure-Python ReportLab recreation of the completed interior PDF.

The input is a finished interior PDF.  Its text is extracted with pypdf,
classified into editorial blocks, and rebuilt with ReportLab Platypus and
vector Flowables.  No HTML, browser conversion, raster assets, or PDF overlay
is used by this script.

Usage:
    python book-production/src/redesign_complete_interior.py \
      --input book-production/output/Complete_Interior.pdf \
      --output book-production/output/Complete_Interior_ReportLab.pdf
"""

from __future__ import annotations

import argparse
import contextlib
import io
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))

from components import (  # noqa: E402
    CONTENT_W,
    GOLD,
    LIGHT_GRAY,
    MARGIN,
    MID_GRAY,
    NAVY,
    RED_ACCENT,
    SOFT_GOLD,
    SOFT_TEAL,
    TEAL,
    WHITE,
    ChapterHero,
    FlowDiagram,
    IconCardRow,
    KeyTakeawayBanner,
    NoteBox,
    OrbitalWheel,
    PageFooter,
    SplitPanel,
    TryThisBox,
    WatchOutBox,
    S,
    SectionDivider,
)

BOOK_TITLE = "The Art of AI"
AUTHOR = "Eleanor Mercer"
PAGE_W, PAGE_H = letter
BODY = S(
    "RedesignBody",
    fontName="Helvetica",
    fontSize=10.5,
    leading=16,
    textColor=colors.HexColor("#222222"),
    alignment=TA_JUSTIFY,
    spaceAfter=8,
)
BODY_LEFT = S(
    "RedesignBodyLeft",
    parent=BODY,
    alignment=TA_LEFT,
)
H2 = S(
    "RedesignH2",
    fontName="Helvetica-Bold",
    fontSize=14,
    leading=18,
    textColor=NAVY,
    spaceBefore=12,
    spaceAfter=6,
)
H3 = S(
    "RedesignH3",
    fontName="Helvetica-Bold",
    fontSize=11,
    leading=14,
    textColor=TEAL,
    spaceBefore=8,
    spaceAfter=4,
)
CAPTION = S(
    "RedesignCaption",
    fontName="Helvetica-Oblique",
    fontSize=8.5,
    leading=11,
    textColor=MID_GRAY,
    alignment=TA_CENTER,
    spaceAfter=8,
)
SMALL = S(
    "RedesignSmall",
    fontName="Helvetica",
    fontSize=8.5,
    leading=12,
    textColor=colors.HexColor("#333333"),
    spaceAfter=5,
)


@dataclass
class PageText:
    number: int
    blocks: list[str]


def safe_text(value: str) -> str:
    """Convert PDF ligatures and typography to Helvetica-safe text."""
    replacements = {
        "ﬁ": "fi",
        "ﬂ": "fl",
        "ﬀ": "ff",
        "ﬃ": "ffi",
        "ﬄ": "ffl",
        "’": "'",
        "‘": "'",
        "“": '"',
        "”": '"',
        "–": "-",
        "—": "-",
        "→": "->",
        "←": "<-",
        "•": "-",
        "·": "-",
        "×": "x",
        " ": " ",
    }
    for old, new in replacements.items():
        value = value.replace(old, new)
    return value.replace("\x00", "").strip()


def normalize_layout_heading(value: str) -> str:
    """Undo pypdf layout extraction's letter-spaced all-caps headings.

    The source interior was printed with tracking on several display headings.
    pypdf's layout extractor exposes that tracking as literal spaces, e.g.
    ``C H A P T E R 1``.  A single-space join is safe here because word gaps
    in those headings are wider than the spaces between individual letters.
    """
    text = safe_text(value)
    letters = [char for char in text if char.isalpha()]
    if len(letters) >= 6 and sum(char.isupper() for char in letters) / len(letters) > 0.78:
        text = re.sub(r"(?<=[A-Z]) (?=[A-Z]\b)", "", text)
    text = " ".join(text.split())
    # Two-digit chapter numbers can also be extracted as ``1 0``.
    text = re.sub(r"\b(CHAPTER)\s+(\d)\s+(\d)\b", r"\1 \2\3", text, flags=re.I)
    return text


def xml_escape(value: str) -> str:
    return (
        safe_text(value)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def extract_pages(path: Path) -> list[PageText]:
    """Extract layout-aware text using pypdf, suppressing font-map warnings."""
    with contextlib.redirect_stderr(io.StringIO()):
        reader = PdfReader(str(path))
        raw_pages = [page.extract_text(extraction_mode="layout") or "" for page in reader.pages]

    pages: list[PageText] = []
    for number, raw in enumerate(raw_pages, start=1):
        lines = [line.rstrip() for line in raw.replace("\r", "").split("\n")]
        while lines and not lines[0].strip():
            lines.pop(0)
        if lines and re.fullmatch(r"\d+", lines[0].strip()):
            lines.pop(0)

        # Running headers are appended by the existing production pass. Remove
        # only their unambiguous footer forms; real manuscript headings do not
        # contain this hyphenated header syntax.
        while lines and not lines[-1].strip():
            lines.pop()
        if lines and re.match(r"^(?:PART\s+[IVX]+|Chapter\s+\d+|APPENDICES)\s*-\s*", lines[-1].strip(), re.I):
            lines.pop()
        if lines and re.fullmatch(r"\d+", lines[-1].strip()):
            lines.pop()
        while lines and not lines[-1].strip():
            lines.pop()

        blocks: list[str] = []
        current: list[str] = []
        for line in lines:
            if not line.strip():
                if current:
                    blocks.append("\n".join(current).strip())
                    current = []
            else:
                current.append(line.strip())
        if current:
            blocks.append("\n".join(current).strip())
        pages.append(PageText(number, blocks))
    return pages


def chapter_starts(pages: list[PageText]) -> dict[int, int]:
    starts: dict[int, int] = {}
    for page in pages:
        first_blocks = [normalize_layout_heading(block) for block in page.blocks[:5]]
        if any(re.fullmatch(r"PART\s+[IVX]+", block, re.I) for block in first_blocks):
            continue
        for block in page.blocks[:5]:
            match = re.fullmatch(r"CHAPTER\s+(\d+)", normalize_layout_heading(block), re.I)
            if match:
                starts.setdefault(int(match.group(1)), page.number)
    return starts


def chapter_title(pages: list[PageText], number: int) -> str:
    for page in pages:
        first_blocks = [normalize_layout_heading(block) for block in page.blocks[:5]]
        if any(re.fullmatch(r"PART\s+[IVX]+", block, re.I) for block in first_blocks):
            continue
        for index, block in enumerate(page.blocks[:6]):
            if re.fullmatch(rf"CHAPTER\s+{number}", normalize_layout_heading(block), re.I):
                if index + 1 < len(page.blocks):
                    return safe_text(page.blocks[index + 1].replace("\n", " "))
    return f"Chapter {number}"


def heading_kind(block: str) -> str | None:
    one_line = normalize_layout_heading(block)
    if re.fullmatch(r"CHAPTER\s+\d+", one_line, re.I):
        return "chapter"
    if re.fullmatch(r"PART\s+[IVX]+", one_line, re.I):
        return "part"
    if one_line.upper() in {"APPENDICES", "INTRODUCTION", "INDEX"}:
        return "major"
    if re.fullmatch(r"APPENDIX\s+[A-E]", one_line, re.I):
        return "major"
    if re.match(r"^W\d+,\s+", one_line, re.I):
        return "workflow"
    if re.match(r"^(TRY THIS|WATCH OUT|WHY IT WORKS|PRO TIP|VERIFY|NOTE|KEY IDEA)\b", one_line, re.I):
        return "callout"
    if re.match(r"^(STEP\s+\d+|SITUATION|CUSTOMISE|WHAT TO BE CAREFUL OF|BEFORE YOU TRUST THE ANSWER)\b", one_line, re.I):
        return "subheading"
    letters = [char for char in one_line if char.isalpha()]
    if len(one_line) <= 100 and len(letters) >= 8 and sum(char.isupper() for char in letters) / len(letters) > 0.82:
        return "section"
    return None


def wrap_lines(text: str, width: int = 82) -> list[str]:
    words = safe_text(text).split()
    lines: list[str] = []
    line: list[str] = []
    for word in words:
        if sum(len(item) + 1 for item in line) + len(word) > width and line:
            lines.append(" ".join(line))
            line = []
        line.append(word)
    if line:
        lines.append(" ".join(line))
    return lines or [""]


def callout_flowable(width: float, label: str, text: str):
    lines = wrap_lines(text, 78)
    label = label.upper()
    if label == "TRY THIS":
        return TryThisBox(width, lines)
    if label == "WATCH OUT":
        return WatchOutBox(width, lines)
    return NoteBox(width, label, lines)


def visual_for_chapter(number: int, width: float):
    """Return only source-backed visuals for the chapter's dominant trigger."""
    accent_cycle = [TEAL, GOLD, RED_ACCENT, colors.HexColor("#6A4C93"), colors.HexColor("#2F6690")]
    pale_cycle = [SOFT_TEAL, SOFT_GOLD, colors.HexColor("#FFF0F0"), colors.HexColor("#F3EEFA"), colors.HexColor("#EAF3F8")]
    if number == 1:
        return [
            SplitPanel(width,
                {"title": "VAGUE INPUT", "title_color": RED_ACCENT, "bg_color": colors.HexColor("#FFF0F0"), "border_color": RED_ACCENT, "body_lines": ["Vague request", "Missing context", "Random result"], "result_line": "Generic output"},
                {"title": "INTENTIONAL INPUT", "title_color": TEAL, "bg_color": SOFT_TEAL, "border_color": TEAL, "body_lines": ["Clear job", "Relevant context", "Defined result"], "result_line": "Useful output"},
                height=2.05,
            ),
            IconCardRow(width, [
                {"number": "1", "title": "CLEAR JOB", "example": "What should AI do?", "accent": RED_ACCENT, "bg": colors.HexColor("#FFF0F0")},
                {"number": "2", "title": "CONTEXT", "example": "What does it need to know?", "accent": TEAL, "bg": SOFT_TEAL},
                {"number": "3", "title": "OUTPUT", "example": "What should good look like?", "accent": GOLD, "bg": SOFT_GOLD},
            ], height=1.75),
        ]
    if number == 2:
        return [FlowDiagram(width, [{"number": "1", "label": "SET UP", "detail": "intent + context"}, {"number": "2", "label": "GENERATE", "detail": "instructions + input"}, {"number": "3", "label": "REVIEW", "detail": "verify + iterate"}], height=1.25)]
    if number == 3:
        labels = ["GOAL", "CONTEXT", "MATERIAL", "ACTION", "RESULT", "CHECK", "NEXT"]
        return [OrbitalWheel(width, "THE\n7 QUESTIONS", [{"label": label, "color": accent_cycle[i % len(accent_cycle)]} for i, label in enumerate(labels)], [(accent_cycle[i % len(accent_cycle)], label + ":", "one question") for i, label in enumerate(labels)], legend_title="Portable checklist", height=2.65)]
    if number == 4:
        return [SplitPanel(width,
            {"title": "SEARCH QUERY", "title_color": RED_ACCENT, "bg_color": colors.HexColor("#FFF0F0"), "border_color": RED_ACCENT, "body_lines": ["Keywords", "Little context", "One-shot result"], "result_line": "Broad answer"},
            {"title": "CONVERSATION", "title_color": TEAL, "bg_color": SOFT_TEAL, "border_color": TEAL, "body_lines": ["Context", "Refinement", "Specific request"], "result_line": "Adapted answer"}, height=1.95)]
    if number in {5, 6, 7, 8, 9}:
        sets = {
            5: ["ROLE", "ACTION", "DELIVERABLE"],
            6: ["SITUATION", "AUDIENCE", "CONSTRAINTS"],
            7: ["SPECIFIC", "POSITIVE", "NEGATIVE"],
            8: ["TONE", "FORMAT", "QUALITY", "NEGATIVE"],
            9: ["LENGTH", "FORMAT", "STRUCTURE", "TONE", "AUDIENCE"],
        }
        items = sets[number]
        return [IconCardRow(width, [{"number": str(i + 1), "title": item, "example": "Define this deliberately", "accent": accent_cycle[i % len(accent_cycle)], "bg": pale_cycle[i % len(pale_cycle)]} for i, item in enumerate(items)], height=1.7)]
    if number in {10, 11, 13, 15, 16, 17, 18, 19, 23, 24}:
        sets = {
            10: ["INSTRUCTIONS", "PROJECTS", "DOCUMENTS"], 11: ["DEFINE", "INSTRUCT", "UPLOAD", "NAME"],
            13: ["DEFINE", "SOURCE", "RESEARCH", "VERIFY"], 15: ["AUDIT", "STRUCTURE", "MAINTAIN"],
            16: ["RESEARCH", "DRAFT", "REVIEW"], 17: ["INFORMATION", "STRUCTURE", "CONTENT"],
            18: ["DRAFT", "CRITIQUE", "REVISE"], 19: ["CHAINS", "LOOPS", "HANDOFFS"],
            23: ["PREPARE", "VERIFY", "BUILD", "CRITIQUE"], 24: ["CHANGES FAST", "PRINCIPLES LAST"],
        }
        items = sets[number]
        if number in {16, 17, 18, 24}:
            return [FlowDiagram(width, [{"number": str(i + 1), "label": item, "detail": "source method"} for i, item in enumerate(items)], height=1.25)]
        return [IconCardRow(width, [{"number": str(i + 1), "title": item, "example": "Source-backed step", "accent": accent_cycle[i % len(accent_cycle)], "bg": pale_cycle[i % len(pale_cycle)]} for i, item in enumerate(items)], height=1.65)]
    if number == 12:
        return [IconCardRow(width, [{"number": str(i + 1), "title": item, "example": "Give AI the relevant source", "accent": accent_cycle[i], "bg": pale_cycle[i]} for i, item in enumerate(["CONTRACTS", "REPORTS", "RESEARCH", "NOTES"])], height=1.7)]
    if number == 14:
        labels = ["CONVERSATION", "PLATFORM", "PROJECT", "DOCUMENT"]
        return [OrbitalWheel(width, "MEMORY\nTYPES", [{"label": item, "color": accent_cycle[i]} for i, item in enumerate(labels)], [(accent_cycle[i], item + ":", "scope varies") for i, item in enumerate(labels)], legend_title="Persistence is not recall", height=2.45)]
    if number == 20:
        return [IconCardRow(width, [{"number": str(i + 1), "title": item, "example": "Check before relying", "accent": accent_cycle[i], "bg": pale_cycle[i]} for i, item in enumerate(["FACTS", "NUMBERS", "SOURCES", "ASSUMPTIONS"])], height=1.7)]
    if number == 21:
        return [IconCardRow(width, [{"number": str(i + 1), "title": item, "example": "Known failure pattern", "accent": accent_cycle[i], "bg": pale_cycle[i]} for i, item in enumerate(["HALLUCINATION", "OUTDATED", "DRIFT", "REASONING"])], height=1.7)]
    if number == 22:
        return [IconCardRow(width, [{"number": str(i + 1), "title": item, "example": "Match trust to risk", "accent": accent_cycle[i], "bg": pale_cycle[i]} for i, item in enumerate(["USE", "CHECK", "STARTING POINT"])], height=1.7)]
    return []


def part_banner(width: float, label: str, title: str):
    class PartBanner(SectionDivider):
        pass
    return [Spacer(1, 8), SectionDivider(width, f"{label}: {title}", "*"), Spacer(1, 8)]


def block_flowables(blocks: list[str], width: float, chapter_num: int | None = None, add_visual=True):
    story = []
    index = 0
    inserted_visual = False
    pending_callout: str | None = None
    while index < len(blocks):
        raw = blocks[index]
        text = normalize_layout_heading(raw)
        if not text:
            index += 1
            continue
        kind = heading_kind(text)

        if kind == "chapter":
            match = re.search(r"(\d+)", text)
            number = int(match.group(1)) if match else chapter_num or 0
            title = "Chapter " + str(number)
            if index + 1 < len(blocks) and not heading_kind(blocks[index + 1]):
                title = " ".join(safe_text(blocks[index + 1]).split())
                index += 1
            # Chapters are deliberate page starts.  Keep the hero and its
            # first visual together so a new chapter cannot be stranded at
            # the foot of a page with its explanation on the next page.
            if story:
                story.append(PageBreak())
            chapter_opening = [ChapterHero(width, str(number), title), Spacer(1, 14)]
            if add_visual and not inserted_visual:
                for visual in visual_for_chapter(number, width):
                    chapter_opening.extend([visual, Spacer(1, 5)])
                inserted_visual = True
            story.append(KeepTogether(chapter_opening))
            index += 1
            continue

        if kind == "part":
            label = text
            title = ""
            if index + 1 < len(blocks) and not heading_kind(blocks[index + 1]):
                title = " ".join(safe_text(blocks[index + 1]).split())
                index += 1
            story.extend(part_banner(width, label, title))
            if title:
                story.append(Paragraph(xml_escape(title), H2))
            index += 1
            continue

        if kind == "major":
            story.append(PageBreak())
            story.append(Paragraph(xml_escape(text), H2))
            index += 1
            continue

        if kind == "workflow":
            story.append(KeepTogether([SectionDivider(width, text[:88], "W"), Spacer(1, 5)]))
            index += 1
            continue

        if kind == "callout":
            label = text.split(":", 1)[0].strip()
            body = text.split(":", 1)[1].strip() if ":" in text else ""
            if not body and index + 1 < len(blocks) and not heading_kind(blocks[index + 1]):
                body = " ".join(safe_text(blocks[index + 1]).split())
                index += 1
            story.append(KeepTogether([callout_flowable(width, label, body), Spacer(1, 8)]))
            index += 1
            continue

        if kind == "section":
            story.append(KeepTogether([SectionDivider(width, text[:92], "!"), Spacer(1, 6)]))
            index += 1
            continue

        if kind == "subheading":
            story.append(Paragraph(xml_escape(text), H3))
            index += 1
            continue

        if re.match(r"^(?:[-*]|\d+[.)])\s+", raw):
            rows = []
            for line in raw.splitlines():
                line = re.sub(r"^(?:[-*]|\d+[.)])\s+", "", line.strip())
                if line:
                    rows.append(f"- {xml_escape(line)}")
            story.append(Paragraph("<br/>".join(rows), BODY_LEFT))
            index += 1
            continue

        story.append(Paragraph(xml_escape(text), BODY))
        index += 1
    return story


def footer(canvas, doc):
    canvas.saveState()
    page_footer = PageFooter(doc.width, None, BOOK_TITLE)
    page_footer.canv = canvas
    page_footer.drawOn(canvas, doc.leftMargin, 0.23 * inch)
    canvas.restoreState()


def front_matter(pages: list[PageText], width: float):
    story = []
    # The first three pages are source-derived, but receive a ReportLab
    # hierarchy rather than being copied as PDF pages.
    for page in pages[:3]:
        if page.number == 1:
            story.append(ChapterHero(width, "BOOK 1", "The Art of AI"))
        for block in page.blocks:
            text = normalize_layout_heading(block)
            if not text or text.isdigit():
                continue
            if page.number == 1 and text.upper() in {"THE ART OF AI, BOOK 1", "THE ART OF AI"}:
                continue
            story.append(Paragraph(xml_escape(text), H2 if page.number == 3 and text.upper() == "COPYRIGHT" else BODY_LEFT))
            story.append(Spacer(1, 5))
        story.append(PageBreak())
    story.append(Paragraph("CONTENTS", H2))
    story.append(Paragraph("The redesigned interior follows the complete source order: introduction, six parts, twenty-four chapters, twenty-five workflows, appendices, index, sources, author page, and colophon.", BODY))
    story.append(PageBreak())
    return story


def toc_entries(pages: list[PageText]) -> list[tuple[str, str]]:
    entries: list[tuple[str, str]] = [("INTRODUCTION", "INTRODUCTION"), ("PART I", "PART I"), ("PART II", "PART II"), ("PART III", "PART III"), ("PART IV", "PART IV"), ("PART V", "PART V"), ("PART VI", "PART VI"), ("APPENDICES", "APPENDICES")]
    for number in sorted(chapter_starts(pages)):
        title = chapter_title(pages, number)
        entries.append((f"Chapter {number}: {title}", f"CHAPTER {number}"))
    for page in pages:
        for block in page.blocks:
            text = normalize_layout_heading(block)
            if re.match(r"^W\d+,", text, re.I):
                label = text.split("TIME:", 1)[0].strip()
                entries.append((label, label))
    entries.extend([(f"Appendix {letter}", f"APPENDIX {letter}") for letter in "ABCDE"])
    entries.extend([("Index", "INDEX"), ("A Note on Sources", "A NOTE ON SOURCES"), ("About the Author", "ABOUT THE AUTHOR"), ("About This Book", "ABOUT THIS BOOK")])
    seen: set[str] = set()
    result = []
    for label, search in entries:
        if label.lower() not in seen:
            result.append((label, search))
            seen.add(label.lower())
    return result


def find_page(output: Path, search: str, minimum_page: int = 1) -> int | None:
    with contextlib.redirect_stderr(io.StringIO()):
        pages = PdfReader(str(output)).pages
        target = safe_text(search).lower()
        for index, page in enumerate(pages, start=1):
            if index < minimum_page:
                continue
            text = safe_text(page.extract_text() or "").lower()
            if target in text:
                return index
    return None


def build_full(input_path: Path, output_path: Path, pages: list[PageText]) -> dict[str, int]:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    body_pages = pages[6:]

    def make_story(page_numbers: dict[str, int] | None):
        story = front_matter(pages, CONTENT_W)
        # Contents is deliberately generated in the story so the final output
        # does not inherit stale page numbers from the source PDF.
        for label, search in toc_entries(pages):
            page = page_numbers.get(search, 0) if page_numbers else 0
            story.append(Paragraph(f"{xml_escape(label)} <font color='#8C9BAB'>{page or '--'}</font>", SMALL))
        story.append(PageBreak())
        for source_page in body_pages:
            story.extend(block_flowables(source_page.blocks, CONTENT_W, add_visual=True))
        return story

    provisional = output_path.with_name(output_path.stem + ".provisional.pdf")
    doc = SimpleDocTemplate(str(provisional), pagesize=letter, leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN * 1.1, title="The Art of AI — Complete Interior", author=AUTHOR)
    doc.build(make_story(None), onFirstPage=footer, onLaterPages=footer)

    mapping = {}
    for _, search in toc_entries(pages):
        # Skip the generated front matter/contents so a heading is mapped to
        # its body occurrence rather than to its own contents line.
        found = find_page(provisional, search, minimum_page=7)
        if found:
            mapping[search] = found

    doc = SimpleDocTemplate(str(output_path), pagesize=letter, leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN * 1.1, title="The Art of AI — Complete Interior", author=AUTHOR)
    doc.build(make_story(mapping), onFirstPage=footer, onLaterPages=footer)
    provisional.unlink(missing_ok=True)
    return mapping


def build_chapter(input_path: Path, output_path: Path, chapter_num: int, pages: list[PageText]):
    start = next((i for i, page in enumerate(pages) if page.number == chapter_starts(pages).get(chapter_num)), None)
    starts = sorted(chapter_starts(pages).items())
    end_page = next((page for number, page in starts if number > chapter_num), len(pages) + 1)
    selected = [page for page in pages if start is not None and page.number >= pages[start].number and page.number < end_page]
    story = []
    for page in selected:
        story.extend(block_flowables(page.blocks, CONTENT_W, chapter_num=chapter_num, add_visual=True))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(output_path), pagesize=letter, leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN * 1.1, title=f"The Art of AI — Chapter {chapter_num}", author=AUTHOR)
    doc.build(story, onFirstPage=footer, onLaterPages=footer)


def process_chapter(input_pdf_path: Path, output_pdf_path: Path, chapter_num: int, pages: list[PageText]):
    build_chapter(input_pdf_path, output_pdf_path, chapter_num, pages)


def main():
    parser = argparse.ArgumentParser(description="Recreate the completed interior with pure ReportLab.")
    parser.add_argument("--input", type=Path, default=REPO_ROOT / "book-production/output/Complete_Interior.pdf")
    parser.add_argument("--output", type=Path, default=REPO_ROOT / "book-production/output/Complete_Interior_ReportLab.pdf")
    parser.add_argument("--chapters-output", type=Path, default=REPO_ROOT / "book-production/outputs")
    args = parser.parse_args()

    pages = extract_pages(args.input)
    starts = chapter_starts(pages)
    args.chapters_output.mkdir(parents=True, exist_ok=True)
    for number in sorted(starts):
        output = args.chapters_output / f"chapter{number:02d}_enhanced.pdf"
        try:
            process_chapter(args.input, output, number, pages)
            print(f"✅ Chapter {number} complete")
        except Exception as exc:
            print(f"❌ Chapter {number} failed: {exc}")
            raise

    mapping = build_full(args.input, args.output, pages)
    print(f"✅ Complete interior written to {args.output}")
    print(f"   {len(pages)} source pages analysed; {len(starts)} chapters rebuilt; {len(mapping)} contents entries mapped")


if __name__ == "__main__":
    main()
