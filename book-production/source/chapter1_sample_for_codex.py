"""
╔══════════════════════════════════════════════════════════════════════════════╗
║         THE ART OF AI — CHAPTER ENHANCER: SAMPLE REFERENCE SCRIPT          ║
║                                                                              ║
║  PURPOSE : Shows Codex exactly how Chapter 1 was built.                     ║
║            Use this as the template for all 40 chapters.                    ║
║                                                                              ║
║  TECH STACK:                                                                 ║
║    - reportlab        → all PDF drawing and layout                          ║
║    - pypdf            → extract text from input PDFs                        ║
║    - math (stdlib)    → geometry for circular/orbital diagrams              ║
║                                                                              ║
║  INSTALL:                                                                    ║
║    pip install reportlab pypdf                                               ║
║                                                                              ║
║  USAGE:                                                                      ║
║    python chapter1_sample_for_codex.py                                      ║
║    → Outputs: outputs/chapter01_enhanced.pdf                                ║
╚══════════════════════════════════════════════════════════════════════════════╝

HOW THE DESIGN DECISIONS WERE MADE FOR CHAPTER 1
─────────────────────────────────────────────────
The original PDF was read and each content block was classified:

  CONTENT FOUND              →  DESIGN DECISION
  ─────────────────────────────────────────────────────────────────────────
  5 complaint quotes         →  Teal grid table (visual grouping)
  Core argument sentence     →  KeyTakeawayBanner (navy full-width)
  Slot machine metaphor      →  SlotMachineInfographic (split panel)
  "Why it works" explainer   →  Dark navy sidebar table (callout box)
  3 input failure types      →  InputFailuresInfographic (3 icon cards)
  Sarah's email example      →  BeforeAfterComparison (split panel)
  5-item framework           →  FiveInputsWheel (orbital diagram)
  5 items also listed        →  Numbered table (text reinforcement)
  "Try This" exercise        →  TryThisBox (gold callout)
  "Watch Out" warning        →  WatchOutBox (red callout)
  All section headings       →  SectionDivider (teal pill)
  Chapter title              →  ChapterHero (navy banner)

  Pure narrative paragraphs  →  STYLE_BODY only — no visual added

VISUAL FREQUENCY IN THIS CHAPTER: 5 infographics across ~6 printed pages
That is on the higher end. For shorter/denser chapters aim for 2-3.
"""

# ─────────────────────────────────────────────────────────────────────────────
# IMPORTS
# ─────────────────────────────────────────────────────────────────────────────
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether, PageBreak, Flowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
import math

# ─────────────────────────────────────────────────────────────────────────────
# COLOR PALETTE  — use identically across ALL 40 chapters for visual consistency
# ─────────────────────────────────────────────────────────────────────────────
NAVY       = colors.HexColor("#0D1B2A")   # headings, banners, dark backgrounds
TEAL       = colors.HexColor("#1B998B")   # primary accent, section dividers
GOLD       = colors.HexColor("#FFBC42")   # Try This, highlights, positive
LIGHT_GRAY = colors.HexColor("#F4F6F9")   # table fills, card backgrounds
MID_GRAY   = colors.HexColor("#8C9BAB")   # captions, footer text
WHITE      = colors.white
RED_ACCENT = colors.HexColor("#E84855")   # Watch Out, warnings, negatives
SOFT_TEAL  = colors.HexColor("#D6F0ED")   # light teal fills
SOFT_GOLD  = colors.HexColor("#FFF4D6")   # light gold fills

# ─────────────────────────────────────────────────────────────────────────────
# PAGE SETUP  — KDP letter interior, 0.85in margins all sides
# ─────────────────────────────────────────────────────────────────────────────
PAGE_W, PAGE_H = letter          # 8.5 × 11 inches
MARGIN     = 0.85 * inch
CONTENT_W  = PAGE_W - 2 * MARGIN  # usable text/graphic width ≈ 456 pt

OUTPUT = "outputs/chapter01_enhanced.pdf"

# ─────────────────────────────────────────────────────────────────────────────
# TYPOGRAPHY STYLES
# Helvetica family only — built into ReportLab, no font embedding needed.
# ─────────────────────────────────────────────────────────────────────────────
def S(name, **kw):
    """Shorthand ParagraphStyle factory."""
    return ParagraphStyle(name, **kw)

STYLE_H1 = S("H1",
    fontName="Helvetica-Bold", fontSize=22, textColor=NAVY,
    spaceBefore=6, spaceAfter=14, leading=28, alignment=TA_LEFT)

STYLE_H2 = S("H2",
    fontName="Helvetica-Bold", fontSize=14, textColor=NAVY,
    spaceBefore=18, spaceAfter=6, leading=18)

STYLE_H3 = S("H3",
    fontName="Helvetica-Bold", fontSize=11, textColor=TEAL,
    spaceBefore=10, spaceAfter=4, leading=14)

STYLE_BODY = S("Body",
    fontName="Helvetica", fontSize=10.5, textColor=colors.HexColor("#222222"),
    spaceAfter=8, leading=16, alignment=TA_JUSTIFY)

STYLE_BODY_SMALL = S("BodySmall",
    fontName="Helvetica", fontSize=9.5, textColor=colors.HexColor("#333333"),
    spaceAfter=6, leading=14, alignment=TA_JUSTIFY)

STYLE_CAPTION = S("Caption",
    fontName="Helvetica-Oblique", fontSize=8.5, textColor=MID_GRAY,
    spaceAfter=4, leading=12, alignment=TA_CENTER)

