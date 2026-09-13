---
layout: default
title: RA8-03 · Sistema, volumen y estrés
---

# RA8-03 · Sistema, configuración, recuperación, volumen y estrés

## Objetivo docente

Evaluar la aplicación completa bajo configuraciones, fallos, conjuntos grandes y carga creciente, siempre en un entorno autorizado.

## Contenido para explicar

Las pruebas de sistema observan comportamiento completo. **Configuración** cambia navegador, ancho o almacenamiento; **recuperación** introduce fallos y comprueba retorno seguro; **volumen** aumenta datos; **estrés** aumenta carga hasta superar el objetivo para conocer degradación y recuperación.

## Ejemplo básico resuelto

| Prueba | Entrada | Oráculo |
|---|---|---|
| Volumen | 10, 100, 1.000 tareas | búsqueda usable y total correcto |
| Recuperación | JSON corrupto | mensaje, datos seguros y reintento |
| Estrés | 1→10 usuarios virtuales | sin errores y p95 bajo presupuesto |

En un panel visual de carga, el escenario autorizado se configura con dos etapas: 20 segundos hasta 5 usuarios simulados y 10 segundos de descenso hasta 0. El alumnado identifica duración, concurrencia, URL autorizada y umbral antes de pulsar **Ejecutar**. La herramienta muestra gráficas, errores y recuperación sin recurrir a comandos.

## RA8-PB03 · Escalón, fallo y recuperación

Carga 10, 100 y 1.000 tareas mediante controles de la aplicación, simula un fallo seleccionando una fuente de prueba corrupta y ejecuta una carga pequeña desde el panel visual contra la copia autorizada. Registra tiempo, errores, comportamiento visible y recuperación.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

La tabla separa tamaño de datos y usuarios concurrentes. Con JSON corrupto aparece error recuperable; tras restaurarlo, **Reintentar** carga sin recargar toda la página. El escenario visual se limita a la copia autorizada, define presupuesto y confirma que vuelve a cero usuarios. Si 1.000 filas degradan la vista, se propone paginación y se repite.

</details>

## Cierre

Indica el primer límite observado y demuestra que la aplicación se recupera cuando cesa la condición.

La herramienta elegida debe permitir fijar límites de carga y detener la prueba desde la propia interfaz.

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA8_02_integracion.html">← RA8-02</a><a href="https://mosqueteroweb.github.io/damDI/RA8_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA8_04_recursos.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA8-04 · Uso de recursos</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
