---
name: Chromium PDF pagination
description: Renderer-specific rules for reliable page numbers and Contents references in the book PDF pipeline.
---

Use Chromium print margin boxes with `@bottom-center { content: counter(page); }` for interior page numbers. A fixed HTML footer using `counter(page)` rendered as zero in this environment.

**Why:** Chromium's fixed-position page counter is not connected to the paged-media counter in this print path, while the margin-box counter produces the actual physical PDF page number.

**How to apply:** Keep Contents references derived from the final rendered PDF, not from source-line estimates. When layout changes, render, extract heading locations, update the Contents, and render again until the references stabilize.