# Registry Directory (Open-Source Index)

The registry index is a curated list of publicly accessible, open-source
registries. The CLI checks it automatically when you use `@namespace` syntax.

Full list: `https://ui.shadcn.com/r/registries.json`

## How it works

When you run `npx shadcn@latest add @acme/button`, the CLI:

1. Checks `components.json` for a `@acme` namespace definition.
2. If not found, looks up `@acme` in the registry index.
3. Automatically adds the resolved URL template to `components.json`.

GitHub registries (`owner/repo/item` addresses) do NOT need to be in the
index. The index is only for `@namespace` registries.

## Submitting a registry

1. Add entry to `apps/v4/registry/directory.json` in
   `https://github.com/shadcn-ui/ui`
2. Run `pnpm validate:registries`
3. Open a pull request to the shadcn/ui repo

## Submission requirements

1. Registry must be open source and publicly accessible.
2. Must return valid JSON conforming to the registry.json schema.
3. Must be a FLAT registry: `/registry.json` and `/component-name.json` at
   the root — no nested paths.
4. `files[]` in the index MUST NOT include a `content` property.

## Valid index registry example

```json title="registry.json"
{
  "$schema": "https://ui.shadcn.com/schema/registry.json",
  "name": "acme",
  "homepage": "https://acme.com",
  "items": [
    {
      "name": "login-form",
      "type": "registry:component",
      "title": "Login Form",
      "description": "A login form component.",
      "files": [
        {
          "path": "registry/new-york/auth/login-form.tsx",
          "type": "registry:component"
        }
      ]
    }
  ]
}
```

Source: registry/registry-index.mdx
