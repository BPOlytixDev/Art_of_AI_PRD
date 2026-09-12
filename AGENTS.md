# The Art of AI — Book 1
## Agent Reference (AGENTS.md)

Production source and reproducible PDF renderer for the 6 × 9 in KDP paperback edition of
*The Art of AI — Book 1* by **Eleanor Mercer**.

This file is the authoritative reference for any AI coding agent (Codex, Claude Code, or
equivalent) working in this repository. Read it in full before touching any file.

---

## 1. Run & Operate

| Command | Purpose |
|---|---|
| `pnpm --filter @workspace/api-server run dev` | Run the API server (port 5000) |
| `pnpm run typecheck` | Full typecheck across all packages |
| `pnpm run build` | Typecheck + build all packages |
| `pnpm --filter @workspace/api-spec run codegen` | Regenerate API hooks and Zod schemas from the OpenAPI spec |
| `pnpm --filter @workspace/db run push` | Push DB schema changes (dev only) |
| `pnpm run build:book` | Render the interior PDF, calculate the final page count, and render the full-wrap cover PDF |
| `python book-production/src/enhance_chapter.py <input.pdf> <output.pdf> <chapter_num>` | Enhance a single chapter PDF with ReportLab visual layer |
| `python book-production/src/batch_enhance.py` | Batch-enhance all chapter PDFs in `book-production/chapters/` |

**Required env:** `DATABASE_URL` — Postgres connection string.

---

## 2. Stack

### Core book-production pipeline
- **Renderer:** Node.js 24, pnpm workspaces, TypeScript 5.9
- **PDF generation (primary pipeline):** Chromium headless (`--headless=new --print-to-pdf`)
- **PDF generation (enhancement layer):** Python 3.13 + ReportLab 4.x + pypdf
- **HTML→print layout:** `book-production/src/build-book.mjs`
- **CSS print system:** `book-production/src/style.css`
- **Visual components:** `book-production/src/visuals.mjs` (Markdown-side), `book-production/src/enhance_chapter.py` (ReportLab-side)

### Application stack
- **API:** Express 5
- **DB:** PostgreSQL + Drizzle ORM
- **Validation:** Zod (`zod/v4`), `drizzle-zod`
- **API codegen:** Orval (from OpenAPI spec)
- **Build:** esbuild (CJS bundle)

---

## 3. Where Things Live

```
book-production/
  source/               ← Markdown manuscript (SOURCE OF TRUTH — never edit generated PDFs)
  src/
    build-book.mjs      ← End-to-end renderer + KDP cover/spine calculation
    markdown.mjs        ← Markdown-to-print HTML conversion
    style.css           ← Print typography and layout system (6×9 KDP)
    visuals.mjs         ← Inline SVG/HTML visual components for Markdown pipeline
    enhance_chapter.py  ← ReportLab chapter enhancer (NEW — see §6)
    batch_enhance.py    ← Batch runner for all chapters (NEW — see §6)
    components.py       ← Reusable ReportLab flowable components (NEW — see §6)
    add-running-headers.py ← PyMuPDF running-header overlay
    pdf_text.py         ← PDF text extraction + merge utilities
  chapters/             ← Input chapter PDFs for the enhancement layer (NEW)
  output/               ← Generated interior PDF, cover PDF, production metadata JSON
  .generated/           ← Intermediate HTML, text extracts, header plans

docs/                   ← Editorial docs, bible, QA reports, implementation plans
attached_assets/        ← Author photo and other production assets
artifacts/              ← API server and mockup sandbox sub-projects
lib/                    ← Shared TypeScript libraries
scripts/                ← Workspace utility scripts
```

---

## 4. Architecture Decisions

### Primary pipeline (unchanged)
- The **Markdown manuscript** is the source of truth; the renderer adds only layout, navigation,
  and visual treatment. Never rewrite manuscript content.
- The production format is **6 × 9 in, black and white on white paper, no interior bleed**.
- Cover spine width is calculated from the rendered interior page count using the KDP
  black-and-white white-paper factor (`pageCount × 0.002252 in`).
- The Contents page is generated from the final heading structure so later manuscript parts
  cannot silently be omitted.
- Interior page numbers are printed in the `@bottom-center` margin box (Chromium paged-media
  counter — *not* a fixed-position element, which renders as zero in this print path).
- Contents references are derived from the final rendered PDF and re-rendered until stable
  (up to 4 passes).
- Running headers are overlaid by `add-running-headers.py` via PyMuPDF after the PDF is
  printed; they are *not* part of the CSS layout.

### Enhancement layer (new — ReportLab)
- The ReportLab enhancement layer operates **after** the Chromium print pass. It reads a
  rendered chapter PDF and writes an enriched PDF that adds infographics, callout boxes, and
  visual explanations where the content warrants them.
