# The Art of AI — Index and Running-Header Implementation Plan

**Status:** Awaiting approval — planning only  
**Prepared:** 2026-09-11  
**Scope:** Book 1 interior navigation and reference value  
**Execution status:** No manuscript, renderer, CSS, PDF, cover, or metadata changes are authorised by this document.

## 1. Decision requested

Approve a focused navigation pass that adds:

1. running headers to the body and reference sections; and
2. a curated, page-accurate back-of-book index.

The pass must preserve the current book flow, 6 × 9 trim, author identity, front/back-matter order, verification thread, and existing Contents-generation process. It must not become an uncontrolled rewrite or a broad typography redesign.

## 2. Validated baseline

The current production pipeline is a Markdown → HTML/CSS → Chromium PDF renderer. The final interior is currently 214 pages at 6 × 9 inches, with mirrored inside/outside margins, a generated page number, and a Contents page whose entries are recalculated from extracted PDF text. The renderer currently has no running-header implementation, no index data model, no index pages, and no source-to-page index markers.

The editorial system explicitly includes “indexes where appropriate” in the production gate and treats navigation, Contents, references, and paperback/Kindle rendering as production checks. The prior QA report correctly leaves both running headers and the index deferred until a dedicated visual/navigation pass.

The second editorial review’s recommendation is therefore valid, but implementation must account for two facts:

- page numbers are not stable until the final PDF has been rendered; and
- an index is not reliable if it simply lists every textual occurrence of a word.

The current Contents convergence loop is the right model to extend: render, measure the PDF, update generated navigation data, and render again until the map and page count stabilise.

## 3. Research and standards validation

### Running headers

