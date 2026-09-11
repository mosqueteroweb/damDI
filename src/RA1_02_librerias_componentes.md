---
layout: default
title: RA1-02 · Librerías de componentes nativas y multiplataforma
---

# RA1-02 — Librerías de componentes nativas y multiplataforma

**Ejemplo RA1-EJ02 · Práctica RA1-PB02 · RA1.a · Sesión orientativa: 55 min.**

---

## Qué aprenderá el alumnado

Al terminar, podrá **comparar alternativas de componentes y justificar cuál encaja en una interfaz web**. El código se estudia como salida de herramientas de IA: el alumnado no tiene que memorizarlo ni escribirlo desde cero, pero sí localizar lo relevante, explicar el cambio y verificar su efecto.

## Idea clave

Una librería aporta componentes reutilizables; no es lo mismo que el editor que coloca elementos ni que la IA que genera código.

## Secuencia de clase

1. **Activación (5 min):** muestra la pantalla o comportamiento y pregunta dónde creen que se define.
2. **Explicación guiada:** presenta la idea clave y separa herramienta, interfaz, datos y comportamiento.
3. **RA1-EJ02:** recorre el ejemplo resuelto y señala las líneas relevantes.
4. **Cambio con IA:** formula una petición pequeña, conserva el original y revisa diferencias.
5. **RA1-PB02:** el alumnado trabaja desde una base independiente.
6. **Cierre:** cada alumno explica una decisión y una comprobación.

## RA1-EJ02 — Ejemplo resuelto

Compara controles HTML nativos y una librería de componentes para un formulario de tareas. Revisa destino, dependencia, personalización, accesibilidad y mantenimiento.

~~~text
<label for="titulo">Título</label>
<input id="titulo" maxlength="80" required>
<button type="submit">Añadir</button>
~~~

### Lectura guiada

- ¿Qué requisito resuelve cada fragmento?
- ¿Qué parte procede de la descripción visual y cuál añade comportamiento?
- ¿Qué cambiaría en pantalla al modificarlo?
- ¿Qué debe conservarse para no romper las conexiones existentes?

### Prompt docente orientativo

~~~text
Analiza este fragmento de una interfaz web generada con IA.
Señala únicamente las líneas relacionadas con: comparar alternativas de componentes y justificar cuál encaja en una interfaz web.
Explica su efecto con lenguaje sencillo y propón un cambio mínimo.
No regeneres el proyecto completo y conserva identificadores y eventos.
Distingue lo que has razonado de lo que debe comprobarse en navegador.
~~~

## RA1-PB02 — Práctica básica

**Punto de partida:** proyecto web preparado por el profesor, ejecutable e independiente de prácticas anteriores.

**Tarea:** Completa una tabla comparativa de dos alternativas y elige una para el formulario. Localiza en dos muestras cómo se referencia la librería y qué componente aporta.

**Entrega:** Tabla con plataformas, componentes, limitaciones, fuentes y decisión argumentada.

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
    <a href="https://mosqueteroweb.github.io/damDI/RA1_01_patrones_arquitectura.html">← RA1-01</a>
    <a href="RA1_00_guia_docente.md">Índice del RA1</a>
  </div>
  <a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA1_03_herramientas_edicion.html">
    <span class="unit-next-card__eyebrow">Siguiente unidad</span>
    <strong>RA1-03 · Herramientas de edición</strong>
    <span class="unit-next-card__arrow" aria-hidden="true">→</span>
  </a>
</nav>
