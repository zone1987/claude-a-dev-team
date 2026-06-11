---
name: sw-api-gen-types
description: >
  TypeScript-Typen für Shopware-Frontends generieren mit @shopware/api-gen: OpenAPI-Schema laden (loadSchema) und
  Typen erzeugen (generate), eigene/Plugin-Endpunkte einbeziehen, #shopware Alias. Trigger: "@shopware/api-gen",
  "api types generieren", "shopware-api-gen", "loadSchema generate", "openapi typescript shopware", "#shopware types".
  Shopware Frontends.
---

# Shopware Frontends — @shopware/api-gen

Generiert TypeScript-Typen (`operations`, `Schemas`) aus der OpenAPI-Spec des Shops — Grundlage der Typsicherheit
des `api-client`.

```bash
# Schema vom Shop laden (Store-API, APP_ENV=dev) und Typen generieren
npx @shopware/api-gen loadSchema --apiType=store --url=https://shop.example.com
npx @shopware/api-gen generate --apiType=store
```

Erzeugt z.B. `api-types/storeApiTypes.d.ts`, im Projekt als `#shopware`-Alias eingebunden. Bei installierten Plugins
mit eigenen Store-API-Routen das Schema neu laden, damit deren Endpunkte typisiert sind (Bezug: `shopware-api` →
`sw-api-catalog`/`sw-store-api-route`). `--apiType=admin` für Admin-Typen.

→ Vollständige Referenz: [references/deep/api-gen-reference.md](references/deep/api-gen-reference.md)
