# The Art of AI — Editorial System

## Purpose

This system exists to ensure the books look and feel like **professional paid reference books**, not AI-generated content.

The standard is closer to a good practical business book or consumer reference manual than a blog post.

---

# 1. Editorial identity

## Voice

- intelligent;
- calm;
- practical;
- confident but not arrogant;
- accessible;
- encouraging;
- evidence-aware;
- occasionally humorous;
- never breathless.

## Avoid

- "revolutionary";
- "game-changing";
- "unlock the power";
- "10X your productivity";
- "secret";
- "magic prompt";
- excessive emojis;
- exaggerated claims;
- generic motivational filler.

---

# 2. Reader language

Assume the reader is intelligent but non-technical.

Never assume they know:

- tokens;
- APIs;
- context windows;
- embeddings;
- MCP;
- XML;
- agents;
- RAG;
- temperature.

If a technical concept matters:

1. explain it in ordinary language;
2. give the technical term;
3. explain why the reader should care;
4. demonstrate it.

---

# 3. Anti-AI-slop rules

## Rule 1

No chapter may exist merely to increase page count.

## Rule 2

Every chapter must solve a recognizable reader problem.

## Rule 3

Avoid repetitive prompt examples.

## Rule 4

Do not use five examples that demonstrate exactly the same idea.

## Rule 5

Every major claim needs evidence or clear qualification.

## Rule 6

Every major technique should include a real-world scenario.

## Rule 7

Every major technique should show at least one failure mode.

## Rule 8

Do not pretend an AI output is correct merely because it sounds professional.

## Rule 9

Do not manufacture fake statistics, testimonials or research findings.

## Rule 10

Never publish untested prompts as "proven".

---

# 4. Signature page architecture

A strong practical section should use:

## The Problem

What the reader is experiencing.

## Why the Simple Approach Fails

Explain the underlying problem.

## Try This

Give the improved interaction.

## What Changed?

Annotate the important parts.

## What You Should Expect

Show likely output characteristics.

## Check It

Teach verification.

## Make It Reusable

Explain how to turn it into a template/workflow.

---

# 5. Prompt presentation format

Do not dump giant blocks of text.

Use:

### The situation

Plain English.

### The prompt

A clean block.

### Why it works

Short explanation.

### Change this

Identify the fields the reader should personalize.

### Watch out

Failure modes.

### Upgrade

Show the next-level version.

---

# 6. Prompt cards

Every reusable prompt should have metadata:

```text
PROMPT NAME:
PURPOSE:
BEST FOR:
INPUTS REQUIRED:
TOOLS / FEATURES:
DIFFICULTY:
EXPECTED OUTPUT:
CUSTOMIZE:
VERIFY:
REUSABILITY:
```

---

# 7. Example quality standard

A strong example contains:

- realistic person;
- realistic objective;
- realistic information;
- realistic constraints;
- realistic output;
- realistic imperfections;
- verification.

Avoid fake businesses with implausibly perfect data unless the example is explicitly instructional.

---

# 8. Show failure

This is one of the strongest differentiators.

Example:

### Reader asks

"Write me a business plan."

### Typical result

Generic plan with:
- invented market size;
- generic marketing advice;
- unrealistic projections.

### Lesson

The AI was not given:
- business model;
- location;
- target customer;
- pricing;
- costs;
- competitors;
- constraints.

Then rebuild the interaction.

---

# 9. Teach verification

Every book should contain a recurring box:

## Before You Trust the Answer

Ask:

- Is this factual or creative?
- Does it contain numbers?
- Does it cite sources?
- Are the sources real?
- Could information have changed?
- Did the AI make an assumption?
- Did it follow my constraints?
- What evidence supports the conclusion?

---

# 10. Visual editorial language

Use consistent callouts.

### TRY THIS

A practical technique.

### WHY IT WORKS

The underlying explanation.

### WATCH OUT

Failure mode.

### PRO TIP

Useful shortcut.

### VERIFY

Accuracy check.

### REAL-WORLD EXAMPLE

Applied scenario.

### NEXT LEVEL

Advanced variation.

This makes the book easy to scan.

---

# 11. Chapter scoring

Every chapter is scored out of 100.

| Dimension | Weight |
|---|---:|
| Practical usefulness | 20 |
| Originality | 15 |
| Accuracy | 20 |
| Examples | 15 |
| Clarity | 10 |
| Reader engagement | 5 |
| Cross-model relevance | 5 |
| Verification | 5 |
| Reusability | 5 |

Minimum publication score:

**85/100**

Any chapter below 80 must be rewritten.

---

# 12. Manuscript QA gates

## Gate 1 — Structural

- Does the chapter have a clear purpose?
- Does it progress logically?
- Is anything redundant?

## Gate 2 — Evidence

- Are product claims current?
- Are citations/source notes recorded?
- Are uncertain claims qualified?

## Gate 3 — Practical

- Can the reader actually use the technique?
- Are inputs clear?
- Are examples realistic?

## Gate 4 — Anti-slop

- repetitive language?
- filler?
- generic headings?
- excessive bullet lists?
- fake enthusiasm?
- suspiciously uniform prose?

## Gate 5 — Reader

Give a section to someone unfamiliar with AI.

Ask:

> "Could you actually follow this?"

## Gate 6 — Production

Check:
- headings;
- tables;
- prompt formatting;
- page breaks;
- typography;
- contents;
- references;
- indexes where appropriate;
- Kindle rendering;
- paperback rendering.

---

# 13. AI-assisted production rules

AI can:

- brainstorm;
- research;
- summarize source material;
- propose outlines;
- generate draft alternatives;
- critique;
- identify repetition;
- simulate beginner questions;
- test prompts;
- compare outputs.

AI should not be allowed to silently determine:

- factual claims;
- final source selection;
- final editorial voice;
- publication readiness.

The editor remains responsible.

---

# 14. Human editorial passes

Every manuscript receives at least five passes.

### Pass 1 — Architecture

Does the book teach something coherent?

### Pass 2 — Accuracy

Are claims correct?

### Pass 3 — Practicality

Can the reader use it?

### Pass 4 — Voice

Does it sound like a professional author?

### Pass 5 — Production

Does it look like a professional book?

---

# 15. The "Paid Book Test"

Before publication ask:

> If the reader had access to a free AI assistant, why would they pay for this book?

The answer must be something like:

- curated methodology;
- tested examples;
- structured progression;
- practical scenarios;
- failure analysis;
- reusable workflows;
- cross-model perspective;
- exercises;
- professional editing;
- comprehensive reference value.

If the answer is merely:

> "Because the book contains prompts."

The book is not ready.

---

# 16. KDP compliance

Maintain an explicit AI-use log.

Record:

- where AI generated text;
- where AI generated images;
- where AI assisted editing;
- what human editorial work was performed.

Amazon KDP requires disclosure of AI-generated text, images or translations when publishing or republishing affected content. AI-assisted work such as brainstorming, editing or refinement is treated differently under the current guidance.

Always recheck KDP's current rules immediately before submission.
