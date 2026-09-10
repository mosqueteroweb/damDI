---
layout: default
title: RA7-03 · Herramientas para crear paquetes
---

# RA7-03 · Herramientas para crear paquetes de instalación

## Objetivo docente

Generar el mismo producto mediante el entorno de desarrollo y una herramienta externa, comparando trazabilidad y repetibilidad.

## Contenido para explicar

El IDE puede exponer una tarea de compilación; la herramienta externa ejecuta la cadena sin interfaz. Ambas deben partir del mismo bloqueo de dependencias, producir una versión identificada y fallar de forma visible. GitHub Actions añade un entorno limpio y conserva el artefacto; no convierte automáticamente una compilación en una release válida.

## Ejemplo básico resuelto

```json
{
  "scripts": {
    "clean": "rimraf dist",
    "build": "vite build",
    "package": "npm run clean && npm run build"
  }
}
```

El código es salida de IA. El alumnado localiza orden, operador que detiene la cadena, carpeta de salida y dependencia externa; después contrasta el resultado con la tarea equivalente del IDE.

## RA7-PB04 · Dos rutas, un artefacto

Genera el paquete una vez desde una tarea del IDE y otra desde terminal o GitHub Actions. Compara listado, tamaño y hash. Explica cualquier diferencia.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

Ambas rutas ejecutan `npm ci` y el mismo script `package`. El registro conserva versiones de Node/npm, commit y resultado. Si los hashes difieren por marcas de tiempo, se documenta y se compara el contenido; no se oculta la diferencia.

</details>

## Cierre

Señala qué evidencia demuestra que la herramienta externa no depende de tu equipo.

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA7_02_instaladores_autoinstalables.html">← RA7-02</a><a href="https://mosqueteroweb.github.io/damDI/RA7_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA7_04_personalizacion.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA7-04 · Personalización de la instalación</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
