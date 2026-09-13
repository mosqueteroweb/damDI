# Auditoría de contenidos sin línea de comandos

Fecha: 13 de septiembre de 2026

## Alcance revisado

- 57 unidades de contenido de RA1–RA8.
- 8 ejercicios integradores.
- Guías docentes, matrices de trazabilidad, portada y README.
- 66 imágenes didácticas y el anexo voluntario de Android.

## Criterio aplicado

El itinerario obligatorio se centra en aplicaciones web, SPA y PWA creadas con IA generativa. Las acciones del alumnado se realizan desde editores, navegadores, grabadores, paneles y plataformas web. El desarrollo móvil nativo se conserva únicamente en su ampliación opcional.

## Cambios realizados

| Bloque | Sustitución |
|---|---|
| RA3-02 | Manipulación desde consola → panel visual de propiedades generado con IA |
| RA3-03 | Registro en consola → panel de actividad dentro de la aplicación |
| RA3-07 | Gestión de paquetes mediante npm → descarga/exportación desde editor web |
| RA6 | Generación documental mediante comando y Pandoc → acción visual de generación, validación y publicación |
| RA7-01 | Script de compilación y ZIP → versión web/PWA exportada o publicada desde interfaz |
| RA7-03 | IDE frente a terminal → editor web con IA frente a interfaz web del repositorio |
| RA7-05 | Cadena no interactiva con códigos de salida → actualización automatizada con estados y bloqueos visibles |
| RA7-06 | Firma con herramientas de consola → servicio visual de firma didáctica |
| RA7 integrador | Scripts, CI y modo desatendido → publicación visual, automatización verificable y PWA |
| RA8 | Playwright, k6 y ZAP como ejecución técnica → grabador visual, panel de carga y auditoría pasiva visual |

## Revisión de imágenes

- Conservadas: 64 imágenes. Explican arquitectura, componentes, accesibilidad, IA, datos, informes, documentación, distribución y pruebas sin depender de una línea de comandos.
- Sustituida `RA7-03`: la original mostraba una terminal. La nueva muestra dos rutas visuales de publicación.
- Sustituida `RA7-05`: la original mostraba consola y código de salida. La nueva representa el ciclo completo de una PWA desde el navegador.
- Conservada la imagen del anexo Android porque pertenece expresamente a una ampliación voluntaria.
- Las nuevas imágenes incluyen texto alternativo y pie coherentes con el contenido revisado.

## Comprobaciones finales pendientes antes de publicar

1. Regenerar o sincronizar los HTML sin perder las figuras ya integradas.
2. Comprobar que cada HTML coincide con su Markdown revisado.
3. Ejecutar la auditoría de enlaces, imágenes, navegación y responsive.
4. Revisar visualmente las páginas RA7-03 y RA7-05 con las imágenes nuevas.
5. Publicar solo después de validar el diff final.

