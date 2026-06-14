---
name: shadcn-registry
description: Eigene shadcn-kompatible Code-Registry bauen & hosten — Struktur, registry.json, Build, Verteilung. Trigger: shadcn registry bauen, custom registry, eigene Komponenten-Registry, host shadcn registry, getting started registry.
---

# shadcn-registry

Build and host your own shadcn-compatible code registry.

## Overview

A registry distributes custom components, hooks, pages, config, rules and any
other files to any project via the `shadcn` CLI. It can be a Next.js app, a
Vite/Vue/PHP project, or any HTTP server — even a public GitHub repository with
a root `registry.json`. Works with React and non-React frameworks.

## References

- [structure.md](references/structure.md) — Single vs. `include`-based layout, add an item, guidelines
- [serve.md](references/serve.md) — Static JSON build vs. dynamic route handlers, content negotiation
- [test-publish.md](references/test-publish.md) — CLI test commands (URL and namespace), publishing

## Quick-start

```bash
# Generate static registry JSON into public/r/
npx shadcn@latest build

# Test the built registry
npx shadcn@latest list http://localhost:3000/r/registry.json
npx shadcn@latest add  http://localhost:3000/r/button.json
```

Source: registry/index.mdx, registry/getting-started.mdx
