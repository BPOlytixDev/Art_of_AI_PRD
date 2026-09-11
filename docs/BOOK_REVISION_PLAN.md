# The Art of AI — Revision and Validation Plan

Status: Executed 2026-09-10; author-dependent items remain pending
Prepared: 2026-09-10
Scope: Editorial, technical-accuracy, source-validation, and production revision plan
Execution note: The plan was approved by the author. Implemented changes are recorded below; no author-dependent facts were invented.

## Execution record

Completed:

- Corrected the Contents resolver so part headings require both the exact part label and its part title on the same divider page.
- Corrected the confirmed Part II Contents entry from page 10 to the actual divider page after rebuild.
- Reframed absolute memory claims around fresh-chat context, project context, saved memory, searchable history, and connected sources.
- Corrected ChatGPT Projects and Custom Instructions plan language.
- Reworked Claude persistence language to cover profile preferences, project instructions, project knowledge, and past-chat search where enabled.
- Replaced volatile product-specific web-search, code-execution, and image-generation claims with capability-based wording.
- Added a platform-neutral Deep Research/web-research workflow with source inspection and verification steps.
- Added official documentation starting points to Appendix E.
- Replaced the unsupported universal “all examples were tested” statement with a defensible review statement.
- Added a short, non-incentivised review request to the back matter.
- Added the supplied About the Author page, biography, and headshot after the colophon.
- Added renderer and stylesheet support for the supplied square author photograph.
- Rebuilt the interior, cover, complete-book PDF, and metadata.
- Performed mechanical PDF checks for page count, parity, trim, Contents output, text presence, source synchronization, and embedded fonts.

Still pending:

- Confirmation of the website's live reader offer before adding a printable card, update page, or newsletter call-to-action.
- Internal evidence/provenance ledger for actual AI-generated versus AI-assisted content and workflow testing.
- Final KDP dashboard AI-content classification and disclosure at upload/republication.
- Optional decision on a hybrid/online Appendix E, running headers, further em-dash variation, and pricing/metadata strategy.
- KDP Print Previewer review and physical proof copy.

## 1. What the review report gets right

The report correctly identifies the highest-risk area: platform-specific claims can become false quickly, and the current manuscript contains several claims that are already contradicted by current first-party documentation.

The following are valid revision priorities:

1. Verify every platform feature, plan, limit, model name, capability, and availability statement against current official documentation.
2. Keep the book principle-led and cross-platform; move volatile feature detail into carefully dated product notes.
3. Add a practical, clearly labelled demonstration of current web research / Deep Research workflows, with source checking.
4. Define jargon on first use and preserve the book's non-technical reader promise.
5. Strengthen step-by-step workflow teaching and chapter-to-chapter transitions.
6. Run a full editorial and technical quality pass before rebuilding the interior.
7. Re-run PDF production and KDP mechanical checks after content changes.

## 2. What the report gets wrong or overstates

### 2.1 It appears not to have reviewed the full manuscript

The report describes several items as missing or hypothetical that are already present:

- The 7 Questions framework is developed in Part I and repeated in Appendix A.
- Before/after examples, prompt blocks, callouts, exercises, failure modes, verification guidance, and reusable workflows already appear throughout the manuscript.
- Part V already contains 25 named workflows.
- Part VI contains a substantial verification framework and checklist.
- Appendix E already contains platform notes and volatility warnings.
- The front matter already contains an AI disclosure statement and says KDP disclosure was completed in the publishing dashboard.

The revision should therefore be a targeted correction and strengthening pass, not a wholesale rewrite from the report's hypothetical sample.

### 2.2 The report's KDP recommendation needs correction

Current KDP policy distinguishes between:

- AI-generated content: content actually created by an AI tool; KDP disclosure is required.
- AI-assisted content: author-created content edited, refined, error-checked, or brainstormed with AI; disclosure is not required.

A public AI-use log is not required by the cited KDP policy. We should maintain an internal provenance/QC record, but should not add an appendix or public log unless the author specifically wants one for transparency.

The existing disclosure language must be reconciled with the actual production history. Before revision, the author must confirm which manuscript passages, images, translations, or cover assets were AI-generated versus author-created and AI-assisted. The KDP dashboard disclosure should be rechecked at submission or republication.

### 2.3 Some report feature recommendations are false or too broad

