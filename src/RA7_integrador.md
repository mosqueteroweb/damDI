---
layout: default
title: RA7-INT01 · Release candidata del gestor
---

# RA7-INT01 · Release candidata del gestor

## Situación

El gestor ya ha sido probado y documentado. El centro necesita una versión que pueda instalarse, verificarse, actualizarse y retirarse sin depender del equipo que la creó.

## Encargo

Prepara una release candidata web/PWA. Parte de configuraciones y scripts generados con Stitch, Gemini y Google AI Studio; identifica cada fragmento, elimina supuestos falsos, ejecútalo y conserva evidencia real.

## Requisitos obligatorios

1. Inventario de componentes, versiones, licencias y exclusiones del paquete.
2. ZIP versionado con compilación limpia y PWA instalable.
3. Generación desde tarea del IDE y desde herramienta externa o CI.
4. Experiencia de instalación personalizada con M3, idioma, cancelación y error.
5. Firma digital del artefacto y verificación positiva y negativa.
6. Instalación desatendida con registro y fallo seguro.
7. Pruebas de instalación, actualización y desinstalación, incluidos datos locales.
8. Plan de Pages, Release y un canal restringido, con retirada y actualización.

## Entregables

- Ficha de versión, commit y entorno.
- Manifiesto de componentes y licencias.
- Artefacto, hash, firma e instrucciones de verificación.
- Configuración del IDE y cadena externa anotadas.
- Prototipo Stitch y textos definitivos del asistente.
- Registros del ciclo limpio y modo desatendido.
- Matriz canal–audiencia–versión–actualización–retirada.
- Registro de correcciones a la salida de IA y defensa individual.

## Casos de prueba mínimos

| Caso | Resultado esperado |
|---|---|
| Compilación limpia | Produce el artefacto identificado sin archivos de trabajo ni secretos |
| Instalación PWA | La aplicación queda instalada desde un perfil limpio |
| Firma original | La verificación identifica el artefacto como íntegro |
| Copia alterada | La verificación falla de forma visible |
| Modo desatendido | Termina sin preguntas y conserva registro y código de salida |
| Actualización | Mantiene la versión esperada y declara qué ocurre con los datos |
| Desinstalación | Retira aplicación y caché según la política documentada |
| Canal alternativo | Define audiencia, actualización y retirada, no solo una URL |

## Guía de corrección por criterios

| CE | Satisfactorio | Insuficiente |
|---|---|---|
| a | Paquete contiene solo componentes requeridos y trazados | Copia la carpeta de trabajo |
| b | Asistente personalizado, claro y accesible | Cambia solo un logotipo |
| c | El IDE genera un paquete verificable | Captura sin artefacto |
| d | Herramienta externa reproduce la salida | Depende de pasos manuales ocultos |
| e | Firma original válida y copia alterada inválida | Presenta solo un hash |
| f | Cadena no interactiva y fallo no nulo | Requiere respuestas manuales |
| g | Retirada comprobada y datos explicados | Confunde cerrar con desinstalar |
| h | Canales tienen audiencia y ciclo de versión | Enumera canales sin estrategia |

## Solución docente orientativa

<details><summary>Mostrar estructura de una solución válida</summary>

La versión `1.0.0-rc.1` se compila desde un bloqueo de dependencias y genera un ZIP sin secretos. La tarea del IDE y CI llaman al mismo script. El manifiesto permite instalar la PWA; Stitch muestra estados accesibles. El ZIP se firma y la copia modificada falla. CI ejecuta sin preguntas y detiene la publicación si fallan pruebas. El ciclo en perfil limpio registra instalación, actualización, desinstalación y estado de datos. Pages es canal principal, Releases conserva artefactos y ad-hoc limita el piloto; cada canal define retirada.

</details>

## Preguntas de defensa

1. ¿Qué archivos excluiste del paquete y por qué?
2. ¿Cómo demuestras que las dos rutas de generación producen el mismo artefacto?
3. ¿Qué diferencia existe entre hash y firma digital?
4. ¿Qué ocurre con los datos después de actualizar y desinstalar?
5. ¿Por qué elegiste cada canal y cómo retirarías una versión defectuosa?

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/RA7_06_firma_canales.html">← RA7-06</a><a href="https://mosqueteroweb.github.io/damDI/RA7_matriz_contenidos_evaluacion.html">Matriz RA7</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/"><span class="unit-next-card__eyebrow">Curso completo</span><strong>Volver al índice general</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
