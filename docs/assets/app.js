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

function handleDockAction(action, state) {
  const s = state.activeSection;
  if (!s) {
    $("#content").insertAdjacentHTML(
      "afterbegin",
      renderDockResponse({
        title: "Pick a section first",
        body: `Select a section in the left navigation, then use the dock actions.`,
      }),
    );
    scrollToTopMain();
    return;
  }

  if (action === "practice") {
    const prompt = pickPracticePrompt(s) || "No prompts available for this section.";
    $("#content").insertAdjacentHTML(
      "afterbegin",
      renderDockResponse({
        title: `Practice · ${s.title}`,
        body: `Predict what Python does, then verify by running the section locally.<br/><br/><strong>Prompt:</strong> ${escapeHtml(prompt)}`,
      }),
    );
    scrollToTopMain();
    return;
  }

  if (action === "explain") {
    $("#content").insertAdjacentHTML(
      "afterbegin",
      renderDockResponse({
        title: `Explain · ${s.title}`,
        body: `Use the goals to guide what “done” looks like. Then run the <span class="kbd">Try this</span> or <span class="kbd">Speed run</span> cells in VS Code.<br/><br/>
        <div class="muted">Beginner goal: ${escapeHtml(s.goal_beginner || "—")}</div>
        <div class="muted">Power goal: ${escapeHtml(s.goal_power || "—")}</div>`,
      }),
    );
    scrollToTopMain();
    return;
  }

  if (action === "show-demo") {
    $("#content").insertAdjacentHTML(
      "afterbegin",
      renderDockResponse({
        title: `Demo source · demo_${s.key}()`,
        body: `Copy this into your editor context, or jump to it in <span class="kbd">python_poweruser.py</span>.`,
        code: s.demo_source || "",
      }),
    );
    scrollToTopMain();
    return;
  }

  if (action === "show-try-this") {
    $("#content").insertAdjacentHTML(
      "afterbegin",
      renderDockResponse({
        title: `Try this (Beginner) · ${s.title}`,
        body: `These are the runnable “Try this” cells captured from the section.`,
        code: s.try_this_source || "",
      }),
    );
    scrollToTopMain();
    return;
  }

  if (action === "show-speed-run") {
    $("#content").insertAdjacentHTML(
      "afterbegin",
      renderDockResponse({
        title: `Speed run (Power User) · ${s.title}`,
        body: `These are the runnable “Speed run” cells captured from the section.`,
        code: s.speed_run_source || "",
      }),
    );
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

  document.addEventListener("keydown", (e) => {
    if (e.key === "/") {
      e.preventDefault();
      $("#sectionSearch").focus();
    }
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
      e.preventDefault();
      focusDockInput();
    }
  });
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

