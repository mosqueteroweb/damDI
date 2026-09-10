---
layout: default
title: RA3-01 · Concepto y características
---

# RA3-01 · Concepto y características de un componente

## Objetivo docente

Distinguir componente, instancia y aplicación; reconocer encapsulación, reutilización, composición y contrato público.

## Contenido para explicar

Un componente visual reúne estructura, aspecto y comportamiento con un propósito concreto. Puede instanciarse varias veces, recibe datos por una interfaz pública y comunica cambios sin conocer toda la aplicación. Un buen componente tiene responsabilidad acotada, estados previsibles, accesibilidad y dependencias explícitas.

En el gestor, `task-card` representa una tarea; la aplicación decide qué lista mostrar y qué hacer al recibir una acción. La tarjeta no debería guardar por sí sola toda la colección.

## Ejemplo básico resuelto

Prompt para Gemini o AI Studio: «Genera un Web Component `task-card` sin dependencias. Debe mostrar título y estado, usar HTML semántico, admitir varias instancias y explicar las cinco líneas que forman su interfaz pública».

```html
<task-card title="Preparar exposición" completed></task-card>
<task-card title="Revisar contraste"></task-card>
<script type="module" src="./task-card.js"></script>
```

Partes relevantes: el nombre contiene guion porque lo exige la plataforma; cada etiqueta es una instancia; los atributos son entradas; el módulo registra la definición una sola vez.

## RA3-PB01 · Extraer una tarjeta reutilizable

Pide a la IA que transforme dos tarjetas HTML duplicadas en un componente. Entrega: prompt, dos instancias con datos distintos, captura de ambos estados y anotación de estructura, estilo, comportamiento y contrato público.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

Una solución válida registra `customElements.define('task-card', TaskCard)`, crea su contenido desde la clase y conserva el título como entrada. Las dos instancias se renderizan sin copiar el HTML interno. La explicación identifica que la clase es la definición, las etiquetas son instancias y `title`/`completed` forman parte del contrato. No es válido sustituir la duplicación por dos bloques todavía idénticos.

</details>

## Comprobación y cierre

- ¿Se puede crear una tercera tarjeta solo cambiando datos?
- ¿La tarjeta sigue teniendo un único propósito?
- ¿Qué parte puede cambiar internamente sin romper a quien la usa?

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA3_00_guia_docente.html">← Guía RA3</a><a href="https://mosqueteroweb.github.io/damDI/RA3_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA3_02_propiedades_metodos.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA3-02 · Propiedades, atributos y métodos</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
