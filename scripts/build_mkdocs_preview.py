#!/usr/bin/env python3
"""Construye una vista MkDocs completa sin alterar la web vigente de la raíz."""

from __future__ import annotations

import re
import json
import shutil
import subprocess
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "src"
STAGING = ROOT / ".mkdocs-preview-src"
CONFIG = ROOT / "mkdocs.preview.yml"
PUBLIC_BASE = "https://mosqueteroweb.github.io/damDI/"


def extract_figure(page: Path) -> str:
    if not page.exists():
        return ""
    match = re.search(
        r'<figure class="concept-figure">.*?</figure>',
        page.read_text(encoding="utf-8"),
        flags=re.DOTALL,
    )
    return match.group(0) if match else ""


def remove_legacy_navigation(markdown: str) -> str:
    return re.sub(
        r'\n*<nav class="unit-nav".*?</nav>\s*',
        "\n",
        markdown,
        flags=re.DOTALL,
    )


def rewrite_internal_links(markdown: str) -> str:
    markdown = markdown.replace(f"{PUBLIC_BASE}#", "index.md#")
    return markdown.replace(PUBLIC_BASE, "")


def add_figure(markdown: str, figure: str) -> str:
    if not figure or 'class="concept-figure"' in markdown:
        return markdown
    section = re.search(r"(^##\s+.+\n(?:\n|.)*?\n)(?=##\s+)", markdown, re.MULTILINE)
    if section:
        position = section.end(1)
        return f"{markdown[:position]}\n{figure}\n\n{markdown[position:]}"
    return f"{markdown}\n\n{figure}\n"


def display_title(source: Path) -> str:
    text = source.read_text(encoding="utf-8")
    front = re.match(r"---\n(.*?)\n---", text, re.DOTALL)
    if front:
        title = re.search(r"^title:\s*(.+)$", front.group(1), re.MULTILINE)
        if title:
            return title.group(1).strip().strip("\"'")
    heading = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    return heading.group(1) if heading else source.stem


def normalize_front_matter(markdown: str) -> str:
    """Hace compatible con YAML estricto un título antiguo que contiene dos puntos."""
    front = re.match(r"---\n(.*?)\n---", markdown, re.DOTALL)
    if not front:
        return markdown
    lines = front.group(1).splitlines()
    for index, line in enumerate(lines):
        if line.startswith("title:"):
            value = line.split(":", 1)[1].strip().strip("\"'")
            lines[index] = f"title: {json.dumps(value, ensure_ascii=False)}"
    normalized = "\n".join(lines)
    return f"---\n{normalized}\n---{markdown[front.end():]}"


def navigation(sources: list[Path]) -> list[dict[str, object]]:
    nav: list[dict[str, object]] = [{"Inicio": "index.md"}]
    for number in range(1, 9):
        prefix = f"RA{number}_"
        items: list[dict[str, str]] = []
        ordered = sorted(p for p in sources if p.name.startswith(prefix))
        for source in ordered:
            label = display_title(source)
            if source.name == f"RA{number}_00_guia_docente.md":
                label = "Guía docente"
            elif "_matriz_" in source.name:
                label = "Matriz de contenidos y evaluación"
            elif "_integrador" in source.name:
                label = "Ejercicio integrador"
            elif "_anexo_android_" in source.name:
                label = "Ampliación voluntaria · Android"
            items.append({label: source.name})
        nav.append({f"RA{number}": items})
    return nav


def prepare_sources() -> list[Path]:
    if STAGING.exists():
        shutil.rmtree(STAGING)
    STAGING.mkdir()
    sources = sorted(SOURCE.glob("*.md"))
    for source in sources:
        markdown = source.read_text(encoding="utf-8")
        markdown = normalize_front_matter(markdown)
        markdown = remove_legacy_navigation(markdown)
        markdown = rewrite_internal_links(markdown)
        output_name = "index.html" if source.name == "index.md" else source.with_suffix(".html").name
        markdown = add_figure(markdown, extract_figure(ROOT / output_name))
        (STAGING / source.name).write_text(markdown, encoding="utf-8")

    shutil.copytree(ROOT / "assets" / "img", STAGING / "assets" / "img")
    shutil.copy2(ROOT / "tareas.html", STAGING / "tareas.html")
    styles = STAGING / "stylesheets"
    styles.mkdir()
    shutil.copy2(ROOT / "mkdocs-preview-assets" / "preview.css", styles / "preview.css")
    return sources


def reuse_published_assets() -> None:
    """Evita duplicar en la comparativa imágenes y demo ya publicadas en la raíz."""
    output = ROOT / "mkdocs-preview"
    for page in output.rglob("*.html"):
        text = page.read_text(encoding="utf-8")
        text = text.replace('src="assets/img/', 'src="../assets/img/')
        text = text.replace('href="tareas.html"', 'href="../tareas.html"')
        page.write_text(text, encoding="utf-8")
    shutil.rmtree(output / "assets" / "img", ignore_errors=True)
    (output / "tareas.html").unlink(missing_ok=True)

    for source_map in output.rglob("*.map"):
        source_map.unlink()
    lunr = output / "assets" / "javascripts" / "lunr"
    for helper in (lunr / "tinyseg.js", lunr / "wordcut.js"):
        helper.unlink(missing_ok=True)
    keep = {"lunr.es.min.js", "lunr.stemmer.support.min.js"}
    for language in (lunr / "min").glob("*.js"):
        if language.name not in keep:
            language.unlink()


def main() -> None:
    mkdocs = Path(sys.executable).with_name("mkdocs")
    if not mkdocs.exists():
        raise SystemExit("MkDocs no está disponible en este entorno de Python.")
    sources = prepare_sources()
    config = yaml.safe_load(CONFIG.read_text(encoding="utf-8"))
    config["nav"] = navigation(sources)
    generated_config = ROOT / ".mkdocs-preview.generated.yml"
    generated_config.write_text(
        yaml.safe_dump(config, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
    try:
        subprocess.run([str(mkdocs), "build", "--clean", "--strict", "-f", str(generated_config)], check=True)
        reuse_published_assets()
    finally:
        generated_config.unlink(missing_ok=True)
        shutil.rmtree(STAGING, ignore_errors=True)


if __name__ == "__main__":
    main()
