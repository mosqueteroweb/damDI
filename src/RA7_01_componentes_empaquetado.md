---
layout: default
title: RA7-01 · Componentes y empaquetado
---

# RA7-01 · Componentes de una aplicación y empaquetado

## Objetivo docente

Reconocer qué necesita la aplicación en ejecución y construir un paquete mínimo, versionado y sin residuos.

## Contenido para explicar

Una entrega web distribuye páginas, recursos, manifiesto, iconos, licencia e instrucciones; excluye borradores, cachés, secretos y datos personales. La versión publicada, la documentación y el manifiesto deben coincidir. La plataforma de creación conserva las dependencias y produce una salida identificable sin que el alumnado tenga que instalarlas mediante comandos.

## Ejemplo básico resuelto

Gemini propone este inventario, que el alumnado contrasta con la salida real:

| Elemento | Se entrega | Razón |
|---|:---:|---|
| Sitio publicado | ✓ | Aplicación web ejecutable |
| `manifest.webmanifest` | ✓ | Metadatos de instalación |
| `.env` | No | Puede contener secretos |
| Dependencias internas del editor | No | Las gestiona la plataforma |
| `README-instalacion.md` | ✓ | Requisitos y verificación |

## RA7-PB01 · Paquete mínimo auditable

Pide a la IA una lista de comprobación para preparar la versión `gestor-1.0.0`. Usa **Exportar** o **Publicar** desde el editor web, identifica la entrada, la salida y los estados de error, y justifica cada elemento incluido o excluido.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

La evidencia contiene versión, revisión publicada, inventario de la salida y ausencia de secretos, borradores y datos personales. El alumnado muestra cómo la interfaz detiene la publicación ante un fallo y comprueba que la página inicial, los recursos, el manifiesto, los iconos y la licencia están presentes.

</details>

## Cierre

Explica por qué «funciona en mi carpeta» no demuestra que el paquete sea distribuible.

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA7_00_guia_docente.html">← Guía RA7</a><a href="https://mosqueteroweb.github.io/damDI/RA7_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA7_02_instaladores_autoinstalables.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA7-02 · Instaladores y paquetes autoinstalables</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
