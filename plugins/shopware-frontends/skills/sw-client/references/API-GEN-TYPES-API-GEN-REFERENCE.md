# @shopware/api-gen — Complete CLI & API reference

Version: **1.5.0**

CLI tool and Node.js API for generating type-safe TypeScript definitions from the Shopware OpenAPI schema.

---

## Contents

- [Installation](#installation)
- [CLI commands](#cli-commands)
- [Configuration file `api-gen.config.json`](#configuration-file-api-genconfigjson)
- [Generated types — structure](#generated-types-structure)
- [Setting up the `#shopware` alias](#setting-up-the-shopware-alias)
- [Recommended workflow](#recommended-workflow)
- [Programmatic API (Node.js)](#programmatic-api-nodejs)
- [Schema patch mechanism](#schema-patch-mechanism)
- [Custom transform hooks](#custom-transform-hooks)
- [Validation rules](#validation-rules)

## Installation

```bash
npm install --save-dev @shopware/api-gen
```

---

## CLI commands

The binary is called `api-gen` (after installation via `npx @shopware/api-gen ...`).

### Overview

```bash
npx @shopware/api-gen <command> [options]

Commands:
  loadSchema    Download the schema from the Shopware shop
  generate      Generate TypeScript types from the schema
  validateJson  Validate the local schema
  split         Split the schema into partial files
```

---

### `loadSchema` — download the schema

```bash
npx @shopware/api-gen loadSchema --apiType=store
npx @shopware/api-gen loadSchema --apiType=admin
```

**Options:**

| Option | Type | Description |
|---|---|---|
| `--apiType` | `store` \| `admin` | API type |
| `--cwd` / `-C` | `string` | Working directory (default: `process.cwd()`) |
| `--filename` | `string` | Output file name (default: `storeApiSchema.json` / `adminApiSchema.json`) |
| `--url` | `string` | Override for the shop URL |

**Output:** `api-types/storeApiSchema.json` or `api-types/adminApiSchema.json`

**Required environment variables:**

For the Store API:
```env
OPENAPI_JSON_URL=https://shop.example.com
OPENAPI_ACCESS_KEY=SWSC...
```

For the Admin API (password grant):
```env
OPENAPI_JSON_URL=https://shop.example.com
SHOPWARE_ADMIN_USERNAME=admin
SHOPWARE_ADMIN_PASSWORD=shopware
```

For the Admin API (client_credentials):
```env
OPENAPI_JSON_URL=https://shop.example.com
SHOPWARE_ADMIN_CLIENT_ID=SWIA...
SHOPWARE_ADMIN_CLIENT_SECRET=mySecret
```

---

### `generate` — generate TypeScript types

```bash
npx @shopware/api-gen generate --apiType=store
npx @shopware/api-gen generate --apiType=admin
```

**Options:**

| Option | Type | Description |
|---|---|---|
| `--apiType` | `store` \| `admin` | Which schema to generate |
| `--cwd` / `-C` | `string` | Working directory |
| `--filename` | `string` | Input file name (default: the schema file name) |
| `--debug` | `boolean` | Enable debug output |
| `--logPatches` | `boolean` | Log the patch application |

**Input:** `api-types/storeApiSchema.json` (local) or a fallback to the bundled default schemas.

**Output:** `api-types/storeApiTypes.d.ts` or `api-types/adminApiTypes.d.ts`

The generated files export:
- `operations` — all Store/Admin API operations
- `components` — all schema components
- `Schemas` = `components["schemas"]` — individual Shopware entities

---

### `validateJson` — validate the schema

```bash
npx @shopware/api-gen validateJson --apiType=store
```

Validates the local schema against:
1. Configured rules (e.g. `COMPONENTS_API_ALIAS` — checks that every component has a correct `apiAlias` enum)
2. Comparison of the paths with the live API endpoints of the shop (via `/_info/routes`)

Reports:
- Endpoints that are missing from the schema (but present in the live shop)
- Endpoints that are in the schema but not in the live shop

---

### `split` — split the schema

```bash
npx @shopware/api-gen split --apiType=store --list tags
npx @shopware/api-gen split --apiType=store --filterBy "Cart,Checkout"
```

**Options:**

| Option | Type | Description |
|---|---|---|
| `--list` | `tags` \| `paths` | Listing mode |
| `--filterBy` | `string` | Comma-separated tags/paths |
| `--verbose-linting` | `boolean` | More verbose linting |

---

## Configuration file `api-gen.config.json`

Optional, in the project root. Enables JSON overrides/patches for the schema.

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

**Format of a patch file (`OverridesSchema`):**

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

**Special `_DELETE_` keyword:** fields in the patch carrying `"_DELETE_": true` are removed from the schema.

---

## Generated types — structure

### `operations`

Every API operation is exported as a type:

```ts
// Example (simplified from the generated storeApiTypes.d.ts)
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
// Usage
import type { Schemas } from '#shopware'

const product: Schemas["Product"]
const cart: Schemas["Cart"]
const category: Schemas["Category"]
```

---

## Setting up the `#shopware` alias

### Nuxt (recommended)

The `@shopware/nuxt-module` sets up the alias automatically. A local `shopware.d.ts` in the project root overrides the default types:

```ts
// shopware.d.ts — own types/extensions
import type { operationsType } from './api-types/storeApiTypes'
import type { components } from './api-types/storeApiTypes'

declare module '#shopware' {
  type operations = operationsType
  type Schemas = components['schemas']
}
```

### Vite / other frameworks

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

## Recommended workflow

```bash
# 1. Load the schema (once, or after a Shopware update)
OPENAPI_JSON_URL=https://shop.example.com OPENAPI_ACCESS_KEY=SWSC... \
  npx @shopware/api-gen loadSchema --apiType=store

# 2. Generate types
npx @shopware/api-gen generate --apiType=store

# 3. Add it to the package.json scripts:
```

```json
{
  "scripts": {
    "generate-types": "api-gen loadSchema --apiType=store && api-gen generate --apiType=store"
  }
}
```

---

## Programmatic API (Node.js)

```ts
import { generate, loadSchema, validateJson } from '@shopware/api-gen'

// Load the schema
await loadSchema({
  cwd: process.cwd(),
  apiType: 'store',
  filename: 'storeApiSchema.json'
})

// Generate types
await generate({
  cwd: process.cwd(),
  apiType: 'store',
  debug: false,
  logPatches: false
})

// Validate the schema
await validateJson({
  cwd: process.cwd(),
  apiType: 'store'
})
```

---

## Schema patch mechanism

`patchJsonSchema` is called internally to modify the schema before generation:

1. **Required fields**: `requestBody.required` is set to `true` (the Shopware default)
2. **Apply patches**: deep merge of the patch arrays per component/path
3. **Outdated detection**: patches that are already contained in the schema are reported as "outdated"
4. **`_DELETE_` support**: keys with `_DELETE_: true` are removed from the schema

---

## Custom transform hooks

When generating, `api-gen` automatically applies the following transformations:

- `format: "binary"` → TypeScript type `Blob`
- Bare `object` types → `GenericRecord` (avoids `Record<string, unknown>`)
- Fields with a `translated` property + string fields → typed `translated` object

---

## Validation rules

### `COMPONENTS_API_ALIAS`

Checks that every component has a correct `apiAlias` enum field:
- `CmsBlock` → `"cms_block"`
- `ProductManufacturer` → `"product_manufacturer"`

Reports deviations and suggests the correct value.
