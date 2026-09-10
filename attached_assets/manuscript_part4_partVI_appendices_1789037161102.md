# PART VI

## The AI User's Playbook

*Part V gave you twenty-five workflows to use. Part VI gives you the habits that make them reliable.*

*This is the part most books skip. They teach you how to get output. They don't teach you what to do with it — how to check it, what to watch for, how much to trust it, and how to build the kind of AI practice that compounds in value over time rather than staying hit-or-miss.*

*That's what the next five chapters cover.*

---

## Chapter 20

### How to Verify AI Output

**The problem with confident prose**

AI writes well. This is, in a specific sense, a problem.

When a source is hesitant, poorly worded, or obviously uncertain, you naturally approach it with scepticism. When a source is fluent, structured, and confident, you're inclined to trust it. This is a reasonable heuristic for human writing. It is a poor heuristic for AI.

AI produces confident prose regardless of whether the underlying content is correct. It does not get uncertain when it reaches the edge of its knowledge. It does not hedge more on the questions it genuinely doesn't know the answer to. It hedges when you ask it to hedge. Without that instruction, it states.

This is not a bug that will be fixed in the next model release. It is structural. Understanding it changes how you use AI — from reading AI output as you would read a newspaper article, to reading it the way you'd read a first draft from a capable but occasionally unreliable colleague.

That change in posture — from consumer to editor — is the foundation of everything in this chapter.

---

**What verification is not**

Verification does not mean checking every sentence of every AI output before you use it.

That would be more work than doing the task yourself, which defeats the purpose.

Verification is proportionate. It is targeted. It is a set of quick, learnable habits that catch the errors that matter — the ones that would embarrass you, cost you money, damage a relationship, or lead to a bad decision — before they do.

The goal is not perfect scepticism. The goal is calibrated trust.

---

**The two categories of AI error**

AI errors fall into two broad categories, and they require different responses.

**Category 1 — Errors of fact**
AI states something that is not true. A date is wrong. A statistic is invented. A product no longer exists. A law changed. A person's title is incorrect. A quote is misattributed.

These errors can look indistinguishable from correct information. They are checked by going to primary sources.

**Category 2 — Errors of reasoning or fit**
AI's information may be correct, but its analysis, recommendation, or application to your specific situation is wrong. It has misunderstood the task. It has applied a general principle incorrectly. It has drawn a conclusion that doesn't follow from the evidence.

These errors are checked by your own judgment. Does this actually make sense? Does this conclusion follow from what the AI has laid out? Does this recommendation fit my actual situation?

Both categories require different verification techniques.

---

**The Before You Trust checklist**

For any output that matters — that you will act on, share, or use in a significant decision — run through these eight questions:

> **VERIFY — Before You Trust the Answer**
>
> 1. **Is this factual or creative?**
> If the task was creative (write a story, draft an email, generate ideas), most of this checklist doesn't apply. If the task required facts, it does.
>
> 2. **Does it contain numbers?**
> Statistics, percentages, counts, dates, prices, and measurements are the most common location of confident errors. Treat any number that matters as unverified until you check it.
>
> 3. **Does it cite sources?**
> AI may produce citations that look real and are not. A convincing title, a plausible author, a credible journal — all fabricated. Do not assume a citation is real because it looks professional.
>
> 4. **Are the sources real?**
> If sources are cited: search for them. The combination of author, title, and year should return the actual source. If you can't find it, it may not exist.
>
> 5. **Could the information have changed?**
> Regulations, product features, prices, personnel, company structures, research findings — these change. AI's knowledge has a cutoff date and may lag even before that. For fast-moving topics, verify from a current source.
>
> 6. **Did AI make an assumption?**
> AI fills gaps with reasonable-sounding assumptions. If you didn't specify something, check what AI assumed. Ask: "What assumptions did you make to answer this?"
>
> 7. **Did it follow my constraints?**
> Read the output against your original instructions. Length, format, tone, what to include, what to exclude. AI occasionally drops constraints, particularly in longer outputs or when the constraints conflict.
>
> 8. **What evidence supports the conclusion?**
> If AI has reached a conclusion or recommendation, ask: where does that follow from? Is the reasoning shown? Would a different set of assumptions lead to a different conclusion?

---

**Verification by task type**

Not every task carries the same risk profile. Here is a practical guide:

| Task type | Main risk | Verification approach |
|---|---|---|
| Factual research | Invented facts, outdated information | Cross-reference key claims with primary sources |
| Summarisation | Omissions, misemphasis | Check summary against original document |
| Document analysis (contract, legal) | Misreading, oversimplification | Read original before acting; professional advice for high stakes |
| Medical information | Incomplete, not personalised, outdated | Treat as background only; discuss with healthcare professional |
| Financial information | Not personalised, not current, not regulated | Supplement with regulated advice for significant decisions |
| Data analysis | Wrong calculations, misinterpretation of the task | Check key figures; test with simple examples |
| Writing (emails, reports, proposals) | Tone wrong, commitment made you didn't intend, assumption not correct | Read carefully before sending; check facts in the text |
| Creative tasks | Lower verification burden, but check for unintended content |  Read for anything that lands differently than intended |

---

**The one-verification-step discipline**

For most everyday AI use, the full checklist is unnecessary. But one verification habit that protects you in almost every scenario: **read the output as if you wrote it and are responsible for it**.

Not as someone reviewing AI. As someone who owns what it says.

This shift in perspective catches a surprising proportion of errors. The email AI drafted that makes a commitment you didn't authorise. The summary that emphasises the wrong point. The report section that draws a conclusion you didn't ask for. The sentence that could be read in a way you didn't intend.

Reading your own name on something changes how carefully you read it.

---

> **REAL-WORLD EXAMPLE**
>
> Marcus is a financial analyst using AI to prepare a briefing on an emerging market for a client presentation. AI produces a thorough, well-structured overview with economic figures, market size estimates, and growth projections — all cited to what appear to be reputable sources.
>
> Marcus runs the Before You Trust checklist. The prose sounds authoritative. The structure is good. But the checklist surfaces three issues:
>
> — Two statistics come from sources he can't locate when he searches. He flags these.
> — One growth projection is clearly based on a report from 2023. He checks whether a more recent estimate exists. It does, and the figures have changed significantly.
> — The conclusion recommends market entry, but re-reading the criteria Marcus specified reveals that AI overlooked the regulatory constraint he mentioned in Step 1. The conclusion doesn't fit the brief.
>
> Marcus catches all three issues before the presentation. The AI briefing is 80% of the way there — useful, structured, and a significant time saving. But the 20% that needed human judgment could have caused real damage if it had gone unchecked.

