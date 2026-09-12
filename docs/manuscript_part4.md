# PART VI

## The AI User's Playbook

*The twenty-five workflows in Part V are only as good as the habits that surround them. A technically perfect workflow can still produce embarrassing or harmful output if the result goes unverified. A strong AI practice is built on something less glamorous than clever prompts: the discipline of knowing when to trust output, what to check, and how to catch errors before they matter.*

*Part VI is about that discipline. It is, in many ways, the most important part of the book.*

---

## Chapter 20

### How to Verify AI Output

**The confidence problem**

AI writes with the same fluent confidence whether it is correct or incorrect.

This is worth pausing on. When a human expert is unsure, they usually show it: they hedge, they qualify, they say "I think" or "you'd want to check this." When AI is unsure, it typically does not. It produces the same well-structured, authoritative-sounding prose it would produce if it knew exactly what it was talking about.

This is not dishonesty. It is a feature of how AI generates text: it produces the most plausible continuation of the words before it, and confident prose is more plausible than tentative prose in most contexts. But the practical effect is that you cannot use prose confidence as a signal of factual accuracy. The two are disconnected.

This means verification is not optional for important work. It is a habit as fundamental as saving your documents.

---

**What verification is, and is not**

Verification is not re-reading the AI output more carefully.

If the output says "the company was founded in 1987," reading it again more carefully will not tell you whether 1987 is right. It will only tell you that AI says 1987 with apparent confidence.

Verification means checking claims against sources that are independent of the AI output: the original document, the company website, a primary source, a qualified professional, your own direct knowledge of the situation.

Verification is proportional to stakes. A quick summary of a document you will read anyway needs a lighter verification pass than a public statement containing statistics that will be published under your name.

---

**The verification framework**

Before trusting and using any significant AI output, work through these eight questions:

<!-- VISUAL: verification-matrix -->

**1. Is this factual or creative?**

Factual content (dates, names, statistics, company information, legal positions, scientific findings) requires verification against sources. Creative content (writing style, structure, framing) can be assessed on its own merits without external sources.

Know which type of output you have. A report that reads like authoritative factual analysis but was written by AI with no source documents is creative content masquerading as factual, and requires the same verification as factual content.

**2. Does it contain specific numbers?**

Numbers are a high-risk category. AI is confidently wrong about numbers with greater frequency than almost any other category. Any specific statistic, date, financial figure, percentage, or calculation deserves independent verification before you use it.

The test: can you find this number in a source you can point to?

**3. Does it cite sources?**

If AI has cited sources, verify them. AI hallucination of citations is a well-documented and persistent failure mode. AI may produce a citation that looks real, a plausible author name, a plausible journal, a plausible year, for a paper that does not exist. Verify by finding the actual source and confirming the claim attributed to it is what the source actually says.

Do not assume that the presence of citations means the claims are verified.

**4. Are the sources real?**

This is distinct from the previous question. Even if AI has provided real source titles or URLs, verify they are what they claim to be and that the content of the source supports the claim AI made.

**5. Could this information have changed?**

AI has a knowledge cutoff. Information about current prices, regulations, leadership, products, statistics, and events may be outdated. For any fast-moving area, technology, regulation, markets, current events, check whether the information reflects the current situation.

Even with web search enabled, AI may not surface the most recent information or may misread what it finds.

**6. Did AI make an assumption?**

Complex prompts often involve AI filling gaps you didn't explicitly address. AI will do this without flagging it unless you specifically ask.

Ask: is there anything in this output that I didn't specify, and has AI assumed correctly? The missing context from Chapter 6 can produce plausible-but-wrong assumptions that make their way into the output.

A useful check: ask AI directly, "What assumptions did you make in producing this output?"

**7. Did it follow my constraints?**

Check that the output respects the specific constraints you gave. Does it stay within the stated word count? Does it avoid the topics you said to avoid? Is it written for the audience you specified? Is the tone what you asked for?

Constraints are sometimes partially honoured. AI may follow most of your instructions and quietly ignore one. Read explicitly for compliance.

**8. What evidence supports the conclusion?**

For outputs that reach conclusions, make recommendations, or offer analysis: is the reasoning sound? Does the conclusion follow from what was provided? Could the same evidence support a different conclusion?

This is the hardest verification task and the one most commonly skipped. It requires judgment, not just source-checking.

---

> **VERIFY**
>
> **Before You Trust the Answer**
>
> Ask:
>, Is this factual or creative?
>, Does it contain numbers?
>, Does it cite sources?
>, Are the sources real?
>, Could the information have changed?
>, Did the AI make an assumption?
>, Did it follow my constraints?
>, What evidence supports the conclusion?

---

**High-risk output categories**

Some types of AI output require particularly rigorous verification:

**Statistics and data**
Verify every number against a primary source. AI confabulates plausible statistics with notable regularity. The figure "studies show that 73% of employees..." is a common pattern, verify that the study exists, that the figure is correctly stated, and that it applies to the context in which you're using it.

**Names and attributions**
Quotes attributed to named individuals should be verified. AI can generate plausible-sounding quotes from real people that those people never said. This is a category where being wrong can cause significant professional or legal damage.

**Legal and regulatory information**
Law changes. Regulations change. Jurisdictional variations are significant. Any legal or regulatory claim should be verified against current official sources. AI may confidently state a legal position that was correct two years ago and is not correct now.

**Medical information**
As above, and with additional stakes. Verify medical information from qualified professionals and current clinical sources.

**Technical specifications**
Product features, software capabilities, technical standards, all change and all deserve verification from current official documentation.

---

**Lower-risk output categories**

Verification should be proportionate. These categories typically need lighter verification:

- Structural and organisational decisions (how to order a document, what sections to include)
- Tone and style adjustments
- Creative framing and presentation
- General conceptual explanations of stable topics
- Grammar, clarity, and prose quality

Even here, read critically. Low-risk doesn't mean no-risk.

---

> **REAL-WORLD EXAMPLE**
>
> Margaret, a retired professional who has taken up writing local history articles, uses AI to help research a piece about a local Victorian factory. AI produces a confident account of the factory's founding, its owner, and the number of workers it employed at its peak.
>
> She runs the verification checklist. The founding date differs from one she has in a local archive document. The owner's name is slightly different from the name she has found in a census record. The employment figure appears plausible but has no source she can trace.
>
> She uses the AI output as a framework and a starting point, it helpfully organised the narrative structure and identified what she should look for. But every specific fact goes back to a source she can cite. The final article is accurate because she verified; it was well-structured because AI helped.
>
> This is the right relationship between AI production and human verification.

---

**Building the verification habit**

