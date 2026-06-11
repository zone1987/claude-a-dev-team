---
name: sw-theme
description: Scaffold eines Storefront-Themes in Shopware 6 (Theme-Plugin mit theme.json, ThemeInterface, SCSS/JS-Struktur und Config-Feldern).
argument-hint: <ThemeName> [--owner Ff|Adt|Ag|Pb]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-theme

Erzeuge ein Theme-Plugin. Skills: `sw-theme`, `sw-theme-config`, `sw-theme-inheritance`.

## Ablauf
1. ThemeName (PascalCase mit Owner-Präfix) bestimmen.
2. Plugin-Basis erzeugen (wie `/sw-plugin-create`), Plugin-Klasse implementiert zusätzlich `ThemeInterface`.
3. `src/Resources/theme.json` mit `views`/`style`/`script`/`asset` (jeweils mit `@Storefront` zuerst) und
   `config.fields` (Farben/Fonts/Switches).
4. SCSS-Einstieg `src/Resources/app/storefront/src/scss/base.scss`, JS-Einstieg, Vorschaubild `preview.png`.
5. Hinweis: `bin/console theme:change` + `theme:compile`.

Reihenfolge in den Arrays = Override-Priorität. Nur Bootstrap-Utilities importieren (kein doppeltes CSS).
