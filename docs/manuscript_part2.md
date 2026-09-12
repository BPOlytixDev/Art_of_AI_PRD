# PART III

## Build an AI Environment

*Most people use AI as if it were a calculator: pick it up, use it once, put it down. Every new calculation starts from zero. Part III shows you how to change that, building a persistent environment where AI carries your context forward, knows your situation, and becomes genuinely more useful the more you invest in setting it up.*

---

## Chapter 10

### Stop Starting From Zero Every Time

**The repetition problem**

If you use AI more than occasionally, you have encountered this situation: you are about to start a new conversation and you find yourself typing, again, the things AI should already know.

*"I work in marketing at a mid-size UK financial services company. I write for a non-specialist audience. I prefer a formal-but-accessible tone. UK spelling throughout. Never use exclamation marks..."*

This is not how a useful working relationship operates. A good colleague doesn't need to be reminded of your name and job every time you speak to them.

The reason this happens is that a fresh AI conversation should not be assumed to have dependable knowledge of previous conversations. Some platforms now offer memory, projects, searchable history, or connected sources, but availability and behaviour vary. Without one of those features being explicitly enabled and used, the context you built in Tuesday's session is not reliably available on Wednesday.

This is one of AI's most significant practical limitations, and one that is largely solvable.

---

**Three strategies for not starting from zero**

**Strategy 1, System instructions (persistent instructions)**
Most AI platforms now offer a way to set persistent instructions that apply to every conversation. Sometimes called "custom instructions," "system prompts," or "memory settings," these are a set of facts and preferences you provide once and that AI carries forward automatically.

This is the most powerful strategy for regular users. Chapter 11 covers it in depth.

**Strategy 2, Projects**
ChatGPT, Claude, and several other platforms offer a "Projects" feature that groups conversations, persists context, and maintains uploaded documents within a dedicated workspace. For recurring work, client accounts, ongoing projects, regular document types, projects eliminate most setup repetition.

**Strategy 3, Context documents**
When platform features are unavailable or insufficient, a context document you paste in at the start of relevant conversations serves the same purpose. A single well-crafted paragraph covering who you are, what you're doing, and what your preferences are can be copied and pasted in seconds.

**A worked first setup**

David runs a small consultancy and keeps starting client proposals from a blank chat. His first persistent-instructions draft is short:

```
I run a six-person UK consultancy. I use AI mainly for proposals,
client communications, meeting preparation, and research briefings.
Write in plain, professional UK English. Assume the reader is busy
and commercially aware. Do not invent client facts, figures, case
studies, or commitments. Flag anything that needs checking.
```

This does not try to describe every preference David has. It captures the context he repeats most often and the errors that would make an output unusable. After a week, he notices that AI still makes proposals too long, so he adds a default: lead with the decision the reader needs to make and keep first drafts under 800 words unless he asks for more. The instructions improve through use rather than through an attempt to predict every future task.

---

> **WHY IT WORKS**
>
> Persistent context doesn't improve AI's underlying capability. It changes what AI has to work with. An AI that knows your role, your audience, your style preferences, and your constraints produces better first drafts and needs fewer iterations. The investment is front-loaded, you write the context once, and the return compounds with every subsequent conversation.

---

**What belonging to the same workspace gives you**

When you work within a project or persistent environment:

- Your uploaded documents remain available without re-uploading
- Your style and tone preferences apply without re-specifying
- Your role and context are understood without re-explaining
- Outputs from previous conversations can inform new ones
- Multiple AI conversations about the same work form a coherent body of output

This is a qualitative shift in how AI integrates into professional work. It moves AI from an occasional tool you use for one-off tasks to something closer to a working partner for ongoing projects.

---

> **REAL-WORLD EXAMPLE**
>
> Sarah manages a marketing account for three different clients. She sets up a separate Project for each:
>
> *Project: Hartley Financial*, contains the brand guidelines document, a style reference email, a note on the client's preferences ("informal tone in client-facing copy; formal in regulatory documents"), the previous quarter's campaign materials, and a standing instruction that the client's compliance team must review any copy before publication.
>
> *Project: Meridian Retail*, contains the target audience profile, previous copy that worked well, a note on what the Marketing Director has rejected in the past, and the seasonal campaign calendar.
>
> When Sarah opens the Hartley Financial project to write new email copy, AI already knows the brand, the style, the constraints, and the history. The first draft is usable. Without the project, she would spend the first five minutes of every session re-briefing context she's already established.

---

> **WATCH OUT**
>
> Persistent context can become stale. If your role changes, a client's preferences shift, or a project evolves, the standing context needs to be updated. Review your projects and persistent instructions every few months. Outdated context is better than no context, but not by much, AI will confidently apply the wrong assumptions.

---

## Chapter 11

### Projects and Persistent Instructions

**Setting up persistent instructions**

Persistent instructions are the highest-leverage single investment most regular AI users can make. Writing them well takes thirty minutes. The return on those thirty minutes compounds with every subsequent AI conversation.

---

**What to include in persistent instructions**

The most valuable things to specify in persistent instructions:

**1. Your professional context**
Who you are, what you do, what organisation or sector you work in. This calibrates AI's assumptions about what background knowledge is relevant and what terminology is appropriate.

*Example:* "I am a senior solicitor at a UK mid-market law firm. My clients are typically owner-managed businesses. I communicate with clients, not other lawyers."

**2. Your communication preferences**
Tone, vocabulary level, things you never want to see in output. This is where you codify the things you would otherwise correct in every first draft.

*Example:* "Write in plain English. No jargon unless I request it. No excessive hedging. No bullet lists unless I specify them. UK English throughout. Professional but accessible."

**3. Your standard audience**
Who reads what you produce? This prevents AI from pitching responses at the wrong level.

