---
layout: default
title: RA3-07 · Documentación y empaquetado
---

# RA3-07 · Documentación y empaquetado

## Objetivo docente

Documentar el contrato y preparar un paquete que otra aplicación pueda importar y utilizar sin conocer su implementación.

## Contenido para explicar

La documentación útil contiene propósito, instalación o importación, ejemplo mínimo, atributos, propiedades, métodos, eventos, estados, accesibilidad y compatibilidad. Empaquetar significa separar fuentes públicas, estilos, pruebas y metadatos, evitando rutas absolutas y dependencias ocultas.

Para esta iniciación basta un módulo ES descargable. `package.json` y npm se muestran como evolución opcional, no como requisito para empezar.

## Ejemplo básico resuelto

```text
task-card/
├── task-card.js
├── task-card.css
├── README.md
├── demo.html
└── tests/task-card.test.html
```

```html
<script type="module" src="./task-card/task-card.js"></script>
<task-card title="Probar paquete"></task-card>
```

El ejemplo mínimo debe funcionar desde una carpeta distinta. El README es parte del producto, no un añadido final.

## RA3-PB07 · Paquete intercambiable

Entrega `status-chip` como carpeta comprimida o módulo versionado. Otra pareja debe abrir `demo.html`, crear una instancia, escuchar un evento y responder una lista de comprobación sin ayuda oral del autor.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

El paquete contiene solo rutas relativas, ejemplo mínimo operativo, tabla del atributo `status` con valor `pending`, evento `status-change`, estados y nota accesible. La prueba se ejecuta desde `tests/`. La pareja consumidora puede usar el componente siguiendo el README. Si necesita copiar código interno a su aplicación, el empaquetado no es suficiente.

</details>

## Lista de salida

- Nombre y versión visibles.
- API pública y valores por defecto documentados.
- Demo y pruebas reproducibles.
- Licencia o condiciones de uso indicadas.
- Archivo sin secretos, rutas locales ni recursos rotos.

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA3_06_pruebas.html">← RA3-06</a><a href="https://mosqueteroweb.github.io/damDI/RA3_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA3_integrador.html"><span class="unit-next-card__eyebrow">Ejercicio integrador</span><strong>RA3-INT01 · Kit visual del gestor de tareas</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
