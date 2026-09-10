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

## RA7-PB06 · Instalación desatendida

Completa y ejecuta una cadena no interactiva sobre un entorno limpio. Debe terminar con éxito sin preguntas o detenerse con error no nulo, conservar registro y producir el artefacto esperado.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

La cadena fija versión de ejecución, usa `npm ci`, prueba antes de compilar, nombra el artefacto con versión y no contiene secretos. Una dependencia rota provoca fallo visible; no se publica una salida parcial.

</details>

## RA7-PB07 · Desinstalación y limpieza verificadas

Instala la PWA, crea dos datos, actualiza y desinstala. Comprueba iconos, ventanas, caché y almacenamiento antes/después. Documenta qué se conserva y ofrece borrado voluntario separado.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

La aplicación desaparece del lanzador y deja de abrirse como ventana independiente. DevTools confirma el estado de service worker, cachés e IndexedDB. Si el navegador conserva datos, el manual lo dice y explica cómo eliminarlos; la evidencia no confunde desinstalación con borrado total.

</details>

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA7_04_personalizacion.html">← RA7-04</a><a href="https://mosqueteroweb.github.io/damDI/RA7_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA7_06_firma_canales.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA7-06 · Firma y canales</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