*Example:* "Assume I am writing for a non-specialist reader unless I specify otherwise. Never assume technical knowledge of legal process or financial instruments."

**4. Key constraints that always apply**
Anything that, if AI ignored it, would make the output unusable. Legal constraints, brand constraints, regulatory constraints, relationship sensitivities.

*Example:* "I work in financial services. Do not make specific investment recommendations. Always include appropriate caveats where content could be interpreted as financial advice."

**5. Things you want AI to always do**
Behaviours you want as default, not just when you remember to ask.

*Example:* "At the end of any factual output, flag any claims I should verify independently. If you are uncertain about any fact, say so explicitly rather than stating it with false confidence."

---

**A template for persistent instructions**

Here is a starting template. Adapt it to your situation:

```
About me:
[Your role, sector, organisation type, years of experience if relevant]

What I typically need AI for:
[Your most common use cases, writing, analysis, research, editing, planning]

My communication preferences:
[Tone, vocabulary level, formatting preferences, things you never want]

My standard audience:
[Who reads your output, clients, colleagues, the public, specialists, generalists]

Key constraints that always apply:
[Legal, regulatory, brand, relationship, or accuracy constraints]

What I always want AI to do:
[Default behaviours you want in every interaction, verification flags, format defaults, etc.]
```

---

> **TRY THIS**
>
> Set up your persistent instructions today. Use the template above. Start with the sections that feel most obvious, your professional context and communication preferences, and add the others as you notice what you keep re-specifying in individual conversations.
>
> After two weeks, review the instructions. What are you still correcting in every conversation? That's a gap in your persistent instructions. Add it.

---

**Setting up a project**

Projects are more powerful than persistent instructions because they can also hold documents, ongoing outputs, and accumulated context. Here is how to approach setting one up:

**Step 1, Define the project's purpose**
What work is this project for? One client? One recurring task type? One ongoing work project? The answer determines what belongs in it.

**Step 2, Write the project instructions**
These are like persistent instructions but scoped to this project. Include the context specific to this work that doesn't belong in your general instructions.

**Step 3, Upload relevant documents**
What documents does AI need to do this project's work? Upload them. Brand guidelines, style guides, reference documents, previous outputs, client briefs.

**Step 4, Name conversations clearly**
Within the project, give conversations descriptive names. "Email sequence for Q4 campaign" is more useful six weeks later than "New Chat (3)."

---

> **PRODUCT NOTE (Verified September 2026):**
> ChatGPT Projects are available on free and paid plans, with file limits that vary by plan. Claude Projects are available on paid plans. Gemini offers workspaces and custom configurations, but the names, file behaviour, and availability vary by product and account. Feature details change frequently; verify current capabilities and limits in the platform's help centre before relying on a specific feature.
>
> Volatility: HIGH

---

**The project for recurring work**

Some of the most valuable AI projects are not for unique work, but for recurring tasks. If you produce the same type of document weekly or monthly, a status report, a client briefing, a team update, a project containing your template, your style reference, and your standard content elements saves significant setup time.

For recurring work, the project contains:

- A template for the document type
- Style and tone specifications
- An example of a completed version you were happy with
- Any standard information that appears in every edition (team structure, project status, recurring context)

Each week or month, you open the project, paste in the new content or data, and ask AI to produce the new version to the same standard as the example.

---

## Chapter 12

### Files, Documents, and Source Material

**Why you should give AI documents, not descriptions**

There is a consistent pattern in how people under-use AI: they describe the document instead of providing it.

*"I have a market research report that says our target demographic is 25-34..."*
*"Based on our company values, which include innovation and customer focus..."*
*"Our pricing is roughly in the mid-range for the sector..."*

These descriptions are always incomplete. They filter the document through the user's current focus and omit everything that doesn't seem immediately relevant, including things that might matter.

When you provide the actual document, AI can read all of it. It can notice things you didn't highlight. It can extract the specific data point you forgot to mention. It can identify tensions between different sections that your description smoothed over.

Provide documents, not descriptions of documents.

---

**What AI can do with documents**

The practical capabilities, as of late 2026:

**Summarise**, Extract key points, findings, or decisions at a specified level of detail.

**Extract**, Pull out specific information: all the action items from meeting notes, all the financial figures from a report, all the dates and deadlines from a contract.

**Analyse**, Identify patterns, inconsistencies, risks, or significant points: flag anything in this contract that differs from our standard terms; identify which sections of this report have the weakest evidence.

**Compare**, Compare multiple documents: these two supplier proposals against the same set of criteria; this year's report against last year's.

**Answer questions**, "What does this contract say about notice periods?" "What is the research paper's conclusion about the effect of X on Y?"

**Rewrite or adapt**, Take an existing document and adapt it: rewrite in simpler language; convert to a different format; update with new information.

---

**What to watch out for with documents**

AI can make mistakes when working with documents, and those mistakes can be difficult to spot:

**Hallucinating content**, AI may generate a plausible-sounding claim about a document that is not actually in the document. Always verify specific extracted facts against the original.

**Missing important nuance**, AI may summarise a complex legal or financial document in a way that loses critical nuance. "The contract allows termination with 30 days notice" may be accurate but miss that this only applies to non-performance situations.

**Incorrect numbers**, AI sometimes misreads or miscalculates figures in documents. Any number extracted from a document should be verified against the source.

**Losing track of long documents**, Very long documents may not be fully attended to. Important information in the middle or end of a very long document is more likely to be missed than information at the beginning.

---

> **VERIFY**
>
> After any significant extraction or analysis task on a document:
> 1. Check at least two specific extracted facts against the source document directly
> 2. Ask AI what it considered to be the most uncertain or ambiguous parts of the document
> 3. Ask AI to flag any information it couldn't find in the document that your prompt might have led it to expect
>
> These three checks catch the most common document-analysis failures.

