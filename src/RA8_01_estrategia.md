---
layout: default
title: RA8-01 · Objetivo, límites y estrategia
---

# RA8-01 · Objetivo, importancia, limitaciones y estrategia

## Objetivo docente

Establecer una estrategia de pruebas basada en riesgos, requisitos, niveles, datos, entorno y criterios de salida.

## Contenido para explicar

Probar busca información sobre calidad; no demuestra que no existan errores. La estrategia indica qué se prueba, por qué, dónde, con qué datos, quién lo ejecuta y cuándo basta. Se prioriza probabilidad × impacto y se enlaza cada requisito con al menos una prueba.

## Ejemplo básico resuelto

| Riesgo | Prob. | Impacto | Prioridad | Prueba |
|---|---:|---:|---:|---|
| Borrar la tarea equivocada | 2 | 3 | 6 | Cancelar y deshacer borrado |
| Filtro sin resultados | 2 | 2 | 4 | Estado vacío y limpieza |
| Título demasiado largo | 3 | 1 | 3 | Límite y adaptación visual |

Prompt: «Genera casos para estos riesgos con precondición, datos, pasos y resultado; no inventes requisitos y marca dudas». El alumnado revisa el oráculo antes de ejecutar.

## RA8-PB01 · Estrategia mínima trazable

Selecciona cinco riesgos del gestor, priorízalos y crea una matriz requisito–riesgo–prueba. Incluye alcance, exclusiones, entornos, datos, criterio de entrada y criterio de salida.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

La estrategia cubre alta, filtrado, borrado, persistencia y accesibilidad. Excluye servicios externos. Entra cuando la versión está desplegada y los datos son conocidos; sale cuando pasan los casos críticos y no quedan defectos de severidad alta. Cada prueba identifica resultado esperado y evidencia, no solo pasos.

</details>

## Cierre

Defiende qué no probarás y qué riesgo conserva esa decisión.

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA8_00_guia_docente.html">← Guía RA8</a><a href="https://mosqueteroweb.github.io/damDI/RA8_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA8_02_integracion.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA8-02 · Pruebas de integración</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
