# THE ART OF AI

## How to Get Better Results From Every AI Conversation

### A Practical Guide to Better Prompts, Better Context, and Better Workflows

**The Art of AI, Book 1**

---

*For every person who typed something into ChatGPT, got a vague wall of text, and quietly wondered whether everyone else was getting something they weren't.*

---

## COPYRIGHT

Copyright © 2026 The Art of AI

All rights reserved. No part of this publication may be reproduced, distributed, or transmitted in any form or by any means, including photocopying, recording, or other electronic or mechanical methods, without the prior written permission of the publisher, except in the case of brief quotations embodied in critical reviews and certain other non-commercial uses permitted by copyright law.

**Published by:** The Art of AI  
**Series:** The Art of AI, Book 1  
**First edition:** 2026

**AI Disclosure:** AI tools were used in the research, drafting, and editing of this book. All factual claims were verified against primary sources at the time of writing. Examples were reviewed for clarity and intended use. Editorial judgment, structure, and final decisions are the author's own.

*Amazon KDP AI disclosure completed in the publishing dashboard per current requirements. KDP's AI content policy should be rechecked before any future edition.*

---

## CONTENTS

**Introduction:** You Are Not Bad at AI

**Part I, A Different Way to Think About AI**
- Chapter 1: Why AI Gives You Generic Answers (and How to Change That)
- Chapter 2: The AI Interaction Stack, What Actually Determines Output Quality
- Chapter 3: The 7 Questions, Your Portable AI Framework
- Chapter 4: How to Talk to an AI (It's Not Google)

**Part II, Build Better Interactions**
- Chapter 5: Give AI a Job, Not Just a Question
- Chapter 6: Context Is Everything
- Chapter 7: Instructions That Actually Work
- Chapter 8: Examples Change Everything
- Chapter 9: Control the Output

**Part III, Build an AI Environment**
- Chapter 10: Stop Starting From Zero Every Time
- Chapter 11: Projects and Persistent Instructions
- Chapter 12: Files, Documents, and Source Material
- Chapter 13: Tools, What AI Can Do Beyond Text
- Chapter 14: The Memory Problem (and How to Work Around It)
- Chapter 15: Building Your Personal AI Workspace

**Part IV, From Prompts to Workflows**
- Chapter 16: When One Prompt Isn't Enough
- Chapter 17: Breaking Tasks Into Steps
- Chapter 18: Critique, Edit, and Improve
- Chapter 19: Chains, Loops, and Handoffs

**Part V, 25 Real-World Workflows**
- W1–W8: Business and Professional
- W9–W12: Marketing and Content
- W13–W16: Research and Learning
- W17–W20: Personal Productivity
- W21–W23: Home and Life
- W24–W25: Writing and Editing

**Part VI, The AI User's Playbook**
- Chapter 20: How to Verify AI Output
- Chapter 21: What AI Gets Wrong (Consistently)
- Chapter 22: Calibrating Trust
- Chapter 23: Building Your AI Habits
- Chapter 24: Keeping Up Without Burning Out

**Appendices**
- A: The 7 Questions Quick Reference Card
- B: The Before → Better → Best Worksheet
- C: Verification Checklist
- D: AI Use Cases by Profession
- E: Product Notes (Platform-Specific Information)

---

## INTRODUCTION

### You Are Not Bad at AI

There is a particular kind of frustration that comes from using a tool that is supposed to be extraordinary and finding it merely annoying.

You type a question into ChatGPT or Claude or Gemini. You wait. You read the response. It is, somehow, both very long and not quite what you wanted. It is technically correct in the way that a weather forecast saying "conditions may vary" is technically correct. It is not wrong. It is not useful. You close the tab and do the task yourself.

This happens to most people most of the time. Not because AI is bad, it isn't, but because the interaction was badly set up from the start.

Here is what no one tells you: the quality of what AI produces is determined less by the AI and more by what you give it. Not your technical knowledge. Not your ability to write special commands. What you give it: the information, the instructions, the structure, the context, the constraints, the documents, the clear job description.

This book is about that system.

**What you will actually learn**

By the end of Part I, you will understand why AI produces generic output and exactly what changes when it produces something good. That understanding alone is worth more than any list of prompts, because it means you can diagnose what went wrong in any interaction and fix it, rather than just trying different words until something works.

By the end of Part II, you will know how to build an AI interaction deliberately: giving AI the role, the context, the instructions, the examples, and the output format that get you the result you need.

By the end of Part III, you will know how to build an AI environment, a persistent workspace where you stop repeating yourself, where your files and preferences carry forward, and where AI actually knows something about your situation.

By the end of Part IV, you will be able to design multi-step workflows: decomposing a complex task into stages, running them in sequence, and using AI's output from one step as the input to the next.

Part V gives you twenty-five tested workflows to use immediately or adapt. Part VI gives you the habits and verification practices that distinguish people who use AI reliably from people who use it hopefully.

**The framework**

Running through all of it is a single seven-question framework you can carry in your head. Before any significant AI interaction, these seven questions identify what you need to provide. They work on every AI platform, ChatGPT, Claude, Gemini, Copilot, and every tool built on these models. They will still work when the current models are replaced by the next generation.

The framework is called The 7 Questions. You will encounter it in Chapter 3, and you will use it for the rest of the book.

**A word about technical knowledge**

None of this requires technical knowledge. You do not need to understand how large language models work. You do not need to know what a token is, or an API, or an embedding. When technical concepts appear in this book, they appear because they directly affect how you use AI, and they are always explained in ordinary language before the technical term is introduced.

What you need is the willingness to think about AI interactions differently, not as typing questions into a search engine, but as briefing a capable colleague who starts every conversation knowing nothing about you, your work, or what you need.

Once you understand that, everything else follows.

Let's begin.

---

# PART I

## A Different Way to Think About AI

*The four chapters in this part build the mental model that makes everything else in the book work. They are short by design. If you understand what this part is teaching, you will already be getting noticeably better results before you reach Part II.*

---

## Chapter 1

### Why AI Gives You Generic Answers (and How to Change That)

**The problem everyone has but nobody explains**

Ask ten people what frustrates them about AI and you will hear the same answers:

*"It's too generic."*
*"It doesn't understand what I actually want."*
*"It's confident but wrong."*
*"The answer doesn't fit my situation."*
*"It gives me five paragraphs when I needed two sentences."*

These are not problems with the AI. They are problems with the interaction.

This chapter explains why generic inputs produce generic outputs, and what specifically changes when they don't.

---

**The slot machine model (and why it's wrong)**

Most people approach AI the way they might approach a vending machine: insert request, press button, hope for the right thing to fall out. When it doesn't, they try slightly different words. Sometimes this works. Usually it's a matter of luck.

This approach treats AI as a slot machine. It also produces slot-machine results: random, unpredictable, and mostly disappointing.

The people who get consistently good results from AI are not luckier. They are not using secret prompts. They understand something that slot-machine users don't: AI output is shaped by input, and almost every dimension of that input is under your control.

---

**Why AI is generic by default**

When you send AI a vague request, "Write me a summary of this report", it has to make assumptions about everything it doesn't know:

- Who is going to read this summary?
- How long should it be?
- What are the most important points to include?
- What should be left out?
- What tone is appropriate?
- What does the reader already know?
- What is the purpose of the summary?

AI will fill in all of these gaps. It will fill them in with the most statistically average answers it can construct, the kind of summary that would be acceptable to the largest number of readers in the largest number of situations. This is why AI output so often feels as though it was written for everyone and therefore fits no one particularly well.

The good news: every assumption AI makes is one you could have specified yourself. The summary would look completely different if you told AI: *"This is for our CEO, who hasn't read the report and needs to decide whether to approve a £200,000 budget. She wants two paragraphs, direct language, and the headline number up front."*

Same document. Same AI. Dramatically different output. The only difference is what you provided.

---

> **WHY IT WORKS**
>
> AI tools generate text by predicting what words should follow what came before, based on patterns learned from enormous quantities of written material. This means the quality and specificity of what they produce is directly shaped by the quality and specificity of what they receive. Providing more relevant information doesn't confuse AI, it constrains the prediction space to something closer to what you actually need.

---

**The three most common input failures**

After looking at hundreds of AI interactions that produced poor results, three input problems appear again and again:

**1. The vague job description**

*"Help me with my presentation"* tells AI you want a presentation. It doesn't tell it the topic, the audience, the desired length, your current draft, what help means, or what "better" would look like. AI has no choice but to respond generically to a generic request.

**2. The missing context**

*"Reply to this email"* gives AI a text to work with. It doesn't tell AI who sent it, what the relationship is, what a good reply should accomplish, whether you need to decline or accept, how formal the tone should be, or what your constraints are. AI will guess. Sometimes it guesses right. Usually the first reply it produces needs significant editing.

**3. The wrong assumed audience**

*"Explain compound interest"* gives AI a topic. But who is asking? A secondary school student? A financial professional? Someone deciding whether to take out a mortgage? AI will produce an explanation pitched at a generic reader, which means it may be too basic, too technical, or simply beside the point for your actual need.

---

> **REAL-WORLD EXAMPLE**
>
> Sarah is a marketing manager who needs to send a follow-up email to a potential agency partner after an introductory call. She types:
>
> *"Write a follow-up email after a business meeting."*
>
> AI produces a template with placeholders like [Name] and [Company] and generic phrases like "It was great connecting with you." It's technically a follow-up email. It has nothing to do with Sarah's actual situation, the tone of the meeting, what was discussed, or what the next step should be.
>
> She then provides: who the meeting was with, what was discussed, what her specific goal for the follow-up is, and how she wants to come across. The email AI produces next is one she could send without changes.
>
> Same AI. Same model. The variable was what she gave it.

---

**What actually changes good AI output**

Five inputs move the needle most consistently. They appear in greater detail throughout this book, but in brief:

1. **A clear job**: What specifically do you want AI to do? (Not "help with", do.)
2. **Relevant context**: What does AI need to know about your situation, audience, and constraints?
3. **Source material**: What documents, notes, or data should AI work from?
4. **Output specifications**: What should the result look like, length, format, tone, structure?
5. **Verification instructions**: How should AI flag uncertainty or potential errors?

This is not a complete list. The next chapter introduces the full model. But if you apply only these five, you will notice an immediate and significant improvement.

---

> **TRY THIS**
>
> Take a prompt you have used before that produced a disappointing result. Write it down.
>
> Now ask yourself: What did I assume AI would know that it couldn't have known? What context did I leave out? What does "good" actually look like for this task?
>
> Rewrite the prompt with those gaps filled in and run both versions. Notice what changed.

---

**What this chapter established**

Generic inputs produce generic outputs. This is a feature, not a bug, it means every improvement you make to your input produces a corresponding improvement in output. You are not at the mercy of the AI. You are in control of the most important variable in every interaction.

The next chapter introduces a model for understanding exactly which variables are in play, and which ones matter most for any given task.

---

> **WATCH OUT**
>
> More detail is not always better. Adding irrelevant information doesn't improve output, it can dilute it. The skill is not writing longer prompts; it's identifying what AI actually needs to know to do this specific task well. You'll develop this judgment through the exercises in Part II.

---

## Chapter 2

### The AI Interaction Stack, What Actually Determines Output Quality

**Introducing a map**

When a piece of work goes wrong, it helps to know where in the process the problem occurred. A cake that doesn't rise failed at a different point than a cake that doesn't taste right. The diagnosis matters.

AI interactions fail at predictable places. This chapter introduces a model, the AI Interaction Stack, that maps those places. It gives you a vocabulary for diagnosing what went wrong and a checklist for getting it right before you start.

---

**The AI Interaction Stack**

The AI Interaction Stack has eleven layers. Each layer represents something that shapes what AI produces. When an interaction produces poor results, at least one of these layers is inadequate or missing.

You do not need all eleven layers for every task. A quick factual question might only need layers 1–4. A complex document workflow might need all eleven. The point is knowing which layers exist so you can deliberately choose which ones to activate.

Here they are, in order:

```
THE AI INTERACTION STACK

11  Iteration       What happens next?
10  Verification    How will you check it?
 9  Output          What should the result look like?
 8  Workflow        One step or several?
 7  Tools           What capabilities are available?
 6  Workspace       What context can persist?
 5  Source material What can AI work from?
 4  Examples        What does good look like?
 3  Instructions    What exactly should AI do?
 2  Context         What does AI need to know?
 1  Intent          What are you trying to achieve?
```

Read the stack from the bottom up. Start with the real goal, then add only the layers that this task needs. The upper layers help you check, improve, and continue the work; they do not replace the clarity of the layers below them.

<!-- VISUAL: interaction-stack -->

---

**Layer 1, Intent**

What are you actually trying to achieve? Not the surface task ("write a summary") but the underlying goal ("help my CEO decide quickly"). These are often different, and the difference matters.

A summary intended to help someone decide looks different from a summary intended to brief someone who already decided. Same task, different intent, different output.

*Before you start:* Can you state your actual goal in one sentence?

---

**Layer 2, Context**

What does AI need to know about your situation? Who is involved? What is the background? What constraints apply? What has already been tried?

Context is the layer most people consistently underinvest in. It is also the layer where providing more almost always pays off.

*Before you start:* What does AI not know that would change its answer?

---

**Layer 3, Instructions**

What exactly should AI do? This is distinct from intent. Intent is the goal; instructions are the specific action you want AI to take to achieve it.

"Summarise this document" is an instruction. "Summarise this document in three bullet points, prioritising financial implications, written for a non-specialist reader" is a better one.

*Before you start:* How specific are your instructions? Could a capable human follow them without asking a question?

---

**Layer 4, Examples**

What does good look like? Sometimes the most efficient way to specify a tone, structure, or style is to show AI an example of it, a previous email you wrote, a format you liked, a sample of the style you want.

Examples do more than description. Telling AI to be "warm but professional" is imprecise. Showing it a warm-but-professional email is not.

*Before you start:* Is there an example that would make the target output clearer?

---

**Layer 5, Source material**

What documents, data, notes, or materials should AI work from? AI can read files, contracts, reports, research papers, meeting notes, spreadsheets, and its output will be grounded in what you provide rather than in generalisation.

When you ask AI to help with a specific document or dataset, provide it. Don't describe it, provide it.

*Before you start:* What source materials could improve the specificity and accuracy of the output?

---

**Layer 6, Workspace**

Have you set up a persistent context, a project, a set of standing instructions, a shared background, so you don't have to repeat essential information every time?

For tasks you do repeatedly, a workspace eliminates repetition and builds consistency. Part III is dedicated to this layer.

*Before you start:* Is this a recurring task where a workspace would save significant setup time?

---

**Layer 7, Tools**

What capabilities does AI have access to in this context? Can it search the web? Run calculations? Read uploaded files? Generate images? Access calendar or email?

Knowing which tools are available, and which aren't, shapes what you can reasonably ask for and where you need to verify externally.

*Before you start:* What tools are available? Does this task benefit from any of them?

---

**Layer 8, Workflow**

Is this a single-step task or a multi-step process? Complex work almost always benefits from decomposition: breaking the task into stages, running each stage separately, reviewing and adjusting between stages.

Single-prompt attempts at complex tasks produce mediocre results that are hard to improve. Staged workflows produce better outputs at each stage and make errors easier to catch.

*Before you start:* Is this a single-step task, or should it be broken into stages?

---

**Layer 9, Output**

What should the result look like? Format, length, structure, tone, audience, medium, all of these shape the output and all are specifiable.

Without output specifications, AI defaults to whatever format its training suggests is most common for this type of request. That default is often wrong for your specific situation.

*Before you start:* Have you specified format, length, tone, and structure?

---

**Layer 10, Verification**

How will you check the output? What specifically might be wrong? AI makes errors, factual, logical, and interpretive, with calm confidence. Your verification approach should match the stakes of the task and the risk profile of the content.

Telling AI to flag its own uncertainties is a useful first step. It doesn't replace your review, but it helps.

*Before you start:* How will you verify this output before you use or share it?

---

**Layer 11, Iteration**

How will you use this output as the starting point for the next stage? AI interactions are rarely single exchanges, they are conversations where each response informs the next prompt. Good output at layer 11 becomes input at layer 2 of the next pass.

*Before you start:* Is this a one-shot task, or will you need to iterate? What will the next step be?

---

> **WHY IT WORKS**
>
> The stack is not a checklist to complete in full before every interaction. It is a diagnostic framework. When output is disappointing, the stack tells you where to look. When you're designing a complex task, the stack tells you what to prepare. Most interactions need four or five layers well-activated; a few need all eleven.

---

**The stack in practice**

Here is the same task at two different levels of stack activation:

**Low stack (layers 1, 3 only):**

*"Summarise this meeting."*

Result: A generic summary with equal weight given to all topics discussed. Possibly bulleted, possibly in paragraphs. Pitched at a generic reader. Takes five minutes to edit into something useful.

**High stack (layers 1–5, 9–10):**

*"I need a meeting summary for three people who weren't present: my manager, the client's account manager, and one of our developers. Each person needs to see different things. My manager wants the key decisions and next steps only. The client account manager wants what the client committed to. The developer wants the technical requirements we discussed. The attached transcript is the source. Write three separate summaries, one for each person, no longer than half a page each. Flag anything that seemed unresolved or ambiguous."*

Result: Three targeted summaries, immediately usable, with potential problems flagged.

The difference is not length of prompt. It is activation of the right layers for the task.

---

> **TRY THIS**
>
> Think of an AI task you need to do this week. Write down what layers of the stack you would normally activate, most people use layers 1, 3, and maybe 9 by default. Now consider which additional layers are relevant to this task. What would you add if you invested two more minutes in the setup?

---

**Which layers matter most?**

The research on what makes AI interactions succeed points consistently to three layers as the highest-leverage investments for most people in most tasks:

**Context (Layer 2)** is the most consistently underinvested layer and the one with the highest return. Providing relevant context costs little and changes output significantly.

**Instructions (Layer 3)** are the most frequently underdeveloped layer. Most instructions are too vague. The skill of writing specific, actionable instructions is developed in Chapter 7.

**Verification (Layer 10)** is the most commonly skipped layer. Part VI covers it in depth. Skipping it is also the source of most AI-related professional embarrassment.

---

> **WATCH OUT**
>
> The stack is a mental model, not a procedure. It does not mean you should spend twenty minutes preparing every AI prompt. A quick factual question needs layers 1 and 3, briefly addressed, and that's correct. The stack is useful when you are planning a complex task or diagnosing a poor result, not as mandatory overhead for every interaction.

---

## Chapter 3

### The 7 Questions, Your Portable AI Framework

**A framework you can carry in your head**

The AI Interaction Stack gives you a complete map. But maps aren't always what you need. Sometimes you need a quick checklist, something you can run through in sixty seconds before an important interaction.

The 7 Questions is that checklist.

It is derived from the stack but simplified into seven questions that cover the most important dimensions of any significant AI interaction. It is short enough to memorise. It is structured enough to catch the most common input failures. And it is abstract enough to work on any AI platform, with any model, now or in the future.

<!-- VISUAL: seven-questions -->

---

**The 7 Questions**

Before any significant AI interaction:

**1. What am I trying to achieve?**

State the underlying goal, not just the surface task. "I want my CEO to approve the budget" is more useful than "I want a summary." The goal shapes every other decision.

**2. What does AI need to know?**

What background information, constraints, relationships, or context is essential to getting a good output? What would a capable human assistant need to know before starting this task?

**3. What information can I provide?**

What documents, data, notes, examples, or materials exist that would make AI's output more specific and more accurate? What can you attach or paste in?

**4. What exactly should AI do?**

What is the specific action? Not "help with", do. Write, summarise, extract, compare, analyse, rewrite, draft, plan. Be precise about the verb and the scope.

**5. What should the result look like?**

Format, length, tone, structure, audience, medium. If you do not specify, AI will choose. Specify.

**6. How will I check it?**

What might be wrong? What specifically needs verification before you use or share this output? Are there numbers, dates, names, claims, or recommendations that require checking?

**7. What should happen next?**

Is this one step in a larger process? What will you do with this output? Will it become input to another AI prompt, a document you share, or a decision you make?

---

> **WHY IT WORKS**
>
> Each question addresses a different failure mode. Question 1 catches the wrong goal. Question 2 catches the missing context. Question 3 catches unused resources. Question 4 catches the vague instruction. Question 5 catches the wrong format. Question 6 catches the unverified output. Question 7 catches the single-step tunnel vision.
>
> You can have a perfect answer to six questions and fail on the seventh. The framework is complete by design.

---

**Using the 7 Questions: a worked example**

Sarah needs to create a briefing document on a potential new supplier for her director.

Let's run through the questions:

**Q1, What am I trying to achieve?**
My director needs to decide whether to invite this supplier to a formal tender. I need to give her the information required to make that decision, not a complete company profile.

**Q2, What does AI need to know?**
The decision context (tender shortlist), the supplier's name (TechFlow Ltd), what the tender is for (CRM software implementation), our current system (Salesforce), our rough budget (£80,000), and what factors matter most to us (integration capability, support quality, UK presence).

**Q3, What information can I provide?**
I have the supplier's website, a brochure they sent us, and notes from a call I took with their sales contact last week.

**Q4, What exactly should AI do?**
Create a supplier briefing document using the materials I provide. Organised under the headings: Company Overview, Relevant Experience, Key Capabilities, Potential Risks, Recommended Questions to Ask.

**Q5, What should the result look like?**
One page, maximum. Professional but plain language. My director doesn't have time for anything longer. Bullet points under each heading.

**Q6, How will I check it?**
I'll verify any specific facts against the brochure and my call notes. I'll flag for my director any claims from the supplier that couldn't be independently verified.

**Q7, What should happen next?**
This document will go to my director for her review. If she decides to proceed, I'll use AI to help draft the invitation to tender based on the same materials.

Now Sarah turns this into a prompt:

*"I need a one-page supplier briefing document for my director, who is deciding whether to include TechFlow Ltd in a CRM software tender shortlist. The tender is for an implementation project with a rough budget of £80,000. Our current system is Salesforce.*
*
*The document should be organised under these five headings: Company Overview, Relevant Experience, Key Capabilities, Potential Risks, Recommended Questions to Ask.*
*
*Please work from the materials I am attaching: [brochure], [call notes]. Plain language, bullet points, maximum one page. Flag any claims in the supplier's materials that you cannot independently verify from what I've provided."*

This is a complete interaction. It took about three minutes to prepare using the 7 Questions. It would have taken considerably longer to produce a good result any other way.

---

> **REAL-WORLD EXAMPLE**
>
> James is a recent graduate preparing for a job interview. He runs through the 7 Questions:
>
> Q1, I want to walk into this interview well-prepared, able to give specific answers about why I want this role.
> Q2, The company is Meridian Digital, a mid-size marketing agency. The role is Junior Account Manager. My background is a marketing degree and six months of internship experience. The interview is in two days.
> Q3, I have the job description, the company's website, their LinkedIn page, and a Glassdoor page with recent employee reviews.
> Q4, I want AI to help me prepare for likely interview questions, draft answers to the hardest ones, and identify things about the company I should know.
> Q5, I want a structured prep document: company background summary, ten likely questions with draft answers, and a section on questions I should ask them.
> Q6, I'll verify any company facts against their current website before the interview.
> Q7, I'll use the document to do a practice run the night before.
>
> The resulting prompt takes forty seconds to write. The output he gets is interview prep he can actually use, not generic "tell me about a time you overcame a challenge" boilerplate.

---

**The 7 Questions as a portable card**

The 7 Questions are reproduced as a reference card in Appendix A. You can photograph it, print it, or simply remember it. The goal is that it becomes automatic, something you run through mentally before any AI interaction that matters.

You do not need to answer every question in full every time. For a simple, low-stakes task, three or four seconds on each question is sufficient. For a complex, high-stakes task, a document going to a senior stakeholder, a recommendation with significant consequences, a piece of work that will be published, the full seven questions deserve a full minute each.

---

> **PRO TIP**
>
> Once you have a well-developed answer to the 7 Questions for a recurring task, a weekly report, a client email format, a type of document you produce regularly, save it as a template. The 7 Questions become a workspace setup (Chapter 11). Run once; reuse indefinitely.

---

> **WATCH OUT**
>
> The 7 Questions are a preparation tool, not a rigid protocol. If you find yourself spending ten minutes answering the questions before a thirty-second task, you are misapplying the framework. Use judgment about scale. The questions exist to catch the gaps that consistently cause problems, not to add overhead to interactions that don't need it.

---

## Chapter 4

### How to Talk to an AI (It's Not Google)

**The search engine habit**

Most people's first instinct when using AI is to type a search query. Short. Keyword-heavy. Punchy.

*"best email subject lines"*
*"how to negotiate salary"*
*"presentation tips"*

This works for Google because Google is retrieving existing documents that match your keywords. The shorter and cleaner the query, the more precisely it matches what's out there.

AI tools are not search engines. They are not retrieving existing content. They are generating new content based on what you've given them. The search-engine reflex is the single most common reason people get worse results than they could.

---

**What AI actually does**

Without requiring a technical explanation: an AI language model generates text by working out what words are most likely to follow what came before, based on patterns learned from enormous quantities of text. It is not looking up answers. It is constructing them.

This has three practical implications:

**1. More relevant input, more relevant output.**
A longer, more specific prompt does not confuse AI. It constrains the range of possible responses toward what you actually need. Specificity is an advantage.

**2. A fresh conversation should not be assumed to know your previous work.**
Unless the platform explicitly provides and uses a memory, project, history, or connected-source feature, a new conversation begins without dependable knowledge of who you are, what you've discussed before, or what your preferences are. This is why context must be provided explicitly, and why workspaces (Part III) matter so much for regular users.

**3. AI generates plausible text, not necessarily accurate text.**
AI's training teaches it what good writing looks like in a given context. This means it can generate fluent, confident text on subjects it is wrong about. The confidence in the prose is not correlated with the accuracy of the content. This is the most important habit to build: treating AI output as a draft that requires verification, not a source that can be trusted.

---

> **WHY IT WORKS**
>
> Understanding the generation model, rather than thinking of AI as an oracle or a search engine, changes how you interact with it. It explains why providing examples works (they constrain the generated text toward the style you want). It explains why AI can be confidently wrong (plausibility and accuracy are different things). It explains why asking AI to explain its reasoning helps (it forces more systematic text generation). These are not quirks to work around; they are features of the model to use deliberately.

---

**The conversation, not the query**

AI tools work best as conversations, not as single-query exchanges. The first response is rarely the last one.

This is not because AI needs multiple chances to get things right (though sometimes it does). It is because a conversation allows you to:

- Add context you forgot in the first prompt
- Adjust the output format based on what you see
- Request a deeper dive on one section
- Push back on something that seems wrong
- Ask AI to regenerate with a different constraint

Think of it as briefing a capable but uninformed colleague. The first briefing gets you a first draft. The subsequent conversation refines it. This is normal, efficient, and often faster than trying to write the perfect prompt in one go.

---

**The anatomy of an effective prompt**

Not every prompt needs all of these elements. But a complete prompt for a significant task includes:

```
ROLE (optional but often useful):
Act as a [role] with expertise in [domain].

CONTEXT:
Background information AI needs to know.
Who is involved, what the situation is, what constraints apply.

TASK:
Exactly what you want AI to do.
Use a clear action verb. Be specific.

SOURCE MATERIAL (when relevant):
[Attached document / pasted text / data]

OUTPUT REQUIREMENTS:
Format, length, tone, audience, structure.

VERIFICATION REQUEST (for factual or high-stakes output):
Please flag any claims you are uncertain about,
any assumptions you've made, and any information
I should verify independently.
```

This is not a template to apply rigidly. It is a map of what a complete prompt includes. For quick tasks, you might cover all of this in two sentences. For complex tasks, each element might be a paragraph.

---

> **TRY THIS**
>
> Take a standard query you might type into a search engine and rewrite it as an AI prompt using the anatomy above. You don't need all six elements, pick the three most relevant.
>
> For example:
>
> *Search query:* "how to negotiate salary"
>
> *AI prompt:* "I am about to have a salary negotiation conversation with my manager. I have been in this role for two years, my performance reviews have both been 'exceeds expectations', and I know from a conversation with a colleague that my salary is about 12% below the market rate for this role in London. I am asking for a 15% increase. Help me prepare for this conversation: what arguments are strongest, what objections might I face, and how should I handle the moment when they counter with a lower number? Tone: calm and factual, not aggressive."
>
> Notice the difference in what AI has to work with.

---

**Asking AI to think, not just write**

One of the most underused techniques is asking AI to reason through a problem before producing an answer.

When AI generates text quickly, it sometimes takes the most obvious route. Asking AI to think first, to break down the problem, identify considerations, or outline before drafting, tends to produce more thoughtful, more accurate results.

Phrases that invoke this:
- *"Before answering, think through the main considerations."*
- *"First give me an outline, then draft the full document."*
- *"Walk me through your reasoning."*
- *"What are the main risks or failure points here?"*

This works because it changes the pattern of text generation, the model is working through intermediate steps rather than jumping to a conclusion. You can think of it as asking someone to show their work rather than just hand you an answer.

---

> **PRO TIP**
>
> When you receive an output that is close to what you want but not quite right, do not start again from scratch. Respond to the output with a specific refinement instruction: "That's good but the tone is too formal, can you make it sound more conversational?" or "The summary is accurate but too long, cut it to three bullet points and keep only the most important point in each." Iteration on an existing draft is almost always faster than rewriting.

---

> **WATCH OUT**
>
> AI confidently produces wrong answers. The fluency of AI prose, the fact that it reads well, sounds authoritative, and doesn't hedge, can make it easy to accept without checking. Any output that contains specific facts, numbers, names, dates, quotes, citations, or recommendations deserves verification before you rely on it. Chapter 20 covers verification in detail. For now, adopt the rule: polished prose is not evidence of accuracy.

---

**What Part I has established**

You now have the foundation:

- Generic inputs produce generic outputs because AI fills gaps with averages
- The AI Interaction Stack identifies the eleven layers that determine output quality
- The 7 Questions give you a portable framework for activating the right layers
- A basic AI chat is a generation tool, not a retrieval tool; search and connected-source tools change what it can access, and conversation is the natural mode of interaction

Part II takes each element of a strong interaction and develops it into a skill.

---

# PART II

## Build Better Interactions

*The five chapters in Part II develop the core skills that apply to every AI interaction you will ever have. Each chapter takes one element of the AI Interaction Stack and teaches you to use it deliberately. Together they account for the majority of the quality difference between people who get good results from AI and people who don't.*

---

## Chapter 5

### Give AI a Job, Not Just a Question

**The question versus the job**

There is a meaningful difference between asking AI a question and giving AI a job.

A question invites a response. A job assigns a task with a clear deliverable, a scope, and implicit quality criteria.

*Question:* "What do I need to know about redundancy letters?"
*Job:* "You are an HR communications specialist. Draft a redundancy letter for a member of our sales team who has been with the company for three years. The reason is restructuring, not performance. Tone: respectful and clear. The letter must include: confirmation of the decision, notice period (one month), details of the settlement package (to be inserted), available support resources, and the process for appeal. UK employment law applies."

The question gets you information about redundancy letters, a textbook answer pitched at an anonymous reader. The job gets you a document you can actually edit and use.

---

> **WHY IT WORKS**
>
> Role assignment and job framing do not change what AI "knows." They change the frame through which AI selects and structures what it produces. A prompt that says "you are an experienced financial analyst" causes AI to draw more heavily from the patterns associated with financial analysis, more technical vocabulary, more rigorous structure, more appropriate caution. A prompt that specifies a deliverable (a letter, a report, an agenda) constrains the format. Together, role and job framing channel AI's generation toward something more precisely useful.

---

**The Before → Better → Best: giving AI a job**

---

*BEFORE (the vague question)*

*"What should I include in a client proposal?"*

What AI produces: A generic list of proposal sections that any business book might contain. Executive summary, scope, timeline, pricing, terms. Correct. Applicable to no one's specific situation.

*Why it's weak:* AI has no information about the client, the industry, the type of work, the relationship, or what distinguishes this proposal from a hundred others.

---

*BETTER (the specific task)*

*"Write an outline for a proposal for a digital marketing retainer, targeting a mid-size UK retail company. The agency specialises in SEO and paid social. The prospect has expressed interest but is also talking to two other agencies. The proposal needs to address: our methodology, relevant case studies, pricing structure (monthly retainer, tiered options), and what makes us different."*

What AI produces: A structured outline specific to this type of proposal with relevant sections and brief notes on what each should contain.

*What improved:* AI now has the industry, the type of work, the competitive context, and the key elements to address.

---

*BEST (role + job + context + output specifications)*

*"You are a senior account director at a boutique UK digital marketing agency. You are writing a proposal for a monthly SEO and paid social retainer for Thornton's, a mid-size UK garden centre chain with 12 locations. The prospect is also considering two larger agencies. The decision maker is the Marketing Director, who has told us she values transparency and long-term partnerships over flashy pitches.*

*Write a proposal outline that: leads with their specific situation rather than our credentials; demonstrates understanding of the garden centre sector and its seasonal patterns; presents three pricing tiers (Starter / Growth / Full Service); and ends with a section on how we measure success and report to clients.*

*Structure: section headings with one-sentence notes on content. Not the full proposal, the outline I will then develop. Max two pages when written up."*

What AI produces: A highly specific outline that could only work for this client, this agency, and this competitive context. The structure respects the decision maker's stated values. The pricing presentation is appropriately tiered. The language is right for the relationship.

*WHAT CHANGED?*

| What was added | Why it mattered |
|---|---|
| Role: senior account director | Contextualised the voice and level of expertise |
| Specific client name and context | Anchored content in a real situation |
| Decision maker's stated values | Shaped the strategic angle of the proposal |
| Sector knowledge requirement | Prompted sector-relevant thinking |
| Clear deliverable | "Outline I will develop" prevented over-generation |
| Output constraints | Kept length appropriate |

---

**Choosing the right role**

Role assignment is optional but often valuable. The rule of thumb: assign a role when the task has a domain, a voice, or a level of expertise that you want AI to reflect.

Useful role frames:
- Professional identity: *"You are an experienced employment solicitor"*
- Expertise level: *"You are a secondary school science teacher"*
- Perspective: *"You are a sceptical reader encountering this argument for the first time"*
- Function: *"You are a copy editor reviewing this draft"*

Role frames that don't help much: overly elaborate backstories, fictional identities with no relevance to the task, vague superlatives ("you are the world's greatest expert"). Keep roles grounded in what kind of expertise or perspective would actually be useful for this task.

---

**Assigning a specific, actionable job**

The instruction "help me with X" is not a job. It is an open invitation that AI will answer with whatever seems most plausibly helpful, which is usually the most generic interpretation of the task.

A job has:
- A clear action verb: write, summarise, extract, compare, identify, structure, rewrite, analyse
- A clear deliverable: a document, a list, a table, a set of questions, a draft
- A clear scope: this document, these notes, this specific situation

Compare:
- *"Help me with my CV"* → AI will ask what kind of help or produce something generic
- *"Rewrite the experience section of my CV to emphasise project management and stakeholder communication, using active verbs, targeting senior operations manager roles in the financial services sector"* → AI has a job

---

> **TRY THIS**
>
> Write down a task you regularly do that takes more than an hour. Now describe it as a job for AI using this structure:
>
> *[Role, if relevant]. [Action verb] [specific deliverable] using [source material]. The output should [format/length/tone specifications]. The intended reader is [audience]. Do not [explicit exclusion if needed].*
>
> Notice how much this forces you to clarify what you actually want before AI starts.

---

> **WATCH OUT**
>
> Assigning an expert role does not make AI's output more accurate. It may make it more fluently confident, which, as noted in Chapter 4, can be more convincing and equally wrong. Role framing improves format, voice, and structure. It does not improve factual accuracy. Verify subject-matter claims regardless of the role you assigned.

---

## Chapter 6

### Context Is Everything

**The context gap**

Here is the practical starting point for most AI interactions: unless you provide relevant context or explicitly enable a persistence feature, AI should be treated as knowing nothing dependable about you, your work, your organisation, your history with this client, your professional constraints, or the specific situation you are dealing with.

You know all of these things. They seem obvious. So you don't mention them.

This is the context gap, the difference between what AI needs to know to give you a genuinely useful answer, and what you actually provide. It is the single most valuable gap to close.

---

**What counts as context**

Context is not just background information. It is any fact about your situation that would change how a knowledgeable person would approach the task. It includes:

**Situational context**, What is happening? What is the history? Why does this matter now?

**Audience context**, Who is going to read, use, or act on this output? What do they know? What do they need? What are their constraints?

**Relationship context**, What is the relationship between parties? Long-standing client? New contact? Internal colleague? Adversarial negotiation?

**Constraint context**, What must the output not include? What word count, format, or style requirements apply? What legal, regulatory, or policy constraints apply?

**Resource context**, What documents, data, or previous work is relevant? What has already been tried?

**Goal context**, What does success look like? What decision will this output inform? What action will it prompt?

---

> **REAL-WORLD EXAMPLE**
>
> David runs a small consulting firm. He is writing a proposal for a client renewal and asks AI to help draft the pricing section.
>
> Without context: AI produces a generic template for presenting consulting fees, day rates, retainer structures, and payment terms that could apply to any consulting firm anywhere.
>
> With context: David tells AI that this client has been with the firm for four years, has three times mentioned "feeling nickel-and-dimed" by itemised billing, is a family business where the owner and CFO are the same person, and that David wants to move to a monthly retainer to create predictable revenue on both sides. He also notes the client's previous annual spend was around £42,000.
>
> The output AI produces with this context is a specifically targeted pricing section that addresses the client's stated frustration, proposes a retainer at a price point consistent with their history, and frames the retainer in terms of what the client gets (predictability, priority access, no surprises) rather than what David gets. It is a usable draft. The generic version was not.
>
> The difference was entirely in the context David provided.

---

**The context test**

A useful diagnostic: before sending a prompt, ask yourself:

*"If I had just hired a very good human assistant who was new to this job, what would they need to know before I asked them to do this?"*

That question surfaces most of the context you are probably omitting. A good assistant would ask about the audience, the history, the constraints, the goal, and the format before starting work. Providing that context in your prompt removes the need for them to ask, and removes the iterations required when AI guesses wrong.

---

**The Before → Better → Best: context**

*BEFORE*

*"Write an email to our supplier about a late delivery."*

Output: A generic, somewhat formal complaint email about a late delivery with placeholder information. Polite but weightless.

---

*BETTER*

*"Write an email to our supplier, BuildRight Ltd, about a delivery that is now 12 days late. The order was for 500 units of packaging material needed for a Christmas promotional campaign. The delay means we cannot start production on time and we risk missing the campaign window."*

Output: A specific email that references the order type, the operational impact, and the time pressure. Usable with minor edits.

---

*BEST*

*"Write an email to BuildRight Ltd, our packaging supplier of five years. Our contact is James Thornton in their sales team. The delivery of 500 units of promotional packaging (order number BRTX-2241) is now 12 days late. This delivery was critical for our Christmas campaign, production was due to start on Monday and we have an external print deadline of 18th November.*

*We do not want to damage the relationship, which has been excellent until this point. The tone should be: firm and clear about the business impact, but not accusatory. We want two things: a confirmed delivery date in writing and an explanation of what happened.*

*Do not threaten to cancel the order or use legal language at this stage."*

Output: An email that reflects the history of the relationship, is specific about the business impact and timeline, makes two clear requests, and observes the explicit constraint about not escalating. Might be sent with no editing.

*WHAT CHANGED?*

| Context added | Why it mattered |
|---|---|
| Five-year relationship | Shaped the non-accusatory tone |
| Named contact | Made the email personal |
| Order number | Made the reference specific and professional |
| Production deadline | Explained why timing matters so much |
| Print deadline date | Created concrete urgency without exaggeration |
| Two specific requests | Focused the email on clear outcomes |
| Explicit constraint (no legal language) | Prevented escalation AI might otherwise include |

---

**Providing constraint context**

Constraints are particularly easy to omit because they feel obvious to you. "Obviously I can't mention the legal proceedings." "Obviously I shouldn't mention the budget number." "Obviously the tone needs to be formal."

These are obvious to you. They are invisible to AI. State every constraint that would make the output unusable if violated.

Useful constraint phrasing:
- *"Do not include [X]."*
- *"This cannot mention [X] for legal reasons."*
- *"The tone must not suggest [X], this would damage the relationship."*
- *"UK spelling and law applies throughout."*
- *"This will be reviewed by [X] so should not contain [Y]."*

---

> **PRO TIP**
>
> For recurring tasks where the context is always the same, you don't need to retype it every time. Chapter 11 covers persistent instructions, a way of establishing your standard context once so it applies automatically to every conversation. The context you would type for every client email, every report, every team communication becomes a standing brief that AI carries forward.

---

> **WATCH OUT**
>
> Providing irrelevant context can dilute the output as much as providing too little. If you paste a twenty-page document when AI only needs three paragraphs, you risk getting a response that is unfocused across all twenty pages. Context should be relevant to this task. If in doubt, introduce the document and tell AI which section matters: *"I'm attaching our full company handbook, but for this task only the redundancy policy section (pages 14-17) is relevant."*

---

## Chapter 7

### Instructions That Actually Work

**Why most instructions are too vague**

Instructions are where most users put most of their effort, and still get disappointing results. The reason is usually not that the instructions are wrong. It is that they are underspecified.

*"Make it more professional"* is an instruction. But "more professional" in what dimension? More formal vocabulary? Shorter sentences? No contractions? Different paragraph structure? Fewer qualifications? More precise language?

AI will choose. And it will choose the version of "more professional" that appears most frequently in its training data for this type of text, which may not be what you meant at all.

Effective instructions are specific enough that a capable human could follow them without asking a clarifying question.

---

**The specificity test**

Before sending an instruction, ask: *"Could two different people interpret this differently?"*

If yes, it is underspecified.

*"Make it shorter"* → How much shorter? Half? A third? A specific word count?
*"Make it more engaging"* → More engaging how? More conversational? Shorter paragraphs? An opening question? Personal examples?
*"Make it suitable for our audience"* → Who is the audience and what do they need?
*"Improve the structure"* → More headings? Different order? Remove sections? Add an introduction?

Each of these pairs shows an instruction that fails the specificity test, and the questions that reveal what was actually meant. Answer those questions in the instruction.

---

**Positive and negative instructions**

Instructions can specify what to do (positive) or what not to do (negative). Both are important. Most people use only positive instructions and then wonder why the output contains things they didn't want.

Negative instructions are particularly useful for:
- Tone and register: *"Do not use exclamation marks. Do not use filler phrases like 'I hope this finds you well.'"*
- Content constraints: *"Do not mention the merger, this is not public."*
- Style: *"Do not use bullet points, this should be flowing prose."*
- Claims: *"Do not make specific claims about delivery times, these vary by region."*

A well-instructed prompt often includes both: *"Write this in a direct, confident tone. Do not use passive voice. Do not hedge claims with phrases like 'it could be argued' or 'some might say.'"*

---

**Instruction types and when to use them**

Different tasks benefit from different instruction types:

**Format instructions**, What structure should the output take?
*"Use a numbered list." / "Present this as a table with columns for X, Y, Z." / "Use three short paragraphs, no headings." / "One page maximum, A4, with a heading and four bullet points."*

**Tone instructions**, How should it sound?
*"Direct and professional." / "Warm but concise." / "Technical but accessible, assume the reader has a science degree but is not a specialist in this field." / "In the voice of the existing document I'm attaching."*

**Priority instructions**, What matters most?
*"Lead with the cost saving, not the process improvement." / "The most important point must be in the first sentence." / "The client's concern about timeline is more important than the features list, address it first."*

**Exclusion instructions**, What to leave out?
*"Do not include implementation details, this is for a non-technical audience." / "Exclude anything older than 2024, the reader will already know the history." / "Do not include a summary, the reader will read the whole thing."*

**Role instructions**, From whose perspective?
*"Write this as if the reader has never heard of our company." / "The reader is a sceptic, address their likely objections before they ask."*

---

**The Before → Better → Best: instructions**

*BEFORE*

*"Rewrite this paragraph to make it better."*

[Paragraph: "Our team has extensive experience in the delivery of complex technology projects. We have worked with a wide range of clients across multiple sectors and have a proven track record of delivering projects on time and on budget."]

Output: AI produces a slightly more polished version of the same paragraph. Same ideas, slightly varied vocabulary. The reader would not notice a meaningful difference.

---

*BETTER*

*"Rewrite this paragraph to remove clichés and make it more specific and credible. Replace phrases like 'extensive experience' and 'proven track record' with concrete language."*

Output: AI produces a version that avoids the worst clichés and becomes more specific in tone, though it invents specifics it doesn't have.

---

*BEST*

*"Rewrite this paragraph for inclusion in a proposal to a housing association considering a digital transformation project. The audience is a director who has seen many similar proposals and is sceptical of vague claims.*

*Instructions:*
*Remove all clichés: 'extensive experience', 'wide range', 'proven track record', 'multiple sectors' must all go.*
*Replace vague claims with specific patterns of evidence. I will provide specifics in a moment, for now, leave [BRACKETS] as placeholders for: number of years in the sector, number of completed projects, one specific client sector, and one specific result we achieved.*
*First sentence should establish relevance to housing sector specifically, not generic technology experience.*
*Maximum two sentences. Punchy, not promotional."*

Output: A tightly constructed two-sentence paragraph that is specific in structure, leaves appropriate placeholders, and is pitched correctly at the sceptical reader.

*WHAT CHANGED?*

| Instruction element | Why it mattered |
|---|---|
| Audience specified | Shaped the pitch level and scepticism antidote |
| Banned phrases listed explicitly | Prevented the most common failure |
| Placeholder pattern | Kept AI honest about missing specifics |
| Structural requirement (first sentence) | Prevented the generic opener |
| Length constraint (two sentences) | Forced concision |
| Tone instruction (not promotional) | Prevented the default enthusiastic pitch |

---

> **TRY THIS**
>
> Take the last AI output you were dissatisfied with. Identify one thing that was wrong with it, too long, wrong tone, too generic, incorrect emphasis, wrong format.
>
> Write a follow-up instruction that specifically addresses that one thing, using the specificity test: could two people interpret this instruction differently?
>
> If yes, refine it until the answer is no.

---

> **WATCH OUT**
>
> Instructions that conflict produce confused output. If you say "be brief and comprehensive," "be formal but conversational," or "be specific but applicable to all situations," AI will attempt to honour all instructions simultaneously and usually succeed at none of them. When instructions conflict, decide which takes priority and say so: *"Be brief, prioritise this over comprehensiveness if necessary."*

---

## Chapter 8

### Examples Change Everything

**Showing versus telling**

There are two ways to specify what you want from AI. You can describe it, or you can demonstrate it.

Describing works for many things. But when tone, format, or style is what you care about, demonstrating is almost always more effective.

This is because language about language is inherently imprecise. "Warm but professional" means something different to you than it does to AI. "Clear and engaging" is interpreted through thousands of examples in AI's training data, most of which are not exactly what you meant. The gap between your description and AI's interpretation is where most style failures live.

An example collapses that gap. Instead of asking AI to match your description of a style, you are showing it the style and asking it to match that.

---

**Types of examples**

Examples can take several forms:

**Tone examples**
A piece of your own writing, or a piece of writing in the voice you want. "Write in the same tone as this email I wrote last year" or "match the style of this example I'm pasting in."

**Format examples**
A previous document in the format you need. "Use the same structure as this report section." "Produce output that looks like this."

**Quality standard examples**
A high-quality output you want to match or improve on. "This is an example of the level of specificity I want."

**Negative examples**
Something you don't want. "Do not write like this" is sometimes as effective as "write like this."

---

> **WHY IT WORKS**
>
> Providing examples is what AI researchers call "few-shot prompting", giving AI a small number of examples from which to infer the desired pattern. The technical reason it works is that examples constrain the generation space toward outputs with similar characteristics: similar vocabulary choices, similar sentence length, similar structural decisions. Your description of "professional" is abstract; an example of it is concrete.

---

**The Before → Better → Best: examples**

The scenario: Margaret wants a weekly AI-generated summary of news relevant to her industry (sustainable packaging) to send to her team. She wants it to sound as if she wrote it, not AI.

*BEFORE*

*"Write a summary of this week's sustainability news for my team."*

Output: A formal, comprehensive news summary. Heavy paragraphs. AI-standard prose. Margaret would have to rewrite it entirely before it sounds like her.

---

*BETTER*

*"Write a summary of this week's sustainability packaging news for my team. Tone: conversational, direct, not overly formal."*

Output: Less formal, but still not quite right. "Conversational" is interpreted differently by different people, and AI doesn't know what Margaret sounds like.

---

*BEST*

*"I write a weekly news summary for my team of 8. Here is an example of one from three months ago that captured the tone exactly right:*

*[EXAMPLE SUMMARY]*

*'Three things from this week:*
*1. The EU is tightening its position on recycled content claims, this matters for our German clients more than anywhere else. Worth watching.*
*2. Paperboard prices stabilised in October after six months of increases. Our procurement team will already know this, but the sector analysis I've linked to is good background.*
*3. Maersk announced a new bio-methanol shipping route. Too early to know if this is real progress or PR. I'll share more when I know more.'*

*Write this week's summary in the same format and voice. Source material I'm attaching covers: [pasted or uploaded articles]. Keep it to three items unless something genuinely warrants a fourth."*

Output: A summary that reads like it could have been written by Margaret, same three-item structure, same direct tone, same characteristic qualification ("too early to know"). She edits two words and sends it.

*WHAT CHANGED?*

| What was added | Why it mattered |
|---|---|
| Example of actual past output | Gave AI a concrete target instead of abstract description |
| Format from example | Three numbered items, short, no preamble |
| Voice characteristics from example | Opinionated, direct, honest about uncertainty |
| Source material provided | Grounded in real content rather than general knowledge |
| Constraint on length | Prevented overgeneration |

---

**Using your own writing as an example**

One of the most practical applications of example-giving is using your own previous writing to teach AI your voice. This is particularly useful for:

- Regular communications: weekly updates, team emails, client newsletters
- Documents with a house style: reports, proposals in a format you've established
- Personal correspondence: emails where you want AI to draft and you want it to sound like you

The method: provide two or three examples of your writing in the relevant genre, and ask AI to match the style. Longer examples give AI more to work from. If you have a document that perfectly captures your voice or style, use that as the primary reference.

> **PRO TIP**
>
> If you save a "style reference" document in your AI workspace (Chapter 11), you don't need to paste examples into every prompt. You reference the document once in your standing instructions and it's available for every subsequent interaction.

---

**When not to use examples**

Examples constrain AI toward the example. This is usually what you want, but not always.

If you want AI to be creative, novel, or to produce something better than your existing examples, providing examples can limit the output. In those cases, describe the qualities you want and explicitly say: *"Feel free to go beyond this starting point."*

Similarly: if the examples you have are not actually that good, AI may faithfully replicate their weaknesses. Use examples you would genuinely like to match.

---

> **WATCH OUT**
>
> Examples are most effective for style and format. They are less effective for accuracy. Providing an example of a data table you want does not teach AI to fill it with correct data. You are specifying format, not content. Verify content as normal regardless of how good the format looks.

---

## Chapter 9

### Control the Output

**The output problem**

You have provided excellent context, a clear job description, specific instructions, and a strong example. AI produces a response.

It is too long.
It is the wrong format.
The most important point is buried in paragraph four.
It uses a slightly different structure than you specified.

This happens because output defaults are baked into AI's training. Without explicit specifications, AI produces the type, length, and format of output most commonly associated with your type of request. That default is often close but rarely exactly right.

Controlling output is the final step in building an effective interaction, specifying not just what to produce, but what the result should look like when it arrives.

---

**The five output dimensions**

Five dimensions of output are almost always worth specifying for significant tasks:

**1. Length**
The most commonly underspecified dimension. How long? Not "short", how many words, sentences, bullet points, or paragraphs? "A one-page briefing," "a three-bullet summary," "a maximum of 150 words," "five sentences", these are unambiguous. "Brief" is not.

**2. Format**
How should the information be structured? Prose paragraphs, numbered list, bullet points, table, structured document with headings, slide deck content, script, dialogue? Different formats serve different purposes. The format should match how the reader will use the output.

**3. Structure**
If the output has sections or parts, what are they and in what order? Specifying structure prevents AI from inventing a structure that may not serve your purpose. "The document should have four sections: Background, Key Findings, Recommendation, Next Steps" is better than allowing AI to choose.

**4. Tone**
How should it sound? The vocabulary level, the degree of formality, the use of first person or third person, the amount of hedging or qualification, the presence or absence of technical language, all are specifiable. Use examples when description alone is insufficient (Chapter 8).

**5. Audience**
Who will read this? What do they know? What do they need? The same information presented to a technical expert and a first-time reader should be substantially different. Specifying audience tells AI how to calibrate complexity, assumed knowledge, and depth of explanation.

---

> **WHY IT WORKS**
>
> AI has no inherent preference for one format over another. It defaults to the format most common in its training data for a given type of request. Explicit output specifications don't constrain AI in ways that affect quality, they redirect its generation toward the format you need. Specifying output is not about limiting AI; it is about using what AI has already generated to its best effect for your purpose.

---

**The Before → Better → Best: output control**

The scenario: James needs a summary of a forty-page government report on graduate employment for a blog post he is writing.

*BEFORE*

*"Summarise this report on graduate employment."*

Output: Six paragraphs, dense, comprehensive, presenting findings in the order they appear in the report. Difficult to read. Not formatted for a blog audience. James would have to restructure it entirely.

---

*BETTER*

*"Summarise the key findings of this report for a general audience interested in graduate careers. Keep it short and clear."*

Output: Shorter, more readable, but still not structured for a blog post. "Short and clear" was under-specified.

---

*BEST*

*"Summarise the key findings of this graduate employment report for a blog post aimed at final-year students. They are interested in practical takeaways about their job prospects, not policy analysis.*

*Format: Three sections with short headings:*
*1. What the data says (two to three bullet points with the most significant statistics)*
*2. What this means for you (two to three practical implications in plain language)*
*3. What to do about it (one or two concrete suggestions)*

*Maximum 300 words total. Active voice. No jargon. Read level: a confident 20-year-old who reads the Guardian.*

*Do not include methodology, policy recommendations, or anything that doesn't directly affect a job-seeking student."*

Output: A structured, audience-appropriate blog summary. The sections are clear, the language is right for the audience, and the length is correct. James reads it once, adds a paragraph of his own at the end, and posts it.

*WHAT CHANGED?*

| Output specification | Why it mattered |
|---|---|
| Three named sections | Imposed a usable structure |
| Bullet count per section | Prevented overgeneration |
| Maximum 300 words | Made length unambiguous |
| "Active voice" | Improved readability |
| Reading level specified | Calibrated vocabulary and complexity |
| Explicit exclusion list | Prevented irrelevant policy content |

---

**Specifying format: a practical reference**

When you need:

| This | Say |
|---|---|
| A concise summary | "Three to five bullet points, one sentence each" |
| A structured document | List the sections explicitly with brief descriptions |
| A table | "Present this as a table with columns for [X], [Y], [Z]" |
| Prose, not bullet points | "Write in flowing paragraphs, no bullet points" |
| An email | "Subject line + body, professional tone, under 150 words" |
| An outline | "Numbered outline with second-level sub-points" |
| A list | "Numbered list, [n] items, no more" |
| A one-pager | "One A4 page of content: heading, three sections" |

---

**Controlling output mid-conversation**

Output control is not only an upfront specification. It is also a live tool in conversation.

When the output is close but not quite right, you can redirect it with a specific instruction:

- *"Good structure but too long, cut it by half."*
- *"Remove the executive summary section, I don't need it."*
- *"This is in bullet points, rewrite as prose paragraphs."*
- *"The third point is the most important, lead with it."*
- *"Change the tone, this reads too formally for the audience."*

Each of these is a specific, actionable correction. AI will act on them precisely. The instruction "make it better" is not a specific correction. Be specific about the dimension you want changed.

---

> **TRY THIS**
>
> For your next significant AI task, write out your output specification separately before you write the main prompt. Answer these five questions:
>
> 1. How long?
> 2. What format?
> 3. What structure?
> 4. What tone?
> 5. Who is the audience?
>
> Then build those answers into the prompt. Notice whether the first output is closer to what you need before you have to ask for revisions.

---

> **WATCH OUT**
>
> Excessive output specification can overconstrain the response. If you specify every sentence, paragraph, and word choice, you are writing the document yourself and asking AI to type it. Specify the frame, length, format, structure, tone, audience, and leave AI to fill it in appropriately. The goal is a usable first draft, not a perfect document that required more work to specify than it would have taken to write.

---

**What Part II has established**

You can now build an effective AI interaction from the ground up:

- Give AI a clear role and a specific job, not a vague question
- Provide the context that closes the gap between what AI assumes and what you actually need
- Write instructions specific enough that a capable person could follow them without asking clarifying questions
- Show AI examples when style, format, or tone matter
- Specify the output in terms of length, format, structure, tone, and audience

Part III moves from individual interactions to the environment in which they happen, and the significant gains available from building that environment deliberately.