The report says anyone can create a custom GPT without coding. Current OpenAI Help says GPTs are available for all users to use, but new GPT creation and publishing are not available on personal Free, Go, Plus, or Pro accounts. The manuscript must not make an unconditional "anyone can create" claim.

The report says ChatGPT Projects are available only on paid plans. Current OpenAI Help says Projects are available globally on free and paid plans, with different file limits by plan.

The report says Custom Instructions are Plus-only. Current OpenAI Help says Custom Instructions are available on all plans.

The report treats current model names as stable. They are not. GPT-4o has been retired from ChatGPT, and Gemini 3.1 Pro is currently a preview model. Model names should appear only in dated examples or in a volatility-controlled appendix.

The report's proposed wording about "Browse" should be replaced with the current product-neutral wording used by each platform: web search, Deep Research, or the current tool name shown in the official documentation.

## 3. Verified technical findings requiring revision

### Must fix

#### A. ChatGPT Projects

Current manuscript locations:

- Part III, Chapter 11 product note.
- Appendix E, E1 Projects feature.

Current issue:

- The manuscript says Projects are available on ChatGPT all paid plans.
- Current OpenAI documentation says Projects are available to free and paid subscription types globally.
- Current file limits are plan-dependent: Free 5, Go/Plus 25, Edu/Pro/Business/Enterprise 40, with separate sharing and workspace conditions.
- Project memory can be default or project-only and depends on account/workspace settings.

Planned correction:

- Replace the paid-only statement with a dated, plan-neutral description.
- Avoid presenting file limits as permanent; include them only if useful and attach a verification date.
- Explain Projects as workspaces containing chats, files, and project instructions.
- Distinguish project context from global saved memory and from ordinary chat history.
- Keep the stable advice: do not assume the system will use every file or remember every detail; verify what context was actually used.

Source to use:
OpenAI Help — Projects in ChatGPT:
https://help.openai.com/en/articles/10169521-projects-in-chatgpt

#### B. Custom Instructions

Current manuscript location:

- Appendix E, E1.

Current issue:

- The manuscript says Custom Instructions are available on Plus and above.
- Current OpenAI documentation says they are available on all plans, web, desktop, iOS, and Android.

Planned correction:

- State that availability is broad but character limits and interface details vary by plan and platform.
- Keep the conceptual distinction between global Custom Instructions and project-specific instructions.

Source to use:
https://help.openai.com/en/articles/8096356-chat-preferences-for-chatgpt

#### C. GPT creation and use

Current manuscript locations:

- Chapter 13 / tool discussion.
- Appendix E, E1, if GPTs are added or expanded in the next pass.

Current issue:

- The review report's unconditional claim that anyone can create a GPT is not currently safe.
- Current OpenAI Help says users can use GPTs when signed in, but creation and publishing are not available on personal Free, Go, Plus, or Pro accounts; eligibility depends on workspace/subscription permissions.

Planned correction:

- Separate “use an existing GPT” from “build/edit/publish a GPT.”
- Avoid promising no-code creation to every reader.
- Explain that access and publishing permissions vary by account and workspace.
- Use “GPTs” and “Apps/Actions” according to current OpenAI terminology, without describing them as a simple replacement for all historical plugins.

Source to use:
https://help.openai.com/en/articles/8554407-what-are-gpts

#### D. Web search and Deep Research

Current manuscript locations:

- Chapter 13.
- Chapter 19 / workflow discussion.
- Part V research workflows.
- Appendix E.

Current issue:

- The manuscript discusses web search generally but does not give a sufficiently explicit, current Deep Research demonstration.
- Current OpenAI and Google documentation describes agentic/multi-step research tools with citations, source selection, file support, and important limitations.
- Citations do not make an answer automatically correct.

Planned correction:

- Add one compact, platform-neutral teaching example showing:
  1. define a current research question;
  2. choose the research/search tool;
  3. specify preferred primary sources;
  4. ask for a source-linked report;
  5. inspect citations;
  6. verify key claims independently.
- Add platform examples only in dated product notes.
- Do not imply that every plan, region, model, or tool has identical access.
- Preserve the existing verification principle.

Sources to use:
OpenAI Deep Research:
https://openai.com/index/introducing-deep-research/
Google Gemini Deep Research Help:
https://support.google.com/gemini/answer/15719111
Anthropic Research Help:
https://support.anthropic.com/en/articles/11088861-using-research-on-claude-ai

