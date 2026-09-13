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

El grabador visual contiene el flujo «una tarea creada aparece en el informe»: abrir el gestor, escribir «Preparar RA8», pulsar «Guardar tarea», abrir «Informes» y comprobar que el texto está visible. La IA propone los pasos; el alumnado distingue preparación, acción y comprobación, y verifica que cada control se identifica por su nombre accesible.

## RA8-PB02 · Dos direcciones de integración

Prueba el contrato `task-card → lista` de abajo arriba con una página de laboratorio y `aplicación → fuente` de arriba abajo usando un selector visual de respuestas JSON simuladas. Elige una variante con un nombre de campo incorrecto y observa dónde falla.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

La prueba ascendente crea una tarjeta, dispara `task-toggle` y comprueba el detalle recibido. La descendente simula `/data/tareas.json` y recorre la interfaz hasta el total. Cambiar `status` por `state` deja el contrato incumplido; la evidencia identifica la frontera y no atribuye el fallo al gráfico.

</details>

## Cierre

Dibuja los elementos reales y sustituidos en cada dirección y explica qué contrato verificaste.

La ejecución puede realizarse con cualquier grabador visual de pruebas de navegador que muestre pasos, resultados y evidencias.

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA8_01_estrategia.html">← RA8-01</a><a href="https://mosqueteroweb.github.io/damDI/RA8_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA8_03_sistema_volumen_estres.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA8-03 · Sistema, volumen y estrés</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
