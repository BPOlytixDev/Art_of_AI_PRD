"""
components.py
=============
Reusable ReportLab Flowable components for The Art of AI — Book 1
enhancement layer.

Import from enhance_chapter.py and batch_enhance.py.
Do NOT duplicate these class definitions elsewhere.

Design system
-------------
All visual elements use only these tokens (B&W-print safe):

  NAVY       #0D1B2A   headings, banners, dark backgrounds
  TEAL       #1B998B   primary accent, section dividers
  GOLD       #FFBC42   TryThis boxes, highlights
  LIGHT_GRAY #F4F6F9   table/card backgrounds
  MID_GRAY   #8C9BAB   captions, footer text
  WHITE      #FFFFFF
  RED_ACCENT #E84855   WatchOut boxes, warnings
  SOFT_TEAL  #D6F0ED   light teal fills
  SOFT_GOLD  #FFF4D6   light gold fills

Typography: Helvetica family only (built-in, no embedding required).
Author: Eleanor Mercer
"""

import math

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Flowable, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

# ── Palette ────────────────────────────────────────────────────────────────────
NAVY       = colors.HexColor("#0D1B2A")
TEAL       = colors.HexColor("#1B998B")
GOLD       = colors.HexColor("#FFBC42")
LIGHT_GRAY = colors.HexColor("#F4F6F9")
MID_GRAY   = colors.HexColor("#8C9BAB")
WHITE      = colors.white
RED_ACCENT = colors.HexColor("#E84855")
SOFT_TEAL  = colors.HexColor("#D6F0ED")
SOFT_GOLD  = colors.HexColor("#FFF4D6")

# ── Page geometry ──────────────────────────────────────────────────────────────
PAGE_W, PAGE_H = letter        # 8.5 × 11 in (standalone review format)
MARGIN         = 0.85 * inch
CONTENT_W      = PAGE_W - 2 * MARGIN

# ── Paragraph style factory ────────────────────────────────────────────────────
def S(name, **kw):
    """Shorthand ParagraphStyle constructor."""
    return ParagraphStyle(name, **kw)

# Pre-built styles — import these in enhance_chapter.py
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


# ══════════════════════════════════════════════════════════════════════════════
# REUSABLE COMPONENTS — use unchanged across all 40 chapters
# ══════════════════════════════════════════════════════════════════════════════

class ChapterHero(Flowable):
    """
    Full-width decorative chapter header banner.
    REUSE IN EVERY CHAPTER — only change chapter_num and chapter_title.

    Visual anatomy:
      Navy background | Teal left accent bar | Gold dots top-right
      "CHAPTER N" label in teal | Title in white (auto word-wrapped)
      Gold underline at bottom-left
    Height: 1.55 in
    """

    def __init__(self, w, chapter_num, chapter_title):
        Flowable.__init__(self)
        self.w = w
        self.h = 1.55 * inch
        self.chapter_num = str(chapter_num)
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

        # Gold decorative dots (top-right, three decreasing sizes)
        for i, x in enumerate([w - 30, w - 50, w - 70]):
            c.setFillColor(GOLD if i == 0 else colors.HexColor("#FFDA8A"))
            c.circle(x, h / 2, 8 - i * 2, fill=1, stroke=0)

        # "CHAPTER N" label
        c.setFillColor(TEAL)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(20, h - 26, f"CHAPTER {self.chapter_num}")

        # Title — auto word-wrap to fit banner width
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

        # Gold bottom decorative underline
        c.setStrokeColor(GOLD)
        c.setLineWidth(2)
        c.line(20, 18, self.w * 0.6, 18)

    def wrap(self, *args):
        return self.w, self.h


