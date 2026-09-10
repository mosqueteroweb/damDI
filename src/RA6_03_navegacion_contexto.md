---
layout: default
title: RA6-03 · Navegación, búsqueda y ayuda contextual
---

# RA6-03 · Tablas de contenidos, índices, búsqueda y ayuda contextual

## Objetivo docente

Construir un centro de ayuda localizable y enlazar cada pantalla con la respuesta pertinente.

## Contenido para explicar

La tabla de contenidos refleja jerarquía; el índice ofrece términos del usuario; la búsqueda encuentra texto y sinónimos; la ayuda contextual abre el tema exacto sin perder la tarea. Los enlaces necesitan títulos claros, foco visible y retorno.

## RA6-EJ03 · Ejemplo resuelto

```html
<a href="ayuda.html#crear-tarea" aria-describedby="help-context">Ayuda</a>
<span id="help-context" hidden>sobre el formulario Crear tarea</span>
```

El fragmento enlaza al ancla específica y aporta contexto al nombre. La página de destino empieza por la respuesta, no por una portada genérica.

## RA6-PB03 · Encontrar ayuda en dos pasos

Diseña con Stitch una portada con contenidos, índice A–Z y búsqueda. Añade ayuda contextual a crear, filtrar y borrar. Prueba cinco consultas, incluidos sinónimos y cero resultados.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

«Nueva», «alta» y «crear» llevan a la misma tarea. Desde Borrar se abre directamente «Eliminar o deshacer». Cero resultados propone términos y contenidos principales. Teclado y botón Atrás conservan foco y contexto. Ningún recorrido supera dos decisiones desde la portada.

</details>

## Cierre

Entrega mapa de navegación y tabla consulta–resultado esperado–real.

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA6_02_herramientas.html">← RA6-02</a><a href="https://mosqueteroweb.github.io/damDI/RA6_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA6_04_manuales_datos.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA6-04 · Manuales y datos persistentes</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
