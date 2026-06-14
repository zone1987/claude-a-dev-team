# Registry Item Types

The `type` field determines the item category and the default target directory
when the CLI installs the item.

## Item-level types

| Type                 | Description                                       |
|----------------------|---------------------------------------------------|
| `registry:base`      | Entire design systems (base style layer)          |
| `registry:block`     | Complex components spanning multiple files        |
| `registry:component` | Simple single-purpose components                  |
| `registry:font`      | Font definitions (requires `font` field)          |
| `registry:lib`       | Library utilities and helpers                     |
| `registry:hook`      | React hooks                                       |
| `registry:ui`        | UI components and single-file primitives          |
| `registry:page`      | Page or file-based routes                         |
| `registry:file`      | Miscellaneous files                               |
| `registry:style`     | Registry styles (e.g. `new-york`)                 |
| `registry:theme`     | Themes                                            |
| `registry:item`      | Universal registry items (cross-framework)        |

## File-level types

Every entry in `files[]` also requires a `type`. You can mix types within one
item.

```json
{
  "files": [
    {
      "path": "registry/default/hello-world/page.tsx",
      "type": "registry:page",
      "target": "app/hello/page.tsx"
    },
    {
      "path": "registry/default/hello-world/hello-world.tsx",
      "type": "registry:component"
    },
    {
      "path": "registry/default/hello-world/use-hello-world.ts",
      "type": "registry:hook"
    },
    {
      "path": "registry/default/hello-world/.env",
      "type": "registry:file",
      "target": "~/.env"
    }
  ]
}
```

`registry:page` and `registry:file` require an explicit `target`.

Source: registry/registry-item-json.mdx
