---
layout: default
title: RA6-04 · Manuales y datos persistentes
---

# RA6-04 · Manuales y documentación de datos persistentes

## Objetivo docente

Adaptar manuales a usuario, consulta, instalación, configuración y administración, y documentar la estructura persistente.

## Contenido para explicar

Cada manual responde a un destinatario: usuario realiza tareas; referencia consulta campos y acciones; instalación prepara; configuración adapta; administración mantiene y recupera. La documentación persistente describe claves, campos, tipos, obligatoriedad, valores, relaciones, versión, migración y conservación.

## RA6-EJ04 · Ejemplo resuelto

| Campo | Tipo | Obligatorio | Regla |
|---|---|---:|---|
| `id` | texto | sí | único |
| `title` | texto | sí | 1–120 caracteres |
| `status` | enumerado | sí | `pending` o `done` |
| `dueDate` | fecha ISO | no | `AAAA-MM-DD` |

La guía de usuario dice «Título»; la referencia incluye `title`; administración explica copia, versión de clave y recuperación.

## RA6-PB04 · Paquete por destinatarios

Documenta alta y borrado en el manual de usuario; crea referencia de campos; escribe instalación local, dos opciones de configuración y copia/restauración administrativa. Añade FAQ con tres preguntas reales.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

El manual de usuario emplea nombres visibles y resultados. La referencia enumera API y datos. Instalación indica requisitos y verificación; configuración explica fuente y tema; administración incluye copia antes de restaurar y criterio de éxito. El diccionario coincide con JSON real y marca datos opcionales.

</details>

## Cierre

Selecciona un párrafo que cambiaría según el destinatario y explica por qué.

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA6_03_navegacion_contexto.html">← RA6-03</a><a href="https://mosqueteroweb.github.io/damDI/RA6_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA6_05_tutoriales.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA6-05 · Elaboración de tutoriales</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
