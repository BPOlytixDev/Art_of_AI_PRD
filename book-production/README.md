# The Art of AI — Book 1 production files

This folder contains the reproducible source and output files for the KDP paperback edition of **The Art of AI — Book 1** by **Mitesh Maharaj**.

## Production decisions

- Trim: 6 × 9 in
- Interior: black and white on white paper
- Interior bleed: none
- Interior margins: 0.65 in top, 0.68 in bottom, 0.72 in binding gutter, 0.56 in outer edge
- Page numbers: centered in the bottom margin on every interior PDF page
- Contents: rendered with dot leaders and page references derived from the final PDF pagination
- Cover: full wrap, modern editorial direction, 0.125 in bleed
- Source of truth: the Markdown files in `source/`

The renderer does not rewrite the manuscript. It converts the supplied Markdown into a print layout, using typography, prompt blocks, callouts, tables, and section openers as the visual system. The cover uses only the title, subtitle, series, author, and deck already present in the manuscript plus the author name supplied for publication.

## Build

From the repository root:

```bash
node book-production/src/build-book.mjs
```

The script:

1. Reads all `source/manuscript_part*.md` files in numeric order.
2. Generates the interior HTML and prints it to PDF with Chromium.
3. Pads the interior to an even page count when needed.
4. Re-renders the Contents until its page references match the final chapter and appendix starts.
5. Calculates the KDP black-and-white white-paper spine width from the final page count.
6. Generates a full-wrap cover PDF with the correct spread dimensions.
7. Writes production metadata and source SHA-256 hashes.

## Outputs

- `output/the-art-of-ai-book-1-interior.pdf`
- `output/the-art-of-ai-book-1-full-wrap-cover.pdf`
- `output/the-art-of-ai-book-1-complete-book.pdf` — full-wrap cover followed by the complete interior
- `output/the-art-of-ai-book-1-metadata.json`

The cover reserves a blank white barcode area on the back cover. If an ISBN is supplied by the publisher, update the metadata and replace the reserved area with the final barcode before upload, or allow KDP to place the barcode.

## Final KDP checks before upload

- Confirm author name, ISBN, and marketplace metadata in KDP.
- Upload the interior and cover separately in KDP Paperback.
- Review the KDP Print Previewer for trim, margins, widows/orphans, and any font substitutions.
- Confirm that the cover preview shows the intended barcode treatment.
- Rebuild after any manuscript edit so the interior page count and cover spine are recalculated together.