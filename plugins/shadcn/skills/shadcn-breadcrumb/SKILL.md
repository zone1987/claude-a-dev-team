---
name: shadcn-breadcrumb
description: >
  shadcn/ui Breadcrumb component — navigation path display. Use when asked
  about Breadcrumb, Brotkruemel, shadcn breadcrumb, Navigationspfad,
  BreadcrumbItem, BreadcrumbLink, BreadcrumbPage, BreadcrumbSeparator,
  BreadcrumbEllipsis, shadcn/ui breadcrumb.
---

# shadcn/ui — Breadcrumb

Displays the path to the current resource using a hierarchy of links. Pure
HTML — no external primitives.

## Sub-components

- `Breadcrumb` — `<nav aria-label="breadcrumb">`
- `BreadcrumbList` — `<ol>` flex container
- `BreadcrumbItem` — `<li>` wrapper
- `BreadcrumbLink` — clickable link (`asChild` / `render` for router links)
- `BreadcrumbPage` — current page (aria-current)
- `BreadcrumbSeparator` — chevron or custom icon
- `BreadcrumbEllipsis` — collapsed items indicator

## Reference files

- `references/installation.md` — CLI and manual install
- `references/source.md` — full component source (Radix + Base)
- `references/api.md` — all sub-component props
- `references/examples.md` — demo, separator, dropdown, ellipsis, link, responsive
- `references/base-vs-radix.md` — render prop vs asChild for BreadcrumbLink