---

**Document types and how to use them**

**Contracts and legal documents**
Most useful for: identifying specific clauses, comparing to standard terms, extracting obligations and deadlines, generating a plain-English summary.
Always verify: any claim about rights, obligations, or liabilities against the exact contract language.

**Financial reports and data**
Most useful for: summarising findings, extracting key figures, identifying trends, generating plain-English explanation.
Always verify: specific numbers against the source.

**Research papers**
Most useful for: summarising methodology and findings, identifying key claims, extracting conclusions.
Always verify: is this what the paper actually concludes? Has the summary missed important limitations?

**Meeting notes and transcripts**
Most useful for: extracting action items, producing a summary, identifying decisions made, creating a follow-up email.
Watch out for: misattributing who said what, missing an action item from a long transcript.

**Internal documents**
Most useful for: adapting existing content, maintaining consistency, finding relevant previous work.
Watch out for: applying information from outdated documents without realising it.

---

> **PRO TIP**
>
> When uploading a long document, help AI navigate it. Tell AI which sections are most relevant: "The contract is 22 pages. For this task, the most relevant sections are the Termination clause (section 8) and the Indemnities (section 14). You can skim the rest unless it's relevant." This focuses AI's attention and tends to produce more accurate extraction from the sections that matter.

---

## Chapter 13

### Tools, What AI Can Do Beyond Text

**AI is not just a text generator**

The AI tools available in late 2026 can do considerably more than generate text. Understanding which capabilities exist, and which don't, determines what you can ask for, what you need to verify externally, and where AI can genuinely replace tasks that previously required separate tools.

This chapter introduces the main tool categories. Because capabilities vary by platform, by plan level, and change frequently, all specific capabilities include a Product Note with a volatility rating. High-volatility items are not in the main body.

<!-- VISUAL: tools-capabilities -->

---

**Web search**

Most major AI platforms can search the web during a conversation. This changes one of AI's most significant limitations: its knowledge cutoff.

Without web search, AI's knowledge has a cutoff date. If you ask about recent events, current prices, or the latest data, AI either doesn't know or (more dangerously) generates plausible-sounding but outdated information.

With web search enabled, AI can retrieve current information and incorporate it into responses. It can check whether something has changed, find recent statistics, and access information published after its training cutoff.

**What web search changes:**
- AI can answer questions about recent events
- AI can retrieve current data rather than estimating from outdated training data
- AI can find specific sources rather than relying on memory

**What web search does not change:**
- AI still interprets and summarises what it finds, and can still get that interpretation wrong
- Not all information is publicly accessible on the web
- AI can still be wrong about which sources to trust
- You still need to verify important claims

> **PRODUCT NOTE (Verified September 2026):**
> OpenAI, Anthropic, and Google all document web-search or research capabilities, but access, names, limits, and default behaviour vary by product, plan, region, and rollout. Always confirm whether search was used in a given response if accuracy matters.
>
> Volatility: MEDIUM

---

**Deep Research and multi-step web research**

Some platforms now offer a research mode that does more than answer a single search question. It can plan a search, investigate several sources, compare what it finds, and return a cited report. The name and exact behaviour vary: a platform may call it Deep Research, Research, or use another label.

Use it when the question is broad, current, and worth the time required for a proper investigation. Do not use it as a shortcut around verification.

**A reliable research brief**

1. State the decision or piece of work the research will support.
2. Define the date range, geography, audience, and terms that matter.
3. Ask for primary or authoritative sources where they exist.
4. Request a source-linked report that separates evidence from interpretation.
5. Review the plan or scope before the research runs, if the platform offers that option.
6. Open the important sources and verify the claims you intend to use.

**Web Research Checklist**

- Did I define the date, place, audience, and decision this research supports?
- Did the tool actually use web sources, or did it answer from its existing context?
- Can I open the cited source and find the claim there?
- Is the source primary or authoritative for this question?
- Did the tool distinguish evidence from interpretation?
- What remains uncertain, disputed, or outside the scope of the search?

For example:

```
Research the current rules for [specific question] in [jurisdiction] as of [date].
This will support [decision or document]. Prefer official government,
regulator, company, or primary research sources. Give me:
1. the answer in plain English;
2. the sources for each important claim;
3. areas where sources disagree or the position is uncertain;
4. a list of facts I should verify before relying on the result.
Do not fill gaps with assumptions. Say what you could not establish.
```

The citations are a map back to the evidence, not a guarantee that the report is correct. Research tools can select weak sources, misread a source, or draw a conclusion the source does not support. The verification step remains yours.

> **PRODUCT NOTE**
> OpenAI, Google, and Anthropic all document research tools that can search across multiple sources and return citations, but access, limits, connected sources, and names vary by plan, region, and product. Check the current help centre before designing a workflow around one. The stable principle is: define the research task, inspect the sources, and verify the claims that matter.
>
> Volatility: HIGH

---

**Code execution and calculation**

Some AI platforms can write and run code within the conversation, enabling reliable calculation and data processing.

This is significant because it addresses one of AI's consistent weaknesses: arithmetic and calculation. When AI uses code execution, it doesn't estimate calculations, it runs them. The result is accurate in the same way a spreadsheet result is accurate (if the formula is right).

Practical uses:
- Accurate calculations on data you provide
- Processing and analysing datasets
- Running formulas or statistical operations
- Generating charts and graphs from data

**What this changes:** Calculations performed via code execution are reliable. Calculations performed without code execution, AI simply generating the answer as text, are not reliably accurate, particularly for anything beyond simple arithmetic.

**The rule:** If your task involves maths that matters, either use a platform with code execution enabled, or verify the calculation yourself.