Verification is most useful when it is habitual rather than occasional. The goal is to make it automatic: before you share, publish, send, or act on significant AI output, you have a brief, consistent check.

The check does not need to be long. For most outputs, running through the eight questions takes two minutes. For high-stakes outputs, it takes longer. The discipline is applying it consistently, not applying it intensively.

The section that does most harm is the one you verified every part of except the one part that was wrong.

---

> **WATCH OUT**
>
> Asking AI to verify its own output has limited value. AI can tell you what it believes to be accurate, but this is circular, if AI believed the claim was wrong, it wouldn't have made it in the first place. AI self-review can catch logical inconsistencies and obvious errors, but it cannot substitute for checking claims against independent sources. Use AI critique for structure and reasoning; use external sources for facts.

---

## Chapter 21

### What AI Gets Wrong (Consistently)

**The failure taxonomy**

AI failures are not random. They fall into predictable categories that appear consistently across different models, different platforms, and different types of task. Knowing these categories means you can anticipate where to look, rather than discovering errors after they've caused a problem.

This chapter is a practical catalogue of known AI failure modes, not to make you sceptical of AI, but to make your scepticism accurate: applied where the risks are highest, relaxed where the risks are lower.

<!-- VISUAL: failure-taxonomy -->

---

**Failure Category 1, Hallucination**

*What it is:* AI generates specific facts, names, dates, statistics, citations, or events that did not happen or do not exist, but presents them with the same confidence as accurate information.

*Why it happens:* AI generates plausible text, not verified text. A hallucinated statistic is generated because it is the kind of statistic that would plausibly appear in this type of document. A hallucinated citation is generated because it is the kind of citation that would plausibly appear in academic writing on this topic.

*Where it appears most:*
- Citations and references (highly specific hallucinations)
- Statistics and percentages (plausible but invented figures)
- Biographical facts about real but less prominent people
- Historical detail about events AI has limited training data on
- Company-specific information AI wasn't trained on

*How to catch it:* Verify specific claims against primary sources. Treat all citations as unverified until confirmed. Be especially sceptical of very specific numbers.

*The severity:* High for professional use. A hallucinated citation in a published article, a made-up statistic in a board presentation, or an incorrect legal date in a contract review, these cause real professional and sometimes legal consequences.

---

**Failure Category 2, Outdated information**

*What it is:* AI presents information that was accurate as of its training cutoff but is no longer current.

*Why it happens:* AI's knowledge is frozen at the point of training. The world continues to change. Models released in 2025 may have training data that lags by twelve to eighteen months before release, and then be used for years after.

*Where it appears most:*
- Technology product details (features, pricing, availability)
- Regulatory and legal information
- Organisational information (who holds which role, company structure)
- Market data and economic statistics
- Current events and recent developments

*How to catch it:* For any fast-moving topic, verify current information from official sources. Even with web search enabled, verify important current-state claims.

*The severity:* Medium to high, depending on context. Outdated legal information is high-severity. A slightly outdated technology feature description is lower.

---

**Failure Category 3, Confident over-generalisation**

*What it is:* AI produces statements that are broadly plausible but overstate how generally applicable they are, missing important exceptions, jurisdictional variations, sector-specific differences, or situational nuances.

*Why it happens:* AI generates the most generally accurate response to the most common interpretation of the question. It doesn't automatically surface the ways in which the answer differs for your specific situation.

