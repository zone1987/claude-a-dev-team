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

- `BREADCRUMB-INSTALLATION.md` — CLI and manual install
- `BREADCRUMB-SOURCE.md` — full component source (Radix + Base)
- `BREADCRUMB-API.md` — all sub-component props
- `BREADCRUMB-EXAMPLES.md` — demo, separator, dropdown, ellipsis, link, responsive
- `BREADCRUMB-BASE-VS-RADIX.md` — render prop vs asChild for BreadcrumbLink
