#!/usr/bin/env python3
"""Genera la web estática de damDI a partir de los Markdown de src/."""

from __future__ import annotations

import html
import hashlib
import json
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "src"
SITE_DESCRIPTION = "Material docente del módulo 0488 con IA, web y Material Design 3."
PUBLIC_BASE_URL = "https://mosqueteroweb.github.io/damDI/"
REVIEW_DATE = "septiembre de 2026"

PRACTICE_DURATIONS = {
    "RA1": "15–35 min",
    "RA2": "35–45 min",
    "RA3": "30–40 min",
    "RA4": "30–40 min",
    "RA5": "30–40 min",
    "RA6": "20–30 min",
    "RA7": "20–30 min",
    "RA8": "30–45 min",
}

TOOL_LABELS = {
    "stitch": "Stitch",
    "gemini": "Gemini",
    "ai studio": "Google AI Studio",
    "devtools": "DevTools",
    "lighthouse": "Lighthouse",
    "playwright": "Playwright",
    "chart.js": "Chart.js",
    "google charts": "Google Charts",
    "teachable machine": "Teachable Machine",
    "mediapipe": "MediaPipe",
    "zap": "OWASP ZAP",
    "k6": "k6",
    "github": "GitHub",
    "gpg": "GPG",
    "cosign": "Cosign",
}


def split_front_matter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    metadata: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            metadata[key.strip()] = value.strip().strip('"\'')
    return metadata, text[end + 5 :]


