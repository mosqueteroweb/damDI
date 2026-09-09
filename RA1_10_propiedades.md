---
layout: default
title: RA1-10 · Propiedades de los componentes
---

# RA1-10 — Propiedades de los componentes

**Ejemplo RA1-EJ10 · Práctica RA1-PB10 · RA1.d · Sesión orientativa: 50 min.**

---

[← Unidad anterior](RA1_09_clases.md) · [Índice del RA1](index.md#itinerario-completo-del-ra1) · [Unidad siguiente →](RA1_11_metodos.md)

## Qué aprenderá el alumnado

Al terminar, podrá **relacionar propiedades con apariencia, contenido, estado y comportamiento**. El código se estudia como salida de herramientas de IA: el alumnado no tiene que memorizarlo ni escribirlo desde cero, pero sí localizar lo relevante, explicar el cambio y verificar su efecto.

## Idea clave

Una propiedad pertenece a un componente y su valor produce un efecto observable. No toda característica visible está almacenada como dato de negocio.

## Secuencia de clase

1. **Activación (5 min):** muestra la pantalla o comportamiento y pregunta dónde creen que se define.
2. **Explicación guiada:** presenta la idea clave y separa herramienta, interfaz, datos y comportamiento.
3. **RA1-EJ10:** recorre el ejemplo resuelto y señala las líneas relevantes.
4. **Cambio con IA:** formula una petición pequeña, conserva el original y revisa diferencias.
5. **RA1-PB10:** el alumnado trabaja desde una base independiente.
6. **Cierre:** cada alumno explica una decisión y una comprobación.

## RA1-EJ10 — Ejemplo resuelto

maxlength limita la entrada, disabled cambia disponibilidad, value fija un valor y textContent actualiza contenido seguro.

~~~text
titulo.maxLength = 80;
prioridad.value = 'normal';
boton.disabled = false;
mensaje.textContent = 'Formulario preparado';
~~~

### Lectura guiada

- ¿Qué requisito resuelve cada fragmento?
- ¿Qué parte procede de la descripción visual y cuál añade comportamiento?
- ¿Qué cambiaría en pantalla al modificarlo?
- ¿Qué debe conservarse para no romper las conexiones existentes?

### Prompt docente orientativo

~~~text
Analiza este fragmento de una interfaz web generada con IA.
Señala únicamente las líneas relacionadas con: relacionar propiedades con apariencia, contenido, estado y comportamiento.
Explica su efecto con lenguaje sencillo y propón un cambio mínimo.
No regeneres el proyecto completo y conserva identificadores y eventos.
Distingue lo que has razonado de lo que debe comprobarse en navegador.
~~~

## RA1-PB10 — Práctica básica

**Punto de partida:** proyecto web preparado por el profesor, ejecutable e independiente de prácticas anteriores.

**Tarea:** Aplica tres requisitos cambiando propiedades desde el editor o con ayuda de IA y comprueba cada efecto.

**Entrega:** Tabla requisito–componente–propiedad–valor y capturas del resultado.

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

[← Unidad anterior](RA1_09_clases.md) · [Índice del RA1](index.md#itinerario-completo-del-ra1) · [Unidad siguiente →](RA1_11_metodos.md)
