---
layout: default
title: RA5-03 · Estructura y secciones
---

# RA5-03 · Estructura general y secciones

## Objetivo docente

Organizar un informe para que responda una pregunta, muestre contexto y permita pasar del resumen al detalle.

## Contenido para explicar

Un informe básico incluye encabezado, contexto y fecha de corte, filtros, indicadores clave, visualización, detalle tabular, notas metodológicas y estados de carga, vacío o error. La jerarquía M3 evita que todas las tarjetas compitan con igual peso.

## Ejemplo básico resuelto

```html
<main>
  <header><h1>Seguimiento de tareas</h1><p>Actualizado: 15/09/2026</p></header>
  <form aria-label="Filtros del informe"></form>
  <section aria-labelledby="summary-title"><h2 id="summary-title">Resumen</h2></section>
  <section aria-labelledby="detail-title"><h2 id="detail-title">Detalle</h2></section>
  <aside aria-labelledby="method-title"><h2 id="method-title">Cómo se calcula</h2></aside>
</main>
```

La estructura generada usa regiones y encabezados; el orden responde primero qué ocurre, después dónde ocurre y finalmente cómo se calculó.

## RA5-PB03 · Esqueleto de informe

Solicita a Stitch un informe responsive con los estados carga, sin datos y error. Pide a Gemini el HTML semántico correspondiente. Anota propósito, entrada y salida de cada sección.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

El encabezado muestra título, periodo y actualización; los filtros preceden a cuatro indicadores; después aparecen gráfico y tabla; metodología cierra el informe. El estado vacío conserva filtros y explica cómo ampliar resultados. El error distingue «no se pudo cargar» de «no hay datos». En móvil se mantiene el mismo orden lógico.

</details>

## Cierre

Comprueba el esquema de encabezados y responde: ¿qué pregunta contesta cada sección y cuál puede eliminarse sin perder la decisión principal?

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA5_02_herramientas_graficas.html">← RA5-02</a><a href="https://mosqueteroweb.github.io/damDI/RA5_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA5_04_filtrado_datos.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA5-04 · Filtrado de datos</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
