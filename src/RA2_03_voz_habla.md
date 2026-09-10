---
layout: default
title: RA2-03 · Voz, habla y reconocimiento
---

# RA2-03 · Voz, habla y reconocimiento

## Objetivo docente

Usar reconocimiento de voz para activar acciones, haciendo visible la transcripción y ofreciendo confirmación, cancelación y alternativa escrita.

## Contenido para explicar

Reconocer voz convierte audio en texto; interpretar una orden relaciona ese texto con una intención. Son pasos distintos. La Web Speech API facilita prototipos, pero su compatibilidad y modo de procesamiento dependen del navegador. Por ello se comprueba la API, se solicita permiso al iniciar y se conserva un campo escrito equivalente.

## Ejemplo básico resuelto

Salida de IA para identificar y explicar:

```js
const Recognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = Recognition ? new Recognition() : null;
if (recognition) {
  recognition.lang = 'es-ES';
  recognition.onresult = event => {
    transcript.value = event.results[0][0].transcript;
    preview.textContent = `He entendido: ${transcript.value}`;
  };
}
```

La primera línea detecta compatibilidad; `lang` fija el idioma; `onresult` conserva la transcripción para revisarla. Todavía no ejecuta una acción destructiva.

## RA2-PB03 · Dos órdenes con confirmación

Genera un prototipo que entienda «mostrar pendientes» y «crear tarea [título]». Debe activarse por botón, mostrar escucha y transcripción, pedir confirmación antes de crear y permitir escribir exactamente las mismas órdenes.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

`mostrar pendientes` aplica el filtro y anuncia cuántos resultados hay. `crear tarea revisar examen` rellena una previsualización; solo «Confirmar» guarda. Si no existe reconocimiento se muestra «La voz no está disponible en este navegador; escribe la orden» y el flujo continúa. Se prueban frase exacta, variante mayúscula, ruido, orden desconocida y cancelación.

</details>

## Privacidad y cierre

No se inicia el micrófono al cargar ni se conserva audio. El indicador de escucha y el botón «Detener» permanecen visibles. El alumno explica dónde se recibe texto y dónde se decide la acción.

Referencia: [guía de Web Speech API de MDN](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API/Using_the_Web_Speech_API).

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA2_02_interfaces_naturales.html">← RA2-02</a><a href="https://mosqueteroweb.github.io/damDI/RA2_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA2_04_cuerpo_movimiento.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA2-04 · Partes y movimientos del cuerpo</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