> **PRODUCT NOTE (Verified September 2026):**
> Several major platforms support code execution, file analysis, or both, but the feature name, access, limits, and supported formats vary. Consult the current platform documentation before relying on a calculation or data workflow.
>
> Volatility: MEDIUM

---

**Image generation**

Some AI tools can generate images from text descriptions. This capability is useful for:
- Rough concept visualisations for design briefs
- Placeholder images for presentations
- Illustrations for non-commercial documents
- Visual brainstorming

**What to be careful of:**
- Generated images may not be suitable for commercial use without checking the platform's terms
- Generated images of people can produce photorealistic results that may be misleading out of context
- Quality varies significantly across platforms

> **PRODUCT NOTE (Verified September 2026):**
> Image generation is integrated into several major AI platforms, but product names, models, access, and licensing terms vary. Verify the platform's current terms and applicable law before using generated images commercially.
>
> Volatility: HIGH, See Appendix E for current details.

---

**File creation and export**

AI tools increasingly support creating downloadable files: documents, spreadsheets, presentations. This is still an evolving area, with quality and reliability varying considerably.

The practical approach: use AI to generate the content and structure, then create the final formatted document in your standard tool (Word, Excel, PowerPoint, Google Workspace). Attempting to produce final, formatted output directly from AI is often slower and less reliable than the two-step approach.

---

**What AI tools cannot reliably do (as of late 2026)**

Equally important is knowing what AI tools currently cannot do well:

- **Send communications on your behalf** without explicit confirmation steps
- **Access your internal systems** (email, calendar, CRM, databases) without integration tools set up by your organisation
- **Make decisions** that require judgment, ethics, or accountability, AI can analyse and recommend; decisions remain with you
- **Replace professional advice** in law, medicine, finance, or other regulated domains, AI can inform; professionals advise

---

> **WATCH OUT**
>
> Tool availability changes. A capability that exists today may be modified, restricted, or removed. A capability that doesn't exist today may arrive. The best practice is to verify current capabilities on the platform's own documentation before designing a workflow around a specific tool feature. This book covers capabilities as of September 2026; check Appendix E and the platform's help centre for current status.

---

## Chapter 14

### The Memory Problem (and How to Work Around It)

**Why AI doesn't reliably remember you**

Unless a platform explicitly supplies relevant saved context, project knowledge, searchable history, or connected sources, every time you start a new conversation with an AI tool, you are meeting a stranger who happens to be very knowledgeable. They do not reliably know your name, your job, your preferences, your previous conversations, or anything about your situation.

The practical effect is that you should spend time re-establishing important context unless you have confirmed which persistence feature is active and what it can access.

Some platforms have begun introducing memory features, where AI can retain facts between conversations. These features are useful but imperfect, and their availability and reliability vary. This chapter covers the memory problem and its most practical workarounds.

---

**The four types of "memory" in current AI tools**

**In-conversation memory (always available)**
Within a single conversation, AI remembers everything that has been said. You can refer to "the document we discussed" or "your earlier suggestion" and AI will understand. This is reliable and consistent.

**Platform memory features (variable)**
Some platforms offer features that carry specific facts across conversations, things you told AI about yourself, preferences you established, key information you asked it to remember. These vary in scope and reliability.

> **PRODUCT NOTE (Verified September 2026):**
> ChatGPT offers saved memory and project memory, with availability and settings varying by plan and workspace. Claude offers profile preferences, project instructions, project knowledge, andwhere enabledsearch across previous chats. These are different mechanisms, not a guarantee that an AI remembers everything. Check the current documentation and verify what context a response actually used.
>
> Volatility: HIGH, See Appendix E.

**Project memory (the most reliable approach)**
Working within a Project creates a persistent context that AI carries across all conversations in that project. This is currently the most robust workaround for the memory problem for regular, recurring work.

**Document memory (the universal workaround)**
A context document you paste in at the start of any conversation. Reliable across all platforms, requires no platform feature, and completely under your control.

---

**Building a context document**

A context document is a brief, structured summary of what AI needs to know about you and the work it will help with. It is the universal workaround for the memory problem.

Here is a template:

```
CONTEXT DOCUMENT, [Your name / role]
Last updated: [Date]

About me:
[2-3 sentences: role, sector, organisation type]

Current work context:
[What I'm working on, any ongoing projects, key relationships]

My communication preferences:
[Tone, format, UK/US spelling, things I never want in output]

Key constraints:
[Anything AI must not say, recommend, or assume]

My standard audience:
[Who reads what I produce]

Things I always want AI to do:
[Default behaviours, verification flags, format defaults, etc.]
```

A well-written context document takes twenty minutes to produce once and can be pasted into any AI conversation in seconds. It is more reliable than any platform feature and works across all tools.

**A filled-in context document**

Consider Priya, a secondary-school teacher preparing differentiated materials. Her context document might begin:

```
CONTEXT DOCUMENT, Priya, Year 8 science teacher
Last updated: September 2026

I teach mixed-ability Year 8 classes in England. Materials must use
plain language, support different reading levels, and align with the
current specification I provide. Never invent curriculum requirements
or present generated material as ready for students without teacher
review. Flag scientific claims, safety issues, and assumptions.

When I ask for differentiated material, give me a core version and
two accessible variations. Keep the learning objective unchanged.
```

The document does not make AI responsible for the lesson. It gives AI a stable starting point and tells Priya what to check. She still supplies the current specification and reviews anything pupils will see, but she no longer has to repeat the class context and safety expectations in every session.

---

**Memory that matters and memory that doesn't**

Not everything needs to be remembered. The investment in persistent context should be proportional to how often you'll need it.

**Worth persisting:**
- Your role, audience, and communication style
- Recurring project context
- Key constraints that always apply
- Your quality standards and preferences

