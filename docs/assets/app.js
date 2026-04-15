const $ = (sel, root = document) => root.querySelector(sel);
const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));

function escapeHtml(s) {
  return s
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function scoreMatch(hay, needle) {
  const h = hay.toLowerCase();
  const n = needle.toLowerCase().trim();
  if (!n) return 1;
  if (h === n) return 100;
  if (h.startsWith(n)) return 80;
  if (h.includes(n)) return 55;
  return 0;
}

function renderCodeBlock(src) {
  if (!src) return "";
  return `<pre class="code"><code>${escapeHtml(src)}</code></pre>`;
}

function contextSnippet(section, prompt) {
  const src = section?.demo_source || "";
  if (!src) return "";
  const lines = src.split("\n");
  const needle = (prompt || "").trim().toLowerCase();

  // Find the most relevant anchor line.
  let idx = -1;
  if (needle) idx = lines.findIndex((l) => l.toLowerCase().includes(needle));
  if (idx < 0) idx = lines.findIndex((l) => l.trim().startsWith("#?"));
  if (idx < 0) idx = Math.min(12, Math.max(0, lines.length - 1));

  // Show a small chunk that likely defines variables before the anchor.
  const maxLines = 8;
  const start = Math.max(0, idx - maxLines);
  const end = Math.min(lines.length, idx + 1);

  const snippet = lines.slice(start, end).filter((l) => l.trim() !== "");
  const clipped = snippet.slice(-maxLines);
  const prefix = start > 0 ? ["# …"] : [];
  return [...prefix, ...clipped].join("\n");
}

function extractTeachings(section, track = "beginner", maxItems = 6) {
  const src = section?.demo_source || "";
  if (!src) return [];
  const lines = src.split("\n");

  const bullets = [];
  const pushBullet = (t) => {
    const s = String(t || "").trim();
    if (!s) return;
    // Avoid duplicates.
    if (bullets.some((b) => b.toLowerCase() === s.toLowerCase())) return;
    bullets.push(s);
  };

  // 1) Pull “Feynman says / Einstein says / TL;DR” lines from the docstring box.
  // Those appear as: "│  ... │"
  for (const l of lines) {
    const m = l.match(/^\s*│\s{0,2}(.+?)\s*│\s*$/);
    if (!m) continue;
    const inner = m[1].replace(/\s+/g, " ").trim();
    if (!inner) continue;
    if (/^\d+\s+—\s+/.test(inner)) continue;
    if (/^TIP:/i.test(inner) || /says:/i.test(inner) || /TL;DR/i.test(inner) || /MNEMONICS/i.test(inner)) {
      pushBullet(inner.replace(/^TIP:\s*/i, "Tip: "));
    }
  }

  // 2) Pull key idea comment lines.
  for (const l of lines) {
    const trimmed = l.trim();
    if (!trimmed.startsWith("#")) continue;
    if (trimmed.startsWith("#* ──")) continue; // section headings
    if (trimmed.startsWith("# ═")) continue;
    if (trimmed.startsWith("# █")) continue;
    if (trimmed.startsWith("#!")) {
      pushBullet(trimmed.replace(/^#!\s*/, "Safety: ").trim());
      continue;
    }
    if (trimmed.startsWith("#?")) {
      pushBullet(trimmed.replace(/^#\?\s*/, "").trim());
      continue;
    }
    if (trimmed.startsWith("#*")) {
      pushBullet(trimmed.replace(/^#\*\s*/, "").trim());
      continue;
    }
    // Plain comment lines with guidance phrasing.
    if (/says:|rule:|tip:|mnemonic|never|always|prefer|avoid/i.test(trimmed)) {
      pushBullet(trimmed.replace(/^#\s*/, "").trim());
    }
  }

  // Track-specific ordering: beginner prefers simpler bullets first.
  const ordered = bullets.slice(0, maxItems);
  if (track === "power") return ordered;
  return ordered;
}

function renderTeachingsList(items) {
  if (!items || items.length === 0) {
    return `<div class="muted">No teaching notes were extracted for this section yet.</div>`;
  }
  return `
    <ul class="teachList">
      ${items.map((t) => `<li class="teachItem">${escapeHtml(t)}</li>`).join("")}
    </ul>
  `;
}

function renderSection(section) {
  const key = section.key;
  const num = String(section.number).padStart(2, "0");
  const title = section.title;
  const gb = section.goal_beginner || "—";
  const gp = section.goal_power || "—";

  const learnRow = `
    <div class="learnRow">
      <div class="learnLabel">Teachings</div>
      <div class="learnBody">
        <div class="learnTitle">Choose your track</div>
        <div class="muted" style="margin-top:4px;">Start with Teachings and “What it’s doing”. Practice problems are optional.</div>
        <div class="learnActions">
          <button class="primary" type="button" data-inline-action="learn-beginner">Beginner</button>
          <button class="ghost" type="button" data-inline-action="learn-power">Power user</button>
        </div>
      </div>
    </div>
  `;

  return `
    <section class="card" data-section="${escapeHtml(key)}">
      <div class="sectionHeader">
        <div>
          <div class="sectionKey">${escapeHtml(num)} · ${escapeHtml(key)}</div>
          <h2 class="sectionTitle" style="margin:4px 0 0;">${escapeHtml(title)}</h2>
        </div>
        <div class="badge">Section ${escapeHtml(num)}</div>
      </div>

      <div class="goals">
        <div class="goal">
          <div class="goalTitle">Goal (Beginner)</div>
          <div class="goalText">${escapeHtml(gb)}</div>
        </div>
        <div class="goal">
          <div class="goalTitle">Goal (Power User)</div>
          <div class="goalText">${escapeHtml(gp)}</div>
        </div>
      </div>

      <div style="margin-top:12px;">
        ${learnRow}
        <div class="muted" style="margin-top:10px;">Tip: you can also use the bottom <span class="kbd">Learn</span> button once a section is selected.</div>
      </div>
    </section>
  `;
}

function renderDockResponse({ title, body, code }) {
  return `
    <section class="card">
      <div class="cardTitle">${escapeHtml(title)}</div>
      <div class="cardBody">${body}</div>
      ${code ? renderCodeBlock(code) : ""}
    </section>
  `;
}

function upsertDockCard({ id, title, body, code }) {
  const content = $("#content");
  const existing = id ? document.getElementById(id) : null;
  const html = `
    <section class="card" ${id ? `id="${escapeHtml(id)}"` : ""}>
      <div class="cardTitle">${escapeHtml(title)}</div>
      <div class="cardBody">${body}</div>
      ${code ? renderCodeBlock(code) : ""}
    </section>
  `;

  if (existing) existing.outerHTML = html;
  else content.insertAdjacentHTML("afterbegin", html);
}

function tinyHash(s) {
  let h = 2166136261;
  for (let i = 0; i < s.length; i += 1) {
    h ^= s.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return (h >>> 0).toString(16);
}

function practiceStorageKey(sectionKey, prompt) {
  return `ppu.practice.${sectionKey}.${tinyHash(prompt || "")}`;
}

function loadPracticeAnswer(sectionKey, prompt) {
  try {
    return localStorage.getItem(practiceStorageKey(sectionKey, prompt)) || "";
  } catch {
    return "";
  }
}

function savePracticeAnswer(sectionKey, prompt, answer) {
  try {
    localStorage.setItem(practiceStorageKey(sectionKey, prompt), answer || "");
  } catch {
    // ignore storage failures (private mode etc.)
  }
}

async function loadSections() {
  const res = await fetch("./content/sections.json", { cache: "no-store" });
  if (!res.ok) throw new Error(`Failed to load sections.json: ${res.status}`);
  const data = await res.json();
  return data.sections || [];
}

function setHeroChips(sections) {
  const chips = $("#heroChips");
  const total = sections.length;
  chips.innerHTML = [
    `<div class="chip"><strong>${total}</strong> sections indexed</div>`,
    `<div class="chip">Mobile-friendly dock</div>`,
    `<div class="chip">Fast search</div>`,
    `<div class="chip">Built from <span style="font-family:var(--mono)">python_poweruser.py</span></div>`,
  ].join("");
}

function renderNavList(sections, activeKey, filterText) {
  const list = $("#navList");
  const ft = (filterText || "").trim();

  const items = sections
    .map((s) => {
      const num = String(s.number).padStart(2, "0");
      const title = s.title;
      const key = s.key;
      const hay = `${num} ${key} ${title}`;
      const sc = scoreMatch(hay, ft);
      return { s, sc };
    })
    .filter((x) => x.sc > 0)
    .sort((a, b) => (b.sc - a.sc) || (a.s.number - b.s.number));

  list.innerHTML = items
    .map(({ s }) => {
      const num = String(s.number).padStart(2, "0");
      const selected = s.key === activeKey;
      return `
        <div class="navItem" role="listitem" tabindex="0"
          data-key="${escapeHtml(s.key)}"
          aria-selected="${selected ? "true" : "false"}">
          <div>
            <div class="navItemTitle">${escapeHtml(num)} — ${escapeHtml(s.title)}</div>
            <div class="navItemMeta">${escapeHtml(s.key)}</div>
          </div>
          <div class="badge">${escapeHtml(num)}</div>
        </div>
      `;
    })
    .join("");
}

function scrollToTopMain() {
  $("#main").scrollTo({ top: 0, behavior: "smooth" });
}

function focusDockInput() {
  $("#dockInput").focus();
}

function pickPracticePrompt(section) {
  const prompts = section?.prompts || [];
  if (prompts.length === 0) return null;
  const idx = Math.floor(Math.random() * prompts.length);
  return prompts[idx];
}

function pickPracticePrompts(section, count = 3) {
  const prompts = (section?.prompts || []).filter(Boolean);
  if (prompts.length === 0) return [];
  const uniq = Array.from(new Set(prompts));
  // Deterministic-ish selection: take first N, but rotate by section number for variety.
  const rot = Math.max(0, (section?.number || 0) % Math.max(1, uniq.length));
  const rotated = uniq.slice(rot).concat(uniq.slice(0, rot));
  return rotated.slice(0, Math.max(1, count));
}

function practiceSnippet(section, prompt) {
  const src = section?.demo_source || "";
  if (!src) return "";

  const lines = src.split("\n");
  const needle = (prompt || "").trim().toLowerCase();

  let idx = -1;
  if (needle) {
    idx = lines.findIndex((l) => l.toLowerCase().includes(needle));
  }
  if (idx < 0) {
    idx = lines.findIndex((l) => l.trim().startsWith("#?"));
  }
  if (idx < 0) {
    return src;
  }

  const before = 10;
  const after = 14;
  const start = Math.max(0, idx - before);
  const end = Math.min(lines.length, idx + after + 1);

  const snippet = lines.slice(start, end).map((l, i) => {
    const isPromptLine = start + i === idx;
    if (!isPromptLine) return l;
    // Mark the prompt line so it stands out even in a plain <pre>.
    return l.replace("#?", "#? ⇢");
  });

  const prefix = start > 0 ? ["# …"] : [];
  const suffix = end < lines.length ? ["# …"] : [];
  return [...prefix, ...snippet, ...suffix].join("\n");
}

function ensurePracticeFlow(state, section) {
  if (!section) return;
  // Don’t clobber an in-progress flow for the same section.
  if (state.practiceFlow && state.practiceFlow.sectionKey === section.key) return;
  const prompts = pickPracticePrompts(section, 3);
  const idx = 0;
  const prompt = prompts[idx] || "";
  const saved = prompt ? loadPracticeAnswer(section.key, prompt) : "";
  state.practiceFlow = {
    sectionKey: section.key,
    step: 1, // 1..6
    practiceEnabled: false, // steps 3-6 only when user opts in
    prompts,
    idx,
    showCode: false,
    answers: { [idx]: saved },
    grades: {}, // idx -> 'correct'|'close'|'notyet'
    lastSavedAt: null,
  };
}

function practiceFlowTitle(section, step) {
  const steps = ["Teachings", "What it’s doing", "Practice problems", "Your answers", "Evaluate", "Feedback"];
  const label = steps[Math.max(0, Math.min(steps.length - 1, (step || 1) - 1))];
  return `Learn · ${section.title} · ${label}`;
}

function renderStepPills(step, practiceEnabled) {
  const steps = practiceEnabled
    ? ["Teachings", "What it’s doing", "Practice", "Answer", "Evaluate", "Feedback"]
    : ["Teachings", "What it’s doing"];
  return `
    <div class="flowSteps" role="list">
      ${steps
        .map((t, i) => {
          const n = i + 1;
          const active = n === step;
          const done = n < step;
          return `<div class="flowStep ${active ? "active" : ""} ${done ? "done" : ""}" role="listitem">
            <span class="flowStepNum">${n}</span>
            <span class="flowStepText">${escapeHtml(t)}</span>
          </div>`;
        })
        .join("")}
    </div>
  `;
}

function renderPracticeFlowCard(state) {
  const s = state.activeSection;
  const pf = state.practiceFlow;
  if (!s || !pf) return "";

  const step = pf.step || 1;
  const practiceEnabled = pf.practiceEnabled === true;
  const track = pf.track === "power" ? "power" : "beginner";
  const teachings = extractTeachings(s, track, 6);
  const runCmd = `python python_poweruser.py -s ${s.key}`;
  const prompts = pf.prompts || [];
  const curPrompt = prompts[pf.idx] || "";
  const answer = (pf.answers && pf.answers[pf.idx]) ? pf.answers[pf.idx] : loadPracticeAnswer(s.key, curPrompt);
  const snippet = practiceSnippet(s, curPrompt);
  const fullDemo = s.demo_source || "";
  const ctx = contextSnippet(s, curPrompt);

  const nav = `
    <div class="flowNav">
      <button class="ghost" type="button" data-inline-action="lf-back" ${step <= 1 ? "disabled" : ""}>Back</button>
      <div class="spacer"></div>
      <button class="primary" type="button" data-inline-action="lf-next">
        ${practiceEnabled ? (step >= 6 ? "Done" : "Next") : (step >= 2 ? "Close" : "Next")}
      </button>
    </div>
  `;

  const step1 = `
    <div class="flowPanel">
      <div class="flowHeadline">Here are the teachings</div>
      ${renderTeachingsList(teachings)}
      <div class="flowTeachings">
        <div class="flowTeach">
          <div class="flowTeachTitle">${track === "power" ? "Beginner goal (supporting)" : "Beginner goal"}</div>
          <div class="flowTeachBody">${escapeHtml(s.goal_beginner || "—")}</div>
        </div>
        <div class="flowTeach">
          <div class="flowTeachTitle">${track === "power" ? "Power goal" : "Power goal (next level)"}</div>
          <div class="flowTeachBody">${escapeHtml(s.goal_power || "—")}</div>
        </div>
      </div>
      <div class="muted" style="margin-top:10px;">
        You’re in <span class="kbd">${track === "power" ? "Power user" : "Beginner"}</span> mode. Next we’ll show what the code is doing.
      </div>
    </div>
  `;

  const step2 = `
    <div class="flowPanel">
      <div class="flowHeadline">Here is what the teaching is doing</div>
      <div class="flowPromptBig">
        <div class="flowPromptLabel">Focus question</div>
        <div class="flowPromptText">${escapeHtml(curPrompt || "Pick a practice problem next.")}</div>
      </div>
      ${ctx ? `<div class="flowPromptContext">
        <div class="flowPromptContextTitle">Context (what variables mean here)</div>
        ${renderCodeBlock(ctx)}
      </div>` : ``}
      <div class="flowActions">
        <button class="ghost" type="button" data-inline-action="lf-toggle-code">
          ${pf.showCode ? "Hide code" : "Show code"}
        </button>
        <button class="ghost" type="button" data-inline-action="lf-copy-cmd" data-cmd="${escapeHtml(runCmd)}">Copy run command</button>
        <div class="spacer"></div>
        <button class="primary" type="button" data-inline-action="lf-start-practice">
          Start practice problems
        </button>
      </div>
      ${pf.showCode ? renderCodeBlock(snippet || fullDemo) : `<div class="muted">Code is hidden to reduce clutter. Use “Show code” if you need it.</div>`}
      <div class="muted" style="margin-top:10px;">
        Practice is optional. If you only want the teaching + explanation, you can close now.
      </div>
    </div>
  `;

  const step3 = `
    <div class="flowPanel">
      <div class="flowHeadline">Here are a few practice problems</div>
      <div class="flowList">
        ${prompts
          .map((p, i) => {
            const active = i === pf.idx;
            return `<button class="flowListItem ${active ? "active" : ""}" type="button"
              data-inline-action="lf-pick-problem" data-idx="${i}">
              <span class="flowListNum">${i + 1}</span>
              <span class="flowListText">${escapeHtml(p)}</span>
            </button>`;
          })
          .join("")}
      </div>
      <div class="muted" style="margin-top:10px;">Select a problem, then continue to answer.</div>
    </div>
  `;

  const step4 = `
    <div class="flowPanel">
      <div class="flowHeadline">Let the user provide answers</div>
      <div class="flowPromptBig">
        <div class="flowPromptLabel">Question ${pf.idx + 1} of ${prompts.length}</div>
        <div class="flowPromptText">${escapeHtml(curPrompt || "—")}</div>
      </div>
      ${ctx ? `<div class="flowPromptContext">
        <div class="flowPromptContextTitle">Context</div>
        ${renderCodeBlock(ctx)}
      </div>` : ``}
      <div class="answerBox" style="margin-top:12px;">
        <label class="answerLabel" for="practiceAnswer">Your answer</label>
        <textarea
          id="practiceAnswer"
          class="answerInput flowAnswerInput"
          rows="4"
          placeholder="Write your prediction clearly (what prints / what evaluates to / why)…"
        >${escapeHtml(answer || "")}</textarea>
        <div class="answerActions">
          <button class="primary" type="button" data-inline-action="lf-save-answer">Save answer</button>
          <button class="ghost" type="button" data-inline-action="lf-clear-answer">Clear</button>
          <div class="spacer"></div>
          <button class="ghost" type="button" data-inline-action="lf-toggle-code">${pf.showCode ? "Hide code" : "Show code"}</button>
          <button class="ghost" type="button" data-inline-action="lf-copy-code">Copy code</button>
        </div>
      </div>
      ${pf.showCode ? renderCodeBlock(snippet || fullDemo) : ""}
      <div class="muted" style="margin-top:10px;">Next: self-evaluate after you run locally and compare.</div>
    </div>
  `;

  const gradeFor = (i) => (pf.grades && pf.grades[i]) ? pf.grades[i] : "";
  const gradeBtn = (i, val, label) => `
    <button class="flowGradeBtn ${gradeFor(i) === val ? "active" : ""}" type="button"
      data-inline-action="lf-grade" data-idx="${i}" data-grade="${val}">
      ${escapeHtml(label)}
    </button>
  `;

  const step5 = `
    <div class="flowPanel">
      <div class="flowHeadline">Evaluate the results</div>
      <div class="muted">After running locally, grade each answer.</div>
      <div class="flowEval">
        ${prompts
          .map((p, i) => `
            <div class="flowEvalRow">
              <div class="flowEvalQ">
                <div class="flowEvalNum">Q${i + 1}</div>
                <div class="flowEvalText">${escapeHtml(p)}</div>
              </div>
              <div class="flowEvalBtns">
                ${gradeBtn(i, "correct", "Correct")}
                ${gradeBtn(i, "close", "Close")}
                ${gradeBtn(i, "notyet", "Not yet")}
              </div>
            </div>
          `)
          .join("")}
      </div>
      <div class="muted" style="margin-top:10px;">
        Tip: if you’re “Not yet”, go back to Answer and tighten your reasoning.
      </div>
    </div>
  `;

  const counts = (() => {
    const g = pf.grades || {};
    const vals = Object.values(g);
    return {
      correct: vals.filter((x) => x === "correct").length,
      close: vals.filter((x) => x === "close").length,
      notyet: vals.filter((x) => x === "notyet").length,
    };
  })();

  const step6 = `
    <div class="flowPanel">
      <div class="flowHeadline">Provide feedback on evaluation</div>
      <div class="flowFeedback">
        <div class="flowFeedbackStat"><span class="pill">Correct</span> <strong>${counts.correct}</strong></div>
        <div class="flowFeedbackStat"><span class="pill">Close</span> <strong>${counts.close}</strong></div>
        <div class="flowFeedbackStat"><span class="pill">Not yet</span> <strong>${counts.notyet}</strong></div>
      </div>
      <div style="margin-top:10px;">
        ${counts.notyet > 0
          ? `<div class="muted">Recommendation: redo the “Not yet” questions. Use “What it’s doing” to re-anchor your mental model, then answer again.</div>`
          : `<div class="muted">Nice. If you want to go faster, try “Speed run” next or switch sections.</div>`}
      </div>
      <div class="flowActions" style="margin-top:12px;">
        <button class="ghost" type="button" data-inline-action="lf-restart">Restart practice</button>
        <button class="ghost" type="button" data-inline-action="lf-go-speedrun">Open Speed run</button>
      </div>
    </div>
  `;

  const body = `
    ${renderStepPills(step, practiceEnabled)}
    ${step === 1 ? step1 : ""}
    ${step === 2 ? step2 : ""}
    ${practiceEnabled && step === 3 ? step3 : ""}
    ${practiceEnabled && step === 4 ? step4 : ""}
    ${practiceEnabled && step === 5 ? step5 : ""}
    ${practiceEnabled && step === 6 ? step6 : ""}
    ${nav}
  `;

  return { id: "dockPracticeCard", title: practiceFlowTitle(s, step), body };
}

function _pulse(el, className, ms = 1400) {
  if (!el) return;
  el.classList.remove(className);
  // Force reflow so repeated pulses restart reliably.
  // eslint-disable-next-line no-unused-expressions
  el.offsetWidth;
  el.classList.add(className);
  window.setTimeout(() => el.classList.remove(className), ms);
}

function nudgePickSection(state, reason = "") {
  const nav = $("#nav");
  const search = $("#sectionSearch");
  const navList = $("#navList");

  // Poka‑yoke: open the section picker and focus it.
  setNavOpen(state, true);
  search?.focus();

  // Visual guidance: glow the nav panel + the search input.
  _pulse(nav, "navNudgePulse", 1600);
  _pulse(search, "inputNudgePulse", 1600);
  _pulse(navList, "listNudgePulse", 1600);

  // Only show ONE nudge card (update it if it already exists).
  const content = $("#content");
  const existing = $("#nudgePickSectionCard");
  const body = `
    <div>Select a section in the left navigation, then use the dock actions.</div>
    <div class="nudgeSteps">
      <div class="nudgeStep"><span class="nudgeStepNum">1</span> Click any section on the left</div>
      <div class="nudgeStep"><span class="nudgeStepNum">2</span> Use <span class="kbd">Practice</span> to start</div>
    </div>
    ${reason ? `<div class="muted nudgeHint">${reason}</div>` : ""}
  `.trim();

  const html = `
    <section class="card nudgeCardPulse" id="nudgePickSectionCard">
      <div class="cardTitle">Pick a section first</div>
      <div class="cardBody">${body}</div>
    </section>
  `;

  if (existing) {
    existing.outerHTML = html;
  } else {
    content.insertAdjacentHTML("afterbegin", html);
  }

  scrollToTopMain();
}

function setNavOpen(state, open) {
  state.navOpen = open === true;
  $("#nav")?.setAttribute("data-open", state.navOpen ? "true" : "false");
}

function setFlowMode(state, mode) {
  state.flowMode = mode;
}

function handleDockAction(action, state) {
  const s = state.activeSection;
  if (!s) {
    setFlowMode(state, "no_section");
    nudgePickSection(state, `Tip: press <span class="kbd">/</span> to focus section search.`);
    return;
  }

  if (action === "learn") {
    setFlowMode(state, "practice");
    ensurePracticeFlow(state, s);
    // Start at Teachings (1) and keep practice disabled by default.
    if (state.practiceFlow) {
      state.practiceFlow.step = 1;
      state.practiceFlow.practiceEnabled = false;
    }
    const card = renderPracticeFlowCard(state);
    upsertDockCard({ id: card.id, title: card.title, body: card.body });
    scrollToTopMain();
    window.setTimeout(() => {
      const pf = state.practiceFlow;
      if (pf?.step === 4) $("#practiceAnswer")?.focus();
    }, 30);
    return;
  }

  if (action === "explain") {
    setFlowMode(state, "explain");
    upsertDockCard({
      id: "dockExplainCard",
      title: `Explain · ${s.title}`,
      body: `Use the goals to guide what “done” looks like. Then run the <span class="kbd">Try this</span> or <span class="kbd">Speed run</span> cells in VS Code.<br/><br/>
      <div class="muted">Beginner goal: ${escapeHtml(s.goal_beginner || "—")}</div>
      <div class="muted">Power goal: ${escapeHtml(s.goal_power || "—")}</div>`,
    });
    scrollToTopMain();
    return;
  }

  if (action === "show-try-this") {
    setFlowMode(state, "try_this");
    upsertDockCard({
      id: "dockTryThisCard",
      title: `Try this (Beginner) · ${s.title}`,
      body: `These are the runnable “Try this” cells captured from the section.`,
      code: s.try_this_source || "",
    });
    scrollToTopMain();
    return;
  }

  if (action === "show-speed-run") {
    setFlowMode(state, "speed_run");
    upsertDockCard({
      id: "dockSpeedRunCard",
      title: `Speed run (Power User) · ${s.title}`,
      body: `These are the runnable “Speed run” cells captured from the section.`,
      code: s.speed_run_source || "",
    });
    scrollToTopMain();
    return;
  }
}

function attachNavHandlers(state) {
  const nav = $("#nav");
  $("#btnToggleNav").addEventListener("click", () => {
    const open = nav.getAttribute("data-open") === "true";
    setNavOpen(state, !open);
    if (!open) $("#sectionSearch").focus();
  });

  $("#navList").addEventListener("click", (e) => {
    const item = e.target.closest(".navItem");
    if (!item) return;
    const key = item.getAttribute("data-key");
    selectSectionByKey(state, key);
  });

  $("#navList").addEventListener("keydown", (e) => {
    if (e.key !== "Enter") return;
    const item = e.target.closest(".navItem");
    if (!item) return;
    const key = item.getAttribute("data-key");
    selectSectionByKey(state, key);
  });

  $("#sectionSearch").addEventListener("input", (e) => {
    state.filterText = e.target.value || "";
    renderNavList(state.sections, state.activeKey, state.filterText);
  });
}

function selectSectionByKey(state, key) {
  const s = state.sections.find((x) => x.key === key);
  if (!s) return;
  state.activeKey = key;
  state.activeSection = s;
  setFlowMode(state, "section_selected");

  $("#content").innerHTML = renderSection(s);
  renderNavList(state.sections, state.activeKey, state.filterText);

  // Close nav on mobile
  setNavOpen(state, false);
  $("#dockHint").textContent = `Active: ${String(s.number).padStart(2, "0")} — ${s.title}. Use the dock pills to practice.`;

  // Clear any "pick a section first" nudge card.
  $("#nudgePickSectionCard")?.remove();
}

function attachDockHandlers(state) {
  $("#dockPills").addEventListener("click", (e) => {
    const btn = e.target.closest("button[data-action]");
    if (!btn) return;
    const action = btn.getAttribute("data-action");
    handleDockAction(action, state);
  });

  $("#content").addEventListener("click", (e) => {
    const btn = e.target.closest("button[data-inline-action]");
    if (!btn) return;
    const action = btn.getAttribute("data-inline-action");
    if (action === "learn-beginner" || action === "learn-power") {
      const s = state.activeSection;
      if (!s) return;
      setFlowMode(state, "practice");
      ensurePracticeFlow(state, s);
      if (state.practiceFlow) {
        state.practiceFlow.step = 1;
        state.practiceFlow.practiceEnabled = false;
        state.practiceFlow.showCode = false;
        state.practiceFlow.track = action === "learn-power" ? "power" : "beginner";
      }
      const card = renderPracticeFlowCard(state);
      upsertDockCard({ id: card.id, title: card.title, body: card.body });
      scrollToTopMain();
      return;
    }

    // Learning flow (new progressive UI)
    if (action === "lf-back" || action === "lf-next" || action === "lf-toggle-code" || action === "lf-start-practice" ||
        action === "lf-pick-problem" || action === "lf-save-answer" || action === "lf-clear-answer" ||
        action === "lf-grade" || action === "lf-copy-cmd" || action === "lf-copy-code" ||
        action === "lf-restart" || action === "lf-go-speedrun") {
      const s = state.activeSection;
      if (!s) return;
      ensurePracticeFlow(state, s);
      const pf = state.practiceFlow;
      if (!pf) return;

      if (action === "lf-back") {
        pf.step = Math.max(1, (pf.step || 1) - 1);
      }

      if (action === "lf-next") {
        const practiceEnabled = pf.practiceEnabled === true;
        if (!practiceEnabled) {
          // In non-practice mode we only have steps 1-2; step 2 "Close".
          if ((pf.step || 1) >= 2) return;
          pf.step = 2;
          return;
        }

        pf.step = Math.min(6, (pf.step || 1) + 1);
        // Auto-focus answer box on step 4.
        if (pf.step === 4) window.setTimeout(() => $("#practiceAnswer")?.focus(), 30);
      }

      if (action === "lf-start-practice") {
        pf.practiceEnabled = true;
        pf.step = 3;
      }

      if (action === "lf-toggle-code") {
        pf.showCode = !pf.showCode;
      }

      if (action === "lf-pick-problem") {
        const idx = Number(btn.getAttribute("data-idx"));
        if (Number.isFinite(idx)) pf.idx = Math.max(0, Math.min((pf.prompts || []).length - 1, idx));
      }

      if (action === "lf-save-answer") {
        const prompt = (pf.prompts || [])[pf.idx] || "";
        const val = $("#practiceAnswer")?.value || "";
        if (!pf.answers) pf.answers = {};
        pf.answers[pf.idx] = val;
        savePracticeAnswer(s.key, prompt, val);
        pf.lastSavedAt = Date.now();
        _pulse($("#practiceAnswer"), "inputNudgePulse", 900);
      }

      if (action === "lf-clear-answer") {
        const ta = $("#practiceAnswer");
        if (ta) {
          ta.value = "";
          ta.focus();
        }
        if (pf.answers) pf.answers[pf.idx] = "";
      }

      if (action === "lf-grade") {
        const idx = Number(btn.getAttribute("data-idx"));
        const grade = btn.getAttribute("data-grade") || "";
        if (!pf.grades) pf.grades = {};
        if (Number.isFinite(idx) && ["correct", "close", "notyet"].includes(grade)) {
          pf.grades[idx] = grade;
        }
      }

      if (action === "lf-copy-cmd") {
        const cmd = btn.getAttribute("data-cmd") || "";
        navigator.clipboard?.writeText?.(cmd);
        _pulse(btn, "inputNudgePulse", 900);
      }

      if (action === "lf-copy-code") {
        const pre = $("#dockPracticeCard pre code");
        const txt = pre?.innerText || "";
        navigator.clipboard?.writeText?.(txt);
        _pulse(btn, "inputNudgePulse", 900);
      }

      if (action === "lf-restart") {
        state.practiceFlow = null;
        ensurePracticeFlow(state, s);
      }

      if (action === "lf-go-speedrun") {
        handleDockAction("show-speed-run", state);
        return;
      }

      const card = renderPracticeFlowCard(state);
      upsertDockCard({ id: card.id, title: card.title, body: card.body });
      return;
    }
  });

  $("#dockForm").addEventListener("submit", (e) => {
    e.preventDefault();
    const q = ($("#dockInput").value || "").trim();
    if (!q) return;
    $("#dockInput").value = "";

    // “Smart search”: if the query matches a section strongly, jump to it.
    const ranked = state.sections
      .map((s) => {
        const hay = `${s.key} ${s.title} ${s.goal_beginner} ${s.goal_power}`;
        return { s, sc: scoreMatch(hay, q) };
      })
      .sort((a, b) => b.sc - a.sc);

    if (ranked[0]?.sc >= 80) {
      selectSectionByKey(state, ranked[0].s.key);
      $("#content").insertAdjacentHTML(
        "afterbegin",
        renderDockResponse({
          title: `Jumped to · ${ranked[0].s.title}`,
          body: `Your query matched this section. Use <span class="kbd">Practice</span> to start a short loop.`,
        }),
      );
      scrollToTopMain();
      return;
    }

    // Otherwise provide a guided response anchored to the active section (if any).
    const s = state.activeSection;
    const body = s
      ? `Interpreting your question within <strong>${escapeHtml(s.title)}</strong>.<br/><br/>
         <div class="muted">Suggestion: use <span class="kbd">Explain</span> then <span class="kbd">Try this</span>, and finish with <span class="kbd">Practice</span>.</div>`
      : `Use the left navigation to pick a section, or type a section name (like <span class="kbd">decorators</span>).`;

    $("#content").insertAdjacentHTML(
      "afterbegin",
      renderDockResponse({
        title: `Query · ${escapeHtml(q)}`,
        body,
      }),
    );
    scrollToTopMain();

    if (!s) {
      setFlowMode(state, "no_section");
      nudgePickSection(state, `Tip: press <span class="kbd">/</span> to focus section search.`);
    }
  });

  document.addEventListener(
    "keydown",
    (e) => {
      // Don't hijack typing inside inputs/contenteditable.
      const ae = document.activeElement;
      const tag = ae?.tagName?.toLowerCase?.() || "";
      const isTypingTarget =
        tag === "input" || tag === "textarea" || ae?.isContentEditable === true;

      const isSlash =
        e.key === "/" || e.code === "Slash" || (e.shiftKey && e.key === "?");

      if (isSlash && !isTypingTarget) {
        e.preventDefault();
        setFlowMode(state, "no_section");
        nudgePickSection(state, `Tip: press <span class="kbd">Ctrl</span><span class="kbd">K</span> to focus the bottom dock.`);
        return;
      }

      // Keep the original “focus dock” shortcut.
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
        e.preventDefault();
        focusDockInput();
      }
    },
    { capture: true },
  );
}

async function main() {
  const state = {
    sections: [],
    filterText: "",
    activeKey: null,
    activeSection: null,
    // Process flow state (UI/HMI)
    flowMode: "boot",
    navOpen: false,
  };

  try {
    state.sections = await loadSections();
    setHeroChips(state.sections);
    renderNavList(state.sections, state.activeKey, state.filterText);
    setFlowMode(state, "no_section");
  } catch (err) {
    $("#content").innerHTML = `
      <section class="card">
        <div class="cardTitle">Failed to load content</div>
        <div class="cardBody">
          <div class="muted">This GitHub Pages build needs <span class="kbd">docs/content/sections.json</span>.</div>
          <pre class="code"><code>${escapeHtml(String(err))}</code></pre>
        </div>
      </section>
    `;
  }

  attachNavHandlers(state);
  attachDockHandlers(state);
}

main();

