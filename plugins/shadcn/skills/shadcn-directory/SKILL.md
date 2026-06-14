---
name: shadcn-directory
description: shadcn Registry Directory — Verzeichnis öffentlicher Registries, Namespaces auflösen und eintragen. Trigger: shadcn directory, shadcn registry directory, third-party registries, shadcn namespaces.
---

# shadcn-directory

The shadcn Registry Directory: a curated, built-in list of open-source
community registries. No configuration required.

## Discovery

Full list: `https://ui.shadcn.com/r/registries.json`

When you run `shadcn add` or `shadcn search`, the CLI automatically checks the
registry index for the given namespace and adds it to `components.json`.

```bash
npx shadcn@latest add @ai-elements/prompt-input
```

## Submit a registry

1. Add your entry to `apps/v4/registry/directory.json` in the shadcn/ui repo.
2. Run `pnpm validate:registries` to validate.
3. Open a pull request to `https://github.com/shadcn-ui/ui`.

## Submission requirements

- Registry must be open source and publicly accessible.
- Must conform to the registry.json schema.
- Must be a flat registry: `/registry.json` and `/component-name.json` files at
  the root.
- `files[]` must NOT include a `content` property in the index.

Note: Public GitHub repositories do NOT need to be listed in the directory to
be usable with `owner/repo/item` addresses. The directory is only for
`@namespace` style registries.

Source: (root)/directory.mdx, registry/registry-index.mdx