#### E. Memory language

Current manuscript locations:

- Part I claim that AI has no persistent memory between conversations.
- Chapter 10.
- Chapter 14.
- Appendix E, E2.

Current issue:

- The stable conceptual point is valid for a fresh chat without enabled persistence: the model should not be treated as a human colleague with guaranteed memory.
- The absolute wording is too broad for current products.
- OpenAI Projects and memory settings, Claude projects/personalization/past-chat search, and Gemini personalization/context features differ by plan, region, and rollout.

Planned correction:

- Change absolute claims to: “A fresh chat should be treated as having no dependable knowledge of your previous work unless the platform explicitly provides and uses a memory, project, history, or connected-source feature.”
- Distinguish:
  - in-conversation context;
  - project knowledge;
  - saved memory/profile preferences;
  - searched past chats;
  - uploaded source material;
  - external connected apps.
- Explain that persistence is not perfect recall and must be checked.

Sources to use:
OpenAI Projects:
https://help.openai.com/en/articles/10169521-projects-in-chatgpt
Anthropic personalization:
https://support.anthropic.com/en/articles/10185728-understanding-claude-personalization-features
Anthropic Projects:
https://support.anthropic.com/en/articles/9519177-how-can-i-create-and-manage-projects

#### F. Claude and Gemini product notes

Current issue:

- The report's specific claims need source-by-source verification rather than wholesale adoption.
- Claude Fable 5 is a real 2026 Anthropic model, but model and plan references are volatile.
- Gemini 3.1 Pro and 1M-token context claims are documented for current API/model documentation, but this does not automatically describe every Gemini consumer plan or interface.
- The manuscript should not transfer API limits directly into consumer-product instructions.

Planned correction:

- Rework Appendix E so every volatile claim has:
  - product name;
  - exact feature;
  - consumer vs API scope;
  - plan/region caveat;
  - “verified [month year]” date;
  - official documentation link in the production source or research ledger.
- Prefer capability descriptions over model-name comparisons.
- Remove claims that cannot be supported by an official source.

Sources to use:
Anthropic Projects:
https://support.anthropic.com/en/articles/9517075-what-are-projects
Anthropic latest model announcement:
https://www.anthropic.com/news/claude-opus-4-7
Google Gemini models:
https://ai.google.dev/gemini-api/docs/models
Google Gemini 3.1 Pro:
https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview
Google Gemini file uploads:
https://support.google.com/gemini/answer/14903178

#### G. GPT-4o, DALL·E, and other named models/products

Current issue:

- The report recommends GPT-4o as a current flagship, but current OpenAI documentation says GPT-4o was retired from ChatGPT in February 2026.
- The manuscript's Appendix E refers to DALL·E as the integrated image system, while current OpenAI Help refers to ChatGPT Images and notes the retirement of the official DALL·E GPT.

Planned correction:

- Remove “latest” and “newest” language from the manuscript.
- Replace named-model examples with task-based, platform-neutral language wherever possible.
- If a named model is retained, date it and explain that availability may have changed.
- Update image-generation terminology and include a commercial-use/rights caveat.

Sources to use:
https://help.openai.com/en/articles/20001051-retiring-gpt-4o-and-otherchatgpt-models
https://help.openai.com/en/articles/11084440-images-in-chatgpt
https://help.openai.com/en/articles/6783457-chatgpt-privacy-and-data-security

### Should fix

#### H. Jargon and reading level

Audit first use of:

- LLM / large language model;
- token;
- context window;
- model snapshot;
- RAG;
- MCP;
- agent;
- tool;
- system/user instruction;
- grounding;
- multimodal.

For each term, either define it in ordinary language before the technical term or move it to a short glossary. Do not add technical detail merely because it is available.

#### I. Pedagogy and transitions

Add or tighten short chapter bridges where they improve the learning arc:

- Chapter 1 → Chapter 2: from generic output to the interaction layers.
- Chapter 2 → Chapter 3: from the diagnostic stack to the portable checklist.
- Chapter 9 → Part III: from controlling output to preserving context.
- Chapter 15 → Part IV: from workspace design to multi-step work.
- Chapter 19 → Part V: from workflow patterns to applied workflows.
- Part V → Part VI: from useful output to responsible verification.

Do not add repetitive “in this chapter” summaries where the existing chapter already performs that function.