CSS paged-media standards define page margin boxes and named strings for running headers. The W3C Generated Content for Paged Media specification specifically describes `string-set`, `string()`, `position: running()`, and `element()` for this purpose. [W3C CSS Generated Content for Paged Media](https://www.w3.org/TR/css-gcpm-3/)

Modern Chromium supports `@page` margin content in print output from Chrome 131 onward, including top/bottom margin boxes and page counters. The Chrome documentation also warns that margin content depends on there being sufficient page margin space, so support must be proven in this exact renderer and geometry rather than assumed. [Chrome for Developers — Add content to the margins of web pages when printed](https://developer.chrome.com/blog/print-margins?hl=en)

MDN confirms the relevant `@page` margin at-rules and cautions that browser support is not uniform for every paged-media feature. [MDN — `@page`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40page)

**Validation conclusion:** use a small local support spike before changing the book. If Chromium correctly renders dynamic named strings and left/right margin boxes in the existing pipeline, CSS margin boxes are the preferred implementation. If not, do not ship empty or inconsistent headers; evaluate a tested pagination/polyfill or post-PDF overlay alternative only after a visual proof.

### Print geometry

KDP identifies 6 × 9 inches as a regular paperback trim size and states that 151–300-page books require at least a 0.5-inch inside margin, with minimum outside margins dependent on bleed. Header text must remain inside the safe text area and must not reduce the effective gutter below the KDP requirement. [KDP — Set Trim Size, Bleed, and Margins](https://kdp.amazon.com/en_US/help/topic/GVBQ3CMEQW3W2VL6), [KDP — Paperback Submission Guidelines](https://kdp.amazon.com/en_US/help/topic/G201857950)

KDP’s paperback guidance also supports adding page numbers to a table of contents and treats chapter headings, author bio, and other front/body/back matter as normal interior production elements. [KDP — Paperback and Hardcover Manuscript Templates](https://kdp.amazon.com/en_US/help/topic/G201834230)

**Validation conclusion:** headers are permissible, but they must be tested against the final extent, mirrored margins, tables, callouts, chapter openers, and print-preview safe areas. Any page-count change must flow through the existing cover-spine and complete-book rebuild process.

## 4. Running-header design specification

### Intended reader-facing behaviour

Use the convention requested by the editorial review:

- **Left/verso pages:** current Part label, for example `PART II — BUILD BETTER INTERACTIONS`.
- **Right/recto pages:** current chapter, workflow, appendix, or other active section title, shortened only where necessary for the header line.
- **Part openers, chapter openers, title/dedication/copyright/Contents pages, blank pages, and the final colophon:** no running header.
- **Appendices:** left pages use `APPENDICES`; right pages use the current appendix title or subsection where it improves retrieval.
- **Part V workflows:** left pages use `PART V — 25 REAL-WORLD WORKFLOWS`; right pages use the current workflow title. Category divider pages remain unheaded.

Header styling should be restrained and monochrome: approximately 7.5–8 pt sans-serif, muted ink, optional hairline rule, no colour-only meaning, and enough top margin to prevent collision with body text. The existing bottom-centre page number remains unless the proof shows that a mirrored outer page number is materially better; changing page-number placement is outside this pass unless separately approved.

### Technical implementation

1. Add semantic classes/data to the generated part, chapter, workflow, appendix, and back-matter headings rather than relying on visual selectors alone.
2. Add explicit running values for the current Part and current section title.
3. Add `@page:left` and `@page:right` margin-box rules only after the support spike passes.
4. Suppress headers on the defined opener/front/back-matter page classes.
5. Add a stable short-header override for long titles; never allow a header to wrap to two lines without an intentional design decision.
6. Keep the body text’s top line position and KDP gutter safe area measurable in the PDF.

### Support-spike acceptance test

Before production implementation, create a temporary test HTML containing:

- two parts;
- two chapters with long and short titles;
- a page break before a chapter;
- a left and right page;
- a table and a callout;
- a first page and a blank page.

Print it with the same Chromium command and inspect extracted text plus rasterised pages. The test passes only if the correct current strings appear on the correct page sides, headers are absent where suppressed, and no body text is displaced or clipped.

If the test fails, the fallback decision hierarchy is:

1. test a maintained paged-media layer such as Paged.js, whose documentation explicitly covers named strings and generated margin-box headers; [Paged.js — Generated Content in Margin Boxes](https://pagedjs.org/en/documentation/7-generated-content-in-margin-boxes/)
2. if that introduces unacceptable pagination drift, use a deterministic PDF overlay pass with measured page geometry and a visual proof; or
3. defer headers for this edition and record the reason in the QA report.

No fallback is approved merely because it produces text at the top of a PDF; it must preserve the existing page flow and pass KDP-oriented geometry checks.

## 5. Index design specification

### Placement

Place the Index after Appendix E and before `A Note on Sources`. This gives the book a conventional reference section without disturbing the already-approved closing sequence:

`A Note on Sources → About the Author → About This Book → colophon`

The Index must be added to Contents and must not displace or reorder the author, About This Book, or colophon blocks.

### Editorial policy

Build a selective index, not a concordance. Include a term when it is useful for retrieval and the page contains a definition, framework explanation, worked example, workflow, verification rule, or substantive comparison. Exclude incidental mentions, generic uses of “AI”, repeated navigation labels, and pages where the term adds no retrieval value.

Initial candidate vocabulary, to be reviewed before implementation:

- 7 Questions; AI Interaction Stack; context; context drift; intent; role; instructions; examples; constraints; output format;
- hallucination; outdated information; over-generalisation; sycophancy; verification; source checking; trust calibration; privacy;
- iteration; critique loops; chains; handoffs; workflows; persistent instructions; projects; memory; context documents;
- files; source material; web search; Deep Research; code execution; image generation; model comparison;
- few-shot prompting; prompt injection; failure log; professional use cases; and each major Appendix/Part V reference where readers are likely to look it up.

The final list must be derived from terms actually present in the four approved manuscript sources. Cross-references should be used where one term is subordinate to another, for example `memory — see also context documents` only where the manuscript supports that relationship. Do not add unsupported concepts merely because they are common in AI literature.

### Data and page-mapping model

Create a version-controlled index configuration separate from prose, with fields equivalent to:

```json
{
  "term": "Hallucination",
  "aliases": ["hallucinations"],
  "subentries": ["verification", "see also outdated information"],
  "policy": "substantive-only"
}
```

The renderer should:

1. scan the final manuscript text/PDF for candidate occurrences;
2. map each occurrence to the rendered page;
3. apply the substantive-only policy and any manually approved exclusions;
4. generate alphabetised index entries with deduplicated page numbers and ranges only when a topic genuinely continues across consecutive pages;
5. insert the generated index into the manuscript;
6. rebuild the PDF; and
7. repeat until the index page numbers, Contents map, page count, parity, and cover extent stabilise.

For terms whose page cannot be determined safely from extracted text—especially a term in a table, code block, or short callout—add an explicit source marker or an approved manual locator. Markers must be semantic and hidden from the reader; they must never appear as visible production artefacts or become selectable junk in the PDF.

### Index layout

- Start the Index on a new page, preferably a recto page if this does not create an unjustified blank page.
- Use two columns only if the final type size remains comfortably readable at 6 × 9 inches.
- Use hanging indents, clear alphabetic grouping, consistent en dashes/semicolons, and `break-inside: avoid` for an entry block.
- Keep index pages unheaded or use `INDEX` as a fixed header; do not let a prior chapter title leak into the index.
- Add the Index heading to Contents and exclude index self-references unless they are useful.

## 6. Integrated build sequence

### Phase 0 — Approval and baseline lock

- Obtain approval for this plan and the candidate-term policy.
- Record the current PDF hash, page count, dimensions, Contents map, and restore checkpoint.
- Do not modify manuscript prose during this pass unless a locator requires a purely structural marker.

### Phase 1 — Running-header support spike

- Test Chromium margin boxes and named strings in isolation.
- Decide CSS margin boxes, a Paged.js/polyfill route, PDF overlay, or deferral based on rendered evidence.
- Save the support result and rejected alternatives in the QA notes.

### Phase 2 — Header implementation

- Add semantic heading metadata and page-class suppression rules.
- Implement the approved header mechanism.
- Build a temporary proof PDF and inspect representative pages: front matter, Part openers, chapter openers, dense prose, tables, callouts, workflows, appendices, author page, and colophon.

### Phase 3 — Index taxonomy and engine

- Finalise the term list from the four approved `docs/manuscript_part*.md` sources.
- Implement the index configuration and page locator.
- Generate the index only from approved terms and substantive locators.
- Ensure all generated content remains reproducible from source and configuration; never hand-edit only the PDF.

### Phase 4 — Convergent final build

- Run the existing Contents convergence loop with the Index included.
- Recalculate Contents, index pages, total pages, page parity, cover spine width, and complete-book assembly.
- Rebuild the interior, cover, full-book PDF, and metadata only after the map stabilises.

### Phase 5 — Editorial and KDP validation

- Verify every sampled running header against its page’s actual Part/section.
- Verify every index locator against the final PDF, including entries that moved because of index insertion.
- Confirm no headers appear on suppressed pages and no header collides with text, tables, callouts, or images.
- Run the KDP preflight checks for trim, page parity, gutter, embedded fonts, glyph round-trip, and cover spine extent.
- Inspect the final PDF in KDP Print Previewer and order a physical proof; these external checks remain required even if mechanical checks pass.

## 7. Acceptance criteria

The pass is complete only when all of the following are true:

- The final PDF remains 6 × 9 inches and satisfies the KDP margin tier for its final page count.
- Running headers are present only on intended body/reference pages, with correct left/right content and no clipping, wrapping, or stale carry-over.
- Part and chapter opener pages remain visually clean and intentional.
- The Index is alphabetised, selective, readable, reproducible, and page-accurate against the final PDF.
- Contents includes the Index and still maps every listed heading to its actual starting page.
- Page parity is even; the cover and complete-book PDF use the final interior extent and recalculated spine.
- `pdftotext`/font checks contain no hidden index-marker artefacts, stale author name, duplicate back matter, or unintended header text on suppressed pages.
- `git diff --check` passes and the generated outputs are traceable to source/configuration changes.
- KDP Print Previewer and physical proof review produce no unresolved navigation, gutter, readability, or print-safety defects.

## 8. Risks and rollback

Primary risks are browser support differences, pagination drift caused by new top margin content, index locators becoming stale after index insertion, two-column index readability, and a page-count change that invalidates the cover spine.

Rollback is to the existing restore checkpoint/tag and the current approved 214-page output. No destructive reset should be used; preserve the approved working tree and generated artifacts until the revised PDF has passed QA.

## 9. Explicitly out of scope

This plan does not authorise:

- a general prose rewrite;
- a font-family redesign;
- new website pages, QR codes, downloadable resources, or marketing funnels;
- changes to the author name or back-matter order;
- a Kindle reflowable index implementation;
- an automatic “index every occurrence” output;
- publication submission before KDP Previewer and physical-proof checks.

## 10. Approval gate

Approval should cover:

1. adding both features in this edition;
2. the running-header convention and suppressed-page list;
3. placing the Index between Appendix E and `A Note on Sources`;
4. using a curated, substantive-only index rather than every occurrence; and
5. allowing the support-spike result to choose between CSS margin boxes, a tested paged-media layer, a tested PDF overlay, or deferral if no option meets the acceptance criteria.

Until those decisions are approved, this file is the implementation plan only. No source, CSS, renderer, PDF, cover, or metadata changes have been made.

## Sources

- [W3C — CSS Generated Content for Paged Media Module](https://www.w3.org/TR/css-gcpm-3/)
- [Chrome for Developers — Add content to the margins of web pages when printed](https://developer.chrome.com/blog/print-margins?hl=en)
- [MDN — `@page` at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40page)
- [Paged.js — Generated Content in Margin Boxes](https://pagedjs.org/en/documentation/7-generated-content-in-margin-boxes/)
- [Amazon KDP — Set Trim Size, Bleed, and Margins](https://kdp.amazon.com/en_US/help/topic/GVBQ3CMEQW3W2VL6)
- [Amazon KDP — Paperback Submission Guidelines](https://kdp.amazon.com/en_US/help/topic/G201857950)
- [Amazon KDP — Paperback and Hardcover Manuscript Templates](https://kdp.amazon.com/en_US/help/topic/G201834230)
- Repository references: `docs/editorial_system.md`, `docs/BOOK_IMPLEMENTATION_PLAN.md`, `docs/BOOK_QA_REPORT.md`, and the four approved manuscript sources.
