---
name: shadcn-tailwind-v4
description: >
  shadcn/ui with Tailwind v4 — @theme directive, @theme inline, oklch colors,
  migration from v3, forwardRef removal, tw-animate-css, data-slot attribute,
  size-* utility, upgrading existing projects. Use when asked about Tailwind v4,
  Tailwind upgrade, oklch, @theme, shadcn v4, React 19 migration.
---

# shadcn/ui — Tailwind v4

shadcn/ui supports Tailwind v4 and React 19. New projects start with v4.
Existing v3 projects continue to work and upgrade via the official path.

## What's new in shadcn/ui + Tailwind v4

- CLI initialises new projects with Tailwind v4
- Full support for `@theme` directive and `@theme inline` option
- All components updated for Tailwind v4 and React 19
- `forwardRef` removed — components use React 19 ref prop directly
- Every primitive has a `data-slot` attribute for styling
- `toast` component deprecated in favour of `sonner`
- Buttons use default cursor
- `default` style deprecated — new projects use `new-york`
- HSL colors converted to OKLCH

**Non-breaking:** existing Tailwind v3 / React 18 apps still work.
New components added before upgrade remain in v3/R18 syntax until you upgrade.

## Reference files

- [references/upgrade-guide.md](references/upgrade-guide.md)
- [references/changelog.md](references/changelog.md)

Source: `/tmp/shadcn-repo/apps/v4/content/docs/(root)/tailwind-v4.mdx`
