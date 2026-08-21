---
name: contao-frontend
description: Contao 5 frontend: content elements, frontend modules, fragment controllers, Twig templates, insert tags, widgets. Use when building a Contao content element or frontend module.
---

# Contao frontend

Everything rendered to a visitor. Content elements and frontend modules are both fragment controllers with a Twig template.

## Reference map

- **[CONTENT-ELEMENTS.md](references/CONTENT-ELEMENTS.md)**: content elements: the basic components, a minimal implementation, every service-tag option, and both registration methods.
- **[MODULES.md](references/MODULES.md)**: front-end modules, the same ground as content elements where the two differ.
- **[FRAGMENT-CONTROLLERS.md](references/FRAGMENT-CONTROLLERS.md)**: the fragment concept, the built-in types, extending legacy classes, and sub-requests with their caching.
- **[TEMPLATES.md](references/TEMPLATES.md)**: the Twig system in 528 lines: `ContaoFilesystemLoader`, naming and scoping, the component pattern, debugging, and legacy interop.
- **[TWIG-REFERENCE.md](references/TWIG-REFERENCE.md)**: every Twig function, filter, global, tag and Contao Twig component, 705 lines.
- **[WIDGETS-REFERENCE.md](references/WIDGETS-REFERENCE.md)**: every form widget with its DCA `eval` options: `checkbox`, `fileTree`, `imageSize`, `inputUnit` and the rest.
- **[INSERT-TAGS.md](references/INSERT-TAGS.md)**: registering an insert tag (Contao 5.2 and later), simple and block tags, and flags.
- **[ASSET-MANAGEMENT.md](references/ASSET-MANAGEMENT.md)**: the global arrays, adding CSS and JavaScript, and the template helper functions.
- **[STIMULUS-CONTROLLERS.md](references/STIMULUS-CONTROLLERS.md)**: the five lifecycle callbacks including Contao's
  own `beforeCache()`, why cleanup in `disconnect()` does not reach the cache, and the four ways to keep
  a DOM transformation idempotent.
- **[IMAGE-PROCESSING.md](references/IMAGE-PROCESSING.md)**: `ImageFactory`, `PictureFactory`, the size-array format, and image sizes from the database.

## Source

Distilled from [docs.contao.org/5.x](https://docs.contao.org/5.x) : the developer documentation and the German end-user manual : plus the [contao/contao](https://github.com/contao/contao) source, retrieved 2026-08-20.
