---
layout: default
title: RA1-08 · Edición del código generado por la herramienta de diseño
---

# RA1-08 — Edición del código generado por la herramienta de diseño

**Ejemplo RA1-EJ08 · Práctica RA1-PB08 · RA1.e, RA1.f · Sesión orientativa: 60 min.**

---

## Qué aprenderá el alumnado

Al terminar, podrá **aplicar cambios pequeños al código exportado conservando estructura y comportamiento**. El código se estudia como salida de herramientas de IA: el alumnado no tiene que memorizarlo ni escribirlo desde cero, pero sí localizar lo relevante, explicar el cambio y verificar su efecto.

## Idea clave

Una buena modificación delimita archivo, elementos y restricciones. Regenerar todo dificulta revisar diferencias y puede romper identificadores.

## Secuencia de clase

1. **Activación (5 min):** muestra la pantalla o comportamiento y pregunta dónde creen que se define.
2. **Explicación guiada:** presenta la idea clave y separa herramienta, interfaz, datos y comportamiento.
3. **RA1-EJ08:** recorre el ejemplo resuelto y señala las líneas relevantes.
4. **Cambio con IA:** formula una petición pequeña, conserva el original y revisa diferencias.
5. **RA1-PB08:** el alumnado trabaja desde una base independiente.
6. **Cierre:** cada alumno explica una decisión y una comprobación.

## RA1-EJ08 — Ejemplo resuelto

Cambia el texto de ayuda y mueve su bloque antes de las acciones, conservando los ids y los eventos existentes.

~~~text
Antes: <p id="ayuda">Completa los datos</p>
Después: <p id="ayuda">Título de 1 a 80 caracteres</p>
~~~

### Lectura guiada

- ¿Qué requisito resuelve cada fragmento?
- ¿Qué parte procede de la descripción visual y cuál añade comportamiento?
- ¿Qué cambiaría en pantalla al modificarlo?
- ¿Qué debe conservarse para no romper las conexiones existentes?

### Prompt docente orientativo

~~~text
Analiza este fragmento de una interfaz web generada con IA.
Señala únicamente las líneas relacionadas con: aplicar cambios pequeños al código exportado conservando estructura y comportamiento.
Explica su efecto con lenguaje sencillo y propón un cambio mínimo.
No regeneres el proyecto completo y conserva identificadores y eventos.
Distingue lo que has razonado de lo que debe comprobarse en navegador.
~~~

## RA1-PB08 — Práctica básica

**Punto de partida:** proyecto web preparado por el profesor, ejecutable e independiente de prácticas anteriores.

**Tarea:** Guarda versión inicial, formula un prompt acotado, revisa la diferencia y vuelve a probar añadir y limpiar.

**Entrega:** Original, prompt, versión final, diferencias comentadas y prueba de regresión.

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
    <a href="https://mosqueteroweb.github.io/damDI/RA1_07_acciones_eventos.html">← RA1-07</a>
    <a href="RA1_00_guia_docente.md">Índice del RA1</a>
  </div>
  <a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA1_09_clases.html">
    <span class="unit-next-card__eyebrow">Siguiente unidad</span>
    <strong>RA1-09 · Clases</strong>
    <span class="unit-next-card__arrow" aria-hidden="true">→</span>
  </a>
</nav>
