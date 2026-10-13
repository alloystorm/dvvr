document.addEventListener("DOMContentLoaded", function () {
  const browser = document.querySelector("[data-support-browser]");
  if (!browser) return;

  const search = browser.querySelector("#supportSearch");
  const type = browser.querySelector("#supportType");
  const results = browser.querySelector(".support-results");
  const count = browser.querySelector(".support-result-count");
  const empty = browser.querySelector(".support-empty");
  const buttons = Array.from(browser.querySelectorAll("[data-category-count]"), node => node.parentElement);
  const normalize = text => text.normalize("NFKD").replace(/\p{M}/gu, "").toLowerCase();
  const entries = Array.from(results.querySelectorAll(".support-item"), (element, order) => ({
    element,
    order,
    category: element.dataset.category,
    type: element.dataset.type,
    question: normalize(element.querySelector(".support-question").textContent),
    keywords: normalize(element.dataset.keywords || ""),
    answer: normalize(element.querySelector(".support-answer-content").textContent),
    metadata: normalize(element.querySelector(".support-tags").textContent + " " +
      (element.querySelector(".support-applicability")?.textContent || ""))
  }));
  let category = "";

  // Only expose categories and answer types with published content.
  buttons.forEach(button => {
    button.hidden = Boolean(button.dataset.category) &&
      !entries.some(entry => entry.category === button.dataset.category);
  });
  Array.from(type.options).forEach(option => {
    option.hidden = Boolean(option.value) && !entries.some(entry => entry.type === option.value);
  });

  function rank(entry, query, terms) {
    if (!terms.length) return 0;
    let score = entry.question.includes(query) ? 20 : 0;
    for (const term of terms) {
      if (entry.question.includes(term)) score += 8;
      else if (entry.keywords.includes(term)) score += 4;
      else if (entry.answer.includes(term) || entry.metadata.includes(term)) score += 1;
      else return -1;
    }
    return score;
  }

  function update() {
    const query = normalize(search.value).trim();
    const terms = query.match(/[\p{L}\p{N}]+/gu) || [];
    const ranked = entries.map(entry => ({ entry, score: rank(entry, query, terms) }));
    const matching = ranked.filter(({ entry, score }) => score >= 0 && (!type.value || entry.type === type.value));
    const visible = matching.filter(({ entry }) => !category || entry.category === category);
    const visibleElements = new Set(visible.map(({ entry }) => entry.element));
    ranked.sort((a, b) => b.score - a.score || a.entry.order - b.entry.order).forEach(({ entry }) => {
      entry.element.hidden = !visibleElements.has(entry.element);
      results.appendChild(entry.element);
    });
    buttons.forEach(button => {
      const total = matching.filter(({ entry }) => !button.dataset.category || entry.category === button.dataset.category).length;
      button.querySelector("[data-category-count]").textContent = String(total);
      button.setAttribute("aria-pressed", String(button.dataset.category === category));
    });
    count.textContent = count.dataset.countTemplate.replace("{count}", String(visible.length));
    empty.hidden = visible.length > 0;
    browser.querySelector(".support-reset").hidden = !search.value && !type.value && !category;
  }

  function reset() {
    search.value = "";
    type.value = "";
    category = "";
    update();
  }

  // A shared link always reveals its answer, including when filters hide it.
  function revealLinkedAnswer() {
    let identifier;
    try { identifier = decodeURIComponent(window.location.hash.slice(1)); }
    catch { return; }
    const entry = entries.find(candidate => candidate.element.id === identifier);
    if (!entry) return;
    reset();
    entry.element.open = true;
    entry.element.scrollIntoView({ block: "start" });
  }

  search.addEventListener("input", update);
  type.addEventListener("change", update);
  buttons.forEach(button => button.addEventListener("click", function () {
    category = button.dataset.category;
    update();
  }));
  browser.querySelector(".support-reset").addEventListener("click", function () {
    reset();
    search.focus();
  });
  browser.querySelectorAll(".support-permalink").forEach(link => link.addEventListener("click", function () {
    // hashchange does not fire when the selected hash is already current.
    reset();
    link.closest("details").open = true;
  }));
  window.addEventListener("hashchange", revealLinkedAnswer);
  browser.querySelector(".support-controls").hidden = false;
  update();
  revealLinkedAnswer();
});