**Not worth persisting:**
- One-off tasks
- Information that changes frequently
- Details specific to a single conversation

The test: if you would type this information again in your next AI session, persist it. If it's specific to today's task and you won't need it tomorrow, don't bother.

---

## Chapter 15

### Building Your Personal AI Workspace

**From ad hoc to systematic**

Part III has covered the building blocks of an AI environment: persistent instructions, projects, document management, tools, and memory. This chapter shows how to put them together into a workspace that reflects how you actually work.

A well-built AI workspace is not a technical achievement. It is a professional one: the result of thinking carefully about what you need AI for, what context it should always have, and how your recurring work is organised.

---

**The workspace audit**

Before building, take stock. Answer these questions:

**What do I use AI for most often?**
List your five most common AI tasks. These are the tasks your workspace should be optimised for.

**What context do I re-enter repeatedly?**
What information do you find yourself providing in almost every session? This is what should be in your persistent instructions.

**What recurring projects or task types do I have?**
What work comes around every week, every month, or for every client? Each recurring type deserves its own Project.

**What documents does AI regularly need?**
What files do you find yourself uploading repeatedly? These belong in the relevant Project.

**What are my quality standards?**
What makes output unusable for you? What do you always correct? These corrections belong in your persistent instructions as explicit rules.

**A completed workspace audit**

Take David's consultancy as an example. His answers produce three workspaces:

- **Client work:** one Project per active client, containing the brief, approved source documents, a tone reference, previous deliverables, and client-specific constraints.
- **Recurring reports:** a Project containing the reporting template, a completed example, the standard headings, and the monthly input checklist.
- **Personal practice:** a small workspace for prompt experiments, failure notes, and reusable patterns that are not tied to a client.

His persistent instructions hold the information that applies everywhere: his role, UK spelling, plain professional language, and a default instruction to flag unsupported facts. Project instructions hold what changes by client or task. This separation prevents a client-specific constraint from leaking into unrelated work.

---

**A simple workspace structure for most professionals**

```
PERSISTENT INSTRUCTIONS (applies to everything)
├── Professional context
├── Communication preferences
├── Standard audience
└── Default behaviours (verification, format, etc.)

PROJECTS
├── Project A: [Client / Ongoing work 1]
│   ├── Project instructions (context specific to this work)
│   ├── Reference documents (brand guide, style reference, etc.)
│   └── Ongoing conversations
│
├── Project B: [Client / Ongoing work 2]
│   └── [Same structure]
│
└── Project C: Recurring tasks
    ├── Weekly report template and example
    ├── Standard document formats
    └── Template prompts for recurring work
```

---

**The recurring task template**

For any task you do on a regular cadence, a template prompt is worth building. A template prompt is a prompt with placeholders, variables you update with each use, built on a structure you've already tested and refined.

Format:

```
[TEMPLATE NAME]

Context (stable):
[Everything that stays the same, purpose, audience, style, constraints]

Variable inputs this week:
[PASTE CONTENT HERE]
[KEY DATES: X]
[KEY DECISIONS: X]

Output required:
[Format, length, structure, specified once, used every time]
```

This reduces a recurring AI task to: open the template, fill in the variables, run. The setup investment is front-loaded; the recurring use is fast.

---

> **PRO TIP**
>
> Keep a "templates" section within your AI workspace, either a Project dedicated to this, or a simple document you maintain. When you write a prompt that works especially well, save it. When you develop an interaction pattern that produces good results consistently, document it. Your prompt library becomes more valuable than any generic prompt template book because it is tested, specific to your work, and continuously refined.

---

**Workspace maintenance**

A workspace that isn't maintained becomes a liability. Outdated context produces confidently wrong outputs. Review your workspace periodically:

- **Monthly:** Are the persistent instructions still accurate? Has anything changed about your role, audience, or constraints?
- **When a project ends:** Archive or close the project so it doesn't contaminate future work with irrelevant context.
- **When something keeps going wrong:** What's in your workspace that might be causing this? What context might AI be applying incorrectly?

The workspace is a living document of your working relationship with AI, not a one-time setup.

---

> **WATCH OUT**
>
> Workspaces created on one platform do not transfer to another. Your Claude Projects, your ChatGPT custom instructions, and your Gemini settings are all separate. If you use multiple platforms, you need to maintain context in each, or accept that some platforms know more about your preferences than others. Many users find it practical to choose a primary platform for their most important work and use secondary platforms with more ad hoc setup.

---

**What Part III has established**

You now have the framework for building an AI environment:

- Persistent instructions that carry your context forward automatically
- Projects that organise your work and maintain document access
- Document handling practices that maximise accuracy and catch common errors
- An understanding of tools and their limitations
- A memory strategy that works across platforms
- A workspace structure suited to professional use

Part IV moves from individual interactions and workspace setup to something qualitatively different: multi-step workflows that tackle complex tasks by breaking them into stages.

---

# PART IV

## From Prompts to Workflows

*Complex work doesn't happen in a single exchange. Part IV introduces the thinking and techniques that take AI from answering individual questions to participating in multi-stage processes, planning, drafting, reviewing, revising, and handing off.*

---

## Chapter 16

### When One Prompt Isn't Enough

**The single-prompt ceiling**

For simple, well-defined tasks, summarise this, draft that, answer this question, a single well-crafted prompt is usually sufficient. But professional work is rarely simple and well-defined.

A business proposal is not one task. It is: research the client, understand their problem, frame the approach, develop the argument, structure the document, draft each section, review for consistency, check for gaps, refine the language, and produce a final version. Each of these is a distinct cognitive task that benefits from distinct treatment.

Attempting to produce a business proposal in a single prompt produces a generic outline at best and a generic document at worst. Neither is what you needed.

