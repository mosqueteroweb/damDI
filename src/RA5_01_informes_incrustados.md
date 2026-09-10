---
layout: default
title: RA5-01 · Informes incrustados y no incrustados
---

# RA5-01 · Informes incrustados y no incrustados

## Objetivo docente

Distinguir un informe integrado en la aplicación de un documento o panel externo y elegir según uso, actualización y distribución.

## Contenido para explicar

Un informe **incrustado** forma parte del flujo de la aplicación: comparte navegación y puede reaccionar a su estado. Uno **no incrustado** se abre o distribuye como recurso independiente —por ejemplo, PDF, hoja o panel— y resulta útil para archivo, impresión o destinatarios sin acceso a la aplicación.

## Ejemplo básico resuelto

| Necesidad | Modalidad | Decisión |
|---|---|---|
| Consultar pendientes mientras se gestionan tareas | Incrustada | Conserva contexto y filtros |
| Acta mensual firmable | No incrustada | Versión cerrada, fechada e imprimible |

Salida de IA que el alumno debe reconocer:

```html
<section aria-labelledby="report-title">
  <h2 id="report-title">Resumen de tareas</h2>
  <div id="report-content"></div>
</section>
<a href="informe-mensual.pdf">Descargar informe mensual</a>
```

`section` integra el resumen y el enlace ofrece la versión independiente. No son dos informes distintos si comparten pregunta, fuente y fecha de corte.

## RA5-PB01 · Dos modos, una decisión

Diseña en Stitch el resumen incrustado y la portada del informe exportado. Entrega una tabla comparando actualización, interacción, acceso, impresión y mantenimiento, y genera ambos accesos en una página.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

El panel incrustado muestra tres indicadores y enlace «Ver detalle». La versión externa incluye título, periodo, fuente y fecha de generación. La decisión explica que el panel cambia con los filtros y el PDF conserva una instantánea. Ambos tienen nombre accesible y la descarga indica formato.

</details>

## Cierre

Explica qué modalidad usarías para seguimiento diario y cuál para una reunión trimestral. Identifica dónde la salida generada incrusta y dónde enlaza.

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA5_00_guia_docente.html">← Guía RA5</a><a href="https://mosqueteroweb.github.io/damDI/RA5_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA5_02_herramientas_graficas.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA5-02 · Herramientas gráficas</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
