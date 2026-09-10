---
layout: default
title: RA5-08 · Fuentes de datos y consultas
---

# RA5-08 · Conexión con fuentes y ejecución de consultas

## Objetivo docente

Conectar un informe a JSON, CSV u hoja tabular, validar el esquema y ejecutar una consulta reproducible antes de representar resultados.

## Contenido para explicar

La fuente aporta registros; la consulta selecciona, filtra, agrupa u ordena; la transformación adapta tipos; la vista presenta. Separar estas fases permite cambiar el gráfico sin alterar la pregunta. Deben documentarse origen, campos, tipos, actualización y tratamiento de errores.

## Ejemplo básico resuelto

```js
async function loadTasks() {
  const response = await fetch('./data/tareas.json');
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  const rows = await response.json();
  return rows.filter(row => row.module && row.status);
}
```

`fetch` conecta; `ok` valida la respuesta; `json` interpreta; `filter` aplica una consulta mínima de calidad. Carga, error y vacío se muestran como estados distintos.

## RA5-PB08 · Dos fuentes, un resultado

Genera el mismo recuento por estado desde `tareas.json` y una hoja exportada a CSV. Crea un diccionario de campos y verifica que ambas fuentes producen el mismo resultado conocido.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

El adaptador JSON y el adaptador CSV devuelven objetos con `{id, title, module, status, hours, dueDate}`. La consulta agrupa por `status` después de normalizar espacios y valores. Con 12 registros, ambos resultados coinciden. Un registro sin `status` se aparta y se comunica como incidencia, no desaparece silenciosamente.

</details>

## Cierre

Dibuja la ruta fuente → validación → consulta → cálculo → vista y explica qué etapa cambiarías para conectar otra hoja.

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA5_07_librerias_codigo.html">← RA5-07</a><a href="https://mosqueteroweb.github.io/damDI/RA5_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA5_integrador.html"><span class="unit-next-card__eyebrow">Ejercicio integrador</span><strong>RA5-INT01 · Informe de seguimiento del aula</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
