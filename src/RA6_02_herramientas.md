---
layout: default
title: RA6-02 · Herramientas de generación
---

# RA6-02 · Herramientas de generación de ayudas

## Objetivo docente

Identificar sistemas de ayuda y seleccionar un flujo reproducible de fuente, generación, validación y publicación.

## Contenido para explicar

Se comparan editor visual, generador estático y procesador documental. Stitch diseña; Gemini/AI Studio redacta y transforma; Markdown mantiene la fuente; Pandoc genera HTML. MkDocs se estudia como opción con navegación y búsqueda, pero el curso conserva su generador actual para no duplicar infraestructura.

## RA6-EJ02 · Ejemplo resuelto

```bash
python scripts/build_static.py
```

El comando recorre `src/`, convierte Markdown y conserva nombres. El alumnado localiza entrada, salida y fallo; no memoriza el script.

| Herramienta | Entrada | Salida | Decisión |
|---|---|---|---|
| Stitch | requisitos | diseño | arquitectura visual |
| Gemini | versión y función | borrador | contenido a verificar |
| Pandoc | Markdown | HTML | publicación estática |

## RA6-PB02 · Cadena reproducible

Genera una página de ayuda desde Markdown, modifica una frase en la fuente, regenera y demuestra que el HTML cambia sin edición manual. Documenta un fallo y su diagnóstico.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

La entrega conserva fuente y salida, comando y versión. Tras cambiar «Eliminar» por «Archivar», solo se edita Markdown y se regenera. Un enlace `.md` se transforma en `.html`; la comprobación evita publicar una ruta rota.

</details>

## Cierre

Justifica por qué el HTML generado no debe convertirse en segunda fuente editable.

Referencia: [manual oficial de Pandoc](https://pandoc.org/MANUAL.html).

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA6_01_formatos_ayuda.html">← RA6-01</a><a href="https://mosqueteroweb.github.io/damDI/RA6_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA6_03_navegacion_contexto.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA6-03 · Navegación, búsqueda y contexto</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
