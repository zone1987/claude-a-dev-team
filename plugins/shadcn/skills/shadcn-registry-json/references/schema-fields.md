# registry.json Schema Fields

Schema URL: `https://ui.shadcn.com/schema/registry.json`

## $schema

```json
{ "$schema": "https://ui.shadcn.com/schema/registry.json" }
```

Specifies the JSON Schema. Optional but recommended for IDE validation.

## name

```json
{ "name": "acme" }
```

Name of the registry. Used for data attributes and metadata. Required on the
root `registry.json`.

## homepage

```json
{ "homepage": "https://acme.com" }
```

Homepage of the registry. Used for metadata. Required on the root
`registry.json`.

## include

```json
{
  "include": [
    "components/ui/registry.json",
    "hooks/registry.json"
  ]
}
```

Composes a registry from multiple `registry.json` files. Each value is a
relative path to an explicit `registry.json` file (folder shorthand is NOT
supported). Included files may omit `name` and `homepage`. `shadcn build`
resolves includes and writes a flattened output without `include`.

File `path` values in included files are relative to the declaring file, not
the project root.

Item names must be unique across the entire resolved registry.

## items

```json
{
  "items": [
    {
      "name": "hello-world",
      "type": "registry:block",
      "title": "Hello World",
      "description": "A simple hello world component.",
      "registryDependencies": [
        "button",
        "@acme/input-form",
        "https://example.com/r/foo"
      ],
      "dependencies": ["is-even@3.0.0", "motion"],
      "files": [
        {
          "path": "registry/default/hello-world/hello-world.tsx",
          "type": "registry:component"
        }
      ]
    }
  ]
}
```

Array of registry item definitions. The root `registry.json` must define at
least one of `items` or `include`. If omitted, defaults to `[]`.

Each item conforms to the registry-item.json schema. See the
[registry-item-json skill](../../shadcn-registry-item-json/references/fields.md)
for full field documentation.

## Minimal registry.json

```json
{
  "$schema": "https://ui.shadcn.com/schema/registry.json",
  "name": "acme",
  "homepage": "https://acme.com",
  "items": []
}
```

## Composed registry.json (include only)

```json
{
  "$schema": "https://ui.shadcn.com/schema/registry.json",
  "name": "acme",
  "homepage": "https://acme.com",
  "include": [
    "components/ui/registry.json",
    "hooks/registry.json"
  ]
}
```

Source: registry/registry-json.mdx
