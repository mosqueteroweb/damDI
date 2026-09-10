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

Script k6 generado para una copia local:

```js
export const options = { stages: [{ duration: '20s', target: 5 }, { duration: '10s', target: 0 }] };
export default function () { http.get('http://localhost:8000/'); sleep(1); }
```

`stages` sube y baja la carga; `target` es concurrencia; la URL nunca apunta a un tercero.

## RA8-PB03 · Escalón, fallo y recuperación

Carga 10, 100 y 1.000 tareas, simula fallo de fuente y ejecuta una carga pequeña contra el servidor local. Registra tiempo, errores, comportamiento visible y recuperación.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

La tabla separa tamaño de datos y usuarios concurrentes. Con JSON corrupto aparece error recuperable; tras restaurarlo, Reintentar carga sin recargar toda la página. La prueba k6 se limita al entorno local, define presupuesto y confirma que vuelve a cero usuarios. Si 1.000 filas degradan la vista, se propone paginación y se repite.

</details>

## Cierre

Indica el primer límite observado y demuestra que la aplicación se recupera cuando cesa la condición.

Referencia: [documentación oficial de k6](https://grafana.com/docs/k6/latest/).

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA8_02_integracion.html">← RA8-02</a><a href="https://mosqueteroweb.github.io/damDI/RA8_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA8_04_recursos.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA8-04 · Uso de recursos</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
