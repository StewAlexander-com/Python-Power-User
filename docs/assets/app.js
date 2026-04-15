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

function renderSection(section) {
  const key = section.key;
  const num = String(section.number).padStart(2, "0");
  const title = section.title;
  const gb = section.goal_beginner || "—";
  const gp = section.goal_power || "—";

  const prompts = (section.prompts || []).slice(0, 8);
  const promptList =
    prompts.length === 0
      ? `<div class="muted">No prompts captured for this section.</div>`
      : `<ul class="muted" style="margin:10px 0 0; padding-left:18px;">
          ${prompts.map((p) => `<li>${escapeHtml(p)}</li>`).join("")}
        </ul>`;

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
        <div class="cardTitle" style="margin-bottom:6px;">Practice prompts</div>
        ${promptList}
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

async function loadSections() {
  const res = await fetch("./content/sections.json", { cache: "no-store" });
  if (!res.ok) throw new Error(`Failed to load sections.json: ${res.status}`);
  const data = await res.json();
  return data.sections || [];
}

function setHeroChips(sections) {
  const chips = $("#heroChips");
  const total = sections.length;
  const keys = ["Foundations", "Data", "Control", "Functions", "OOP", "Iterators", "Text", "Stdlib"];
  chips.innerHTML = [
    `<div class="chip"><strong>${total}</strong> sections indexed</div>`,
    `<div class="chip">Mobile-friendly dock</div>`,
    `<div class="chip">Fast search</div>`,
    `<div class="chip">Built from <span style="font-family:var(--mono)">python_poweruser.py</span></div>`,
    ...keys.slice(0, 4).map((k) => `<div class="chip">${k}</div>`),
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
  nav?.setAttribute("data-open", "true");
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

function handleDockAction(action, state) {
  const s = state.activeSection;
  if (!s) {
    nudgePickSection(state, `Tip: press <span class="kbd">/</span> to focus section search.`);
    return;
  }

  if (action === "practice") {
    const prompt = pickPracticePrompt(s) || "No prompts available for this section.";
    const snippet = practiceSnippet(s, prompt);
    upsertDockCard({
      id: "dockPracticeCard",
      title: `Practice · ${s.title}`,
      body: `
        <div>Answer the prompt using the code below. Then verify by running the section locally.</div>
        <div style="margin-top:10px;"><strong>Prompt:</strong> ${escapeHtml(prompt)}</div>
        <div class="muted" style="margin-top:10px;">Tip: the prompt line is marked with <span class="kbd">⇢</span>.</div>
      `,
      code: snippet,
    });
    scrollToTopMain();
    return;
  }

  if (action === "explain") {
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

  if (action === "show-demo") {
    upsertDockCard({
      id: "dockDemoCard",
      title: `Demo source · demo_${s.key}()`,
      body: `Copy this into your editor context, or jump to it in <span class="kbd">python_poweruser.py</span>.`,
      code: s.demo_source || "",
    });
    scrollToTopMain();
    return;
  }

  if (action === "show-try-this") {
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
    nav.setAttribute("data-open", open ? "false" : "true");
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

  $("#content").innerHTML = renderSection(s);
  renderNavList(state.sections, state.activeKey, state.filterText);

  // Close nav on mobile
  $("#nav").setAttribute("data-open", "false");
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
  };

  try {
    state.sections = await loadSections();
    setHeroChips(state.sections);
    renderNavList(state.sections, state.activeKey, state.filterText);
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

