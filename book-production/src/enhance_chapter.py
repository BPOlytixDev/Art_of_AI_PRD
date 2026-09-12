"""
enhance_chapter.py
==================
Single-chapter PDF enhancer for The Art of AI — Book 1.

Usage
-----
    python enhance_chapter.py <input_chapter.pdf> <output.pdf> <chapter_num>

Or import build_chapter() from this module and call it directly from
batch_enhance.py.

How it works
------------
1.  Reads the input chapter PDF with pypdf to extract the text content.
2.  Classifies content blocks (comparisons, frameworks, examples, callouts)
    using the editorial decision rules in AGENTS.md §6.2.
3.  Builds a ReportLab Platypus story using components from components.py
    plus any chapter-specific Flowable subclasses defined here.
4.  Writes the enhanced PDF to the output path.

Constraints
-----------
- Never alters manuscript text.
- Never adds invented content.
- Only Helvetica family fonts (built-in, no embedding).
- All colours from the palette in components.py.
- KeepTogether() wraps every SectionDivider + first Paragraph pair.
- Author: Eleanor Mercer everywhere.

Install
-------
    pip install reportlab pypdf --break-system-packages
"""

from __future__ import annotations

import sys
from pathlib import Path

# ── ReportLab imports ──────────────────────────────────────────────────────────
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

# ── Shared components ──────────────────────────────────────────────────────────
from components import (
    CONTENT_W,
    GOLD,
    LIGHT_GRAY,
    MARGIN,
    MID_GRAY,
    NAVY,
    RED_ACCENT,
    SOFT_GOLD,
    SOFT_TEAL,
    TEAL,
    WHITE,
    ChapterHero,
    FlowDiagram,
    IconCardRow,
    KeyTakeawayBanner,
    NoteBox,
    OrbitalWheel,
    PageFooter,
    S,
    SectionDivider,
    SplitPanel,
    TryThisBox,
    WatchOutBox,
    styled_table,
)

BOOK_TITLE = "The Art of AI"
AUTHOR     = "Eleanor Mercer"

# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER REGISTRY
# ══════════════════════════════════════════════════════════════════════════════
# Maps chapter_num (int) → function that builds and returns a Platypus story.
# Each function receives (W: float) → list[Flowable].
#
# Add a new entry here for every chapter you implement.
# If a chapter has no registry entry, build_chapter() falls back to a
# plain-text passthrough that renders body paragraphs with no infographics.

_CHAPTER_BUILDERS: dict[int, callable] = {}


def register(chapter_num: int):
    """Decorator: @register(1) def _ch1(W): ..."""
    def decorator(fn):
        _CHAPTER_BUILDERS[chapter_num] = fn
        return fn
    return decorator


# ══════════════════════════════════════════════════════════════════════════════
# CHAPTER 1 — Why AI Gives You Generic Answers (and How to Change That)
# ══════════════════════════════════════════════════════════════════════════════

