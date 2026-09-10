---
layout: default
title: RA8 · Guía docente
---

# RA8 · Evaluación y pruebas de aplicaciones

> **Duración propuesta: 12 horas · Ruta web · Objetivo WCAG 2.2 AA**

## Resultado de aprendizaje

Evalúa el funcionamiento de aplicaciones diseñando y ejecutando pruebas.

## Producto del RA

El alumnado somete el gestor de tareas y sus informes a una estrategia de pruebas reproducible. La IA ayuda a proponer casos y generar scripts; el alumnado identifica preparación, acción y resultado esperado, ejecuta, conserva evidencias, diagnostica fallos y comprueba la corrección. No escribe suites desde cero.

## Secuencia docente

| Sesión | Unidades | Horas | Evidencia principal |
|---:|---|---:|---|
| 1 | Estrategia de pruebas | 2 | Plan priorizado y trazable |
| 2 | Integración ascendente y descendente | 2 | Pruebas de conexión entre elementos |
| 3 | Sistema, configuración, recuperación, volumen y estrés | 2 | Límites y recuperación observados |
| 4 | Uso de recursos | 2 | Medición con presupuesto verificable |
| 5 | Seguridad, regresión y automatización | 2 | Hallazgos contrastados y suite mínima |
| 6 | Integrador y defensa | 2 | Informe completo antes/después |

Las seis unidades corresponden a los seis contenidos básicos; seguridad y herramientas comparten la quinta sesión.

## Flujo de cada clase

1. Partir de riesgo y requisito, no de la herramienta.
2. Definir precondición, datos, acción y oráculo antes de ejecutar.
3. Pedir a Gemini/AI Studio un caso o script pequeño y explicado.
4. Localizar selectores, datos, aserciones, métricas y umbrales.
5. Ejecutar y conservar salida real.
6. Provocar o aislar un fallo, corregir y repetir.
7. Documentar límites: una prueba superada reduce incertidumbre, no demuestra ausencia de defectos.

## Herramientas

- **Stitch:** estados que deben probarse y mapa visual de flujos.
- **Gemini / Google AI Studio:** generación y explicación de casos, datos y scripts delimitados.
- **Playwright:** integración y regresión de flujos web; complemento justificado por ejecución real en navegador.
- **Chrome DevTools y Lighthouse:** red, rendimiento, memoria, accesibilidad y uso de recursos.
- **k6:** volumen y estrés sobre un entorno autorizado; scripts generados y cargas pequeñas en clase.
- **OWASP ZAP Baseline:** revisión pasiva inicial de seguridad; nunca sustituye la comprobación manual.
- **Material Design 3 y WCAG 2.2 AA:** referencia de estados y calidad de interacción.

## Evaluación

Las prácticas básicas producen evidencias parciales y el integrador cubre los siete criterios. Un listado de casos no demuestra ejecución: cada evidencia incluye versión, entorno, datos, resultado esperado, resultado real, prueba conservada y conclusión.

## Preparación del profesor

- Crear una copia autorizada del gestor con defectos controlados.
- Preparar datos pequeños, grandes y corruptos sin información personal.
- Prohibir pruebas de carga o seguridad sobre servicios de terceros.
- Guardar una versión base para regresión.
- Mantener Android/Java como ampliación voluntaria.

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/">← Inicio</a><a href="https://mosqueteroweb.github.io/damDI/RA8_matriz_contenidos_evaluacion.html">Matriz RA8</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA8_01_estrategia.html"><span class="unit-next-card__eyebrow">Primera unidad</span><strong>RA8-01 · Objetivo, límites y estrategia</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
