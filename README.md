# Desarrollo de Interfaces — DAM

Web docente del módulo 0488, con itinerario principal de aplicaciones web generadas con IA y Material Design 3.

- [Abrir la web docente](https://mosqueteroweb.github.io/damDI/)
- [Repositorio](https://github.com/mosqueteroweb/damDI)

Android Studio, XML y Java aparecen únicamente como ampliación voluntaria.

## Generación de la web

La web se publica como HTML estático. Los documentos editables están en `src/`
y las páginas se generan localmente con:

```bash
python scripts/build_static.py
```

El archivo `.nojekyll` evita que GitHub vuelva a compilar el contenido. Tras
generar las páginas, basta con subir los cambios de la rama `main`.
