#!/usr/bin/env python3
"""Genera la web estática de damDI a partir de los Markdown de src/."""

from __future__ import annotations

import html
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "src"
SITE_DESCRIPTION = "Material docente del módulo 0488 con IA, web y Material Design 3."
PUBLIC_BASE_URL = "https://mosqueteroweb.github.io/damDI/"


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


def prepare_body(markdown: str, output_name: str) -> str:
    body = render_markdown(markdown)
    body = remove_first_heading(body)
    body = deduplicate_navigation(body)
    body = wrap_tables(body)
    body = collapse_home_outline(body, output_name)
    toc = page_toc(body, output_name)
    return f"{toc}\n{body}" if toc else body


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
    return (
        '<nav class="context-nav" aria-label="Accesos del resultado de aprendizaje">'
        f'<div class="context-nav__inner">{"".join(links)}</div>'
        '</nav>'
    )


def document(title: str, body: str, css_class: str, output_name: str) -> str:
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
    context_nav = context_navigation(output_name)
    context_markup = f"  {context_nav}\n" if context_nav else ""
    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="{theme_color}">
  <meta name="description" content="{safe_description}">
  <title>{safe_title} · Desarrollo de Interfaces</title>
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body class="{css_class}">
  <a class="skip-link" href="#contenido">Saltar al contenido</a>
  <header class="page-header" role="banner">
    <div class="page-header__inner">
{brand}      <h1 class="project-name">{safe_title}</h1>
{tagline}    </div>
  </header>
{context_markup}  <main id="contenido" class="main-content" role="main">
{body}
    <footer class="site-footer">
      <a class="back-to-top" href="#contenido">↑ Volver arriba</a>
      <span>Desarrollo de Interfaces · DAM · Módulo 0488</span>
    </footer>
  </main>
</body>
</html>
"""


def main() -> None:
    sources = sorted(SOURCE.glob("*.md"))
    if not sources:
        raise SystemExit("No se han encontrado fuentes Markdown en src/")
    for source in sources:
        metadata, markdown = split_front_matter(source.read_text(encoding="utf-8"))
        output_name = "index.html" if source.name == "index.md" else source.with_suffix(".html").name
        title = metadata.get("title") or plain_heading(markdown, source.stem)
        (ROOT / output_name).write_text(
            document(title, prepare_body(markdown, output_name), ra_class(source.name), output_name),
            encoding="utf-8",
        )
    print(f"Generadas {len(sources)} páginas HTML estáticas.")


if __name__ == "__main__":
    main()
