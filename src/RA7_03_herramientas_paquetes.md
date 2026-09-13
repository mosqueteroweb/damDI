---
layout: default
title: RA7-03 · Herramientas para crear paquetes
---

# RA7-03 · Herramientas para crear paquetes de instalación

## Objetivo docente

Generar la misma versión web mediante dos interfaces visuales, comparando trazabilidad y repetibilidad.

## Contenido para explicar

El editor con IA puede ofrecer una acción de publicación y GitHub puede crear una versión desde su interfaz web. Ambas rutas deben partir de la misma revisión, producir una versión identificada y mostrar los fallos de forma visible. El historial de la plataforma aporta trazabilidad, pero no convierte automáticamente cualquier resultado en una versión válida.

<figure class="concept-figure"><img src="assets/img/ra7/ra7-03-rutas-sin-comandos.png" alt="Dos rutas visuales, el editor web con IA y la interfaz web del repositorio, parten de la misma revisión y recorren revisar, validar, publicar y verificar." loading="lazy" width="1672" height="941"><figcaption>Dos interfaces son equivalentes solo si parten de la misma revisión y producen la misma versión publicada y verificable.</figcaption></figure>

## Ejemplo básico resuelto

La IA propone una tarjeta de publicación con cuatro estados visibles: **Revisar**, **Validar**, **Publicar** y **Verificar**. El alumnado identifica la revisión de entrada, el orden, el punto que bloquea la publicación y la URL resultante; después contrasta el resultado con la creación de una versión desde la interfaz web del repositorio.

## RA7-PB03 · Dos rutas, un artefacto

Publica una versión desde la acción visual del editor y crea otra desde la interfaz web del repositorio usando la misma revisión. Compara archivos, tamaño, identificador e integridad. Explica cualquier diferencia.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

Ambas rutas parten de la misma revisión y aplican las mismas validaciones. El registro conserva identificador, fecha, versión y resultado. Si los valores de integridad difieren por metadatos, se documenta y se compara el contenido; no se oculta la diferencia.

</details>

## Cierre

Señala qué evidencia demuestra que la herramienta externa no depende de tu equipo.

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA7_02_instaladores_autoinstalables.html">← RA7-02</a><a href="https://mosqueteroweb.github.io/damDI/RA7_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA7_04_personalizacion.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA7-04 · Personalización de la instalación</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
