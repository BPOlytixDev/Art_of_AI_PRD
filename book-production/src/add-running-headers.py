import json
import sys
from pathlib import Path

import pymupdf as fitz


PAGE_WIDTH = 432
PAGE_HEIGHT = 648


FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def overlay_pdf(input_path, headers, output_path):
    document = fitz.open(input_path)
    font = fitz.Font(fontfile=FONT_PATH)
    for page, header in zip(document, headers):
        left = header.get("left", "")
        right = header.get("right", "")
        if left:
            page.insert_text(
                (40, 616),
                left,
                fontsize=7.5,
                fontfile=FONT_PATH,
                fontname="HeaderSans",
                color=(0.40, 0.39, 0.36),
            )
        if right:
            width = min(280, font.text_length(right, fontsize=7.5))
            page.insert_text(
                (392 - width, 616),
                right,
                fontsize=7.5,
                fontfile=FONT_PATH,
                fontname="HeaderSans",
                color=(0.40, 0.39, 0.36),
            )
    document.save(output_path, garbage=4, deflate=True)
    document.close()


def main():
    input_path, output_path, plan_path = sys.argv[1:4]
    headers = json.loads(Path(plan_path).read_text())
    overlay_pdf(input_path, headers, output_path)


if __name__ == "__main__":
    main()