The ceiling of single-prompt AI use is low. Most professional work requires workflows.

---

**What makes something a workflow**

A workflow, for our purposes, is any AI task that:

- Involves more than one distinct phase (research, then structure, then draft, then review)
- Produces output that becomes input to the next stage
- Benefits from human review and adjustment at one or more stages
- Is too complex for a single prompt to handle well

Most significant pieces of work, proposals, reports, analyses, plans, complex communications, are workflows. The shift to thinking in workflows is one of the biggest quality improvements available to regular AI users.

---

**Why breaking tasks into stages works**

When you ask AI to do too many things at once, it compromises on everything. The research is superficial because the prompt also asked for structure. The draft is generic because the prompt also asked for analysis. The analysis is shallow because the prompt also asked for recommendations.

Breaking a task into stages allows AI to do each stage well, with appropriate depth and focus. It also allows you to review and adjust at each stage before committing the next stage to an approach that might be wrong.

The best analogy is professional practice: a good architect doesn't hand you the construction drawings at the first meeting. They produce a brief, then a concept, then a scheme, then detailed drawings, each stage reviewed and approved before the next begins.

---

**The three most common multi-stage patterns**

**The Research-Plan-Draft pattern**
Stage 1: Research and gather information. Stage 2: Plan the structure. Stage 3: Draft the content.

This is the most universally useful workflow. Almost any document benefits from separating the gathering of content from the writing of it.

**The Draft-Review-Refine pattern**
Stage 1: Produce a complete draft. Stage 2: Review the draft against explicit criteria. Stage 3: Refine based on the review.

This is particularly valuable because Stage 2 uses a different cognitive mode than Stage 1. Writing mode and editing mode are different, and separating them, even within AI, produces better results.

**The Decompose-Execute-Assemble pattern**
Stage 1: Break a large task into components. Stage 2: Execute each component separately. Stage 3: Assemble the components.

This is most useful for large documents or complex outputs where different sections require different content or expertise.

---

> **REAL-WORLD EXAMPLE**
>
> David needs to produce a quarterly business review for his consultancy's three largest clients.
>
> **Single-prompt approach:** "Write a quarterly business review for Client X." Result: A generic template that David has to fill in entirely himself.
>
> **Workflow approach:**
>
> *Stage 1:* "I'm going to paste in my notes from the last three months of client interactions, plus their project status reports. Extract: key achievements, challenges faced, decisions made, and open items. Present as a structured list, not prose."
>
> David reviews the extraction, adds two items AI missed, removes one that was irrelevant.
>
> *Stage 2:* "Using the extracted information, create a narrative structure for the quarterly review. Three sections: What We Achieved, What We Learned, and What Comes Next. For each section, suggest what the key two or three points should be."
>
> David adjusts the suggested structure, moves one point to a different section, adds a point AI didn't suggest.
>
> *Stage 3:* "Now draft the quarterly review document using the structure we agreed. Professional tone, plain language, about 800 words. The client is the owner and will share it with their management team."
>
> The resulting document is specific, accurate, and usable. It took less time than the single-prompt version and produced dramatically better output, not because AI was better, but because the workflow allowed human judgment to guide it at each stage.

---

> **WHY IT WORKS**
>
> Multi-stage workflows work for the same reason that professional processes work: each stage has a clear purpose, a clear deliverable, and a defined handoff point. Breaking work into stages allows you to catch errors before they compound. It allows you to apply different types of thinking to different types of sub-tasks. And it allows AI to do each sub-task well rather than doing all sub-tasks adequately.

---

## Chapter 17

### Breaking Tasks Into Steps

**The decomposition skill**

The most important skill in multi-step AI work is not writing better prompts. It is breaking tasks into the right stages.

A well-decomposed task has stages that:
- Have distinct deliverables
- Can be reviewed independently
- Build on each other in a clear sequence
- Are each achievable to a high standard in a single focused interaction

Poorly decomposed tasks break in the wrong places, create dependencies that are hard to manage, or duplicate work across stages.

This chapter teaches the decomposition patterns that work most reliably across common professional tasks.

---

**Decomposition pattern 1: Information → Structure → Content**

The most broadly applicable pattern. Works for almost any document.

```
Stage 1, Information gathering
"Extract all the relevant information from [source(s)]."
→ Output: Raw material, structured as a list

Stage 2, Structure design
"Given this information, propose a document structure.
 What are the main sections? What is the most logical order?
 What is the key argument or narrative?"
→ Output: Document structure with brief section notes

[Human review: Adjust structure before committing to draft]

Stage 3, Draft
"Draft [Document X] using the agreed structure."
→ Output: Full draft

Stage 4, Review and refine (optional, Chapter 18)
```

This pattern works for: proposals, reports, articles, presentations, plans, briefing documents.

---

**Decomposition pattern 2: Clarify → Explore → Recommend**

Most useful for analysis and decision support.

```
Stage 1, Clarify the question
"Help me define exactly what question I need to answer.
 Here is the situation: [context]
 Here is what I'm trying to decide: [decision]
 What additional information would be most valuable? What are the key sub-questions?"
→ Output: Sharper framing of the problem

Stage 2, Explore options and evidence
"Given this framing, what are the main options or considerations?
 What does the evidence suggest about each?"
→ Output: Analysis of options

Stage 3, Recommend
"Based on what we've established, what would you recommend and why?
 What are the main risks of your recommendation?"
→ Output: Recommendation with reasoning and risk assessment
```

This pattern works for: decision preparation, strategy analysis, problem diagnosis, options assessment.

---

**Decomposition pattern 3: Components → Draft each → Assemble**

Most useful for large documents with distinct sections.

