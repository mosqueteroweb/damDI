---
layout: default
title: RA1-05 · Componentes: características y campo de aplicación
---

# RA1-05 — Componentes: características y campo de aplicación

**Ejemplo RA1-EJ05 · Práctica RA1-PB05 · RA1.b, RA1.d · Sesión orientativa: 60 min.**

---

## Qué aprenderá el alumnado

Al terminar, podrá **elegir controles apropiados y configurar propiedades con un propósito verificable**. El código se estudia como salida de herramientas de IA: el alumnado no tiene que memorizarlo ni escribirlo desde cero, pero sí localizar lo relevante, explicar el cambio y verificar su efecto.

## Idea clave

El control se elige por el tipo de dato y la interacción: texto libre, selección cerrada, acción o estado comunicado.

## Secuencia de clase

1. **Activación (5 min):** muestra la pantalla o comportamiento y pregunta dónde creen que se define.
2. **Explicación guiada:** presenta la idea clave y separa herramienta, interfaz, datos y comportamiento.
3. **RA1-EJ05:** recorre el ejemplo resuelto y señala las líneas relevantes.
4. **Cambio con IA:** formula una petición pequeña, conserva el original y revisa diferencias.
5. **RA1-PB05:** el alumnado trabaja desde una base independiente.
6. **Cierre:** cada alumno explica una decisión y una comprobación.

## RA1-EJ05 — Ejemplo resuelto

Para título se usa entrada de texto; para prioridad con dos valores, un selector; para confirmar, un botón de envío.

~~~text
<input id="titulo" type="text" maxlength="80" required>
<select id="prioridad">
  <option>Normal</option><option>Alta</option>
</select>
~~~

### Lectura guiada

- ¿Qué requisito resuelve cada fragmento?
- ¿Qué parte procede de la descripción visual y cuál añade comportamiento?
- ¿Qué cambiaría en pantalla al modificarlo?
- ¿Qué debe conservarse para no romper las conexiones existentes?

### Prompt docente orientativo

~~~text
Analiza este fragmento de una interfaz web generada con IA.
Señala únicamente las líneas relacionadas con: elegir controles apropiados y configurar propiedades con un propósito verificable.
Explica su efecto con lenguaje sencillo y propón un cambio mínimo.
No regeneres el proyecto completo y conserva identificadores y eventos.
Distingue lo que has razonado de lo que debe comprobarse en navegador.
~~~

## RA1-PB05 — Práctica básica

**Punto de partida:** proyecto web preparado por el profesor, ejecutable e independiente de prácticas anteriores.

**Tarea:** Completa un formulario incompleto en el editor y justifica cada control. Ajusta etiqueta, valor inicial, límite y estado requerido.

**Entrega:** Pantalla editable y tabla requisito–control–propiedad.

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
    <a href="https://mosqueteroweb.github.io/damDI/RA1_04_lenguajes_descriptivos.html">← RA1-04</a>
    <a href="RA1_00_guia_docente.md">Índice del RA1</a>
  </div>
  <a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA1_06_enlace_datos.html">
    <span class="unit-next-card__eyebrow">Siguiente unidad</span>
    <strong>RA1-06 · Enlace de datos</strong>
    <span class="unit-next-card__arrow" aria-hidden="true">→</span>
  </a>
</nav>
