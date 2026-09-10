---
layout: default
title: RA2-02 · Interfaces naturales y tipos
---

# RA2-02 · Interfaces naturales y tipos

## Objetivo docente

Diseñar una interacción natural completa y elegir entre voz, gesto, mirada, tacto o combinación multimodal según el contexto.

## Contenido para explicar

El ciclo es **entrada → interpretación → intención → acción → respuesta**. La interfaz debe mostrar cuándo capta datos, qué ha entendido y cómo cancelar o corregir. La modalidad adecuada depende del ruido, iluminación, movilidad, privacidad, precisión, fatiga y capacidades de la persona.

Una interfaz multimodal permite combinar canales o sustituir uno por otro. «Natural» no significa invisible: la persona necesita saber si el sistema escucha o mira.

## Ejemplo básico resuelto

| Tarea | Entrada | Intención | Acción | Respuesta | Alternativa |
|---|---|---|---|---|---|
| Ver tareas pendientes | «Mostrar pendientes» | Filtrar | Aplicar filtro | Chip y anuncio de resultado | Botón «Pendientes» |
| Completar tarea | Mano abierta 1 s | Confirmar | Cambiar estado | Animación y texto | Casilla etiquetada |

Stitch genera los estados reposo, solicitando permiso, activo, no entendido y detenido. Gemini revisa que cada estado tenga texto y no dependa solo del color.

## RA2-PB02 · Diseñar un flujo natural

Elige dos tareas del gestor y crea su mapa completo. Incluye contexto favorable, contexto problemático, señal de activación, corrección, cancelación y alternativa convencional. Genera con Stitch los cinco estados del sistema.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

Para «crear tarea», la voz es útil con manos ocupadas, pero problemática en un aula ruidosa. Se activa con un botón explícito, transcribe antes de guardar y permite editar o cancelar. Para «avanzar tarjeta», un gesto puede servir a distancia; se exige mantenerlo 600 ms y existe un botón «Siguiente». Los mockups distinguen permiso, captación, interpretación, confirmación y error.

</details>

## Comprobación y cierre

Explica por qué la modalidad elegida mejora una tarea concreta y en qué situación la empeora. Demuestra que detener el sensor no bloquea la aplicación.

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA2_01_aprendizaje_automatico.html">← RA2-01</a><a href="https://mosqueteroweb.github.io/damDI/RA2_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA2_03_voz_habla.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA2-03 · Voz, habla y reconocimiento</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