STYLE_CALLOUT = S("Callout",
    fontName="Helvetica-Bold", fontSize=10, textColor=NAVY,
    spaceAfter=4, leading=14)


# ═════════════════════════════════════════════════════════════════════════════
# REUSABLE COMPONENT FLOWABLES
# Each is a Python class extending Flowable.
# Codex should reuse ALL of these unchanged across every chapter.
# Only the chapter-specific infographics change per chapter.
# ═════════════════════════════════════════════════════════════════════════════

class ChapterHero(Flowable):
    """
    Full-width decorative chapter header banner.
    REUSE IN EVERY CHAPTER — just change chapter_num and chapter_title.

    Visual anatomy:
      [navy background] [teal left bar] [CHAPTER N label] [title in white]
      [gold decorative dots top-right]  [gold underline bottom]
    """
    def __init__(self, w, chapter_num, chapter_title):
        Flowable.__init__(self)
        self.w = w
        self.h = 1.55 * inch
        self.chapter_num = chapter_num
        self.chapter_title = chapter_title

    def draw(self):
        c = self.canv
        w, h = self.w, self.h

        # Navy background
        c.setFillColor(NAVY)
        c.roundRect(0, 0, w, h, 10, fill=1, stroke=0)

        # Teal left accent bar
        c.setFillColor(TEAL)
        c.roundRect(0, 0, 6, h, 3, fill=1, stroke=0)

        # Gold decorative dots (top right)
        for i, x in enumerate([w-30, w-50, w-70]):
            c.setFillColor(GOLD if i == 0 else colors.HexColor("#FFDA8A"))
            c.circle(x, h/2, 8-i*2, fill=1, stroke=0)

        # "CHAPTER N" label in teal
        c.setFillColor(TEAL)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(20, h - 26, f"CHAPTER {self.chapter_num}")

        # Title in white — auto word-wraps to fit banner width
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 16)
        words = self.chapter_title.split()
        lines, line = [], []
        for word in words:
            test = " ".join(line + [word])
            if c.stringWidth(test, "Helvetica-Bold", 16) < self.w - 80:
                line.append(word)
            else:
                lines.append(" ".join(line))
                line = [word]
        if line:
            lines.append(" ".join(line))
        y = h - 48
        for ln in lines:
            c.drawString(20, y, ln)
            y -= 22

        # Gold bottom underline
        c.setStrokeColor(GOLD)
        c.setLineWidth(2)
        c.line(20, 18, self.w * 0.6, 18)

    def wrap(self, *args):
        return self.w, self.h


class SectionDivider(Flowable):
    """
    Teal pill-shaped section header. Use before every major section heading.
    REUSE IN EVERY CHAPTER.

    Args:
      text      — section heading text (uppercase recommended)
      icon_char — single emoji or symbol shown in teal badge on left
    """
    def __init__(self, w, text, icon_char="●"):
        Flowable.__init__(self)
        self.w = w
        self.h = 0.52 * inch
        self.text = text
        self.icon = icon_char

    def draw(self):
        c = self.canv
        # Soft teal pill background
        c.setFillColor(SOFT_TEAL)
        c.roundRect(0, 4, self.w, self.h - 8, 8, fill=1, stroke=0)
        # Solid teal left badge
        c.setFillColor(TEAL)
        c.roundRect(0, 4, 36, self.h - 8, 8, fill=1, stroke=0)
        # Icon in badge
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 14)
        c.drawCentredString(18, self.h/2 - 4, self.icon)
        # Section text
        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(46, self.h/2 - 4, self.text)

    def wrap(self, *args):
        return self.w, self.h


class KeyTakeawayBanner(Flowable):
    """
    Full-width navy banner for the single most important sentence per chapter.
    REUSE IN EVERY CHAPTER — typically used once or twice max per chapter.

    Args:
      text — the key sentence (auto-splits to two lines if too wide)
    """
    def __init__(self, w, text):
        Flowable.__init__(self)
        self.w = w
        self.text = text
        self.h = 0.9 * inch

    def draw(self):
        c = self.canv
        w, h = self.w, self.h
        # Navy background
        c.setFillColor(NAVY)
        c.roundRect(0, 0, w, h, 10, fill=1, stroke=0)
        # Faint teal quotation mark decoration
        c.setFillColor(TEAL)
        c.setFont("Helvetica-Bold", 48)
        c.setFillAlpha(0.18)
        c.drawString(8, 2, "\u201c")
        c.setFillAlpha(1)
        # White bold-italic text, centred
        c.setFillColor(WHITE)
        c.setFont("Helvetica-BoldOblique", 11.5)
        tw = c.stringWidth(self.text, "Helvetica-BoldOblique", 11.5)
        if tw > w - 80:
            words = self.text.split()
            mid = len(words) // 2
            l1 = " ".join(words[:mid])
            l2 = " ".join(words[mid:])
            c.drawCentredString(w/2, h/2 + 6, l1)
            c.drawCentredString(w/2, h/2 - 10, l2)
        else:
            c.drawCentredString(w/2, h/2 - 4, self.text)
        # Gold underline
        c.setStrokeColor(GOLD)
        c.setLineWidth(2)
        c.line(w * 0.25, 14, w * 0.75, 14)

    def wrap(self, *args):
        return self.w, self.h


