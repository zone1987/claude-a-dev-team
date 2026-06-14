---
name: shadcn-vue-breadcrumb
description: >
  shadcn-vue Breadcrumb component (Vue-Port von shadcn/ui, reka-ui Primitive, Tailwind v4, SFC .vue).
  Triggers: "shadcn-vue breadcrumb", "breadcrumb vue", "breadcrumb nuxt",
  "navigation pfad vue", "breadcrumb komponente vue",
  "pfadnavigation vue", "breadcrumb trail vue", "navigations-pfad anzeigen vue"
---

# shadcn-vue: Breadcrumb

A navigation component that displays the current page's location within a hierarchy,
helping users understand where they are and navigate back up the tree.
Built with semantic HTML (`<nav>`, `<ol>`, `<li>`) and full WAI-ARIA support.

## Sub-Components

- `Breadcrumb` — Root `<nav aria-label="breadcrumb">` container
- `BreadcrumbList` — `<ol>` wrapper with flex layout and muted text color
- `BreadcrumbItem` — `<li>` for each navigation segment (link or current page)
- `BreadcrumbLink` — Anchor element using reka-ui `Primitive`; supports `asChild` for custom routers (NuxtLink, RouterLink)
- `BreadcrumbPage` — `<span>` marking the current page with `aria-current="page"` and `aria-disabled="true"`
- `BreadcrumbSeparator` — `<li role="presentation" aria-hidden="true">` with default ChevronRight icon; accepts custom slot content
- `BreadcrumbEllipsis` — `<span role="presentation" aria-hidden="true">` with MoreHorizontal icon for collapsed paths

## Key Features

- **Custom separator** — Replace the default `ChevronRight` by passing content into `BreadcrumbSeparator`'s default slot (e.g. `<SlashIcon />`)
- **Dropdown support** — Wrap a `DropdownMenu` inside a `BreadcrumbItem` to show collapsed intermediate pages
- **asChild links** — Use `BreadcrumbLink as-child` to render framework-native links (NuxtLink, RouterLink) without extra DOM wrappers
- **Ellipsis for collapse** — Use `BreadcrumbEllipsis` to indicate hidden intermediate segments on small screens
- **Fully accessible** — `aria-label`, `aria-current="page"`, `aria-hidden`, `role="presentation"` wired correctly out of the box

## Reference Files

- `references/installation.md` — CLI and manual installation steps
- `references/source.md` — Complete Vue source code for all 7 component files + index.ts
- `references/api.md` — Props, accessibility attributes, and asChild notes per sub-component
- `references/examples.md` — All demo examples with full code (basic, dropdown, custom links)
