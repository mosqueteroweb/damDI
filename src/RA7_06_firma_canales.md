---
layout: default
title: RA7-06 · Firma digital y canales
---

# RA7-06 · Firma digital y canales de distribución

## Objetivo docente

Demostrar origen e integridad del artefacto y seleccionar canales según audiencia, actualización y riesgo.

## Contenido para explicar

Un hash detecta cambios, pero no identifica por sí solo al autor. La firma vincula artefacto e identidad mediante una clave o identidad verificable. La clave privada nunca se copia a prompts ni al repositorio. La verificación debe fallar al alterar el paquete. Pages sirve la web; Releases distribuye versiones; una store añade revisión y actualización; ad-hoc limita destinatarios; correo es frágil para binarios y versiones.

## Ejemplo básico resuelto

```text
artefacto → SHA-256 → firma separada → canal
receptor → descarga → verifica firma → instala
```

La explicación de IA se corrige: HTTPS protege el transporte, pero no sustituye la comprobación del artefacto descargado fuera del sitio.

## RA7-PB08 · Firma que detecta cambios

Genera el hash y firma didáctica del ZIP con GPG o Cosign. Verifica el original, altera una copia y registra el fallo. Explica qué demuestra cada comprobación.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

La entrega separa paquete, suma y firma; publica instrucciones de verificación y solo la clave pública necesaria. El original verifica y la copia alterada falla. La clave privada no aparece en archivos, historial, prompts ni capturas.

</details>

## RA7-PB09 · Plan multicanal

Diseña una tabla para Pages, Release, store/ad-hoc y correo con destinatario, formato, actualización, retirada y riesgo. Selecciona un canal principal y justifica los complementarios.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

Pages es el canal principal de la PWA, Release conserva la versión descargable, ad-hoc se reserva al piloto y el correo comparte el enlace, no un binario sin procedencia. Cada canal identifica la versión vigente y cómo retirar una versión defectuosa.

</details>

## Cierre

Explica la diferencia entre cifrar, calcular un hash y firmar.

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA7_05_ciclo_instalacion.html">← RA7-05</a><a href="https://mosqueteroweb.github.io/damDI/RA7_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA7_integrador.html"><span class="unit-next-card__eyebrow">Ejercicio integrador</span><strong>RA7-INT01 · Release candidata del gestor</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