#### J. Workflow demonstrations

Select a small number of high-value workflows for deeper treatment rather than adding two or three examples to every chapter.

Candidate demonstrations:

1. Source-grounded document summary and extraction.
2. Current web research with citations.
3. Draft → critique → revision loop.
4. Multi-step proposal or briefing workflow.
5. Spreadsheet/data analysis with explicit verification.

Each selected demonstration should include objective, inputs, exact prompt sequence, expected output shape, failure mode, and verification step.

The report's hypothetical model-comparison table must not be inserted as fact. Multi-model results should be included only if actual transcripts, dates, model identifiers, prompts, and evaluation criteria exist.

## 2A. Second-review findings validated against the PDF

The second review was checked against the current 210-page interior rather than accepted at face value.

### Confirmed publication blockers

1. **Table of Contents defect.** The current PDF's Contents page lists `PART II — BUILD BETTER INTERACTIONS` as page 10. The actual Part II divider is page 36. This is a real production/pagination defect, not a text-extraction artefact. The contents-generation logic is finding the first page containing the Part II label rather than the actual part-divider page and must be corrected and audited for every part, chapter, appendix, and workflow entry.

2. **Claude memory statement.** Appendix E2 currently states that Claude does not have a persistent cross-conversation memory feature equivalent to ChatGPT's Memory. That absolute statement is no longer safe. Current Anthropic documentation describes profile preferences, project instructions, project knowledge, and rolling availability of past-chat search. The manuscript should describe the actual persistence mechanisms and their limits rather than make a binary “has/no memory” comparison.

### Confirmed additions worth including

3. **About the Author page.** The current back matter has “About This Book” but no author biography. Add an author page only after the author supplies the factual biography, professional background, and intended positioning. No biography should be invented from the name alone.

4. **Review request.** Add a brief, non-incentivised review request near the end of the book if the author approves. It must not offer compensation, make a misleading claim, or imply that a positive review is required.

5. **Website purpose.** The manuscript names `theartofai.com` but does not state what the reader receives there. Add a clear, durable reader benefit only after the website destination and lead magnet/update mechanism are confirmed. The proposed 7 Questions printable card and live Appendix E update page are suitable options, not automatic requirements.

### Recommendations to keep optional

- Moving Appendix E online can reduce decay, but a printed dated reference should still explain what is online and how the reader benefits. This is a content/website decision, not a silent manuscript change.
- Varying some em-dashes is a worthwhile copy-edit pass, but not a release blocker.
- Running headers may improve print navigation, but require a design decision and visual proofing; do not add them solely because the review suggested them.
- The reported words-per-page average is not a defect. The existing short paragraphs and white space are part of the book's readability system. Pricing recommendations are outside this revision plan and require a separate market/metadata decision.

### Claim requiring author evidence

The front matter says “All examples were tested.” Before publication, create an internal evidence ledger mapping that statement to the tested prompts, platform, date, account tier, model/tool, expected result, and observed result. If the evidence does not support the universal wording, revise the statement to accurately describe the testing performed. Do not add speculative cross-model test results.

#### K. Verification language

Preserve the strong Part VI material. Add only where needed:

- source citations are evidence to inspect, not proof;
- tool-assisted research can still misread sources;
- current information must be checked against authoritative sources;
- professional, medical, legal, and financial use needs qualified human judgment.

Avoid promising that self-critique or iterative prompting guarantees accuracy.

#### L. Cross-platform feature framing

Use a consistent pattern:

- stable principle first;
- example on one platform;
- current availability caveat;
- verification instruction;
- official documentation source.

This keeps the book useful after interfaces change.

## 4. KDP and publication compliance plan

1. Confirm the provenance of manuscript text, cover art, and interior artwork.
2. Classify each as author-created/AI-assisted or AI-generated under current KDP definitions.
3. If any actual content was AI-generated, ensure the KDP dashboard disclosure is made at publication/republication.
4. Keep an internal AI-use/provenance log for audit and editorial control; do not add it to the public book unless approved.
5. Verify all quotations, examples, tables, diagrams, and third-party images for rights and attribution.
6. Recheck metadata, categories, keywords, and description against current KDP rules at upload time. Do not hard-code report claims about limits without verifying the current KDP help pages.
7. Run a full KDP interior preflight after the final rebuild:
   - 6 × 9 trim;
   - even page count;
   - gutter minimum;
   - text round-trip;
   - fonts;
   - contents pagination;
   - cover spine against actual interior extent.
