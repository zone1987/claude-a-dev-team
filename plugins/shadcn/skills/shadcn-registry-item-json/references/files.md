# registry-item.json: files[] Field

## Structure

Each entry in `files` has three properties:

| Property | Required | Description                                          |
|----------|----------|------------------------------------------------------|
| `path`   | Yes      | Path to the source file in your registry             |
| `type`   | Yes      | File type (see types.md)                             |
| `target` | Conditional | Where to place the file in the consuming project |

`target` is required for `registry:page` and `registry:file` types. It is
optional for other types.

## Path resolution

In a single-file `registry.json`, `path` is relative to the project root.
When using `include`, `path` is relative to the `registry.json` file that
declares the item.

## target placeholders

Use target placeholders to place files under the directories configured by the
consumer's `components.json`. Placeholders are only supported at the START of
the `target` string.

| Placeholder    | Resolves to (`components.json`)  |
|----------------|----------------------------------|
| `@components/` | `aliases.components`             |
| `@ui/`         | `aliases.ui`                     |
| `@lib/`        | `aliases.lib`                    |
| `@hooks/`      | `aliases.hooks`                  |
| `~/`           | Project root                     |

`@utils/` is NOT supported (`utils` points to a file, not a directory).
Unknown placeholders (e.g. `@foo/`) are treated as literal paths.

Placeholders work regardless of the project's import prefix (`@/`, `#`,
package imports, workspace exports).

Anything after the placeholder is preserved:
`@ui/ai/prompt-input.tsx` → installs at `<ui-dir>/ai/prompt-input.tsx`

```json
{
  "files": [
    {
      "path": "registry/default/example/button.tsx",
      "type": "registry:ui",
      "target": "@ui/button.tsx"
    },
    {
      "path": "registry/default/example/prompt-input.tsx",
      "type": "registry:ui",
      "target": "@ui/ai/prompt-input.tsx"
    },
    {
      "path": "registry/default/example/card.tsx",
      "type": "registry:component",
      "target": "@components/card.tsx"
    },
    {
      "path": "registry/default/example/helper.ts",
      "type": "registry:lib",
      "target": "@lib/helper.ts"
    },
    {
      "path": "registry/default/example/use-demo.ts",
      "type": "registry:hook",
      "target": "@hooks/use-demo.ts"
    },
    {
      "path": "registry/default/example/.env",
      "type": "registry:file",
      "target": "~/.env"
    }
  ]
}
```

## target vs type

The `target` decides where the file is WRITTEN. It can point to a different
shadcn directory than the file `type`. For example, a `registry:ui` file can
be installed into the `@lib/` directory:

```json
{
  "files": [
    {
      "path": "registry/default/example/format-date.ts",
      "type": "registry:ui",
      "target": "@lib/format-date.ts"
    }
  ]
}
```

Source: registry/registry-item-json.mdx
