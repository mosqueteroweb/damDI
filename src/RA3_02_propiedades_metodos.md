---
layout: default
title: RA3-02 · Propiedades, atributos y métodos
---

# RA3-02 · Propiedades, atributos y métodos

## Objetivo docente

Definir un contrato público pequeño, con valores por defecto, tipos comprensibles y métodos que expresen acciones del componente.

## Contenido para explicar

Los **atributos** aparecen en HTML y resultan adecuados para configuración declarativa. Las **propiedades** se consultan o cambian desde JavaScript y pueden contener valores más ricos. Los **métodos** piden al componente que haga algo. El contrato debe indicar nombres, tipos, valores por defecto y efecto esperado.

Conviene reflejar atributo y propiedad cuando el estado sea visible y simple. La fuente de verdad debe ser única para evitar que HTML, JavaScript y pantalla discrepen.

## Ejemplo básico resuelto

```js
class TaskCard extends HTMLElement {
  static observedAttributes = ['title', 'completed'];
  get title() { return this.getAttribute('title') ?? 'Tarea sin título'; }
  set title(value) { this.setAttribute('title', value); }
  get completed() { return this.hasAttribute('completed'); }
  set completed(value) { this.toggleAttribute('completed', Boolean(value)); }
  toggle() { this.completed = !this.completed; }
  attributeChangedCallback() { this.render(); }
}
```

La IA ha generado un título seguro por defecto, una propiedad booleana y un método público. El alumnado debe localizar dónde se convierte cada valor y dónde se solicita el nuevo renderizado.

## RA3-PB02 · Diseñar el contrato

Amplía `task-card` con `priority` (`normal` por defecto), `dueDate` (vacía) y el método `focusAction()`. Produce una tabla de contrato y tres casos: configuración mínima, completa y valor inesperado.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

| Miembro | Tipo | Predeterminado | Efecto |
|---|---|---|---|
| `title` | texto | `Tarea sin título` | Encabezado visible |
| `completed` | booleano | `false` | Estado y estilo |
| `priority` | `low`, `normal`, `high` | `normal` | Indicador de prioridad |
| `dueDate` | fecha ISO o vacío | vacío | Fecha opcional |
| `focusAction()` | método | — | Lleva foco a la acción principal |

Si `priority` no pertenece al conjunto, el componente usa `normal` y no rompe el renderizado. La entrega incluye el fragmento generado que aplica esa normalización.

</details>

## Comprobación y cierre

Cambia cada propiedad desde la consola y explica si se refleja en el atributo y en la pantalla. Justifica por qué no se expone un método genérico `doEverything()`.

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA3_01_concepto_componentes.html">← RA3-01</a><a href="https://mosqueteroweb.github.io/damDI/RA3_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA3_03_eventos_acciones.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA3-03 · Eventos y acciones</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
