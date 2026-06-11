# @shopware/api-gen — Vollständige CLI & API-Referenz

Version: **1.5.0**

CLI-Tool und Node.js-API zum Generieren typsicherer TypeScript-Definitionen aus dem Shopware OpenAPI-Schema.

---

## Installation

```bash
npm install --save-dev @shopware/api-gen
```

---

## CLI-Befehle

Das Binary lautet `api-gen` (nach Installation via `npx @shopware/api-gen ...`).

### Übersicht

```bash
npx @shopware/api-gen <command> [options]

Commands:
  loadSchema    Schema vom Shopware-Shop herunterladen
  generate      TypeScript-Typen aus dem Schema generieren
  validateJson  Lokales Schema validieren
  split         Schema in Teildateien aufteilen
```

---

### `loadSchema` — Schema herunterladen

```bash
npx @shopware/api-gen loadSchema --apiType=store
npx @shopware/api-gen loadSchema --apiType=admin
```

**Optionen:**

| Option | Typ | Beschreibung |
|---|---|---|
| `--apiType` | `store` \| `admin` | API-Typ |
| `--cwd` / `-C` | `string` | Arbeitsverzeichnis (default: `process.cwd()`) |
| `--filename` | `string` | Ausgabedateiname (default: `storeApiSchema.json` / `adminApiSchema.json`) |
| `--url` | `string` | Override für Shop-URL |

**Ausgabe:** `api-types/storeApiSchema.json` oder `api-types/adminApiSchema.json`

**Erforderliche Umgebungsvariablen:**

Für Store-API:
```env
OPENAPI_JSON_URL=https://shop.example.com
OPENAPI_ACCESS_KEY=SWSC...
```

Für Admin-API (password grant):
```env
OPENAPI_JSON_URL=https://shop.example.com
SHOPWARE_ADMIN_USERNAME=admin
SHOPWARE_ADMIN_PASSWORD=shopware
```

Für Admin-API (client_credentials):
```env
OPENAPI_JSON_URL=https://shop.example.com
SHOPWARE_ADMIN_CLIENT_ID=SWIA...
SHOPWARE_ADMIN_CLIENT_SECRET=mySecret
```

---

### `generate` — TypeScript-Typen generieren

```bash
npx @shopware/api-gen generate --apiType=store
npx @shopware/api-gen generate --apiType=admin
```

**Optionen:**

| Option | Typ | Beschreibung |
|---|---|---|
| `--apiType` | `store` \| `admin` | Welches Schema generieren |
| `--cwd` / `-C` | `string` | Arbeitsverzeichnis |
| `--filename` | `string` | Eingabedateiname (default: Schema-Dateiname) |
| `--debug` | `boolean` | Debug-Output aktivieren |
| `--logPatches` | `boolean` | Patch-Anwendung loggen |

**Eingabe:** `api-types/storeApiSchema.json` (lokal) oder Fallback auf eingebundene Standard-Schemata.

**Ausgabe:** `api-types/storeApiTypes.d.ts` oder `api-types/adminApiTypes.d.ts`

Die generierten Dateien exportieren:
- `operations` — alle Store-/Admin-API-Operationen
- `components` — alle Schema-Komponenten
- `Schemas` = `components["schemas"]` — einzelne Shopware-Entitäten

---

### `validateJson` — Schema validieren

```bash
npx @shopware/api-gen validateJson --apiType=store
```

Validiert das lokale Schema gegen:
1. Konfigurierte Regeln (z.B. `COMPONENTS_API_ALIAS` — prüft dass jede Komponente ein korrektes `apiAlias`-Enum hat)
2. Vergleich der Pfade mit den Live-API-Endpunkten des Shops (via `/_info/routes`)

Meldet:
- Endpunkte die im Schema fehlen (im Live-Shop aber vorhanden)
- Endpunkte die im Schema sind aber nicht im Live-Shop

---

### `split` — Schema aufteilen

```bash
npx @shopware/api-gen split --apiType=store --list tags
npx @shopware/api-gen split --apiType=store --filterBy "Cart,Checkout"
```

**Optionen:**

| Option | Typ | Beschreibung |
|---|---|---|
| `--list` | `tags` \| `paths` | Auflistungsmodus |
| `--filterBy` | `string` | Kommaseparierte Tags/Pfade |
| `--verbose-linting` | `boolean` | Ausführlicheres Linting |

---

## Konfigurationsdatei `api-gen.config.json`

Optional im Projektroot. Ermöglicht JSON-Overrides/Patches für das Schema.

```json
{
  "store": {
    "patches": ["./api-types/patches/store-patches.json"],
    "rules": {
      "COMPONENTS_API_ALIAS": true
    }
  },
  "admin": {
    "patches": ["./api-types/patches/admin-patches.json"]
  }
}
```

**Format eines Patch-Files (`OverridesSchema`):**

