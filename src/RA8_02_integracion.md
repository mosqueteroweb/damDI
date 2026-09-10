---
layout: default
title: RA8-02 · Pruebas de integración
---

# RA8-02 · Integración ascendente y descendente

## Objetivo docente

Comprobar contratos entre componentes, almacenamiento, informes y aplicación mediante integración ascendente y descendente.

## Contenido para explicar

La integración **ascendente** empieza por piezas inferiores y sustituye temporalmente consumidores con drivers. La **descendente** empieza por el flujo superior y sustituye dependencias inferiores con stubs. Ambas aíslan fronteras: evento, parámetro, formato de datos o respuesta.

## Ejemplo básico resuelto

```js
test('una tarea creada aparece en el informe', async ({ page }) => {
  await page.goto('/tareas.html');
  await page.getByLabel('Título').fill('Preparar RA8');
  await page.getByRole('button', { name: 'Guardar tarea' }).click();
  await page.getByRole('link', { name: 'Informes' }).click();
  await expect(page.getByText('Preparar RA8')).toBeVisible();
});
```

La IA ha generado un flujo entre formulario, persistencia e informe. El alumnado reconoce preparación, acción y aserción; los selectores se apoyan en nombres accesibles.

## RA8-PB02 · Dos direcciones de integración

Prueba el contrato `task-card → lista` de abajo arriba con un contenedor de prueba y `aplicación → fuente` de arriba abajo interceptando una respuesta JSON. Provoca un nombre de campo incorrecto y observa dónde falla.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

La prueba ascendente crea una tarjeta, dispara `task-toggle` y comprueba el detalle recibido. La descendente simula `/data/tareas.json` y recorre la interfaz hasta el total. Cambiar `status` por `state` deja el contrato incumplido; la evidencia identifica la frontera y no atribuye el fallo al gráfico.

</details>

## Cierre

Dibuja los elementos reales y sustituidos en cada dirección y explica qué contrato verificaste.

Referencia: [pruebas de navegador con Playwright](https://playwright.dev/docs/writing-tests).

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA8_01_estrategia.html">← RA8-01</a><a href="https://mosqueteroweb.github.io/damDI/RA8_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA8_03_sistema_volumen_estres.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA8-03 · Sistema, volumen y estrés</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
