---
layout: default
title: RA7-05 · Instalación y desinstalación
---

# RA7-05 · Instalación, automatización y desinstalación

## Objetivo docente

Probar desde el navegador el ciclo completo de instalación, actualización y retirada sin dejar una PWA inconsistente.

## Contenido para explicar

El navegador guía la instalación de una PWA y la plataforma de publicación puede actualizarla automáticamente a partir de una revisión aprobada. El proceso debe mostrar estado, resultado y recuperación mediante controles visuales. Desinstalar una PWA retira la aplicación, pero los datos del sitio pueden requerir una acción separada; la documentación debe explicarlo sin prometer borrados que no se han verificado.

<figure class="concept-figure"><img src="assets/img/ra7/ra7-05-ciclo-sin-comandos.png" alt="Ciclo visual de una PWA: instalar desde el navegador, verificar, crear datos, publicar una actualización, comprobar la versión y desinstalar; la validación puede publicar o bloquear el cambio." loading="lazy" width="1672" height="941"><figcaption>El ciclo completo se comprueba desde el navegador y distingue la aplicación instalada de los datos conservados por el sitio.</figcaption></figure>

## Ejemplo básico resuelto

La IA genera un diagrama del ciclo: **versión aprobada → validación → publicación → aviso de actualización → comprobación**. El alumnado identifica el orden, la condición que bloquea el avance y el resultado mostrado en cada pantalla, y detecta si faltan versión, autorización o evidencia de publicación.

## RA7-PB05 · Ciclo desatendido y retirada

Configura desde la interfaz una actualización automática para una versión aprobada. Después instala la PWA en un perfil limpio, crea dos datos, publica la actualización, acepta o comprueba el aviso correspondiente y desinstala. Registra los estados visibles y comprueba iconos, caché y almacenamiento antes y después.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

La publicación identifica la versión, valida antes de hacerla pública y no contiene secretos. Una validación fallida bloquea el cambio y muestra una explicación. Tras desinstalar, la aplicación desaparece del lanzador; el panel de almacenamiento del navegador permite comprobar cachés e IndexedDB. Si quedan datos, el manual lo declara y explica su borrado voluntario.

</details>

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA7_04_personalizacion.html">← RA7-04</a><a href="https://mosqueteroweb.github.io/damDI/RA7_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA7_06_firma_canales.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA7-06 · Firma y canales</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
