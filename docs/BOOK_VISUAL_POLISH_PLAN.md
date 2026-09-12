# The Art of AI — Book 1
## Interior Design, Structure, and Visual Polish Implementation Plan

**Status:** Implemented and mechanically QA-checked on 2026-09-11  
**Scope:** Interior PDF design, structure, visual teaching aids, and production QA  
**Current source of truth:** `book-production/source/` plus `docs/manuscript_part4.md` for Part VI and Appendices  
**Renderer:** `book-production/src/build-book.mjs`, `markdown.mjs`, and `style.css`  
**Current proof reviewed:** 206-page interior PDF, 6 × 9 in trim, black and white interior with muted red accent

This plan was implemented as the source-driven visual polish pass. The implementation record below identifies the completed changes and the remaining publication-gate checks.

## 1. Review summary

The current interior has a coherent editorial identity:

- restrained charcoal, warm paper, and muted red palette;
- readable serif body text paired with sans-serif headings;
- clear part and chapter hierarchy;
- generous margins and white space;
- consistent callout boxes and prompt blocks;
- clean part opener pages;
- a useful Part V workflow navigator;
- compact, professional cover/interior alignment.

The book currently reads as a strong text-led guide. Its main opportunity is not a new design direction; it is adding a small number of purposeful visual explanations so that the framework-driven material is easier to understand and easier to revisit as a reference.

## 2. Issues that must be addressed before visual additions

### 2.1 Index collision — production blocker

The index is technically single-column, but long page-number lists still run into neighbouring entries. This is visible on the rendered index page: terms and page references collide or wrap into the next entry.

**Required fix:** change the index entry layout from a flexible two-item row into a controlled term/reference layout.

**Implementation:**

1. Keep the index as one column.
2. Render each entry as a two-column CSS grid:
   - term column: `minmax(0, 1fr)`;
   - page-reference column: fixed or bounded width.
3. Allow page references to wrap within their own column using `overflow-wrap: anywhere` or grouped page-number spans.
4. Set `min-width: 0` on both grid children.
5. Keep each index entry together with `break-inside: avoid`.
6. Use a hanging indent only on the term column, not on the complete row.
7. Validate the rendered text blocks with PyMuPDF coordinates so no term and page-number bounding boxes intersect.

This is a layout repair, not a content rewrite.

### 2.2 Confirm running-header stability

The running-header overlay was recently corrected. It should remain a formal regression check during this pass:

- no character-spacing corruption;
- no header on part/chapter opener pages where the design intentionally leaves the top area quiet;
- correct left/right placement on verso/recto pages;
- no header collision with the body text;
- header text remains readable at print size.

### 2.3 Protect the existing typography

The current body typography and page geometry should remain the baseline. Visual additions must not globally increase font sizes, alter the trim, or change the body font stack.

Any page-count increase caused by diagrams must be explicit and measured because it changes the cover spine width and contents pagination.

## 3. Design principles for the polish pass

### Preserve the existing system

All new visuals should use the existing design tokens:

- `--ink` for primary text;
- `--muted` for secondary labels;
- `--accent` for active emphasis and key lines;
- `--accent-dark` for headings;
- `--wash` for quiet panels;
- `--rule` for secondary dividers.

No new colour family, decorative illustration style, or unrelated font should be introduced.

### Prefer explanation over decoration

Every visual must answer one of these reader questions:

- What are the parts of this framework?
- How does this process move from one stage to another?
- Which option should I choose?
- What should I check before trusting the result?
- Where should I start?

Visuals should not be added merely to fill white space.

### Use vector-first production

Diagrams should be produced as inline SVG or HTML/CSS components rather than screenshots or low-resolution images.

This will provide:

- sharp print output at KDP resolution;
- predictable black-and-white conversion;
- no external image licensing dependency;
- consistent typography and colour;
- easy regeneration when page numbers change.

### Do not invent manuscript claims

The diagrams should be derived from existing headings, lists, frameworks, and workflow metadata. Any new explanatory prose, labels, or examples must be approved separately. The planned pass can add visual structure without rewriting the manuscript.

## 4. Proposed visual additions

### Priority 1 — AI Interaction Stack diagram

**Location:** Chapter 2, immediately after the introduction to the Stack and before the layer-by-layer explanations.

**Purpose:** Give readers a spatial model of the eleven layers before they encounter the detailed descriptions.