class SectionDivider(Flowable):
    """
    Teal pill-shaped section header. Place before every major section heading.
    REUSE IN EVERY CHAPTER.

    Args:
        text      Section heading text (uppercase recommended)
        icon_char Single character/emoji shown in the teal badge on the left
    Height: 0.52 in
    """

    def __init__(self, w, text, icon_char="\u25cf"):
        Flowable.__init__(self)
        self.w = w
        self.h = 0.52 * inch
        self.text = text
        self.icon = icon_char

    def draw(self):
        c = self.canv
        # Soft-teal pill background
        c.setFillColor(SOFT_TEAL)
        c.roundRect(0, 4, self.w, self.h - 8, 8, fill=1, stroke=0)
        # Solid teal left badge
        c.setFillColor(TEAL)
        c.roundRect(0, 4, 36, self.h - 8, 8, fill=1, stroke=0)
        # Icon in badge
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 14)
        c.drawCentredString(18, self.h / 2 - 4, self.icon)
        # Section text
        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(46, self.h / 2 - 4, self.text)

    def wrap(self, *args):
        return self.w, self.h


class KeyTakeawayBanner(Flowable):
    """
    Full-width navy banner for the single most important sentence per chapter.
    REUSE IN EVERY CHAPTER — use once or at most twice per chapter.

    Auto-splits text to two lines if too wide for a single line.
    Height: 0.9 in
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

        # Faint teal quotation-mark decoration
        c.setFillColor(TEAL)
        c.setFont("Helvetica-Bold", 48)
        c.setFillAlpha(0.18)
        c.drawString(8, 2, "\u201c")
        c.setFillAlpha(1)          # IMPORTANT: reset alpha after every transparency use

        # White bold-italic text, centred; split if too wide
        c.setFillColor(WHITE)
        c.setFont("Helvetica-BoldOblique", 11.5)
        tw = c.stringWidth(self.text, "Helvetica-BoldOblique", 11.5)
        if tw > w - 80:
            words = self.text.split()
            mid = len(words) // 2
            l1 = " ".join(words[:mid])
            l2 = " ".join(words[mid:])
            c.drawCentredString(w / 2, h / 2 + 6, l1)
            c.drawCentredString(w / 2, h / 2 - 10, l2)
        else:
            c.drawCentredString(w / 2, h / 2 - 4, self.text)

        # Gold underline
        c.setStrokeColor(GOLD)
        c.setLineWidth(2)
        c.line(w * 0.25, 14, w * 0.75, 14)

    def wrap(self, *args):
        return self.w, self.h


class TryThisBox(Flowable):
    """
    Gold exercise / action-prompt box.
    REUSE IN EVERY CHAPTER — for any "Try This" or hands-on exercise.

    Args:
        lines  List of strings, one per body line.
               Pass "" for a blank spacer line between items.
    Height: calculated from len(lines).
    """

    def __init__(self, w, lines):
        Flowable.__init__(self)
        self.w = w
        self.lines = lines
        self.h = 0.45 * inch + len(lines) * 18 + 16

    def draw(self):
        c = self.canv
        w, h = self.w, self.h

        # Soft-gold background with gold border
        c.setFillColor(SOFT_GOLD)
        c.roundRect(0, 0, w, h, 10, fill=1, stroke=0)
        c.setStrokeColor(GOLD)
        c.setLineWidth(2.5)
        c.roundRect(0, 0, w, h, 10, fill=0, stroke=1)

        # Gold header bar
        c.setFillColor(GOLD)
        c.roundRect(0, h - 34, w, 34, 10, fill=1, stroke=0)
        c.rect(0, h - 34, w, 14, fill=1, stroke=0)   # flatten bottom corners
        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(16, h - 23, "TRY THIS")

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
    Red warning box.
    REUSE IN EVERY CHAPTER — for "Watch Out", caveats, or common mistakes.

    Args:
        lines  List of strings, one per body line.
    Height: calculated from len(lines).
    """

    def __init__(self, w, lines):
        Flowable.__init__(self)
        self.w = w
        self.lines = lines
        self.h = 0.45 * inch + len(lines) * 18 + 16

    def draw(self):
        c = self.canv
        w, h = self.w, self.h

        # Light-red background with red border
        c.setFillColor(colors.HexColor("#FFF3F0"))
        c.roundRect(0, 0, w, h, 10, fill=1, stroke=0)
        c.setStrokeColor(RED_ACCENT)
        c.setLineWidth(2.5)
        c.roundRect(0, 0, w, h, 10, fill=0, stroke=1)

        # Red header bar
        c.setFillColor(RED_ACCENT)
        c.roundRect(0, h - 34, w, 34, 10, fill=1, stroke=0)
        c.rect(0, h - 34, w, 14, fill=1, stroke=0)   # flatten bottom corners
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(16, h - 23, "WATCH OUT")

        # Body lines
        c.setFont("Helvetica", 9.5)
        c.setFillColor(colors.HexColor("#3A1010"))
        ty = h - 50
        for ln in self.lines:
            c.drawString(16, ty, ln)
            ty -= 18

    def wrap(self, *args):
        return self.w, self.h


