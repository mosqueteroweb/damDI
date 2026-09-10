---
layout: default
title: RA5-INT01 · Informe de seguimiento del aula
---

# RA5-INT01 · Informe de seguimiento del aula

## Situación

El equipo docente necesita conocer carga, avance y distribución de tareas sin revisar cada registro del gestor. También requiere una versión imprimible para reuniones.

## Encargo

Con Stitch, Gemini y Google AI Studio, crea un informe web incrustado en el gestor y una versión independiente. Parte de datos y código facilitados o generados; identifica, verifica y explica los cambios, sin programar desde cero.

## Requisitos obligatorios

1. Definir encabezado, contexto, filtros, indicadores, gráficos, detalle y metodología.
2. Generar el informe desde JSON y una segunda fuente CSV u hoja mediante un asistente.
3. Filtrar por módulo, estado y rango de fecha; mostrar filtros activos y restablecerlos.
4. Incluir numeración, recuento total, completadas, porcentaje y suma de horas.
5. Añadir al menos dos gráficos adecuados con tabla equivalente.
6. Usar una librería de informes o gráficos y localizar sus clases/objetos, métodos y atributos.
7. Modificar una salida generada por IA mediante un cambio delimitado y documentar el antes/después.
8. Integrar el informe en la aplicación y proporcionar una versión imprimible no incrustada.

## Entregables

- Informe incrustado y versión independiente.
- Fuentes ficticias, diccionario de datos y fecha de corte.
- Diseño Stitch con estados carga, vacío y error.
- Prompts, decisiones y diff de una modificación.
- Tabla de fórmulas y comprobación manual.
- Casos de prueba de filtros, fuentes y gráficos.
- Fragmentos anotados de conexión, consulta, cálculo y dibujo.
- Defensa individual de cinco minutos.

## Casos de prueba mínimos

| Caso | Resultado esperado |
|---|---|
| Fuente JSON conocida | Totales coinciden con cálculo manual |
| Segunda fuente | Produce el mismo esquema y resultado |
| Módulo + estado | Tabla, indicadores y gráficos se sincronizan |
| Rango sin resultados | Estado vacío, no error ni gráfico antiguo |
| Registro incompleto | Se comunica y aplica la regla documentada |
| Gráfico | Título, unidad, escala y tabla equivalentes |
| Fallo de red | Estado de error y opción de reintento |
| Impresión | Conserva título, fecha, filtros y datos esenciales |

## Guía de corrección por criterios

| CE | Satisfactorio | Insuficiente |
|---|---|---|
| a | Estructura completa y orientada a una pregunta | Secciones decorativas o sin contexto |
| b | Informes básicos correctos desde dos fuentes y asistente | Datos pegados o una sola fuente sin generación |
| c | Tres filtros sincronizan todas las salidas | Solo ocultan filas visualmente |
| d | Cálculos definidos y comprobados | Totales sin fórmula o conjunto ambiguo |
| e | Gráficos adecuados, etiquetados y verificables | Tipo engañoso o sin alternativa tabular |
| f | Identifica y usa la herramienta que genera la integración | No puede explicar de dónde procede el código |
| g | Cambio acotado con diff y prueba | Reemplazo completo sin trazabilidad |
| h | Aplicación funcional con informe incrustado | Informe aislado sin integración |

## Solución docente orientativa

<details><summary>Mostrar estructura de una solución válida</summary>

El gestor incorpora «Informes» en su navegación. Una única colección filtrada alimenta cuatro indicadores, barras por módulo, línea semanal y tabla numerada. Dos adaptadores normalizan JSON y CSV. La interfaz indica actualización, fuente y filtros; distingue carga, vacío y error. Google Charts dibuja desde agregados comprobados y cada gráfico tiene tabla. La versión imprimible conserva contexto y metodología. El dossier muestra el cambio de columnas a barras sin alterar datos y explica `fetch`, filtro, `reduce`, clase de gráfico y `draw`.

</details>

## Preguntas de defensa

1. ¿Qué pregunta responde el informe y qué elemento aporta la respuesta principal?
2. ¿Cómo sabes que el total es correcto después de filtrar?
3. ¿Qué parte cambiarías para conectar otra fuente?
4. ¿Qué decisión de la IA rechazaste y por qué?
5. ¿Por qué elegiste cada gráfico?

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA5_08_fuentes_consultas.html">← RA5-08</a><a href="https://mosqueteroweb.github.io/damDI/RA5_matriz_contenidos_evaluacion.html">Matriz RA5</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/"><span class="unit-next-card__eyebrow">Volver al curso</span><strong>Índice general del módulo</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
