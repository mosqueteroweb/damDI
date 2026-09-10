---
layout: default
title: RA4-01 · Usabilidad, accesibilidad y estándares
---

# RA4-01 · Usabilidad, accesibilidad y estándares

## Objetivo docente

Distinguir usabilidad y accesibilidad, identificar estándares y convertir un problema observado en un requisito comprobable.

## Contenido para explicar

La **usabilidad** estudia si las personas alcanzan sus objetivos con eficacia, eficiencia y satisfacción. La **accesibilidad** busca que puedan percibir, comprender, navegar e interactuar personas con capacidades y contextos diversos. Se relacionan, pero una interfaz cómoda para la mayoría puede seguir excluyendo a alguien.

Referencias de trabajo: WCAG 2.2 para accesibilidad web, WAI-ARIA cuando HTML nativo no basta, heurísticas de usabilidad como instrumento de inspección y Material Design 3 como sistema visual. ARIA no repara una estructura HTML incorrecta.

## Ejemplo básico resuelto

Problema: el botón de borrar solo muestra un icono de papelera gris claro.

| Observación | Riesgo | Decisión | Prueba |
|---|---|---|---|
| No tiene nombre visible ni accesible | No se comprende con lector de pantalla | Añadir nombre accesible y ayuda textual cuando sea necesaria | Revisar nombre accesible y activar con teclado |
| Contraste débil | Puede pasar inadvertido | Usar color de rol y estado perceptible | Medir contraste y revisar en contexto |
| Acción destructiva inmediata | Facilita errores | Confirmación o posibilidad de deshacer | Borrar una tarea y recuperarla |

Código que la IA puede producir y el alumno debe reconocer:

```html
<button type="button" aria-label="Eliminar tarea Matemáticas">
  <span aria-hidden="true">delete</span>
</button>
```

Partes relevantes: `button` aporta interacción nativa; `aria-label` proporciona el nombre; el icono decorativo se oculta al árbol accesible.

## RA4-PB01 · Diagnóstico razonado

Analiza una pantalla del gestor de tareas y registra seis hallazgos: dos de usabilidad, dos de accesibilidad y dos que afecten a ambas. Vincula cada hallazgo con una pauta o principio y propone una comprobación.

### Solución orientativa

<details><summary>Mostrar ejemplo de solución</summary>

- Campo sin etiqueta: accesibilidad; asociar `label` y verificar el nombre accesible.
- Botón «OK»: usabilidad; cambiar a «Guardar tarea» y preguntar a dos usuarios qué ocurrirá.
- Foco invisible: ambas; aplicar indicador visible y recorrer la página con Tab.
- Error expresado solo con rojo: ambas; añadir texto e icono y simular visión sin color.
- Formulario sin orden lógico: usabilidad; reorganizar según la tarea y medir retrocesos.
- Texto con contraste insuficiente: accesibilidad; corregir el rol de color y medirlo.

</details>

## Cierre

El alumno entrega tabla de hallazgos, referencias consultadas y priorización. Debe explicar consecuencias, no limitarse a nombrar normas.

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA4_00_guia_docente.html">← Guía RA4</a><a href="https://mosqueteroweb.github.io/damDI/RA4_matriz_contenidos_evaluacion.html">Matriz</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA4_02_medicion_herramientas.html"><span class="unit-next-card__eyebrow">Siguiente unidad</span><strong>RA4-02 · Medidas y herramientas</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
