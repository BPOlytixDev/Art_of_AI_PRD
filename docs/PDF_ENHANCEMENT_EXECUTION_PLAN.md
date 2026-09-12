# KDP Chapter PDF Enhancement — Phased Execution Plan

## Scope

Recreate supplied chapter PDFs as visually enriched, KDP-ready PDFs using only
Python, ReportLab, pypdf, and the Python standard library. The source chapter
PDF is read for editorial analysis; the output is newly composed with Platypus
and vector canvas drawing. No HTML, browser conversion, raster assets, or
intermediate formats are used in this enhancement path.

The existing Markdown/Chromium book renderer remains a separate primary
pipeline. This plan applies to the chapter-PDF enhancement workflow only.

## Current repository state

- Enhancement modules exist in `book-production/src/`:
  `components.py`, `enhance_chapter.py`, and `batch_enhance.py`.
- The required Python packages are installed in `/tmp/art-of-ai-pdfvenv`:
  ReportLab, pypdf, and PyMuPDF. PyMuPDF is available for existing repository
  utilities, but it is not part of this pure enhancement implementation.
- TypeScript workspace typecheck passes.
- `book-production/chapters/` currently contains no chapter PDFs, so no
  chapter-specific visual decisions or output validation have been performed.

## Phase 0 — Input and baseline audit

1. Confirm the input set in `book-production/chapters/` and accept only files
   named `chapter01.pdf` through `chapter40.pdf` (or an explicitly documented
   equivalent).
2. For each PDF, use `pypdf.PdfReader` to extract page count and text.
3. Record extraction failures, empty pages, page dimensions, chapter number,
   chapter title, and the source page count in a review log.
4. Preserve the source PDFs unchanged. Outputs go to `outputs/` and use the
   names `chapter01_enhanced.pdf`, `chapter02_enhanced.pdf`, and so on.

## Phase 1 — Editorial content analysis

For every chapter, parse extracted text into a structured outline before
building any story. Identify:

- chapter number and title;
- section and subsection headings;
- body paragraphs;
- numbered and bulleted lists;
- comparisons, contrasts, and before/after examples;
- frameworks, models, and sequences;
- named examples or case studies;
- warnings, exercises, notes, and other callouts;
- quotes, pull quotes, summaries, and takeaways.

The classifier must describe evidence found in the source text. It must not
invent facts, examples, statistics, or manuscript prose. Any generated label
or caption must be a concise presentation of source content.

## Manuscript-driven chapter visual map

The chapter decisions below are based on the headings, lists, frameworks,
examples, and callouts in `book-production/source/manuscript_part1.md` through
`manuscript_part4.md`. They are a planning baseline, not permission to add
unseen content. During implementation, the exact source wording and available
page space must be rechecked from the input manuscript/PDF.