class TryThisBox(Flowable):
    """
    Gold exercise/action box. Use for any 'Try This' or hands-on prompt.
    REUSE IN EVERY CHAPTER.

    Args:
      lines — list of strings, one per line in the box body
               Use "" for blank spacer lines between items
    """
    def __init__(self, w, lines):
        Flowable.__init__(self)
        self.w = w
        self.lines = lines
        self.h = 0.45 * inch + len(lines) * 18 + 16

    def draw(self):
        c = self.canv
        w, h = self.w, self.h
        # Soft gold background
        c.setFillColor(SOFT_GOLD)
        c.roundRect(0, 0, w, h, 10, fill=1, stroke=0)
        c.setStrokeColor(GOLD)
        c.setLineWidth(2.5)
        c.roundRect(0, 0, w, h, 10, fill=0, stroke=1)
        # Gold header bar
        c.setFillColor(GOLD)
        c.roundRect(0, h - 34, w, 34, 10, fill=1, stroke=0)
        c.rect(0, h - 34, w, 14, fill=1, stroke=0)
        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(16, h - 23, "\u270f  TRY THIS")
        # Body lines
        c.setFont("Helvetica", 9.5)
        c.setFillColor(colors.HexColor("#1A2A3A"))
        ty = h - 50
        for ln in self.lines:
            c.drawString(16, ty, ln)
            ty -= 18

    def wrap(self, *args):
        return self.w, self.h


class WatchOutBox(Flowable):
    """
    Red warning box. Use for 'Watch Out', caveats, or common mistakes.
    REUSE IN EVERY CHAPTER.

    Args:
      lines — list of strings, one per line in the box body
    """
    def __init__(self, w, lines):
        Flowable.__init__(self)
        self.w = w
        self.lines = lines
        self.h = 0.45 * inch + len(lines) * 18 + 16

    def draw(self):
        c = self.canv
        w, h = self.w, self.h
        # Light red background
        c.setFillColor(colors.HexColor("#FFF3F0"))
        c.roundRect(0, 0, w, h, 10, fill=1, stroke=0)
        c.setStrokeColor(RED_ACCENT)
        c.setLineWidth(2.5)
        c.roundRect(0, 0, w, h, 10, fill=0, stroke=1)
        # Red header bar
        c.setFillColor(RED_ACCENT)
        c.roundRect(0, h - 34, w, 34, 10, fill=1, stroke=0)
        c.rect(0, h - 34, w, 14, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(16, h - 23, "\u26a0  WATCH OUT")
        # Body lines
        c.setFont("Helvetica", 9.5)
        c.setFillColor(colors.HexColor("#3A1010"))
        ty = h - 50
        for ln in self.lines:
            c.drawString(16, ty, ln)
            ty -= 18

    def wrap(self, *args):
        return self.w, self.h


class PageFooter(Flowable):
    """
    Teal-ruled footer with book title (left) and page number (right).
    REUSE IN EVERY CHAPTER — update page_num per chapter.
    """
    def __init__(self, w, page_num, book_title):
        Flowable.__init__(self)
        self.w = w
        self.h = 0.35 * inch
        self.page_num = page_num
        self.book_title = book_title

    def draw(self):
        c = self.canv
        c.setStrokeColor(TEAL)
        c.setLineWidth(0.8)
        c.line(0, self.h - 2, self.w, self.h - 2)
        c.setFillColor(MID_GRAY)
        c.setFont("Helvetica", 8)
        c.drawString(0, 4, self.book_title)
        c.drawRightString(self.w, 4, str(self.page_num))

    def wrap(self, *args):
        return self.w, self.h


# ═════════════════════════════════════════════════════════════════════════════
# CHAPTER-SPECIFIC INFOGRAPHICS
# These were built specifically for Chapter 1's content.
# For other chapters, Codex builds NEW infographic classes using the same
# pattern: extend Flowable, implement draw() using self.canv commands.
# ═════════════════════════════════════════════════════════════════════════════

class SlotMachineInfographic(Flowable):
    """
    CHAPTER 1 SPECIFIC — built because the chapter contrasts two approaches.
    Content trigger: comparison/contrast → use split panel pattern.

    Left panel  = negative approach (red tones, slot machine icon)
    Right panel = positive approach (teal tones, target icon)
    VS badge    = gold circle between panels
    """
    def __init__(self, w):
        Flowable.__init__(self)
        self.w = w
        self.h = 2.6 * inch

    def draw(self):
        c = self.canv
        w, h = self.w, self.h
        half = w / 2 - 8

        # ── LEFT PANEL: Slot Machine approach ──────────────────────────────
        c.setFillColor(colors.HexColor("#FFF0F0"))
        c.roundRect(0, 0, half, h, 8, fill=1, stroke=0)
        c.setStrokeColor(RED_ACCENT)
        c.setLineWidth(1.5)
        c.roundRect(0, 0, half, h, 8, fill=0, stroke=1)

        c.setFillColor(RED_ACCENT)
        c.setFont("Helvetica-Bold", 10)
        c.drawCentredString(half/2, h - 20, "\u274c  SLOT MACHINE APPROACH")

        # Slot machine icon (3 reels with ? marks)
        slot_x, slot_y, sw, sh = half/2 - 28, h - 90, 56, 52
        c.setFillColor(colors.HexColor("#DDDDDD"))
        c.roundRect(slot_x, slot_y, sw, sh, 5, fill=1, stroke=0)
        c.setFillColor(colors.HexColor("#BBBBBB"))
        c.rect(slot_x+6, slot_y+8, sw-12, sh-20, fill=1, stroke=0)
        c.setFillColor(WHITE)
        for xi in [slot_x+8, slot_x+22, slot_x+36]:
            c.rect(xi, slot_y+10, 12, sh-24, fill=1, stroke=0)
        c.setFillColor(RED_ACCENT)
        c.setFont("Helvetica-Bold", 9)
        for xi in [slot_x+10, slot_x+24, slot_x+38]:
            c.drawString(xi, slot_y+18, "?")

        bullets_l = ["Vague request", "Hope for the best",
                     "Random results", "Mostly disappointing"]
        c.setFont("Helvetica", 9)
        c.setFillColor(colors.HexColor("#555555"))
        by = h - 108
        for b in bullets_l:
            c.drawString(12, by, f"\u2022 {b}")
            by -= 15

        # ── RIGHT PANEL: Intentional approach ──────────────────────────────
        rx = half + 16
        c.setFillColor(SOFT_TEAL)
        c.roundRect(rx, 0, half, h, 8, fill=1, stroke=0)
        c.setStrokeColor(TEAL)
        c.setLineWidth(1.5)
        c.roundRect(rx, 0, half, h, 8, fill=0, stroke=1)

        c.setFillColor(TEAL)
        c.setFont("Helvetica-Bold", 10)
        c.drawCentredString(rx + half/2, h - 20, "\u2713  INTENTIONAL APPROACH")

        # Target/bullseye icon (4 concentric circles)
        cx_t, cy_t = rx + half/2, h - 68
        for r, col in [(24, SOFT_TEAL), (17, colors.HexColor("#9EE4DA")),
                       (10, TEAL), (4, NAVY)]:
            c.setFillColor(col)
            c.setStrokeColor(WHITE)
            c.setLineWidth(1)
            c.circle(cx_t, cy_t, r, fill=1, stroke=1)

        bullets_r = ["Clear job specified", "Context provided",
                     "Predictable output", "Consistent results"]
        c.setFont("Helvetica", 9)
        c.setFillColor(colors.HexColor("#1A3A34"))
        by = h - 108
        for b in bullets_r:
            c.drawString(rx + 12, by, f"\u2022 {b}")
            by -= 15

        # ── VS badge centred between panels ────────────────────────────────
        badge_x = half + 1
        badge_y = h/2 - 14
        c.setFillColor(GOLD)
        c.circle(badge_x + 7, badge_y + 14, 14, fill=1, stroke=0)
        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 9)
        c.drawCentredString(badge_x + 7, badge_y + 10, "VS")

    def wrap(self, *args):
        return self.w, self.h


