# The Art of AI — Book 1

Production source and reproducible PDF renderer for the 6 × 9 in KDP paperback edition of *The Art of AI — Book 1* by Mitesh Maharaj.

## Run & Operate

- `pnpm --filter @workspace/api-server run dev` — run the API server (port 5000)
- `pnpm run typecheck` — full typecheck across all packages
- `pnpm run build` — typecheck + build all packages
- `pnpm --filter @workspace/api-spec run codegen` — regenerate API hooks and Zod schemas from the OpenAPI spec
- `pnpm --filter @workspace/db run push` — push DB schema changes (dev only)
- Required env: `DATABASE_URL` — Postgres connection string
- `pnpm run build:book` — render the interior PDF, calculate the final page count, and render the full-wrap cover PDF

## Stack

- pnpm workspaces, Node.js 24, TypeScript 5.9
- API: Express 5
- DB: PostgreSQL + Drizzle ORM
- Validation: Zod (`zod/v4`), `drizzle-zod`
- API codegen: Orval (from OpenAPI spec)
- Build: esbuild (CJS bundle)

## Where things live

- `book-production/source/` — source Markdown manuscript parts; do not edit the generated PDFs directly
- `book-production/src/build-book.mjs` — end-to-end renderer and KDP cover-spine calculation
- `book-production/src/markdown.mjs` — Markdown-to-print HTML conversion
- `book-production/src/style.css` — print typography and layout system
- `book-production/output/` — generated interior PDF, full-wrap cover PDF, and production metadata JSON

## Architecture decisions

- The Markdown manuscript is the source of truth; the renderer adds only layout, navigation, and visual treatment.
- The production format is 6 × 9 in, black and white on white paper, with no interior bleed.
- Cover spine width is calculated from the rendered interior page count using the KDP black-and-white white-paper factor.
- The Contents page is generated from the final heading structure so later manuscript parts cannot silently be omitted.
- Interior page numbers are printed in the bottom margin, and Contents references are remapped from the final rendered PDF.

## Product

The repository produces the publication-ready files for a practical nonfiction book on prompts, context, workflows, verification, and responsible AI use.

## User preferences

- Do not deviate from the manuscript; do not add invented content to the book or cover copy.
- Prioritize a high-quality, editorial design over generic AI styling.

## Gotchas

- Rebuild after any manuscript change so the interior page count and cover spine stay synchronized.
- ISBN and barcode placement still need publisher/KDP confirmation before upload.

## Pointers

- See the `pnpm-workspace` skill for workspace structure, TypeScript setup, and package details
