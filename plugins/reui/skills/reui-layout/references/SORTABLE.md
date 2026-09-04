# Sortable

Custom Shadcn Sortable for React and Tailwind CSS. A drag-and-drop sortable component designed for
seamless item reordering with vertical, grid, and nested layouts. Built on dnd-kit.

Free component — no licence key required.

## Contents

- [Installation](#installation)
- [Import](#import)
- [Usage](#usage)
- [Examples (3 total, titles enumerated upstream)](#examples-3-total-titles-enumerated-upstream)
- [Persisting order](#persisting-order)
- [API Reference](#api-reference)
- [Base UI vs Radix UI](#base-ui-vs-radix-ui)
- [Source](#source)

## Installation

```
pnpm dlx shadcn@latest add @reui/sortable
```

## Import

```tsx
import {
  Sortable,
  SortableItem,
  SortableItemHandle,
} from "@/components/reui/sortable"
```

## Usage

```tsx
<Sortable value={items} onValueChange={setItems} getItemValue={(item) => item.id}>
  {items.map((item) => (
    <SortableItem key={item.id} value={item.id}>
      <SortableItemHandle>
        <GripVertical />
      </SortableItemHandle>
      {item.content}
    </SortableItem>
  ))}
</Sortable>
```

## Examples (3 total, titles enumerated upstream)

Grid, Nested, Persist to a backend.

### Grid / Nested

Titles only in this mirror — the "View Code" bodies for Grid and Nested were collapsed in the
mirrored markdown (only the "Copy" / "View Code" tab labels were captured, no expanded JSX). What is
attested: `Sortable` accepts `strategy="grid"` per the API Reference below, which is presumably what
the Grid example demonstrates; "Nested" presumably nests one `Sortable` inside a `SortableItem` of
another, but this is inferred from the title, not read from expanded code.

### Persist to a backend

```tsx
"use client"

import { useState } from "react"
import { Badge } from "@/components/reui/badge"
import {
  Sortable,
  SortableItem,
  SortableItemHandle,
  type SortableCommitMeta,
} from "@/components/reui/sortable"
import { toast } from "sonner"
import { GripVerticalIcon } from "lucide-react"

interface Item {
  id: string
  title: string
}

const defaultItems: Item[] = [
  { id: "1", title: "Draft the release notes" },
  { id: "2", title: "Review open pull requests" },
  { id: "3", title: "Update the changelog" },
  { id: "4", title: "Cut the release tag" },
  { id: "5", title: "Announce on the blog" },
]

// Simulated backend. Swap for a tRPC mutation or fetch in your app. Rejects
// roughly one in four calls so the optimistic rollback is easy to see.
function persistOrder(meta: SortableCommitMeta<Item>): Promise<void> {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (Math.random() < 0.25) {
        reject(new Error("Network error"))
      } else {
        resolve()
      }
    }, 700)
  })
}

export function Pattern() {
  const [items, setItems] = useState<Item[]>(defaultItems)

  // Sortable commits once, on drop. `onValueChange` has already applied the
  // new order optimistically; meta.previousValue is the order before the drag.
  const handleValueCommit = (next: Item[], meta: SortableCommitMeta<Item>) => {
    const previous = meta.previousValue
    const moved = next[meta.overIndex]
    toast.promise(persistOrder(meta), {
      loading: "Saving order...",
      success: () => `Saved "${moved.title}" at position ${meta.overIndex + 1}`,
      error: () => {
        // Roll back to the pre-drag order. In production prefer a refetch here
        // so a newer drag is not clobbered by this snapshot.
        setItems(previous)
        return "Could not save the new order. Restored."
      },
    })
  }

  return (
    <div className="mx-auto w-full max-w-xl p-6">
      <Sortable
        value={items}
        onValueChange={setItems}
        onValueCommit={handleValueCommit}
        getItemValue={(item) => item.id}
        strategy="vertical"
        className="space-y-2"
      >
        {items.map((item, index) => (
          <SortableItem key={item.id} value={item.id}>
            <div className="bg-background border-border flex items-center gap-3 rounded-md border p-3">
              <SortableItemHandle className="text-muted-foreground hover:text-foreground">
                <GripVerticalIcon className="h-4 w-4" />
              </SortableItemHandle>
              <Badge variant="outline" className="tabular-nums">
                {index + 1}
              </Badge>
              <span className="min-w-0 flex-1 truncate text-sm font-medium">{item.title}</span>
            </div>
          </SortableItem>
        ))}
      </Sortable>
    </div>
  )
}
```

## Persisting order

Sortable commits once, on drop, so `onValueChange` alone is already enough to persist the whole
array. When you want index-based mutations and a one-line rollback, use `onValueCommit`: it fires
with the reordered array and a `previousValue` snapshot.

```tsx
const reorder = api.list.reorder.useMutation()

<Sortable
  value={items}
  onValueChange={setItems}
  getItemValue={(item) => item.id}
  onValueCommit={(next, meta) => {
    reorder.mutate(
      { id: next[meta.overIndex].id, toIndex: meta.overIndex },
      {
        onError: () => {
          setItems(meta.previousValue) // roll back
          toast.error("Could not save the new order. Restored.")
        },
      },
    )
  }}
>
  {/* ... */}
</Sortable>
```

## API Reference

### Sortable

The root component that manages the sortable state and drag-and-drop context.

| Prop | Type | Default | Description |
|---|---|---|---|
| `value` | `T[]` | `-` | Required. The array of items to sort. |
| `onValueChange` | `(value: T[]) => void` | `-` | Required. Fired once, on drop, with the reordered array. This alone is enough to persist the whole array. |
| `getItemValue` | `(item: T) => string` | `-` | Required. Function to extract a unique ID from an item. |
| `onValueCommit` | `(value: T[], meta: SortableCommitMeta) => void` | `-` | Fired on drop with the reordered array and a `previousValue` snapshot. Convenient for index-based backend mutations and one-line rollback. See "Persisting order". |
| `onMove` | `(event: { event: DragEndEvent; activeIndex: number; overIndex: number }) => void` | `-` | Opt-in. When set, replaces the default `onValueChange` reorder so you apply the move yourself. |
| `strategy` | `"horizontal" \| "vertical" \| "grid"` | `"vertical"` | The sorting strategy and layout of the list. |
| `onDragStart` | `(event: DragStartEvent) => void` | `-` | Raw dnd-kit passthrough, fired when a drag starts. |
| `onDragEnd` | `(event: DragEndEvent) => void` | `-` | Raw dnd-kit passthrough, fired before the reorder is applied (so `onValueChange` is the persistence seam, not this). |
| `onDragCancel` | `(event: DragCancelEvent) => void` | `-` | Raw dnd-kit passthrough, fired when a drag is cancelled. |
| `accessibility` | `DndContextProps["accessibility"]` | `-` | dnd-kit accessibility options (announcements and screen reader instructions). |
| `modifiers` | `Modifiers` | `-` | dnd-kit modifiers applied to the drag. |
| `className` | `string` | `-` | Additional CSS classes for the container. |

`SortableCommitMeta<T>` is `{ event: DragEndEvent; activeIndex: number; overIndex: number;
previousValue: T[] }`.

### SortableItem

An individual draggable item within the sortable list.

| Prop | Type | Default | Description |
|---|---|---|---|
| `value` | `string` | `-` | Required. The unique identifier for the item. |
| `disabled` | `boolean` | `false` | Whether the item is draggable. |
| `className` | `string` | `-` | Additional CSS classes for the item. |

### SortableItemHandle

The drag handle for an individual sortable item.

| Prop | Type | Default | Description |
|---|---|---|---|
| `className` | `string` | `-` | Additional CSS classes for the handle. |

## Base UI vs Radix UI

The API Reference table and usage are identical between builds, but this component is one of two in
scope (with Badge and Timeline) where the **import path itself changes**, not just the underlying
primitive:

| Build | Install | Import |
|---|---|---|
| Base UI | `pnpm dlx shadcn@latest add @reui/sortable` | `@/components/reui/sortable` |
| Radix UI | `pnpm dlx shadcn@latest add @reui/r-sortable` | `@/components/reui/r-sortable` |

The `r-` prefix marks the Radix build's registry item and import path. Component names
(`Sortable`, `SortableItem`, `SortableItemHandle`) and all props are unchanged.

To tell which build a project is on, check `components.json`: `style: "base-nova"` means Base UI
(`@reui/sortable`), `style: "radix-nova"` means Radix UI (`@reui/r-sortable`).

## Source

- Base UI: `docs/components/base/sortable` — mirror captured 2026-09-04.
- Radix UI: `docs/components/radix/sortable` — mirror captured 2026-09-04.
