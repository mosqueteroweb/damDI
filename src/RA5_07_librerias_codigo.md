---
layout: default
title: RA5-07 · Librerías y código generado
---

# RA5-07 · Librerías, clases, métodos y atributos

## Objetivo docente

Reconocer en el código generado cómo se carga, configura y ejecuta una librería de informes, y modificar un requisito localizado.

## Contenido para explicar

Una librería ofrece clases u objetos, métodos y opciones. En Google Charts, el alumnado localiza carga de paquetes, construcción de datos, clase de gráfico, método `draw` y objeto de opciones. No necesita reproducirlos de memoria: debe relacionar cada parte con el resultado visible y consultar la documentación.

## Ejemplo básico resuelto

```js
google.charts.load('current', { packages: ['corechart'] });
google.charts.setOnLoadCallback(drawReport);
function drawReport() {
  const chart = new google.visualization.ColumnChart(chartNode);
  chart.draw(data, { title: 'Tareas terminadas por semana' });
}
```

`load` solicita la biblioteca; el callback espera; `ColumnChart` elige la clase; `draw` ejecuta; el objeto final contiene atributos de configuración.

## RA5-PB07 · Modificación explicada

Entrega a Gemini una salida que usa columnas y pide convertirla en barras horizontales, conservar datos y añadir título de eje. Presenta diff, prueba antes/después y explicación de cinco líneas relevantes.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

La modificación cambia `ColumnChart` por `BarChart` y añade `hAxis: {title: 'Número de tareas', minValue: 0}` sin tocar la consulta. El alumno rechaza una propuesta que cambia simultáneamente colores, datos y estructura porque impide atribuir el resultado. La prueba confirma iguales categorías y valores.

</details>

## Cierre

Señala qué parte procede de la librería, cuál pertenece a la aplicación y qué cambio mínimo satisface el requisito.

Referencia: [uso de Google Charts](https://developers.google.com/chart/interactive/docs).

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA5_06_graficos.html">← RA5-06</a><a href="https://mosqueteroweb.github.io/damDI/RA5_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA5_08_fuentes_consultas.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA5-08 · Fuentes de datos y consultas</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
