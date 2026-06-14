# Registry FAQ

## Complex component example (page + components + hook + lib + config)

```json
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "hello-world",
  "title": "Hello World",
  "type": "registry:block",
  "description": "A complex hello world component",
  "files": [
    { "path": "registry/new-york/hello-world/page.tsx",
      "type": "registry:page", "target": "app/hello/page.tsx" },
    { "path": "registry/new-york/hello-world/components/hello-world.tsx",
      "type": "registry:component" },
    { "path": "registry/new-york/hello-world/components/formatted-message.tsx",
      "type": "registry:component" },
    { "path": "registry/new-york/hello-world/hooks/use-hello.ts",
      "type": "registry:hook" },
    { "path": "registry/new-york/hello-world/lib/format-date.ts",
      "type": "registry:lib" },
    { "path": "registry/new-york/hello-world/hello.config.ts",
      "type": "registry:file", "target": "~/hello.config.ts" }
  ]
}
```

## How do I add a Tailwind color?

Add to `cssVars` under `light` and `dark`. After install, usable as
`bg-brand`, `text-brand-accent`, etc.

```json
{
  "cssVars": {
    "light": { "brand-background": "oklch(0.205 0.015 18)" },
    "dark":  { "brand-background": "oklch(0.205 0.015 18)" }
  }
}
```

## How do I override a Tailwind theme variable?

Add to `cssVars.theme`:

```json
{
  "cssVars": {
    "theme": {
      "text-base": "3rem",
      "ease-in-out": "cubic-bezier(0.4, 0, 0.2, 1)",
      "font-heading": "Poppins, sans-serif"
    }
  }
}
```

## Why does `button` in registryDependencies not use my GitHub repo?

Bare names always resolve to the official shadcn/ui registry. For a
same-repo dep, use the full GitHub address:

```json
{ "registryDependencies": ["acme/ui/button"] }
```

## How do I pin a GitHub registry item?

Add `#ref` (branch, tag, or full commit SHA):

```bash
npx shadcn@latest add acme/ui/button#v1.2.0
npx shadcn@latest add acme/ui/button#c0ffee254729296a45d6691db565cf707a3fef5d
```

For published install commands, prefer tags or full commit SHAs.

## Can GitHub registry addresses use private repos?

No. GitHub addresses support only public `github.com` repositories.
For private registries use a namespace with authenticated URLs.

Source: registry/faq.mdx
