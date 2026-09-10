---
layout: default
title: RA5-05 · Numeración, recuentos y totales
---

# RA5-05 · Numeración, recuentos y totales

## Objetivo docente

Incluir números de línea, recuentos, sumas y valores calculados, indicando conjunto, fórmula y unidad.

## Contenido para explicar

Numerar filas facilita referencia, pero no crea un identificador estable. **Recuento** cuenta elementos; **total** agrega una magnitud; **valor calculado** deriva información, como porcentaje completado. El denominador debe ser el conjunto filtrado y el caso cero necesita una regla explícita.

## Ejemplo básico resuelto

```js
const total = rows.length;
const completed = rows.filter(row => row.status === 'done').length;
const completionRate = total === 0 ? 0 : completed / total * 100;
const estimatedHours = rows.reduce((sum, row) => sum + (row.hours ?? 0), 0);
```

`length` cuenta; `filter` obtiene completadas; el condicional evita división entre cero; `reduce` suma horas y trata un nulo como cero. La interfaz mostrará `63 %`, pero conservará el valor sin redondear para cálculos.

## RA5-PB05 · Cuatro indicadores comprobados

Genera fila numerada y tarjetas para total, completadas, porcentaje y horas estimadas. Calcula manualmente el resultado de un conjunto de ocho filas y repite después de filtrar.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

Con 8 tareas, 5 completadas y horas `[2,1,3,2,0,1,2,1]`, el informe muestra total 8, completadas 5, 62,5 % y 12 h. Tras filtrar, todos se recalculan sobre las filas visibles. La numeración comienza en 1, pero cada fila mantiene un ID distinto. La metodología declara que una hora nula cuenta como 0 y advierte esa decisión.

</details>

## Cierre

Explica numerador, denominador, redondeo y tratamiento de nulos. Un número correcto sin fórmula no constituye evidencia suficiente.

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA5_04_filtrado_datos.html">← RA5-04</a><a href="https://mosqueteroweb.github.io/damDI/RA5_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA5_06_graficos.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA5-06 · Gráficos</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
