# shadcn/registry, shadcn/schema, shadcn/preset APIs

Install the `shadcn` package as a runtime dependency:

```bash
npm install shadcn
```

---

## shadcn/registry

### Common options

All functions accept these optional options:

| Option     | Type             | Default                  | Description                                |
|------------|------------------|--------------------------|--------------------------------------------|
| `config`   | `Partial<Config>`| built-in registries only | Resolved `components.json` for namespaces  |
| `useCache` | `boolean`        | `true`                   | In-memory process cache; set `false` for long-running servers |

### getRegistry

Fetch a single registry by name.

```ts
import { getRegistry } from "shadcn/registry"

const registry = await getRegistry("@acme", { config, useCache: true })
```

### getRegistryItems

Fetch one or more registry items by qualified name.

```ts
import { getRegistryItems } from "shadcn/registry"

const items = await getRegistryItems(["@acme/button", "@acme/card"], {
  config,
  useCache: true,
})
```

Returns an array of registry items with `files[].content` inlined.

### resolveRegistryItems

Like `getRegistryItems` but recursively walks `registryDependencies` and merges
everything — files, dependencies, CSS variables — into a single installable
tree.

```ts
import { resolveRegistryItems } from "shadcn/registry"

const tree = await resolveRegistryItems(
  ["@acme/button", "@acme/card", "@acme/dialog"],
  { config }
)
```

Returns a single merged object with `files[]`, `dependencies[]`,
`cssVars`, and `docs`.

### getRegistries

Fetch the registry directory (list of all indexed namespaces).

```ts
import { getRegistries } from "shadcn/registry"

const registries = await getRegistries({ useCache: true })
// [{ name: "@shadcn", url: "...", homepage: "..." }, ...]
```

### searchRegistries

Fuzzy-search across one or more registries.

```ts
import { searchRegistries } from "shadcn/registry"

const results = await searchRegistries(["@shadcn"], {
  query: "button",
  types: ["registry:component"],
  limit: 100,
  offset: 0,
  config,
  continueOnError: true,
})
// { pagination: { total, offset, limit, hasMore }, items: [...] }
```

### loadRegistry (server-side)

Read and resolve a local `registry.json` from disk, following `include`
references. Returns catalog without file contents.

```ts
import { loadRegistry } from "shadcn/registry"

const catalog = await loadRegistry({
  cwd: process.cwd(),       // default: process.cwd()
  registryFile: "registry.json", // default: "registry.json"
})
```

### loadRegistryItem (server-side)

Read a single item from a local `registry.json` by name, with file contents
read from disk and inlined.

```ts
import { loadRegistryItem, RegistryItemNotFoundError } from "shadcn/registry"

const item = await loadRegistryItem("login-form", { cwd: process.cwd() })
```

### Error classes

All functions throw typed errors extending `RegistryError`:

- `RegistryError`
- `RegistryNotFoundError`
- `RegistryUnauthorizedError`
- `RegistryForbiddenError`
- `RegistryFetchError`
- `RegistryNotConfiguredError`
- `RegistryLocalFileError`
- `RegistryParseError`
- `RegistryValidationError`
- `RegistryItemNotFoundError`
- `RegistriesIndexParseError`
- `RegistryMissingEnvironmentVariablesError`
- `RegistryInvalidNamespaceError`

---

## shadcn/schema

Zod schemas for validating registry JSON:

```ts
import { registryItemSchema, registrySchema } from "shadcn/schema"

const result = registryItemSchema.safeParse(json)
if (!result.success) {
  console.error(result.error)
}
```

### Key schemas

- `registrySchema`
- `registryItemSchema`
- `registryItemFileSchema`
- `registryItemTypeSchema`
- `registryItemCssVarsSchema`
- `registryItemTailwindSchema`
- `registryBaseColorSchema`
- `configSchema`
- `presetSchema`

### Inferred TypeScript types

- `Registry`
- `RegistryItem`
- `RegistryBaseItem`
- `RegistryFontItem`
- `Preset`
- `ConfigJson`

---

## shadcn/preset

### encodePreset

Encode a `Partial<PresetConfig>` into a URL-safe preset code.

```ts
import { encodePreset } from "shadcn/preset"

const code = encodePreset({
  style: "vega",
  baseColor: "stone",
  theme: "blue",
  radius: "large",
  font: "geist",
})
// "bJ4FLU0"
```

### decodePreset

Decode a preset code back into a full `PresetConfig`. Returns `null` if invalid.

```ts
import { decodePreset } from "shadcn/preset"

const config = decodePreset("bJ4FLU0")
// { style, baseColor, theme, chartColor, iconLibrary, font, fontHeading,
//   radius, menuAccent, menuColor }
```

### Other exports

Functions:
- `isPresetCode`, `isValidPreset`
- `generateRandomConfig`, `generateRandomPreset`
- `toBase62`, `fromBase62`

Constants:
- `PRESET_BASES`, `PRESET_STYLES`, `PRESET_BASE_COLORS`, `PRESET_THEMES`
- `PRESET_ICON_LIBRARIES`, `PRESET_FONTS`, `PRESET_FONT_HEADINGS`
- `PRESET_RADII`, `PRESET_MENU_ACCENTS`, `PRESET_MENU_COLORS`
- `PRESET_CHART_COLORS`, `DEFAULT_PRESET_CONFIG`

Source: registry/api-reference.mdx
