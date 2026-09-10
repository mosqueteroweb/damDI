---
layout: default
title: RA2 · Guía docente
---

# RA2 · Interfaces naturales de usuario

> **Duración propuesta: 12 horas · Ruta web · Material Design 3 como referencia visual**

## Resultado de aprendizaje

Genera interfaces naturales de usuario utilizando herramientas visuales.

## Producto del RA

El alumnado añade al gestor de tareas una capa de interacción por voz, gesto corporal y realidad aumentada. No programa desde cero: parte de ejemplos oficiales y salidas de IA, identifica entrada, interpretación, acción y respuesta, modifica decisiones acotadas y demuestra el resultado con pruebas.

## Principio didáctico

Una interfaz natural aprovecha capacidades habituales —hablar, mirar, señalar o moverse—, pero no es automáticamente intuitiva ni accesible. Toda interacción por cámara o micrófono tendrá consentimiento previo, estado visible, parada clara y alternativa mediante controles convencionales.

## Secuencia docente

| Sesión | Unidad | Horas | Evidencia principal |
|---:|---|---:|---|
| 1 | Aprendizaje automático y entrenamiento | 2 | Modelo visual probado y ficha de datos |
| 2 | Interfaces naturales y tipos | 2 | Mapa entrada–intención–respuesta |
| 3 | Voz y habla | 2 | Dos acciones por voz con alternativa escrita |
| 4 | Partes y movimientos del cuerpo | 2 | Dos gestos estables y comprobables |
| 5 | Realidad aumentada | 2 | Objeto contextual colocado y alternativa 3D |
| 6 | Integrador y defensa | 2 | Asistente multimodal verificado |

## Flujo de cada clase

1. Presentar la tarea y el contexto de uso.
2. Probar un ejemplo ya generado u oficial.
3. Identificar sensor, datos, interpretación, umbral, acción y respuesta.
4. Formular un prompt de modificación con límites de privacidad y accesibilidad.
5. Ejecutar la práctica básica y contrastarla con la solución.
6. Registrar falsos positivos, falsos negativos y alternativa disponible.
7. Cerrar explicando qué fragmento generado controla la decisión.

## Herramientas

- **Stitch:** diseño de estados de escucha, detección, permiso, error y alternativa manual.
- **Gemini / Google AI Studio:** generación y explicación de prototipos web, reglas de decisión y casos de prueba.
- **Teachable Machine:** entrenamiento visual introductorio sin partir de código.
- **Web Speech API:** reconocimiento de voz en navegadores compatibles.
- **MediaPipe Tasks Vision:** detección de manos y postura; complemento justificado por sus modelos y ejemplos web.
- **`<model-viewer>`:** visualización 3D y lanzamiento de RA compatible, con modo 3D de respaldo.
- **Material Design 3:** estados, permisos, controles y respuesta visual coherente.

## Evaluación

Las cinco prácticas generan evidencias parciales y el integrador cubre los seis criterios. Se evalúan decisiones, funcionamiento, límites conocidos y explicación del código generado. No se penaliza que un dispositivo carezca de una API si el alumno aporta simulación reproducible y alternativa funcional.

## Preparación del profesor

- Comprobar HTTPS, permisos y compatibilidad de cámara/micrófono.
- Preparar vídeos o imágenes de prueba para quien no pueda usar cámara.
- Evitar que se suban grabaciones o imágenes personales innecesarias.
- Facilitar un prototipo inicial y fragmentos oficiales para modificar.
- Recordar que Android Studio, XML y Java son solo ampliación voluntaria.

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/">← Inicio</a><a href="https://mosqueteroweb.github.io/damDI/RA2_matriz_contenidos_evaluacion.html">Matriz RA2</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA2_01_aprendizaje_automatico.html"><span class="unit-next-card__eyebrow">Primera unidad</span><strong>RA2-01 · Aprendizaje automático y entrenamiento</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
