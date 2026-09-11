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

function renderList(lines, ordered) {
  const tag = ordered ? "ol" : "ul";
  const matcher = ordered ? /^\s*\d+\.\s+(.*)$/ : /^\s*[-*]\s+(.*)$/;
  const items = lines
    .map((line) => line.match(matcher)?.[1] ?? line.trim())
    .map((item) => `<li>${inlineMarkdown(item)}</li>`)
    .join("");
  return `<${tag}>${items}</${tag}>`;
}

export function renderMarkdown(source) {
  const lines = Array.isArray(source) ? source : source.split(/\r?\n/);
  const output = [];
  let index = 0;

  while (index < lines.length) {
    const line = lines[index];
    if (!line.trim()) {
      index += 1;
      continue;
    }

    if (line.trim().startsWith("<!--")) {
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
      output.push(
        `<pre class="prompt-block"><code>${escapeHtml(code.join("\n"))}</code></pre>`,
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
      if (level === 1 && /^PART\b/i.test(text)) classes.push("part-heading");
      if (level === 2 && (/^Chapter\b/i.test(text) || /^Introduction\b/i.test(text))) {
        classes.push("chapter-heading");
      }
      if (level === 2 && /^About the Author$/i.test(text)) classes.push("author-heading");
      if (level === 3 && /^W\d+\b/.test(text)) classes.push("workflow-heading");
      output.push(
        `<h${level}${classes.length ? ` class="${classes.join(" ")}"` : ""}>${inlineMarkdown(text)}</h${level}>`,
      );
      index += 1;
      continue;
    }

    if (/^---+$/.test(line.trim())) {
      output.push('<div class="section-rule" aria-hidden="true"></div>');
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

    if (/^\s*\d+\.\s+/.test(line)) {
      const list = [];
      while (index < lines.length && /^\s*\d+\.\s+/.test(lines[index])) {
        list.push(lines[index]);
        index += 1;
      }
      output.push(renderList(list, true));
      continue;
    }

    if (/^\*\*[^*]+\*\*$/.test(line.trim())) {
      output.push(`<h4 class="label-heading">${inlineMarkdown(line.trim())}</h4>`);
      index += 1;
      continue;
    }

    if (/^\*[^*].*\*$/.test(line.trim()) && !line.includes("**")) {
      output.push(`<p class="standfirst">${inlineMarkdown(line.trim())}</p>`);
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
    output.push(`<p>${paragraph.map(inlineMarkdown).join("<br>")}</p>`);
  }

  return output.join("\n");
}
