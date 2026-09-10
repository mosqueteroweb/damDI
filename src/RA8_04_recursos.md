---
layout: default
title: RA8-04 · Uso de recursos
---

# RA8-04 · Pruebas de uso de recursos

## Objetivo docente

Medir carga, transferencia, CPU y memoria con un escenario repetible y un presupuesto explícito.

## Contenido para explicar

Una medición necesita dispositivo, navegador, red, versión, datos y recorrido. DevTools muestra peticiones, tiempo y memoria; Lighthouse aporta una auditoría reproducible, pero su puntuación no sustituye las métricas ni la interpretación. Se comparan varias ejecuciones y se informa variabilidad.

## Ejemplo básico resuelto

| Presupuesto | Umbral |
|---|---:|
| JavaScript transferido | ≤ 250 KB comprimidos |
| Peticiones iniciales | ≤ 20 |
| Memoria tras 20 aperturas/cierres | vuelve cerca de la línea base |
| Respuesta al filtrar 1.000 filas | ≤ 200 ms en equipo de aula |

La IA puede proponer un script, pero el alumno debe medir en el mismo escenario antes y después.

## RA8-PB04 · Presupuesto y fuga aparente

Define cuatro límites, registra tres ejecuciones, abre y cierra 20 veces un diálogo y compara memoria. Optimiza un recurso o escuchador, repite y documenta el efecto.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

La captura de red identifica imagen sin comprimir; la corrección reduce transferencia sin alterar legibilidad. El perfil de memoria crece porque cada apertura añade otro escuchador; mover el registro fuera de la función de apertura estabiliza el valor. El informe conserva mediana, rango y entorno, no solo una puntuación.

</details>

## Cierre

Relaciona cada recurso con impacto observable y evita afirmar «hay fuga» a partir de una única lectura.

Referencia: [documentación de Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/).

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA8_03_sistema_volumen_estres.html">← RA8-03</a><a href="https://mosqueteroweb.github.io/damDI/RA8_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA8_05_seguridad.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA8-05 · Pruebas de seguridad</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
