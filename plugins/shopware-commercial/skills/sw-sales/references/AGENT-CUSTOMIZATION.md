# Sales Agent — Customization

Full reference: [AGENT-CUSTOMIZATION-CUSTOMIZATION.md](AGENT-CUSTOMIZATION-CUSTOMIZATION.md)

## Core principle: Nuxt layers

Sales Agent uses the **Nuxt layer concept**. The default layer `sales-agent`
remains untouched. Customizations are made in your own layer.
An example layer `example` ships with the source code.

## Quick overview

| Topic | Approach |
|-------|---------|
| Favicon | `public/favicon.ico` in your own layer |
| App title | `nuxt.config.ts` → `app.head.title` |
| Primary color | override the CSS variable `--color-interaction-primary-default` |
| Override a component | copy the file from `layers/sales-agent/` into your own layer |
| Override i18n | `nuxt.config.ts` + `i18n/src/langs/` in your own layer |