class NoteBox(Flowable):
    """
    Navy-left-border informational note box (lighter than WatchOut).
    Use for "Why it works", "How this works", context explanations.

    Args:
        label  Short header label, e.g. "WHY IT WORKS"
        lines  List of body strings
    """

    def __init__(self, w, label, lines):
        Flowable.__init__(self)
        self.w = w
        self.label = label
        self.lines = lines
        self.h = 0.45 * inch + len(lines) * 16 + 16

    def draw(self):
        c = self.canv
        w, h = self.w, self.h

        # LIGHT_GRAY background
        c.setFillColor(LIGHT_GRAY)
        c.roundRect(0, 0, w, h, 8, fill=1, stroke=0)

        # NAVY left accent bar
        c.setFillColor(NAVY)
        c.roundRect(0, 0, 5, h, 3, fill=1, stroke=0)

        # Label
        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 8.5)
        c.drawString(16, h - 20, self.label.upper())

        # Separator line
        c.setStrokeColor(MID_GRAY)
        c.setLineWidth(0.5)
        c.line(16, h - 26, w - 16, h - 26)

        # Body lines
        c.setFont("Helvetica", 9)
        c.setFillColor(colors.HexColor("#222222"))
        ty = h - 44
        for ln in self.lines:
            c.drawString(16, ty, ln)
            ty -= 16

    def wrap(self, *args):
        return self.w, self.h


class PageFooter(Flowable):
    """
    Teal-ruled footer with book title (left) and page number (right).
    REUSE IN EVERY CHAPTER — update page_num per chapter.
    Height: 0.35 in
    """

    def __init__(self, w, page_num, book_title):
        Flowable.__init__(self)
        self.w = w
        self.h = 0.35 * inch
        self.page_num = page_num
        self.book_title = book_title

    def draw(self):
        c = self.canv
        # Teal top rule
        c.setStrokeColor(TEAL)
        c.setLineWidth(0.8)
        c.line(0, self.h - 2, self.w, self.h - 2)
        # Text
        c.setFillColor(MID_GRAY)
        c.setFont("Helvetica", 8)
        c.drawString(0, 4, self.book_title)
        page_num = self.canv.getPageNumber() if self.page_num is None else self.page_num
        c.drawRightString(self.w, 4, str(page_num))

    def wrap(self, *args):
        return self.w, self.h


# ══════════════════════════════════════════════════════════════════════════════
# GENERIC INFOGRAPHIC TEMPLATES
# Chapter-specific infographics should subclass or follow these patterns.
# ══════════════════════════════════════════════════════════════════════════════

