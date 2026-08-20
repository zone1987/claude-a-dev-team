# Breadcrumb — API Reference

## Composition

```
Breadcrumb
└── BreadcrumbList
    ├── BreadcrumbItem
    │   └── BreadcrumbLink
    ├── BreadcrumbSeparator
    ├── BreadcrumbItem
    │   └── BreadcrumbLink
    ├── BreadcrumbSeparator
    └── BreadcrumbItem
        └── BreadcrumbPage
```

## Breadcrumb

Root `<nav aria-label="breadcrumb">` element.

| Prop | Type | Default |
|------|------|---------|
| `className` | `string` | — |

## BreadcrumbList

`<ol>` flex container with wrapping.

| Prop | Type | Default |
|------|------|---------|
| `className` | `string` | — |

## BreadcrumbItem

`<li>` inline-flex wrapper.

| Prop | Type | Default |
|------|------|---------|
| `className` | `string` | — |

## BreadcrumbLink

Clickable anchor. Use `asChild` (Radix) or `render` (Base) for router links.

| Prop | Type | Default |
|------|------|---------|
| `asChild` (Radix) | `boolean` | `false` |
| `render` (Base) | render prop | — |
| `className` | `string` | — |

```tsx
// Radix — Next.js Link
<BreadcrumbLink asChild>
  <Link href="/">Home</Link>
</BreadcrumbLink>

// Base UI — Next.js Link
<BreadcrumbLink render={<Link href="/" />}>Home</BreadcrumbLink>
```

## BreadcrumbPage

Current page — `aria-current="page"`, not clickable.

| Prop | Type | Default |
|------|------|---------|
| `className` | `string` | — |

## BreadcrumbSeparator

Default icon: `ChevronRight`. Override via children.

| Prop | Type | Default |
|------|------|---------|
| `children` | `ReactNode` | chevron icon |
| `className` | `string` | — |

## BreadcrumbEllipsis

Collapsed items indicator (MoreHorizontal icon).

| Prop | Type | Default |
|------|------|---------|
| `className` | `string` | — |

---
Source: `/tmp/shadcn-repo/apps/v4/content/docs/components/radix/breadcrumb.mdx`