class InputFailuresInfographic(Flowable):
    """
    CHAPTER 1 SPECIFIC — built because the chapter lists 3 named failure types.
    Content trigger: numbered framework (3 items) → use icon card row pattern.

    Each card: accent-coloured numbered badge + title + example prompt box
    Cards use distinct accent colours so they read as separate categories.
    """
    def __init__(self, w):
        Flowable.__init__(self)
        self.w = w
        self.h = 2.1 * inch

    def draw(self):
        c = self.canv
        w, h = self.w, self.h
        pad = 10
        col_w = (w - pad * 2) / 3

        items = [
            ("1", "Vague Job\nDescription", '"Help me with\nmy presentation"',
             RED_ACCENT, colors.HexColor("#FFF0F0")),
            ("2", "Missing\nContext", '"Reply to\nthis email"',
             colors.HexColor("#E87722"), colors.HexColor("#FFF5EC")),
            ("3", "Wrong\nAssumed Audience", '"Explain compound\ninterest"',
             colors.HexColor("#8E44AD"), colors.HexColor("#F8F0FF")),
        ]

        for i, (num, title, example, accent, bg) in enumerate(items):
            x = i * (col_w + pad)
            # Card
            c.setFillColor(bg)
            c.roundRect(x, 0, col_w, h, 8, fill=1, stroke=0)
            c.setStrokeColor(accent)
            c.setLineWidth(2)
            c.roundRect(x, 0, col_w, h, 8, fill=0, stroke=1)
            # Number badge
            c.setFillColor(accent)
            c.circle(x + col_w/2, h - 22, 16, fill=1, stroke=0)
            c.setFillColor(WHITE)
            c.setFont("Helvetica-Bold", 14)
            c.drawCentredString(x + col_w/2, h - 27, num)
            # Title
            c.setFillColor(NAVY)
            c.setFont("Helvetica-Bold", 9.5)
            yt = h - 52
            for ln in title.split("\n"):
                c.drawCentredString(x + col_w/2, yt, ln)
                yt -= 13
            # Example prompt box
            c.setFillColor(WHITE)
            c.roundRect(x + 8, 12, col_w - 16, 52, 5, fill=1, stroke=0)
            c.setFillColor(accent)
            c.setFont("Helvetica-Oblique", 8.5)
            ey = 50
            for ln in example.split("\n"):
                c.drawCentredString(x + col_w/2, ey, ln)
                ey -= 13
            c.setFillColor(MID_GRAY)
            c.setFont("Helvetica", 7.5)
            c.drawCentredString(x + col_w/2, 16, "typical bad prompt \u2191")

    def wrap(self, *args):
        return self.w, self.h


