---
layout: default
title: RA5-04 · Filtrado de datos
---

# RA5-04 · Filtrado de datos

## Objetivo docente

Definir filtros comprensibles, aplicarlos sobre una fuente y demostrar qué filas entran o salen del informe.

## Contenido para explicar

Un filtro reduce el conjunto según condiciones. Debe mostrar valor activo, permitir limpiar, actualizar todos los componentes y diferenciar cero resultados de un error. Los filtros combinados han de documentar si usan **Y** —se cumplen todos— u **O** —basta uno—.

## Ejemplo básico resuelto

Salida de IA para filtrar por módulo y estado:

```js
const visible = tasks.filter(task =>
  (moduleValue === 'all' || task.module === moduleValue) &&
  (statusValue === 'all' || task.status === statusValue)
);
renderReport(visible);
```

Cada condición permite `all` o exige coincidencia. `&&` aplica ambas. `renderReport` recibe una sola colección para sincronizar tabla, total y gráfico.

## RA5-PB04 · Filtros verificables

Con 12 tareas conocidas, genera filtros de módulo, estado y rango de fecha. Define cinco casos de prueba antes de pedir el código. Añade resumen textual «8 de 12 tareas» y botón «Limpiar filtros».

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

La combinación DI + pendiente devuelve las filas previstas en la tabla manual. Todos los indicadores y el gráfico usan esas mismas filas. Un rango invertido produce un mensaje claro y no cifras engañosas. Limpiar restablece 12 de 12. La entrega señala las condiciones y el punto único de renderizado.

</details>

## Cierre

Selecciona una fila excluida y explica exactamente qué condición la descartó. Comprueba el resultado sin confiar solo en la interfaz.

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA5_03_estructura_secciones.html">← RA5-03</a><a href="https://mosqueteroweb.github.io/damDI/RA5_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA5_05_recuentos_totales.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA5-05 · Numeración, recuentos y totales</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
