---
layout: default
title: RA2-01 · Aprendizaje automático y entrenamiento
---

# RA2-01 · Herramientas de aprendizaje automático y entrenamiento

## Objetivo docente

Identificar herramientas visuales de aprendizaje automático y comprender datos, etiquetas, entrenamiento, inferencia, confianza y error.

## Contenido para explicar

Una herramienta visual permite aportar ejemplos etiquetados, entrenar un modelo y probarlo sin implementar el algoritmo. **Entrenar** ajusta el modelo con ejemplos; **inferir** aplica el modelo a una entrada nueva. La confianza no es certeza: una clase ganadora con poca separación puede producir una acción insegura.

Teachable Machine resulta apropiado para la primera experiencia; MediaPipe aporta modelos ya entrenados de gestos y partes del cuerpo; Gemini ayuda a describir el flujo y generar la integración. Se comparan por datos necesarios, privacidad, exportación, latencia y funcionamiento en el dispositivo.

## Ejemplo básico resuelto

Se entrenan dos clases visuales: «mesa libre» y «mesa ocupada», con igual número de imágenes y fondos variados. Regla generada por IA:

```js
const accepted = prediction.className === 'mesa libre'
  && prediction.probability >= 0.85;
status.textContent = accepted ? 'Mesa disponible' : 'No se puede confirmar';
```

Partes relevantes: se comprueba clase y umbral; el caso dudoso no ejecuta una acción; el mensaje comunica incertidumbre. El alumnado no memoriza la sintaxis: explica la condición y prueba ejemplos nuevos.

## RA2-PB01 · Entrenar y cuestionar un clasificador

Con Teachable Machine, crea dos clases de gesto con al menos 20 muestras variadas por clase. Prueba diez entradas nuevas y registra aciertos, falsos positivos y falsos negativos. Pide a Gemini una regla que solo confirme cuando la confianza sea suficiente.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

La ficha indica clases, número de muestras, variaciones de luz/fondo, umbral y limitaciones. La prueba separa datos de entrenamiento y prueba. Una solución válida no afirma «100 % fiable»: ante confianza menor del 85 % solicita repetir o usar un botón. El alumno localiza en la salida de IA la etiqueta, la probabilidad y la decisión.

</details>

## Comprobación y cierre

¿Qué grupo o situación aparece poco en los datos? ¿Qué daño causaría un falso positivo? ¿Cuándo es preferible no decidir?

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA2_00_guia_docente.html">← Guía RA2</a><a href="https://mosqueteroweb.github.io/damDI/RA2_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA2_02_interfaces_naturales.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA2-02 · Interfaces naturales y tipos</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
