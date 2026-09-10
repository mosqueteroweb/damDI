---
layout: default
title: RA4-INT01 · Rediseño accesible del gestor
---

# RA4-INT01 · Rediseño accesible del gestor de tareas

## Situación

El centro quiere publicar el gestor creado en RA1. Antes necesita una versión que pueda utilizarse con claridad en ordenador y móvil, mediante ratón o teclado, y que documente sus decisiones de diseño.

## Encargo

Rediseña con Stitch, Gemini y/o Google AI Studio la aplicación del RA1. No debes programarla desde cero. Debes dirigir la generación, seleccionar propuestas, localizar cambios relevantes y comprobar el resultado.

## Requisitos obligatorios

1. Identificar al menos cuatro referencias o pautas aplicables y explicar su importancia.
2. Crear navegación principal y un menú contextual o secundario.
3. Distribuir acciones por frecuencia, contexto y riesgo.
4. Entregar wireframe y mockup M3.
5. Justificar la elección de ocho controles.
6. Definir roles de color, escala tipográfica, iconos y reglas de distribución.
7. Revisar todos los mensajes de validación, confirmación y resultado.
8. Permitir completar el alta, filtrado y borrado con teclado.
9. Realizar pruebas automáticas y manuales antes y después.

## Entregables

- URL o archivo ejecutable de la versión final.
- Prompts y decisiones aceptadas o rechazadas.
- Wireframe y mockup.
- Tabla de correspondencia requisito–control.
- Fragmentos relevantes anotados de HTML, CSS y JavaScript.
- Inventario de mensajes antes/después.
- Informe de pruebas con evidencias.
- Defensa individual de cinco minutos.

## Casos de prueba mínimos

| Caso | Resultado esperado |
|---|---|
| Recorrido completo con teclado | Foco visible, orden lógico y activación posible |
| Zoom al 200 % | No se pierde contenido ni funcionalidad |
| Alta sin título | Mensaje específico, asociado y recuperable |
| Borrado accidental | Existe confirmación o deshacer |
| Cambio de ancho | Controles mantienen agrupación y lectura |
| Auditor automático | Hallazgos interpretados y contrastados manualmente |

## Guía de corrección por criterios

| CE | Satisfactorio | Insuficiente |
|---|---|---|
| a | Identifica estándares y los aplica a hallazgos | Solo enumera siglas |
| b | Explica consecuencias y prioridad | Afirma que son importantes sin evidencia |
| c | Presenta dos menús coherentes | Agrupa acciones sin criterio |
| d | Ubica acciones por uso, contexto y riesgo | Todas compiten con igual peso |
| e | Distribución comprensible y adaptable | Hay solapamientos u orden confuso |
| f | Controles apropiados y justificados | Decide solo por apariencia |
| g | Sistema visual legible y comprobado | Colores y fuentes sin verificación |
| h | Mensajes claros, concretos y accionables | Mensajes genéricos o códigos de error |
| i | Protocolo reproducible antes/después | Solo aporta una puntuación automática |

## Solución docente orientativa

<details><summary>Mostrar estructura de una solución válida</summary>

La versión válida ofrece navegación por estado, acción principal «Nueva tarea» y menú contextual por elemento. El formulario emplea controles nativos etiquetados; los errores conservan datos y se asocian al campo. Los roles M3 mantienen contraste y jerarquía. El borrado ofrece deshacer. El dossier compara resultados con teclado, zoom, contraste, herramienta automática y una prueba breve con usuarios. Los fragmentos anotados señalan semántica, estilos de estado y asociación de eventos; no se exige escribirlos de memoria.

</details>

## Preguntas de defensa

1. ¿Qué decisión de la IA rechazaste y por qué?
2. ¿Qué CE demuestra mejor tu evidencia?
3. ¿Qué problema no detectó la herramienta automática?
4. ¿Qué fragmento generado controla el foco o el mensaje?
5. ¿Qué mejorarías con más tiempo?

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA4_07_secuencia_control.html">← RA4-07</a><a href="https://mosqueteroweb.github.io/damDI/RA4_matriz_contenidos_evaluacion.html">Matriz RA4</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/"><span class="unit-next-card__eyebrow">Volver al curso</span><strong>Índice general del módulo</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
