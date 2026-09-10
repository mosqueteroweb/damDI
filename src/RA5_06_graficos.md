---
layout: default
title: RA5-06 · Gráficos
---

# RA5-06 · Gráficos generados a partir de datos

## Objetivo docente

Elegir un gráfico según la pregunta, conectarlo a los datos filtrados y ofrecer título, unidades y alternativa tabular.

## Contenido para explicar

Barras comparan categorías; líneas muestran evolución temporal; dispersión relaciona dos variables; sectores solo ayudan con pocas partes de un total. El eje debe respetar la magnitud y el color no puede ser el único portador de significado. Un gráfico acompaña a los datos, no los sustituye.

## Ejemplo básico resuelto

```js
const summary = Object.entries(groupByModule(rows));
const data = google.visualization.arrayToDataTable([
  ['Módulo', 'Tareas'],
  ...summary
]);
new google.visualization.BarChart(chartNode).draw(data, {
  title: 'Tareas por módulo', legend: { position: 'none' },
  colors: ['#984061']
});
```

La primera fila define columnas; `summary` contiene categorías y recuentos; el nodo decide dónde se incrusta; las opciones nombran y personalizan. El resumen se presenta también en tabla.

## RA5-PB06 · Un gráfico que responda una pregunta

Genera dos candidatos para «¿qué módulo concentra más tareas pendientes?». Elige uno, justifica el descarte, añade etiquetas y tabla equivalente, y prueba que cambia con los filtros.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

Se eligen barras horizontales ordenadas porque comparan módulos con nombres largos. Se descarta el gráfico de sectores porque dificulta comparar valores próximos. El eje empieza en cero, cada barra muestra valor, el título especifica «pendientes» y la tabla conserva módulo/recuento. El filtro de fecha actualiza ambas salidas.

</details>

## Cierre

Una defensa válida explica pregunta, variables, tipo, escala y alternativa, además de localizar la preparación de datos y la llamada de dibujo.

Referencia: [galería oficial de Google Charts](https://developers.google.com/chart/interactive/docs/gallery).

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA5_05_recuentos_totales.html">← RA5-05</a><a href="https://mosqueteroweb.github.io/damDI/RA5_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA5_07_librerias_codigo.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA5-07 · Librerías y código generado</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