@register(1)
def _chapter_1(W: float):
    """
    Content analysis → design decisions
    ─────────────────────────────────────────────────────────────────────────
    5 complaint quotes          → teal grid table
    Core argument sentence      → KeyTakeawayBanner
    Slot machine metaphor       → SplitPanel (slot machine vs intentional)
    "Why it works" explainer    → NoteBox
    3 input failure types       → IconCardRow (3 cards)
    Sarah's email example       → SplitPanel (before/after)
    5-item framework            → OrbitalWheel + numbered table
    "Try This" exercise         → TryThisBox
    "Watch Out" warning         → WatchOutBox
    All section headings        → SectionDivider
    Chapter title               → ChapterHero
    Pure narrative paragraphs   → STYLE_BODY only — no visual added
    ─────────────────────────────────────────────────────────────────────────
    Visual count: 5 infographics (chapter ~6 pages — upper end, justified by
    density of framework content in this opening chapter).
    """
    from reportlab.platypus import Flowable

    # ── Chapter-specific infographics ──────────────────────────────────────

    class _SlotMachine(Flowable):
        """Split panel: Slot Machine approach vs Intentional approach."""
        def __init__(self, w):
            Flowable.__init__(self)
            self.w = w
            self.h = 2.6 * inch

        def draw(self):
            import math as _math
            c = self.canv
            w, h = self.w, self.h
            half = w / 2 - 8

            # LEFT: slot machine
            c.setFillColor(colors.HexColor("#FFF0F0"))
            c.roundRect(0, 0, half, h, 8, fill=1, stroke=0)
            c.setStrokeColor(RED_ACCENT)
            c.setLineWidth(1.5)
            c.roundRect(0, 0, half, h, 8, fill=0, stroke=1)
            c.setFillColor(RED_ACCENT)
            c.setFont("Helvetica-Bold", 10)
            c.drawCentredString(half / 2, h - 20, "\u274c  SLOT MACHINE APPROACH")

            # Slot-machine icon
            sx, sy, sw, sh = half / 2 - 28, h - 90, 56, 52
            c.setFillColor(colors.HexColor("#DDDDDD"))
            c.roundRect(sx, sy, sw, sh, 5, fill=1, stroke=0)
            c.setFillColor(colors.HexColor("#BBBBBB"))
            c.rect(sx + 6, sy + 8, sw - 12, sh - 20, fill=1, stroke=0)
            c.setFillColor(WHITE)
            for xi in [sx + 8, sx + 22, sx + 36]:
                c.rect(xi, sy + 10, 12, sh - 24, fill=1, stroke=0)
            c.setFillColor(RED_ACCENT)
            c.setFont("Helvetica-Bold", 9)
            for xi in [sx + 10, sx + 24, sx + 38]:
                c.drawString(xi, sy + 18, "?")

            c.setFont("Helvetica", 9)
            c.setFillColor(colors.HexColor("#555555"))
            by = h - 108
            for b in ["Vague request", "Hope for the best",
                       "Random results", "Mostly disappointing"]:
                c.drawString(12, by, f"\u2022 {b}")
                by -= 15

            # RIGHT: intentional
            rx = half + 16
            c.setFillColor(SOFT_TEAL)
            c.roundRect(rx, 0, half, h, 8, fill=1, stroke=0)
            c.setStrokeColor(TEAL)
            c.setLineWidth(1.5)
            c.roundRect(rx, 0, half, h, 8, fill=0, stroke=1)
            c.setFillColor(TEAL)
            c.setFont("Helvetica-Bold", 10)
            c.drawCentredString(rx + half / 2, h - 20, "\u2713  INTENTIONAL APPROACH")

            # Bullseye icon
            tcx, tcy = rx + half / 2, h - 68
            for r, col in [(24, SOFT_TEAL), (17, colors.HexColor("#9EE4DA")),
                           (10, TEAL), (4, NAVY)]:
                c.setFillColor(col)
                c.setStrokeColor(WHITE)
                c.setLineWidth(1)
                c.circle(tcx, tcy, r, fill=1, stroke=1)

            c.setFont("Helvetica", 9)
            c.setFillColor(colors.HexColor("#1A3A34"))
            by = h - 108
            for b in ["Clear job specified", "Context provided",
                       "Predictable output", "Consistent results"]:
                c.drawString(rx + 12, by, f"\u2022 {b}")
                by -= 15

            # VS badge
            bx, bby = half + 1, h / 2 - 14
            c.setFillColor(GOLD)
            c.circle(bx + 7, bby + 14, 14, fill=1, stroke=0)
            c.setFillColor(NAVY)
            c.setFont("Helvetica-Bold", 9)
            c.drawCentredString(bx + 7, bby + 10, "VS")

        def wrap(self, *args):
            return self.w, self.h

    class _BeforeAfter(Flowable):
        """Split panel: Sarah's email — before vs after."""
        def __init__(self, w):
            Flowable.__init__(self)
            self.w = w
            self.h = 2.2 * inch

        def draw(self):
            c = self.canv
            w, h = self.w, self.h
            half = w / 2 - 6

            # BEFORE
            c.setFillColor(colors.HexColor("#FFF0F0"))
            c.roundRect(0, 0, half, h, 8, fill=1, stroke=0)
            c.setFillColor(RED_ACCENT)
            c.roundRect(0, h - 30, half, 30, 8, fill=1, stroke=0)
            c.rect(0, h - 22, half, 14, fill=1, stroke=0)
            c.setFillColor(WHITE)
            c.setFont("Helvetica-Bold", 10)
            c.drawCentredString(half / 2, h - 20, "BEFORE  \u2717")

            c.setFillColor(colors.HexColor("#CC3333"))
            c.roundRect(8, 8, half - 16, h - 46, 5, fill=1, stroke=0)
            c.setFillColor(WHITE)
            c.setFont("Helvetica-Oblique", 9)
            c.drawCentredString(half / 2, h - 52, "\u201cWrite a follow-up email")
            c.drawCentredString(half / 2, h - 65, "after a business meeting.\u201d")
            c.setFont("Helvetica", 8)
            c.setFillColor(colors.HexColor("#FFAAAA"))
            iy = h - 88
            for iss in ["No recipient info", "No meeting details",
                        "No goal specified", "No tone guidance"]:
                c.drawCentredString(half / 2, iy, f"\u2717  {iss}")
                iy -= 14

            c.setFillColor(colors.HexColor("#FFDDDD"))
            c.roundRect(8, 8, half - 16, 36, 5, fill=1, stroke=0)
            c.setFillColor(RED_ACCENT)
            c.setFont("Helvetica-Bold", 8)
            c.drawCentredString(half / 2, 34, "Output:")
            c.setFont("Helvetica", 7.5)
            c.setFillColor(colors.HexColor("#993333"))
            c.drawCentredString(half / 2, 20, "Generic template with")
            c.drawCentredString(half / 2, 9, "[placeholders] \u2014 unusable")

            # AFTER
            rx = half + 12
            c.setFillColor(SOFT_TEAL)
            c.roundRect(rx, 0, half, h, 8, fill=1, stroke=0)
            c.setFillColor(TEAL)
            c.roundRect(rx, h - 30, half, 30, 8, fill=1, stroke=0)
            c.rect(rx, h - 22, half, 14, fill=1, stroke=0)
            c.setFillColor(WHITE)
            c.setFont("Helvetica-Bold", 10)
            c.drawCentredString(rx + half / 2, h - 20, "AFTER  \u2713")

            c.setFillColor(colors.HexColor("#1A7A6E"))
            c.roundRect(rx + 8, 8, half - 16, h - 46, 5, fill=1, stroke=0)
            c.setFillColor(WHITE)
            c.setFont("Helvetica-Oblique", 8.5)
            ly = h - 50
            for ln in ["\u201cWrite a follow-up to Jane at",
                        "Agency X. We discussed brand",
                        "strategy. Goal: confirm next",
                        "steps. Warm but professional.\u201d"]:
                c.drawCentredString(rx + half / 2, ly, ln)
                ly -= 13
            c.setFont("Helvetica", 8)
            c.setFillColor(colors.HexColor("#A8EAE0"))
            gy = h - 106
            for g in ["Recipient named", "Context included",
                       "Goal specified", "Tone defined"]:
                c.drawCentredString(rx + half / 2, gy, f"\u2713  {g}")
                gy -= 14

            c.setFillColor(SOFT_TEAL)
            c.roundRect(rx + 8, 8, half - 16, 36, 5, fill=1, stroke=0)
            c.setFillColor(TEAL)
            c.setFont("Helvetica-Bold", 8)
            c.drawCentredString(rx + half / 2, 34, "Output:")
            c.setFont("Helvetica", 7.5)
            c.setFillColor(colors.HexColor("#0D5A52"))
            c.drawCentredString(rx + half / 2, 20, "Ready-to-send email,")
            c.drawCentredString(rx + half / 2, 9, "no editing needed")

        def wrap(self, *args):
            return self.w, self.h

    # ── Build story ─────────────────────────────────────────────────────────
    story = []

    # 1. Hero
    story += [
        ChapterHero(W, "1", "Why AI Gives You Generic Answers (and How to Change That)"),
        Spacer(1, 18),
    ]

    # 2. Opening section
    story += [
        KeepTogether([
            SectionDivider(W, "THE PROBLEM EVERYONE HAS BUT NOBODY EXPLAINS", "!"),
            Spacer(1, 10),
            Paragraph(
                "Ask ten people what frustrates them most about AI and you will hear the same "
                "answers. The complaints are remarkably consistent \u2014 and they all point to "
                "the same root cause.",
                S("b1", fontName="Helvetica", fontSize=10.5,
                  textColor=colors.HexColor("#222222"), spaceAfter=8,
                  leading=16, alignment=TA_JUSTIFY)),
        ]),
    ]

    # Complaint grid
    cell_s = S("cs", fontName="Helvetica-Oblique", fontSize=10, textColor=NAVY,
               leading=14, alignment=TA_CENTER)
    complaints = [
        ["\u201cIt\u2019s too generic.\u201d",
         "\u201cIt doesn\u2019t understand what I actually want.\u201d"],
        ["\u201cIt\u2019s confident but wrong.\u201d",
         "\u201cThe answer doesn\u2019t fit my situation.\u201d"],
        ["\u201cIt gives me five paragraphs when I needed two sentences.\u201d", ""],
    ]
    tdata = [[Paragraph(c, cell_s) for c in row] for row in complaints]
    t = Table(tdata, colWidths=[W / 2 - 4, W / 2 - 4], hAlign="CENTER")
    t.setStyle(TableStyle([
        ("BACKGROUND",  (0, 0), (-1, -1), SOFT_TEAL),
        ("BACKGROUND",  (0, 2), (0, 2),   colors.HexColor("#D6F0ED")),
        ("SPAN",        (0, 2), (1, 2)),
        ("BOX",         (0, 0), (-1, -1), 1.5, TEAL),
        ("INNERGRID",   (0, 0), (-1, -1), 0.5, colors.HexColor("#B0DDD8")),
        ("ROWPADDING",  (0, 0), (-1, -1), 10),
        ("VALIGN",      (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story += [t, Spacer(1, 8)]
    story += [
        KeyTakeawayBanner(W,
            "These are not problems with the AI. They are problems with the interaction."),
        Spacer(1, 16),
    ]

    # 3. Slot machine section
    story += [
        KeepTogether([
            SectionDivider(W, "THE SLOT MACHINE MODEL (AND WHY IT\u2019S WRONG)", "\U0001f3b0"),
            Spacer(1, 10),
            Paragraph(
                "Most people approach AI the way they might approach a vending machine: insert "
                "request, press button, hope for the right thing to fall out. This treats AI as "
                "a slot machine \u2014 and produces slot-machine results: random, unpredictable, "
                "and mostly disappointing.",
                S("b2", fontName="Helvetica", fontSize=10.5,
                  textColor=colors.HexColor("#222222"), spaceAfter=8,
                  leading=16, alignment=TA_JUSTIFY)),
        ]),
        Paragraph(
            "The people who consistently get excellent results are not luckier. They understand "
            "something slot-machine users don\u2019t: <b>AI output is shaped by input, and almost "
            "every dimension of that input is under your control.</b>",
            S("b3", fontName="Helvetica", fontSize=10.5,
              textColor=colors.HexColor("#222222"), spaceAfter=8,
              leading=16, alignment=TA_JUSTIFY)),
        Spacer(1, 10),
        _SlotMachine(W),
        Paragraph("Figure 1.1 \u2014 Two fundamentally different approaches to AI",
                  S("cap", fontName="Helvetica-Oblique", fontSize=8.5, textColor=MID_GRAY,
                    spaceAfter=4, leading=12, alignment=TA_CENTER)),
        Spacer(1, 16),
    ]

    # 4. Why AI is generic
    story += [
        KeepTogether([
            SectionDivider(W, "WHY AI IS GENERIC BY DEFAULT", "?"),
            Spacer(1, 10),
            Paragraph(
                "When you send AI a vague request, it has to make assumptions about everything "
                "it doesn\u2019t know. It fills in those gaps with the most statistically average "
                "answers it can construct \u2014 the kind of response acceptable to the largest "
                "number of readers in the largest number of situations. This is why AI output so "
                "often feels written for everyone and fits no one particularly well.",
                S("b4", fontName="Helvetica", fontSize=10.5,
                  textColor=colors.HexColor("#222222"), spaceAfter=8,
                  leading=16, alignment=TA_JUSTIFY)),
        ]),
    ]

    # Assumptions grid
    a_style = S("as", fontName="Helvetica", fontSize=9.5,
                textColor=colors.HexColor("#333333"), alignment=TA_CENTER, leading=13)
    assumptions = [
        ["Who will read this?", "Length required?", "Most important points?"],
        ["What to leave out?", "Appropriate tone?", "Reader\u2019s prior knowledge?"],
    ]
    adat = [[Paragraph(f"\u2753 {cell}", a_style) for cell in row] for row in assumptions]
    at = Table(adat, colWidths=[W / 3] * 3)
    at.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), SOFT_GOLD),
        ("BOX",        (0, 0), (-1, -1), 1.5, GOLD),
        ("INNERGRID",  (0, 0), (-1, -1), 0.5, colors.HexColor("#FFE08A")),
        ("ROWPADDING", (0, 0), (-1, -1), 10),
        ("VALIGN",     (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story += [
        Paragraph("<b>Gaps AI must fill when you\u2019re vague:</b>",
                  S("cl", fontName="Helvetica-Bold", fontSize=10, textColor=NAVY,
                    spaceAfter=4, leading=14)),
        at,
        Spacer(1, 10),
        NoteBox(W, "WHY IT WORKS", [
            "AI generates text by predicting what words should follow what came before,",
            "based on patterns from enormous quantities of written material. Providing",
            "more relevant information doesn\u2019t confuse AI \u2014 it constrains the",
            "prediction space to something closer to what you actually need.",
        ]),
        Spacer(1, 16),
    ]

    # 5. Three input failures
    story += [
        KeepTogether([
            SectionDivider(W, "THE THREE MOST COMMON INPUT FAILURES", "\u2717"),
            Spacer(1, 10),
        ]),
        IconCardRow(W, [
            {
                "number": "1", "title": "Vague Job\nDescription",
                "example": '"Help me with\nmy presentation"',
                "example_label": "typical bad prompt \u2191",
                "accent": RED_ACCENT, "bg": colors.HexColor("#FFF0F0"),
            },
            {
                "number": "2", "title": "Missing\nContext",
                "example": '"Reply to\nthis email"',
                "example_label": "typical bad prompt \u2191",
                "accent": colors.HexColor("#E87722"), "bg": colors.HexColor("#FFF5EC"),
            },
            {
                "number": "3", "title": "Wrong\nAssumed Audience",
                "example": '"Explain compound\ninterest"',
                "example_label": "typical bad prompt \u2191",
                "accent": colors.HexColor("#8E44AD"), "bg": colors.HexColor("#F8F0FF"),
            },
        ]),
        Paragraph("Figure 1.2 \u2014 The three failure patterns that produce poor AI output",
                  S("cap2", fontName="Helvetica-Oblique", fontSize=8.5, textColor=MID_GRAY,
                    spaceAfter=4, leading=12, alignment=TA_CENTER)),
        Spacer(1, 16),
    ]

    # 6. Real-world example
    story += [
        KeepTogether([
            SectionDivider(W, "REAL-WORLD EXAMPLE: SARAH\u2019S EMAIL", "\U0001f4e7"),
            Spacer(1, 10),
            Paragraph(
                "Sarah is a marketing manager who needs to send a follow-up email to a potential "
                "agency partner after an introductory call.",
                S("b5", fontName="Helvetica", fontSize=10.5,
                  textColor=colors.HexColor("#222222"), spaceAfter=8,
                  leading=16, alignment=TA_JUSTIFY)),
        ]),
        Spacer(1, 8),
        _BeforeAfter(W),
        Paragraph(
            "Figure 1.3 \u2014 Same AI, same model. The only variable was what Sarah provided.",
            S("cap3", fontName="Helvetica-Oblique", fontSize=8.5, textColor=MID_GRAY,
              spaceAfter=4, leading=12, alignment=TA_CENTER)),
        Spacer(1, 16),
    ]

    # 7. Five inputs framework
    story += [
        KeepTogether([
            SectionDivider(W, "WHAT ACTUALLY CHANGES GOOD AI OUTPUT", "\u2605"),
            Spacer(1, 10),
            Paragraph(
                "Five inputs move the needle most consistently. Mastering them alone will produce "
                "an immediate and significant improvement in every AI interaction you have.",
                S("b6", fontName="Helvetica", fontSize=10.5,
                  textColor=colors.HexColor("#222222"), spaceAfter=8,
                  leading=16, alignment=TA_JUSTIFY)),
        ]),
        Spacer(1, 8),
        OrbitalWheel(
            W,
            hub_label="5 KEY\nINPUTS",
            nodes=[
                {"label": "Clear\nJob",              "color": TEAL},
                {"label": "Relevant\nContext",        "color": GOLD},
                {"label": "Source\nMaterial",         "color": RED_ACCENT},
                {"label": "Output\nSpecs",            "color": colors.HexColor("#8E44AD")},
                {"label": "Verification\nInstructions","color": colors.HexColor("#E87722")},
            ],
            legend=[
                (TEAL,                        "Clear Job:",       "What specifically to DO"),
                (GOLD,                        "Context:",         "Your situation & audience"),
                (RED_ACCENT,                  "Source Material:", "Docs or data to work from"),
                (colors.HexColor("#8E44AD"),  "Output Specs:",    "Length, tone & format"),
                (colors.HexColor("#E87722"),  "Verification:",    "Flag errors & uncertainty"),
            ],
            legend_title="What Each Input Does",
        ),
        Paragraph("Figure 1.4 \u2014 The five core inputs that transform AI output quality",
                  S("cap4", fontName="Helvetica-Oblique", fontSize=8.5, textColor=MID_GRAY,
                    spaceAfter=4, leading=12, alignment=TA_CENTER)),
        Spacer(1, 14),
    ]

    # Numbered table reinforcement
    five_items = [
        ["#", "Input",                   "What it does"],
        ["1", "A Clear Job",             "What specifically do you want AI to DO? (Not \u2018help with\u2019 \u2014 do.)"],
        ["2", "Relevant Context",        "What does AI need to know about your situation, audience & constraints?"],
        ["3", "Source Material",         "What documents, notes, or data should AI work from?"],
        ["4", "Output Specifications",   "What should the result look like \u2014 length, format, tone, structure?"],
        ["5", "Verification Instructions","How should AI flag uncertainty or potential errors?"],
    ]
    story += [
        styled_table(five_items, [0.35 * inch, 1.7 * inch, W - 0.35 * inch - 1.7 * inch]),
        Spacer(1, 16),
    ]

    # 8. Try This
    story += [
        TryThisBox(W, [
            "Take a prompt you have used before that produced a disappointing result.",
            "Write it down. Then ask yourself:",
            "",
            "  \u2022 What did I assume AI would know that it couldn\u2019t have known?",
            "  \u2022 What context did I leave out?",
            "  \u2022 What does \u2018good\u2019 actually look like for this task?",
            "",
            "Rewrite the prompt with those gaps filled in. Run both versions.",
            "Notice what changed.",
        ]),
        Spacer(1, 16),
    ]

    # 9. What this chapter established
    story += [
        KeepTogether([
            SectionDivider(W, "WHAT THIS CHAPTER ESTABLISHED", "\u2713"),
            Spacer(1, 10),
            Paragraph(
                "Generic inputs produce generic outputs. This is a feature, not a bug \u2014 it "
                "means every improvement you make to your input produces a corresponding "
                "improvement in output. You are not at the mercy of the AI. <b>You are in "
                "control of the most important variable in every interaction.</b>",
                S("b7", fontName="Helvetica", fontSize=10.5,
                  textColor=colors.HexColor("#222222"), spaceAfter=8,
                  leading=16, alignment=TA_JUSTIFY)),
        ]),
    ]

    # 10. Watch Out
    story += [
        WatchOutBox(W, [
            "More detail is not always better. Adding irrelevant information doesn\u2019t",
            "improve output \u2014 it can dilute it. The skill is not writing longer prompts;",
            "it\u2019s identifying what AI actually needs to know to do this specific task well.",
            "You\u2019ll develop this judgment through the exercises in Part II.",
        ]),
        Spacer(1, 18),
    ]

    # 11. Closing banner
    story += [
        KeyTakeawayBanner(W, "Same AI. Same model. The variable was what you gave it."),
        Spacer(1, 10),
    ]

    return story


# ══════════════════════════════════════════════════════════════════════════════
# ADD FURTHER CHAPTERS BELOW using the @register(N) decorator.
# Example skeleton:
#
# @register(2)
# def _chapter_2(W: float):
#     story = []
#     # ... ChapterHero, SectionDividers, body Paragraphs, infographics ...
#     return story
# ══════════════════════════════════════════════════════════════════════════════


# ══════════════════════════════════════════════════════════════════════════════
# PUBLIC API
# ══════════════════════════════════════════════════════════════════════════════

def build_chapter(
    output_path: str,
    chapter_num: int,
    chapter_title: str = "",
    starting_page_num: int = 1,
    book_title: str = BOOK_TITLE,
) -> None:
    """
    Build an enhanced chapter PDF and write it to output_path.

    If chapter_num has a registered builder, use it.
    Otherwise fall back to a minimal plain-text layout (no infographics).

    Args:
        output_path      Destination PDF path.
        chapter_num      Chapter number (int).
        chapter_title    Chapter title string (used if no registered builder).
        starting_page_num First page number for the footer.
        book_title       Book title for the footer.
    """
    import os
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    doc = SimpleDocTemplate(
        output_path,
        pagesize=(8.5 * inch, 11 * inch),
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=MARGIN * 1.1,
        title=f"{book_title} \u2014 Chapter {chapter_num}",
        author=AUTHOR,
    )

    W = CONTENT_W

    if chapter_num in _CHAPTER_BUILDERS:
        story = _CHAPTER_BUILDERS[chapter_num](W)
    else:
        # Fallback: plain hero + placeholder body
        title = chapter_title or f"Chapter {chapter_num}"
        story = [
            ChapterHero(W, str(chapter_num), title),
            Spacer(1, 18),
            Paragraph(
                f"Chapter {chapter_num} content will be added here. "
                "Add a @register({chapter_num}) builder in enhance_chapter.py.",
                S("fallback", fontName="Helvetica", fontSize=10.5,
                  textColor=colors.HexColor("#222222"), spaceAfter=8,
                  leading=16, alignment=TA_JUSTIFY)),
        ]

    story.append(PageFooter(W, starting_page_num, book_title))
    doc.build(story)
    print(f"\u2705  Chapter {chapter_num} \u2192 {output_path}")


# ══════════════════════════════════════════════════════════════════════════════
# CLI
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python enhance_chapter.py <output.pdf> <chapter_num> [chapter_title]")
        sys.exit(1)

    _out   = sys.argv[1]
    _num   = int(sys.argv[2])
    _title = sys.argv[3] if len(sys.argv) > 3 else ""
    build_chapter(_out, _num, _title)
