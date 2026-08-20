# shadcn-vue Pagination Component

## Triggers
shadcn-vue pagination, pagination vue, seitennavigation vue, pagination component shadcn,
pagination reka-ui vue, page navigation vue, pagination ellipsis vue, pagination first last vue,
pager vue

## Overview

The `Pagination` component renders accessible page navigation built on reka-ui's `PaginationRoot`. It manages current page state, total pages, and exposes slot props for rendering page items. Navigation buttons use `buttonVariants` for consistent sizing.

## Sub-components

| Component | reka-ui Base | Description |
|---|---|---|
| `Pagination` | `PaginationRoot` | Root container with slot props |
| `PaginationContent` | `PaginationList` | Horizontal list of items |
| `PaginationItem` | `PaginationListItem` | Individual page number button |
| `PaginationEllipsis` | `PaginationEllipsis` | "..." placeholder |
| `PaginationPrevious` | `PaginationPrev` | Previous page button |
| `PaginationNext` | `PaginationNext` | Next page button |
| `PaginationFirst` | `PaginationFirst` | First page button |
| `PaginationLast` | `PaginationLast` | Last page button |

## PaginationItem Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `isActive` | `boolean` | `false` | Active page style (outline variant) |
| `size` | `ButtonVariants["size"]` | `"icon"` | Button size |
| All `PaginationListItemProps` | — | — | Forwarded |

## PaginationContent Slot Props

```ts
// from PaginationRoot v-slot
{ pages: PageItemType[], page: number }
```

## reka-ui Reference
https://reka-ui.com/docs/components/pagination

## References
- Source: `PAGINATION-SOURCE.md`
- API: `PAGINATION-API.md`
- Examples: `PAGINATION-EXAMPLES.md`
- Installation: `PAGINATION-INSTALLATION.md`