class SplitPanel(Flowable):
    """
    Generic side-by-side split panel.
    Use for comparisons and before/after examples.

    Args:
        left_config   dict with keys: title, title_color, bg_color, border_color,
                      body_lines (list[str]), result_line (str)
        right_config  same structure as left_config
        height        panel height in inches (default 2.4)
        vs_label      text in the VS badge between panels (default "VS")
    """

    def __init__(self, w, left_config, right_config, height=2.4, vs_label="VS"):
        Flowable.__init__(self)
        self.w = w
        self.h = height * inch
        self.left = left_config
        self.right = right_config
        self.vs_label = vs_label

    def _draw_panel(self, c, x, panel_w, h, cfg):
        # Background
        c.setFillColor(cfg["bg_color"])
        c.roundRect(x, 0, panel_w, h, 8, fill=1, stroke=0)
        c.setStrokeColor(cfg["border_color"])
        c.setLineWidth(1.5)
        c.roundRect(x, 0, panel_w, h, 8, fill=0, stroke=1)

        # Header bar
        c.setFillColor(cfg["title_color"])
        c.roundRect(x, h - 30, panel_w, 30, 8, fill=1, stroke=0)
        c.rect(x, h - 22, panel_w, 14, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 10)
        c.drawCentredString(x + panel_w / 2, h - 20, cfg["title"])

        # Body lines
        c.setFont("Helvetica", 8.5)
        c.setFillColor(colors.HexColor("#333333"))
        ty = h - 48
        for ln in cfg.get("body_lines", []):
            c.drawCentredString(x + panel_w / 2, ty, ln)
            ty -= 14

        # Result box
        if cfg.get("result_line"):
            c.setFillColor(cfg["bg_color"])
            c.roundRect(x + 8, 8, panel_w - 16, 32, 5, fill=1, stroke=0)
            c.setFillColor(cfg["title_color"])
            c.setFont("Helvetica-Bold", 8)
            c.drawCentredString(x + panel_w / 2, 30, "Result:")
            c.setFont("Helvetica", 7.5)
            c.drawCentredString(x + panel_w / 2, 14, cfg["result_line"])

    def draw(self):
        c = self.canv
        w, h = self.w, self.h
        half = w / 2 - 8

        self._draw_panel(c, 0, half, h, self.left)
        self._draw_panel(c, half + 16, half, h, self.right)

        # VS badge between panels
        bx, by = half + 1, h / 2 - 14
        c.setFillColor(GOLD)
        c.circle(bx + 7, by + 14, 14, fill=1, stroke=0)
        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 9)
        c.drawCentredString(bx + 7, by + 10, self.vs_label)

    def wrap(self, *args):
        return self.w, self.h


class IconCardRow(Flowable):
    """
    Horizontal row of 2–5 icon cards.
    Use for numbered frameworks, failure types, item lists.

    Args:
        cards   List of dicts, each with:
                  number      string badge label ("1", "2", ...)
                  title       multi-line title (use \\n to split)
                  example     example text shown in white box at bottom
                  accent      accent color (HexColor)
                  bg          background color (HexColor)
        height  card height in inches (default 2.1)
    """

    def __init__(self, w, cards, height=2.1):
        Flowable.__init__(self)
        self.w = w
        self.h = height * inch
        self.cards = cards

    def draw(self):
        c = self.canv
        w, h = self.w, self.h
        n = len(self.cards)
        pad = 10
        col_w = (w - pad * (n - 1)) / n

        for i, card in enumerate(self.cards):
            x = i * (col_w + pad)
            accent = card["accent"]
            bg = card["bg"]

            # Card background
            c.setFillColor(bg)
            c.roundRect(x, 0, col_w, h, 8, fill=1, stroke=0)
            c.setStrokeColor(accent)
            c.setLineWidth(2)
            c.roundRect(x, 0, col_w, h, 8, fill=0, stroke=1)

            # Number badge
            c.setFillColor(accent)
            c.circle(x + col_w / 2, h - 22, 16, fill=1, stroke=0)
            c.setFillColor(WHITE)
            c.setFont("Helvetica-Bold", 14)
            c.drawCentredString(x + col_w / 2, h - 27, card["number"])

            # Title (multi-line)
            c.setFillColor(NAVY)
            c.setFont("Helvetica-Bold", 9.5)
            yt = h - 52
            for ln in card["title"].split("\n"):
                c.drawCentredString(x + col_w / 2, yt, ln)
                yt -= 13

            # Example box
            if card.get("example"):
                c.setFillColor(WHITE)
                c.roundRect(x + 8, 12, col_w - 16, 52, 5, fill=1, stroke=0)
                c.setFillColor(accent)
                c.setFont("Helvetica-Oblique", 8.5)
                ey = 50
                for ln in card["example"].split("\n"):
                    c.drawCentredString(x + col_w / 2, ey, ln)
                    ey -= 13
                c.setFillColor(MID_GRAY)
                c.setFont("Helvetica", 7.5)
                c.drawCentredString(x + col_w / 2, 16, card.get("example_label", "example \u2191"))

    def wrap(self, *args):
        return self.w, self.h


