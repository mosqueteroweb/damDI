---
layout: default
title: RA3-06 · Pruebas de componentes
---

# RA3-06 · Pruebas unitarias de componentes

## Objetivo docente

Diseñar y ejecutar pruebas unitarias sobre el contrato público, los estados, los eventos y la accesibilidad básica.

## Contenido para explicar

Una prueba unitaria comprueba un comportamiento pequeño en condiciones controladas. Se estructura como preparar, actuar y comprobar. Para un componente interesa probar valores por defecto, cambios de atributos/propiedades, métodos, eventos y contenido accesible. Una prueba no debe depender de detalles visuales irrelevantes.

## Ejemplo básico resuelto

```js
const card = document.createElement('task-card');
document.body.append(card);
console.assert(card.title === 'Tarea sin título', 'título por defecto');

let received;
card.addEventListener('task-toggle', event => received = event.detail);
card.shadowRoot.querySelector('[data-action="toggle"]').click();
console.assert(received.completed === true, 'publica el nuevo estado');
card.remove();
```

La prueba observa el contrato: valor inicial y evento publicado. La consulta interna solo simula la acción; no valida colores exactos.

## RA3-PB06 · Banco de seis pruebas

Solicita a la IA seis pruebas y revisa que cubran: valor por defecto, atributo válido, atributo inesperado, método, evento y nombre accesible. Ejecuta cada una, provoca deliberadamente un fallo y registra diagnóstico y corrección.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

| Caso | Resultado esperado |
|---|---|
| Sin `title` | Usa «Tarea sin título» |
| `priority="high"` | Expone prioridad alta |
| Prioridad desconocida | Normaliza a `normal` |
| `toggle()` | Cambia `completed` |
| Acción de borrar | Emite una vez `{id}` |
| Botón principal | Tiene nombre accesible |

El fallo inducido elimina `bubbles:true`; la prueba desde el contenedor deja de recibir el evento. La corrección restablece la propagación y todas las pruebas pasan.

</details>

## Comprobación y cierre

Entrega salida fechada de las pruebas y explica qué error detectaría cada una. «La IA dice que funciona» no cuenta como ejecución.

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA3_05_herramientas.html">← RA3-05</a><a href="https://mosqueteroweb.github.io/damDI/RA3_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA3_07_documentacion_empaquetado.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA3-07 · Documentación y empaquetado</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