```
Stage 1, Define components
"This document has [N] sections: [list them]. 
 Let's draft each one separately. Start with Section 1."

Stage 2, Draft each component
[For each section:]
"Draft Section [N]: [title]. 
 Key points to cover: [list].
 Length: [specification].
 Tone: [specification]."

Stage 3, Assemble and review
"I'm going to paste in all sections now. 
 Review them as a complete document:
, Do they flow logically?
, Are there repetitions or gaps?
, Is the tone consistent throughout?
, What would you change?"
```

This pattern works for: annual reports, long proposals, training materials, multi-section documents.

---

**Making handoffs explicit**

Between stages, always do two things:

**1. Review the output.**
Does the output of Stage N accurately reflect what you wanted? Is anything missing? Is anything wrong? Correct it before it propagates to Stage N+1.

**2. Carry forward what matters.**
When moving to the next stage, either reference the previous output directly (in the same conversation, AI will remember it) or paste in what AI needs to know. Don't assume AI will apply context from Stage 1 accurately at Stage 3 if the conversation is very long.

---

> **TRY THIS**
>
> Take a piece of work you need to produce in the next week. Spend five minutes mapping it:
>
> 1. What are the distinct stages this work naturally has?
> 2. What is the deliverable of each stage?
> 3. Where is human review most important, where could an error in Stage N make Stage N+1 irretrievably wrong?
>
> Now design the workflow before you start. The map will tell you what to ask AI for at each stage.

---

> **WATCH OUT**
>
> Stages that are too granular create overhead without benefit. If you find yourself doing ten stages for a task that could be done in three, you have over-decomposed. The right granularity is: each stage produces something that can be reviewed and corrected before the next stage begins. If a stage is so small that there's nothing meaningful to review, combine it with the adjacent stage.

---

## Chapter 18

### Critique, Edit, and Improve

**Using AI against its own output**

One of the most underused techniques in AI work is asking AI to critique what it has produced.

This sounds circular, and it is, slightly. AI is reviewing its own work, which might seem unlikely to catch errors it didn't notice the first time. But it is more effective than it sounds, for a practical reason: critique mode is a different cognitive stance than generation mode. When you ask AI to switch from producing to evaluating, it activates different patterns and often catches problems it generated in draft mode.

---

**The critique loop**

The basic critique loop has three steps:

**Step 1, Produce a draft**
Ask AI to produce the draft as normal.

**Step 2, Apply the critique prompt**
Ask AI to evaluate the draft against explicit criteria. The more specific the criteria, the more useful the critique.

**Step 3, Revise based on critique**
Ask AI to produce a revised version addressing the issues raised.

---

**The critique prompt template**

```
Please review the [document/email/proposal/plan] you just produced.

Evaluate it against the following criteria:
[Criterion 1: e.g., Does it clearly address the reader's main concern?]
[Criterion 2: e.g., Is the argument in the right order?]
[Criterion 3: e.g., Are there claims that could be questioned?]
[Criterion 4: e.g., Is there anything missing?]
[Criterion 5: e.g., Is the tone right for the audience?]

For each criterion: identify what is working well and what could be improved.
At the end: give a one-paragraph overall assessment.
Do not be generous. The goal is a better document, not reassurance.
```

The instruction "do not be generous" matters. Without it, AI tends to produce critique that finds much to praise and softens its concerns. This produces pleasant but not especially useful critique.

---

> **WHY IT WORKS**
>
> Critique mode works better than it theoretically should because AI is drawing on large bodies of material about what constitutes good work in different domains. When asked to evaluate against explicit criteria, it can apply those standards more rigorously than it applies them by default in generation mode. Think of it as asking a writer to switch hats: generation mode produces content; critique mode applies editorial judgment.

---

**The Before → Better → Best: critique loop**

The scenario: Sarah has used AI to draft a proposal section and wants to improve it before sending.

*Stage 1, Draft produced*

[AI produces a draft proposal section about the agency's approach to the client's brief]

*Stage 2, Critique applied*

Sarah sends: *"Please review the proposal section you just drafted. Evaluate it against these criteria: Does it address the client's specific situation or is it generic? Is the argument clear and logical? Are there any claims that aren't supported by what I've told you? Is the tone right for a director-level reader at a mid-size retail company? What's missing? Be direct, I need useful feedback, not reassurance."*

AI responds: *"A few issues to flag. The opening paragraph describes the agency's general approach rather than the client's specific situation, a sceptical reader will notice you haven't demonstrated understanding of their particular challenge. The 'proven results' claim on page two isn't backed by anything specific in what you've provided. The case study section is good but should come earlier, it's currently buried after the methodology, but for this type of client, demonstrated experience is probably the first thing they want to see. The tone is appropriate throughout."*

*Stage 3, Revision*

Sarah: *"Revise the draft addressing these points: lead with the client's situation, move the case study up, remove the 'proven results' claim and replace it with [SPECIFIC RESULT I'LL ADD]."*

The resulting revision is substantively better. The critique took two minutes to run. The revision took thirty seconds to instruct. The improvement would have taken Sarah much longer to identify and articulate without the structured critique loop.

---

**Specific critique types**

Different types of work benefit from different critique focuses:

**For persuasive documents (proposals, bids, pitches):**
*"Does this make the reader want to say yes? What objections might they raise? Is the value proposition clear? What is the weakest point in the argument?"*

**For explanatory documents (reports, briefings, guides):**
*"Is the key finding easy to identify? Is the logic clear? Are there technical terms an educated non-specialist would need explained? Is anything assumed that shouldn't be?"*

**For communications (emails, letters, announcements):**
*"Is the purpose of this communication immediately clear? Is the tone right for the relationship? Could anything be misinterpreted? Is there anything missing the recipient will need to act on this?"*