class OrbitalWheel(Flowable):
    """
    Orbital wheel diagram for 3–7-item frameworks.
    Centre hub with concept label; nodes placed by sin/cos at equal angles;
    spokes connect hub to nodes; right-side legend.

    Args:
        hub_label   Two-line string for the centre circle (use \\n to split)
        nodes       List of dicts, each with:
                      label   Two-line label (use \\n to split)
                      color   HexColor for this node
        legend      List of tuples: (color, bold_text, rest_text)
        legend_title  String above the legend (default "Key")
        height      Diagram height in inches (default 2.7)
    """

    def __init__(self, w, hub_label, nodes, legend, legend_title="Key", height=2.7):
        Flowable.__init__(self)
        self.w = w
        self.h = height * inch
        self.hub_label = hub_label
        self.nodes = nodes
        self.legend = legend
        self.legend_title = legend_title

    def draw(self):
        c = self.canv
        w, h = self.w, self.h

        # Background card
        c.setFillColor(LIGHT_GRAY)
        c.roundRect(0, 0, w, h, 10, fill=1, stroke=0)

        # Centre hub
        cx, cy = w * 0.28, h / 2
        c.setFillColor(NAVY)
        c.circle(cx, cy, 44, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 9)
        hub_lines = self.hub_label.split("\n")
        for j, ln in enumerate(hub_lines):
            offset = (len(hub_lines) - 1) * 5 - j * 10
            c.drawCentredString(cx, cy + offset, ln)

        # Nodes
        n = len(self.nodes)
        r_orbit, r_node, r_hub = 82, 28, 44
        for i, node in enumerate(self.nodes):
            angle = math.radians(i * (360 / n) - 90)
            nx = cx + r_orbit * math.cos(angle)
            ny = cy + r_orbit * math.sin(angle)
            col = node["color"]

            # Spoke
            sx = cx + r_hub * math.cos(angle)
            sy = cy + r_hub * math.sin(angle)
            ex = nx - r_node * math.cos(angle)
            ey = ny - r_node * math.sin(angle)
            c.setStrokeColor(col)
            c.setLineWidth(1.5)
            c.line(sx, sy, ex, ey)

            # Node circle
            c.setFillColor(col)
            c.circle(nx, ny, r_node, fill=1, stroke=0)

            # Node label
            c.setFillColor(WHITE)
            c.setFont("Helvetica-Bold", 7.5)
            node_lines = node["label"].split("\n")
            for j, ln in enumerate(node_lines):
                offset = (len(node_lines) - 1) * 4.5 - j * 9
                c.drawCentredString(nx, ny + offset, ln)

        # Right-side legend
        lx = w * 0.56
        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(lx, h - 22, self.legend_title)
        c.setStrokeColor(TEAL)
        c.setLineWidth(1.5)
        c.line(lx, h - 28, lx + 140, h - 28)

        dy = h - 46
        for col, bold, rest in self.legend:
            c.setFillColor(col)
            c.circle(lx - 8, dy + 4, 4, fill=1, stroke=0)
            c.setFillColor(NAVY)
            c.setFont("Helvetica-Bold", 8.5)
            bw = c.stringWidth(bold, "Helvetica-Bold", 8.5)
            c.drawString(lx, dy, bold)
            c.setFont("Helvetica", 8.5)
            c.setFillColor(colors.HexColor("#444444"))
            c.drawString(lx + bw + 3, dy, rest)
            dy -= 18

    def wrap(self, *args):
        return self.w, self.h


