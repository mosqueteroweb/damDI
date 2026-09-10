---
layout: default
title: RA2-05 · Realidad aumentada
---

# RA2-05 · Realidad aumentada

## Objetivo docente

Integrar un objeto digital en el entorno real, conservar una alternativa 3D y explicar activación, compatibilidad, escala y utilidad contextual.

## Contenido para explicar

La realidad aumentada combina la escena real con contenido digital situado en el espacio. Para una primera ruta web, `<model-viewer>` muestra un modelo 3D y ofrece un botón de RA cuando el dispositivo dispone de un modo compatible. El mismo contenido debe seguir siendo consultable en 3D si la RA no está disponible.

Una integración útil relaciona objeto, tarea y contexto; no añade RA como adorno. Se comprueban tamaño, orientación, iluminación, espacio seguro y salida clara.

## Ejemplo básico resuelto

Código solicitado a IA a partir del ejemplo oficial:

```html
<model-viewer src="models/router.glb" alt="Router con sus conexiones señaladas"
  ar ar-modes="webxr scene-viewer quick-look" camera-controls
  poster="images/router-poster.webp">
  <button slot="ar-button">Ver el router en mi espacio</button>
</model-viewer>
```

`src` aporta el modelo; `alt` describe su propósito; `ar` habilita la opción; `ar-modes` enumera rutas compatibles; `camera-controls` conserva exploración 3D; el botón comunica la acción.

## RA2-PB05 · Ayuda contextual en RA

Elige una tarea de montaje o identificación, prepara en Stitch la ficha M3 y solicita a Gemini la integración de un modelo con tres puntos informativos. Debe incluir instrucciones previas, botón de salida y alternativa 3D con la misma información.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

La ficha «Conectar el router» muestra modelo, propósito, requisitos y acción «Ver en mi espacio». Tres puntos explican alimentación, WAN y LAN. En un dispositivo compatible se abre RA; en escritorio se rota y amplía el mismo modelo. Si falta el recurso aparece una ilustración y una lista textual. La prueba comprueba escala aproximada, lectura, orientación, cancelación y alternativa.

</details>

## Comprobación y cierre

Justifica qué información mejora al verla situada y qué riesgo aparece al caminar mirando la pantalla. No se obliga a instalar una aplicación ni a publicar imágenes del entorno.

Referencia: [ejemplos de realidad aumentada de `<model-viewer>`](https://modelviewer.dev/examples/augmentedreality/).

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA2_04_cuerpo_movimiento.html">← RA2-04</a><a href="https://mosqueteroweb.github.io/damDI/RA2_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA2_integrador.html"><span class="unit-next-card__eyebrow">Ejercicio integrador</span><strong>RA2-INT01 · Asistente natural del aula</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
