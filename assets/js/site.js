(() => {
  const normalize = (value) => value
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase();

  const dialog = document.querySelector("#site-search");
  const input = document.querySelector("#site-search-input");
  const status = document.querySelector("#site-search-status");
  const results = document.querySelector("#site-search-results");
  const index = Array.isArray(window.DI_SEARCH_INDEX) ? window.DI_SEARCH_INDEX : [];

  const closeSearch = () => {
    if (dialog?.open) dialog.close();
  };

  const renderResults = (query) => {
    const normalizedQuery = normalize(query.trim());
    results.replaceChildren();
    if (normalizedQuery.length < 2) {
      status.textContent = "Escribe al menos dos caracteres.";
      return;
    }
    const terms = normalizedQuery.split(/\s+/).filter(Boolean);
    const matches = index
      .map((entry) => {
        const title = normalize(`${entry.ra} ${entry.kind} ${entry.title}`);
        const text = normalize(entry.text);
        if (!terms.every((term) => title.includes(term) || text.includes(term))) return null;
        const score = terms.reduce((total, term) => total + (title.includes(term) ? 5 : 1), 0);
        return { entry, score };
      })
      .filter(Boolean)
      .sort((a, b) => b.score - a.score || a.entry.title.localeCompare(b.entry.title, "es"))
      .slice(0, 20);

    status.textContent = matches.length
      ? `${matches.length} resultado${matches.length === 1 ? "" : "s"}.`
      : "No se han encontrado resultados.";
    for (const { entry } of matches) {
      const item = document.createElement("li");
      const link = document.createElement("a");
      const meta = document.createElement("span");
      const title = document.createElement("strong");
      link.href = entry.url;
      meta.textContent = `${entry.ra} · ${entry.kind}`;
      title.textContent = entry.title;
      link.append(meta, title);
      item.append(link);
      results.append(item);
    }
  };

  document.querySelectorAll("[data-search-open]").forEach((button) => {
    button.addEventListener("click", () => {
      dialog.showModal();
      input.focus();
    });
  });
  document.querySelector("[data-search-close]")?.addEventListener("click", closeSearch);
  dialog?.addEventListener("click", (event) => {
    if (event.target === dialog) closeSearch();
  });
  input?.addEventListener("input", () => renderResults(input.value));

  const copyStatus = document.querySelector("#copy-status");
  document.querySelectorAll("[data-copy-target]").forEach((button) => {
    button.addEventListener("click", async () => {
      const source = document.getElementById(button.dataset.copyTarget);
      const card = button.closest(".practice-card");
      if (!source || !card) return;
      const heading = card.querySelector("h2")?.textContent.trim();
      const metadata = [...card.querySelectorAll(".practice-meta > div")]
        .map((item) => `${item.querySelector("dt")?.textContent}: ${item.querySelector("dd")?.textContent}`)
        .join("\n");
      const text = `${heading}\n\n${metadata}\n\n${source.innerText.trim()}`;
      try {
        await navigator.clipboard.writeText(text);
        const original = button.textContent;
        button.textContent = "Enunciado copiado";
        copyStatus.textContent = `${heading}: enunciado copiado al portapapeles.`;
        window.setTimeout(() => {
          button.textContent = original;
          copyStatus.textContent = "";
        }, 2200);
      } catch {
        copyStatus.textContent = "No se pudo copiar automáticamente. Selecciona el enunciado manualmente.";
      }
    });
  });
})();
