# The Art of AI — Book 1
## Final Implementation Plan for Editorial and Production Revision

**Status:** Locked and executed for repository-scoped work; publication-dependent items remain pending

**Baseline reviewed:** 214-page interior PDF, repository documentation, manuscript sources, production renderer, metadata, and current output files.

**Publication author decision:** Use **Eleanor Mercer** consistently as the public author name. Replace any conflicting legacy author name wherever it appears in publication-facing material, generated metadata, production code, documentation, cover text, title-page output, and the final PDF. Do not preserve the conflicting name in any public-facing artifact.

## 1. Purpose and scope

This plan responds to the September 2026 editorial and reader review while preserving the book's central architecture: the 7 Questions framework, the AI Interaction Stack, Before → Better → Best teaching examples, 25 workflows, and the verification thread.

The goal is to move the book from the reported 80/100 publication assessment to at least the editorial system's 85/100 threshold without turning the manuscript into a platform-specific feature manual or a substantially different book.

The plan includes:

- resolving the author-identity contradiction;
- correcting current platform and KDP claims against primary documentation;
- deepening the thinest high-value chapters with targeted examples;
- improving navigation and reference value;
- preserving the existing voice, UK spelling, examples, verification emphasis, and cross-platform principles;
- rebuilding and mechanically and visually checking the final production files.

The plan does not authorise execution. Manuscript edits, code changes, asset creation, web-page creation, QR-code destinations, or PDF rebuilds begin only after approval.

## 2. Findings validated against the repository and current sources

### Confirmed and accepted as must-fix

1. **Author conflict is real.** Older generated material and production records contain a conflicting legacy author name; the supplied author page uses `Eleanor Mercer`. The implementation decision is now fixed: use `Eleanor Mercer` throughout.

2. **The 214-page baseline is real.** The current interior is 6 × 9 inches and 214 pages. It is even, but any revision that changes pagination must regenerate the cover spine and complete-book PDF.

3. **The author page needs paragraph treatment.** This has already been corrected in the working source, but it must be preserved in the approved revision and rechecked in the final PDF.

4. **Appendix E remains fast-decaying.** It should retain a dated verification point and official links, but stable principles should remain in the main text. High-volatility claims should be minimised and phrased as capability descriptions rather than permanent product promises.

5. **The current production renderer needs an author-identity correction.** The hard-coded author constant affects the title page, HTML metadata, cover spine/front, and generated metadata. The README, repository note, and any publication-facing records must also be audited.

### Confirmed, but requiring careful qualification

- **ChatGPT Projects:** OpenAI's current help documentation says Projects are available to free and paid subscription types globally, and can group chats, files, instructions, and project memory. File limits and memory behaviour vary by plan and workspace. The manuscript should retain the broad availability claim but avoid presenting memory as complete recall. [OpenAI, “Projects in ChatGPT”](https://help.openai.com/en/articles/10169521-projects-in-chatgpt)