- The enhancement layer must **never alter manuscript text**. It only adds visual elements
  alongside existing content.
- Visual additions use only the tokens from the existing design system (see §7).
- Any page-count change caused by the enhancement layer must be measured and the primary
  pipeline re-run so that spine width and Contents pagination stay correct.
- The enhancement layer is **optional per chapter** — chapters where flowing prose is
  sufficient receive no visual additions beyond the standard callout boxes.

---

## 5. KDP Production Requirements

These are hard constraints. No agent action may violate them.

| Requirement | Value |
|---|---|
| Trim size | 6 × 9 in |
| Interior colour | Black and white on white paper |
| Interior bleed | None |
| Inside margin (binding gutter) | 0.72 in (exceeds KDP 0.5 in minimum for 151–300 pp) |
| Outside margin | 0.56 in |
| Top margin | 0.65 in |
| Bottom margin | 0.68 in |
| Page numbers | Centered, bottom margin, every interior page |
| Spine width formula | `pageCount × 0.002252 in` (KDP B&W white paper) |
| Cover bleed | 0.125 in |
| Fonts | Embedded or PDF-safe only. Body: Georgia. Heads/UI: Arial/Helvetica. ReportLab: Helvetica family (built-in, no embedding required). |
| No interior colour | All ReportLab visuals must render legibly in greyscale/B&W print |
| Author name | Eleanor Mercer (everywhere — no other name) |
| AI disclosure | KDP requires disclosure of AI-*generated* content; AI-*assisted* editing/refinement does not require disclosure. Classify accurately. |

---

## 6. ReportLab Enhancement Layer — Full Specification

### 6.1 Purpose

The enhancement layer adds purposeful visual explanations to chapters where diagrams,
comparisons, frameworks, or callout boxes improve comprehension. It does not add decoration.

### 6.2 Visual decision rules

**Add a visual when the content is:**

| Content type | Visual pattern to use |
|---|---|
| Comparison or contrast (A vs B) | Side-by-side split panel |
| Numbered framework (3–7 items) | Icon card row or orbital wheel diagram |
| Process or sequence (step 1 → 2 → 3) | Horizontal flow/arrow diagram |
| Named before/after example | Annotated split panel |
| Warning or caveat | `WatchOutBox` callout |
| Exercise or action prompt | `TryThisBox` callout |
| Single most important sentence | `KeyTakeawayBanner` |
| Statistics or quantities | Bar or progress visual |

**Do NOT add a visual when the content is:**
- Pure narrative or explanation (flowing prose needs no illustration)
- A single point or list under 3 items
- A point already made clearly in a nearby existing table or diagram

**Frequency guideline:**
- Short chapters (< 8 pages): 1–2 visuals maximum
- Average chapters (8–12 pages): 2–4 visuals
- Long chapters (> 12 pages): up to 5 visuals
- Every chapter always gets: `ChapterHero` banner + at least one callout box

### 6.3 Install dependencies

```bash
pip install reportlab pypdf --break-system-packages
```

### 6.4 File structure for the enhancement layer

```
book-production/src/
  components.py        ← All reusable Flowable classes (shared across all chapters)
  enhance_chapter.py   ← Single-chapter enhancer: reads input PDF, builds story, writes output
  batch_enhance.py     ← Loops over book-production/chapters/*.pdf and enhances each

book-production/chapters/   ← Drop raw chapter PDFs here before running batch_enhance.py
book-production/output/     ← Enhanced chapter PDFs are written here
```

### 6.5 Color palette — use identically across ALL chapters

```python
from reportlab.lib import colors

NAVY       = colors.HexColor("#0D1B2A")   # headings, banners, dark backgrounds
TEAL       = colors.HexColor("#1B998B")   # primary accent, section dividers
GOLD       = colors.HexColor("#FFBC42")   # TryThis boxes, highlights
LIGHT_GRAY = colors.HexColor("#F4F6F9")   # table/card fills
MID_GRAY   = colors.HexColor("#8C9BAB")   # captions, footer text
WHITE      = colors.white
RED_ACCENT = colors.HexColor("#E84855")   # WatchOut boxes, warnings, negatives
SOFT_TEAL  = colors.HexColor("#D6F0ED")   # light teal fills
SOFT_GOLD  = colors.HexColor("#FFF4D6")   # light gold fills
```

> **B&W print note:** All colours above were chosen to produce sufficient contrast when
> converted to greyscale by a B&W printer. Do not introduce any colour that relies solely on
> hue to convey meaning — always pair colour with shape, position, or label.

### 6.6 Typography — Helvetica family only

ReportLab's built-in Helvetica family requires no font embedding and is PDF-safe.

