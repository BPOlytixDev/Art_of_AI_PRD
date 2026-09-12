const escapeHtml = (value) =>
  String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");

const stackLayers = [
  ["11", "Iteration", "What happens next?"],
  ["10", "Verification", "How will you check it?"],
  ["9", "Output", "What should the result look like?"],
  ["8", "Workflow", "One step or several?"],
  ["7", "Tools", "What capabilities are available?"],
  ["6", "Workspace", "What context can persist?"],
  ["5", "Source material", "What can AI work from?"],
  ["4", "Examples", "What does good look like?"],
  ["3", "Instructions", "What exactly should AI do?"],
  ["2", "Context", "What does AI need to know?"],
  ["1", "Intent", "What are you trying to achieve?"],
];

const questions = [
  ["Q1", "What am I trying to achieve?"],
  ["Q2", "What does AI need to know?"],
  ["Q3", "What information can I provide?"],
  ["Q4", "What exactly should AI do?"],
  ["Q5", "What should the result look like?"],
  ["Q6", "How will I check it?"],
  ["Q7", "What should happen next?"],
];

const toolCapabilities = [
  ["Web search", "Current information", "Check sources and dates"],
  ["Research", "Multi-source reports", "Inspect citations"],
  ["Code execution", "Calculations and data", "Check formulas and inputs"],
  ["Files and images", "Source material and visual input", "Confirm what was actually read"],
];

const failureCategories = [
  ["01", "Hallucination"],
  ["02", "Outdated information"],
  ["03", "Confident over-generalisation"],
  ["04", "Arithmetic errors"],
  ["05", "Context drift"],
  ["06", "Sycophancy"],
  ["07", "Instruction drift"],
  ["08", "Plausible but wrong reasoning"],
];

const workflows = {
  "Quick win": ["W1", "W4", "W9", "W19", "W24"],
  "Medium build": ["W2", "W3", "W6", "W8", "W10", "W13", "W16", "W20"],
  "Deep work": ["W5", "W7", "W14", "W15", "W17", "W18", "W21", "W22", "W23", "W25"],
};

const workflowMeta = new Map([
  ...workflows["Quick win"].map((id) => [id, ["About 5 minutes", "Quick win"]]),
  ...workflows["Medium build"].map((id) => [id, ["15–30 minutes", "Medium build"]]),
  ...workflows["Deep work"].map((id) => [id, ["30+ minutes", "Deep work"]]),
]);

function visualShell(className, label, content) {
  return `<section class="visual-diagram ${className}" role="img" aria-label="${escapeHtml(label)}">${content}</section>`;
}

export function renderInteractionStackDiagram() {
  const items = stackLayers
    .map(
      ([number, name, description]) =>
        `<div class="stack-layer"><span class="stack-layer-number">${number}</span><strong>${escapeHtml(name)}</strong><span>${escapeHtml(description)}</span></div>`,
    )
    .join("");
  return visualShell(
    "stack-diagram",
    "The AI Interaction Stack: eleven layers from intent to iteration",
    `<div class="visual-kicker">The AI Interaction Stack</div><p class="visual-caption">Read from the bottom up. Activate only the layers this task needs.</p><div class="stack-list">${items}</div>`,
  );
}

export function renderSevenQuestionsVisual() {
  const items = questions
    .map(
      ([number, question]) =>
        `<div class="question-card"><span class="question-number">${number}</span><span>${escapeHtml(question)}</span></div>`,
    )
    .join("");
  return visualShell(
    "questions-diagram",
    "The 7 Questions portable AI framework",
    `<div class="visual-kicker">The 7 Questions</div><p class="visual-caption">A quick checklist before any significant AI interaction.</p><div class="question-grid">${items}</div>`,
  );
}

export function renderToolsCapabilityMap() {
  const items = toolCapabilities
    .map(
      ([name, enables, check]) =>
        `<div class="capability-card"><strong>${escapeHtml(name)}</strong><span>${escapeHtml(enables)}</span><small>Check: ${escapeHtml(check)}</small></div>`,
    )
    .join("");
  return visualShell(
    "capability-diagram",
    "AI capabilities beyond text and their verification needs",
    `<div class="visual-kicker">Beyond text</div><div class="capability-grid">${items}</div>`,
  );
}