**Format:** One-page or half-page vertical stack of eleven labelled boxes.

**Content source:** Existing layer names in Chapter 2. Use the existing labels only; descriptions remain in the prose.

**Visual treatment:**

- numbered boxes;
- accent rule on the active layer edge;
- alternating white and warm-wash fills;
- compact arrows or a continuous vertical spine;
- a small note that the Stack is a diagnostic model, not a mandatory eleven-step procedure, using the existing manuscript wording if retained.

**Implementation:**

- Add a renderer helper such as `renderInteractionStackDiagram()` in `markdown.mjs` or a dedicated `visuals.mjs` module.
- Insert it using an explicit source marker, for example `<!-- VISUAL: interaction-stack -->`.
- Render semantic HTML plus inline SVG lines/arrows.
- Add `.visual-diagram`, `.stack-diagram`, and print-safe child styles to `style.css`.
- Apply `break-inside: avoid` and reserve enough height that the diagram cannot split across pages.

### Priority 1 — Seven Questions flow/card

**Location:** Chapter 3, after the first complete introduction of the framework. Appendix A remains the printable reference card.

**Purpose:** Make the framework memorable in the main narrative, not only in the appendix.

**Format:** Seven compact numbered cards arranged as a vertical decision flow or two-column sequence.

**Content source:** Existing Q1–Q7 labels and their current short explanations.

**Implementation:**

- use a reusable `question-card` component;
- keep the cards short and link each to the detailed section already present in the chapter;
- use CSS grid for print stability rather than a flex row that may wrap unpredictably;
- use a vertical fallback at narrow print widths;
- keep the appendix version more compact and printable.

### Priority 1 — Chains, loops, and handoffs workflow diagram

**Location:** Chapter 19, alongside or immediately before the existing worked workflow.

**Purpose:** Turn the most abstract workflow chapter into a concrete visual sequence.

**Format:** A process diagram showing:

```text
Chain → Loop → Human handoff → Next stage
```

The diagram should also show that a loop can return to an earlier stage and that a handoff is a deliberate control point.

**Content source:** Existing Chapter 19 definitions and seven-stage example.

**Implementation:**

- create the diagram as inline SVG with labelled nodes and arrows;
- use a different border treatment for AI stages and human handoff stages;
- include a print-safe legend using existing terminology;
- place the visual before the detailed explanation if the chapter is later restructured;
- ensure the diagram is readable in grayscale.

### Priority 1 — Verification risk matrix

**Location:** Chapter 20, after the Verification Framework is introduced.

**Purpose:** Help readers choose a proportionate verification effort.

**Format:** A two-axis matrix:

- horizontal axis: low to high consequence;
- vertical axis: easy to verify to difficult to verify.

**Content source:** Existing verification principles and risk-based guidance.

**Implementation:**

- use an HTML table/grid with four to six labelled cells;
- use the existing muted palette rather than traffic-light colours;
- keep text to existing concepts such as source checking, calculation checking, expert review, and human judgment;
- include a visible caption stating that verification should be proportionate to stakes.

### Priority 2 — Part V workflow route map

**Location:** Part V opener, before W1.

**Purpose:** Improve navigation through the 25-workflow reference library.

**Format:** A visual three-lane route map:

- Quick win;
- Medium build;
- Deep work.

Each lane contains the existing workflow IDs from the current navigator table.

**Implementation:**

- retain the existing table as the accessible/text reference unless testing shows it can be safely replaced;
- add a visual lane component above or beside it only if it fits without pushing W1 unnecessarily;
- generate the workflow IDs from the same data structure used by the Contents and workflow headings so the map cannot drift;
- use small complexity/time badges at the start of each workflow page, derived from the same classification.

### Priority 2 — Workflow complexity markers

**Location:** Each W1–W25 heading or workflow metadata block.

**Purpose:** Let readers scan for a suitable starting point without reading every Situation paragraph.

**Format:** Small, consistent metadata line:

```text
TIME: 5 MINUTES · COMPLEXITY: QUICK WIN
```

**Implementation:**

- define a single workflow metadata object in `build-book.mjs`;
- use it to generate the Part V navigator and the per-workflow marker;
- do not manually duplicate classifications in the manuscript;
- keep the marker visually subordinate to the workflow title.

### Priority 2 — Tools capability map

**Location:** Chapter 13.