---

> **WATCH OUT**
>
> The more impressive the output looks, the easier it is to skip verification. This is backwards. A beautifully formatted, confident, comprehensive AI response is exactly the situation that calls for checking — because the polish can mask errors that would have been obvious in a rougher draft.

---

**When to ask AI to verify itself**

AI cannot reliably verify its own factual claims — it has no external access to confirm whether something is true. But it can be a useful diagnostic tool:

```
Review what you just told me.

What are you most confident about in this response?
What are you least confident about?
Are there any areas where you might be working from incomplete or outdated information?
What would I need to check before acting on this?
```

This does not produce perfect self-criticism. But it often surfaces genuine uncertainties that were not flagged in the original response — and it tells you where to focus your independent verification.

---

> **PRO TIP**
>
> Build a personal "high-stakes list" — the specific types of output you will always verify before using. For most professionals, this includes: statistics and figures you will quote, legal and regulatory statements, financial projections, and any claim that will go in front of a client, employer, or decision-maker. Knowing your own list in advance means you verify consistently, not only when something happens to feel uncertain.

---

## Chapter 21

### What AI Gets Wrong (Consistently)

**The honest chapter**

Every book that teaches you how to use AI better should also tell you, plainly, what AI is not good at. This is that chapter.

These are not edge cases or obscure failure modes. They are patterns — things that happen often enough that a thoughtful AI user learns to anticipate them. Knowing them in advance doesn't mean avoiding AI for these tasks. It means approaching them differently: with more careful setup, more targeted verification, and a clear understanding of where the human judgment needs to be applied.

---

**Failure 1 — It invents facts with full confidence**

This is the most important failure mode to understand, and the one that has caused the most damage to AI's reputation in serious use.

AI is trained to produce plausible, coherent text. When asked for a fact it doesn't have, it does not always say "I don't know." It often produces a fact-shaped sentence — a number, a name, a date, a citation — that fits the context and sounds correct.

These invented facts are sometimes called "hallucinations" — a term that is evocative but slightly misleading, because it implies something random and dream-like. In practice, AI's invented facts tend to be plausible in the specific way that makes them hardest to catch: they're in the right ballpark, they fit the pattern, they have the right shape.

A real statistic about a real topic from the right approximate era. A paper that could plausibly exist, by an author who does exist, in a journal that does exist. A court case that didn't happen, but probably should have.

**When to be especially alert:** specific numbers, citations and references, historical details, quotes attributed to real people, claims about specific laws or regulations, product specifications, recent events.

---

**Failure 2 — Its knowledge has a cutoff (and lags before it)**

All AI models have a training cutoff — a date beyond which they have no information. But even before that date, knowledge can be uneven: events from the months immediately before the cutoff may be underrepresented simply because there hadn't been time for them to generate extensive written material.

The practical implication: for fast-moving topics, AI may be out of date even when you think its information should be current.

**When to be especially alert:** anything that changes frequently — regulations, product features, pricing, personnel, company structures, market conditions, medical guidelines, software versions.

The workaround: use AI for context and framework, then verify time-sensitive specifics from current sources.

---

**Failure 3 — It tells you what you want to hear**

AI is trained partly on human feedback, and humans tend to prefer responses that agree with them, confirm their views, and are positive about their ideas. This creates a consistent bias toward validation.

If you present a plan and ask whether it's good, AI will typically find things to praise — even if the plan has significant problems. If you present an argument and ask whether it's convincing, AI will often agree that it is. If you say "I'm thinking about doing X — what do you think?" the response will usually be more supportive than critical.

This is a problem when you need genuine critique. It is especially dangerous when the decision matters.

**How to counteract it:** ask explicitly for criticism, not balance. "What is wrong with this plan?" is better than "What do you think of this plan?" "What would someone argue against this?" is better than "Is this a good argument?" Structuring the prompt to make critique the explicit task breaks the validation bias more reliably than asking for "honest feedback."

---

> **TRY THIS**
>
> Test this yourself. Take something you've decided to do — a business decision, a plan, a piece of writing you're proud of. Ask AI: "What do you think of this?" Note the response. Then ask: "What are the strongest arguments against this?" Compare. The second response will almost always be more useful.

---

**Failure 4 — It loses track in long conversations**

AI's effective attention has limits. In long conversations — particularly those covering multiple topics, with many back-and-forth exchanges, or involving complex instructions given early on — AI can lose track of earlier context.

This manifests as: forgetting a constraint you specified at the start, contradicting something it established earlier, gradually drifting away from the specified format, or simply not carrying an important piece of context into a later response.

**When to be especially alert:** long conversations, complex multi-part tasks, any situation where you specified important constraints or context early and haven't referenced them since.

The workaround: for long or complex work, periodically restate key constraints. For multi-step workflows, include a brief context reminder at the start of each major step. If something important disappears, simply re-establish it.

---

**Failure 5 — It applies general knowledge incorrectly to specific situations**

AI knows a lot about how things work in general. It knows less about your specific situation, your specific industry's norms, your specific organisation's constraints, and the specific context you're operating in.

When AI applies general knowledge to a specific situation, the gap between the general and the specific is where errors live.

The legal principle that applies generally may not apply in your jurisdiction. The marketing approach that works in most industries may not work in yours. The management technique that AI recommends may be appropriate for most workplace cultures but not yours.

**When to be especially alert:** any time AI is making a recommendation or applying a framework to your specific situation, particularly in regulated fields, specialist industries, or contexts with unusual constraints.

The workaround: provide the specific context explicitly. Tell AI what makes your situation different from the general case. Then ask it to apply its knowledge to those specifics — and assess whether the result accounts for them.

---

**Failure 6 — It can't tell you what it doesn't know**

Ask AI a question it can't answer well, and it will usually attempt to answer it anyway. The absence of knowledge is rarely clearly flagged.