class FiveInputsWheel(Flowable):
    """
    CHAPTER 1 SPECIFIC — built because the chapter introduces a 5-item framework.
    Content trigger: 5-item framework → use orbital wheel diagram.

    Centre circle = concept label
    5 nodes placed using sin/cos at equal angular intervals around orbit
    Spokes connect centre to each node
    Right-side legend = text descriptions of each node
    """
    def __init__(self, w):
        Flowable.__init__(self)
        self.w = w
        self.h = 2.7 * inch

    def draw(self):
        c = self.canv
        w, h = self.w, self.h

        # Light grey background card
        c.setFillColor(LIGHT_GRAY)
        c.roundRect(0, 0, w, h, 10, fill=1, stroke=0)

        # Centre hub
        cx, cy = w * 0.28, h / 2
        c.setFillColor(NAVY)
        c.circle(cx, cy, 44, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 9)
        c.drawCentredString(cx, cy + 6, "5 KEY")
        c.drawCentredString(cx, cy - 6, "INPUTS")

        # Node definitions: (label, colour, angle_degrees)
        inputs = [
            ("Clear\nJob",              TEAL,                            0),
            ("Relevant\nContext",        GOLD,                           72),
            ("Source\nMaterial",         RED_ACCENT,                    144),
            ("Output\nSpecs",            colors.HexColor("#8E44AD"),    216),
            ("Verification\nInstructions", colors.HexColor("#E87722"),  288),
        ]

        r_orbit = 82   # distance from centre to node centre
        r_node  = 28   # radius of each node circle
        r_hub   = 44   # radius of centre hub

        for label, col, angle_deg in inputs:
            angle = math.radians(angle_deg - 90)  # -90 so 0° is at top
            nx = cx + r_orbit * math.cos(angle)
            ny = cy + r_orbit * math.sin(angle)

            # Spoke line from hub edge to node edge
            sx = cx + r_hub   * math.cos(angle)
            sy = cy + r_hub   * math.sin(angle)
            ex = nx - r_node  * math.cos(angle)
            ey = ny - r_node  * math.sin(angle)
            c.setStrokeColor(col)
            c.setLineWidth(1.5)
            c.line(sx, sy, ex, ey)

            # Node circle
            c.setFillColor(col)
            c.circle(nx, ny, r_node, fill=1, stroke=0)

            # Node label (white, centred, multiline)
            c.setFillColor(WHITE)
            c.setFont("Helvetica-Bold", 7.5)
            lines = label.split("\n")
            for j, ln in enumerate(lines):
                offset = (len(lines) - 1) * 4.5 - j * 9
                c.drawCentredString(nx, ny + offset, ln)

        # Right-side legend panel
        lx = w * 0.56
        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(lx, h - 22, "What Each Input Does")
        c.setStrokeColor(TEAL)
        c.setLineWidth(1.5)
        c.line(lx, h - 28, lx + 140, h - 28)

        legend = [
            (TEAL,                         "Clear Job:",       "What specifically to DO"),
            (GOLD,                         "Context:",         "Your situation & audience"),
            (RED_ACCENT,                   "Source Material:", "Docs or data to work from"),
            (colors.HexColor("#8E44AD"),   "Output Specs:",    "Length, tone & format"),
            (colors.HexColor("#E87722"),   "Verification:",    "Flag errors & uncertainty"),
        ]
        dy = h - 46
        for col, bold, rest in legend:
            # Colour dot
            c.setFillColor(col)
            c.circle(lx - 8, dy + 4, 4, fill=1, stroke=0)
            # Bold key
            c.setFillColor(NAVY)
            c.setFont("Helvetica-Bold", 8.5)
            bw = c.stringWidth(bold, "Helvetica-Bold", 8.5)
            c.drawString(lx, dy, bold)
            # Normal description
            c.setFont("Helvetica", 8.5)
            c.setFillColor(colors.HexColor("#444444"))
            c.drawString(lx + bw + 3, dy, rest)
            dy -= 18

    def wrap(self, *args):
        return self.w, self.h


