---
layout: default
title: RA1-04 · Lenguajes descriptivos para definir interfaces
---

# RA1-04 — Lenguajes descriptivos para definir interfaces

**Ejemplo RA1-EJ04 · Práctica RA1-PB04 · RA1.e · Sesión orientativa: 55 min.**

---

## Qué aprenderá el alumnado

Al terminar, podrá **leer la estructura declarativa de una pantalla y relacionarla con lo visible**. El código se estudia como salida de herramientas de IA: el alumnado no tiene que memorizarlo ni escribirlo desde cero, pero sí localizar lo relevante, explicar el cambio y verificar su efecto.

## Idea clave

HTML describe una jerarquía de elementos. CSS decide buena parte de su presentación y JavaScript añade comportamiento; ninguno sustituye por sí solo a los otros.

## Secuencia de clase

1. **Activación (5 min):** muestra la pantalla o comportamiento y pregunta dónde creen que se define.
2. **Explicación guiada:** presenta la idea clave y separa herramienta, interfaz, datos y comportamiento.
3. **RA1-EJ04:** recorre el ejemplo resuelto y señala las líneas relevantes.
4. **Cambio con IA:** formula una petición pequeña, conserva el original y revisa diferencias.
5. **RA1-PB04:** el alumnado trabaja desde una base independiente.
6. **Cierre:** cada alumno explica una decisión y una comprobación.

## RA1-EJ04 — Ejemplo resuelto

Relaciona el formulario, sus contenedores, etiquetas e identificadores con la pantalla que genera el navegador.

~~~text
<main>
  <h1>Tareas</h1>
  <form id="formulario">
    <label for="titulo">Título</label>
    <input id="titulo">
  </form>
</main>
~~~

### Lectura guiada

- ¿Qué requisito resuelve cada fragmento?
- ¿Qué parte procede de la descripción visual y cuál añade comportamiento?
- ¿Qué cambiaría en pantalla al modificarlo?
- ¿Qué debe conservarse para no romper las conexiones existentes?

### Prompt docente orientativo

~~~text
Analiza este fragmento de una interfaz web generada con IA.
Señala únicamente las líneas relacionadas con: leer la estructura declarativa de una pantalla y relacionarla con lo visible.
Explica su efecto con lenguaje sencillo y propón un cambio mínimo.
No regeneres el proyecto completo y conserva identificadores y eventos.
Distingue lo que has razonado de lo que debe comprobarse en navegador.
~~~

## RA1-PB04 — Práctica básica

**Punto de partida:** proyecto web preparado por el profesor, ejecutable e independiente de prácticas anteriores.

**Tarea:** Marca cinco correspondencias pantalla–código, dibuja el árbol de contenedores y predice el efecto de mover el input fuera del form.

**Entrega:** Plano anotado, jerarquía de contenedores y predicción razonada.

**Comprobación mínima:**

- El resultado se abre y funciona en navegador.
- El alumno localiza el fragmento relevante.
- El cambio está delimitado y existe una comparación antes/después cuando corresponda.
- La explicación usa evidencias propias; una respuesta copiada de la IA no basta.
- Se conserva el enfoque visual de Material Design 3 y el funcionamiento con teclado.

### Solución orientativa

| Nivel | Evidencia observable |
|---|---|
| Satisfactorio | Cumple la tarea, localiza el fragmento, explica la relación y aporta una prueba coherente. |
| En revisión | El resultado funciona, pero falta justificar la elección o demostrar el proceso. |
| Insuficiente | Solo aporta una captura o texto de IA, no localiza el código o el comportamiento no corresponde al requisito. |

## Comprobación y cierre

1. ¿Qué elemento o fragmento fue decisivo?
2. ¿Qué pidió exactamente a la IA?
3. ¿Qué diferencia revisó?
4. ¿Cómo sabe que no se rompió otra parte?


---

<nav class="unit-nav" aria-label="Navegación entre unidades">
  <div class="unit-nav__secondary">
    <a href="https://mosqueteroweb.github.io/damDI/RA1_03_herramientas_edicion.html">← RA1-03</a>
    <a href="RA1_00_guia_docente.md">Índice del RA1</a>
  </div>
  <a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA1_05_componentes.html">
    <span class="unit-next-card__eyebrow">Siguiente unidad</span>
    <strong>RA1-05 · Componentes</strong>
    <span class="unit-next-card__arrow" aria-hidden="true">→</span>
  </a>
</nav>
