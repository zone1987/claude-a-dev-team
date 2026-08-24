---
name: sw-theme
description: Scaffolds a storefront theme in Shopware 6 (a theme plugin with theme.json, ThemeInterface, the SCSS and JS structure, and config fields).
argument-hint: <ThemeName> [--owner Ff|Adt|Ag|Pb]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-theme

Produce a theme plugin. Skill: `sw-theme`.

## Steps
1. Settle the theme name (PascalCase with an owner prefix).
2. Create the plugin base (as `/sw-plugin-create` does); the plugin class also implements
   `ThemeInterface`.
3. `src/Resources/theme.json` with `views`, `style`, `script` and `asset` (each listing `@Storefront`
   first) plus `config.fields` (colours, fonts, switches).
4. The SCSS entry point `src/Resources/app/storefront/src/scss/base.scss`, the JS entry point, and a
   `preview.png`.
5. Note the follow-up: `bin/console theme:change` and `theme:compile`.

Order within those arrays is override priority. Import only the Bootstrap utilities you need, so the
CSS is not duplicated.
