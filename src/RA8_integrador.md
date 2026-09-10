---
layout: default
title: RA8-INT01 · Certificación interna del gestor
---

# RA8-INT01 · Certificación interna del gestor

## Situación

Antes de distribuir el gestor, el centro necesita una decisión razonada sobre su preparación. No busca «cero fallos», sino riesgos conocidos, resultados reproducibles y límites explícitos.

## Encargo

Diseña y ejecuta con Stitch, Gemini/AI Studio y herramientas de prueba una estrategia completa sobre una versión identificada. Parte de plantillas y scripts generados; comprende, adapta y verifica cada prueba.

## Requisitos obligatorios

1. Estrategia con alcance, riesgos, entornos, datos, responsabilidades y criterios de salida.
2. Integración ascendente y descendente sobre dos fronteras distintas.
3. Suite de regresión automática con cinco flujos críticos y revisión manual complementaria.
4. Pruebas de volumen y estrés local con carga progresiva, límite y recuperación.
5. Cinco comprobaciones de seguridad y contraste manual de dos avisos de herramienta.
6. Presupuesto de recursos con al menos cuatro métricas y tres ejecuciones.
7. Informe que vincule requisito, caso, resultado, evidencia, defecto, corrección y repetición.

## Entregables

- Plan y matriz de trazabilidad.
- Versión/commit y descripción del entorno.
- Datos de prueba ficticios y procedimiento de reinicio.
- Casos manuales y scripts generados anotados.
- Salidas de Playwright, Lighthouse, k6 y ZAP sobre entorno autorizado.
- Registro de defectos antes/después.
- Conclusión: apto, apto con condiciones o no apto.
- Defensa individual de cinco minutos.

## Casos mínimos

| Familia | Evidencia |
|---|---|
| Integración | Contratos componente–lista y aplicación–fuente |
| Regresión | Cinco flujos, incluido un defecto corregido |
| Volumen/estrés | Escalones, presupuesto y recuperación |
| Seguridad | Entrada/salida, secretos, almacenamiento, dependencia, cabecera |
| Recursos | Transferencia, peticiones, respuesta y memoria |
| Sistema | Configuración, fuente caída y datos corruptos |

## Guía de corrección por criterios

| CE | Satisfactorio | Insuficiente |
|---|---|---|
| a | Estrategia priorizada, acotada y trazable | Lista de herramientas sin estrategia |
| b | Dos integraciones con frontera y sustitutos claros | Solo prueba piezas aisladas |
| c | Suite reproduce un defecto antes/después | Automatiza sin demostrar regresión |
| d | Volumen y estrés miden degradación y recuperación | Carga sin umbral o sobre terceros |
| e | Hallazgos de seguridad reproducidos y contrastados | Copia avisos automáticos |
| f | Métricas repetidas contra presupuesto | Solo presenta puntuación global |
| g | Informe permite repetir y decidir | Capturas sin entorno ni conclusión |

## Solución docente orientativa

<details><summary>Mostrar estructura de una solución válida</summary>

La estrategia prioriza pérdida de datos, borrado y discrepancias del informe. Playwright prueba integración y cinco regresiones sobre estado reiniciado. El volumen crece hasta 1.000 tareas y la carga k6 permanece local; se documenta el primer límite y la recuperación. Lighthouse y DevTools comparan tres ejecuciones. ZAP se usa pasivamente y los avisos se verifican. Cada defecto tiene pasos, esperado/real, severidad, corrección y repetición. La conclusión «apto con condiciones» enumera riesgos residuales y fecha de revisión.

</details>

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA8_06_manual_automatica_regresion.html">← RA8-06</a><a href="https://mosqueteroweb.github.io/damDI/RA8_matriz_contenidos_evaluacion.html">Matriz RA8</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/"><span class="unit-next-card__eyebrow">Volver al curso</span><strong>Índice general del módulo</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