export function renderWorkflowMechanicsDiagram() {
  return visualShell(
    "mechanics-diagram",
    "Chains, loops, and human handoffs in a multi-stage AI workflow",
    `<div class="visual-kicker">Three workflow mechanics</div><div class="mechanics-flow"><div class="mechanic-node"><strong>Chain</strong><span>A → B → C</span><small>Each output becomes the next input.</small></div><span class="mechanic-arrow" aria-hidden="true">→</span><div class="mechanic-node mechanic-loop"><strong>Loop</strong><span>Produce → Review → Improve</span><small>Repeat until the standard is met.</small></div><span class="mechanic-arrow" aria-hidden="true">→</span><div class="mechanic-node mechanic-handoff"><strong>Handoff</strong><span>AI ↔ Human</span><small>Judgment enters at a deliberate control point.</small></div></div>`,
  );
}

export function renderVerificationMatrix() {
  return visualShell(
    "verification-diagram",
    "Verification effort should increase with the consequences of being wrong",
    `<div class="visual-kicker">Verification is proportional to stakes</div><div class="risk-matrix"><div class="risk-axis risk-axis-y">How easy is it to check?</div><div class="risk-cell risk-low"><strong>Lower stakes</strong><span>Quick read-through and obvious-error check</span></div><div class="risk-cell risk-medium"><strong>Important work</strong><span>Check sources, numbers, assumptions, and constraints</span></div><div class="risk-cell risk-high"><strong>High consequence</strong><span>Independent sources, expert review, and explicit accountability</span></div><div class="risk-cell risk-critical"><strong>Hard to verify</strong><span>Do not rely on fluent prose alone; obtain evidence or qualified review</span></div><div class="risk-axis risk-axis-x">Consequences if wrong →</div></div>`,
  );
}

export function renderWorkflowRouteMap() {
  const lanes = Object.entries(workflows)
    .map(
      ([label, ids]) =>
        `<div class="route-lane"><strong>${escapeHtml(label)}</strong><span>${ids.join(" · ")}</span></div>`,
    )
    .join("");
  return visualShell(
    "route-map-diagram",
    "Twenty-five workflows organised by time and complexity",
    `<div class="visual-kicker">Find a workflow by time and complexity</div><div class="route-lanes">${lanes}</div>`,
  );
}

export function renderFailureTaxonomyGrid() {
  const items = failureCategories
    .map(
      ([number, name]) =>
        `<div class="failure-card"><span>${number}</span><strong>${escapeHtml(name)}</strong></div>`,
    )
    .join("");
  return visualShell(
    "failure-diagram",
    "Eight predictable categories of AI failure",
    `<div class="visual-kicker">The failure taxonomy</div><div class="failure-grid">${items}</div>`,
  );
}

export function renderWorkflowMeta(heading) {
  const id = heading.match(/^(W\d+)/i)?.[1]?.toUpperCase();
  const meta = id ? workflowMeta.get(id) : null;
  if (!meta) return "";
  return `<p class="workflow-meta"><span>Time: ${escapeHtml(meta[0])}</span><span>Complexity: ${escapeHtml(meta[1])}</span></p>`;
}

export function renderVisual(marker) {
  switch (marker) {
    case "interaction-stack":
      return renderInteractionStackDiagram();
    case "seven-questions":
      return renderSevenQuestionsVisual();
    case "tools-capabilities":
      return renderToolsCapabilityMap();
    case "workflow-mechanics":
      return renderWorkflowMechanicsDiagram();
    case "verification-matrix":
      return renderVerificationMatrix();
    case "workflow-route-map":
      return renderWorkflowRouteMap();
    case "failure-taxonomy":
      return renderFailureTaxonomyGrid();
    default:
      return "";
  }
}