*Where it appears most:*
- Legal questions with jurisdictional variation ("employment law says X" without specifying which country's)
- Medical questions with individual variation ("the standard treatment is X")
- Business advice without sector or context sensitivity
- Technical guidance where the "standard" approach isn't appropriate for specific circumstances

*How to catch it:* Ask explicitly: "In what situations might this advice not apply? What are the important exceptions?" For professional matters, verify against advice calibrated to your specific jurisdiction and circumstances.

---

**Failure Category 4, Arithmetic errors**

*What it is:* AI makes errors in arithmetic, calculation, and numerical reasoning, particularly on multi-step calculations, percentage calculations, and anything requiring exact arithmetic.

*Why it happens:* AI generates text. Numbers are text. When AI produces "the answer is 43%," it has generated the number 43 because it is plausible in context, not because it has calculated and arrived at 43. Text generation and mathematical calculation are different processes. Without code execution, AI maths is unreliable.

*Where it appears most:*
- Percentage calculations in reports or analyses
- Financial modelling or estimation
- Multi-step arithmetic
- Unit conversions
- Time-based calculations (especially with complex date arithmetic)

*How to catch it:* Check all arithmetic independently. Use code execution when available for anything that matters. Never use an AI-generated financial figure without verifying the arithmetic.

*The severity:* High when numbers appear in decisions, reports, or presentations. A wrong percentage in a financial summary is a professional error regardless of where it came from.

---

**Failure Category 5, Context drift**

*What it is:* In long conversations, AI gradually loses track of constraints and context established early in the conversation, reverting to defaults it would apply without those constraints.

*Why it happens:* AI attends to the full conversation but with diminishing precision as length increases. Constraints stated in message one of a twenty-message conversation may be less firmly applied at message eighteen than they were at message two.

*Where it appears most:*
- Long editing sessions where style constraints gradually slip
- Extended research conversations where early framing becomes less influential
- Multi-stage workflows where the first stage's constraints should carry forward but don't

*How to catch it:* For long conversations, periodically re-state key constraints. When output seems to have drifted from what you specified, check the early conversation and explicitly re-anchor the constraint.

---

**Failure Category 6, Sycophancy**

*What it is:* AI tends to agree with and validate what the user presents, even when the user is wrong. It will often affirm an incorrect claim rather than challenge it, adjust its previous answer to accommodate the user's pushback even when its original answer was correct, and frame critique in ways that are so mild as to be useless.

*Why it happens:* AI is trained using human feedback, which tends to reward agreeable responses. This creates a bias toward agreement and validation.

*Where it appears most:*
- When you present a flawed plan and ask AI to review it
- When you push back on AI's correct assessment and it backs down
- When you ask AI to evaluate your own writing or thinking

*How to catch it:* Actively ask for challenge. Use adversarial critique prompts (Chapter 18). Ask "what is wrong with this?" not "what do you think of this?" When AI agrees with you completely, treat that as a flag worth checking, not a validation.

*The severity:* Moderate. Sycophancy is more a quality issue than a factual one, but it can lead to significant errors when you're looking for honest critique of important work.

---

**Failure Category 7, Instruction drift**

*What it is:* AI partially follows instructions rather than fully following them. It may honour the spirit of an instruction while missing a specific requirement, or follow all instructions except one.

*Why it happens:* Complex sets of instructions create competing pressures. AI optimises across them in ways that may not match your priority ordering. An instruction to "be brief" may be honoured by shortening paragraphs while maintaining a section structure you asked to be removed.

*Where it appears most:*
- Multi-constraint prompts with several specific requirements
- Editing instructions where some changes are made but others are missed
- Format specifications where the structure is approximately right but details are wrong

*How to catch it:* For important outputs, review explicitly against your stated constraints. Check each instruction in your prompt: was it followed? If not, restate it as the sole instruction in a follow-up.

---

**Failure Category 8, Plausible but wrong reasoning**

*What it is:* AI produces reasoning that appears sound, logical structure, coherent argument, sensible-sounding progression, but reaches the wrong conclusion, misapplies a principle, or draws on an incorrect premise.

*Why it happens:* Plausible reasoning is generated in the same way as plausible text. A well-structured argument is a pattern AI has encountered many times and can reproduce convincingly. The quality of the reasoning structure does not guarantee the quality of the reasoning.

*Where it appears most:*
- Legal analysis
- Financial reasoning
- Causal analysis ("X happened because...")
- Risk assessment
- Strategic recommendations

*How to catch it:* For important analytical output, apply the verification question: "Does the conclusion actually follow from the premises?" Test the reasoning by looking for an alternative explanation or conclusion that the same evidence could support. Have a qualified person review reasoning in high-stakes domains.

---

> **PRO TIP**
>
> When you receive an output that matters, ask AI: "What are the three most important ways this analysis could be wrong? What assumptions am I relying on that might not hold?" This is not a perfect catch-all, but it surfaces failure modes AI can identify, which is often enough to direct your verification effort toward the right areas.

---

**A practical summary: where to be most careful**

| Output type | Primary failure risk | Verification priority |
|---|---|---|
| Statistics and numbers | Hallucination, arithmetic error | HIGH, verify all figures |
| Citations and references | Hallucination | HIGH, verify all citations exist |
| Legal/regulatory claims | Outdated info, over-generalisation | HIGH, verify from current official sources |
| Medical information | Over-generalisation | HIGH, verify from clinical sources |
| Reasoning and analysis | Plausible-wrong reasoning, sycophancy | MEDIUM, check argument logic |
| Current events/market data | Outdated information | MEDIUM, verify recency |
| Technology specifications | Outdated information | MEDIUM, verify from official docs |
| Writing and structure | Instruction drift | LOW, read against your brief |
| Creative framing | Generally lower risk | LOW, assess on merits |

---

## Chapter 22

### Calibrating Trust

**Trust as a calibration problem**

The wrong response to AI's failure modes is distrust of everything AI produces. The right response is calibrated trust: knowing which outputs to use confidently, which to verify before using, and which to treat as starting points only.

Calibration means your level of trust is proportionate to the actual risk profile of the output. A person who trusts everything AI produces equally, the sentence structure and the legal claim alike, will eventually rely on something they should have checked. A person who trusts nothing AI produces is throwing away most of the tool's value for no good reason.

---

**The trust calibration matrix**

Two dimensions determine how much trust is appropriate:

**Stakes**, What happens if this output is wrong?

- High stakes: wrong output causes significant professional, financial, legal, or personal harm
- Medium stakes: wrong output causes embarrassment, rework, or moderate professional consequences
- Low stakes: wrong output is caught before any harm, or the consequences are easily reversible

**Verifiability**, How easily can you check this?

- Easy: you can verify against a source you have access to in minutes
- Moderate: verification requires more effort, finding sources, specialist input, research
- Hard: verification requires expertise or information you don't have easy access to

Use these two dimensions to calibrate your verification investment:

| Stakes \ Verifiability | Easy to verify | Moderate | Hard to verify |
|---|---|---|---|
| **High stakes** | Verify and document | Verify carefully, seek expert input | Do not rely on AI alone, use as one input among several |
| **Medium stakes** | Verify key claims | Spot-check critical elements | Flag uncertainty; present as AI-assisted |
| **Low stakes** | Read critically | Use with awareness | Use cautiously; review if consequences grow |

---

**Building a personal trust calibration**

Over time, you will build a sense of where AI performs reliably for your specific use cases and where it consistently needs correction.

This is worth tracking, at least informally. When you notice a consistent failure pattern, AI always overestimates timelines in project plans; AI never quite captures your organisation's formal register; AI gets financial calculations wrong, note it. That pattern becomes a standing verification rule in your practice.

When you notice consistent strengths, AI always produces excellent first-draft email structures; AI is consistently right about the logical order of a presentation; AI's summarisation of meeting notes is almost always accurate, you can extend trust in those areas and invest verification effort where it's most needed.

Calibration is personal and task-specific. It improves with experience.

---

> **REAL-WORLD EXAMPLE**
>
> David has now used AI consistently for six months across his consultancy work. He has noticed:
>
> *Reliable:* Drafting client emails (he rarely changes more than a sentence). Structuring proposals. Summarising meeting notes from his own bullet-point notes (not from transcripts). Producing presentation outlines.
>
> *Needs checking:* Any output that contains specific market data or statistics. Recommendations that require knowing something about a client he may not have fully briefed. Legal or regulatory claims about anything jurisdiction-specific.
>
> *Use as starting point only:* Any financial projections or estimates. Technical specifications for systems he isn't deeply expert in. Anything where the quality of the output depends heavily on current information he hasn't provided.
>
> His verification practice is proportionate: high effort where he knows errors are likely; lighter touch where AI is consistently reliable. He doesn't spend time verifying email structure and doesn't use AI financial projections without checking every number.

---

**Communicating AI-assisted work**

In professional contexts, it is worth having a clear internal policy on how you represent AI-assisted work:

**What to disclose:** When AI has generated factual claims, analysis, or recommendations that appear in work presented to clients, stakeholders, or colleagues, it is good practice to note that AI tools were used in preparation and that claims have been verified. This is both honest and a natural quality signal.

**What you remain responsible for:** AI is a tool. You are accountable for the work. If an AI-generated figure in a report is wrong, "AI produced it" is not a professional defence. Your review process, your verification standard, and your decision to include it are yours.

**The credibility calculation:** In most professional contexts, "I used AI to help draft this and then carefully verified it" is now a normal and credible statement. "I relied on AI without checking" is not. The trust question is whether your process is sound, not whether AI was involved.

---

> **WATCH OUT**
>
> Trust miscalibration can go in both directions. Over-trusting AI produces errors that damage professional credibility. But over-distrusting AI, refusing to use well-verified AI output because it came from AI, is also a miscalibration. It adds unnecessary time and effort and fails to take advantage of a tool that works well in the right context. The goal is accurate calibration, not maximum scepticism.

---

## Chapter 23

### Building Your AI Habits

**Why habits matter more than techniques**

Every technique in this book is available to you from today. The 7 Questions, the Before → Better → Best approach, the critique loop, the verification framework, all of them can be applied immediately.

But techniques that aren't habitual are techniques that get used occasionally, in high-stakes situations, when you remember, and not used the rest of the time. The people who get the most consistent value from AI are not necessarily the most technically sophisticated. They are the people who have built consistent habits that apply the right practices automatically.

This chapter is about building those habits.

---

**The four habits that matter most**

From watching how people build effective AI practices, four habits account for most of the difference between occasional useful results and consistently good output:

**Habit 1, Prepare before you prompt**

The single biggest quality leverage point is the thirty seconds spent applying the 7 Questions before starting a significant AI task. Most people skip this and type whatever is on their mind. Those who make it habitual find that they invest slightly more time upfront and substantially less time in revision.

Make it automatic: for any AI task that involves more than a few minutes of work, run the 7 Questions first. Even quickly. Even imperfectly. The discipline of asking "what am I trying to achieve?" before typing is worth far more than any clever prompt technique.

**Habit 2, Verify before you use**

Establish a consistent minimum verification standard for any output you will use professionally. The specific standard depends on the stakes of your work, but the habit is non-negotiable: before you send, publish, present, or act on significant AI output, you have checked something.

For most professional use, the minimum is: read critically, check any numbers and specific facts, and confirm the output follows the constraints you set. This takes two to five minutes. Make it as automatic as saving a file.

**Habit 3, Build your workspace iteratively**

Your AI workspace is not something you set up once and leave. It improves every time you notice a gap, every time AI gets something wrong that it would have got right with better standing instructions, every time you re-type context you've already established, every time you use a prompt that worked particularly well.

The habit: when something goes wrong that a better workspace would have prevented, fix the workspace. When you write a prompt that works especially well, save it. When you notice you're re-entering the same context repeatedly, persist it. Small iterative improvements to your workspace compound into significant efficiency gains over time.

**Habit 4, Critique before you finish**

Before finalising any significant piece of AI-assisted work, run it through a critique pass. This doesn't need to be formal, it can be as simple as asking AI "what is weak about this?" and reading the response with genuine openness.

People who skip this step send proposals with obvious structural weaknesses, publish articles with underdeveloped arguments, and submit reports with claims that don't hold up. People who make critique a habit catch these things before they matter.

---

**Building habits: the practical approach**

Knowing what the habits are is not the same as having them. Three approaches help:

**Attach habits to existing triggers.**
Link new AI habits to things you already do. Before opening ChatGPT for a task: run the 7 Questions. Before closing a document you've used AI to help produce: run the verification checklist. The existing action becomes the trigger for the new habit.

**Start smaller than feels necessary.**
A habit that takes thirty seconds and is done every time is more valuable than a thorough process that is done occasionally. Begin with the minimum viable version of each habit. Add complexity as it becomes automatic.

**Review periodically.**
Once a month, look at what you're using AI for and ask: is my practice serving me well? What am I getting that's consistently poor quality? What am I spending time verifying that I could build into my workspace? What technique from this book have I not tried yet that might help?

---

**A week in the life of a calibrated AI user**

To make this concrete, here is what a week of integrated AI use looks like for someone with established habits:

*Monday morning:*
Preparing for a client review meeting. Opens the client's Project. Pastes in the latest project data and asks AI for a status summary. Reviews it against his own knowledge, catches one outdated figure. Uses the agenda workflow (W8). Both ready in thirty minutes.

*Tuesday:*
Needs to draft a challenging email to a supplier about a missed deadline. Runs the 7 Questions briefly. Uses W1. Reviews the draft, adjusts the tone. Sends within twenty minutes of starting.

*Wednesday:*
Writing a quarterly business report. Starts with the Information → Structure → Content pattern (Chapter 17). Reviews the structure before drafting. Runs a critique loop on the draft (Chapter 18). Verifies the two financial figures independently. Done in two hours rather than half a day.

*Thursday:*
Reviewing a contract. Uses W22. Checks the flag list AI produces against her solicitor's advice. Updates her standing workspace instructions to include a note about a contract clause type she should always flag.

*Friday:*
Reflecting on the week. One output needed correction, AI got a date wrong. Updates her personal verification checklist to add "verify dates in contract summaries." Small improvement. Compounds over time.

---

> **PRO TIP**
>
> The most powerful single thing you can do this week: set up your persistent instructions if you haven't already. Spend thirty minutes writing a context document that covers your professional context, communication preferences, standard audience, and key constraints. Paste it into every AI session this week and notice how much setup time you save. Then move it into your platform's persistent instructions setting so it applies automatically.

---

**What good AI use does not look like**

It is worth being explicit about the patterns that look like productive AI use but aren't:

**Prompt collecting without application.** Building a library of prompts from the internet and using them once before returning to the same vague requests as before.

**Volume without quality.** Generating large quantities of AI output and editing it all manually because it's not quite right, faster to produce, slower overall because verification and correction eat the time savings.

**Outsourcing judgment.** Using AI to make decisions that require accountability. AI can inform decisions; it cannot make them on your behalf.

**Ignoring failure patterns.** Noticing that AI consistently gets something wrong and continuing to rely on it in that area without verification or adjustment.

**Treating the first draft as final.** The first AI output on a complex task is almost never the best it can be. One iteration, a critique loop, a refinement pass, a targeted revision, consistently improves it.

---

## Chapter 24

### Keeping Up Without Burning Out

**The pace problem**

AI capabilities are changing faster than most professional skills do. A technique that works well today may be less useful in six months because the models have improved and no longer need that scaffolding. A feature you relied on may be removed, replaced, or significantly altered. New capabilities that genuinely change what's possible appear with some regularity.

This pace is genuinely exhausting if you try to follow all of it. It is also largely unnecessary.

---

**What actually changes and what doesn't**

The most important distinction for anyone trying to keep up: some things change rapidly, and some things don't.

**Things that change rapidly:**
- Specific model capabilities (what a given version of ChatGPT, Claude, or Gemini can do)
- Platform features (what tools are available in which product at which price point)
- UI and interface details (where to find which setting)
- Best-in-class techniques for specific edge cases
- Pricing and availability

**Things that change slowly or not at all:**
- The principles of good interaction design (context, instructions, examples, output specs)
- The 7 Questions framework, these questions are derived from human communication theory, not from AI quirks
- The verification mindset
- The workflow thinking
- The habit of preparing before prompting

The core framework in this book, the 7 Questions, the AI Interaction Stack, the verification habits, the workflow patterns, is designed to be durable. These are not tricks that work today because of a specific model behaviour. They are principles that reflect what it means to communicate a task clearly to a capable but uninformed agent. That doesn't change when the models improve.

What you need to update is the feature-level detail: which capabilities exist, what the product notes say, where volatile information lives. That is why this book puts product-specific detail in Appendix E rather than in the main text.

---

**A sustainable information diet**

You do not need to read every AI newsletter. You do not need to watch every YouTube tutorial about the latest model release. A sustainable information diet for a professional AI user has three elements:

**1. A quarterly check-in on major developments.**
Once a quarter, spend an hour reading about what has changed. Look for: new capabilities that might affect your use cases, changes to platforms you rely on, anything that suggests a technique you use needs updating. This is sufficient for most professional users.

**2. Platform-specific notifications for things you rely on.**
If you use a specific AI tool for important work, follow that tool's official announcements. When it announces significant changes, read them. This catches the changes that affect your specific workflow.

**3. Practical experimentation over passive consumption.**
The most efficient way to learn about AI improvements is to use them, not to read about them. When a new capability is announced that seems relevant to your work, try it on an actual task. Fifteen minutes of practical use teaches you more than an hour of reading reviews.

What to largely ignore: hype cycles, "the new model is 1000% better" content, and AI influencer output that is primarily optimised for engagement rather than practical value.

---

**When to update your practice**

You need to update your practice when:

- A tool you rely on has changed significantly (feature removed, new capability worth using)
- You encounter a consistent failure mode that a new technique might address
- Your work situation has changed and your AI use should reflect that
- Something in your workspace is producing consistently poor output

You do not need to update your practice because:

- A new model was released
- Someone on the internet claims a new technique is revolutionary
- Your colleague uses AI differently than you

---

**The trajectory of a skilled AI user**

The early period of AI use is typically characterised by inconsistency: some interactions work well, most don't, and the reasons feel opaque. This book is intended to take you out of that phase.

The middle period, where good habits are established and the core framework is internalised, is where most of the professional value lives. Consistent results, predictable quality, reliable verification. This is not exciting. It is useful.

The advanced period involves increasing sophistication in workflow design, more precise calibration of trust, and the ability to identify the right tool and technique for novel situations without referring back to a guide. It comes with accumulated practice, not with reading more AI content.

The trajectory is this: from opaque and inconsistent to systematic and reliable, then from reliable to sophisticated. Part I and Part II get you to systematic. Part III and Part IV get you to reliable. The habits in Part VI get you to sophisticated over time.

---

> **WHY IT WORKS**
>
> The people who develop the best AI practices are not the ones who read the most about AI. They are the ones who use it most consistently, reflect on what works, and gradually refine their approach. The 7 Questions and the verification habits give you a framework to do that reflection productively, so that each iteration of your practice is an improvement on the last.

---

**A final word**

Learning to use AI well is a practical craft: techniques can be taught, but judgment develops through practice and reflection.

You now have the framework, the techniques, and the workflows. The rest is practice.

Apply the 7 Questions. Build your workspace. Design workflows that match your work. Verify before you trust. Iterate until it's right. Reflect on what worked. Update what didn't.

And, in time, it becomes less like following a framework and more like simply knowing how to work.

---

# APPENDICES

---

## Appendix A

### The 7 Questions, Quick Reference Card

*Print this. Photograph it. Keep it visible until the questions become automatic.*

**Before every significant AI interaction**

1. **What am I trying to achieve?**, State the real goal, not just the surface task.
2. **What does AI need to know?**, Add the background, audience, constraints, and relationships that matter.
3. **What information can I provide?**, Attach or paste documents, data, examples, and previous work.
4. **What exactly should AI do?**, Use a clear action verb and define the scope.
5. **What should the result look like?**, Specify format, length, tone, structure, and audience.
6. **How will I check it?**, Identify the facts, numbers, assumptions, and reasoning that need review.
7. **What should happen next?**, Decide whether this is the final result or the input to another stage.

**The Interaction Stack, compressed**

Intent · Context · Instructions · Examples · Source material · Workspace · Tools · Workflow · Output · Verification · Iteration

**Before you trust the output**

Factual or creative? Contains numbers? Citations present? Sources real? Could the information have changed? Did AI make an assumption? Were the constraints followed? Does the conclusion follow from the evidence?

The full explanations appear in Chapters 2, 3, and 20. This page is designed as a quick reference, not as a replacement for those chapters.

---

## Appendix B

### The Before → Better → Best Worksheet

*Use this when you want to systematically improve a prompt. Work through the questions before redrafting.*

---

**YOUR CURRENT PROMPT**

Write out your current prompt exactly as you usually send it:

```
[Your current prompt here]
```

---

**STAGE 1, DIAGNOSE THE GAPS**

Answer these questions about your current prompt:

**Job clarity**
What specific action have you asked AI to take?
If the answer is vague ("help me," "work on," "assist with"), rewrite with a clear verb and scope.

**Context provided**
What background have you given AI that it couldn't know on its own?
What is the most important thing AI doesn't know that would change its answer?

**Information provided**
What documents, data, or examples have you attached or pasted?
Is there source material that would make the output more accurate or specific?

**Output specified**
Have you specified: format, length, tone, audience?
If any of these are unspecified, what is AI likely to default to, and is that what you want?

**Verification planned**
What specifically might be wrong in the output?
How will you check it?

---

**STAGE 2, BUILD THE BETTER VERSION**

Using your diagnosis, write the improved prompt:

```
ROLE (if relevant):
You are a [role] with expertise in [domain].

CONTEXT:
[Background information, situation, history, constraints, relationships]

TASK:
[Specific action verb] [specific deliverable] for [purpose].

SOURCE MATERIAL:
[Attached: / Using: / Based on:]

OUTPUT REQUIREMENTS:
Format: [prose / bullet points / table / structured document]
Length: [word count / page count / number of points]
Tone: [formal / professional-informal / conversational]
Audience: [who this is for and what they know]

CONSTRAINTS:
Do not: [explicit exclusions]
Must include: [required elements]

VERIFICATION REQUEST:
Please flag any claims you are uncertain about and any
assumptions you have made.
```

---

**STAGE 3, THE BEST VERSION**

After receiving output from the Better version:

**What worked well?**

**What still needs improvement?**

**What follow-up instruction would make it right?**

**What should I add to my standing workspace to avoid this gap next time?**

---

**EXAMPLE: BEFORE → BETTER → BEST**

| Stage | Prompt | What changed |
|---|---|---|
| Before | "Help me with a presentation for our board." | Vague task, no context, no output specs |
| Better | "Create a presentation outline for our Q3 board update covering financial performance, key decisions, and outlook." | Specific task, content defined |
| Best | "You are preparing a board presentation for [Company]. Audience: eight non-executive directors, one of whom is new. Format: twelve slides maximum. Content: Q3 financial performance (headline numbers I'll provide), two strategic decisions made this quarter, and a twelve-month outlook. Tone: direct and professional. Lead with the most important finding, not with agenda. Do not include operational detail, board level only. Flag any section where you've made assumptions about emphasis that I should review." | Role, specific deliverable, audience, slide count, content list, tone, structural requirement, exclusion, verification request |

---

## Appendix C

### Verification Checklist

*A single-page reference for use before relying on significant AI output.*

---

**THE EIGHT-QUESTION VERIFICATION CHECKLIST**

Work through these before sending, publishing, presenting, or acting on any significant AI output.

---

☐ **1. Factual or creative?**
Identify which type of output this is. Factual claims require source verification. Creative output (structure, framing, style) can be assessed on its own merits.

---

☐ **2. Numbers present?**
Identify every specific number, percentage, statistic, or calculation in the output.
For each one: can you find it in a source you can point to?
If no: do not use it until you can.

---

☐ **3. Citations present?**
If AI has cited sources, references, or research:
For each one: does the source exist? Does it actually say what AI claims?
Search for the source independently. Do not assume.

---

☐ **4. Sources real?**
Beyond checking that sources exist: does the source's content actually support the claim AI has attributed to it? A real paper may be misquoted or misapplied.

---

☐ **5. Could this have changed?**
For any claim about current facts, who holds a role, what a product costs, what a regulation says, what an organisation does, is this current? AI knowledge has a cutoff. For fast-moving topics, verify from official current sources.

---

☐ **6. Assumptions made?**
Ask AI directly: "What assumptions did you make in producing this output?" Review the assumptions. Are they correct? Are there important exceptions in your situation?

---

☐ **7. Constraints followed?**
Check each instruction you gave against the output. Were all followed? Is anything missing that you required? Is anything present that you excluded?

---

☐ **8. Reasoning sound?**
For analytical outputs: does the conclusion actually follow from the evidence? Could the same evidence support a different conclusion? What would have to be true for the conclusion to be wrong?

---

**RISK-CALIBRATED VERIFICATION GUIDE**

| Output type | Priority checks |
|---|---|
| Report with statistics | 2 (numbers), 5 (currency), 8 (reasoning) |
| Academic or research content | 2, 3 (citations), 4 (sources), 8 |
| Legal or regulatory content | 5 (currency), 6 (assumptions), 8 |
| Medical information | 5, 6, 8, plus qualified professional review |
| Client-facing communications | 6 (assumptions), 7 (constraints), 8 |
| Internal communications | 7 (constraints), light check on others |
| Creative/editorial content | Read critically; 7 (constraints) |

---

**WHEN YOU FIND AN ERROR**

1. Correct the specific error
2. Ask whether the error is isolated or a signal of a broader problem with this output
3. Consider whether your workflow should have caught this earlier
4. Update your standing verification rules if this is a pattern

---

## Appendix D

### AI Use Cases by Profession

*A practical starting point for common professional contexts. Use this to identify which workflows and techniques are most relevant to your work, and to think about what your workspace should contain.*

*This is a starting point, not an exhaustive list. Your specific situation will always have uses and constraints not captured here.*

---

### Marketing and Communications

**Most valuable use cases:**
- Drafting and editing client communications, campaigns, and copy (W1, W9, W10, W11, W12)
- Research and briefing preparation for campaigns (W3, W13)
- Repurposing content across channels (W11)
- Preparing for client presentations (W3, W7)
- Producing first drafts from briefs (W25)

**Key workspace elements:**
- Brand guidelines document (uploaded to each client project)
- Tone-of-voice reference (example copy that captures the right register)
- Target audience profiles
- Standard exclusions per client (regulatory constraints, competitor references, etc.)

**Where to be most careful:**
Statistics and market claims in copy, these are high-visibility and often checked by clients or regulators. Verify every specific figure before it goes into client-facing material.

---

### Small Business Owners and Entrepreneurs

**Most valuable use cases:**
- Client proposals and pitches (W5)
- Client and supplier communications (W1, W2)
- Summarising information for decisions (W4, W15)
- Business planning and project management (W17)
- Marketing content (W9, W10, W12)

**Key workspace elements:**
- Company background and positioning statement
- Target customer description
- Standard terms and constraints
- Tone guide (how the business communicates)
- Any regulatory constraints on the business

**Where to be most careful:**
Legal and financial claims in business documents, and any content that will be seen by clients before internal review.

---

### HR and People Professionals

**Most valuable use cases:**
- Job descriptions and postings (W6)
- Employee communications
- Policy and process documentation
- Meeting notes and follow-ups (W8)
- Difficult conversation preparation (W2)

**Key workspace elements:**
- Organisation name and structure
- HR policy documents (relevant sections uploaded for reference)
- Employment law jurisdiction
- Standard communication tone
- Constraints (legal language to avoid in employee communications, etc.)

**Where to be most careful:**
Employment law and HR policy claims are jurisdiction-specific and change regularly. Never rely on AI for specific legal positions without verification from qualified legal sources and your current policy documents.

---

### Legal Professionals

**Most valuable use cases:**
- Document summarisation and review (W4, W14)
- Research preparation and briefing (W3, W13)
- Drafting non-legal client communications (W1)
- Meeting preparation (W3, W8)
- Summarising case materials for internal briefing

**Key workspace elements:**
- Jurisdiction and area of practice
- Firm style and communication standards
- Standard disclaimers and qualification language
- What AI output is and is not used for (internal note: AI is a drafting aid; all legal content is reviewed by qualified solicitors)

**Where to be most careful:**
AI should not be used to generate legal advice or opinions without qualified review. Legal knowledge changes; AI may state outdated positions confidently. AI summaries of contracts and legal documents should always be checked against the original for anything that matters.

---

### Finance and Accounting Professionals

**Most valuable use cases:**
- Summarising reports and financial documents (W4)
- Client communication drafts (W1, W7)
- Research preparation (W3, W13)
- Project and planning support (W17)
- Preparing for meetings (W3, W8)

**Key workspace elements:**
- Regulatory jurisdiction and relevant standards
- Client confidentiality constraints
- Appropriate disclaimer language for client-facing communications
- Technical terminology explanations for non-specialist communications

**Where to be most careful:**
All financial figures in AI output must be verified against source data. AI arithmetic is unreliable without code execution. Any regulatory or tax claim must be verified against current HMRC/relevant authority guidance. Never include AI-generated financial projections in client work without independent verification.

---

### Teachers and Education Professionals

**Most valuable use cases:**
- Lesson planning and resource development (W16, W25)
- Differentiated materials for different ability levels
- Parent communications (W1)
- Research and preparation for topics (W13)
- Assessment question development

**Key workspace elements:**
- Year group / age range and subject
- Curriculum framework (e.g. National Curriculum in England)
- School's communication style and tone
- Any relevant pastoral or safeguarding context that affects communications

**Where to be most careful:**
Curriculum-specific content should be verified against current specifications. Content for student consumption should be reviewed by a teacher before use. Subject matter accuracy should be verified, especially in science, history, and other factually complex areas.

---

### Researchers and Academics

**Most valuable use cases:**
- Literature orientation for new topics (W13)
- Summarising papers and documents (W4, W14)
- Structuring arguments and papers (W17, W25)
- Editing and improving prose (W24)
- Preparing for seminars and presentations (W3)

**Key workspace elements:**
- Field and sub-discipline
- Preferred citation style
- Institutional guidelines on AI use (these vary significantly; check your institution's current policy)
- Level of technical language appropriate for target publication

**Where to be most careful:**
All citations must be verified independently, AI hallucination of academic references is well-documented. AI summaries of research papers may miss important methodological nuance. AI should not be used to generate empirical claims or research findings. Follow your institution's and target journal's guidelines on AI disclosure.

---

### General Professionals (Broad Business Contexts)

**Most valuable starting workflows:**
- W1 (Professional email), universally applicable
- W3 (Meeting preparation), very high return
- W4 (Summarising documents), immediate time saving
- W8 (Meeting agenda and follow-up), immediately practical
- W15 (Building a workspace), the highest long-term leverage point

**Minimum viable workspace:**
- Your role and organisation type (two sentences)
- Your standard communication tone
- UK/US English preference
- Things AI should never include in your output (jargon, specific competitors, etc.)
- Default verification instruction ("please flag any claims I should verify independently")

---

## Appendix E

### Product Notes, Platform-Specific Information

*This appendix contains product-specific information that is subject to change. All entries are verified as of September 2026. Volatility ratings indicate how likely information is to have changed since verification.*

*Before relying on any of this information for a workflow or decision, check the platform's current documentation. AI product features, pricing, and availability change frequently and sometimes without announcement.*

---

**HOW TO CHECK CURRENT INFORMATION**

For each major platform:
- **ChatGPT:** help.openai.com
- **Claude:** support.anthropic.com and docs.anthropic.com
- **Gemini:** support.google.com/gemini
- **Microsoft Copilot:** support.microsoft.com

For pricing specifically, always check the platform's pricing page directly. Prices listed by third parties (including this book) become outdated.

Useful official starting points:
- ChatGPT Projects: https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- ChatGPT Custom Instructions: https://help.openai.com/en/articles/8096356-chat-preferences-for-chatgpt
- ChatGPT GPTs: https://help.openai.com/en/articles/8798878-building-and-publishing-a-gpt
- Claude Projects and personalisation: https://support.anthropic.com/en/articles/9519177-how-can-i-create-and-manage-projects
- Gemini Deep Research: https://support.google.com/gemini/answer/15719111

---

### E1, ChatGPT (OpenAI)

**Plans available (September 2026):** Free, Plus, Pro, Team, Enterprise

**Projects feature:**
Available on free and paid plans. Projects group conversations, project instructions, and reference files; memory settings and file limits vary by plan and workspace. Check current documentation for the limits that apply to your account.
*Volatility: MEDIUM*

**Memory feature:**
Saved memory and project memory can carry selected context across conversations, but availability, settings, and behaviour vary by plan, workspace, and region. Treat memory as a convenience, not as complete or infallible recall.
*Volatility: MEDIUM*

**Web search:**
Available across plans (with limitations on Free). Search quality varies; results should be treated as a starting point for verification, not a verified source.
*Volatility: MEDIUM*

**Code execution (Advanced Data Analysis):**
Some ChatGPT plans and tools support code execution, file analysis, and chart generation. Availability and limits vary. Most reliable arithmetic is obtained when the calculation is actually executed and the inputs and formula are checked.
*Volatility: LOW*

**Custom instructions (persistent instructions):**
Available across ChatGPT plans, with limits and interface details varying by plan and platform. They apply broadly, while project instructions are scoped to a particular project and may take precedence within it.
*Volatility: LOW*

**GPTs:**
You can use existing GPTs where your account and workspace permit it. Creating or publishing a new GPT is subject to current account, plan, workspace, and eligibility rules; personal ChatGPT accounts may not be able to create or publish new GPTs. Check OpenAI's current GPT documentation before promising this capability to every reader.
*Volatility: HIGH*

**Image generation (ChatGPT Images):**
Integrated into ChatGPT, with capabilities and access changing over time. Commercial use is subject to OpenAI's current terms and applicable law, verify both before using generated images in commercial projects.
*Volatility: HIGH, terms and capabilities change*

**File upload:**
PDF, Word, Excel, images and other formats. Size and count limits apply, check current documentation.
*Volatility: MEDIUM*

---

### E2, Claude (Anthropic)

**Plans available (September 2026):** Free, Pro, Team, Enterprise

**Projects feature:**
Available on Pro and above. Similar to ChatGPT Projects, groups conversations, maintains uploaded documents, supports project-level instructions. One of the more mature implementations of this feature.
*Volatility: MEDIUM*

**System prompts / persistent instructions:**
Available via Projects and via platform settings. Robust and reliable as of verification date.
*Volatility: LOW*

**Web search:**
Available on Pro and above, via tool integration. As with all AI web search: verify important findings from primary sources.
*Volatility: MEDIUM*

**File upload:**
PDFs, Word documents, images, and other formats supported. Claude has historically handled long documents well, but verify large document behaviour from current documentation.
*Volatility: MEDIUM*

**Memory:**
Claude provides several forms of persistence and personalisation, including profile preferences, project instructions, project knowledge, andwhere enabledsearch across previous chats. These mechanisms differ from one another and do not guarantee complete recall across conversations. Check current availability and settings in Claude's documentation.
*Volatility: HIGH*

**Extended context window:**
Claude models have historically supported long context windows, enabling analysis of very long documents. Specific limits depend on the current model version.
*Volatility: MEDIUM*

---

### E3, Gemini (Google)

**Plans available (September 2026):** Gemini (free), Gemini Advanced (paid subscription), Gemini for Workspace (business integration)

**Google Workspace integration:**
Gemini integrates with Google Docs, Gmail, Drive, Sheets, and Slides for users with Workspace accounts. For professionals already using Google Workspace, this integration is significant for productivity. Depth and reliability of integration varies by product.
*Volatility: HIGH, integration features are actively expanding*

**Web search:**
Gemini has native Google Search integration, which is a meaningful advantage for tasks requiring current information. Search quality is generally strong; verify important claims as normal.
*Volatility: LOW (integration is core to the product)*

**Gems (custom AI configurations):**
Gemini offers custom configurations called Gems. Creation, file support, and availability vary by account, plan, region, and product version; check the current Gemini help centre before relying on a specific capability.
*Volatility: MEDIUM*

**File upload:**
Images, PDFs, and other formats supported. Google Workspace document integration provides additional access to Drive files.
*Volatility: MEDIUM*

---

### E4, Microsoft Copilot

**Plans available (September 2026):** Copilot (free, integrated into Windows and Edge), Copilot Pro (paid), Microsoft 365 Copilot (business, requires M365 subscription)

**Primary use case:**
Copilot's primary value for professional users is its integration with Microsoft 365 applications, Word, Excel, Outlook, Teams, PowerPoint. For organisations running M365, this integration can be significant.

**Microsoft 365 Copilot:**
If your organisation has deployed M365 Copilot, AI assistance is available within the applications you already use. Capabilities include: summarising emails and meetings, drafting documents within Word, analysing data in Excel, generating presentations in PowerPoint.
*Volatility: HIGH, M365 Copilot is rapidly evolving*

**Data security:**
For organisations using M365 Copilot under an enterprise agreement, data handling follows Microsoft's enterprise data protection terms. This is significant for regulated industries. Verify current terms with your IT and legal teams.
*Volatility: MEDIUM*

---

### E5, Cross-Platform Notes

**Choosing a primary platform:**
For most professional users, the choice of primary AI platform should be based on: integration with your existing tools (if you use Google Workspace, Gemini's integration is worth considering; if you use M365, Copilot may be relevant); the specific capabilities you need most (long document analysis, code execution, image generation); and the plan that provides the right features for your use.

**Using multiple platforms:**
Many users find it practical to use more than one platform. A common pattern: one platform as the primary for ongoing projects (with workspace set up), a second for specific tasks it handles better (e.g., using web-search-heavy research tasks with a strong search-integrated tool).

**Privacy and data:**
All major AI platforms have privacy policies governing how they use your inputs. Key questions to check in current documentation:
- Is your data used to train models?
- What is the opt-out process?
- For enterprise accounts: what are the data retention and usage terms?

For professional use involving client data, sensitive business information, or personally identifiable information, review the platform's current privacy and data terms before processing that information.

*Volatility: HIGH, policies change; verify before processing sensitive data*

---

### E6, Image Generation (All Platforms)

**Current state (September 2026):**
Image generation is integrated into ChatGPT through its current image-generation experience and is available through several other platforms. Product names, models, access, and quality change frequently.

**Commercial use:**
Before using AI-generated images in commercial contexts (client work, marketing, publications), verify the current terms of service of the specific platform. Terms for commercial use vary and have changed multiple times. Verify before use.

**Copyright considerations:**
The legal status of AI-generated images for commercial use is an evolving area in multiple jurisdictions. Current legal guidance in the UK and elsewhere is subject to ongoing development. Check current legal guidance before relying on AI-generated images in commercial contexts.

*Volatility: VERY HIGH, both platform terms and legal frameworks are actively changing*

---

*Appendix E was verified in September 2026. Product features, pricing, availability, and terms change frequently. Always verify from the platform's own current documentation before relying on specific features or capabilities for professional use.*

---

## A Note on Sources

*This book does not use footnotes in the main text, because most of the principles it describes are based on documented patterns of AI behaviour rather than a single research paper or study. The following notes point to the most useful reference points for readers who want to go further.*

**On AI failure modes and hallucination:**
The phenomenon of AI hallucination is well-documented in academic literature. A practical starting point is work published by researchers at major AI labs themselves, Anthropic, OpenAI, and Google DeepMind all publish research findings on model behaviour that is accessible to non-specialists on their respective research websites.

**On prompt engineering:**
The field has produced several peer-reviewed studies on what makes prompts effective. The most reliable summary of current understanding remains the documentation produced by each AI lab, particularly Anthropic's documentation on working with Claude and OpenAI's guidance on ChatGPT. These are updated more frequently than academic publications.

**On verification practices:**
Standards for AI output verification in professional contexts are still emerging. In the UK, professional bodies in law, accounting, and medicine have begun to publish guidance, check your relevant professional body's current guidance.

**On platform features:**
All platform-specific information should be verified from the platform's own documentation. The most current information is always on the platform's help centre, not in any third-party publication.

---

## About the Author

<!-- ============================================================
PRODUCTION NOTE, PHOTO PLACEMENT
Insert a professional author headshot here.
Dimensions: 1:1 square crop, minimum 300 dpi for print.
Alignment: centred, or floated left with text wrapping right,
depending on interior layout template.
File reference: eleanor-mercer-author-photo.jpg
See photo brief in the Author File for full specification.
============================================================ -->

![Eleanor Mercer](../../attached_assets/eleanor-mercer-author-photo.png)

Eleanor Mercer is a professional development trainer and consultant who has worked with professionals across law, financial services, and management consulting for fifteen years. Her original practice focused on communication, writing, and presentation, the skills that separate people who can do excellent work from people who can also explain it clearly.

When AI tools entered professional workplaces in 2022, she began testing them, helping clients use them, and watching closely what happened when capable professionals sat down with capable technology and still got mediocre results.

The pattern was consistent: the gap was almost never technical. It was what people gave AI before they started, the context, the instructions, the job description, the source material, and the verification process.

The 7 Questions framework and the AI Interaction Stack in this book were developed through that observation, tested in professional training practice, and refined over two years of real use before appearing in print.

*The Art of AI* is the first book in a planned series on professional AI skills for non-technical users. Eleanor writes, trains, and publishes through The Art of AI.

**theartofai.com**

---

## About This Book

*The Art of AI, Book 1, is the first in a planned series covering practical AI skills for non-technical professionals. Future books in the series will cover AI for specific professional contexts, advanced workflow design, and team-level AI integration.*

---

*AI tools were used in the research, drafting, and editing of this book. All factual claims were verified against primary sources at the time of writing. All examples were tested. All editorial decisions, structure, voice, inclusion, emphasis, are the author's own.*

*Published 2026. First edition.*

---