class FlowDiagram(Flowable):
    """
    Horizontal step-flow diagram for 3–6 sequential steps.
    Steps connected by arrows.

    Args:
        steps   List of dicts, each with:
                  number  "1", "2", ...
                  label   Step name
                  detail  Short description (optional)
                colors_cycle  List of fill colors (alternates TEAL/NAVY by default)
        height  in inches (default 1.5)
    """

    def __init__(self, w, steps, height=1.5):
        Flowable.__init__(self)
        self.w = w
        self.h = height * inch
        self.steps = steps

    def draw(self):
        c = self.canv
        w, h = self.w, self.h
        n = len(self.steps)
        arrow_w = 18
        total_arrow = arrow_w * (n - 1)
        box_w = (w - total_arrow) / n
        default_colors = [TEAL, NAVY, TEAL, NAVY, TEAL, NAVY]

        for i, step in enumerate(self.steps):
            x = i * (box_w + arrow_w)
            fill = step.get("color", default_colors[i % len(default_colors)])

            # Step box
            c.setFillColor(fill)
            c.roundRect(x, 0, box_w, h, 6, fill=1, stroke=0)

            # Number label above
            c.setFillColor(GOLD)
            c.setFont("Helvetica-Bold", 7)
            c.drawCentredString(x + box_w / 2, h - 14, step["number"])

            # Step label
            c.setFillColor(WHITE)
            c.setFont("Helvetica-Bold", 8.5)
            label_lines = step["label"].split("\n")
            ly = h / 2 + (len(label_lines) - 1) * 5
            for ln in label_lines:
                c.drawCentredString(x + box_w / 2, ly, ln)
                ly -= 10

            # Detail text
            if step.get("detail"):
                c.setFont("Helvetica", 7)
                c.setFillColor(colors.HexColor("#CCE8E5"))
                c.drawCentredString(x + box_w / 2, 10, step["detail"])

            # Arrow
            if i < n - 1:
                ax = x + box_w
                c.setFillColor(GOLD)
                c.setFont("Helvetica-Bold", 14)
                c.setLineWidth(1.2)
                c.line(ax + 2, h / 2, ax + arrow_w - 5, h / 2)
                c.line(ax + arrow_w - 5, h / 2, ax + arrow_w - 9, h / 2 + 4)
                c.line(ax + arrow_w - 5, h / 2, ax + arrow_w - 9, h / 2 - 4)

    def wrap(self, *args):
        return self.w, self.h


# ══════════════════════════════════════════════════════════════════════════════
# HELPER UTILITIES
# ══════════════════════════════════════════════════════════════════════════════

def styled_table(data, col_widths, header_bg=NAVY, row_bg=LIGHT_GRAY, accent=TEAL):
    """
    Build a styled ReportLab Table with a navy header row and light-gray body rows.

    Args:
        data        List of lists; first row is the header.
        col_widths  List of column widths in points.
        header_bg   Fill color for header row.
        row_bg      Fill color for body rows.
        accent      Border color.

    Returns:
        reportlab.platypus.Table instance ready to append to a story.
    """
    from reportlab.platypus import Table, TableStyle

    hdr_style = ParagraphStyle("TblHdr",
        fontName="Helvetica-Bold", fontSize=8.5, textColor=WHITE,
        alignment=TA_LEFT, leading=11)
    cell_style = ParagraphStyle("TblCell",
        fontName="Helvetica", fontSize=8.5, textColor=colors.HexColor("#222222"),
        alignment=TA_LEFT, leading=12)

    styled_data = []
    for r_idx, row in enumerate(data):
        style = hdr_style if r_idx == 0 else cell_style
        styled_data.append([Paragraph(str(cell), style) for cell in row])

    t = Table(styled_data, colWidths=col_widths)
    ts = [
        ("BACKGROUND", (0, 0), (-1, 0), header_bg),
        ("BACKGROUND", (0, 1), (-1, -1), row_bg),
        ("BOX", (0, 0), (-1, -1), 1.5, accent),
        ("INNERGRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CCCCCC")),
        ("ROWPADDING", (0, 0), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]
    t.setStyle(TableStyle(ts))
    return t
