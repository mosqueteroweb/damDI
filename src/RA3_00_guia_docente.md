---
layout: default
title: RA3 · Guía docente
---

# RA3 · Creación de componentes visuales

> **Duración propuesta: 16 horas · Ruta web · Material Design 3 como referencia visual**

## Resultado de aprendizaje

Crea componentes visuales valorando y empleando herramientas específicas.

## Producto del RA

El alumnado convierte partes repetidas del gestor de tareas de RA1/RA4 en componentes web reutilizables. La IA genera el punto de partida; el alumnado identifica la interfaz pública, ajusta cambios localizados, prueba, documenta y empaqueta. No se exige escribir el componente desde cero.

## Decisión tecnológica

Se emplean **Web Components** (`customElements`, plantillas HTML y módulos JavaScript) porque funcionan en el navegador sin instalar un framework, permiten observar con claridad propiedades, métodos y eventos, y se pueden empaquetar como módulos. Es un complemento justificado a Stitch, Gemini y Google AI Studio. Material Design 3 guía la anatomía, los estados y los tokens visuales; no se copia una librería completa.

## Secuencia docente

| Sesión | Unidad | Horas | Evidencia principal |
|---:|---|---:|---|
| 1 | Concepto y características | 2 | Anatomía y primer componente |
| 2 | Propiedades, atributos y métodos | 2 | Contrato público con valores por defecto |
| 3 | Eventos y acciones | 2 | Evento personalizado verificable |
| 4 | Persistencia | 2 | Estado restaurado sin duplicar responsabilidades |
| 5 | Herramientas de diseño y desarrollo | 2 | Flujo comparado y componente refinado |
| 6 | Pruebas de componentes | 2 | Pruebas unitarias y registro de resultados |
| 7 | Documentación y empaquetado | 2 | Paquete reutilizable documentado |
| 8 | Integrador y defensa | 2 | Biblioteca mínima usada por una aplicación |

## Flujo de cada clase

1. Mostrar una repetición o un problema real de la interfaz.
2. Explicar un concepto y resolver un ejemplo pequeño.
3. Pedir a la IA un cambio acotado con criterios de aceptación.
4. Localizar en el código generado la parte que define el contrato del componente.
5. Ejecutar la práctica básica y su comprobación.
6. Comparar la entrega con la solución orientativa.
7. Cerrar con una explicación oral breve: qué entra, qué sale y qué se ha probado.

## Herramientas

- **Stitch:** diseño de anatomía, variantes y estados del componente.
- **Gemini / Google AI Studio:** generación, explicación, refactorización delimitada y propuesta de pruebas.
- **DevTools del navegador:** inspección de atributos, propiedades, eventos, almacenamiento y accesibilidad.
- **Web Test Runner, Vitest o un banco HTML con `console.assert`:** pruebas; se empieza por la alternativa sin instalación.
- **Material Design 3:** referencia para roles visuales, estados y comportamiento coherente.

## Evaluación

Las siete prácticas básicas producen evidencias parciales. El integrador cubre los ocho criterios de evaluación y exige una aplicación que use los componentes creados. Una captura o un código generado sin explicación ni prueba no demuestra el criterio.

## Preparación del profesor

- Conservar una versión del gestor de tareas con tarjetas y botones repetidos.
- Preparar un componente defectuoso: valores rígidos, evento global y ausencia de prueba.
- Probar el almacenamiento del navegador en modo normal y privado.
- Recordar que el objetivo es comprender y gobernar la salida de IA, no memorizar la API.

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/">← Inicio</a><a href="https://mosqueteroweb.github.io/damDI/RA3_matriz_contenidos_evaluacion.html">Matriz RA3</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA3_01_concepto_componentes.html"><span class="unit-next-card__eyebrow">Primera unidad</span><strong>RA3-01 · Concepto y características</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