def plain_heading(markdown: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", markdown, re.MULTILINE)
    if not match:
        return fallback
    heading = re.sub(r"\[([^]]+)]\([^)]*\)", r"\1", match.group(1))
    return re.sub(r"[*_`]", "", heading).strip()


def render_markdown(markdown: str) -> str:
    result = subprocess.run(
        ["pandoc", "--from=gfm+yaml_metadata_block", "--to=html5", "--wrap=none"],
        input=markdown,
        text=True,
        capture_output=True,
        check=True,
    )
    rendered = re.sub(
        r'href="([^"#]+)\.md(#[^"]*)?"',
        lambda match: f'href="{match.group(1)}.html{match.group(2) or ""}"',
        result.stdout,
    )
    rendered = rendered.replace(f'href="{PUBLIC_BASE_URL}#', 'href="index.html#')
    rendered = rendered.replace(f'href="{PUBLIC_BASE_URL}"', 'href="index.html"')
    return rendered.replace(f'href="{PUBLIC_BASE_URL}', 'href="')


def remove_first_heading(body: str) -> str:
    """La cabecera de la plantilla ya contiene el único h1 de la página."""
    return re.sub(r"\s*<h1\b[^>]*>.*?</h1>\s*", "\n", body, count=1, flags=re.DOTALL)


def deduplicate_navigation(body: str) -> str:
    """Conserva la última copia cuando una fuente contiene la misma navegación dos veces."""
    pattern = re.compile(r'<nav class="unit-nav"\b.*?</nav>', re.DOTALL)
    matches = list(pattern.finditer(body))
    if len(matches) < 2:
        return body
    normalized = [re.sub(r"\s+", " ", match.group(0)).strip() for match in matches]
    if len(set(normalized)) != 1:
        return body
    for match in reversed(matches[:-1]):
        body = body[: match.start()] + body[match.end() :]
    return body


def wrap_tables(body: str) -> str:
    """Añade un contenedor de desplazamiento sin alterar la semántica de la tabla."""
    return re.sub(
        r"(<table\b.*?</table>)",
        r'<div class="table-scroll">\1</div>',
        body,
        flags=re.DOTALL,
    )


def text_only(fragment: str) -> str:
    """Convierte un fragmento HTML en texto compacto para metadatos y búsqueda."""
    without_tags = re.sub(r"<[^>]+>", " ", fragment)
    return re.sub(r"\s+", " ", html.unescape(without_tags)).strip()


def practice_metadata() -> dict[str, dict[str, str]]:
    """Extrae CE y evidencias de las matrices, y tiempos exactos cuando existen."""
    metadata: dict[str, dict[str, str]] = {}
    for matrix in SOURCE.glob("RA[1-8]_matriz_contenidos_evaluacion.md"):
        ra_match = re.match(r"(RA[1-8])_", matrix.name)
        if not ra_match:
            continue
        ra = ra_match.group(1)
        source = matrix.read_text(encoding="utf-8")
        for line in source.splitlines():
            code_match = re.search(r"\b(PB\d{2})\b", line)
            if not code_match or not line.lstrip().startswith("|"):
                continue
            code = f"{ra}-{code_match.group(1)}"
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            ce = ""
            for cell in cells:
                if re.fullmatch(r"(?:RA[1-8]\.)?[a-i](?:\s*[,–-]\s*(?:RA[1-8]\.)?[a-i])*", cell):
                    ce = cell
            if ce and not ce.upper().startswith("RA"):
                ce = ", ".join(f"{ra}.{letter}" for letter in re.findall(r"[a-i]", ce))
            updates: dict[str, str] = {}
            if ce:
                updates["criteria"] = ce
            if len(cells) == 4 and ra != "RA1" and cells[-1]:
                updates["evidence"] = cells[-1]
            if updates:
                metadata.setdefault(code, {}).update(updates)

        if ra == "RA1":
            for match in re.finditer(
                r"^###\s+(RA1-PB\d{2})\b.*?(?=^###\s+RA1-PB|^##\s+|\Z)",
                source,
                flags=re.MULTILINE | re.DOTALL,
            ):
                code, block = match.group(1), match.group(0)
                time_match = re.search(r"^-\s+\*\*Tiempo:\*\*\s*(.+)$", block, re.MULTILINE)
                delivery_match = re.search(r"^-\s+\*\*Entrega:\*\*\s*(.+)$", block, re.MULTILINE)
                if time_match:
                    metadata.setdefault(code, {})["duration"] = time_match.group(1).rstrip(".")
                if delivery_match:
                    metadata.setdefault(code, {})["evidence"] = delivery_match.group(1).rstrip(".")
    return metadata


def practice_tools(markdown: str) -> str:
    """Devuelve las herramientas citadas, evitando una lista manual por actividad."""
    lowered = markdown.split("<nav", 1)[0].lower()
    labels = [label for needle, label in TOOL_LABELS.items() if needle in lowered]
    return ", ".join(dict.fromkeys(labels)) or "Navegador y proyecto base"


def practice_cards(
    body: str,
    markdown: str,
    output_name: str,
    metadata: dict[str, dict[str, str]],
) -> str:
    """Convierte cada PB en una ficha operativa y copiable para el profesor."""
    ra_match = re.match(r"(RA[1-8])_", output_name)
    if not ra_match:
        return body
    ra = ra_match.group(1)
    tools = practice_tools(markdown)

    pattern = re.compile(
        r'(<h2 id="(?P<anchor>ra[1-8]-pb\d{2})[^\"]*">(?P<title>.*?)</h2>)'
        r'(?P<content>.*?)(?=<h2\b|<nav class="unit-nav"|\Z)',
        re.DOTALL | re.IGNORECASE,
    )

    def replace(match: re.Match[str]) -> str:
        title_html = match.group("title")
        code_match = re.search(r"RA[1-8]-PB\d{2}", text_only(title_html), re.IGNORECASE)
        if not code_match:
            return match.group(0)
        code = code_match.group(0).upper()
        details = metadata.get(code, {})
        duration = details.get("duration", PRACTICE_DURATIONS[ra])
        criteria = details.get("criteria") or f"Consultar matriz {ra}"
        evidence = details.get("evidence") or "Producto funcional, explicación y comprobación"
        content = match.group("content")
        solution = re.search(r'<h3 id="soluci[^\"]*">.*', content, flags=re.DOTALL | re.IGNORECASE)
        if solution:
            student_content = content[: solution.start()]
            teacher_content = solution.group(0)
            if "<details" not in teacher_content:
                heading_match = re.match(r"(<h3\b.*?</h3>)(.*)", teacher_content, re.DOTALL)
                if heading_match:
                    teacher_content = (
                        f'{heading_match.group(1)}<details><summary>Mostrar guía de corrección</summary>'
                        f'{heading_match.group(2)}</details>'
                    )
        else:
            student_content = content
            teacher_content = ""
        copy_id = f"copy-{code.lower()}"
        return (
            f'<section class="practice-card" data-practice="{html.escape(code)}">'
            '<div class="practice-card__label">Práctica básica</div>'
            f'{match.group(1)}'
            '<dl class="practice-meta">'
            f'<div><dt>Duración</dt><dd>{html.escape(duration)}</dd></div>'
            f'<div><dt>Criterios</dt><dd>{html.escape(criteria)}</dd></div>'
            f'<div><dt>Recursos</dt><dd>{html.escape(tools)}</dd></div>'
            f'<div><dt>Entrega solicitada</dt><dd>{html.escape(evidence)}</dd></div>'
            '</dl>'
            f'<button class="copy-practice" type="button" data-copy-target="{copy_id}">Copiar enunciado</button>'
            f'<div class="practice-student-copy" id="{copy_id}">'
            '<h3>Enunciado para publicar</h3>'
            f'{student_content}</div>'
            + (f'<div class="practice-teacher-solution">{teacher_content}</div>' if teacher_content else "")
            + '</section>'
        )

    return pattern.sub(replace, body)


def page_toc(body: str, output_name: str) -> str:
    """Genera un índice desplegable en documentos internos con varias secciones."""
    if output_name == "index.html":
        return ""
    headings = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body, flags=re.DOTALL)
    if len(headings) < 4:
        return ""
    items = []
    for anchor, label in headings:
        clean_label = html.unescape(re.sub(r"<[^>]+>", "", label)).strip()
        items.append(f'<li><a href="#{html.escape(anchor)}">{html.escape(clean_label)}</a></li>')
    return (
        '<details class="page-toc">'
        '<summary>Contenido de la página</summary>'
        f'<ol>{"".join(items)}</ol>'
        '</details>'
    )


