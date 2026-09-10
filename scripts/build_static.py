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
    return re.sub(
        r'href="([^"#]+)\.md(#[^"]*)?"',
        lambda match: f'href="{match.group(1)}.html{match.group(2) or ""}"',
        result.stdout,
    )


def ra_class(filename: str) -> str:
    match = re.match(r"RA([1-8])_", filename, re.IGNORECASE)
    return f"ra-ra{match.group(1)}" if match else "site-home"


def document(title: str, body: str, css_class: str) -> str:
    safe_title = html.escape(title)
    safe_description = html.escape(SITE_DESCRIPTION)
    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#6750a4">
  <meta name="description" content="{safe_description}">
  <title>{safe_title} · Desarrollo de Interfaces</title>
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body class="{css_class}">
  <a class="skip-link" href="#contenido">Saltar al contenido</a>
  <header class="page-header" role="banner">
    <h1 class="project-name">{safe_title}</h1>
    <p class="project-tagline">{safe_description}</p>
  </header>
  <main id="contenido" class="main-content" role="main">
{body}
    <footer class="site-footer">
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
            document(title, render_markdown(markdown), ra_class(source.name)),
            encoding="utf-8",
        )
    print(f"Generadas {len(sources)} páginas HTML estáticas.")


if __name__ == "__main__":
    main()
