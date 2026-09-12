# The Art of AI — Revision QA Report

## 2026-09-12 execution update

- Publication author identity corrected to **Eleanor Mercer** across the renderer, README, repository note, generated title page, cover, metadata, and PDF.
- Added the AI Interaction Stack diagram and Part V workflow navigator.
- Added targeted worked examples to Part III, including persistent instructions, current web research verification, a context document, and a workspace audit.
- Reordered Chapter 19 so the concrete workflow is introduced before the mechanics it demonstrates.
- Added a broader non-office use case to W16 and tightened the closing paragraph.
- Condensed Appendix A into a single-page quick reference card.
- Added restrained black-and-white callout differentiation.
- Updated GPT documentation wording and link in Appendix E.
- Added a generated, substantive-only Index after Appendix E and before A Note on Sources.
- Added deterministic left/right running headers as a post-pagination PDF overlay so the foundational HTML/CSS flow is not reflowed by unsupported browser named strings; the final overlay uses an embedded DejaVu Sans font.
- Corrected the renderer to read all four authoritative manuscripts from `book-production/source/`.
- Restored the supplied About the Author and About This Book pages to the final interior, including the approved author photo.
- Removed the Contents section's unconditional trailing page break, eliminating an empty page before the Introduction.
- Rebuilt interior, cover, complete-book PDF, `Complete_Interior.pdf`, and metadata.
- Final interior is 208 pages at 6 × 9 inches; the Index begins on page 202, A Note on Sources on page 205, About the Author on page 206, and About This Book on page 207. Page 208 is the required final parity page.
- The obsolete `book-production/source/manuscript_part4_partVI_appendices_1789037161102.md` source remains deleted; the build reads Part VI and Appendices from `book-production/source/manuscript_part4.md`.

## Remaining before publication

- Complete the AI provenance and example-testing ledger in `docs/AI_PROVENANCE_AND_TESTING_LEDGER.md`.
- Review the PDF in KDP Print Previewer and order/read a physical proof copy.
- Confirm the live website resource before adding any QR code, lead magnet, review request, or online Appendix E promise.
- The Index and running-header pass is complete; KDP Print Previewer and physical-proof checks remain outstanding.

Date: 2026-09-12
Artifacts: `book-production/output/Complete_Interior.pdf`, `book-production/output/the-art-of-ai-book-1-interior.pdf`

## Completed checks

- Interior page count: 208.
- Page parity: passed; 208 is even.
- Page size: passed; 432 × 648 points (6 × 9 inches).
- Contents/navigation: passed mechanically; the generated Contents includes the Index, all four parts of the manuscript, all 25 workflows, all appendices, and the restored end matter with final rendered page references.
- Source provenance: passed; the build metadata names all four authoritative `book-production/source/manuscript_part*.md` files, with no reference to the deleted replacement source.
- Stale-claim scan: passed for the corrected claims; the old Claude-memory, paid-only Projects/Custom Instructions, and obsolete GPT/DALL·E wording no longer occur in the production sources.
- Updated content presence: passed for the Stack diagram, Deep Research verification checklist, Part III examples, workflow navigator, Chapter 19 reordering, and condensed Appendix A.
- Back matter: passed; the final interior contains A Note on Sources, About the Author, About This Book, and the final parity page in the approved order.
- Index: passed mechanically; curated entries are alphabetised, generated from rendered page text, and placed before A Note on Sources.
- Index continuation pages are excluded from their own page-reference search, so the final Index does not self-reference pages 202-204.
- Running headers: passed mechanically; sampled body pages contain the current Part on verso pages and current section on recto pages, with opener/back-matter suppression.
- Embedded fonts: passed mechanically; the body fonts and the running-header DejaVu Sans font are embedded in the interior and complete-book PDFs.
- Visual QA: passed on representative part openers, chapter pages, diagrams, Appendix A-C pages, Index pages, A Note on Sources, and the closing colophon.
- Typography QA: passed; the rendered interior contains no em dash characters and no malformed character-spaced running-header pattern.
- Cover regeneration: passed; the cover and complete-book PDF were rebuilt for the 208-page interior. The generated spine width is 0.4684 inches.
- Metadata regeneration: passed; metadata records the 208-page extent, complete-interior artifact, and updated source hashes.
- `git diff --check`: passed.

## Still required before publication

- Review the revised PDF in KDP Print Previewer, page by page, especially gutter, Contents, callouts, page breaks, and any widows/orphans.
- Order and read a physical proof copy.
- Complete the internal AI provenance/testing ledger and confirm KDP's AI-generated versus AI-assisted classification in the publishing dashboard.
- Confirm the live website offer before adding a printable download, update page, or newsletter call-to-action.
- Review the changed 208-page extent against the prior proof in KDP Print Previewer; confirm that the current Chromium print output preserves the intended physical reading scale before publication.

This report does not declare the book ready to print; the remaining checks require the KDP previewer, author input, or a physical proof.
