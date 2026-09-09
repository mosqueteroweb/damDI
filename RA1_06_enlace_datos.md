---
layout: default
title: RA1-06 · Enlace de componentes a orígenes de datos
---

# RA1-06 — Enlace de componentes a orígenes de datos

**Ejemplo RA1-EJ06 · Práctica RA1-PB06 · RA1.e, RA1.f · Sesión orientativa: 65 min.**

---

<nav class="unit-nav" aria-label="Navegación entre unidades">
  <div class="unit-nav__secondary">
    <a href="RA1_05_componentes.md">← RA1-05</a>
    <a href="index.md#itinerario-completo-del-ra1">Índice del RA1</a>
  </div>
  <a class="unit-next-card" href="RA1_07_acciones_eventos.md">
    <span class="unit-next-card__eyebrow">Siguiente unidad</span>
    <strong>RA1-07 · Acciones y eventos</strong>
    <span class="unit-next-card__arrow" aria-hidden="true">→</span>
  </a>
</nav>

## Qué aprenderá el alumnado

Al terminar, podrá **seguir el recorrido de un dato desde una colección hasta su representación visual**. El código se estudia como salida de herramientas de IA: el alumnado no tiene que memorizarlo ni escribirlo desde cero, pero sí localizar lo relevante, explicar el cambio y verificar su efecto.

## Idea clave

El array es el origen de datos; los elementos de la lista son su representación. Escribir texto fijo no demuestra enlace ni actualización.

## Secuencia de clase

1. **Activación (5 min):** muestra la pantalla o comportamiento y pregunta dónde creen que se define.
2. **Explicación guiada:** presenta la idea clave y separa herramienta, interfaz, datos y comportamiento.
3. **RA1-EJ06:** recorre el ejemplo resuelto y señala las líneas relevantes.
4. **Cambio con IA:** formula una petición pequeña, conserva el original y revisa diferencias.
5. **RA1-PB06:** el alumnado trabaja desde una base independiente.
6. **Cierre:** cada alumno explica una decisión y una comprobación.

## RA1-EJ06 — Ejemplo resuelto

Una colección de tareas alimenta la lista. Al añadir prioridad a la plantilla, cada fila debe mostrar el valor real de su objeto.

~~~text
const tareas = [{ titulo: 'Leer', prioridad: 'Alta' }];
for (const tarea of tareas) {
  const fila = document.createElement('li');
  fila.textContent = `${tarea.titulo} — ${tarea.prioridad}`;
  lista.append(fila);
}
~~~

### Lectura guiada

- ¿Qué requisito resuelve cada fragmento?
- ¿Qué parte procede de la descripción visual y cuál añade comportamiento?
- ¿Qué cambiaría en pantalla al modificarlo?
- ¿Qué debe conservarse para no romper las conexiones existentes?

### Prompt docente orientativo

~~~text
Analiza este fragmento de una interfaz web generada con IA.
Señala únicamente las líneas relacionadas con: seguir el recorrido de un dato desde una colección hasta su representación visual.
Explica su efecto con lenguaje sencillo y propón un cambio mínimo.
No regeneres el proyecto completo y conserva identificadores y eventos.
Distingue lo que has razonado de lo que debe comprobarse en navegador.
~~~

## RA1-PB06 — Práctica básica

**Punto de partida:** proyecto web preparado por el profesor, ejecutable e independiente de prácticas anteriores.

**Tarea:** Localiza colección, recorrido y representación. Pide a la IA un cambio localizado para mostrar prioridad y prueba con dos valores distintos.

**Entrega:** Antes/después, prompt, captura y explicación del recorrido del dato.

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
    <a href="RA1_05_componentes.md">← RA1-05</a>
    <a href="index.md#itinerario-completo-del-ra1">Índice del RA1</a>
  </div>
  <a class="unit-next-card" href="RA1_07_acciones_eventos.md">
    <span class="unit-next-card__eyebrow">Siguiente unidad</span>
    <strong>RA1-07 · Acciones y eventos</strong>
    <span class="unit-next-card__arrow" aria-hidden="true">→</span>
  </a>
</nav>