def collapse_home_outline(body: str, output_name: str) -> str:
    """Mantiene la portada breve sin eliminar el inventario detallado del curso."""
    if output_name != "index.html":
        return body
    marker = re.search(r'<h2 id="ra1[^\"]*">', body)
    if not marker:
        return body
    return (
        body[: marker.start()]
        + '<details class="course-outline"><summary>Consultar el desarrollo completo de los ocho RA</summary>'
        + '<div class="course-outline__content">'
        + body[marker.start() :]
        + '</div></details>'
    )


def prepare_body(
    markdown: str,
    output_name: str,
    practices: dict[str, dict[str, str]],
    units: dict[str, list[dict[str, str]]],
) -> str:
    body = render_markdown(markdown)
    body = remove_first_heading(body)
    body = deduplicate_navigation(body)
    body = practice_cards(body, markdown, output_name, practices)
    body = wrap_tables(body)
    body = collapse_home_outline(body, output_name)
    toc = page_toc(body, output_name)
    route = ra_route(output_name, units)
    additions = "\n".join(item for item in (toc, route) if item)
    return f"{additions}\n{body}" if additions else body


def ra_class(filename: str) -> str:
    match = re.match(r"RA([1-8])_", filename, re.IGNORECASE)
    return f"ra-ra{match.group(1)}" if match else "site-home"


THEME_COLORS = {
    "ra-ra1": "#6750a4",
    "ra-ra2": "#006a6a",
    "ra-ra3": "#8c5000",
    "ra-ra4": "#006b5f",
    "ra-ra5": "#984061",
    "ra-ra6": "#3f5f90",
    "ra-ra7": "#5b5f00",
    "ra-ra8": "#745b00",
}


def ra_number(output_name: str) -> str | None:
    match = re.match(r"RA([1-8])_", output_name, re.IGNORECASE)
    return match.group(1) if match else None


def unit_catalog(sources: list[Path]) -> dict[str, list[dict[str, str]]]:
    """Cataloga las unidades reales para posición e itinerarios docentes."""
    units: dict[str, list[dict[str, str]]] = {str(number): [] for number in range(1, 9)}
    for source in sources:
        match = re.match(r"RA([1-8])_(\d{2})_(.+)\.md$", source.name)
        if not match or match.group(2) == "00":
            continue
        metadata, markdown = split_front_matter(source.read_text(encoding="utf-8"))
        title = metadata.get("title") or plain_heading(markdown, source.stem)
        practice = re.search(r"^##\s+(RA[1-8]-PB\d{2})\b", markdown, re.MULTILINE)
        units[match.group(1)].append(
            {
                "number": str(int(match.group(2))),
                "title": title,
                "url": source.with_suffix(".html").name,
                "practice": practice.group(1) if practice else "",
            }
        )
    for items in units.values():
        items.sort(key=lambda item: int(item["number"]))
    return units


