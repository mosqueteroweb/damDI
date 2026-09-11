---
layout: default
title: RA1-13 · Escuchadores de eventos
---

# RA1-13 — Escuchadores de eventos

**Ejemplo RA1-EJ13 · Práctica RA1-PB13 · RA1.e, RA1.f, RA1.g · Sesión orientativa: 60 min.**

---

## Qué aprenderá el alumnado

Al terminar, podrá **localizar registro y callback, y corregir una asociación duplicada**. El código se estudia como salida de herramientas de IA: el alumnado no tiene que memorizarlo ni escribirlo desde cero, pero sí localizar lo relevante, explicar el cambio y verificar su efecto.

## Idea clave

Un escuchador registra qué función responderá a un evento. Si se registra dos veces, una sola interacción puede ejecutar dos veces la acción.

## Secuencia de clase

1. **Activación (5 min):** muestra la pantalla o comportamiento y pregunta dónde creen que se define.
2. **Explicación guiada:** presenta la idea clave y separa herramienta, interfaz, datos y comportamiento.
3. **RA1-EJ13:** recorre el ejemplo resuelto y señala las líneas relevantes.
4. **Cambio con IA:** formula una petición pequeña, conserva el original y revisa diferencias.
5. **RA1-PB13:** el alumnado trabaja desde una base independiente.
6. **Cierre:** cada alumno explica una decisión y una comprobación.

## RA1-EJ13 — Ejemplo resuelto

La misma llamada a addEventListener aparece duplicada; se conserva un único registro y se verifica el contador.

~~~text
// Incorrecto: registro duplicado
boton.addEventListener('click', añadir);
boton.addEventListener('click', añadir);

// Correcto
boton.addEventListener('click', añadir);
~~~

### Lectura guiada

- ¿Qué requisito resuelve cada fragmento?
- ¿Qué parte procede de la descripción visual y cuál añade comportamiento?
- ¿Qué cambiaría en pantalla al modificarlo?
- ¿Qué debe conservarse para no romper las conexiones existentes?

### Prompt docente orientativo

~~~text
Analiza este fragmento de una interfaz web generada con IA.
Señala únicamente las líneas relacionadas con: localizar registro y callback, y corregir una asociación duplicada.
Explica su efecto con lenguaje sencillo y propón un cambio mínimo.
No regeneres el proyecto completo y conserva identificadores y eventos.
Distingue lo que has razonado de lo que debe comprobarse en navegador.
~~~

## RA1-PB13 — Práctica básica

**Punto de partida:** proyecto web preparado por el profesor, ejecutable e independiente de prácticas anteriores.

**Tarea:** Diagnostica la doble ejecución, pide una corrección localizada y compara antes/después sin cambiar la función añadir.

**Entrega:** Diagnóstico, prompt, diferencia y prueba que demuestre una sola ejecución.

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
    <a href="https://mosqueteroweb.github.io/damDI/RA1_12_eventos.html">← RA1-12</a>
    <a href="RA1_00_guia_docente.md">Índice del RA1</a>
  </div>
  <a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA1_integrador.html">
    <span class="unit-next-card__eyebrow">Siguiente unidad</span>
    <strong>RA1-INT01 · Gestor de tareas del aula</strong>
    <span class="unit-next-card__arrow" aria-hidden="true">→</span>
  </a>
</nav>