8. Review the final PDF in KDP Print Previewer and order a proof copy.

Current KDP AI policy:
https://kdp.amazon.com/en_US/help/topic/G200672390

## 5. Proposed execution phases — after approval only

### Phase 0 — Baseline and evidence ledger

- Freeze a copy/hash of the current manuscript and PDFs.
- Create a feature-claim inventory with file, line, claim, volatility, official source, and disposition.
- Create a provenance ledger for AI-assisted/AI-generated material.
- Record the current 210-page interior baseline.
- Capture the current Contents page and actual divider-page map, including the confirmed Part II 10-versus-36 defect.

Deliverables:
- claim inventory;
- source ledger;
- provenance/QC ledger;
- baseline build record.

### Phase 1 — Must-fix factual revisions

- Correct Projects, Custom Instructions, GPT creation, memory, web search, Deep Research, Claude, Gemini, model, and image-generation claims.
- Replace absolute or plan-confused language.
- Add dated source notes where volatile detail remains.
- Keep platform-neutral principles in the main chapters.
- Correct the Claude memory claim and audit all related persistence language.

Deliverable:
- factually corrected manuscript with tracked claim dispositions.

### Phase 2 — Reader clarity and pedagogy

- Define jargon on first use.
- Tighten selected transitions.
- Improve only the highest-value examples and workflow demonstrations.
- Add one current web-research/Deep Research demonstration.
- Review medical/legal/financial examples for appropriate warnings.
- Remove repetition and unsupported “tested/proven” implications.
- Add an author biography only from author-supplied facts.
- Add a short review request only if approved.
- Clarify the website's reader benefit only if the destination and offer are ready.

Deliverable:
- editorially revised manuscript with a chapter-level QC checklist.

### Phase 3 — Appendix and source-system revision

- Rebuild Appendix E as a dated, source-linked, capability-based reference.
- Decide whether to add a glossary; add it only if the jargon audit shows a real need.
- Keep the public AI disclosure concise and accurate.
- Keep the detailed AI-use log internal unless separately approved.
- Decide whether Appendix E remains fully printed, becomes a concise dated reference with an online update page, or uses a hybrid approach.

Deliverable:
- final reference appendix and editorial/source record.

### Phase 4 — Technical and production QA

- Update the Markdown production source from the approved manuscript.
- Build the interior PDF.
- Validate contents, page parity, trim, fonts, text round-trip, and source hash.
- Verify every Contents entry against the actual first page of its corresponding divider/heading; specifically require Part II to resolve to its actual divider page, not page 10.
- Rebuild cover and complete-book PDF if page count changes.
- Run KDP preflight and inspect the final PDF visually.

Deliverables:
- final interior PDF;
- regenerated cover and complete-book PDF;
- metadata;
- preflight report;
- release checklist.

## 6. Acceptance criteria

The revision is complete only when:

- Every volatile product claim has an official source or has been removed.
- The Contents page maps every part, chapter, appendix, and workflow to the actual PDF page where its heading begins; the confirmed Part II defect is fixed.
- Appendix E does not contain an unsupported absolute claim about Claude memory or any other platform's persistence.
- No statement says ChatGPT Projects or Custom Instructions are paid-only.
- No statement promises GPT creation to every personal-account user.
- Memory claims distinguish fresh-chat context from product persistence.
- Deep Research/web-search teaching includes citations and verification, without implying infallibility.
- Current model names are dated or removed from stable teaching.
- Jargon is defined or moved to a glossary.
- The manuscript retains its central 7 Questions / Interaction Stack / workflow architecture.
- Existing useful examples are preserved unless factually or editorially defective.
- AI disclosure treatment matches KDP's AI-generated vs AI-assisted distinction.
- The final PDF passes mechanical preflight and visual review.
- The “all examples were tested” statement is supported by an internal testing ledger or is revised to match the evidence.
- Any author bio, review request, website offer, running headers, and online-reference strategy are deliberate approved additions, not unrequested scope.

## 7. Final status

The approved execution has been completed for all work that could be performed from the repository and supplied evidence. Remaining author-dependent and publication-dependent items are listed in the execution record above and in `docs/BOOK_QA_REPORT.md`.