def page_position(output_name: str, units: dict[str, list[dict[str, str]]]) -> str:
    number = ra_number(output_name)
    if not number:
        return "Curso completo · 8 resultados de aprendizaje"
    if output_name == f"RA{number}_00_guia_docente.html":
        return f"RA{number} · Guía docente"
    if output_name == f"RA{number}_matriz_contenidos_evaluacion.html":
        return f"RA{number} · Matriz curricular"
    if output_name == f"RA{number}_integrador.html":
        return f"RA{number} · Integrador"
    for index, item in enumerate(units[number], start=1):
        if item["url"] == output_name:
            return f"RA{number} · Unidad {index} de {len(units[number])}"
    return f"RA{number} · Material complementario"


def ra_route(output_name: str, units: dict[str, list[dict[str, str]]]) -> str:
    """Añade a cada guía un itinerario inequívoco de unidades, PB e integrador."""
    number = ra_number(output_name)
    if not number or output_name != f"RA{number}_00_guia_docente.html":
        return ""
    cards = []
    for index, item in enumerate(units[number], start=1):
        practice = f'<span>{html.escape(item["practice"])}</span>' if item["practice"] else ""
        cards.append(
            f'<a class="ra-route__step" href="{html.escape(item["url"])}">'
            f'<small>Unidad {index}</small><strong>{html.escape(item["title"])}</strong>{practice}</a>'
        )
    cards.append(
        f'<a class="ra-route__step ra-route__step--integrator" href="RA{number}_integrador.html">'
        f'<small>Evaluación</small><strong>Integrador RA{number}</strong><span>INT01</span></a>'
    )
    return (
        '<section class="ra-route" aria-labelledby="itinerario-ra">'
        '<h2 id="itinerario-ra">Itinerario del RA</h2>'
        '<p>Acceso directo a las unidades, sus prácticas y la evaluación integradora.</p>'
        f'<div class="ra-route__grid">{"".join(cards)}</div></section>'
    )


def context_navigation(output_name: str) -> str:
    number = ra_number(output_name)
    if not number:
        return ""
    destinations = [
        ("index.html", "Inicio"),
        (f"RA{number}_00_guia_docente.html", f"Guía RA{number}"),
        (f"RA{number}_matriz_contenidos_evaluacion.html", "Matriz"),
        (f"RA{number}_integrador.html", "Integrador"),
    ]
    links = []
    for href, label in destinations:
        if href == output_name:
            links.append(f'<span aria-current="page">{html.escape(label)}</span>')
        else:
            links.append(f'<a href="{href}">{html.escape(label)}</a>')
    links.append('<button class="search-toggle" type="button" data-search-open>Buscar</button>')
    return (
        '<nav class="context-nav" aria-label="Accesos del resultado de aprendizaje">'
        f'<div class="context-nav__inner">{"".join(links)}</div>'
        '</nav>'
    )


def search_dialog() -> str:
    return """  <dialog class="search-dialog" id="site-search" aria-labelledby="search-title">
    <div class="search-dialog__header">
      <div><small>Buscador docente</small><h2 id="search-title">Buscar en el curso</h2></div>
      <button class="search-close" type="button" data-search-close aria-label="Cerrar buscador">×</button>
    </div>
    <label class="search-field">Concepto, criterio, herramienta o práctica
      <input type="search" id="site-search-input" autocomplete="off" placeholder="Ej.: RA4.g, accesibilidad, PB03…">
    </label>
    <p class="search-status" id="site-search-status" aria-live="polite">Escribe al menos dos caracteres.</p>
    <ol class="search-results" id="site-search-results"></ol>
  </dialog>"""


