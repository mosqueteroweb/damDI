---
layout: default
title: RA7-05 · Instalación y desinstalación
---

# RA7-05 · Instalación, modo desatendido y desinstalación

## Objetivo docente

Probar el ciclo completo de alta, actualización, automatización y retirada sin dejar una instalación inconsistente.

## Contenido para explicar

Un asistente guía decisiones; el modo desatendido recibe configuración previa, no pregunta y devuelve un código fiable. En web, la cadena automatizada instala dependencias, prueba, compila y despliega. Desinstalar una PWA retira la aplicación, pero los datos del sitio pueden requerir una acción separada; la documentación debe explicarlo sin prometer borrados que no se han verificado.

## Ejemplo básico resuelto

```yaml
- run: npm ci
- run: npm test
- run: npm run build
```

La IA generó estos pasos. El alumnado identifica orden, condición de parada y salida, y detecta que aún faltan versión, artefacto y despliegue autorizado.

## RA7-PB05 · Ciclo desatendido y retirada

Completa y ejecuta una cadena no interactiva sobre un entorno limpio. Después instala la PWA, crea dos datos, actualiza y desinstala. Registra el código de salida y comprueba iconos, caché y almacenamiento antes/después.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

La cadena fija versión, usa `npm ci`, prueba antes de compilar y no contiene secretos. Una dependencia rota provoca fallo visible. Tras desinstalar, la aplicación desaparece del lanzador; DevTools confirma cachés e IndexedDB. Si quedan datos, el manual lo declara y explica su borrado voluntario.

</details>

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA7_04_personalizacion.html">← RA7-04</a><a href="https://mosqueteroweb.github.io/damDI/RA7_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA7_06_firma_canales.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA7-06 · Firma y canales</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
