---
layout: default
title: RA7-01 · Componentes y empaquetado
---

# RA7-01 · Componentes de una aplicación y empaquetado

## Objetivo docente

Reconocer qué necesita la aplicación en ejecución y construir un paquete mínimo, versionado y sin residuos.

## Contenido para explicar

Un paquete distribuye código compilado, recursos, manifiesto, licencia e instrucciones; excluye fuentes innecesarias, pruebas, cachés, secretos y datos personales. La versión del paquete, del código y de la documentación debe coincidir. `package-lock.json` fija el árbol de dependencias y `npm ci` instala desde él sin reescribirlo.

## Ejemplo básico resuelto

Gemini propone este inventario, que el alumnado contrasta con la salida real:

| Elemento | Se entrega | Razón |
|---|:---:|---|
| `dist/` | ✓ | Aplicación compilada |
| `manifest.webmanifest` | ✓ | Metadatos de instalación |
| `.env` | No | Puede contener secretos |
| `node_modules/` | No | Se reconstruye desde el bloqueo |
| `README-instalacion.md` | ✓ | Requisitos y verificación |

## RA7-PB01 · Paquete mínimo auditable

Obtén con IA un script que limpie, compile y comprima `dist/`. Identifica sus entradas, salida y código de error. Crea `gestor-1.0.0.zip`, lista su contenido y justifica cada exclusión.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

La evidencia contiene commit, versión, `npm ci`, `npm run build`, listado del ZIP y ausencia de `.env`, fuentes y dependencias de desarrollo. El alumnado señala dónde se detiene el script ante un fallo y comprueba que `index.html`, recursos, manifiesto y licencia están presentes.

</details>

## Cierre

Explica por qué «funciona en mi carpeta» no demuestra que el paquete sea distribuible.

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA7_00_guia_docente.html">← Guía RA7</a><a href="https://mosqueteroweb.github.io/damDI/RA7_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA7_02_instaladores_autoinstalables.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA7-02 · Instaladores y paquetes autoinstalables</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
