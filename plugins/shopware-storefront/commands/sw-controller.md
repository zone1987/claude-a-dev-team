---
name: sw-controller
description: Scaffold eines Storefront-Controllers in Shopware 6 inkl. Route (routes.xml/#[Route]), PageLoader + Page-Struct und Twig-Template.
argument-hint: <Name> [--plugin <PluginName>] [--path /ff/example]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-controller

Erzeuge einen Storefront-Controller mit Page/PageLoader/Template. Skills: `sw-storefront-controller`,
`sw-page-loader`, `sw-storefront-page`, `sw-twig-templates`.

## Ablauf
1. Name + Ziel-Plugin + Route-Pfad bestimmen; Route-Name `frontend.<owner>.<name>`.
2. Erzeugen:
   - `src/Storefront/Controller/<Name>Controller.php` (extends `StorefrontController`, `_routeScope storefront`).
   - `src/Storefront/Page/<Name>/<Name>Page.php` + `<Name>PageLoader.php` (+ `<Name>PageLoadedEvent`).
   - Template `src/Resources/views/storefront/page/<name>/index.html.twig` (`sw_extends` Base-Layout).
   - Route-Registrierung (`routes.xml` oder `#[Route]`), services.xml für Controller/Loader.
3. Hinweis: ggf. `_httpCache` setzen (`sw-storefront-caching`), Snippets ergänzen.

Daten im PageLoader laden (nicht im Controller). Bestehende Dateien nicht überschreiben.