def document(
    title: str,
    body: str,
    css_class: str,
    output_name: str,
    asset_version: str,
    units: dict[str, list[dict[str, str]]],
) -> str:
    safe_title = html.escape(title)
    safe_description = html.escape(SITE_DESCRIPTION)
    theme_color = THEME_COLORS.get(css_class, "#6750a4")
    home = output_name == "index.html"
    brand = (
        ""
        if home
        else '      <a class="site-brand" href="index.html">Desarrollo de Interfaces · DAM</a>\n'
    )
    tagline = f'      <p class="project-tagline">{safe_description}</p>\n' if home else ""
    position = html.escape(page_position(output_name, units))
    context_nav = context_navigation(output_name)
    context_markup = (
        f"  {context_nav}\n"
        if context_nav
        else '  <nav class="site-tools" aria-label="Herramientas del curso"><div class="site-tools__inner"><button class="search-toggle" type="button" data-search-open>Buscar en el curso</button></div></nav>\n'
    )
    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="{theme_color}">
  <meta name="description" content="{safe_description}">
  <title>{safe_title} · Desarrollo de Interfaces</title>
  <link rel="stylesheet" href="assets/css/style.css?v={asset_version}">
  <script src="assets/js/search-index.js?v={asset_version}" defer></script>
  <script src="assets/js/site.js?v={asset_version}" defer></script>
</head>
<body class="{css_class}">
  <a class="skip-link" href="#contenido">Saltar al contenido</a>
  <header class="page-header" role="banner">
    <div class="page-header__inner">
{brand}      <h1 class="project-name">{safe_title}</h1>
{tagline}      <p class="page-position">{position}</p>
      <p class="page-reviewed">Revisado: {REVIEW_DATE}</p>
    </div>
  </header>
{context_markup}  <main id="contenido" class="main-content" role="main">
{body}
    <footer class="site-footer">
      <a class="back-to-top" href="#contenido">↑ Volver arriba</a>
      <span>Desarrollo de Interfaces · DAM · Módulo 0488</span>
    </footer>
  </main>
{search_dialog()}
  <div class="copy-status" id="copy-status" aria-live="polite"></div>
</body>
</html>
"""


def page_kind(output_name: str) -> str:
    if output_name == "index.html":
        return "Curso"
    if "_00_guia_docente" in output_name:
        return "Guía docente"
    if "_matriz_" in output_name:
        return "Matriz"
    if "_integrador" in output_name:
        return "Integrador"
    if "_anexo_" in output_name:
        return "Anexo"
    return "Unidad"


def main() -> None:
    sources = sorted(SOURCE.glob("*.md"))
    if not sources:
        raise SystemExit("No se han encontrado fuentes Markdown en src/")
    units = unit_catalog(sources)
    practices = practice_metadata()
    script_path = ROOT / "assets/js/site.js"
    version_material = (ROOT / "assets/css/style.css").read_bytes() + script_path.read_bytes()
    version_material += b"".join(source.read_bytes() for source in sources)
    asset_version = hashlib.sha256(version_material).hexdigest()[:10]
    search_entries = []
    for source in sources:
        metadata, markdown = split_front_matter(source.read_text(encoding="utf-8"))
        output_name = "index.html" if source.name == "index.md" else source.with_suffix(".html").name
        title = metadata.get("title") or plain_heading(markdown, source.stem)
        body = prepare_body(markdown, output_name, practices, units)
        (ROOT / output_name).write_text(
            document(
                title,
                body,
                ra_class(source.name),
                output_name,
                asset_version,
                units,
            ),
            encoding="utf-8",
        )
        number = ra_number(output_name)
        search_entries.append(
            {
                "title": title,
                "url": output_name,
                "ra": f"RA{number}" if number else "Curso",
                "kind": page_kind(output_name),
                "text": text_only(body)[:7000],
            }
        )
    search_path = ROOT / "assets/js/search-index.js"
    search_path.write_text(
        "window.DI_SEARCH_INDEX = "
        + json.dumps(search_entries, ensure_ascii=False, separators=(",", ":"))
        + ";\n",
        encoding="utf-8",
    )
    print(f"Generadas {len(sources)} páginas HTML estáticas.")


if __name__ == "__main__":
    main()
