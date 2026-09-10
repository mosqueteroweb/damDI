---
layout: default
title: RA8-05 · Pruebas de seguridad
---

# RA8-05 · Pruebas de seguridad

## Objetivo docente

Comprobar riesgos básicos de entrada, salida, almacenamiento, dependencias y configuración sin atacar sistemas ajenos.

## Contenido para explicar

Las pruebas se realizan solo sobre la copia local autorizada. Se revisan validación, codificación de salida, secretos, permisos, almacenamiento, cabeceras y dependencias. Un escáner ofrece indicios; cada hallazgo se reproduce, clasifica y verifica manualmente antes de concluir.

## Ejemplo básico resuelto

Dato de prueba: `<img src=x onerror=alert(1)>`. Si se asigna con `textContent`, aparece como texto; con `innerHTML` puede interpretarse. La corrección generada debe cambiar el punto de salida, no «limpiar» caracteres al azar.

```js
titleNode.textContent = task.title;
```

El alumnado explica que `textContent` trata el valor como texto y vuelve a ejecutar el caso.

## RA8-PB05 · Cinco controles seguros

Prueba entrada maliciosa como texto, secreto simulado en archivos, almacenamiento de datos sensibles, dependencia desactualizada y cabeceras en servidor local. Ejecuta ZAP Baseline de forma pasiva y contrasta dos avisos.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

La aplicación muestra literalmente la cadena, no incluye claves, almacena solo datos ficticios y documenta dependencias. ZAP señala una cabecera ausente; el alumno confirma la respuesta HTTP y propone configuración. Un aviso no aplicable se marca con evidencia. Tras corregir la salida, la prueba de regresión de seguridad pasa.

</details>

## Cierre

Entrega alcance autorizado, evidencia reproducible, severidad, corrección y repetición. No incluyas cargas contra GitHub Pages ni servicios externos.

Referencia: [ZAP Baseline Scan](https://www.zaproxy.org/docs/docker/baseline-scan/).

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA8_04_recursos.html">← RA8-04</a><a href="https://mosqueteroweb.github.io/damDI/RA8_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA8_06_manual_automatica_regresion.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA8-06 · Pruebas manuales, automáticas y regresión</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
