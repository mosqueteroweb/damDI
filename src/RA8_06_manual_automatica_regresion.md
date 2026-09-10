---
layout: default
title: RA8-06 · Pruebas manuales, automáticas y regresión
---

# RA8-06 · Pruebas manuales, automáticas y de regresión

## Objetivo docente

Elegir qué automatizar, construir una suite mínima de regresión y documentar resultados repetibles.

## Contenido para explicar

La prueba manual favorece exploración, percepción y casos nuevos; la automática repite comprobaciones estables con rapidez. La regresión protege comportamientos que funcionaban antes de un cambio. Una suite pequeña debe ser determinista, aislar datos y producir mensajes útiles.

## Ejemplo básico resuelto

```js
test.beforeEach(async ({ page }) => {
  await page.goto('/tareas.html');
  await page.evaluate(() => localStorage.clear());
});

test('conserva el título al fallar la validación', async ({ page }) => {
  await page.getByLabel('Título').fill('Revisar informe');
  await page.getByRole('button', { name: 'Guardar tarea' }).click();
  await expect(page.getByDisplayValue('Revisar informe')).toBeVisible();
});
```

`beforeEach` aísla el estado; el nombre describe comportamiento; la aserción protege una regresión concreta.

## RA8-PB06 · Del defecto a la regresión

Elige un defecto corregido, escribe primero caso manual, pide a Gemini su versión Playwright, identifica selectores y aserción, ejecútala antes/después y añade la prueba a una suite de cinco flujos críticos.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

La suite cubre alta, validación, filtro, borrado recuperable e informe. Usa datos reiniciados y selectores accesibles. La prueba del defecto falla en la versión base y pasa tras la corrección. El informe registra comando, navegador, versión, 5/5 pruebas y duración; una revisión manual de foco y claridad complementa la suite.

</details>

## Cierre

Justifica qué caso mantienes manual y qué señal te haría retirar o reparar una prueba automática inestable.

Referencia: [generación de informes de Playwright](https://playwright.dev/docs/test-reporters).

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA8_05_seguridad.html">← RA8-05</a><a href="https://mosqueteroweb.github.io/damDI/RA8_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA8_integrador.html"><span class="unit-next-card__eyebrow">Ejercicio integrador</span><strong>RA8-INT01 · Certificación interna del gestor</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