| Chapter | Manuscript trigger | Planned visual treatment |
|---|---|---|
| 1 | Slot-machine contrast; three input failures; Sarah before/after email; five inputs; Try This and Watch Out | Use the supplied Chapter 1 sample as the reference composition: comparison panel, three-card failure row, before/after panel, five-input wheel or compact card row, and the existing callouts. Keep the total restrained if the output is short. |
| 2 | Eleven-layer AI Interaction Stack; low-stack versus high-stack practice; diagnostic framework | Full-width layered stack diagram, then a compact low/high comparison. Use a Watch Out callout for “mental model, not procedure.” |
| 3 | Seven Questions; James interview-preparation worked example; portable card | Seven-step numbered card/grid or vertical checklist, followed by a worked-example flow from goal to next action. Use a KeyTakeaway or Try This only where the source callout supports it. |
| 4 | Search-engine habit versus conversational interaction; prompt anatomy; iterative conversation | Side-by-side search-query/conversation contrast and a labelled prompt-anatomy diagram. Use a short refinement loop for the conversation sequence. |
| 5 | Question versus job; Before → Better → Best; role types and actionable job structure | Before/Better/Best progression panel plus a role/action/deliverable/scope flow. Do not add examples beyond the manuscript’s CV and role examples. |
| 6 | Context gap; context test; David pricing example; constraint context; Before → Better → Best | Context-layer comparison using the David example and a context checklist/card. Keep constraint examples as text inside a callout or table rather than decorative repetition. |
| 7 | Specificity test; positive versus negative instructions; instruction types; Before → Better → Best | Specificity test split panel and positive/negative instruction comparison. Use a Watch Out for conflicting instructions. |
| 8 | Showing versus telling; tone, format, quality-standard, and negative examples; Before → Better → Best | Example taxonomy card row and a showing-versus-telling comparison. Use a Watch Out to distinguish style/format learning from factual accuracy. |
| 9 | Five output dimensions; practical format reference; mid-conversation corrections; Before → Better → Best | Five-dimension wheel or stacked control panel, followed by a revision loop. Keep the five dimensions legible as text reinforcement. |
| 10 | Three persistence strategies; worked first setup; workspace benefits; Sarah’s client Projects | Three-strategy comparison and a workspace map showing instructions, Projects, and context documents. Use the Sarah example as the annotated case panel. |
| 11 | Persistent-instruction template; five instruction categories; four project setup steps; recurring-work project | Five-part instruction card row and four-step project setup flow. Keep product note visually separated from stable principles. |
| 12 | Document types and uses; document-specific cautions; VERIFY and PRO TIP callouts | Document-type matrix or six-card reference grid. Add a verification path from document supplied → AI use → human check. |
| 13 | Web search; Deep Research; reliable research brief; web research checklist; code, image, and file tools; boundaries | Research brief six-step flow and a “changes / does not change” comparison. Use a warning boundary panel for sending, internal access, decisions, and professional advice. |
| 14 | Four types of memory; project/document workaround; context document; worth/not worth persisting | Four-layer memory model and worth/not-worth persistence comparison. Use a template-style context-document panel based only on the manuscript fields. |
| 15 | Workspace audit questions; client/report/personal structures; maintenance cycle | Workspace audit checklist plus three workspace patterns. Add a maintenance cycle with monthly, project-end, and recurring-problem checkpoints. |
| 16 | Single-prompt ceiling; three multi-stage patterns; David workflow example | Three workflow-pattern cards and a single-prompt versus workflow comparison. Preserve the human review points in the David example. |
| 17 | Three decomposition patterns; explicit handoffs; ordered steps | Three decomposition flows with a handoff marker between stages. Use Try This and Watch Out as source-backed callouts. |
| 18 | Critique loop; draft → critique → revise; critique types; adversarial persona | Circular three-stage critique loop and a critique-type matrix. Keep the adversarial-persona idea as a labelled variation, not a separate invented method. |
| 19 | Seven-stage David workflow; chains, loops, handoffs; disciplines and stopping rules | Seven-stage horizontal/vertical workflow with explicit human handoff nodes, plus a compact chain/loop/handoff legend. |
| 20 | Eight-question verification framework; high-risk/low-risk categories; Margaret example | Eight-question verification checklist and risk-category comparison. Use the source VERIFY box prominently; do not imply that AI self-verification is sufficient. |
| 21 | Eight failure categories and examples | Failure taxonomy grid, grouped by hallucination/currentness, reasoning/arithmetic, context/instruction drift, and sycophancy. Avoid a dense infographic that makes the long catalogue unreadable. |
| 22 | Stakes × verification difficulty trust-calibration matrix; David reliability bands | Two-axis trust matrix and a reliable/check/starting-point three-band panel. Keep the bidirectional over-trust/over-distrust warning visible. |
| 23 | Four habits; practical habit-building; week-in-the-life sequence | Four-habit card row and a weekly sequence. Use the source PRO TIP as the action callout. |
| 24 | Pace problem; fast versus stable knowledge; sustainable information diet; update triggers | Fast-changing versus stable principles comparison and a quarterly/update decision flow. Treat the appendices as separate reference pages, not as chapter decoration. |

The sample reference supports this approach: it uses a hero, section dividers,
source-backed callouts, comparison panels, card rows, a wheel, and text
reinforcement rather than illustrating every paragraph. Its five visuals across
five pages are a high-density Chapter 1 reference, not a target for every
chapter. The sample metadata author is `The Art of AI`; production outputs must
use `Eleanor Mercer` as required by the repository.

## Complete interior sequence

The enhanced chapter outputs are only one layer of the deliverable. The final
interior must be assembled as a single continuous book in the following source
order. Page starts, page endings, headers, footers, and Contents references
must be validated after the complete assembly, not inferred from individual
chapter files.

### Front matter

1. **Title page** — `THE ART OF AI`, subtitle, deck, series line, author name,
   and dedication. Use a quiet title treatment with deliberate whitespace; do
   not place a running header on this page.
2. **Copyright and publication page** — copyright notice, publisher, series,
   edition, AI disclosure, and dated KDP policy reminder exactly as supplied in
   the manuscript. Set the author identity consistently to Eleanor Mercer.
3. **Contents** — generated from the final assembled page map. Include the
   Introduction, Parts I–VI, Chapters 1–24, Part V workflow categories and
   workflows, Appendices A–E, A Note on Sources, About the Author, and About
   This Book where the final interior design exposes them as navigable entries.
   Use dot leaders and a bounded page-number column; never hand-type page
   references.

Front matter uses lowercase or unnumbered treatment only if that choice is
supported by the final KDP pagination implementation. Otherwise retain a
single physical page counter and suppress visible numbers on the title,
copyright, and Contents pages through the approved interior convention.

### Introduction and part openers

