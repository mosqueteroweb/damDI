---
layout: default
title: RA8-06 · Pruebas manuales, automáticas y regresión
---

# RA8-06 · Pruebas manuales, automáticas y de regresión

## Objetivo docente

Elegir qué automatizar, construir una suite mínima de regresión y documentar resultados repetibles.

## Contenido para explicar

La prueba manual favorece exploración, percepción y casos nuevos; la automática repite comprobaciones estables con rapidez. La regresión protege comportamientos que funcionaban antes de un cambio. Una suite pequeña debe ser determinista, aislar datos y producir mensajes útiles.

## Ejemplo básico resuelto

El grabador visual define una preparación «Restablecer datos», un caso llamado «Conserva el título al fallar la validación» y una comprobación final: el campo sigue mostrando «Revisar informe». La preparación aísla el estado; el nombre describe el comportamiento; la comprobación protege una regresión concreta.

## RA8-PB06 · Del defecto a la regresión

Elige un defecto corregido, escribe primero el caso manual, pide a Gemini que lo transforme en pasos para el grabador visual, identifica controles y comprobación, ejecútalo antes y después y añade la prueba a una colección de cinco flujos críticos.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

La colección cubre alta, validación, filtro, borrado recuperable e informe. Usa datos reiniciados y controles identificados por nombres accesibles. La prueba del defecto falla en la versión base y pasa tras la corrección. El informe registra navegador, versión, 5/5 pruebas y duración; una revisión manual de foco y claridad complementa la colección.

</details>

## Cierre

Justifica qué caso mantienes manual y qué señal te haría retirar o reparar una prueba automática inestable.

El informe se consulta y exporta desde el panel de resultados del grabador visual.

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA8_05_seguridad.html">← RA8-05</a><a href="https://mosqueteroweb.github.io/damDI/RA8_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA8_integrador.html"><span class="unit-next-card__eyebrow">Ejercicio integrador</span><strong>RA8-INT01 · Certificación interna del gestor</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
