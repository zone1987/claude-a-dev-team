# Pagination — API reference

## Pagination (Root)

Based on reka-ui `PaginationRoot`.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `page` | `number` | — | Current page (controlled) |
| `defaultPage` | `number` | `1` | Start page (uncontrolled) |
| `total` | `number` | — | Total number of entries |
| `itemsPerPage` | `number` | `10` | Entries per page |
| `siblingCount` | `number` | `1` | Number of visible pages next to the current one |
| `showEdges` | `boolean` | `false` | Always show first/last page |
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes |

### Emits

| Event | Type | Description |
|---|---|---|
| `update:page` | `number` | Page change |

### Slot Props

```ts
// v-slot="{ page, pages }"
// pages: Array of { type: 'page' | 'ellipsis', value?: number }
```

---

## PaginationContent

Based on reka-ui `PaginationList`.

### Props

| Prop | Type | Description |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |

### Slot Props

```ts
// v-slot="{ items }"
```

---

## PaginationItem

Based on reka-ui `PaginationListItem`.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `value` | `number` | — | Page number |
| `isActive` | `boolean` | `false` | Active page (outline variant) |
| `size` | `ButtonVariants["size"]` | `"icon"` | Button size |
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes |

---

## PaginationEllipsis

### Props

| Prop | Type | Description |
|---|---|---|
| `index` | `number` | Unique position (required) |
| `class` | `HTMLAttributes["class"]` | Additional CSS classes |

---

## PaginationPrevious / PaginationNext / PaginationFirst / PaginationLast

All are based on the corresponding reka-ui primitives.

### Props

| Prop | Type | Default | Description |
|---|---|---|---|
| `size` | `ButtonVariants["size"]` | `"default"` | Button size |
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes |

---

## reka-ui reference
- https://reka-ui.com/docs/components/pagination