class BeforeAfterComparison(Flowable):
    """
    CHAPTER 1 SPECIFIC — built because the chapter has a named before/after example.
    Content trigger: named example with before/after → use annotated split panel.

    Left  = BEFORE (red tones, annotated with what's missing)
    Right = AFTER  (teal tones, annotated with what was added)
    Both panels have a result box at the bottom showing the output quality.
    """
    def __init__(self, w):
        Flowable.__init__(self)
        self.w = w
        self.h = 2.2 * inch

    def draw(self):
        c = self.canv
        w, h = self.w, self.h
        half = w / 2 - 6

        # ── BEFORE panel (left) ────────────────────────────────────────────
        c.setFillColor(colors.HexColor("#FFF0F0"))
        c.roundRect(0, 0, half, h, 8, fill=1, stroke=0)
        # Red header
        c.setFillColor(RED_ACCENT)
        c.roundRect(0, h - 30, half, 30, 8, fill=1, stroke=0)
        c.rect(0, h - 22, half, 14, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 10)
        c.drawCentredString(half/2, h - 20, "BEFORE  \u2717")
        # Prompt display
        c.setFillColor(colors.HexColor("#CC3333"))
        c.roundRect(8, 8, half - 16, h - 46, 5, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Oblique", 9)
        c.drawCentredString(half/2, h - 52, '"Write a follow-up email')
        c.drawCentredString(half/2, h - 65, 'after a business meeting."')
        # Missing info annotations
        c.setFont("Helvetica", 8)
        c.setFillColor(colors.HexColor("#FFAAAA"))
        issues = ["No recipient info", "No meeting details",
                  "No goal specified", "No tone guidance"]
        iy = h - 90
        for iss in issues:
            c.drawCentredString(half/2, iy, f"\u2717  {iss}")
            iy -= 14
        # Output result box
        c.setFillColor(colors.HexColor("#FFDDDD"))
        c.roundRect(8, 8, half - 16, 38, 5, fill=1, stroke=0)
        c.setFillColor(RED_ACCENT)
        c.setFont("Helvetica-Bold", 8)
        c.drawCentredString(half/2, 36, "Output:")
        c.setFont("Helvetica", 7.5)
        c.setFillColor(colors.HexColor("#993333"))
        c.drawCentredString(half/2, 22, "Generic template with")
        c.drawCentredString(half/2, 11, "[placeholders] — unusable")

        # ── AFTER panel (right) ────────────────────────────────────────────
        rx = half + 12
        c.setFillColor(SOFT_TEAL)
        c.roundRect(rx, 0, half, h, 8, fill=1, stroke=0)
        # Teal header
        c.setFillColor(TEAL)
        c.roundRect(rx, h - 30, half, 30, 8, fill=1, stroke=0)
        c.rect(rx, h - 22, half, 14, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 10)
        c.drawCentredString(rx + half/2, h - 20, "AFTER  \u2713")
        # Improved prompt display
        c.setFillColor(colors.HexColor("#1A7A6E"))
        c.roundRect(rx + 8, 8, half - 16, h - 46, 5, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Oblique", 8.5)
        prompt_lines = ['"Write a follow-up to Jane at',
                        'Agency X. We discussed brand',
                        'strategy. Goal: confirm next',
                        'steps. Warm but professional."']
        ly = h - 50
        for ln in prompt_lines:
            c.drawCentredString(rx + half/2, ly, ln)
            ly -= 13
        # What was added annotations
        c.setFont("Helvetica", 8)
        c.setFillColor(colors.HexColor("#A8EAE0"))
        goods = ["Recipient named", "Context included",
                 "Goal specified", "Tone defined"]
        gy = h - 108
        for g in goods:
            c.drawCentredString(rx + half/2, gy, f"\u2713  {g}")
            gy -= 14
        # Output result box
        c.setFillColor(SOFT_TEAL)
        c.roundRect(rx + 8, 8, half - 16, 38, 5, fill=1, stroke=0)
        c.setFillColor(TEAL)
        c.setFont("Helvetica-Bold", 8)
        c.drawCentredString(rx + half/2, 36, "Output:")
        c.setFont("Helvetica", 7.5)
        c.setFillColor(colors.HexColor("#0D5A52"))
        c.drawCentredString(rx + half/2, 22, "Ready-to-send email,")
        c.drawCentredString(rx + half/2, 11, "no editing needed")

    def wrap(self, *args):
        return self.w, self.h


# ═════════════════════════════════════════════════════════════════════════════
# DOCUMENT ASSEMBLY  — build_pdf() puts the story together
# ═════════════════════════════════════════════════════════════════════════════

def build_pdf():
    """
    Assembles all flowables into the final PDF using Platypus SimpleDocTemplate.
    story = ordered list of Flowable objects, processed top-to-bottom.
    Platypus handles page breaks automatically when content overflows.
    """
    import os
    os.makedirs("outputs", exist_ok=True)

    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=letter,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=MARGIN * 1.1,
        title="The Art of AI \u2014 Chapter 1",
        author="The Art of AI",
    )

    story = []
    W = CONTENT_W
    BOOK = "The Art of AI"

    # ── 1. CHAPTER HERO ───────────────────────────────────────────────────────
    story.append(ChapterHero(W, "1",
        "Why AI Gives You Generic Answers (and How to Change That)"))
    story.append(Spacer(1, 18))

    # ── 2. OPENING PROBLEM ────────────────────────────────────────────────────
    story.append(SectionDivider(W, "THE PROBLEM EVERYONE HAS BUT NOBODY EXPLAINS", "!"))
    story.append(Spacer(1, 10))

    story.append(Paragraph(
        "Ask ten people what frustrates them most about AI and you will hear the same answers. "
        "The complaints are remarkably consistent \u2014 and they all point to the same root cause.",
        STYLE_BODY))

    # Complaint quotes as a teal grid table
    cell_style = ParagraphStyle("Cell", fontName="Helvetica-Oblique",
        fontSize=10, textColor=NAVY, leading=14, alignment=TA_CENTER)
    complaints = [
        ['"It\'s too generic."',           '"It doesn\'t understand what I actually want."'],
        ['"It\'s confident but wrong."',   '"The answer doesn\'t fit my situation."'],
        ['"It gives me five paragraphs when I needed two sentences."', ''],
    ]
    tdata = [[Paragraph(cell, cell_style) for cell in row] for row in complaints]
    t = Table(tdata, colWidths=[W/2 - 4, W/2 - 4], hAlign="CENTER")
    t.setStyle(TableStyle([
        ("BACKGROUND",  (0, 0), (-1, -1), SOFT_TEAL),
        ("BACKGROUND",  (0, 2), (0, 2),   colors.HexColor("#D6F0ED")),
        ("SPAN",        (0, 2), (1, 2)),
        ("BOX",         (0, 0), (-1, -1), 1.5, TEAL),
        ("INNERGRID",   (0, 0), (-1, -1), 0.5, colors.HexColor("#B0DDD8")),
        ("ROWPADDING",  (0, 0), (-1, -1), 10),
        ("VALIGN",      (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(t)
    story.append(Spacer(1, 8))

    story.append(KeyTakeawayBanner(W,
        "These are not problems with the AI. They are problems with the interaction."))
    story.append(Spacer(1, 16))

    # ── 3. SLOT MACHINE SECTION ───────────────────────────────────────────────
    story.append(SectionDivider(W, "THE SLOT MACHINE MODEL (AND WHY IT'S WRONG)", "\U0001f3b0"))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "Most people approach AI the way they might approach a vending machine: insert request, "
        "press button, hope for the right thing to fall out. When it doesn\u2019t, they try "
        "slightly different words. This treats AI as a slot machine \u2014 and produces "
        "slot-machine results: random, unpredictable, and mostly disappointing.",
        STYLE_BODY))
    story.append(Paragraph(
        "The people who consistently get excellent results are not luckier. They are not using "
        "secret prompts. They understand something slot-machine users don\u2019t: <b>AI output "
        "is shaped by input, and almost every dimension of that input is under your control.</b>",
        STYLE_BODY))
    story.append(Spacer(1, 10))
    story.append(SlotMachineInfographic(W))
    story.append(Paragraph("Figure 1.1 \u2014 Two fundamentally different approaches to AI",
                            STYLE_CAPTION))
    story.append(Spacer(1, 16))

    # ── 4. WHY AI IS GENERIC ──────────────────────────────────────────────────
    story.append(SectionDivider(W, "WHY AI IS GENERIC BY DEFAULT", "?"))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "When you send AI a vague request \u2014 <i>\"Write me a summary of this report\"</i> "
        "\u2014 it has to make assumptions about everything it doesn\u2019t know. The AI fills "
        "in those gaps with the most statistically average answers it can construct: the kind of "
        "response acceptable to the largest number of readers in the largest number of situations. "
        "This is why AI output so often feels written for everyone and fits no one particularly well.",
        STYLE_BODY))

    # Assumptions grid (gold table)
    a_style = ParagraphStyle("Assum", fontName="Helvetica", fontSize=9.5,
        textColor=colors.HexColor("#333333"), alignment=TA_CENTER, leading=13)
    assumptions = [
        ["Who will read this?",  "Length required?",    "Most important points?"],
        ["What to leave out?",   "Appropriate tone?",   "Reader\u2019s prior knowledge?"],
    ]
    adata = [[Paragraph(f"\u2753 {cell}", a_style) for cell in row] for row in assumptions]
    at = Table(adata, colWidths=[W/3]*3)
    at.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), SOFT_GOLD),
        ("BOX",        (0, 0), (-1, -1), 1.5, GOLD),
        ("INNERGRID",  (0, 0), (-1, -1), 0.5, colors.HexColor("#FFE08A")),
        ("ROWPADDING", (0, 0), (-1, -1), 10),
        ("VALIGN",     (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(Paragraph("<b>Gaps AI must fill when you\u2019re vague:</b>", STYLE_CALLOUT))
    story.append(at)
    story.append(Spacer(1, 10))

    # "Why It Works" dark navy explainer sidebar (table used as styled box)
    how_data = [[
        Paragraph("<b>WHY IT WORKS</b>",
                  ParagraphStyle("hw_t", fontName="Helvetica-Bold", fontSize=10,
                                 textColor=WHITE, leading=13)),
        Paragraph(
            "AI generates text by predicting what words should follow what came before, "
            "based on patterns learned from enormous quantities of written material. "
            "Providing more relevant information doesn\u2019t confuse AI \u2014 it "
            "<b>constrains the prediction space</b> to something closer to what you actually need.",
            ParagraphStyle("hw_b", fontName="Helvetica", fontSize=9.5,
                           textColor=WHITE, leading=14, alignment=TA_JUSTIFY)),
    ]]
    ht = Table(how_data, colWidths=[1.2*inch, W - 1.2*inch])
    ht.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("ROWPADDING", (0, 0), (-1, -1), 12),
        ("VALIGN",     (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(ht)
    story.append(Spacer(1, 16))

    # ── 5. THREE INPUT FAILURES ───────────────────────────────────────────────
    story.append(SectionDivider(W, "THE THREE MOST COMMON INPUT FAILURES", "\u2717"))
    story.append(Spacer(1, 10))
    story.append(InputFailuresInfographic(W))
    story.append(Paragraph(
        "Figure 1.2 \u2014 The three failure patterns that produce poor AI output",
        STYLE_CAPTION))
    story.append(Spacer(1, 10))

    failures = [
        ("1. The Vague Job Description",
         '"Help me with my presentation" tells AI you want a presentation. It doesn\u2019t '
         'tell it the topic, the audience, the desired length, your current draft, what help '
         'means, or what \u201cbetter\u201d would look like. AI has no choice but to respond '
         'generically to a generic request.'),
        ("2. The Missing Context",
         '"Reply to this email" gives AI a text to work with. It doesn\u2019t tell AI who '
         'sent it, what the relationship is, what a good reply should accomplish, how formal '
         'the tone should be, or what your constraints are. AI will guess. Sometimes it guesses '
         'right. Usually the first reply needs significant editing.'),
        ("3. The Wrong Assumed Audience",
         '"Explain compound interest" gives AI a topic. But who is asking? A secondary school '
         'student? A financial professional? Someone deciding whether to take out a mortgage? '
         'AI will produce an explanation pitched at a generic reader \u2014 which may be too '
         'basic, too technical, or simply beside the point.'),
    ]
    for h3, body in failures:
        story.append(Paragraph(f"<b>{h3}</b>", STYLE_H3))
        story.append(Paragraph(body, STYLE_BODY))
    story.append(Spacer(1, 10))

    # ── 6. REAL-WORLD EXAMPLE ─────────────────────────────────────────────────
    story.append(SectionDivider(W, "REAL-WORLD EXAMPLE: SARAH\u2019S EMAIL", "\U0001f4e7"))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "Sarah is a marketing manager who needs to send a follow-up email to a potential "
        "agency partner after an introductory call.", STYLE_BODY))
    story.append(Spacer(1, 8))
    story.append(BeforeAfterComparison(W))
    story.append(Paragraph(
        "Figure 1.3 \u2014 Same AI, same model. The only variable was what Sarah provided.",
        STYLE_CAPTION))
    story.append(Spacer(1, 16))

    # ── 7. FIVE INPUTS FRAMEWORK ──────────────────────────────────────────────
    story.append(SectionDivider(W, "WHAT ACTUALLY CHANGES GOOD AI OUTPUT", "\u2605"))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "Five inputs move the needle most consistently. Mastering them alone will produce "
        "an immediate and significant improvement in every AI interaction you have.",
        STYLE_BODY))
    story.append(Spacer(1, 8))
    story.append(FiveInputsWheel(W))
    story.append(Paragraph(
        "Figure 1.4 \u2014 The five core inputs that transform AI output quality",
        STYLE_CAPTION))
    story.append(Spacer(1, 14))

    # Numbered summary table (text reinforcement of the wheel above)
    five_items = [
        ("1", "A Clear Job",               "What specifically do you want AI to DO? (Not \u2018help with\u2019 \u2014 do.)"),
        ("2", "Relevant Context",           "What does AI need to know about your situation, audience & constraints?"),
        ("3", "Source Material",            "What documents, notes, or data should AI work from?"),
        ("4", "Output Specifications",      "What should the result look like \u2014 length, format, tone, structure?"),
        ("5", "Verification Instructions",  "How should AI flag uncertainty or potential errors?"),
    ]
    num_s = ParagraphStyle("Num", fontName="Helvetica-Bold", fontSize=13,
        textColor=WHITE, alignment=TA_CENTER, leading=16)
    key_s = ParagraphStyle("Key", fontName="Helvetica-Bold", fontSize=10,
        textColor=NAVY, leading=13)
    val_s = ParagraphStyle("Val", fontName="Helvetica", fontSize=9.5,
        textColor=colors.HexColor("#333333"), leading=13)

    fdata = [[Paragraph(n, num_s), Paragraph(k, key_s), Paragraph(v, val_s)]
             for n, k, v in five_items]

    teal_shades = [TEAL, colors.HexColor("#1D8A7E"), colors.HexColor("#1F9A8C"),
                   colors.HexColor("#17766A"), colors.HexColor("#14635A")]
    ft = Table(fdata, colWidths=[0.35*inch, 1.7*inch, W - 0.35*inch - 1.7*inch])
    ts = [
        ("VALIGN",     (0, 0), (-1, -1), "MIDDLE"),
        ("ROWPADDING", (0, 0), (-1, -1), 10),
        ("INNERGRID",  (0, 0), (-1, -1), 0.5, colors.HexColor("#CCCCCC")),
        ("BOX",        (0, 0), (-1, -1), 1.5, TEAL),
        ("BACKGROUND", (1, 0), (-1, -1), LIGHT_GRAY),
    ]
    for i, col in enumerate(teal_shades):
        ts.append(("BACKGROUND", (0, i), (0, i), col))
    ft.setStyle(TableStyle(ts))
    story.append(ft)
    story.append(Spacer(1, 16))

    # ── 8. TRY THIS ───────────────────────────────────────────────────────────
    try_lines = [
        "Take a prompt you have used before that produced a disappointing result.",
        "Write it down. Then ask yourself:",
        "",
        "  \u2022 What did I assume AI would know that it couldn\u2019t have known?",
        "  \u2022 What context did I leave out?",
        "  \u2022 What does \u2018good\u2019 actually look like for this task?",
        "",
        "Rewrite the prompt with those gaps filled in. Run both versions.",
        "Notice what changed.",
    ]
    story.append(TryThisBox(W, try_lines))
    story.append(Spacer(1, 16))

    # ── 9. WHAT THIS CHAPTER ESTABLISHED ─────────────────────────────────────
    story.append(SectionDivider(W, "WHAT THIS CHAPTER ESTABLISHED", "\u2713"))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "Generic inputs produce generic outputs. This is a feature, not a bug \u2014 it means "
        "every improvement you make to your input produces a corresponding improvement in output. "
        "You are not at the mercy of the AI. <b>You are in control of the most important variable "
        "in every interaction.</b>",
        STYLE_BODY))
    story.append(Paragraph(
        "The next chapter introduces a model for understanding exactly which variables are in "
        "play \u2014 and which ones matter most for any given task.",
        STYLE_BODY))
    story.append(Spacer(1, 12))

    # ── 10. WATCH OUT ─────────────────────────────────────────────────────────
    watch_lines = [
        "More detail is not always better. Adding irrelevant information doesn\u2019t",
        "improve output \u2014 it can dilute it. The skill is not writing longer prompts;",
        "it\u2019s identifying what AI actually needs to know to do this specific task well.",
        "You\u2019ll develop this judgment through the exercises in Part II.",
    ]
    story.append(WatchOutBox(W, watch_lines))
    story.append(Spacer(1, 18))

    # ── 11. CLOSING BANNER ────────────────────────────────────────────────────
    story.append(KeyTakeawayBanner(W,
        "Same AI. Same model. The variable was what you gave it."))
    story.append(Spacer(1, 10))

    # ── 12. PAGE FOOTER ───────────────────────────────────────────────────────
    story.append(PageFooter(W, 11, BOOK))

    doc.build(story)
    print(f"\u2705  PDF saved to {OUTPUT}")


# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    build_pdf()
