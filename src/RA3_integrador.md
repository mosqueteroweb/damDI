---
layout: default
title: RA3-INT01 · Kit visual del gestor de tareas
---

# RA3-INT01 · Kit visual reutilizable del gestor de tareas

## Situación

El centro quiere reutilizar la interfaz del gestor en otras aplicaciones. Las tarjetas, etiquetas de estado y avisos están duplicados y cada copia se comporta de forma distinta.

## Encargo

Con Stitch, Gemini y/o Google AI Studio, transforma esas piezas en una biblioteca mínima de **tres Web Components** y úsalos en una aplicación web funcional. No programes desde cero: conserva prompts y versiones, identifica el código relevante, prueba el contrato y justifica las decisiones.

## Requisitos obligatorios

1. Comparar al menos tres herramientas de diseño o prueba y asignarles una función.
2. Crear `task-card`, `status-chip` y `app-notice` con anatomía y estados M3 coherentes.
3. Definir y documentar propiedades, atributos y métodos, incluidos sus valores por defecto.
4. Publicar eventos de dominio y asociarlos a acciones en la aplicación anfitriona.
5. Persistir la colección y una preferencia visual, con recuperación ante datos ausentes o inválidos.
6. Ejecutar al menos seis pruebas unitarias por componente, incluyendo accesibilidad básica.
7. Empaquetar los componentes con demo, pruebas, versión y documentación.
8. Desarrollar una pantalla del gestor que importe y use los tres componentes.

## Entregables

- Aplicación web ejecutable y carpeta `components/`.
- Tablero o capturas de Stitch con anatomía y estados.
- Historial breve de prompts, decisiones aceptadas y rechazadas.
- Tabla completa del contrato público.
- Fragmentos anotados que muestran registro, valor por defecto, método, evento y persistencia.
- Informe de pruebas con resultado real.
- README y paquete reutilizable.
- Defensa individual de cinco minutos.

## Casos de prueba mínimos

| Caso | Resultado esperado |
|---|---|
| Instancia mínima | Aplica valores por defecto documentados |
| Cambio de atributo | Actualiza solo el componente afectado |
| Método público | Produce el efecto documentado |
| Acción interna | Emite una vez el evento de dominio correcto |
| Recarga | Restaura tareas y preferencia |
| Datos persistidos corruptos | Recupera valores seguros sin bloquear la app |
| Importación en `demo.html` | Funciona sin copiar implementación |
| Teclado y nombre accesible | Acciones alcanzables y comprensibles |

## Guía de corrección por criterios

| CE | Satisfactorio | Insuficiente |
|---|---|---|
| a | Compara herramientas y las usa con propósito | Solo enumera marcas |
| b | Entrega tres componentes visuales reutilizables | Presenta bloques duplicados o no funcionales |
| c | Contrato tipado, pequeño y con valores por defecto | Entradas ambiguas o sin predeterminados |
| d | Eventos de dominio documentados y acciones asociadas | Dependencia directa de funciones globales |
| e | Pruebas unitarias ejecutadas, incluido un fallo corregido | Código de prueba no ejecutado |
| f | README, API, ejemplos y accesibilidad documentados | Documentación incompleta o solo capturas |
| g | Paquete importable, versionado y sin rutas rotas | Requiere copiar código interno |
| h | La aplicación usa los tres componentes creados | Componentes aislados sin aplicación consumidora |

## Solución docente orientativa

<details><summary>Mostrar estructura de una solución válida</summary>

La biblioteca contiene módulos separados y un índice de exportación. `task-card` recibe datos y emite solicitudes; `status-chip` representa estados permitidos; `app-notice` anuncia resultados. La aplicación posee la lista, escucha eventos y guarda JSON versionado. Cada README documenta contrato y ejemplo mínimo. Las pruebas comprueban predeterminados, cambios, métodos, eventos, entradas erróneas y nombres accesibles. Una segunda página importa los módulos sin modificarlos, demostrando empaquetado y reutilización.

</details>

## Preguntas de defensa

1. ¿Qué parte forma el contrato público y cuál puede cambiar sin afectar a la aplicación?
2. ¿Qué decisión de la IA rechazaste y por qué?
3. ¿Cómo evita tu diseño que el componente conozca toda la aplicación?
4. ¿Qué prueba detectó un fallo real?
5. ¿Cómo sabes que el paquete es reutilizable?

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA3_07_documentacion_empaquetado.html">← RA3-07</a><a href="https://mosqueteroweb.github.io/damDI/RA3_matriz_contenidos_evaluacion.html">Matriz RA3</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/"><span class="unit-next-card__eyebrow">Volver al curso</span><strong>Índice general del módulo</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
