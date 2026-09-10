# RA1 — Correspondencia entre contenidos, prácticas y criterios de evaluación

**Módulo:** 0488 — Desarrollo de Interfaces (DAM).  
**Destinatario:** profesorado.  
**Versión:** 1.1, 8 de septiembre de 2026.  
**Duración propuesta:** 18 horas de las 100 del módulo.  
**Estado:** diseño curricular de las actividades; no constituye todavía el capítulo de contenidos ni un conjunto de soluciones técnicas ejecutadas.  
**Fuente:** [Relación RA–CE–contenidos proporcionada por el profesor](https://mosqueteroweb.github.io/ismie01/DAM/dam_di_relaciones.html), consultada para esta matriz.

## 1. Reglas de elaboración

**Itinerario acordado: aplicaciones web.** HTML, CSS y JavaScript se leen como ejemplos de salida de IA, sin exigir programación manual. [Material Design 3](https://m3.material.io/) rige el diseño de todo el curso. Android Studio, XML y Java se reservan a anexos voluntarios no evaluables y fuera de las 100 horas.

El índice de contenidos es el de la página de referencia. Se conserva su orden en el documento y solo se desglosan apartados que contienen varios conceptos diferenciados. La secuencia de clase puede recorrerlos en otro orden para facilitar el aprendizaje.

El alumnado conoce Java y no conoce interfaces visuales. Dispone de ordenador individual e Internet. Construirá y modificará las aplicaciones mediante herramientas de IA, sin escribir código desde cero. Deberá localizar y explicar los fragmentos relevantes y comprobar el efecto de las modificaciones.

- Cada concepto de la delimitación siguiente tendrá un ejemplo básico resuelto en los contenidos y una práctica básica sencilla de evaluación con solución docente.
- Habrá un integrador del RA con solución de referencia.
- Los ejemplos resueltos sirven para enseñar: **no acreditan por sí solos cobertura de evaluación**.
- Cada CE debe contar con una tarea y una evidencia en las prácticas básicas o en el integrador.
- Los pesos y reglas de calificación y recuperación permanecen aplazados.
- Las actividades del alumnado dispondrán de archivos iniciales independientes. Reutilizar el contexto no obligará a terminar una práctica para comenzar la siguiente.

## 2. Resultado de aprendizaje y criterios de referencia

**RA1:** Genera interfaces gráficos de usuario mediante editores visuales utilizando las funcionalidades del editor y adaptando el código generado.

La tabla resume los criterios para facilitar su uso; su redacción de referencia se encuentra en la fuente curricular enlazada.

| Identificador | Síntesis del CE |
|---|---|
| RA1.a | Analizar herramientas y librerías disponibles para generar interfaces gráficas. |
| RA1.b | Crear una interfaz mediante herramientas de un editor visual. |
| RA1.c | Utilizar las funciones del editor para ubicar componentes. |
| RA1.d | Modificar propiedades de los componentes según las necesidades de la aplicación. |
| RA1.e | Analizar el código generado por el editor visual. |
| RA1.f | Modificar el código generado por el editor visual. |
| RA1.g | Asociar acciones a eventos. |
| RA1.h | Desarrollar una aplicación que incluya la interfaz obtenida. |

## 3. Índice curricular y actividades previstas

Los títulos de la segunda columna conservan los diez apartados de contenidos básicos de la fuente. Se delimitan trece conceptos didácticos: el apartado 9 se divide en clases, propiedades y métodos; el 10, en eventos y escuchadores. Los restantes se trabajan como conceptos conjuntos con una práctica cada uno. MVC y MVVM, por ejemplo, serán alternativas comparadas dentro del concepto de arquitectura, no unidades adicionales con proyectos completos.

`EJ` identifica un ejemplo resuelto dentro de los contenidos; `PB`, una práctica básica de evaluación. Todos los identificadores llevan el prefijo `RA1-`.

| Nº | Contenido básico: título del índice | Concepto y ejemplo resuelto previsto | Práctica de evaluación | CE que aporta a evaluar |
|---:|---|---|---|---|
| 1 | Patrones de arquitectura de las aplicaciones gráficas. | Arquitectura: localizar vista, datos y coordinación en una pantalla de tareas; comparación introductoria MVC/MVVM. EJ01. | PB01. Mapa de responsabilidades. | e |
| 2 | Librerías de componentes nativas y multiplataforma. Características. | Librerías: comparar dos alternativas de componentes para un mismo formulario. EJ02. | PB02. Elegir una librería. | a |
| 3 | Herramientas propietarias y libres de edición de interfaces. | Herramientas: comparar diseño con IA y edición visual, incluyendo una herramienta libre de contraste. EJ03. | PB03. Crear y distribuir un formulario en el editor. | a, b, c |
| 4 | Lenguajes descriptivos para la definición de interfaces. | Descripción de interfaz: relacionar estructura declarativa, contenedores e identificadores con una pantalla. EJ04. | PB04. Leer el plano de una pantalla. | e |
| 5 | Componentes: características y campo de aplicación. | Selección de componentes: elegir campos, botones y controles de selección para una tarea. EJ05. | PB05. Elegir los controles adecuados. | b, d |
| 6 | Enlace de componentes a orígenes de datos. | Enlace de datos: seguir cómo una colección preparada alimenta una lista. EJ06. | PB06. Mostrar y actualizar datos. | e, f |
| 7 | Asociación de acciones a eventos. | Asociación: seguir la pulsación de un botón hasta la acción y su resultado. EJ07. | PB07. Conectar una acción. | g |
| 8 | Edición del código generado por la herramienta de diseño. | Cambio asistido: pedir a Gemini una modificación localizada del código exportado y revisar las diferencias. EJ08. | PB08. Modificar sin romper la interfaz. | e, f |
| 9 | Clases, propiedades, métodos. | Clases: reconocer el papel de una clase de pantalla y de una clase de datos. EJ09. | PB09. Identificar clases y responsabilidades. | e |
| 9 | Clases, propiedades, métodos. | Propiedades: relacionar texto, estado y otras propiedades con lo que ve el usuario. EJ10. | PB10. Cambiar propiedades. | d |
| 9 | Clases, propiedades, métodos. | Métodos: identificar nombre, entrada, efecto y llamadas de un método. EJ11. | PB11. Explicar un método de la interfaz. | e |
| 10 | Eventos; escuchadores. | Eventos: distinguir qué ocurre al pulsar, cambiar un valor o seleccionar un elemento. EJ12. | PB12. Reconocer y elegir eventos. | g |
| 10 | Eventos; escuchadores. | Escuchadores: localizar registro, callback y acción; reconocer el problema de una asociación duplicada. EJ13. | PB13. Localizar y corregir un escuchador. | e, f, g |

Las letras de la última columna se refieren a RA1. Son aportaciones de las prácticas al criterio; la matriz de la sección 6 concreta qué demuestra cada evidencia. RA1.h se evalúa en el integrador.

## 4. Fichas de las prácticas básicas

Cada ficha es una especificación para redactar posteriormente el enunciado completo y su solución reproducible. Los resultados esperados de este documento no sustituyen los archivos ni las pruebas de una solución técnica.

### RA1-PB01 — Mapa de responsabilidades

- **Tiempo:** 15 minutos.
- **Punto de partida:** aplicación generada y preparada por el profesor, con una pantalla y una pequeña colección de tareas.
- **Tarea:** señalar qué fragmentos representan la interfaz, los datos y la coordinación entre ambos. Explicar qué parte debería cambiar si se modifica el aspecto, manteniendo los datos.
- **Lectura de código:** tres fragmentos breves con sus archivos de origen.
- **Entrega:** mapa archivo–responsabilidad–efecto y una explicación propia.
- **CE:** RA1.e; se analiza expresamente el código procedente del editor en el fragmento de la vista.
- **Resultado esperado:** distingue presentación, datos y coordinación; no confunde una etiqueta visible con el valor almacenado.

### RA1-PB02 — Elegir una librería

- **Tiempo:** 20 minutos.
- **Punto de partida:** fichas y documentación seleccionada de una librería nativa y otra multiplataforma.
- **Tarea:** comparar plataformas, componentes disponibles y adecuación a un formulario sencillo; justificar una elección.
- **Lectura de código:** reconocer en ejemplos proporcionados la importación o referencia a la librería y un componente que utiliza.
- **Entrega:** tabla comparativa, referencias y decisión razonada.
- **CE:** RA1.a, parte relativa a librerías.
- **Resultado esperado:** diferencia herramienta de generación, editor y librería; entiende que pedir M3 a una IA no identifica la librería utilizada.

### RA1-PB03 — Crear y distribuir un formulario en el editor

- **Tiempo:** 35 minutos.
- **Punto de partida:** entorno preparado y boceto sencillo de una pantalla de alta de tareas.
- **Tarea:** comparar brevemente una herramienta propietaria y una libre a partir de fichas proporcionadas; crear la pantalla en el editor visual elegido, insertar componentes y cambiar su distribución con las funciones del editor.
- **Lectura de código:** localizar los identificadores y el contenedor correspondiente a la distribución creada.
- **Entrega:** comparación breve, archivo editable, capturas antes/después y explicación de las operaciones del editor realizadas.
- **CE:** RA1.a, RA1.b y RA1.c.
- **Resultado esperado:** existe una interfaz editable y se demuestra la colocación mediante herramientas del editor. Un mockup o una captura final aislada no bastan.

### RA1-PB04 — Leer el plano de una pantalla

- **Tiempo:** 20 minutos.
- **Punto de partida:** pantalla creada por un editor y su descripción declarativa.
- **Tarea:** relacionar cinco elementos de la pantalla con los fragmentos que los describen, identificar la jerarquía de contenedores y predecir el efecto de un cambio mostrado por el profesor.
- **Lectura de código:** estructura, identificadores y atributos; distinguir descripción de interfaz y lógica de comportamiento.
- **Entrega:** correspondencias anotadas y predicción justificada.
- **CE:** RA1.e.
- **Resultado esperado:** reconoce la relación entre jerarquía declarativa y distribución visual sin tener que escribirla.

### RA1-PB05 — Elegir los controles adecuados

- **Tiempo:** 25 minutos.
- **Punto de partida:** formulario incompleto de título, prioridad y estado de una tarea.
- **Tarea:** completar los controles en el editor y configurar propiedades sencillas. Justificar por qué cada control responde al dato o acción solicitados.
- **Lectura de código:** tipo de componente, identificador y propiedad relevante.
- **Entrega:** pantalla editable, relación requisito–control y propiedades modificadas.
- **CE:** RA1.b y RA1.d.
- **Resultado esperado:** el formulario usa controles adecuados y las propiedades tienen un propósito verificable.

### RA1-PB06 — Mostrar y actualizar datos

- **Tiempo:** 30 minutos.
- **Punto de partida:** lista visual y colección local preparada; no requiere servidor ni base de datos.
- **Tarea:** identificar el origen de datos y su enlace con la lista. Pedir a la IA que modifique el enlace o plantilla de representación generados para mostrar también la prioridad; comprobar la actualización al cambiar un dato.
- **Lectura de código:** colección, enlace o mecanismo de actualización y representación de cada elemento.
- **Entrega:** fragmentos inicial y final, petición, captura de la lista y explicación del recorrido del dato.
- **CE:** RA1.e y RA1.f, sobre el fragmento generado del enlace o representación que se haya modificado.
- **Resultado esperado:** se muestra la prioridad real de cada elemento y se explica por qué el cambio llega a la pantalla; no se acepta texto fijo simulando datos.

### RA1-PB07 — Conectar una acción

- **Tiempo:** 25 minutos.
- **Punto de partida:** formulario con un botón sin comportamiento.
- **Tarea:** pedir a Gemini que asocie la pulsación con la lectura del título y un mensaje de confirmación. Probar dos títulos distintos.
- **Lectura de código:** botón, evento, asociación, lectura del valor y acción.
- **Entrega:** fragmento de la conexión, explicación de la cadena y dos pruebas.
- **CE:** RA1.g.
- **Resultado esperado:** el mensaje utiliza el valor introducido y el alumno puede seguir la cadena desde la pulsación.

### RA1-PB08 — Modificar sin romper la interfaz

- **Tiempo:** 25 minutos.
- **Punto de partida:** código generado y exportado desde el editor visual con un formulario funcional.
- **Tarea:** pedir un cambio localizado del texto de ayuda y de la disposición de dos elementos, conservando sus identificadores y las acciones existentes.
- **Lectura de código:** diferencias del archivo declarativo generado y referencias que deben conservarse.
- **Entrega:** versión inicial, instrucción, versión final, diferencias comentadas y prueba del comportamiento conservado.
- **CE:** RA1.e y RA1.f.
- **Resultado esperado:** modifica el código de origen sin sustituir todo el proyecto; explica las diferencias y verifica que el formulario sigue funcionando.

### RA1-PB09 — Identificar clases y responsabilidades

- **Tiempo:** 15 minutos.
- **Punto de partida:** fragmentos sencillos de clases de pantalla, componentes y datos.
- **Tarea:** distinguir clase e instancia y explicar qué responsabilidad tiene cada clase en la aplicación.
- **Lectura de código:** declaración, instancia y relación con los elementos de la interfaz generada.
- **Entrega:** tres correspondencias y una explicación sobre qué clase se relaciona con un elemento visible.
- **CE:** RA1.e, cuando se analiza la clase o referencia generada por el editor.
- **Resultado esperado:** aprovecha los conocimientos de Java sin confundir un objeto de datos con un control visual. Si el proyecto principal no usa clases explícitas, se proporcionará un microejemplo generado de una clase JavaScript que sí permita estudiarlas, aprovechando la comparación con Java; no se requerirá Android.

### RA1-PB10 — Cambiar propiedades

- **Tiempo:** 15 minutos.
- **Punto de partida:** pantalla editable con controles ya colocados.
- **Tarea:** cambiar texto, valor inicial y estado habilitado de controles según tres requisitos, utilizando el editor o cambios asistidos.
- **Lectura de código:** propiedad, valor y componente al que pertenece.
- **Entrega:** tabla requisito–propiedad–valor y captura del resultado.
- **CE:** RA1.d.
- **Resultado esperado:** diferencia propiedades de apariencia, contenido y comportamiento y comprueba sus efectos.

### RA1-PB11 — Explicar un método de la interfaz

- **Tiempo:** 15 minutos.
- **Punto de partida:** método breve que limpia los campos o muestra una confirmación, dentro de una solución generada.
- **Tarea:** identificar su nombre, parámetros si existen, efecto y punto desde el que se llama; predecir qué ocurriría si no se invocara.
- **Lectura de código:** declaración del método y llamada desde el código de interacción.
- **Entrega:** explicación anotada y comprobación de la predicción con una variante preparada.
- **CE:** RA1.e; se incluirá el punto de llamada o referencia del código generado por el editor, no solo una función aislada de otro origen.
- **Resultado esperado:** distingue definir un método de ejecutarlo.

### RA1-PB12 — Reconocer y elegir eventos

- **Tiempo:** 15 minutos.
- **Punto de partida:** pantalla preparada con botón, campo y selector.
- **Tarea:** distinguir tres eventos y pedir que una actualización se produzca al cambiar la selección, en lugar de depender de un botón de confirmación.
- **Lectura de código:** evento seleccionado y acción asociada.
- **Entrega:** tabla interacción–evento–acción y prueba de la asociación solicitada.
- **CE:** RA1.g.
- **Resultado esperado:** la acción ocurre en el momento requerido y el alumno identifica el evento que la provoca.

### RA1-PB13 — Localizar y corregir un escuchador

- **Tiempo:** 20 minutos.
- **Punto de partida:** pequeña aplicación con una asociación duplicada preparada por el profesor.
- **Tarea:** localizar los registros del escuchador, explicar por qué la acción se ejecuta dos veces y pedir a la IA una corrección localizada.
- **Lectura de código:** registro, callback y acción; distinguir el suceso del mecanismo que responde.
- **Entrega:** diagnóstico, petición, diferencias del código y prueba antes/después.
- **CE:** RA1.e, RA1.f y RA1.g; la variante contendrá la conexión generada desde el editor para que e/f tengan evidencia pertinente.
- **Resultado esperado:** cada interacción provoca una sola acción y la explicación identifica la duplicación real.

## 5. RA1-INT01 — Gestor sencillo de tareas de aula

### 5.1 Alcance

Una aplicación web de una pantalla con título de tarea, selector de prioridad, botón de añadir, lista de tareas y acción para limpiar el formulario. Datos en memoria: no se requieren autenticación, nube, persistencia ni distribución. El contexto es propio de este RA, no un proyecto transversal obligatorio.

**Duración de evaluación:** 150 minutos, más revisión y explicación individual dentro del tiempo docente reservado. El alumnado recibe el entorno y un proyecto base vacío ejecutable, sin la interfaz resuelta.

### 5.2 Tareas y evidencias

| Tarea | Trabajo del alumno | Evidencia | CE |
|---|---|---|---|
| T1 | Comparar dos herramientas y dos librerías utilizando las fichas trabajadas y justificar la elección. | Tabla breve con diferencias y decisión. | a |
| T2 | Crear la interfaz con el editor visual a partir de un boceto propio o generado con Stitch. | Proyecto editable y captura de la creación. | b |
| T3 | Distribuir y reubicar los controles mediante funciones del editor. | Dos estados de distribución y operaciones identificadas. | c |
| T4 | Ajustar propiedades a los requisitos: etiquetas, opciones y estados. | Tabla de propiedades y resultado. | d |
| T5 | Localizar y explicar el contenedor, dos componentes, el enlace de datos y la conexión de un evento. | Fragmentos del código generado por el editor anotados y explicación propia. | e |
| T6 | Solicitar una modificación delimitada del código generado, conservar el original y revisar diferencias. | Antes/después, prompt, explicación y verificación. | f |
| T7 | Asociar añadir y limpiar con sus acciones mediante IA. | Conexiones identificadas y pruebas de ambos botones. | g |
| T8 | Ejecutar la aplicación completa y demostrar el recorrido de alta y visualización de tareas. | Proyecto ejecutable e informe de pruebas. | h |

### 5.3 Comprobaciones funcionales mínimas

1. Al añadir una tarea con título y prioridad, aparece en la lista con los valores introducidos.
2. Al añadir otra, la anterior se conserva durante la ejecución.
3. Un título vacío produce un mensaje claro y no añade una tarea vacía.
4. Limpiar restablece el formulario sin borrar las tareas de la lista.
5. La modificación de T6 conserva los eventos y el funcionamiento anterior.

### 5.4 Lectura guiada y solución docente futura

El alumno debe señalar dónde se describe la pantalla, qué representa el dato de una tarea, cómo llega a la lista, dónde se asocian los eventos y qué cambió en T6. No necesita explicar todas las dependencias del proyecto.

El solucionario incluirá proyecto completo, versión inicial y modificada, prompts orientativos, capturas, fragmentos explicados, respuestas a las preguntas y resultados de las cinco comprobaciones. Se admitirán nombres y estructuras diferentes cuando cumplan los requisitos y el alumno pueda justificarlos.

## 6. Matriz de cobertura de evaluación

| CE | Prácticas básicas que aportan evidencia | Evidencia del integrador | Condición para considerar cubierto el criterio |
|---|---|---|---|
| RA1.a | PB02 y PB03 conjuntamente | T1 | Análisis tanto de herramientas como de librerías; una lista de nombres no basta. |
| RA1.b | PB03, PB05 | T2 | Interfaz creada con herramientas del editor visual y archivo editable. |
| RA1.c | PB03 | T3 | Operaciones de ubicación realizadas con funciones del editor, documentadas. |
| RA1.d | PB05, PB10 | T4 | Propiedades modificadas según requisitos y efecto comprobado. |
| RA1.e | PB01, PB04, PB06, PB08, PB09, PB11, PB13 | T5 | Análisis propio de fragmentos procedentes del editor, vinculados a la pantalla o a sus conexiones. |
| RA1.f | PB06, PB08, PB13 | T6 | Modificación efectiva del código generado por el editor, conservando antes/después y verificando el resultado. |
| RA1.g | PB07, PB12, PB13 | T7 | Asociación concreta entre evento y acción, identificada y probada. |
| RA1.h | Se reserva al integrador | T8 | Aplicación ejecutable que incorpora y utiliza la interfaz obtenida. |

**Resultado de la planificación:** los ocho CE tienen evidencia prevista en evaluación. La cobertura efectiva se verificará al redactar y ejecutar las soluciones. La presencia de una etiqueta CE no sustituye la tarea requerida.

## 7. Distribución de las 18 horas

| Uso del tiempo | Minutos | Horas |
|---|---:|---:|
| Explicación y 13 ejemplos básicos resueltos, con lectura de código | 450 | 7 h 30 min |
| 13 prácticas básicas de evaluación | 275 | 4 h 35 min |
| Integrador | 150 | 2 h 30 min |
| Revisión, explicaciones individuales y puesta en común | 145 | 2 h 25 min |
| Acceso al entorno y margen de incidencias | 60 | 1 h |
| **Total** | **1080** | **18 h** |

Los minutos de cada PB suman 275. Los 450 minutos de explicación incluyen la exposición de conceptos y la demostración docente, no solo la ejecución de los ejemplos. La revisión puede distribuirse entre las actividades; no implica 145 minutos de entrevistas individuales por alumno.

### Secuencia didáctica propuesta

Se conserva el índice curricular en la documentación, pero se propone impartir los conceptos en este orden:

1. Herramientas, librerías y primera creación visual: apartados 3 y 2, PB03 y PB02.
2. Componentes, descripción y propiedades: apartados 5, 4 y parte de 9, PB05, PB04 y PB10.
3. Clases, métodos y arquitectura: resto de 9 y apartado 1, PB09, PB11 y PB01.
4. Datos e interacción: apartados 6, 10 y 7, PB06, PB12, PB07 y PB13.
5. Modificación controlada: apartado 8, PB08.
6. Integrador y revisión.

Los proyectos iniciales y fichas preparados son necesarios para que las actividades breves sean viables. No se dedicará el tiempo del alumnado a construir infraestructura auxiliar.

## 8. Herramientas y condiciones de implementación

- **Stitch:** propuesta visual inicial.
- **Gemini:** explicación, generación de lógica y cambios localizados.
- **Google AI Studio:** generación y experimentación funcional cuando encaje con el formato de proyecto.
- **Editor visual complementario:** se seleccionará una ruta que permita crear, ubicar, configurar y exportar código de interfaz de manera comprobable. Se validará una herramienta de edición visual web para las operaciones que no queden cubiertas por las herramientas de Google. Android Studio no forma parte de esta ruta obligatoria.

No es obligatorio usar todas las herramientas en todas las prácticas. Se evitará que el alumno mantenga varias implementaciones equivalentes para un mismo ejercicio. El boceto de Stitch podrá servir de referencia visual: no se presupone una importación automática ni compatibilidad de exportación sin comprobarla.

### Prueba técnica previa a la redacción de soluciones

1. Crear una pantalla en el editor elegido y ubicar sus controles con funciones visuales.
2. Identificar el archivo generado, modificarlo mediante IA y comprobar su coherencia con el editor.
3. Asociar un evento, enlazar una colección local y ejecutar la aplicación.
4. Confirmar que los fragmentos resultan comprensibles para alumnado que conoce Java.
5. Conservar una versión de referencia para que las actividades no dependan de obtener la misma respuesta de IA.

Si una herramienta únicamente genera una imagen o código a partir de prompts, no se utilizará como única evidencia de RA1.b y RA1.c. La selección técnica es responsabilidad de la preparación docente y no requiere volver a pedir al profesor que elija un lenguaje.

## 9. Criterios de redacción de los materiales siguientes

- Redactar los contenidos siguiendo los diez títulos curriculares de la sección 3.
- Incluir los trece ejemplos y las trece prácticas previstos; si surge un concepto nuevo independiente, asignarle práctica y reajustar el tiempo antes de ampliar el alcance.
- Separar enunciados de soluciones de evaluación, aunque la publicación prevista esté destinada al profesorado.
- Explicar la sintaxis necesaria y relacionarla con lo conocido de Java.
- Mostrar fragmentos breves del proyecto real y su localización, evitando pseudocódigo presentado como código ejecutado.
- Etiquetar cada práctica con CE, tarea y evidencia.
- No declarar probadas las soluciones hasta ejecutar la ruta técnica y registrar los resultados.
- Mantener Markdown como fuente, compatible con una futura web estática en GitHub Pages.

## 10. Comprobación de esta matriz

- [x] Se conservan los diez apartados de contenidos básicos de RA1.
- [x] Se delimitan trece conceptos con un ejemplo y una práctica por concepto.
- [x] Se proyecta un integrador autónomo.
- [x] Los ocho CE tienen tareas y evidencias de evaluación previstas.
- [x] Los ejemplos docentes no se contabilizan como evaluación.
- [x] Todas las prácticas incluyen lectura del código relevante.
- [x] La propuesta suma 18 horas.
- [ ] Validar la ruta técnica y las soluciones ejecutables.
- [ ] Redactar los contenidos, enunciados y solucionarios completos.