4. **Introduction** — “You Are Not Bad at AI,” including its “What you will
   actually learn,” framework, and technical-knowledge sections. Treat this as
   a short opening essay with one restrained framework callout, not as a
   numbered chapter.
5. **Part I opener** — “A Different Way to Think About AI,” including the
   supplied part overview and four-chapter overview card/grid. Then Chapters 1–4
   in sequence.
6. **Part II opener** — “Build Better Interactions,” with its overview, then
   Chapters 5–9.
7. **Part III opener** — “Build an AI Environment,” with its overview, then
   Chapters 10–15.
8. **Part IV opener** — “From Prompts to Workflows,” with its overview, then
   Chapters 16–19.
9. **Part V opener** — “25 Real-World Workflows.” Use the workflow navigator
   and category structure already present in the manuscript. Render all 25
   workflows W1–W25 as usable reference entries, with category dividers for
   Business and Professional, Marketing and Content, Research and Learning,
   Personal Productivity, Home and Life, and Writing and Editing. Do not treat
   workflows as ordinary chapters or omit their category navigation.
10. **Part VI opener** — “The AI User’s Playbook,” with its overview, then
    Chapters 20–24.

Each part opener begins on a fresh page. The part label, title, overview copy,
and overview cards belong together where space permits. If the overview cannot
fit cleanly, move the complete overview to the next page rather than leaving a
heading and a few lines stranded at the bottom of the opener. Chapter openers
follow the same rule: a chapter hero and its first explanatory block stay
together, while the body may continue naturally.

### Appendices and end matter

11. **Appendices opener** — a clear transition from Part VI into reference
    material.
12. **Appendix A** — “The 7 Questions, Quick Reference Card.” Treat the seven
    questions as a compact, printable reference layout with enough white space
    to scan quickly.
13. **Appendix B** — “The Before → Better → Best Worksheet.” Preserve the
    worksheet sequence and provide writing space without adding prompts or
    examples.
14. **Appendix C** — “Verification Checklist.” Keep the eight-question
    checklist and risk-calibrated guide together where possible; separate the
    error-response sequence only when page fit requires it.
15. **Appendix D** — “AI Use Cases by Profession.” Use profession category
    dividers and consistent treatment for valuable use cases, key workspace
    elements, and caution areas. Keep each profession’s block together when
    practical; do not shrink the body type to force a fit.
16. **Appendix E** — “Product Notes, Platform-Specific Information.” Separate
    stable cross-platform principles from volatile product notes. Keep the
    verification date and volatility warnings visible. These are reference
    pages, not decorative infographic pages.
17. **A Note on Sources** — render as a short end-matter essay with clean
    source-category headings.
18. **About the Author** — render Eleanor Mercer’s supplied biography, the
    approved author photo from `attached_assets/`, and the website line in the
    primary interior pipeline. The pure ReportLab enhancement path must not
    invent a substitute portrait or require an external image; the approved
    asset is a primary-pipeline exception explicitly present in the manuscript.
19. **About This Book and colophon** — include the series description, AI-use
    disclosure, publication year, and first-edition line as supplied. Keep this
    as the final reader-facing page or final coherent end-matter block.

## End-to-end assembly and flow contract

The complete interior builder must use a single ordered story or an equivalent
single-pass assembly model. It must not concatenate visually incompatible
chapter PDFs and hope that page furniture aligns. The assembly contract is:

- manuscript order is the authority for content order;
- chapter-specific visuals are inserted only at source-backed trigger points;
- page dimensions, margins, body typography, and footer treatment are
  consistent across front matter, parts, workflows, chapters, and appendices;
- part openers, chapter heroes, appendix openers, and the Contents page are
  explicit layout boundaries;
- headings never appear as the final isolated element on a page;
- short callouts, diagrams, workflow steps, and worksheet blocks use
  `KeepTogether` or controlled splitting so they do not break into unusable
  fragments;
- long prose and tables may flow across pages, but each continuation begins
  with enough context to remain intelligible;
- no page is padded with invented copy, decorative filler, or a forced blank
  area merely to reach a target page count;
- any intentional blank verso page required by the chosen KDP opening
  convention is recorded in the assembly manifest;
- the final physical page count is measured after all page furniture, then
  checked for even parity if the production specification requires it;
- Contents references, running-header ranges, metadata, and any cover-spine
  calculation are derived from the final measured interior.

### Page-start and page-end review

After the first complete render, generate a page manifest containing page
number, opening element, closing element, extracted text length, and visual
blocks. Review every page boundary for:

1. isolated section or chapter headings;
2. a new section beginning with only one to three lines before continuation;
3. split callouts, diagrams, tables, worksheets, or workflow steps;
4. excessive blank space caused by an over-large `KeepTogether`;
5. a part, chapter, appendix, or end-matter transition that lacks a clear
   opening page;
