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

## Registry Directory Details

### What it is

A curated list of open-source community registries that work out of the box
with `shadcn add @namespace/item` syntax. No manual URL configuration needed.

Full JSON list: `https://ui.shadcn.com/r/registries.json`

### How the CLI uses it

When you run `npx shadcn@latest add @ai-elements/prompt-input`:

1. CLI checks `components.json` for a `@ai-elements` registry definition.
2. If not found, looks it up in the directory.
3. Resolves the URL template and adds it to `components.json`.
4. Fetches and installs the item.

### GitHub registries vs directory

Public GitHub repositories (`owner/repo/item` addresses) do NOT need to be
listed in the directory. The directory is only for `@namespace` registries.

### Listing requirements

1. Registry must be open source and publicly accessible.
2. Must return valid JSON conforming to the registry.json schema.
3. Must be a flat registry: `/registry.json` and `/component-name.json` at
   the root.
4. `files[]` in the index must NOT include a `content` property.

### How to submit

1. Add entry to `apps/v4/registry/directory.json` in
   `https://github.com/shadcn-ui/ui`
2. Run `pnpm validate:registries`
3. Open a pull request

### Example usage

```bash
## From a registry in the directory — no components.json config needed
npx shadcn@latest add @ai-elements/prompt-input

## List all items in a directory namespace
npx shadcn@latest list @ai-elements

## Search a directory namespace
npx shadcn@latest search @ai-elements --query "input"
```

Source: (root)/directory.mdx, registry/registry-index.mdx
