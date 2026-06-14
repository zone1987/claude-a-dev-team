---
name: shadcn-toast
description: >
  shadcn/ui Toast — deprecated, use Sonner instead. Toast notification, Toaster,
  toast success error warning info promise, Benachrichtigungen, Toast deprecated,
  sonner migration, use sonner component, toast component shadcn
---

# shadcn/ui Toast (deprecated)

> The toast component has been deprecated. Use the [Sonner](/docs/components/sonner) component instead.

shadcn/ui now ships the `sonner` component as the recommended toast solution. Sonner is an
opinionated toast component by emilkowalski built on the `sonner` library.

## Quick Reference — Sonner

- **Install**: `npx shadcn@latest add sonner`
- **Deps**: `sonner`, `next-themes`
- **Exports**: `Toaster` (wrapper component)
- **Usage**: `import { toast } from "sonner"` to trigger toasts
- **Place `<Toaster />` once** in your root layout

## Reference files

- [migration.md](references/migration.md) — Deprecation notice and migration guidance
- [sonner-source.md](references/sonner-source.md) — Complete Sonner component source
- [sonner-examples.md](references/sonner-examples.md) — All Sonner examples
