# Pagination — API Reference

## Composition

```text
Pagination
└── PaginationContent
    ├── PaginationItem
    │   └── PaginationPrevious
    ├── PaginationItem
    │   └── PaginationLink
    ├── PaginationItem
    │   └── PaginationEllipsis
    └── PaginationItem
        └── PaginationNext
```

## Pagination

Semantic `<nav role="navigation" aria-label="pagination">` wrapper. `mx-auto flex w-full justify-center`.

## PaginationContent

`<ul>` with `flex flex-row items-center gap-1`.

## PaginationItem

Plain `<li>` wrapper.

## PaginationLink

Anchor tag styled as a Button. Active page gets `variant="outline"` and `aria-current="page"`.

| Prop       | Type      | Default  | Description                              |
| ---------- | --------- | -------- | ---------------------------------------- |
| `isActive` | `boolean` | `false`  | Highlights as current page               |
| `size`     | Button size | `"icon"` | Button size variant from `buttonVariants` |
| `href`     | `string`  |          | Navigation target                        |

### Next.js integration

To use Next.js `<Link>`, update the type and element in `pagination.tsx`:

```diff
+ import Link from "next/link"

- type PaginationLinkProps = ... & React.ComponentProps<"a">
+ type PaginationLinkProps = ... & React.ComponentProps<typeof Link>

const PaginationLink = ({...}: PaginationLinkProps) => (
  <PaginationItem>
-   <a ...>
+   <Link ...>
-   </a>
+   </Link>
  </PaginationItem>
)
```

## PaginationPrevious

Pre-built previous button with `ChevronLeftIcon`. Text label hidden on small screens.

| Prop | Type | Description |
| ---- | ---- | ----------- |
| `text` | `string` | Override "Previous" label (RTL support) |

## PaginationNext

Pre-built next button with `ChevronRightIcon`. Text label hidden on small screens.

| Prop | Type | Description |
| ---- | ---- | ----------- |
| `text` | `string` | Override "Next" label (RTL support) |

## PaginationEllipsis

`<span aria-hidden>` with `MoreHorizontalIcon` and a screen-reader-only "More pages" label.

---
Source: `content/docs/components/base/pagination.mdx`
