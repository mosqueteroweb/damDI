---
layout: default
title: RA3-03 · Eventos y acciones
---

# RA3-03 · Eventos y asociación de acciones

## Objetivo docente

Determinar los eventos del componente, asociar acciones internas y comunicar intenciones a la aplicación sin acoplarla.

## Contenido para explicar

El componente atiende eventos internos como `click` o teclado, pero publica eventos de dominio como `task-toggle` o `task-delete-request`. Así, la aplicación decide si actualiza datos, confirma o muestra un mensaje. El evento debe tener nombre, momento, datos y reglas de propagación documentados.

## Ejemplo básico resuelto

```js
button.addEventListener('click', () => {
  this.dispatchEvent(new CustomEvent('task-toggle', {
    detail: { id: this.taskId, completed: !this.completed },
    bubbles: true,
    composed: true
  }));
});
```

Partes relevantes: el clic es interno; `task-toggle` expresa intención; `detail` transporta solo los datos necesarios; `bubbles` permite escuchar desde la lista; `composed` permite atravesar el límite del Shadow DOM.

## RA3-PB03 · Publicar acciones sin acoplamiento

Genera con IA dos eventos: `task-toggle` y `task-delete-request`. La tarjeta no puede modificar `localStorage` ni borrar su propia instancia. La aplicación anfitriona debe registrar ambos y mostrar en pantalla la acción recibida.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

La tarjeta emite `{id, completed}` al alternar y `{id}` al solicitar borrado. Un único escuchador en el contenedor usa delegación:

```js
list.addEventListener('task-delete-request', (event) => {
  status.textContent = `Solicitud de borrado: ${event.detail.id}`;
});
```

La evidencia demuestra que dos instancias funcionan con el mismo escuchador. Si la tarjeta llama directamente a una función global de la aplicación, todavía existe acoplamiento.

</details>

## Comprobación y cierre

Registra temporalmente los eventos en consola, activa por ratón y teclado y explica qué acción corresponde al componente y cuál a la aplicación.

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA3_02_propiedades_metodos.html">← RA3-02</a><a href="https://mosqueteroweb.github.io/damDI/RA3_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA3_04_persistencia.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA3-04 · Persistencia del componente</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