6. footer/header collisions or inconsistent page furniture.

Correct problems in this order: adjust local spacing, split a visual at a
semantic boundary, move a complete section opener, then revise the visual’s
height or text density. Do not globally change body font size, trim, or margins
to hide a local pagination defect. Repeat the full render and Contents mapping
until stable.

## Phase 2 — Component and layout implementation

Implement and reuse these Flowables in `components.py`:

- `ChapterHero`
- `SectionDivider`
- `KeyTakeawayBanner`
- `TryThisBox`
- `WatchOutBox`
- `PageFooter`

Implement chapter-specific infographic Flowables only when Phase 1 identifies
a matching content trigger:

- comparison → side-by-side split panel;
- 3–7 item framework → icon-card row or orbital wheel;
- sequence → horizontal flow diagram;
- before/after → annotated split panel;
- quantities → labelled bar/progress visual;
- warning or exercise → styled callout.

Use the supplied NAVY, TEAL, GOLD, gray, white, red, soft-teal, and soft-gold
tokens consistently. Use only Helvetica-family fonts. All drawing must be
vector canvas operations, and all text must be ReportLab `Paragraph` or canvas
text. Do not use Unicode subscript or superscript characters.

## Phase 3 — Page-flow and KDP layout rules

Build each output with `SimpleDocTemplate`, letter pagesize, and 0.85-inch
margins as specified by the task. Every chapter receives a hero and at least
one relevant callout. Visual frequency is limited by source page count:

- under 8 pages: 1–2 visuals;
- 8–12 pages: 2–4 visuals;
- over 12 pages: no more than 5 visuals unless review explicitly approves it.

Prevent abrupt page endings using these rules:

1. Wrap every section heading with its first paragraph in `KeepTogether`.
2. Keep each infographic with its heading, lead-in, and caption where it fits.
3. Use `KeepTogether` for short callout blocks and list introductions.
4. Use `PageBreak` only when a section or chapter opener would otherwise leave
   an orphaned heading or an unusable fragment at the bottom of the page.
5. Let long prose flow naturally; do not force every paragraph onto a new page.
6. After rendering, inspect page occupancy and adjust spacing, split long
   visuals, or move the complete section opener so pages begin with a chapter,
   section, or coherent continuation rather than three isolated lines.
7. Do not create blank pages merely to improve symmetry.

## Phase 4 — Single-chapter implementation and validation

Before batch processing, implement and test one representative chapter:

1. Extract and classify its content.
2. Build `chapter01_enhanced.pdf` (or the first available chapter).
3. Confirm PDF metadata title and author (`Eleanor Mercer`).
4. Confirm the output opens with `pypdf`, has the expected page size, contains
   selectable text, and contains no raster image dependencies.
5. Check that every page has readable margins, no clipped text, no overlapping
   visual elements, and no orphaned section heading.
6. Check the chapter hero, at least one callout, and every selected infographic
   against the supplied palette and typography.
7. Compare source and output text semantically to ensure no manuscript content
   was silently omitted or rewritten.
8. Record findings and corrections in the plan's validation log or a companion
   QA report before proceeding.

## Phase 5 — Batch processing

`process_chapter(input_pdf_path, output_pdf_path, chapter_num)` will be the
single-chapter entry point. `main()` will iterate over sorted chapter PDFs,
write one output per input, and continue after an error while logging exactly:

- `✅ Chapter N complete`
- `❌ Chapter N failed: reason`

Each chapter is processed independently. A failed chapter must not produce a
misleading success output, and the batch summary must list missing, completed,
and failed chapter numbers.

## Phase 6 — Batch QA and release gate

For every output:

- verify naming and one-to-one input/output coverage;
- verify metadata, page dimensions, page count, and text extraction;
- verify fonts are Helvetica-family and PDF-safe;
- verify visuals are vector-only and legible in grayscale;
- inspect page starts and endings for abrupt fragments or excessive blank space;
- check for clipped content, overflows, overlaps, and orphaned headings;
- compare extracted source/output content for preservation;
- retain a machine-readable QA summary and a human review list.

The batch is not release-ready until every supplied chapter either passes these
checks or has an explicitly documented exception approved for that chapter.

## Deliverables

- `book-production/src/components.py` — shared vector Flowables;
- `book-production/src/enhance_chapter.py` — extraction, classification,
  single-chapter build, and validation hooks;
- `book-production/src/batch_enhance.py` — independent batch runner;
- `book-production/outputs/chapterNN_enhanced.pdf` — one output per input;
- a QA report documenting page-flow decisions and validation results.

## Entry condition

Implementation and chapter-level validation begin when one or more source PDFs
are placed in `book-production/chapters/`. Until then, only the repository
scaffold and this execution plan can be reviewed; no chapter-specific visual
design should be invented.
