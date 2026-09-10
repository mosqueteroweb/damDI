---
layout: default
title: RA4-07 · Secuencia de control y mensajes
---

# RA4-07 · Secuencia de control y mensajes

## Objetivo docente

Diseñar recorridos comprensibles, prevenir errores y redactar mensajes claros, accionables y verificables.

## Contenido para explicar

La secuencia de control describe estados y transiciones: inicio, entrada, validación, confirmación, resultado y recuperación. La interfaz debe mantener informado al usuario, impedir pérdidas evitables y ofrecer salida. Un mensaje útil dice qué ocurrió, dónde y qué puede hacerse.

## Ejemplo básico resuelto

Mensaje inicial: «Error 17».

Revisión: «No se guardó la tarea porque falta el título. Escríbelo y vuelve a pulsar Guardar».

El segundo mensaje identifica resultado, causa y acción. Debe aparecer cerca del campo, asociarse programáticamente y conservar los datos ya escritos.

```html
<input id="titulo" aria-describedby="error-titulo" aria-invalid="true">
<p id="error-titulo">Escribe un título para guardar la tarea.</p>
```

## RA4-PB07 · Flujo recuperable

Dibuja el flujo de alta y borrado. Reescribe seis mensajes, añade recuperación ante borrado y ejecuta cinco casos: correcto, vacío, dato inválido, cancelación y recuperación.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

Estados mínimos: formulario vacío → edición → validación → guardado o error; tarea visible → borrado → aviso con «Deshacer» → restaurada o eliminación confirmada. Las pruebas registran entrada, acción, resultado esperado, resultado observado y evidencia.

</details>

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA4_06_elementos_interactivos.html">← RA4-06</a><a href="https://mosqueteroweb.github.io/damDI/RA4_00_guia_docente.html">Índice RA4</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA4_integrador.html"><span class="unit-next-card__eyebrow">Evaluación integradora</span><strong>RA4-INT01 · Rediseño accesible del gestor</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