**Purpose:** Make the text, web search, code execution, file, and image capabilities easier to compare.

**Format:** Four- or five-cell capability map with a consistent structure:

- capability;
- what it enables;
- what still needs checking.

**Content source:** Existing Chapter 13 sections.

**Implementation:**

- use the existing callout/card language;
- avoid screenshots of rapidly changing product interfaces;
- keep platform-specific details in Appendix E and use durable capability labels in the diagram;
- create the map as HTML/CSS so it remains editable and printable.

### Priority 3 — Failure taxonomy reference grid

**Location:** Chapter 21 and optionally Appendix C.

**Purpose:** Make the eight failure categories usable as a quick-reference tool.

**Format:** Two-column or four-by-two grid of the existing failure categories.

**Implementation:**

- derive labels from the chapter headings/data;
- use a small icon or geometric marker only if it remains clear in black and white;
- pair the grid with a short “what to check” line only where that line already exists in the manuscript;
- create a downloadable companion version later from the same source data.

### Priority 3 — Appendix A and C reference treatment

**Appendix A:** Treat the seven-question card as a deliberate printable card with a border, clear cut line, and compact hierarchy. Preserve the current single-page requirement.

**Appendix C:** Add checkbox styling, grouped verification stages, and a clearly separated “stop and investigate” area using existing checklist content.

**Implementation:**

- use CSS pseudo-elements or Unicode-safe square boxes only after font round-trip testing;
- prefer CSS-drawn empty squares if glyph substitution is a concern;
- keep the actual content unchanged;
- provide a print-friendly layout with no background dependency for meaning.

## 5. Visual hierarchy improvements that do not require new content

### Callout differentiation

The current callouts are clean but visually similar. Add a restrained system:

- `TRY THIS` and `WATCH OUT`: stronger accent border;
- `VERIFY`: darker or double rule;
- `WHY IT WORKS` and `PRO TIP`: lighter explanatory rule;
- `REAL-WORLD EXAMPLE`: warm-wash panel with a small label marker.

This should be done with border weight, spacing, and existing colours, not large shaded blocks.

### Chapter and workflow opener rhythm

Keep chapter openers text-led, but add a small visual orientation line under the chapter title where appropriate:

- framework chapter;
- workflow chapter;
- reference/checklist chapter.

These markers should be generated from heading classes and should not alter body font sizing.

### Contents navigation

After the index collision is fixed, review the Contents pages for:

- minimum readable type size;
- consistent indentation of workflows and appendix children;
- clear separation between Parts, chapters, and reference material;
- page numbers aligned on a stable right edge.

No Contents compression should be attempted until the final page count is known.

## 6. Technical implementation plan

### 6.1 Add a visual component layer

Create a small renderer module, preferably:

```text
book-production/src/visuals.mjs
```

It should export pure functions such as:

```text
renderInteractionStackDiagram()
renderSevenQuestionsVisual()
renderWorkflowMechanicsDiagram()
renderVerificationMatrix()
renderWorkflowRouteMap()
renderFailureTaxonomyGrid()
```

The functions should return deterministic HTML/SVG strings and contain no page-specific absolute coordinates.

### 6.2 Use explicit source markers

Insert visual markers at intentional manuscript locations, for example:

```html
<!-- VISUAL: interaction-stack -->
```

The Markdown renderer should recognize these markers and replace them with the corresponding visual component. This keeps visual placement with the manuscript flow while keeping the diagram implementation in the layout layer.

### 6.3 Keep data single-sourced

Create data definitions for:

- Stack layers;
- Seven Questions;
- workflow IDs, time bands, and complexity bands;
- failure categories;
- verification stages.

Use those definitions for diagrams, navigators, labels, and any future downloadable companion assets.

### 6.4 Establish print-safe CSS primitives

Add reusable styles for:

- `.visual-diagram`;
- `.diagram-caption`;
- `.diagram-key`;
- `.card-grid`;
- `.flow-node`;
- `.flow-arrow`;
- `.risk-matrix`;
- `.workflow-meta`;
- `.reference-card`.

Every visual style must include:

- `break-inside: avoid`;
- print colour preservation;
- grayscale-safe borders;
- predictable minimum/maximum heights;
- a narrow-column fallback;
- no reliance on hover, animation, or external fonts.

### 6.5 Keep SVG accessible and robust

Each SVG should include:

- a descriptive `role="img"`;
- an `aria-label` or adjacent text caption;
- text labels duplicated in the HTML when the visual carries essential meaning;
- no external image or font references;
- stroke widths large enough for print reproduction.

## 7. Page-budget and sequencing rules

The current book is 202 interior pages. Visual additions should be controlled to avoid unnecessary expansion.

Target page budget:

- Priority 1 diagrams: up to 4 additional pages;
- Priority 2 visuals: up to 3 additional pages;
- Priority 3 appendix/reference refinements: up to 2 additional pages;
- index repair: no intentional page increase unless unavoidable.

Target total after polish: approximately 204–211 interior pages, subject to actual layout.

If a visual forces a new page, it must be reviewed as a complete spread decision. Do not allow a diagram to create a nearly empty page or orphan the next heading.

## 8. Execution phases after approval

### Phase 0 — Baseline and repair

1. Copy the current PDFs into a temporary proof baseline.
2. Repair index collisions.
3. Confirm running-header placement.
4. Record current page count, trim, fonts, and Contents map.

### Phase 1 — Visual primitives

1. Add `visuals.mjs`.
2. Add marker handling to `markdown.mjs`.
3. Add print-safe visual CSS.
4. Add deterministic data definitions.
5. Render one test diagram and inspect at print scale.

### Phase 2 — Core framework visuals

Implement and proof:

1. AI Interaction Stack;
2. Seven Questions;
3. Chains, loops, and handoffs;
4. Verification risk matrix.

These deliver the greatest reader value and should be completed before decorative refinements.

### Phase 3 — Workflow navigation

1. Build the Part V route map.
2. Add workflow metadata markers.
3. Review repeated workflow pages for monotony without changing their established structure.

### Phase 4 — Reference and appendix polish

1. Redesign Appendix A as a stronger printable card.
2. Improve Appendix C checklist scanning.
3. Add failure taxonomy grid.
4. Review the Contents and Index at final extent.

### Phase 5 — Final proof and production outputs

1. Rebuild the interior.
2. Recalculate Contents page numbers and index references.
3. Rebuild running headers.
4. Recalculate cover spine width.
5. Rebuild full-wrap cover and complete-book PDF.
6. Run KDP preflight checks.
7. Render representative pages and review visually.
8. Record the final page count and outstanding issues in the QA report.

## 9. Acceptance criteria

The polish pass is complete only when:

- the index has no term/page-reference collisions;
- all headers are normal, correctly positioned, and absent from intentional opener pages;
- no visual splits across pages unexpectedly;
- all diagrams remain readable in grayscale and at print size;
- no diagram introduces unsupported or missing glyphs;
- no body typography changes occur outside approved visual components;
- the Contents matches the final PDF page map;
- the interior remains 6 × 9 in with correct alternating margins;
- the interior page count is even;
- the full-wrap cover spine reflects the final page count;
- no interior author/about pages are reintroduced;
- no em dashes are present in the rendered interior;
- the complete-book PDF contains exactly one cover page followed by the interior;
- representative pages have been inspected at 100% and high-resolution render scale.

## 10. Implementation record

The approved visual polish pass has been executed end to end:

1. Repaired the single-column Index layout and regenerated its page references from the final rendered PDF.
2. Added source-marked visuals for the AI Interaction Stack, 7 Questions, tools capability map, workflow mechanics, verification matrix, Part V route map, and failure taxonomy.
3. Added workflow complexity/time metadata and retained the existing workflow structure and typography.
4. Added Appendix A card treatment and Appendix C checkbox/reference styling without changing the checklist prose.
5. Preserved the original body font stack, trim, margins, and editorial flow.
6. Corrected the contents/page-map resolver so chapter entries point to their actual chapter openers rather than part-opener cards.
7. Regenerated running headers with an embedded DejaVu Sans font, eliminating the previous malformed character-spaced header issue and avoiding a non-embedded Helvetica overlay.
8. Rebuilt the interior, full-wrap cover, complete-book PDF, and metadata from `docs/manuscript_part4.md`; the obsolete Part IV/Appendices source file is deleted.
9. Completed mechanical artifact QA and representative high-resolution visual inspection.

The final outputs are 206 interior pages, 1 cover page, and a 207-page complete-book PDF. The remaining publication gates are the KDP Print Previewer, a physical proof, and the author-controlled provenance/website decisions listed in the QA report.
