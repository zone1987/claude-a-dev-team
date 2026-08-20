# shadcn-rtl

First-class RTL (right-to-left) support for shadcn/ui: Arabic, Hebrew, Persian
and any other RTL language. The CLI auto-converts physical CSS classes to CSS
logical equivalents on install.

## References

- [concepts.md](`RTL-CONCEPTS.md`) — How RTL works, migrations, animations, font recommendations
- [next.md](`RTL-NEXT.md`) — Next.js setup
- [vite.md](`RTL-VITE.md`) — Vite setup
- [start.md](`RTL-START.md`) — TanStack Start setup

## Enable RTL in a new project

```bash
# Next.js
npx shadcn@latest create --template next --rtl

# Vite
npx shadcn@latest create --template vite --rtl

# TanStack Start
npx shadcn@latest create --template start --rtl
```

Sets `"rtl": true` in `components.json`.

## Migrate existing components

```bash
npx shadcn@latest migrate rtl [path]
```

## DirectionProvider (Next.js layout)

```tsx
import { DirectionProvider } from "@/components/ui/direction"

<html lang="ar" dir="rtl">
  <body>
    <DirectionProvider direction="rtl">{children}</DirectionProvider>
  </body>
</html>
```

## Supported styles

Automatic CLI transformation only for projects using `shadcn create` with the
new styles (`base-nova`, `radix-nova`, etc.).

Source: rtl/index.mdx, rtl/next.mdx, rtl/vite.mdx, rtl/start.mdx
