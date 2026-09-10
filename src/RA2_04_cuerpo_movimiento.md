---
layout: default
title: RA2-04 · Partes y movimientos del cuerpo
---

# RA2-04 · Detección de partes y movimientos del cuerpo

## Objetivo docente

Convertir puntos corporales detectados en gestos estables que activen acciones, con umbral, tiempo de permanencia y alternativa manual.

## Contenido para explicar

MediaPipe Pose Landmarker devuelve puntos de referencia del cuerpo; Hand Landmarker devuelve puntos de la mano. Una aplicación no debe reaccionar a un fotograma aislado: necesita confianza mínima, varias observaciones coherentes o permanencia, zona segura y tiempo de espera para impedir repeticiones.

La cámara se inicia mediante una acción clara y puede detenerse. Las imágenes de evaluación pueden sustituirse por vídeos autorizados o material sintético.

## Ejemplo básico resuelto

Regla generada para «mano derecha levantada»:

```js
const wrist = landmarks[16];
const shoulder = landmarks[12];
const raised = wrist.visibility > 0.7 && wrist.y < shoulder.y;
if (raised) dwell.start('next'); else dwell.cancel('next');
```

`y` crece hacia abajo en la imagen, por eso muñeca menor que hombro significa más alta. La visibilidad evita decidir con un punto dudoso; `dwell` exige mantener el gesto antes de avanzar.

## RA2-PB04 · Gesto corporal y gesto de mano

Desde el ejemplo web oficial, pide a Gemini que añada: mano levantada durante 800 ms para mostrar la tarea siguiente y pulgar arriba durante 800 ms para completarla. Añade indicador, espera de dos segundos y botones equivalentes.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

El prototipo solo actúa con confianza suficiente y permanencia cumplida. Tras la acción entra en espera, muestra «Tarea siguiente» o «Marcada como completada» y no repite mientras se mantiene el gesto. Incluye Iniciar/Detener cámara y botones Siguiente/Completar. La tabla de prueba usa tres distancias, dos iluminaciones y un caso sin detección.

</details>

## Rendimiento y cierre

La inferencia de vídeo puede bloquear el hilo principal; se limita la frecuencia y se documenta el uso de un worker como ampliación. El alumno señala qué puntos usa, cómo calcula el gesto y qué evita repeticiones.

Referencias: [Pose Landmarker para web](https://developers.google.com/edge/mediapipe/solutions/vision/pose_landmarker/web_js) y [Hand Landmarker para web](https://developers.google.com/edge/mediapipe/solutions/vision/hand_landmarker/web_js).

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA2_03_voz_habla.html">← RA2-03</a><a href="https://mosqueteroweb.github.io/damDI/RA2_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA2_05_realidad_aumentada.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA2-05 · Realidad aumentada</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
