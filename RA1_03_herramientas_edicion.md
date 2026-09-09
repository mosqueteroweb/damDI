---
layout: default
title: RA1-03 · Herramientas propietarias y libres de edición de interfaces
---

# RA1-03 — Herramientas propietarias y libres de edición de interfaces

**Ejemplo RA1-EJ03 · Práctica RA1-PB03 · RA1.a, RA1.b, RA1.c · Sesión orientativa: 75 min.**

---

<nav class="unit-nav" aria-label="Navegación entre unidades">
  <div class="unit-nav__secondary">
    <a href="RA1_02_librerias_componentes.md">← RA1-02</a>
    <a href="index.md#itinerario-completo-del-ra1">Índice del RA1</a>
  </div>
  <a class="unit-next-card" href="RA1_04_lenguajes_descriptivos.md">
    <span class="unit-next-card__eyebrow">Siguiente unidad</span>
    <strong>RA1-04 · Lenguajes descriptivos</strong>
    <span class="unit-next-card__arrow" aria-hidden="true">→</span>
  </a>
</nav>

## Qué aprenderá el alumnado

Al terminar, podrá **distinguir herramientas y crear un formulario manipulando componentes en un editor visual**. El código se estudia como salida de herramientas de IA: el alumnado no tiene que memorizarlo ni escribirlo desde cero, pero sí localizar lo relevante, explicar el cambio y verificar su efecto.

## Idea clave

El resultado final no basta: hay que demostrar qué operaciones de inserción, selección, alineación y reubicación se realizaron en el editor.

## Secuencia de clase

1. **Activación (5 min):** muestra la pantalla o comportamiento y pregunta dónde creen que se define.
2. **Explicación guiada:** presenta la idea clave y separa herramienta, interfaz, datos y comportamiento.
3. **RA1-EJ03:** recorre el ejemplo resuelto y señala las líneas relevantes.
4. **Cambio con IA:** formula una petición pequeña, conserva el original y revisa diferencias.
5. **RA1-PB03:** el alumnado trabaja desde una base independiente.
6. **Cierre:** cada alumno explica una decisión y una comprobación.

## RA1-EJ03 — Ejemplo resuelto

Parte de un boceto de alta de tareas, genera una propuesta con Stitch y contrástala con un editor visual web como GrapesJS.

~~~text
<form class="panel">
  <input id="titulo">
  <select id="prioridad"></select>
  <button>Añadir</button>
</form>
~~~

### Lectura guiada

- ¿Qué requisito resuelve cada fragmento?
- ¿Qué parte procede de la descripción visual y cuál añade comportamiento?
- ¿Qué cambiaría en pantalla al modificarlo?
- ¿Qué debe conservarse para no romper las conexiones existentes?

### Prompt docente orientativo

~~~text
Analiza este fragmento de una interfaz web generada con IA.
Señala únicamente las líneas relacionadas con: distinguir herramientas y crear un formulario manipulando componentes en un editor visual.
Explica su efecto con lenguaje sencillo y propón un cambio mínimo.
No regeneres el proyecto completo y conserva identificadores y eventos.
Distingue lo que has razonado de lo que debe comprobarse en navegador.
~~~

## RA1-PB03 — Práctica básica

**Punto de partida:** proyecto web preparado por el profesor, ejecutable e independiente de prácticas anteriores.

**Tarea:** Crea el formulario, inserta sus controles y cambia al menos una vez su distribución usando funciones visuales. Conserva capturas antes/después.

**Entrega:** Comparación de herramientas, archivo editable, dos estados visuales y operaciones del editor identificadas.

**Comprobación mínima:**

- El resultado se abre y funciona en navegador.
- El alumno localiza el fragmento relevante.
- El cambio está delimitado y existe una comparación antes/después cuando corresponda.
- La explicación usa evidencias propias; una respuesta copiada de la IA no basta.
- Se conserva el enfoque visual de Material Design 3 y el funcionamiento con teclado.

## Corrección rápida

| Nivel | Evidencia observable |
|---|---|
| Satisfactorio | Cumple la tarea, localiza el fragmento, explica la relación y aporta una prueba coherente. |
| En revisión | El resultado funciona, pero falta justificar la elección o demostrar el proceso. |
| Insuficiente | Solo aporta una captura o texto de IA, no localiza el código o el comportamiento no corresponde al requisito. |

## Preguntas de cierre

1. ¿Qué elemento o fragmento fue decisivo?
2. ¿Qué pidió exactamente a la IA?
3. ¿Qué diferencia revisó?
4. ¿Cómo sabe que no se rompió otra parte?


---

<nav class="unit-nav" aria-label="Navegación entre unidades">
  <div class="unit-nav__secondary">
    <a href="RA1_02_librerias_componentes.md">← RA1-02</a>
    <a href="index.md#itinerario-completo-del-ra1">Índice del RA1</a>
  </div>
  <a class="unit-next-card" href="RA1_04_lenguajes_descriptivos.md">
    <span class="unit-next-card__eyebrow">Siguiente unidad</span>
    <strong>RA1-04 · Lenguajes descriptivos</strong>
    <span class="unit-next-card__arrow" aria-hidden="true">→</span>
  </a>
</nav>
