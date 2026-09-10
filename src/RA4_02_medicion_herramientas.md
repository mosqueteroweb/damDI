---
layout: default
title: RA4-02 · Medidas y herramientas
---

# RA4-02 · Medidas de usabilidad y accesibilidad

## Objetivo docente

Diseñar una prueba reproducible y combinar herramientas automáticas con comprobaciones humanas.

## Contenido para explicar

Una medida necesita tarea, participante o procedimiento, condición y resultado. En usabilidad pueden observarse finalización, tiempo, errores, retrocesos y satisfacción. En accesibilidad se combinan validadores, inspección del árbol accesible, teclado, ampliación y revisión manual.

Una puntuación global no explica qué falla ni demuestra que una persona pueda completar la tarea.

## Ejemplo básico resuelto

Tarea: «Añade una tarea urgente y elimínala».

| Medida | Resultado inicial | Interpretación |
|---|---:|---|
| Finalización | 2/3 | Una persona no localizó prioridad |
| Errores | 4 | Dos borrados accidentales |
| Pulsaciones Tab | 11 | El foco pasa por controles ocultos |
| Hallazgos automáticos | 3 | Falta confirmar manualmente impacto |

Decisión: arreglar primero el orden de foco y el borrado recuperable; después repetir exactamente el protocolo.

## RA4-PB02 · Auditoría reproducible

Ejecuta Lighthouse o herramienta equivalente y tres pruebas manuales: teclado, zoom al 200 % y comprensión de mensajes. Corrige un problema y repite la prueba.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

Informe mínimo: versión y URL; herramienta; pasos; resultado inicial; cambio; resultado posterior; límite de la prueba. Ejemplo: al 200 % el botón se solapa; se sustituye ancho fijo por distribución flexible; se repite a igual tamaño; desaparece el solapamiento. No se concluye que toda la web sea accesible.

</details>

## Fragmentos relevantes

El alumno localiza la regla CSS cambiada, el elemento afectado y la evidencia anterior/posterior. La IA puede explicar el cambio, pero la comprobación debe realizarse en navegador.

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA4_01_usabilidad_accesibilidad.html">← RA4-01</a><a href="https://mosqueteroweb.github.io/damDI/RA4_00_guia_docente.html">Índice RA4</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA4_03_wireframes_mockups.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA4-03 · Wireframes y mockups</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
