---
layout: default
title: RA2-INT01 · Asistente natural del aula
---

# RA2-INT01 · Asistente natural del aula

## Situación

El gestor de tareas debe poder utilizarse durante una práctica cuando la persona está lejos del teclado o tiene las manos ocupadas. El centro también quiere una ayuda en RA para reconocer o montar un elemento del aula.

## Encargo

Con Stitch, Gemini y Google AI Studio, añade una interfaz multimodal al gestor. Parte de ejemplos y código generado: no escribas la solución desde cero. Debes comprender y explicar entrada, interpretación, acción, respuesta, privacidad y alternativa.

## Requisitos obligatorios

1. Comparar herramientas de aprendizaje automático relacionadas con la interfaz y justificar las elegidas.
2. Diseñar en Stitch todos los estados de una interfaz natural: reposo, permiso, activa, interpretación, confirmación y error.
3. Implementar por voz «mostrar pendientes» y «crear tarea [título]».
4. Implementar un movimiento corporal y un gesto de mano con confianza, permanencia y espera.
5. Integrar una ayuda contextual en RA con modelo 3D alternativo.
6. Mantener botones o entrada escrita equivalentes para todas las acciones.
7. Mostrar cuándo cámara o micrófono están activos y permitir detenerlos.
8. Probar entradas correctas, ambiguas, no detectadas y no compatibles.

## Entregables

- URL o archivos ejecutables del prototipo.
- Flujo visual de Stitch y tabla entrada–intención–acción–respuesta.
- Comparativa de herramientas y ficha del entrenamiento o modelo.
- Prompts y cambios aceptados o rechazados.
- Fragmentos anotados de voz, puntos corporales, umbral y RA.
- Matriz de pruebas con resultados y dispositivos usados.
- Declaración de privacidad y alternativas.
- Defensa individual de cinco minutos.

## Casos de prueba mínimos

| Caso | Resultado esperado |
|---|---|
| Navegador sin voz | Ofrece orden escrita equivalente |
| Orden reconocida | Muestra transcripción antes de actuar |
| Creación por voz | Exige confirmación editable |
| Gesto breve o dudoso | No ejecuta acción |
| Gesto mantenido | Ejecuta una vez y entra en espera |
| Cámara detenida | No continúa procesando imágenes |
| Dispositivo con RA | Permite colocar y abandonar el objeto |
| Dispositivo sin RA | Conserva modelo 3D e información textual |

## Guía de corrección por criterios

| CE | Satisfactorio | Insuficiente |
|---|---|---|
| a | Identifica y compara herramientas de ML por tarea, datos y límites | Enumera herramientas sin criterio |
| b | Interfaz natural completa, comprensible y recuperable | Demo aislada sin estados ni respuesta |
| c | Dos acciones por voz verificadas y con alternativa | Solo transcribe o depende obligatoriamente de voz |
| d | Movimiento corporal estable activa una acción | Reacciona a un fotograma o no controla repetición |
| e | Detecta una parte corporal para otra acción y explica los puntos | Usa un gesto opaco sin evidencia |
| f | RA contextual funcional con alternativa 3D | Objeto 3D decorativo o inaccesible sin RA |

## Solución docente orientativa

<details><summary>Mostrar estructura de una solución válida</summary>

La aplicación inicia sensores solo al pulsar. Voz filtra o prepara una tarea pendiente de confirmación. Pose Landmarker reconoce mano levantada para avanzar y Hand Landmarker reconoce pulgar arriba para completar; ambos usan confianza, 800 ms de permanencia y dos segundos de espera. La ayuda de montaje abre RA cuando está disponible y mantiene visor 3D y texto. Cada acción dispone de botón o campo equivalente. El informe incluye errores reales y explica en qué fragmentos se configuran idioma, puntos, umbral y modos de RA.

</details>

## Preguntas de defensa

1. ¿Qué diferencia hay entre reconocer una entrada e interpretar una intención?
2. ¿Qué falso positivo sería más peligroso y cómo lo reduces?
3. ¿Qué parte de la salida de IA controla la permanencia del gesto?
4. ¿Qué ocurre si se deniega un permiso?
5. ¿Por qué la RA mejora esta tarea concreta?

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA2_05_realidad_aumentada.html">← RA2-05</a><a href="https://mosqueteroweb.github.io/damDI/RA2_matriz_contenidos_evaluacion.html">Matriz RA2</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/"><span class="unit-next-card__eyebrow">Volver al curso</span><strong>Índice general del módulo</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
