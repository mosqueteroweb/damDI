---
layout: default
title: RA7-02 · Instaladores y paquetes autoinstalables
---

# RA7-02 · Instaladores y paquetes autoinstalables

## Objetivo docente

Distinguir archivo, instalador y aplicación web instalable, y comprobar los requisitos de una PWA.

## Contenido para explicar

Un ZIP se extrae; un instalador guía y modifica el sistema; una PWA se instala desde el navegador y conserva una identidad propia. La ruta web usa HTTPS, manifiesto, iconos, nombre, URL inicial y comportamiento de visualización. El alumnado no debe confundir «se puede añadir a inicio» con «funciona sin conexión»: la caché es una decisión separada.

## Ejemplo básico resuelto

```json
{
  "name": "Gestor de aula",
  "short_name": "Gestor",
  "start_url": "./",
  "display": "standalone",
  "theme_color": "#5b5f00",
  "background_color": "#fffff4",
  "icons": []
}
```

La IA generó el borrador. El alumnado debe detectar que `icons` vacío impide una entrega completa, añadir tamaños adecuados y explicar `start_url`, `display` y colores.

## RA7-PB02 · Elegir e instalar

Compara brevemente PWA, instalador nativo y paquete portable. Selecciona la PWA para el gestor, completa el manifiesto generado por IA y comprueba su instalación desde un perfil limpio.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

La PWA reduce fricción y mantiene la ruta web, pero depende del navegador; el instalador nativo ofrece más integración y permisos; el portable no registra instalación. El informe confirma nombre, iconos, `start_url`, `scope`, modo `standalone` y apertura independiente. No afirma soporte offline sin probarlo.

</details>

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA7_01_componentes_empaquetado.html">← RA7-01</a><a href="https://mosqueteroweb.github.io/damDI/RA7_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA7_03_herramientas_paquetes.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA7-03 · Herramientas de creación</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