| Role | Font | Size | Colour |
|---|---|---|---|
| Chapter title | Helvetica-Bold | 22 pt | NAVY |
| Section heading (H2) | Helvetica-Bold | 14 pt | NAVY |
| Sub-heading (H3) | Helvetica-Bold | 11 pt | TEAL |
| Body text | Helvetica | 10.5 pt | `#222222` |
| Callout body | Helvetica | 9.5 pt | varies |
| Caption | Helvetica-Oblique | 8.5 pt | MID_GRAY |
| Footer | Helvetica | 8 pt | MID_GRAY |

### 6.7 Page setup

```python
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

PAGE_W, PAGE_H = letter   # 8.5 × 11 in (agent preview/standalone)
# NOTE: The primary KDP interior uses 6×9 in via Chromium.
# The ReportLab layer produces standalone per-chapter PDFs at letter
# size for review. Final integration into the 6×9 pipeline is a
# separate merge step using pdf_text.py.

MARGIN    = 0.85 * inch
CONTENT_W = PAGE_W - 2 * MARGIN
```

### 6.8 Reusable Flowable components (all defined in components.py)

Every component below must be implemented in `components.py` and imported by
`enhance_chapter.py` and `batch_enhance.py`. Do not duplicate class definitions.

#### ChapterHero(w, chapter_num, chapter_title)
Navy rounded banner. Teal left accent bar. Gold decorative dots top-right. Chapter label in
teal. Title in white (auto word-wrapped). Gold underline bottom-left. Height: 1.55 in.

#### SectionDivider(w, text, icon_char="●")
Soft-teal pill background. Solid teal left badge with icon. Navy bold section text. Height:
0.52 in. Use before every major section heading.

#### KeyTakeawayBanner(w, text)
Full-width navy rounded rect. Faint teal quotation-mark decoration (alpha 0.18). White
bold-italic centred text (auto-splits to two lines if wider than `w - 80`). Gold underline.
Height: 0.9 in. Use for the single most important sentence per chapter.

#### TryThisBox(w, lines: list[str])
Soft-gold background, gold border (2.5 pt). Gold header bar: "✏  TRY THIS" in navy bold.
Body lines in Helvetica 9.5 pt, 18 pt line spacing. Empty string in `lines` renders as a
blank spacer line. Height calculated from `len(lines)`.

#### WatchOutBox(w, lines: list[str])
Light-red background, red border (2.5 pt). Red header bar: "⚠  WATCH OUT" in white bold.
Body lines in Helvetica 9.5 pt. Height calculated from `len(lines)`.

#### PageFooter(w, page_num, book_title)
Teal top rule (0.8 pt). Book title left-aligned, page number right-aligned. Helvetica 8 pt,
MID_GRAY. Height: 0.35 in.

### 6.9 Chapter-specific infographic pattern

For every new chapter, create chapter-specific Flowable classes following this pattern:

```python
class MyChapterInfographic(Flowable):
    """
    CHAPTER N SPECIFIC
    Content trigger: <describe what content type triggered this visual>
    Visual pattern: <split panel | icon cards | orbital wheel | flow diagram>
    """
    def __init__(self, w):
        Flowable.__init__(self)
        self.w = w
        self.h = 2.5 * inch   # set appropriate height

    def draw(self):
        c = self.canv
        # All drawing via c.setFillColor(), c.roundRect(), c.circle(),
        # c.drawString(), c.drawCentredString(), c.line(), etc.
        # Use CONTENT_W-relative positioning only — no hardcoded pixel coords
        # that assume a specific page width.
        pass

    def wrap(self, *args):
        return self.w, self.h
```

### 6.10 Document assembly pattern

```python
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from components import ChapterHero, SectionDivider, KeyTakeawayBanner, TryThisBox, WatchOutBox, PageFooter

def build_chapter(output_path, chapter_num, chapter_title, book_title):
    import os
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN, bottomMargin=MARGIN * 1.1,
        title=f"{book_title} — Chapter {chapter_num}",
        author="Eleanor Mercer",
    )
    story = []
    W = CONTENT_W

    # 1. Hero banner (every chapter)
    story.append(ChapterHero(W, chapter_num, chapter_title))
    story.append(Spacer(1, 18))

    # 2. Sections: SectionDivider + body paragraphs + optional infographics
    # ...

    # 3. TryThis or WatchOut boxes where present in manuscript
    # ...

    # 4. KeyTakeawayBanner for the chapter's core thesis
    # ...

    # 5. PageFooter
    story.append(PageFooter(W, starting_page_num, book_title))

    doc.build(story)
```

### 6.11 Batch runner pattern