You can prompt AI to be more explicit about uncertainty — "Please tell me where you're uncertain about this" or "What are the limits of your knowledge here?" — and this helps. But it doesn't fully solve the problem. AI's metacognition (its ability to know what it doesn't know) is imperfect.

The implication: you cannot rely on AI to raise its own hand when it's out of its depth. You have to build verification habits that don't depend on AI alerting you to problems.

---

**Failure 7 — Maths and calculation**

This has improved significantly with newer models and tool access, but remains worth flagging: AI language models are not calculators, and numerical reasoning — particularly multi-step arithmetic, complex calculations, and data interpretation — can produce errors that are presented with complete confidence.

For simple calculations, AI is generally reliable. For complex ones, use a calculator or spreadsheet and have AI work through the reasoning rather than just produce a number.

**When to be especially alert:** any output where a calculation determines a recommendation, projection, or conclusion. Check the arithmetic independently.

---

> **WHY IT WORKS**
>
> Understanding these failure patterns doesn't make you cynical about AI — it makes you calibrated. A tool used with clear awareness of its failure modes is far more valuable than the same tool used without that awareness. A surgeon who understands exactly what can go wrong in a procedure is more reliable than one who hasn't thought about it, not less. The same logic applies here.

---

**A summary table**

| What AI gets wrong | Why it happens | How to protect yourself |
|---|---|---|
| Inventing facts | Trained to produce plausible text | Verify specific claims from primary sources |
| Outdated information | Knowledge cutoff and lag | Check time-sensitive facts from current sources |
| Telling you what you want to hear | Human feedback bias | Ask explicitly for criticism, not balance |
| Losing track in long conversations | Attention limits | Restate key constraints; use structured workflows |
| Misapplying general knowledge | Can't know your specific situation | Provide specific context; verify recommendations fit your case |
| Not flagging uncertainty | Metacognition limits | Don't rely on AI to signal its own limits |
| Numerical errors | Language models aren't calculators | Verify significant calculations independently |

---

## Chapter 22

### Calibrating Trust

**Trust is not binary**

The question people most often ask about AI reliability is the wrong question. They ask: "Can I trust it?" — expecting a yes or no.

The useful question is: "How much trust is appropriate for this specific type of output, from this specific model, for this specific task?" And the answer varies considerably.

AI is not uniformly reliable or uniformly unreliable. It is excellent in some areas, unreliable in others, and variable in the middle. Calibrated trust — knowing roughly where the edges of reliability are — is one of the most practically valuable skills you can develop as an AI user.

This chapter gives you a framework for developing it.

---

**The three trust zones**

Think of AI output as falling into three broad zones:

**Zone 1 — High reliability (use with normal care)**

Tasks where AI performs consistently well and errors, when they occur, are usually obvious:

- Drafting and editing prose where you provide the substance
- Brainstorming and generating options
- Explaining concepts in plain language
- Summarising content you have provided (with caveats for long documents)
- Formatting and restructuring text
- Generating questions, frameworks, and checklists
- Creative tasks with clear parameters
- Translation (major languages, non-specialist content)

For Zone 1 tasks: read the output, apply your own judgment, send it. Occasional light verification is sufficient.

**Zone 2 — Moderate reliability (verify before acting)**

Tasks where AI is often useful but errors are consequential and not always obvious:

- Research on topics where facts matter and you will use them
- Summarising documents you haven't read yourself
- Analysis and recommendations where the reasoning matters
- Professional writing that will carry your name or organisation's name
- Any output that includes specific numbers, names, dates, or citations

For Zone 2 tasks: run the Before You Trust checklist. Verify key facts. Read carefully before sending or acting.

**Zone 3 — High risk (use as input, not output)**

Tasks where AI can assist but human expertise is essential before acting:

- Legal analysis — use AI to understand the terrain, consult a professional before acting
- Medical information — use AI to prepare questions, speak to a healthcare professional for decisions
- Financial advice — use AI for general orientation, consult a regulated professional for significant decisions
- Regulatory compliance — use AI to identify the relevant framework, verify current requirements from official sources
- Any situation where being wrong has significant professional, financial, legal, or health consequences

For Zone 3 tasks: treat AI output as useful background and a starting point for the right questions. Do not act on it directly for high-stakes decisions.

---

> **WATCH OUT**
>
> Zone 3 doesn't mean "don't use AI here." It means: use AI to be better informed, to ask better questions, and to understand the landscape — then take the decision or action with appropriate professional support. AI can make your conversation with your solicitor, doctor, or financial adviser significantly more productive. It is not a substitute for those conversations.

---

**How to build your personal trust calibration**

Calibration comes from experience — specifically, from noticing when AI is right and when it isn't. This requires a deliberate habit:

1. **When AI gets something wrong, note it.** Not obsessively — just a mental note, or a brief log. What type of task was it? What type of error? This pattern recognition compounds over time.

2. **When AI gets something unexpectedly right, note that too.** Calibration isn't just about catching failures. Understanding where AI reliably exceeds your expectations is equally valuable.

3. **Test AI in areas where you already know the answer.** For any domain where you have expertise, run some test prompts. Where does it perform well? Where does it make errors? This is much more informative than discovering failures in unfamiliar territory where you can't recognise the error.

4. **Ask AI for its confidence.** Not because the self-assessment is perfectly accurate, but because the pattern of what AI claims confidence in versus where it hedges gives you useful signal. A response full of hedges is worth reading differently from one delivered with total certainty.

---

**The model matters (but less than you think)**

Different AI models have different strengths, weaknesses, and reliability profiles. Claude tends toward more careful hedging. GPT models have historically been more prone to confident invention but have improved significantly. Gemini has particular strengths in real-time information access.

These differences are real and worth being aware of. But they're smaller than the effect of how you prompt. A well-structured interaction on a mid-tier model will outperform a poorly structured interaction on the most capable model available. The quality of the interaction setup — clear task, relevant context, explicit constraints, structured verification — matters more than the model choice for most everyday tasks.

The exception: for genuinely difficult analytical tasks, complex reasoning, or work that requires sustained accuracy across a long document, the model choice starts to matter more. Choose accordingly.

---

> **PRO TIP**
>
> Run the same prompt on two different models for any output you'll rely on heavily. Not because you'll always get different answers — often you won't — but because where the models disagree is exactly where you should look most carefully. Disagreement between models is a flag, not a tiebreaker. It means the question deserves more investigation.

---

**The trust-building loop**

Trust, properly calibrated, is not a fixed setting. It develops through a loop:

1. Use AI for a task
2. Verify the output
3. Note where it was right and where it wasn't
4. Adjust your trust calibration for that task type
5. Design your prompts and verification accordingly

This loop, repeated across different task types over time, produces something genuinely useful: a personal model of how AI performs for your specific work. That model — the accumulated experience of knowing where to push hard and where to verify carefully — is one of the most valuable things you can develop as a practitioner.

---

## Chapter 23

### Building Your AI Habits

**The habits gap**

There is a gap between people who use AI occasionally and people who use it well. It is not, primarily, a knowledge gap. Most people who use AI regularly have read the same articles, tried the same features, seen the same demonstrations.

The gap is a habits gap. People who get consistently good results from AI have built small, consistent practices that compound over time. People who get inconsistent results haven't.

This chapter is about the habits that bridge that gap.

---

**The four habits that matter most**

**Habit 1 — Front-load the context**

The most common reason AI produces a mediocre first response is insufficient context. The most common fix — "make it more specific," "add my role," "be less generic" — is a correction to a problem that didn't need to happen.

The habit: before you start typing a prompt, spend thirty seconds asking yourself: what does AI need to know to do this well? Then put that in the prompt.

This is the 7 Questions framework in its most everyday form. You don't need to run all seven questions before every interaction. You do need the instinct — pausing before you prompt to ask: have I given AI what it needs?

This habit alone, consistently applied, produces a measurable improvement in first-draft quality. It reduces the edit-and-retry cycle. It compounds: the time saved on not re-prompting is time you keep.

---

**Habit 2 — Separate creation from critique**

One of the most consistent ways to produce better AI-assisted output is to separate the creation step from the critique step.

In a single-pass approach, you ask AI to produce something and evaluate what comes back. The problem with this is that evaluation is harder when you're still in generation mode. You're reading to understand, not to critique.

In a two-pass approach, AI creates. Then — in a fresh perspective — AI critiques. Or you do. This separation almost always produces better output.

The habit: for anything that matters, build in a critique step. After getting a first draft, send it back with a specific critique brief: "What's weak here? What's missing? Where does the argument not follow?" The critique step takes two minutes and routinely finds something worth fixing.

---

**Habit 3 — Keep a prompt library**

Every time you find a prompt structure that works well — for a type of task you do regularly, a format that reliably produces the right output, a critique framework that catches what matters — write it down.

Not the specific content. The structure. The prompt template that you can reuse, adapting the specifics to each new situation.

This is not complicated. A shared note, a simple document, a section of a personal reference file. Ten prompt templates that cover your most common AI tasks are worth more than a hundred prompts you'll never use again.

The habit: when you produce an interaction that works particularly well, before you close the tab, copy the prompt structure to your library. Over three months, this library becomes one of the most practically useful things you own as an AI user.

---

**Habit 4 — Review, don't just generate**

The instinct of most AI users is: prompt, read, use. The practice of consistently effective AI users is: prompt, read, verify, edit, use.

The word that bridges the gap is *editor*. Effective AI users are editors of AI output, not just consumers of it.

This doesn't mean correcting every sentence. It means reading the output as if you wrote it: looking for the thing that's slightly off, the conclusion that doesn't follow, the tone that's not quite right, the sentence that makes a commitment you didn't authorise.

The habit: before you send any AI-assisted work out into the world, read it once as its author, not as its reader. What would you change if this were your first draft? Usually it's one or two things. Make those changes.

---

**Building the habits: a practical approach**

Habits don't form through intention. They form through repetition in specific contexts. Here is a practical approach to building each of the four:

**Habit 1 (Front-load context):** Put a sticky note next to your screen for one week: "What does AI need to know?" Read it before you start every prompt. After a week, the question will have become automatic.

**Habit 2 (Separate creation and critique):** For the next ten pieces of writing AI helps you with, run a critique step before you finalise. Note whether it finds anything. After ten times, you'll know whether it's worth the two minutes (it is).

**Habit 3 (Prompt library):** Create a document called "AI Prompts" in the same place you keep other working documents. For the next month, add a prompt template every time you find one that works well. After a month, decide how useful it is.

**Habit 4 (Review as editor):** Before your next five AI-assisted emails, read them once as the recipient before sending. Notice how often you catch something small. That small catch is the habit paying off.

---

> **REAL-WORLD EXAMPLE**
>
> David runs a small consulting firm. He started using AI for client proposals and found the output reasonable but generic.
>
> He builds four habits over eight weeks:
>
> — He creates a project for each active client, loaded with brief context documents: the client's priorities, the project scope, his firm's standard approach.
> — He builds a proposal template prompt: a structured brief that covers context, audience, key messages, and constraints. It takes ninety seconds to fill in.
> — After every AI proposal draft, he runs a two-question critique: "What's weak?" and "What's missing?"
> — He reads every draft once from the client's perspective before it goes out.
>
> Three months later: his proposals take half the time to produce and he has received more unsolicited positive feedback from clients about their quality than in the previous two years.
>
> The AI hasn't changed. The habits have.

---

> **WHY IT WORKS**
>
> Each of these habits addresses a different failure mode. Front-loading context prevents mediocre first drafts. Separating creation from critique catches the problems that good first drafts obscure. A prompt library prevents starting from zero on repeat tasks. Reviewing as editor catches the specific kind of drift — confident, plausible, subtly wrong — that AI output is prone to. Together, they close most of the gap between occasional and reliable results.

---

**What these habits are not**

They are not rigid procedures. They are defaults — starting positions that you adapt to the task.

A quick email to a colleague doesn't need a full context front-load. A routine internal summary doesn't need a formal critique step. The habits are most valuable when the stakes are high, the task is complex, or the output will carry your name somewhere it matters.

Part of developing as an AI user is knowing when the full habit stack applies and when a lighter touch is appropriate. That judgment develops with practice.

---

## Chapter 24

### Keeping Up Without Burning Out

**The pace problem**

AI is developing faster than any of us can track. New models, new features, new platforms, new capabilities — often multiple announcements in a single week. For people who use AI professionally, this creates a particular kind of anxiety: the fear of being perpetually behind.

This chapter is about that anxiety — and why it is, in most practical respects, unnecessary.

---

**What actually changes (and what doesn't)**

Here is something that the breathless pace of AI announcements obscures: the things that make AI interactions work well — clear task definition, relevant context, specific instructions, calibrated verification — are not features. They are practices. They don't become obsolete when a new model releases.

The 7 Questions framework will work on models that don't exist yet. Context-building habits will transfer across platforms. Verification instincts don't expire. The difference between a vague prompt and a well-structured one will remain relevant regardless of how capable models become, because the improvement from structured prompting comes from the quality of the information you provide, not from the model's limitations.

What does change:
- Specific features and where to find them in interfaces
- Which tasks models can now do that they couldn't before
- The quality ceiling — the best output available for a given task
- Platform-specific tooling (projects, memory, integrations)

What doesn't change:
- The underlying principles of what makes a good interaction
- The verification habits that protect you from errors
- The workflow structures that organise complex tasks
- The judgment about what AI is and isn't appropriate for

If you have internalised this book's framework, you are not starting from zero every time a new model drops. You are updating the features while keeping the foundations.

---

**A sustainable information diet**

You don't need to read every AI newsletter, watch every YouTube video about the latest model, or test every new feature the week it launches. Here is a sustainable approach:

**Tier 1 — Quarterly attention (30-60 minutes)**
Once per quarter, spend an hour reviewing what has changed across your primary AI platforms. Focus on: new features relevant to how you actually use AI, any changes to the reliability or behaviour of models you rely on, anything that might change how you structure your regular workflows.

This is enough to stay genuinely current without AI becoming a part-time hobby.

**Tier 2 — Opportunistic learning (as it arises)**
When you read something specific that sounds relevant to a task you actually do — a new feature, a better approach to a problem you've encountered — test it on that specific task. Don't add it to your mental backlog. Test it, assess it, adopt it or discard it.

**Tier 3 — Passive exposure (as background)**
A single good source — one newsletter, one podcast, one informed person in your network — is sufficient background. You don't need to keep up with the field. You need to keep up with the practical changes to tools you use.

---

> **PRO TIP**
>
> The most important question for any AI news item is: does this change anything I do today? Most announcements, even genuinely significant ones, don't change anything about your practice immediately. Filter ruthlessly. When the answer is "yes, this changes how I should do X" — pay attention. When the answer is "interesting, but no practical implication" — move on.

---

**Testing new capabilities intelligently**

When a new model or significant feature launches, here is a practical testing approach:

1. Identify two or three tasks from your real work that you regularly use AI for.
2. Run those tasks on the new model or with the new feature exactly as you would normally.
3. Compare the output to what you've been getting. Is it better? In what specific ways?
4. If better: update your practice. If not: keep what you have.

This is faster and more useful than testing on artificial benchmark tasks or reading evaluation reports. You learn what the change means for your specific work, not for some averaged user.

---

**The experience curve**

There is a compounding that happens with AI practice that is easy to miss while you're in it.

The first few months of deliberate use — building prompt habits, setting up workspaces, running workflows, verifying output — feel effortful. You're building processes where there were none.

By six months, most of those processes are instinctive. You don't think about how to set up context; you just do it. You don't consciously decide to run a critique step; it happens automatically. The cognitive overhead drops, and the benefit stays.

By a year, your AI practice has a shape: a set of trusted workflows, a prompt library that reflects your actual work, a personal calibration of what AI does well for you and where to be careful. This is not something a new model release can disrupt, because it is built on practice, not features.

The people who benefit most from AI over time are not the ones who adopted it earliest or follow its development most closely. They're the ones who built consistent habits and let those habits compound.

---

**When to reassess**

There are moments that do warrant a more deliberate reassessment of your AI practice. Not because you're behind, but because the landscape has genuinely shifted in ways that affect your work:

- A task you previously found AI unreliable for now has significantly better model support
- A new category of tool (multi-modal, agentic, integrated) becomes stable and practical
- Your work changes significantly and the workflows you've built no longer fit
- A major platform change affects the tools you rely on

At these moments, run the equivalent of a quarterly review, but more deliberately: what has changed, what does it mean for how I work, what should I change?

This is not anxiety. It is the normal maintenance of a professional practice.

---

**What the AI user's playbook actually is**

The five chapters of Part VI reduce to a few core commitments:

Verify proportionately. Know what AI gets wrong. Calibrate your trust to the task. Build four habits and let them compound. Keep up without chasing.

None of these is complicated. All of them take practice. The payoff is a relationship with AI that is reliable, efficient, and genuinely useful — not a slot machine you occasionally win at, but a tool you have learned to use well.

---

*This completes Part VI. The Appendices that follow are reference materials: the 7 Questions quick reference card, the Before → Better → Best worksheet, the verification checklist, the use-cases guide, and the platform product notes.*

---

---

# APPENDICES

---

## Appendix A

### The 7 Questions Quick Reference Card

*Cut out or save this. Use it before any AI interaction that matters.*

---

**THE 7 QUESTIONS**
*Ask these before every significant AI interaction.*

---

**Q1 — What am I trying to achieve?**
State the outcome, not the task. Not "write a summary" but "summarise this report so that my manager can decide whether to read the full document."

---

**Q2 — What does AI need to know?**
Background. Context. Your role. The audience. The purpose. What would help AI understand this situation the way you do?

---

**Q3 — What information can I provide?**
Documents, data, previous work, examples, reference material. What do you have that AI should use? What should AI not rely on from its own training?

---

**Q4 — What exactly should AI do?**
Be specific about the task. Not "help me" but "draft a three-paragraph response that acknowledges the concern, explains our position, and ends with a clear next step."

---

**Q5 — What should the result look like?**
Format. Length. Tone. Structure. Audience. What does good look like for this specific output?

---

**Q6 — How will I check it?**
Before you prompt: know how you'll verify the output. Numbers? Sources? Fit with constraints? What will you check and how?

---

**Q7 — What should happen next?**
Will this output feed into something else? Does AI need to know about the next step to make this one useful? Is this a one-off or part of a workflow?

---

**QUICK REFERENCE — The AI Interaction Stack**

| Layer | Question it answers |
|---|---|
| Intent | What am I trying to achieve? |
| Context | What does AI need to know? |
| Instructions | What exactly should AI do? |
| Examples | What does good look like? |
| Source material | What information can I provide? |
| Workspace | Where is this work living? |
| Tools | Does AI need any capabilities? |
| Workflow | What happens before and after? |
| Output | What should the result look like? |
| Verification | How will I check it? |
| Iteration | What happens next? |

---

**THE BEFORE YOU TRUST CHECKLIST**

Before acting on AI output that matters:

- [ ] Is this factual or creative?
- [ ] Does it contain numbers? Verified?
- [ ] Are citations real? Checked?
- [ ] Could the information have changed?
- [ ] Did AI make assumptions I should check?
- [ ] Did it follow my constraints?
- [ ] Does the conclusion follow from the evidence?
- [ ] Have I read it as if I wrote it?

---

## Appendix B

### The Before → Better → Best Worksheet

*Use this template to apply the Before → Better → Best method to any task.*

---

**YOUR TASK**

What do you want AI to produce?
_________________________________________________

---

**STEP 1 — BEFORE (the natural request)**

Write the prompt you would have sent before reading this book:

```
[Your instinctive first prompt]
```

What is missing from this prompt?

— Role/context: ___________________________________
— Audience: ______________________________________
— Format: _______________________________________
— Constraints: ____________________________________
— Examples: _____________________________________
— Verification: ____________________________________

---

**STEP 2 — BETTER (add the most important missing element)**

Identify the single most important thing missing from the BEFORE prompt. Add it:

```
[Improved prompt with the key missing element added]
```

What changed and why does it matter?
_________________________________________________

---

**STEP 3 — BEST (apply the full 7 Questions)**

Work through each question:

| Question | Your answer |
|---|---|
| Q1: What am I trying to achieve? | |
| Q2: What does AI need to know? | |
| Q3: What information can I provide? | |
| Q4: What exactly should AI do? | |
| Q5: What should the result look like? | |
| Q6: How will I check it? | |
| Q7: What should happen next? | |

Now write the BEST prompt incorporating all of the above:

```
[Your best prompt]
```

---

**STEP 4 — COMPARE**

Run all three prompts. Record:

| | BEFORE | BETTER | BEST |
|---|---|---|---|
| Quality (1-5) | | | |
| Usefulness (1-5) | | | |
| Needed editing? | | | |
| Verified? | | | |
| Would use? | | | |

What did you learn?
_________________________________________________

---

**REUSABILITY**

Could this BEST prompt be turned into a reusable template?

Template name: _________________________________

Placeholders to add (things that change each time):
_________________________________________________

Where you'll save it:
_________________________________________________

---

## Appendix C

### Verification Checklist

*Use this checklist for any AI output you will act on, share, or use in a significant decision.*

---

**PART 1 — CONTENT VERIFICATION**

**Factual claims**
- [ ] Key facts identified (numbers, dates, names, statistics, citations)
- [ ] High-priority facts checked against primary sources
- [ ] Sources cited by AI verified as real and accessible
- [ ] Time-sensitive information checked from a current source
- [ ] Any claim I would quote or share publicly verified independently

**Reasoning and conclusions**
- [ ] AI's reasoning is shown (not just the conclusion)
- [ ] The conclusion follows from the evidence provided
- [ ] I've identified what assumptions AI made
- [ ] The recommendation or conclusion fits my specific situation (not just the general case)
- [ ] I've considered alternative conclusions and whether AI's is the best-supported

---

**PART 2 — INSTRUCTION ADHERENCE**

- [ ] Output is the length specified
- [ ] Output uses the format specified
- [ ] Tone matches what was requested
- [ ] All constraints from the prompt are observed
- [ ] Nothing is included that was explicitly excluded
- [ ] Nothing important is omitted that was explicitly requested

---

**PART 3 — TASK-SPECIFIC CHECKS**

*Complete the rows relevant to your task.*

| Task type | Specific check |
|---|---|
| Professional email | Read from recipient's perspective. Any unintended commitments? Tone correct? |
| Research summary | Key claims checked. Summary matches source material accurately. |
| Document analysis | Read original document for anything AI may have misread or simplified. |
| Data or calculation | Key figures checked. Calculation steps verified. |
| Legal or regulatory content | Not relied upon without professional advice for high-stakes decisions. |
| Medical information | Not acted upon without healthcare professional consultation. |
| Creative writing | Read for anything that lands differently than intended. Voice preserved. |
| Proposal or recommendation | Reasoning reviewed. Fit with specific situation confirmed. |

---

**PART 4 — FINAL REVIEW**

- [ ] Read the output once as its author (not its reader)
- [ ] Anything you would not have written this way? Address it.
- [ ] Anything missing that you intended? Add it.
- [ ] Does it represent your position accurately?
- [ ] Are you comfortable with your name on it?

---

**High-stakes sign-off (for output in regulated, legal, medical, or financial areas)**

- [ ] Treated as background and context, not authoritative guidance
- [ ] Professional advice obtained where required
- [ ] Any specific claims verified from official current sources
- [ ] Not relied upon as a substitute for professional judgment

---

## Appendix D

### AI Use Cases by Profession

*This guide maps common professional roles to the AI workflows most likely to be useful. It is a starting point for identifying where AI can integrate into your work — not a comprehensive list.*

---

**How to use this appendix**

Find your profession or the closest equivalent. Review the use cases listed. Cross-reference with the Part V workflows that match each use case. For each use case marked with a ⚠, apply the high-stakes verification checklist from Appendix C before acting on output.

---

**MARKETING AND COMMUNICATIONS**

| Use case | Relevant workflows | Notes |
|---|---|---|
| Email and copy drafting | W1, W24, W25 | Review for tone, brand fit, any claims that need verification |
| Campaign brief writing | W25 | Provide existing brand guidelines as source material |
| Research and competitor analysis | W3, W5, W13 | Verify time-sensitive market data from current sources |
| Social and content production | W9, W10, W11 | Review for accuracy before publication |
| Presentation preparation | W8, W3 | Check facts; review from audience perspective |
| Meeting preparation | W3 | Supplement with primary research for critical decisions |

---

**MANAGEMENT AND LEADERSHIP**

| Use case | Relevant workflows | Notes |
|---|---|---|
| Difficult conversation preparation | W2 | Your judgment on tone and specifics is essential |
| Report and proposal writing | W7, W25 | Review conclusions carefully before sharing |
| Decision research | W13, W14 | Verify key facts; apply your contextual knowledge |
| Team communication drafting | W1, W24 | Review for tone; you know the relationship context |
| Meeting preparation | W3 | Check current data for any fast-moving areas |
| Performance frameworks | W6, W7 | Adapt general frameworks to your organisation's context |

---

**FINANCE AND ACCOUNTING**

| Use case | Relevant workflows | Notes |
|---|---|---|
| Document summarisation | W4, W5 | ⚠ Verify figures against source documents |
| Research for client briefing | W3, W13 | ⚠ Verify from regulated, current sources |
| Report drafting | W7, W25 | ⚠ All figures and claims verified independently |
| Regulatory framework overview ⚠ | W13 | Starting point only; verify from official current guidance |
| Client communication | W1, W24 | Review for any inadvertent commitments or advice |
| Presentation and briefing preparation | W8, W3 | ⚠ All figures and sources verified |

---

**LEGAL AND COMPLIANCE**

| Use case | Relevant workflows | Notes |
|---|---|---|
| Document review and summarisation ⚠ | W4, W22 | Starting point; read original; professional review for high stakes |
| Contract red-flag identification ⚠ | W22 | Use to prepare for professional review, not replace it |
| Research briefing ⚠ | W13, W14 | Verify from current primary sources |
| Client communication drafting | W1, W24 | Review carefully; legal professional review where required |
| Regulatory overview ⚠ | W13 | Starting point only; verify from current official guidance |

*Note: AI is not a substitute for legal professional advice. Use cases marked ⚠ should be treated as research and preparation tools, not as authoritative legal guidance.*

---

**EDUCATION AND ACADEMIA**

| Use case | Relevant workflows | Notes |
|---|---|---|
| Research and literature overview | W13, W14 | ⚠ Verify citations independently; check sources exist |
| Writing and editing | W24, W25 | Check for voice preservation; verify any claims |
| Lesson and course planning | W6, W7, W25 | Adapt AI output to your specific context and students |
| Summarisation and note-making | W4, W5 | Cross-reference against original materials |
| Learning and understanding | W15, W16 | Excellent use case; verify technical claims in specialist areas |
| Feedback drafting | W24 | Review carefully; you know the individual student's context |

---

**SMALL BUSINESS OWNERS**

| Use case | Relevant workflows | Notes |
|---|---|---|
| Proposal and bid writing | W7, W25 | Review for your specific situation; verify pricing figures |
| Client communication | W1, W24 | Review for tone; add personal knowledge of client relationship |
| Research | W3, W13 | Verify key market and competitor data from current sources |
| Marketing content | W9, W10, W11 | Review for brand fit and accuracy |
| Financial planning overview ⚠ | W14 | Starting point; consult a financial professional for decisions |
| Contract review ⚠ | W22 | Preparation tool; professional review for significant contracts |

---

**HEALTHCARE PROFESSIONALS**

| Use case | Relevant workflows | Notes |
|---|---|---|
| Summarising clinical documents | W4, W5 | ⚠ Verify against source; professional judgment applies |
| Patient communication drafting | W1, W24 | Review carefully; clinical accuracy is your responsibility |
| Research and literature overview | W13, W14 | ⚠ Verify from current clinical sources |
| Administrative writing | W7, W25 | Standard professional review applies |
| Training material development | W6, W7 | Review for clinical accuracy |

*Note: AI should not be used to generate clinical guidance, diagnoses, or treatment plans. These use cases cover administrative and professional communication tasks.*

---

**HOME AND PERSONAL USE**

| Use case | Relevant workflows | Notes |
|---|---|---|
| Travel planning | W21 | ⚠ Verify booking details, visa requirements, and entry requirements from official sources |
| Understanding contracts and documents ⚠ | W22 | Preparation tool; professional advice for significant decisions |
| Health questions ⚠ | W23 | Background information only; consult a healthcare professional |
| Learning something new | W15, W16 | Excellent use case; verify technical claims in specialist areas |
| Personal writing | W24, W25 | Good use case; check for voice preservation |
| Household decisions | W17, W18, W19, W20 | Use as a thinking partner; apply your own judgment |

---

## Appendix E

### Product Notes — Platform-Specific Information

*This appendix contains platform-specific feature information that was current at the time of writing. AI products change frequently. All product notes should be treated as a starting point — verify current availability and behaviour from the platform's official documentation before relying on any specific feature.*

---

> **IMPORTANT**
> The information in this appendix was verified in September 2026. Feature availability, naming, pricing, and behaviour may have changed. Before relying on any feature described here:
> 1. Check the platform's current help documentation
> 2. Look for any announcements about feature changes
> 3. Test the feature yourself before building it into your workflow

---

**How to find current documentation**

| Platform | Documentation URL |
|---|---|
| ChatGPT / OpenAI | help.openai.com |
| Claude / Anthropic | support.anthropic.com |
| Gemini / Google | support.google.com/gemini |
| Microsoft Copilot | support.microsoft.com/copilot |

For any specific feature mentioned in this appendix, search the relevant help documentation using the feature name.

---

### E1 — Persistent Instructions and Custom Instructions

**What this feature does**
Allows you to set instructions that apply to every conversation without having to retype them. The AI reads these instructions at the start of each session.

**Where to find it (September 2026)**

| Platform | Feature name | Location |
|---|---|---|
| ChatGPT | Custom Instructions | Settings → Personalisation → Custom Instructions |
| Claude | Personal preferences / system prompt | Settings → Profile |
| Gemini | Personalisation settings | Profile menu → Personalisation |
| Microsoft Copilot | Varies by version | Settings or account preferences |

**Volatility: MEDIUM** — Feature names and locations change with interface updates. The concept is stable; the location may have moved.

**What to include in persistent instructions**
- Your name and role
- Your typical audience (who you write for)
- Your preferred tone and style
- Any consistent constraints (UK/US spelling, never use X format, always include Y)
- The context of your work that applies broadly

**What not to include**
- Project-specific information (use Projects for this)
- Instructions that only apply to some conversations
- Very long documents or detailed reference material

---

### E2 — Projects

**What this feature does**
Groups conversations under a named project, with persistent uploaded documents and context that is shared across all conversations in that project. Designed for ongoing work where you return to the same context repeatedly.

**Where to find it (September 2026)**

| Platform | Feature name | Notes |
|---|---|---|
| ChatGPT | Projects | Available in the left sidebar |
| Claude | Projects | Available in the main navigation |
| Gemini | Gems | Named AI configurations with system instructions |
| Microsoft Copilot | Varies | Check current feature availability |

**Volatility: MEDIUM** — Projects features were in active development as of September 2026 across all major platforms. Feature behaviour, capacity limits, and capabilities were subject to change.

**Best for**
- Recurring client accounts
- Ongoing research projects
- Regular document types with consistent context
- Any work where you return to the same AI context more than a few times

---

### E3 — File and Document Upload

**What this feature does**
Upload documents, images, spreadsheets, and other files for AI to read and reference within the conversation.

**September 2026 status**

| Platform | Supported file types (approximate) | Notes |
|---|---|---|
| ChatGPT | PDF, Word, Excel, images, CSV, code files | Size limits apply; check current documentation |
| Claude | PDF, Word, images, text files | Context window limits determine effective size |
| Gemini | PDF, images, some office formats | Check current support list |
| Microsoft Copilot | Microsoft Office formats; varies by version | Tightest integration with Word/Excel/PowerPoint |

**Volatility: HIGH** — Supported file types, size limits, and how documents are processed change frequently. Check current documentation for limits.

**Key behaviour to understand**
AI reads the document you upload and uses its contents to answer your questions or complete the task. It does not store the document permanently — it is available for the current conversation (or project, if uploaded there). For large documents, AI may not be able to process the full content at once; for very long documents, directing AI to specific sections is more reliable than assuming it has read every page.

---

### E4 — Web Search

**What this feature does**
Allows AI to search the web for current information during a conversation, accessing content beyond its training data cutoff.

**September 2026 status**

| Platform | Status | Notes |
|---|---|---|
| ChatGPT | Available (with search tool enabled) | Can be toggled on in conversation |
| Claude | Available via web search tool | Check current feature availability |
| Gemini | Integrated by default | Built into responses where relevant |
| Microsoft Copilot | Integrated | Bing search integrated throughout |
| Perplexity | Core feature | Built on web search as primary capability |

**Volatility: MEDIUM** — Web search availability and integration depth have been changing rapidly. Current status may differ.

**When it helps**
- Current events and recent news
- Current prices, product availability, or specifications
- Recent regulatory or policy changes
- Any information that changes frequently

**Limitations to understand**
Even with web search, AI may not access paywalled content, may retrieve outdated pages if not directed to current sources, and should still be verified for high-stakes factual claims.

---

### E5 — Voice and Audio

**What this feature does**
Allows conversation with AI by voice rather than text, with AI responding by voice or text.

**September 2026 status**

| Platform | Feature name | Notes |
|---|---|---|
| ChatGPT | Voice mode / Advanced Voice | Available in mobile app and some desktop versions |
| Claude | Voice (mobile) | Available in Claude mobile apps |
| Gemini | Voice input | Available in the Gemini app |
| Apple Intelligence | Siri with AI integration | Built into Apple devices |
| Google Assistant | AI integration | Available on Android |

**Volatility: HIGH** — Voice features were in rapid development as of September 2026. Capabilities, languages supported, and availability change frequently.

**Best used for**
- Hands-free situations (commuting, exercising, cooking)
- Thinking out loud and capturing ideas
- When typing is inconvenient
- Accessibility needs

**Limitations**
Voice mode typically has less precise instruction-following than text. For complex or structured prompts, text input remains more reliable.

---

### E6 — Memory

**What this feature does**
Some platforms allow AI to remember facts across conversations — so that something you tell AI in one session is available in a future session without you restating it.

**September 2026 status**

| Platform | Memory feature | Notes |
|---|---|---|
| ChatGPT | Memory | Can be reviewed, edited, and deleted in settings |
| Claude | Memory (in Claude.ai) | User-controlled; viewable in settings |
| Gemini | Personalisation | Some cross-session personalisation |

**Volatility: HIGH** — Memory features were actively developing as of September 2026. Behaviour, what is remembered, and privacy controls may have changed.

**Privacy consideration**
Memory stores information from your conversations for future use. Review what is stored periodically (most platforms provide this in settings). Delete anything you don't want retained.

**Best used for**
- Persistent professional context that doesn't change often
- Preferences that apply across all your AI use
- Background about yourself you always want AI to know

**Not a substitute for**
Project-specific context, document uploads, or detailed instructions. Memory stores facts and preferences; Projects stores ongoing work context and documents.

---

### E7 — Model differences (brief reference)

*A very brief guide to how the major models differ in behaviour as of September 2026. Model behaviour changes with updates — this is a starting orientation, not a permanent characterisation.*

| Model family | Characteristic behaviour | Best for |
|---|---|---|
| GPT-4o / GPT-5 class (OpenAI) | Strong all-round capability; good instruction following; creative tasks | General professional use; coding; complex reasoning |
| Claude (Anthropic) | Careful, thorough responses; tends to flag uncertainty; good at document tasks | Document analysis; careful writing; nuanced tasks |
| Gemini (Google) | Good real-time information access; strong with Google Workspace | Research with current information; Workspace integration |
| Microsoft Copilot | Integrated into Microsoft 365; strong with Office document workflows | Office document tasks; enterprise workflows |

**Volatility: VERY HIGH** — Model capabilities change significantly with each major release. This table reflects September 2026 characteristics only. Current comparisons should be assessed from recent evaluations and your own testing.

---

*This completes the Appendices.*

---

---

## A Note on What Comes Next

This is the first book in the Art of AI series. Book 1 has covered the foundations: the mental model, the interaction skills, the environment, the workflows, and the habits.

Books in development for the series include:

**Book 2 — The Art of AI at Work**
Deep-dive workflows for professional use cases: managing teams, client communication, research, analysis, and professional writing at a higher level of sophistication.

**Book 3 — The Art of AI for Business Owners**
AI systems for small and growing businesses: marketing, proposals, operations, customer communication, and financial planning support.

*Visit [the series page] for updates on publication dates and to join the reader list.*

---

*The Art of AI, Book 1*
*First edition, 2026*

*All factual claims verified at time of writing. Platform-specific information in Appendix E should be verified from current official sources before reliance. AI tools were used in the research, drafting, and editing of this manuscript. All editorial judgment, structure, and final decisions are the author's own.*
