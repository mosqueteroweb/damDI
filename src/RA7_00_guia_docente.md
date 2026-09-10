---
layout: default
title: RA7 · Guía docente
---

# RA7 · Distribución de aplicaciones

> **Duración propuesta: 8 horas · Ruta web/PWA · Material Design 3**

## Resultado de aprendizaje

Prepara aplicaciones para su distribución evaluando y utilizando herramientas específicas.

## Producto del RA

El alumnado convierte el gestor web probado y documentado en una entrega identificable, instalable y verificable: inventario de componentes, paquete reproducible, experiencia de instalación, firma, desinstalación y publicación por varios canales. Stitch define la experiencia; Gemini/Google AI Studio generan borradores de configuración y comandos; el alumnado localiza, entiende, ejecuta y explica cada parte relevante, sin programarla desde cero.

## Secuencia docente

| Sesión | Unidad | Horas | Evidencia |
|---:|---|---:|---|
| 1 | Componentes y empaquetado | 1 | Inventario y ZIP versionado |
| 2 | Instaladores y paquetes autoinstalables | 1 | PWA instalable y comprobada |
| 3 | Herramientas de creación | 1 | Paquetes por dos rutas |
| 4 | Personalización | 1 | Asistente coherente con M3 |
| 5 | Instalación, modo desatendido y desinstalación | 1 | Ciclo limpio reproducible |
| 6 | Firma y canales | 1 | Artefacto verificado y plan multicanal |
| 7 | Integrador y defensa | 2 | Release candidata completa |

## Flujo de clase

1. Partir de una versión probada e identificar sus componentes.
2. Pedir a la IA un fragmento pequeño de configuración, nunca credenciales.
3. Localizar entradas, salidas, versión, permisos y comandos.
4. Ejecutar en un entorno limpio y conservar la salida real.
5. Verificar integridad, instalación, actualización y retirada.
6. Explicar qué generó la IA, qué se corrigió y por qué.

## Herramientas

- **Stitch:** pantallas y estados de instalación, actualización y retirada.
- **Gemini / Google AI Studio:** borradores explicados de manifiestos, scripts y listas de comprobación.
- **Navegador y DevTools:** instalación PWA, almacenamiento, caché y responsive.
- **npm y Vite:** dependencias bloqueadas y compilación web; complemento justificado por su salida reproducible.
- **GitHub Actions, Releases y Pages:** automatización, artefactos y canales diferenciados.
- **GPG o Sigstore Cosign:** firma/verificación sin publicar claves privadas.
- **Material Design 3:** identidad, textos, estados y accesibilidad del flujo.

## Evaluación

Las nueve prácticas básicas aportan al menos una evidencia por cada contenido; el integrador reúne los ocho criterios. No basta entregar un ZIP: se exige procedencia, versión, hash o firma, instalación limpia, modo desatendido, desinstalación, canales y evidencia de verificación.

## Preparación del profesor

- Proporcionar una versión estable del gestor y datos ficticios.
- Preparar un perfil de navegador limpio y una release con un fallo intencionado.
- No introducir secretos reales en prompts, repositorios ni capturas.
- Usar firmas didácticas o identidades efímeras controladas.
- Mantener Android Studio, XML, Java y empaquetado nativo como ampliación voluntaria.

<nav class="unit-nav" aria-label="Navegación entre unidades"><div class="unit-nav__secondary"><a href="https://mosqueteroweb.github.io/damDI/">← Inicio</a><a href="https://mosqueteroweb.github.io/damDI/RA7_matriz_contenidos_evaluacion.html">Matriz RA7</a></div><a class="unit-next-card" href="https://mosqueteroweb.github.io/damDI/RA7_01_componentes_empaquetado.html"><span class="unit-next-card__eyebrow">Primera unidad</span><strong>RA7-01 · Componentes y empaquetado</strong><span class="unit-next-card__arrow" aria-hidden="true">→</span></a></nav>