```python
# batch_enhance.py
import os, glob
from enhance_chapter import build_chapter

CHAPTERS_DIR = "book-production/chapters"
OUTPUT_DIR   = "book-production/output"

for pdf_path in sorted(glob.glob(f"{CHAPTERS_DIR}/chapter*.pdf")):
    chapter_num = ...   # parse from filename
    try:
        out = os.path.join(OUTPUT_DIR, os.path.basename(pdf_path).replace(".pdf", "_enhanced.pdf"))
        build_chapter(out, chapter_num, ...)
        print(f"✅  Chapter {chapter_num} → {out}")
    except Exception as e:
        print(f"❌  Chapter {chapter_num} failed: {e}")
```

---

## 7. Design System Tokens — for ALL visual work in this project

These tokens apply to **both** the CSS print system (primary pipeline) and the ReportLab
enhancement layer. They are the single shared design language.

| Token | CSS variable | ReportLab hex | Role |
|---|---|---|---|
| Ink | `--ink` | `#202124` | Primary body text |
| Muted | `--muted` | `#66625c` | Secondary labels, captions |
| Rule | `--rule` | `#d8d1c6` | Secondary dividers |
| Wash | `--wash` | `#f3f0e9` | Quiet background panels |
| Accent | `--accent` | `#9d3427` → TEAL `#1B998B` | Key lines, active emphasis* |
| Accent dark | `--accent-dark` | `#6f241c` → NAVY `#0D1B2A` | Headings, strong emphasis* |
| Gold | — | `#FFBC42` | ReportLab callouts only |
| Red accent | — | `#E84855` | ReportLab warnings only |

> *The CSS pipeline uses a warm muted-red accent palette. The ReportLab enhancement layer
> uses NAVY/TEAL/GOLD — a cooler palette chosen for clarity at larger visual scale. Both are
> within the same editorial identity (restrained, editorial, non-decorative). Do not mix the
> warm reds into ReportLab infographics, and do not introduce the cool teal/navy into the
> base CSS layout.

---

## 8. Constraints — What Agents Must Never Do

1. **Never edit the manuscript.** `book-production/source/manuscript_part*.md` are read-only
   from the agent's perspective. Content lives in the manuscript; layout lives in the renderer.
2. **Never add invented content.** Do not add new facts, claims, examples, or chapter text
   that does not come from the manuscript source.
3. **Never hardcode `Mitesh Maharaj`.** The author is `Eleanor Mercer` everywhere.
4. **Never use external fonts** in the ReportLab layer. Helvetica family only.
5. **Never use HTML or browser-side CSS** in the ReportLab layer.
6. **Never use `localStorage` or `sessionStorage`** in any artifact or sandbox code.
7. **Never introduce new colour families** beyond the tokens in §7.
8. **Never increase body font size, alter trim dimensions, or change the body font stack**
   in `style.css`.
9. **Rebuild after any manuscript change** so the interior page count and cover spine stay
   synchronized (`pnpm run build:book`).
10. **Never skip the KeepTogether wrapper** around heading + first paragraph pairs in the
    ReportLab layer — orphaned headings at page breaks are a KDP quality failure.

---

## 9. Gotchas

- Chromium's fixed-position `counter(page)` renders as zero in this print path. Always use
  `@bottom-center { content: counter(page); }` margin boxes for page numbers.
- `ws.max_row` in openpyxl read-only mode may return `None` — iterate rows instead.
- PyMuPDF font insertion uses `fontfile=` path; confirm `/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf`
  exists in the deployment environment before running `add-running-headers.py`.
- The ReportLab `setFillAlpha()` call must be reset to `1` after any transparency effect or
  subsequent fills will be semi-transparent.
- `KeepTogether([heading, first_para])` prevents heading orphans. Use it wherever a
  `SectionDivider` is followed immediately by a `Paragraph`.
- Page count parity: the primary pipeline pads to an even page count. The ReportLab
  enhancement layer must not assume a fixed page count — always recalculate after render.
- ISBN and barcode placement still require publisher/KDP confirmation before upload.

---

## 10. Pointers

- See `book-production/README.md` for the detailed production build process.
- See `docs/BOOK_1_BIBLE.md` for positioning, USP, and the complete product specification.
- See `docs/editorial_system.md` for voice, anti-AI-slop rules, and reader language standards.
- See `docs/BOOK_VISUAL_POLISH_PLAN.md` for the design principles governing visual additions.
- See `docs/BOOK_IMPLEMENTATION_PLAN.md` for the phased revision plan and accepted changes.
- See `.agents/memory/` for renderer-specific memory (Chromium pagination rules, etc.).
- See `book-production/src/chapter1_sample_for_codex.py` for the annotated Chapter 1 reference
  implementation of the ReportLab enhancement layer.
