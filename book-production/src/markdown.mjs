import { renderVisual, renderWorkflowMeta } from "./visuals.mjs";

const escapeHtml = (value) =>
  value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");

export function inlineMarkdown(value) {
  const escaped = escapeHtml(value);
  return escaped
    .replace(/`([^`]+)`/g, "<code>$1</code>")
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
    .replace(/\*([^*]+)\*/g, "<em>$1</em>")
    .replace(/  $/, "<br>");
}

function isTableSeparator(line) {
  return /^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$/.test(line);
}

function tableCells(line) {
  const trimmed = line.trim().replace(/^\|/, "").replace(/\|$/, "");
  return trimmed.split("|").map((cell) => cell.trim());
}

function renderTable(lines) {
  const headers = tableCells(lines[0]);
  const bodyRows = lines.slice(2).map(tableCells);
  return [
    '<div class="table-wrap"><table><thead><tr>',
    headers.map((cell) => `<th>${inlineMarkdown(cell)}</th>`).join(""),
    "</tr></thead><tbody>",
    bodyRows
      .map(
        (row) =>
          `<tr>${headers
            .map((_, index) => `<td>${inlineMarkdown(row[index] ?? "")}</td>`)
            .join("")}</tr>`,
      )
      .join(""),
    "</tbody></table></div>",
  ].join("");
}

function renderList(lines, ordered, className = "") {
  const tag = ordered ? "ol" : "ul";
  const matcher = ordered ? /^\s*\d+\.\s+(.*)$/ : /^\s*[-*]\s+(.*)$/;
  const classAttribute = className ? ` class="${className}"` : "";
  const items = lines
    .map((line) => line.match(matcher)?.[1] ?? line.trim())
    .map((item) => `<li>${inlineMarkdown(item)}</li>`)
    .join("");
  return `<${tag}${classAttribute}>${items}</${tag}>`;
}

function partChapters(lines, startIndex) {
  const chapters = [];
  for (let index = startIndex + 1; index < lines.length; index += 1) {
    if (/^# (PART [IVX]+|APPENDICES)$/i.test(lines[index].trim())) break;
    const chapter = lines[index].match(/^## (Chapter \d+)$/i);
    if (!chapter) continue;
    let next = index + 1;
    while (next < lines.length && !lines[next].trim()) next += 1;
    const title = lines[next]?.match(/^### (.+)$/)?.[1];
    if (title) chapters.push({ label: chapter[1], title });
  }
  return chapters;
}

function renderPartOverview(chapters) {
  if (!chapters.length) return "";
  return `<section class="part-overview" aria-label="Chapters in this part">
    <p class="part-overview-label">In this part</p>
    <div class="part-overview-grid">
      ${chapters
        .map(
          ({ label, title }) =>
            `<div class="part-overview-card"><span class="part-overview-number">${inlineMarkdown(label)}</span><span class="part-overview-title">${inlineMarkdown(title)}</span></div>`,
        )
        .join("\n")}
    </div>
  </section>`;
}

export function renderMarkdown(source) {
  const lines = Array.isArray(source) ? source : source.split(/\r?\n/);
  const output = [];
  let index = 0;
  let currentPart = null;
  let currentAppendix = null;
  let partOverviewPending = false;
  let partOverviewChapters = [];

  while (index < lines.length) {
    const line = lines[index];
    if (!line.trim()) {
      index += 1;
      continue;
    }

    if (line.trim().startsWith("<!--")) {
      const visualMarker = line.trim().match(/^<!--\s*VISUAL:\s*([a-z0-9-]+)\s*-->$/i);
      if (visualMarker) {
        output.push(renderVisual(visualMarker[1].toLowerCase()));
        index += 1;
        continue;
      }
      const comment = [line];
      index += 1;
      while (index < lines.length) {
        if (lines[index].includes("-->")) {
          comment.push(lines[index]);
          index += 1;
          break;
        }
        comment.push(lines[index]);
        index += 1;
      }
      output.push(comment.join("\n"));
      continue;
    }

    const image = line.match(/^\s*!\[([^\]]*)\]\(([^)]+)\)\s*$/);
    if (image) {
      output.push(
        `<figure class="author-photo"><img src="${escapeHtml(image[2])}" alt="${escapeHtml(image[1])}"></figure>`,
      );
      index += 1;
      continue;
    }

    if (line.trim() === "```") {
      const code = [];
      index += 1;
      while (index < lines.length && lines[index].trim() !== "```") {
        code.push(lines[index]);
        index += 1;
      }
      index += 1;
      const isStackAscii = code[0]?.trim() === "THE AI INTERACTION STACK";
      output.push(
        `<pre class="prompt-block${isStackAscii ? " stack-ascii" : ""}"><code>${escapeHtml(code.join("\n"))}</code></pre>`,
      );
      continue;
    }

    if (
      line.includes("|") &&
      index + 1 < lines.length &&
      isTableSeparator(lines[index + 1])
    ) {
      const table = [line, lines[index + 1]];
      index += 2;
      while (index < lines.length && lines[index].includes("|") && lines[index].trim()) {
        table.push(lines[index]);
        index += 1;
      }
      output.push(renderTable(table));
      continue;
    }

    const heading = line.match(/^(#{1,6})\s+(.+?)\s*#*$/);
    if (heading) {
      const level = heading[1].length;
      const text = heading[2];
      const classes = [];
      if (level === 1 && (/^PART\b/i.test(text) || /^APPENDICES$/i.test(text))) classes.push("part-heading");
      if (level === 1 && /^APPENDICES$/i.test(text)) classes.push("appendices-heading");
      if (level === 2 && (/^Chapter\b/i.test(text) || /^Introduction\b/i.test(text))) {
        classes.push("chapter-heading");
      }
      if (level === 2 && /^About the Author$/i.test(text)) classes.push("author-heading");
      if (level === 2 && /^A Note on Sources$/i.test(text)) classes.push("sources-heading");
      if (level === 2 && /^About This Book$/i.test(text)) classes.push("about-book-heading");
      if (level === 2 && /^Appendix [A-E]$/i.test(text)) classes.push("appendix-heading");
      if (level === 3 && /^Verification Checklist$/i.test(text)) classes.push("checklist-heading");
      if (level === 3 && /^W\d+\b/.test(text)) classes.push("workflow-heading");
      if (level === 1 && /^PART\b/i.test(text)) currentPart = text;
      if (level === 2) {
        const appendix = text.match(/^Appendix ([A-E])$/i);
        currentAppendix = appendix ? appendix[1].toLowerCase() : null;
      }
      if (level === 2 && currentPart && !/^Chapter\b/i.test(text)) {
        partOverviewPending = currentPart !== "PART V";
        partOverviewChapters = partOverviewPending ? partChapters(lines, index - 1) : [];
      }
      output.push(
        `<h${level}${classes.length ? ` class="${classes.join(" ")}"` : ""}>${inlineMarkdown(text)}</h${level}>`,
      );
      if (classes.includes("workflow-heading")) output.push(renderWorkflowMeta(text));
      index += 1;
      continue;
    }

    if (/^---+$/.test(line.trim())) {
      index += 1;
      continue;
    }

    if (/^\s*>\s?/.test(line)) {
      const quote = [];
      while (index < lines.length && /^\s*>\s?/.test(lines[index])) {
        quote.push(lines[index].replace(/^\s*>\s?/, ""));
        index += 1;
      }
      const quoteHtml = renderMarkdown(quote);
      const label = quoteHtml.match(/<p><strong>(TRY THIS|WATCH OUT|PRO TIP|KEY IDEA|THE POINT)<\/strong><\/p>/i);
      output.push(
        `<aside class="callout ${label ? label[1].toLowerCase().replaceAll(" ", "-") : ""}">${quoteHtml}</aside>`,
      );
      continue;
    }

    if (/^\s*[-*]\s+/.test(line)) {
      const list = [];
      while (index < lines.length && /^\s*[-*]\s+/.test(lines[index])) {
        list.push(lines[index]);
        index += 1;
      }
      output.push(renderList(list, false));
      continue;
    }

    if (/^\s*☐\s+/.test(line)) {
      const checklist = [];
      while (index < lines.length) {
        if (/^\s*☐\s+/.test(lines[index])) {
          checklist.push(lines[index].replace(/^\s*☐\s+/, ""));
          index += 1;
          continue;
        }
        if (!lines[index].trim()) {
          let next = index + 1;
          while (next < lines.length && !lines[next].trim()) next += 1;
          if (next < lines.length && /^\s*☐\s+/.test(lines[next])) {
            index = next;
            continue;
          }
        }
        break;
      }
      output.push(
        `<div class="checklist-items">${checklist
          .map((item) => `<div class="check-item"><span class="check-box" aria-hidden="true"></span><span>${inlineMarkdown(item)}</span></div>`)
          .join("\n")}</div>`,
      );
      continue;
    }

    if (/^\s*\d+\.\s+/.test(line)) {
      const list = [];
      while (index < lines.length && /^\s*\d+\.\s+/.test(lines[index])) {
        list.push(lines[index]);
        index += 1;
      }
      output.push(renderList(list, true, currentAppendix === "a" ? "appendix-a-list" : ""));
      continue;
    }

    if (/^\*\*[^*]+\*\*$/.test(line.trim())) {
      output.push(`<h4 class="label-heading">${inlineMarkdown(line.trim())}</h4>`);
      index += 1;
      continue;
    }

    if (/^\*[^*].*\*$/.test(line.trim()) && !line.includes("**")) {
      output.push(`<p class="standfirst">${inlineMarkdown(line.trim())}</p>`);
      if (partOverviewPending) {
        output.push(renderPartOverview(partOverviewChapters));
        partOverviewPending = false;
      }
      index += 1;
      continue;
    }

    const paragraph = [line];
    index += 1;
    while (
      index < lines.length &&
      lines[index].trim() &&
      !/^```$/.test(lines[index].trim()) &&
      !/^(#{1,6})\s+/.test(lines[index]) &&
      !/^---+$/.test(lines[index].trim()) &&
      !/^\s*>/.test(lines[index]) &&
      !/^\s*[-*]\s+/.test(lines[index]) &&
      !/^\s*\d+\.\s+/.test(lines[index]) &&
      !/^\s*\|/.test(lines[index])
    ) {
      paragraph.push(lines[index]);
      index += 1;
    }
    const paragraphClass = currentAppendix === "a" && paragraph[0].startsWith("The full explanations appear")
      ? ' class="appendix-a-note"'
      : "";
    output.push(`<p${paragraphClass}>${paragraph.map(inlineMarkdown).join("<br>")}</p>`);
    if (partOverviewPending) {
      output.push(renderPartOverview(partOverviewChapters));
      partOverviewPending = false;
    }
  }

  return output.join("\n");
}