- **Custom Instructions:** OpenAI says Custom Instructions are available on all plans on web, desktop, iOS, and Android. The manuscript must not describe them as Plus-only. [OpenAI, “ChatGPT Custom Instructions”](https://help.openai.com/en/articles/8096356-custom-instructions)

- **GPT creation:** The review's suggestion that anyone can create a GPT is no longer safe. OpenAI's current help pages say personal ChatGPT accounts cannot create or publish new GPTs; managed-workspace permissions and existing GPT access differ. The manuscript should distinguish using GPTs from creating or publishing them. [OpenAI, “Sharing and publishing GPTs”](https://help.openai.com/en/articles/8798878-building-and-publishing-a-gpt), [OpenAI, “Troubleshooting GPTs”](https://help.openai.com/en/articles/11325361)

- **Web search and Deep Research:** The report is directionally correct that current AI products can perform web research, but citations are not proof. OpenAI describes Deep Research as a documented, source-linked research process; Google describes Gemini Deep Research as real-time research that can use Google Search, uploaded files, and selected sources. The book should teach source inspection and claim verification rather than present any tool as infallible. [OpenAI, “Deep research in ChatGPT”](https://help.openai.com/en/articles/10500283-deep-research-daq), [Google, “Use Deep Research in Gemini Apps”](https://support.google.com/gemini/answer/15719111)

- **Claude persistence:** The second review correctly flags the danger of an absolute “Claude has no memory” statement. Anthropic documents profile preferences, project instructions, project knowledge, styles, and rolling past-chat search availability. These are distinct persistence mechanisms, not a guarantee of complete memory. [Anthropic, “Understanding Claude's Personalization Features”](https://support.anthropic.com/en/articles/10185728-understanding-claude-personalization-features), [Anthropic, “What are projects?”](https://support.anthropic.com/en/articles/9517075-what-are-projects)

- **Named models and image products:** GPT-4o has been retired from ChatGPT, and OpenAI's current image documentation refers to ChatGPT Images while noting the retirement of the official DALL·E GPT. Named models should be dated or removed from stable teaching. [OpenAI, “Retiring GPT-4o and other ChatGPT models”](https://help.openai.com/en/articles/20001051-retiring-gpt-4o-and-otherchatgpt-models), [OpenAI, “Images in ChatGPT”](https://help.openai.com/en/articles/11084440-images-in-chatgpt)

- **KDP AI disclosure:** KDP currently requires disclosure of AI-generated text, images, or translations, but does not require disclosure of AI-assisted work such as editing, refinement, error-checking, or brainstorming where the author created the content. The provenance ledger must therefore classify material accurately rather than treating every AI touch as AI-generated. [Amazon KDP, “Content Guidelines”](https://kdp.amazon.com/en_US/help/topic/G200672390)

- **KDP geometry:** KDP lists 6 × 9 inches as a regular trim size and requires a 0.5-inch minimum inside margin for 151–300-page paperbacks without bleed. The current production margins exceed that minimum, but the final PDF must be checked again after pagination changes. [KDP, “Set Trim Size, Bleed, and Margins”](https://kdp.amazon.com/en_US/help/topic/GVBQ3CMEQW3W2VL6), [KDP, “Paperback Submission Guidelines”](https://kdp.amazon.com/en_US/help/topic/G201857950)

### Recommendations accepted as valuable but not automatically required

- Part III chapters 10, 13, 14, and 15 need targeted expansion or stronger worked examples; the goal is depth where it improves reader action, not padding.
- A visual AI Interaction Stack diagram is worthwhile and should be tested in the black-and-white interior.
- Running headers, an index, a Part V navigator, and a redesigned Appendix A have strong reference-book value, but each requires layout testing.
- A digital-resource reference, QR codes, lead magnets, online Appendix E updates, a review request, and a newsletter funnel depend on confirmed website destinations and author approval. They are not to be invented or added as placeholder promises.
- A premium font change is optional and must not be attempted during the factual revision pass unless a visual proof confirms a clear improvement without damaging pagination or embedded-font reliability.

## 3. Author identity resolution — Phase 0 blocker

Before any substantive revision:

1. Replace any legacy renderer author constant with `Eleanor Mercer`.
2. Update the production README and repository-facing publication note where they describe the book's public author.
3. Regenerate title page, cover front/spine, HTML metadata, complete-book PDF, and metadata JSON.
4. Search all tracked publication-facing files and generated outputs for any conflicting legacy author name.
5. Confirm that the supplied biography, author photo, title page, copyright page, cover, spine, metadata, and any KDP-facing records all use `Eleanor Mercer`.
6. Do not change unrelated historical notes or commit metadata unless they are presented as publication-facing information.

**Acceptance test:** no conflicting legacy author name remains in the final publication package; `Eleanor Mercer` appears consistently in the title page, cover, metadata, and author page.

## 4. Editorial implementation phases

### Phase 1 — Baseline, evidence, and claim inventory

- Hash and archive the current manuscript sources and 214-page PDF before edits.
- Create a feature-claim inventory covering Projects, Custom Instructions, GPTs, search, Deep Research, memory, files, code execution, image generation, privacy, and model names.
- Record claim location, exact wording, volatility, official source, disposition, and verification date.
- Create an internal provenance/testing ledger for the statement “All examples were tested”. Each entry should record workflow or example, exact prompt, input, platform, plan/account tier if relevant, model/tool identifier, date, expected result, observed result, verification result, and whether the example is safe to describe as tested.
- Do not insert hypothetical cross-model results into the manuscript.

### Phase 2 — Must-fix factual and identity revision

- Complete the Eleanor Mercer identity correction.
- Audit and correct all platform claims using the official sources above.
- Replace absolute memory language with distinctions between conversation context, project knowledge, saved preferences, search across past chats, and manually supplied context.
- Separate “using a GPT” from “creating or publishing a GPT”.
- Remove obsolete GPT-4o/DALL·E claims or make them dated historical notes where genuinely useful.
- Keep product-specific claims in Appendix E where possible and retain the stable principle first in main chapters.
- Preserve the existing verification language: citations are evidence to inspect, not proof.

### Phase 3 — Targeted reader and pedagogy revision

Implement only changes that improve the reader's ability to act:

1. **Chapter 10:** add one worked persistent-instructions setup, including the initial version, rationale, and resulting improvement.
2. **Chapter 13:** expand current web research/Deep Research with one concrete, source-linked example and a compact verification checklist.
3. **Chapter 14:** add a worked context-document example using a realistic professional or educator.
4. **Chapter 15:** walk through one complete workspace audit and show the resulting structure.
5. **Part II:** break the repeated B→B→B rhythm once, preferably with an annotated prompt or diagnostic exercise in Chapter 8 or 9. Preserve the framework; vary the teaching device.
6. **Chapter 19:** lead with the seven-stage client-brief example, then name and explain chains, loops, and handoffs from what the reader has just seen.
7. **Part V:** replace or adapt one workflow example to signal a non-professional-services audience, such as a teacher, healthcare worker, creative professional, or small retailer. Preserve safety boundaries for regulated use.
8. **Closing:** review the “art is deliberate” paragraph and shorten or remove it if the imperative reader-focused close is stronger without it.
9. Add brief persona callbacks only where they improve continuity; avoid forced narrative repetition.

### Phase 4 — Navigation, reference value, and layout

- Add a simple, black-and-white AI Interaction Stack diagram near the beginning of Chapter 2.
- Add a Part V visual navigator organised by task complexity/time-to-value only if the categories accurately match the actual workflows.
- Redesign Appendix A as a genuinely single-page reference card; retain the full explanation elsewhere if needed.
- Generate an index after all text and pagination are stable. Index terms should include concepts actually present, such as hallucination, context drift, few-shot prompting, sycophancy, code execution, verification, projects, and workflows.
- Evaluate running headers using the existing HTML/CSS renderer. If browser margin boxes are unreliable, do not ship an unstable implementation; use a tested alternative.
- Improve callout differentiation with restrained black-and-white border treatment only after a visual print proof. Do not introduce decorative colour dependence.
- Keep the existing 6 × 9 trim unless a separate commercial decision approves a 7 × 10 edition.

### Phase 5 — Digital resource and commercial decisions

These are gated decisions, not automatic edits:

- Confirm what `theartofai.com` will actually provide before adding a URL promise.
- If approved and live, add one durable reference such as `/book1`, a printable 7 Questions card, downloadable worksheets, or a dated Appendix E update page.
- Add QR codes only after each destination is live, stable, tested on a phone, and appropriate for a printed book.
- Decide separately whether to include a non-incentivised review request.
- Prepare metadata separately from the interior revision. KDP currently allows up to three categories and up to seven keywords; selections must accurately describe the book. [KDP Metadata Guidelines](https://kdp.amazon.com/en_US/help/topic/G201097560), [KDP Keywords](https://kdp.amazon.com/en_US/help/topic/G201743260), [KDP Categories](https://kdp.amazon.com/en_US/help/topic/G200652170)

## 5. Production and quality gates

After approved manuscript changes:

1. Synchronise `docs/` and `book-production/source/` from the approved source of truth.
2. Build the interior PDF.
3. Recalculate Contents from actual rendered heading pages. Every part, chapter, appendix, and workflow entry must point to the page where its heading begins; specifically verify the Part II divider rather than relying on the first textual mention.
4. Confirm the author name in title page, copyright/front matter, cover, spine, HTML metadata, metadata JSON, and PDF text.
5. Confirm author biography paragraphing, image rendering, hidden production comment behaviour, and final back-matter order.
6. Check 6 × 9 trim, page parity, inside gutter, outside margins, embedded fonts, text round-trip, image resolution, table/callout rendering, widows/orphans, and blank pages.
7. Rebuild the full-wrap cover and complete-book PDF using the final interior page count and spine width.
8. Run the repository's mechanical preflight checks and retain the report.
9. Review the PDF in KDP Print Previewer page by page, then order and read a physical proof copy.

## 6. Acceptance criteria for release recommendation

The revision is complete only when:

- `Eleanor Mercer` is the only public author name in the publication package.
- No stale or unsupported platform claim remains without an official source, date, or appropriate qualification.
- Projects, Custom Instructions, GPT creation, Claude persistence, Deep Research, image generation, and model references match current documentation or are clearly dated.
- The author identity and author biography are internally consistent.
- The 7 Questions, Interaction Stack, workflows, and verification architecture remain intact.
- The selected Part III improvements materially improve actionability without filler.
- The Contents page matches actual PDF heading pages.
- Appendix A is either a usable single-page card or the redesign decision is explicitly declined.
- Any index, running headers, diagram, navigator, QR code, website offer, review request, or online-reference promise is deliberate, live/tested where applicable, and approved.
- “All examples were tested” is supported by the internal evidence ledger or is revised to match the evidence.
- KDP AI disclosure classification is based on actual provenance: AI-generated material is disclosed in the KDP dashboard; AI-assisted work is not incorrectly classified as AI-generated.
- The final PDF passes mechanical checks, KDP Print Previewer review, and physical proof review.

## 7. Deliverables after approval

- Revised manuscript sources in `docs/` and `book-production/source/`.
- Updated production renderer and documentation with `Eleanor Mercer`.
- Claim/source inventory.
- AI provenance and example-testing ledger.
- Revised interior PDF.
- Regenerated full-wrap cover PDF and complete-book PDF.
- Regenerated metadata JSON.
- Contents/page-map audit.
- KDP mechanical preflight report.
- Final visual QA and proof-copy checklist.

## 8. Approval gate

Approval should explicitly cover:

1. The publication author name: **Eleanor Mercer** — already selected by instruction.
2. Whether targeted Part III expansions are included.
3. Whether the visual Stack diagram, Part V navigator, single-page Appendix A, running headers, callout refinements, and index are included in this edition.
4. Whether the website resource, QR codes, review request, and online Appendix E update are included.
5. Whether the closing paragraph is trimmed.

The repository-scoped implementation described above has been executed. The approved index and running-header navigation pass has now also been executed. Website resources, QR destinations, online Appendix E updates, and any font redesign remain approval-gated.

## Sources consulted

- [Amazon KDP Content Guidelines](https://kdp.amazon.com/en_US/help/topic/G200672390)
- [Amazon KDP Trim Size, Bleed, and Margins](https://kdp.amazon.com/en_US/help/topic/GVBQ3CMEQW3W2VL6)
- [Amazon KDP Paperback Submission Guidelines](https://kdp.amazon.com/en_US/help/topic/G201857950)
- [Amazon KDP Metadata Guidelines](https://kdp.amazon.com/en_US/help/topic/G201097560)
- [Amazon KDP Keywords](https://kdp.amazon.com/en_US/help/topic/G201743260)
- [Amazon KDP Categories](https://kdp.amazon.com/en_US/help/topic/G200652170)
- [OpenAI Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt)
- [OpenAI Custom Instructions](https://help.openai.com/en/articles/8096356-custom-instructions)
- [OpenAI GPT sharing and publishing](https://help.openai.com/en/articles/8798878-building-and-publishing-a-gpt)
- [OpenAI GPT troubleshooting and creation limits](https://help.openai.com/en/articles/11325361)
- [OpenAI Deep Research](https://help.openai.com/en/articles/10500283-deep-research-daq)
- [OpenAI GPT-4o retirement](https://help.openai.com/en/articles/20001051-retiring-gpt-4o-and-otherchatgpt-models)
- [OpenAI Images in ChatGPT](https://help.openai.com/en/articles/11084440-images-in-chatgpt)
- [Anthropic Claude personalisation features](https://support.anthropic.com/en/articles/10185728-understanding-claude-personalization-features)
- [Anthropic Claude Projects](https://support.anthropic.com/en/articles/9517075-what-are-projects)
- [Google Gemini Deep Research](https://support.google.com/gemini/answer/15719111)
