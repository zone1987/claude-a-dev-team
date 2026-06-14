# Namespaced Registries

Configure multiple registries in `components.json` under the `registries` key.
Each namespace starts with `@`.

## Basic configuration (URL template)

```json title="components.json"
{
  "registries": {
    "@v0": "https://v0.dev/chat/b/{name}",
    "@acme": "https://registry.acme.com/resources/{name}.json"
  }
}
```

`{name}` is required and is replaced by the item name.
`{style}` is optional and is replaced by the project's style setting.

## Advanced configuration (with auth)

```json title="components.json"
{
  "registries": {
    "@private": {
      "url": "https://api.company.com/registry/{name}.json",
      "headers": {
        "Authorization": "Bearer ${REGISTRY_TOKEN}",
        "X-API-Key": "${API_KEY}"
      },
      "params": {
        "version": "latest"
      }
    }
  }
}
```

`${VAR_NAME}` values are expanded from `process.env` at runtime — never stored.

## CLI commands for namespaces

```bash
# Register a namespace in components.json
npx shadcn@latest registry add @acme=https://acme.com/r/{name}.json

# Add items
npx shadcn@latest add @acme/button @acme/card

# List all items in a namespace
npx shadcn@latest list @acme

# Search a namespace
npx shadcn@latest search @acme --query "auth"

# View item payload
npx shadcn@latest view @acme/button
```

## Namespace vs GitHub registry

| Use case                         | Approach           |
|----------------------------------|--------------------|
| Public GitHub repo               | `owner/repo/item`  |
| Stable alias / custom hosting    | `@namespace/item`  |
| Private repo or auth required    | namespace only     |

## Dependency resolution

1. Parse `@namespace/item` — extract namespace and item name.
2. Look up namespace in `components.json`.
3. Build URL by replacing `{name}` (and `{style}`).
4. Apply auth headers / params.
5. Fetch item JSON.
6. Validate against registry-item.json schema.
7. Recursively resolve `registryDependencies`.
8. Topological sort, deduplicate files (last wins), deep-merge configs.

Resolution order example — last dep wins if same target:

```json
{
  "registryDependencies": [
    "@shadcn/card",
    "@vendor/chart",
    "@custom/card"
  ]
}
```

`@custom/card` overwrites `@shadcn/card` if it targets the same file.

## Organizing multiple registries

```json
{
  "registries": {
    "@acme-ui":     "https://registry.acme.com/ui/{name}.json",
    "@acme-docs":   "https://registry.acme.com/docs/{name}.json",
    "@acme-ai":     "https://registry.acme.com/ai/{name}.json",
    "@acme-themes": "https://registry.acme.com/themes/{name}.json"
  }
}
```

## Error messages

| Situation                 | Error text excerpt                                       |
|---------------------------|----------------------------------------------------------|
| Namespace not configured  | `Unknown registry "@non-existent". Define it in components.json` |
| Missing env var           | `Registry "@private" requires env vars: REGISTRY_TOKEN` |
| Item not found (404)      | `The item at … was not found.`                           |
| Unauthorized (401)        | `You are not authorized to access the item at …`         |
| Forbidden (403)           | `Access forbidden for …`                                 |

Source: registry/namespace.mdx
