---
name: sw-sales-agent-customization
description: >
  Anpassung der Sales-Agent-App: Nuxt-Layer-Konzept, Branding (Favicon,
  Titel, CSS-Variablen via Meteor Component Library), Komponenten überschreiben, i18n.
  Triggers: "sales agent anpassen", "customize sales agent", "sales agent branding",
  "sales agent nuxt layer", "sales agent theme color", "sales agent CSS variables",
  "meteor component library sales agent", "sales agent i18n", "sales agent login page"
---

# Sales Agent — Customization

Vollständige Referenz: [references/deep/customization.md](references/deep/customization.md)

## Kernprinzip: Nuxt Layer

Sales Agent nutzt das **Nuxt Layer Konzept**. Der Default-Layer `sales-agent`
bleibt unberührt. Anpassungen erfolgen in einem eigenen Layer.
Ein Beispiel-Layer `example` liegt im Quellcode bei.

## Schnellübersicht

| Thema | Vorgehen |
|-------|---------|
| Favicon | `public/favicon.ico` im eigenen Layer |
| App-Titel | `nuxt.config.ts` → `app.head.title` |
| Primärfarbe | CSS-Variable `--color-interaction-primary-default` überschreiben |
| Komponente überschreiben | Datei aus `layers/sales-agent/` in eigenen Layer kopieren |
| i18n überschreiben | `nuxt.config.ts` + `i18n/src/langs/` im eigenen Layer |