**For creative or marketing content:**
*"Is the opening strong enough to keep a reader going? Is there any generic marketing language that a sceptical reader would discount? Is the call to action clear?"*

---

**Critique with an adversarial persona**

For high-stakes documents, a more powerful critique technique is asking AI to adopt a specific adversarial perspective:

*"Review this proposal as if you are a procurement director at a large company who has seen hundreds of similar proposals and is looking for reasons to discount this one. What would make you sceptical? What would make you put this in the discard pile?"*

*"Review this contract clause as if you are a lawyer representing the other party. What would you challenge? What ambiguity would you exploit?"*

*"Review this business case as if you are a CFO who has been burned by overoptimistic projections before. What assumptions are too aggressive? What risks are underplayed?"*

These adversarial critique prompts produce more rigorous feedback than neutral evaluation and are particularly valuable before anything is presented to an actual sceptical audience.

---

> **WATCH OUT**
>
> AI critique has two consistent weaknesses. First, it tends to be comprehensive in format but inconsistent in depth, it will often identify a problem without identifying the correct solution. Second, it may miss issues that require external knowledge it doesn't have: the client context it wasn't given, the regulatory nuance that requires specialist knowledge, or the political sensitivities you didn't mention. Use AI critique to catch structural, logical, and stylistic issues. Use human review to catch everything that requires knowledge or judgment AI doesn't have.

---

## Chapter 19

### Chains, Loops, and Handoffs

**Start with a complete workflow**

Before naming the mechanics, look at what a useful workflow feels like in practice. David needs to produce a client brief from call notes, emails, and earlier project context:

1. AI extracts the client's requirements and uncertainties.
2. David reviews the extraction, corrects one mistake, and adds two missing requirements.
3. AI proposes a structure for the brief.
4. David approves the structure before AI drafts it.
5. AI drafts the brief section by section.
6. AI critiques the draft against the agreed brief.
7. AI revises the draft, and David makes the final decision about what can be sent.

The quality comes from the connections between the stages: clear outputs, deliberate human review, and a defined standard for improvement. Now we can name the three mechanics that make those connections work.

**The building blocks of complex workflows**

Chapter 17 introduced decomposition patterns. This chapter introduces the mechanics of connecting stages together, the "plumbing" of multi-step AI workflows.

Three mechanics cover most of what you will encounter:

**Chains**, Sequential stages where each output becomes the next input
**Loops**, Iterative cycles where output is reviewed and refined until it meets a standard
**Handoffs**, Points where the work passes from AI to a human (or vice versa) for a specific contribution

Understanding which mechanic applies to which part of a task is what turns a list of stages into a functioning workflow.

<!-- VISUAL: workflow-mechanics -->

---

**Chains**

A chain is the simplest multi-step pattern: A → B → C. Each step's output is the input to the next.

The key discipline in a chain is maintaining coherence: each step should produce output that is complete enough and well-formed enough to be a useful input to the next step. If Step 2 depends on Step 1 and Step 1 is mediocre, Step 3 will inherit and amplify that mediocrity.

**The chain discipline:**
- Review each step's output before proceeding to the next
- If a step's output is substantially wrong, correct it before proceeding
- Be explicit about what carries forward: "Using the outline from Step 1, now draft Section 3"

---

**Loops**

A loop is an iterative cycle: Produce → Review → Improve → (Review again) → (Improve again) → Done.

Loops are appropriate when:
- The quality bar is high and the first draft is unlikely to meet it
- The criteria for success are explicit and can be systematically applied
- Time spent iterating is less than time spent correcting downstream

The critique loop in Chapter 18 is a loop. So is any scenario where you are refining a draft toward a specific standard.

**The loop discipline:**
- Define what "done" looks like before you start looping, otherwise loops run indefinitely
- Be specific about what is wrong in each review cycle, vague feedback produces marginal improvement
- Know when to stop: a document that is 90% right and been through two loops is usually better to complete by hand than to loop a third time

---

**Handoffs**

A handoff is a point where the work passes between AI and human. Handoffs are not failures, they are deliberate design choices about where human judgment adds value that AI cannot.

The best workflows design handoffs deliberately:

**AI → Human handoffs** occur when:
- AI has produced material that needs human judgment to evaluate (is this claim actually correct?)
- The next step requires knowledge AI doesn't have (what does the client actually want?)
- A decision needs to be made that carries accountability (does this represent our position?)
- The work will be put in front of someone who needs to trust it

**Human → AI handoffs** occur when:
- A human has made a judgment that AI should now implement (here's the structure I want, now draft it)
- New information has arrived that AI needs to incorporate (here's their response, now draft a reply)
- A human review has identified specific changes that AI should make

---

---

> **PRO TIP**
>
> Document your best workflows. When you design a workflow that works well for a type of task, write it down as a template. The workflow structure, not just individual prompts but the sequence, the handoff points, and the review criteria, is reusable. Over time, a small library of tested workflow templates is one of the most valuable assets you can build as a professional AI user.

---

> **WATCH OUT**
>
> Over-engineered workflows add overhead without proportionate benefit. A three-paragraph email does not need a seven-stage workflow. Scale the process to the stakes and complexity of the work. A major proposal warrants multiple stages with careful review. A routine internal update does not. The workflow discipline is most valuable when the stakes are high and the output will be scrutinised, apply proportionate judgment elsewhere.

---

**What Part IV has established**

You can now design and execute multi-step AI workflows:

- Recognise when a task requires multiple stages
- Break tasks into stages with clear deliverables and handoff points
- Apply three decomposition patterns to different task types
- Use the critique loop to improve drafts systematically
- Connect stages with chains, loops, and deliberate handoffs

Part V applies these skills to twenty-five specific, tested workflows across the most common professional and personal use cases.
