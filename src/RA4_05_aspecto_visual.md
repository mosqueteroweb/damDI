---
layout: default
title: RA4-05 · Aspecto visual y legibilidad
---

# RA4-05 · Color, tipografía, iconos y distribución

## Objetivo docente

Aplicar un sistema visual consistente y justificar legibilidad con evidencias, no con preferencias personales.

## Contenido para explicar

Material Design 3 organiza decisiones mediante roles y tokens. El color comunica jerarquía y estado, pero no debe ser el único canal. La tipografía necesita escala, contraste y espacio. Los iconos ambiguos requieren texto o nombre accesible. La distribución debe conservar agrupación y lectura al cambiar el ancho.

## Ejemplo básico resuelto

```css
:root {
  --md-sys-color-primary: #6750a4;
  --md-sys-color-on-primary: #ffffff;
  --md-sys-color-error: #b3261e;
  --md-sys-color-on-error: #ffffff;
}
```

El alumno identifica parejas superficie/contenido. No elige blanco «porque queda bien»: verifica contraste, uso y estado. Un error añade texto e icono además del color.

## RA4-PB05 · Sistema visual legible

Pide a Gemini dos variantes M3 del gestor. Define seis tokens, una escala tipográfica corta y tres reglas de distribución. Comprueba contraste y zoom al 200 %.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

La solución conserva una pareja principal/on-primary, superficie/on-surface y error/on-error; usa título, cuerpo y etiqueta; limita ancho de lectura; permite salto de línea; y no fija alturas que corten texto. Se documentan valores medidos y una comprobación visual a zoom.

</details>

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA4_04_estructura_navegacion.html">← RA4-04</a><a href="https://mosqueteroweb.github.io/damDI/RA4_00_guia_docente.html">Índice RA4</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA4_06_elementos_interactivos.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA4-06 · Elementos interactivos</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
