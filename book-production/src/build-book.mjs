import { execFileSync } from "node:child_process";
import { createHash } from "node:crypto";
import { copyFile, mkdir, readFile, readdir, rename, writeFile } from "node:fs/promises";
import { readFileSync } from "node:fs";
import { basename, dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { inlineMarkdown, renderMarkdown } from "./markdown.mjs";

const here = dirname(fileURLToPath(import.meta.url));
const root = resolve(here, "..");
const repositoryRoot = resolve(root, "..");
const sourceDir = join(root, "source");
const outputDir = join(root, "output");
const generatedDir = join(root, ".generated");
const python = "/tmp/art-of-ai-pdfvenv/bin/python";
const pdfTextTool = join(here, "pdf_text.py");
const css = await readFile(join(here, "style.css"), "utf8");
const author = "Eleanor Mercer";
const title = "The Art of AI";
const subtitle = "How to Get Better Results From Every AI Conversation";
const deck = "A Practical Guide to Better Prompts, Better Context, and Better Workflows";
const series = "The Art of AI, Book 1";

await mkdir(outputDir, { recursive: true });
await mkdir(generatedDir, { recursive: true });

const productionSourceFiles = (await readdir(sourceDir))
  .filter((name) => name.endsWith(".md"))
  .sort((a, b) => {
    const partA = Number(a.match(/part(\d+)/)?.[1] ?? 0);
    const partB = Number(b.match(/part(\d+)/)?.[1] ?? 0);
    return partA - partB;
  });

const sourceSpecs = [
  ...productionSourceFiles.map((name) => ({ name, path: join(sourceDir, name) })),
].sort((a, b) => {
  const partA = Number(a.name.match(/part(\d+)/)?.[1] ?? 0);
  const partB = Number(b.name.match(/part(\d+)/)?.[1] ?? 0);
  return partA - partB;
});
const sourceFiles = sourceSpecs.map(({ name }) => name);

if (sourceFiles.length < 4) {
  throw new Error("Expected four manuscript parts before building the final book.");
}

const sourceTexts = await Promise.all(
  sourceSpecs.map(async ({ name, path }) => ({
    name,
    text: await readFile(path, "utf8"),
  })),
);

const firstLines = sourceTexts[0].text.split(/\r?\n/);
const copyrightStart = firstLines.findIndex((line) => /^## COPYRIGHT$/.test(line.trim()));
const contentsStart = firstLines.findIndex((line) => /^## CONTENTS$/.test(line.trim()));
const introductionStart = firstLines.findIndex((line) => /^## INTRODUCTION$/.test(line.trim()));
const dedication = firstLines.find(
  (line, index) => index > 6 && index < copyrightStart && /^\*[^*].*\*$/.test(line.trim()),
);

if (copyrightStart < 0 || contentsStart < 0 || introductionStart < 0) {
  throw new Error("The first manuscript part is missing the expected front matter headings.");
}

const bodyParts = [
  firstLines.slice(introductionStart),
  ...sourceTexts.slice(1).map(({ text }) => text.split(/\r?\n/)),
];
const bodyLines = bodyParts.flat();
const renderBodyLines = bodyLines;

const indexTerms = [
  { term: "7 Questions", searches: ["7 Questions"] },
  { term: "AI Interaction Stack", searches: ["AI Interaction Stack"] },
  { term: "chains", searches: ["chains"] },
  { term: "code execution", searches: ["code execution"] },
  { term: "context", searches: ["context"] },
  { term: "context documents", searches: ["context document", "context documents"] },
  { term: "context drift", searches: ["context drift"] },
  { term: "constraints", searches: ["constraints"] },
  { term: "Deep Research", searches: ["Deep Research"] },
  { term: "examples", searches: ["examples"] },
  { term: "few-shot prompting", searches: ["few-shot prompting", "few shot prompting"] },
  { term: "hallucination", searches: ["hallucination", "hallucinations"] },
  { term: "handoffs", searches: ["handoffs", "handoff"] },
  { term: "instructions", searches: ["instructions"] },
  { term: "iteration", searches: ["iteration", "iterative"] },
  { term: "memory", searches: ["memory"] },
  { term: "output format", searches: ["output format"] },
  { term: "persistent instructions", searches: ["persistent instructions"] },
  { term: "privacy", searches: ["privacy"] },
  { term: "Projects", searches: ["Projects"] },
  { term: "prompt injection", searches: ["prompt injection"] },
  { term: "role", searches: ["role"] },
  { term: "source material", searches: ["source material"] },
  { term: "sycophancy", searches: ["sycophancy"] },
  { term: "verification", searches: ["verification", "verify"] },
  { term: "web search", searches: ["web search"] },
  { term: "workflows", searches: ["workflows", "workflow"] },
];

function contentsEntries() {
  const entries = [];
  let currentPart = null;
  let pendingSection = null;

  for (const line of renderBodyLines) {
    const part = line.match(/^# (PART [IVX]+|APPENDICES)$/i);
    if (part) {
      currentPart = {
        kind: "part",
        id: part[1].toLowerCase().replaceAll(" ", "-"),
        label: part[1],
        title: "",
        searches: [part[1]],
      };
      entries.push(currentPart);
      pendingSection = null;
      continue;
    }

    const levelTwo = line.match(/^## (.+)$/);
    if (levelTwo) {
      const heading = levelTwo[1];
      if (/^A Note on Sources$/i.test(heading)) {
        entries.push({ kind: "index", id: "index", label: "Index", searches: ["Index"] });
      }
      if (/^INTRODUCTION$/i.test(heading)) {
        pendingSection = {
          kind: "intro",
          id: "introduction",
          label: heading,
          title: "",
          searches: [heading],
        };
        entries.push(pendingSection);
      } else if (/^Chapter \d+$/i.test(heading)) {
        pendingSection = {
          kind: "chapter",
          id: heading.toLowerCase().replaceAll(" ", "-"),
          label: heading,
          title: "",
          searches: [heading],
        };
        entries.push(pendingSection);
      } else if (/^Appendix [A-E]$/i.test(heading)) {
        pendingSection = {
          kind: "appendix",
          id: heading.toLowerCase().replaceAll(" ", "-"),
          label: heading,
          title: "",
          searches: [heading],
          children: [],
        };
        entries.push(pendingSection);
      } else if (currentPart?.label !== "APPENDICES" && currentPart?.title === "") {
        currentPart.title = heading;
        currentPart.searches.push(heading);
      } else if (currentPart?.label === "PART V") {
        entries.push({ kind: "category", id: `category-${entries.length}`, label: heading });
      } else {
        entries.push({
          kind: "section",
          id: `section-${entries.length}`,
          label: heading,
          searches: [heading],
        });
      }
      continue;
    }

    const titleHeading = line.match(/^### (.+)$/);
    if (!titleHeading) continue;
    const heading = titleHeading[1];

    if (pendingSection && !pendingSection.title) {
      pendingSection.title = heading;
      pendingSection.searches.push(heading);
      continue;
    }

    if (currentPart?.label === "APPENDICES" && /^E\d+\s*,/.test(heading)) {
      const appendix = entries.find((entry) => entry.id === "appendix-e");
      appendix?.children.push({
        kind: "appendix-child",
        id: heading.toLowerCase().replaceAll(" ", "-"),
        label: heading,
        searches: [heading],
      });
      continue;
    }

    if (currentPart?.label === "PART V" && /^W\d+\s*,/.test(heading)) {
      entries.push({
        kind: "workflow",
        id: heading.toLowerCase().replaceAll(" ", "-"),
        label: heading,
        searches: [heading],
      });
    }
  }

  return entries;
}

function normalizePdfText(value) {
  return value
    .replace(/\u00ad/g, "")
    .replace(/[“”]/g, '"')
    .replace(/[‘’]/g, "'")
    .replace(/\s+/g, " ")
    .trim()
    .toLowerCase();
}

function compactPdfText(value) {
  return normalizePdfText(value).replace(/[^a-z0-9]+/g, "");
}

function pageTextsFromPdf(pdfPath) {
  const textPath = join(generatedDir, "pdf-text.txt");
  execFileSync(python, [pdfTextTool, "text", pdfPath, textPath], { stdio: "inherit" });
  const text = readFileSync(textPath, "utf8");
  return text.split("\f");
}

function pageForSearches(pageTexts, searches, startPage) {
  const normalizedSearches = searches.map(normalizePdfText).filter(Boolean);
  const compactSearches = searches.map(compactPdfText).filter(Boolean);
  for (let index = startPage - 1; index < pageTexts.length; index += 1) {
    const page = pageTexts[index];
    const compactPage = compactPdfText(page);
    if (
      normalizedSearches.some((search) => page.includes(search)) ||
      compactSearches.some((search) => compactPage.includes(search))
    ) {
      return index + 1;
    }
  }
  return null;
}

function contentsPageMap(pdfPath) {
  const rawPageTexts = pageTextsFromPdf(pdfPath);
  const pageTexts = rawPageTexts.map(normalizePdfText);
  const introductionPages = pageTexts
    .map((page, index) => (page.includes("introduction") ? index + 1 : null))
    .filter(Boolean);
  const introTitlePages = pageTexts
    .map((page, index) => (page.includes("you are not bad at ai") ? index + 1 : null))
    .filter(Boolean);
  const bodyStartPage = introTitlePages.at(-1) ?? introductionPages.at(-1) ?? 5;
  const pageMap = new Map();

  function headingPageFor(entry, minimumPage = bodyStartPage) {
    const label = compactPdfText(entry.label);
    const title = compactPdfText(entry.title ?? "");
    return rawPageTexts.findIndex((rawPage, index) => {
      if (index + 1 < minimumPage) return false;
      const pageLines = rawPage
        .split(/\r?\n/)
        .map((line) => line.trim())
        .filter(Boolean)
        .map(compactPdfText);
      // A part title can be mentioned in prose on an earlier page. Requiring
      // both the exact part label and its title identifies the actual divider.
      return pageLines.includes(label) && (!title || compactPdfText(rawPage).includes(title));
    }) + 1;
  }

  let activePartPage = bodyStartPage - 1;
  for (const entry of contentsEntries()) {
    const minimumHeadingPage =
      entry.kind === "chapter" ? Math.max(bodyStartPage, activePartPage + 1) : bodyStartPage;
    const headingPage = ["intro", "part", "chapter", "appendix"].includes(entry.kind)
      ? headingPageFor(entry, minimumHeadingPage)
      : 0;
    const page =
      headingPage > 0
        ? headingPage
        : pageForSearches(pageTexts, entry.searches ?? [], bodyStartPage);
    if (page) pageMap.set(entry.id, page);
    if (entry.kind === "part" && page) activePartPage = page;
    for (const child of entry.children ?? []) {
      const childPage = pageForSearches(pageTexts, child.searches, bodyStartPage);
      if (childPage) pageMap.set(child.id, childPage);
    }
  }
  return pageMap;
}

function contentsRow(entry, pageMap) {
  const page = pageMap?.get(entry.id);
  const pageLabel = page ? String(page) : "00";
  const title = entry.title ? `${entry.label}, ${entry.title}` : entry.label;
  const className = `contents-entry contents-${entry.kind}`;
  return `<li class="${className}"><span class="contents-entry-title">${inlineMarkdown(title)}</span><span class="contents-leader" aria-hidden="true"></span><span class="contents-page-number">${pageLabel}</span></li>`;
}

function contentsFromHeadings(pageMap) {
  return contentsEntries()
    .map((entry) => {
      if (entry.kind === "category") {
        return `<li class="contents-category">${inlineMarkdown(entry.label)}</li>`;
      }
      const children = (entry.children ?? [])
        .map((child) => contentsRow(child, pageMap))
        .join("\n");
      return `${contentsRow(entry, pageMap)}${children}`;
    })
    .join("\n");
}

function indexPageNumbers(pdfPath) {
  const rawPageTexts = pageTextsFromPdf(pdfPath);
  const pageTexts = rawPageTexts.map(normalizePdfText);
  const introTitlePages = pageTexts
    .map((page, index) => (page.includes("you are not bad at ai") ? index + 1 : null))
    .filter(Boolean);
  const introductionPages = pageTexts
    .map((page, index) => (page.includes("introduction") ? index + 1 : null))
    .filter(Boolean);
  const bodyStartPage = introTitlePages.at(-1) ?? introductionPages.at(-1) ?? 5;
  const sourcePage = pageForSearches(pageTexts, ["A Note on Sources"], bodyStartPage) ?? pageTexts.length + 1;
  const indexStart = rawPageTexts.findIndex((page, pageIndex) => {
    if (pageIndex + 1 < bodyStartPage || pageIndex + 1 >= sourcePage) return false;
    return page
      .split(/\r?\n/)
      .map((line) => compactPdfText(line))
      .includes("index");
  }) + 1;
  const indexPages = new Set();
  if (indexStart > 0) {
    for (let pageIndex = indexStart; pageIndex < sourcePage; pageIndex += 1) {
      indexPages.add(pageIndex);
    }
  }

  return indexTerms
    .map(({ term, searches }) => {
      const pages = new Set();
      const normalizedSearches = searches.map(normalizePdfText);
      for (let pageIndex = bodyStartPage; pageIndex < sourcePage; pageIndex += 1) {
        if (indexPages.has(pageIndex)) continue;
        const page = pageTexts[pageIndex - 1];
        if (normalizedSearches.some((search) => page.includes(search))) pages.add(pageIndex);
      }
      return { term, pages: [...pages].sort((a, b) => a - b) };
    })
    .filter(({ pages }) => pages.length > 0);
}

function renderIndex(pdfPath) {
  if (!pdfPath) {
    return `<section class="index-page"><h2 class="index-heading">Index</h2><p class="index-pending">Index page references will be generated after the first layout pass.</p></section>`;
  }
  const entries = indexPageNumbers(pdfPath)
    .map(({ term, pages }) => `<div class="index-entry"><span class="index-term">${inlineMarkdown(term)}</span><span class="index-pages">${pages.join(", ")}</span></div>`)
    .join("\n");
  return `<section class="index-page"><h2 class="index-heading">Index</h2><div class="index-columns">${entries}</div></section>`;
}

function renderBody(pageMap, pdfPath) {
  const insertion = renderBodyLines.findIndex((line) => /^## A Note on Sources$/i.test(line.trim()));
  if (insertion < 0) return renderMarkdown(renderBodyLines);
  const before = renderBodyLines.slice(0, insertion);
  const after = renderBodyLines.slice(insertion);
  return `${renderMarkdown(before)}${renderIndex(pdfPath)}${renderMarkdown(after)}`;
}

function renderFrontMatter() {
  return `
    <section class="front-matter-page title-page">
      <p class="eyebrow">${inlineMarkdown(series)}</p>
      <h1>${inlineMarkdown(title)}</h1>
      <p class="subtitle">${inlineMarkdown(subtitle)}</p>
      <p class="deck">${inlineMarkdown(deck)}</p>
      <p class="author">${inlineMarkdown(author)}</p>
      <p class="series-line">First edition · 2026</p>
    </section>
    <section class="front-matter-page dedication-page">
      <p>${inlineMarkdown(dedication.replace(/^\*|\*$/g, ""))}</p>
    </section>
    <section class="front-matter-page copyright-page">
      ${renderMarkdown(firstLines.slice(copyrightStart, contentsStart))}
    </section>
    <section class="front-matter-page contents-page">
      <h2>Contents</h2>
      <ul>${contentsFromHeadings(pageMap)}</ul>
    </section>
  `;
}

function htmlDocument(body, pageSize = "6in 9in", extraCss = "") {
  const pageRule =
    pageSize === "6in 9in"
      ? `@page { size: ${pageSize}; }`
      : `@page { size: ${pageSize}; margin: 0; @bottom-center { content: none; } }`;
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>${title}, Book 1</title>
  <meta name="author" content="${author}">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>${css}\n${extraCss}\n${pageRule}</style>
</head>
<body>${body}</body>
</html>`;
}

const interiorHtmlPath = join(generatedDir, "interior.html");
const interiorPdfPath = join(outputDir, "the-art-of-ai-book-1-interior.pdf");

function printPdf(htmlPath, pdfPath) {
  execFileSync(
    process.env.ART_OF_AI_CHROME ?? "chromium",
    [
      "--headless=new",
      "--no-sandbox",
      "--disable-gpu",
      "--hide-scrollbars",
      "--no-pdf-header-footer",
      `--print-to-pdf=${pdfPath}`,
      `file://${htmlPath}`,
    ],
    { stdio: "inherit" },
  );
}

function pdfPageCount(pdfPath) {
  return Number(execFileSync(python, [pdfTextTool, "count", pdfPath], { encoding: "utf8" }).trim());
}

function buildInteriorHtml(pageMap, addBlankPage) {
  const blankPage = addBlankPage ? '<div class="blank-page" aria-hidden="true"></div>' : "";
  return htmlDocument(
    `<div class="page-number" aria-hidden="true"></div><main class="book">${renderFrontMatter(pageMap)}<article class="manuscript">${renderBody(pageMap, interiorPdfPath)}</article>${blankPage}</main>`,
  );
}

function headerPlan(pageMap, pdfPath) {
  const entries = contentsEntries();
  const pageCount = pdfPageCount(pdfPath);
  const bodyStart = Math.min(...entries.map((entry) => pageMap.get(entry.id) ?? Number.MAX_SAFE_INTEGER));
  const parts = entries.filter((entry) => entry.kind === "part");
  const sections = entries.filter((entry) =>
    ["intro", "chapter", "appendix", "appendix-child", "workflow", "index"].includes(entry.kind),
  );
  const backMatterStart = Math.min(
    ...entries
      .filter((entry) => ["A Note on Sources", "About the Author", "About This Book"].includes(entry.label))
      .map((entry) => pageMap.get(entry.id) ?? Infinity),
  );
  const headerText = (entry) => entry.title ? `${entry.label} - ${entry.title}` : entry.label;
  const plan = [];
  for (let page = 1; page <= pageCount; page += 1) {
    const part = [...parts].reverse().find((entry) => (pageMap.get(entry.id) ?? Infinity) <= page);
    const section = [...sections].reverse().find((entry) => (pageMap.get(entry.id) ?? Infinity) <= page);
    const isOpener = [part, section].some((entry) => entry && pageMap.get(entry.id) === page);
    const isBackMatter = page >= (pageMap.get("index") ?? Infinity);
    const header = { left: "", right: "" };
    if (page >= bodyStart && !isOpener && !isBackMatter && part) {
      header.left = headerText(part).toUpperCase();
      if (section) header.right = headerText(section);
    } else if (
      isBackMatter &&
      section &&
      section.kind === "index" &&
      page > pageMap.get("index") &&
      page < backMatterStart
    ) {
      header.right = "INDEX";
    }
    if (page % 2 === 0) {
      plan.push({ left: header.left });
    } else {
      plan.push({ right: header.right });
    }
  }
  return plan;
}

let pageMap = null;
let pageCount = 0;
for (let attempt = 0; attempt < 4; attempt += 1) {
  const provisionalHtml = buildInteriorHtml(pageMap, false);
  await writeFile(interiorHtmlPath, provisionalHtml);
  printPdf(interiorHtmlPath, interiorPdfPath);
  pageCount = pdfPageCount(interiorPdfPath);

  if (pageCount % 2 !== 0) {
    const paddedHtml = buildInteriorHtml(pageMap, true);
    await writeFile(interiorHtmlPath, paddedHtml);
    printPdf(interiorHtmlPath, interiorPdfPath);
    pageCount = pdfPageCount(interiorPdfPath);
  }

  const nextPageMap = contentsPageMap(interiorPdfPath);
  const sameMap =
    pageMap &&
    [...nextPageMap.entries()].length === [...pageMap.entries()].length &&
    [...nextPageMap.entries()].every(([id, page]) => pageMap.get(id) === page);
  pageMap = nextPageMap;
  if (sameMap) break;
}

const headerPlanPath = join(generatedDir, "running-headers.json");
const headerOutputPath = join(generatedDir, "interior-with-headers.pdf");
await writeFile(headerPlanPath, JSON.stringify(headerPlan(pageMap, interiorPdfPath), null, 2));
execFileSync(python, [join(here, "add-running-headers.py"), interiorPdfPath, headerOutputPath, headerPlanPath], { stdio: "inherit" });
await rename(headerOutputPath, interiorPdfPath);
const completeInteriorPdfPath = join(outputDir, "Complete_Interior.pdf");
await copyFile(interiorPdfPath, completeInteriorPdfPath);

const bleed = 0.125;
const trimWidth = 6;
const trimHeight = 9;
const spineWidth = pageCount * 0.002252;
const coverWidth = bleed * 2 + trimWidth * 2 + spineWidth;
const coverHeight = bleed * 2 + trimHeight;
const frontX = bleed + trimWidth + spineWidth;

const coverSvg = `
<svg class="cover-art" viewBox="0 0 1200 900" role="img" aria-label="Abstract editorial cover artwork">
  <rect width="1200" height="900" fill="#efe9de"/>
  <path d="M0 700 C210 570 240 160 520 210 C690 240 670 560 870 595 C1010 620 1070 510 1200 450 L1200 900 L0 900 Z" fill="#1e2428"/>
  <path d="M0 600 C190 470 280 120 470 160 C620 190 660 445 820 485 C1000 530 1060 420 1200 350 L1200 415 C1040 495 1005 580 835 545 C640 505 610 245 465 220 C300 190 260 545 0 665 Z" fill="#b43d2e"/>
  <circle cx="925" cy="220" r="88" fill="#b43d2e"/>
  <circle cx="925" cy="220" r="34" fill="#efe9de"/>
  <path d="M860 220h130M925 155v130" stroke="#1e2428" stroke-width="8"/>
  <path d="M130 210h290M130 245h180" stroke="#1e2428" stroke-width="9" opacity=".72"/>
</svg>`;

const coverHtml = htmlDocument(
  `<main class="cover" style="--cover-width:${coverWidth}in;--cover-height:${coverHeight}in;--front-x:${frontX}in;--spine:${spineWidth}in">
    <div class="cover-back">
      <div class="back-rule"></div>
      <p class="back-series">${inlineMarkdown(series)}</p>
      <p class="back-deck">${inlineMarkdown(deck)}</p>
      <div class="barcode-reserve" aria-label="Reserved barcode area"></div>
    </div>
    <div class="cover-spine"><span>${inlineMarkdown(title)} · ${inlineMarkdown(author)}</span></div>
    <div class="cover-front">
      ${coverSvg}
      <div class="front-copy">
        <p class="front-series">${inlineMarkdown(series)}</p>
        <h1>${inlineMarkdown(title)}</h1>
        <p class="front-subtitle">${inlineMarkdown(subtitle)}</p>
        <p class="front-deck">${inlineMarkdown(deck)}</p>
        <p class="front-author">${inlineMarkdown(author)}</p>
      </div>
    </div>
  </main>`,
  `${coverWidth}in ${coverHeight}in`,
  `
  .cover { position: relative; width: var(--cover-width); height: var(--cover-height); overflow: hidden; background: #efe9de; color: #1e2428; font-family: Arial, Helvetica, sans-serif; }
  .cover-back, .cover-front { position: absolute; top: 0; height: var(--cover-height); overflow: hidden; }
  .cover-back { left: 0; width: ${bleed + trimWidth}in; padding: 0.72in 0.72in 0.52in 0.72in; background: #efe9de; }
  .cover-front { left: var(--front-x); width: ${trimWidth + bleed}in; background: #efe9de; }
  .cover-spine { position: absolute; left: ${bleed + trimWidth}in; top: 0; width: var(--spine); height: var(--cover-height); background: #b43d2e; color: #efe9de; display: flex; align-items: center; justify-content: center; overflow: hidden; z-index: 3; }
  .cover-spine span { transform: rotate(-90deg); white-space: nowrap; font-size: 8pt; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; }
  .cover-art { position: absolute; inset: 0; width: 100%; height: 100%; }
  .front-copy { position: absolute; inset: 0; display: flex; flex-direction: column; padding: 0.7in 0.62in 0.62in 0.62in; }
  .front-series, .back-series { margin: 0; color: #b43d2e; font-size: 8pt; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; }
  .front-copy h1 { margin: .22in 0 0; max-width: 4.6in; color: #1e2428; font-size: 35pt; letter-spacing: -.065em; line-height: .88; }
  .front-subtitle { max-width: 3.8in; margin: .22in 0 0; color: #1e2428; font-family: Georgia, serif; font-size: 15pt; line-height: 1.05; }
  .front-deck { max-width: 3.6in; margin: .18in 0 0; color: #544c44; font-family: Georgia, serif; font-size: 9.5pt; line-height: 1.25; }
  .front-author { margin: auto 0 0; color: #efe9de; font-size: 9pt; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; }
  .back-rule { width: .62in; height: .075in; margin-bottom: .42in; background: #b43d2e; }
  .back-deck { max-width: 3.8in; margin: .3in 0 0; color: #1e2428; font-family: Georgia, serif; font-size: 15pt; line-height: 1.1; }
  .back-note { max-width: 3.45in; margin-top: .22in; color: #544c44; font-family: Georgia, serif; font-size: 10pt; line-height: 1.32; }
  .barcode-reserve { position: absolute; right: .52in; bottom: .45in; width: 1.5in; height: .9in; background: #fff; }
  `,
);
const coverHtmlPath = join(generatedDir, "cover.html");
const coverPdfPath = join(outputDir, "the-art-of-ai-book-1-full-wrap-cover.pdf");
const completeBookPdfPath = join(outputDir, "the-art-of-ai-book-1-complete-book.pdf");
await writeFile(coverHtmlPath, coverHtml);
printPdf(coverHtmlPath, coverPdfPath);
const coverSizedPath = join(generatedDir, "cover-sized.pdf");
execFileSync(
  python,
  [pdfTextTool, "resize", coverPdfPath, String(coverWidth * 72), String(coverHeight * 72), coverSizedPath],
  { stdio: "inherit" },
);
await rename(coverSizedPath, coverPdfPath);
execFileSync(python, [pdfTextTool, "merge", coverPdfPath, interiorPdfPath, completeBookPdfPath], { stdio: "inherit" });

const fileHashes = Object.fromEntries(
  await Promise.all(
    sourceTexts.map(async ({ name, text }) => [name, createHash("sha256").update(text).digest("hex")]),
  ),
);

const metadata = {
  title,
  subtitle,
  author,
  series: "The Art of AI",
  seriesNumber: 1,
  edition: "First edition",
  publicationYear: 2026,
  language: "en",
  trimSizeInches: { width: 6, height: 9 },
  interior: {
    color: "black-and-white",
    paper: "white",
    bleed: false,
    marginsInches: {
      top: 0.65,
      bottom: 0.68,
      inside: 0.72,
      outside: 0.56,
    },
  },
  cover: { style: "modern editorial", bleed: 0.125, spineWidthInches: Number(spineWidth.toFixed(4)) },
  pageCount,
  isbn: null,
  kdpBarcode: "reserved-for-KDP-or-publisher-supplied-ISBN",
  sourceFiles,
  sourceSha256: fileHashes,
  outputs: {
    completeInteriorPdf: "output/Complete_Interior.pdf",
    interiorPdf: "output/the-art-of-ai-book-1-interior.pdf",
    fullWrapCoverPdf: "output/the-art-of-ai-book-1-full-wrap-cover.pdf",
    completeBookPdf: "output/the-art-of-ai-book-1-complete-book.pdf",
    metadataJson: "output/the-art-of-ai-book-1-metadata.json",
  },
  contentsNote:
    "The production contents list is generated from the supplied headings so Appendices D and E are included.",
  generatedAt: new Date().toISOString(),
};
await writeFile(
  join(outputDir, "the-art-of-ai-book-1-metadata.json"),
  `${JSON.stringify(metadata, null, 2)}\n`,
);

console.log(
  JSON.stringify(
    {
      sourceFiles,
      pageCount,
      spineWidthInches: Number(spineWidth.toFixed(4)),
      interiorPdf: interiorPdfPath,
      coverPdf: coverPdfPath,
    },
    null,
    2,
  ),
);