```json
{
  "components": {
    "Cart": [
      {
        "properties": {
          "customField": { "type": "string" }
        }
      }
    ]
  },
  "paths": {
    "/checkout/cart": {
      "post": [
        {
          "requestBody": {
            "content": {
              "application/json": {
                "schema": {
                  "properties": {
                    "myParam": { "type": "boolean" }
                  }
                }
              }
            }
          }
        }
      ]
    }
  }
}
```

**Spezielles `_DELETE_`-Schlüsselwort:** Felder im Patch mit `"_DELETE_": true` werden aus dem Schema entfernt.

---

## Generierte Typen — Struktur

### `operations`

Jede API-Operation wird als Typ exportiert:

```ts
// Beispiel (vereinfacht aus generierten storeApiTypes.d.ts)
export type operations = {
  "readProduct post /product": {
    body?: {
      limit?: number
      page?: number
      filter?: Array<{ type: string; field: string; value: unknown }>
      // ...
    }
    response: {
      elements?: Array<components["schemas"]["Product"]>
      total?: number
      // ...
    }
    responseCode: 200
  }

  "readProductDetail post /product/{productId}": {
    pathParams: { productId: string }
    body?: { /* criteria */ }
    response: components["schemas"]["ProductDetailResponse"]
    responseCode: 200
  }
}
```

### `Schemas` / `components["schemas"]`

```ts
// Verwendung
import type { Schemas } from '#shopware'

const product: Schemas["Product"]
const cart: Schemas["Cart"]
const category: Schemas["Category"]
```

---

## `#shopware`-Alias einrichten

### Nuxt (empfohlen)

Das `@shopware/nuxt-module` richtet den Alias automatisch ein. Eine lokale `shopware.d.ts` im Projektroot überschreibt die Standard-Typen:

```ts
// shopware.d.ts — eigene Typen/Erweiterungen
import type { operationsType } from './api-types/storeApiTypes'
import type { components } from './api-types/storeApiTypes'

declare module '#shopware' {
  type operations = operationsType
  type Schemas = components['schemas']
}
```

### Vite / andere Frameworks

```ts
// vite.config.ts
import { resolve } from 'path'

export default {
  resolve: {
    alias: {
      '#shopware': resolve('./api-types/storeApiTypes.d.ts')
    }
  }
}
```

### TypeScript `paths`

```json
// tsconfig.json
{
  "compilerOptions": {
    "paths": {
      "#shopware": ["./api-types/storeApiTypes.d.ts"]
    }
  }
}
```

---

## Empfohlener Workflow

```bash
# 1. Schema laden (einmalig oder nach Shopware-Update)
OPENAPI_JSON_URL=https://shop.example.com OPENAPI_ACCESS_KEY=SWSC... \
  npx @shopware/api-gen loadSchema --apiType=store

# 2. Typen generieren
npx @shopware/api-gen generate --apiType=store

# 3. In package.json-Scripts eintragen:
```

```json
{
  "scripts": {
    "generate-types": "api-gen loadSchema --apiType=store && api-gen generate --apiType=store"
  }
}
```

---

## Programmatische API (Node.js)

```ts
import { generate, loadSchema, validateJson } from '@shopware/api-gen'

// Schema laden
await loadSchema({
  cwd: process.cwd(),
  apiType: 'store',
  filename: 'storeApiSchema.json'
})

// Typen generieren
await generate({
  cwd: process.cwd(),
  apiType: 'store',
  debug: false,
  logPatches: false
})

// Schema validieren
await validateJson({
  cwd: process.cwd(),
  apiType: 'store'
})
```

---

## Schema-Patch-Mechanismus

`patchJsonSchema` wird intern aufgerufen um das Schema vor der Generierung zu modifizieren:

1. **Pflichtfelder**: `requestBody.required` wird auf `true` gesetzt (Shopware-Standard)
2. **Patches anwenden**: Tiefes Merge der Patch-Arrays per Komponente/Pfad
3. **Outdated-Erkennung**: Patches die bereits im Schema enthalten sind werden als "outdated" gemeldet
4. **`_DELETE_`-Support**: Schlüssel mit `_DELETE_: true` werden aus dem Schema entfernt

---

## Custom Transform-Hooks

`api-gen` wendet beim Generieren automatisch folgende Transformationen an:

- `format: "binary"` → TypeScript-Typ `Blob`
- Bare `object`-Typen → `GenericRecord` (vermeidet `Record<string, unknown>`)
- Felder mit `translated`-Property + String-Feldern → typisiertes `translated`-Objekt

---

## Validation-Regeln

### `COMPONENTS_API_ALIAS`

Prüft dass jede Komponente ein korrektes `apiAlias`-Enum-Feld hat:
- `CmsBlock` → `"cms_block"`
- `ProductManufacturer` → `"product_manufacturer"`

Meldet Abweichungen und schlägt den korrekten Wert vor.
