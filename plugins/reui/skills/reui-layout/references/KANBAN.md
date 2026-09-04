# Kanban

Custom Shadcn Kanban for React and Tailwind CSS. A drag-and-drop kanban component designed for
seamless item organization across customizable columns. Built on dnd-kit.

Free component — no licence key required.

## Contents

- [Installation](#installation)
- [Import](#import)
- [Usage](#usage)
- [Examples (2 titled, plus a Pro-blocks pointer)](#examples-2-titled-plus-a-pro-blocks-pointer)
- [Persisting moves](#persisting-moves)
- [API Reference](#api-reference)
- [Base UI vs Radix UI](#base-ui-vs-radix-ui)
- [Source](#source)

## Installation

```
pnpm dlx shadcn@latest add @reui/kanban
```

## Import

```tsx
import {
  Kanban,
  KanbanBoard,
  KanbanColumn,
  KanbanColumnContent,
  KanbanColumnHandle,
  KanbanItem,
  KanbanItemHandle,
  KanbanOverlay,
} from "@/components/reui/kanban"
```

## Usage

```tsx
<Kanban value={columns} onValueChange={setColumns} getItemValue={(item) => item.id}>
  <KanbanBoard>
    {Object.entries(columns).map(([id, items]) => (
      <KanbanColumn key={id} value={id}>
        <KanbanColumnHandle>
          <h3>{id}</h3>
        </KanbanColumnHandle>
        <KanbanColumnContent value={id}>
          {items.map((item) => (
            <KanbanItem key={item.id} value={item.id}>
              <KanbanItemHandle>{item.content}</KanbanItemHandle>
            </KanbanItem>
          ))}
        </KanbanColumnContent>
      </KanbanColumn>
    ))}
  </KanbanBoard>
  <KanbanOverlay>
    <div className="bg-muted size-full rounded-md" />
  </KanbanOverlay>
</Kanban>
```

## Examples (2 titled, plus a Pro-blocks pointer)

### Overlay

Demonstrates `<KanbanOverlay>` as the drag ghost element.

### Persist to a backend

Demonstrates `onValueCommit` for persisting moves, per the "Persisting moves" section below.

The page also notes: "This primitive also powers ready-made ReUI Pro blocks: complete kanban board
sections assembled on top of the exact component documented here... Preview all 10 Shadcn Kanban
Board Pro blocks in the ReUI blocks gallery." (Pro blocks are out of scope — this reference covers
only the free primitive.)

## Persisting moves

Keep `value` and `onValueChange` so the board reshuffles live while dragging, and use
`onValueCommit` to save. It fires once per completed drag (never during the hover preview) with the
final board and a `previousValue` snapshot, so you can update optimistically and roll back on error.
Its `meta.kind` tells you whether a card moved (`"item"`) or a column was reordered (`"column"`).

```tsx
const moveCard = api.board.moveCard.useMutation()
const reorderColumns = api.board.reorderColumns.useMutation()

<Kanban
  value={columns}
  onValueChange={setColumns}
  getItemValue={(task) => task.id}
  onValueCommit={(next, meta) => {
    if (meta.kind === "column") {
      reorderColumns.mutate({ order: Object.keys(next) })
      return
    }
    moveCard.mutate(
      { id: String(meta.event.active.id), to: meta.overContainer, index: meta.overIndex },
      {
        onError: () => {
          setColumns(meta.previousValue) // roll back
          toast.error("Could not move the card. Your board was restored.")
        },
      },
    )
  }}
>
  {/* ... */}
</Kanban>
```

If a user might start another drag before the mutation settles, prefer a refetch in `onError` instead
of restoring the snapshot, so a newer arrangement is not clobbered.

If you do not need the live cross-column preview, `onMove` is a simpler alternative: it fires once on
drop for item moves and lets you apply the move yourself. Column reorders still arrive through
`onValueChange`.

## API Reference

### Kanban

The root component that provides the kanban context and manages the items state.

| Prop | Type | Default | Description |
|---|---|---|---|
| `value` | `Record<string, T[]>` | `-` | Required. The current state of columns and their items. |
| `onValueChange` | `(value: Record<string, T[]>) => void` | `-` | Required. Fired when items move within or between columns. In the default mode it also fires during the drag to render the live preview, so avoid persisting from here directly. |
| `getItemValue` | `(item: T) => string` | `-` | Required. Function to get a unique identifier for an item. |
| `onValueCommit` | `(value: Record<string, T[]>, meta: KanbanCommitMeta) => void` | `-` | Fired once per completed drag with the final board and a `previousValue` snapshot. Use it to persist moves to a backend. See "Persisting moves". |
| `onMove` | `(event: KanbanMoveEvent) => void` | `-` | Opt-in single commit point for item moves. When set, the live preview is disabled and you apply the move yourself. |
| `restoreOnCancel` | `boolean` | `false` | When `true`, cancelling a drag (for example pressing Escape) restores the board to its pre-drag arrangement. |
| `onDragStart` | `(event: DragStartEvent) => void` | `-` | Raw dnd-kit passthrough, fired when a drag starts. |
| `onDragEnd` | `(event: DragEndEvent) => void` | `-` | Raw dnd-kit passthrough, fired after internal cleanup and before the final `onValueChange`/`onMove` call. In the default mode, `onValueChange` has already fired during dragOver. |
| `onDragCancel` | `(event: DragCancelEvent) => void` | `-` | Raw dnd-kit passthrough, fired when a drag is cancelled. |
| `accessibility` | `DndContextProps["accessibility"]` | `-` | dnd-kit accessibility options (announcements and screen reader instructions). |
| `modifiers` | `Modifiers` | `-` | dnd-kit modifiers applied to the drag. |
| `className` | `string` | `-` | Additional CSS classes for the container. |

`KanbanCommitMeta<T>` is:
```ts
{
  kind: "item" | "column"
  event: DragEndEvent
  activeContainer: string
  activeIndex: number
  overContainer: string
  overIndex: number
  previousValue: Record<string, T[]>
}
```

### KanbanBoard

The horizontal container for kanban columns.

| Prop | Type | Default | Description |
|---|---|---|---|
| `className` | `string` | `-` | Additional CSS classes for the board. |

### KanbanColumn

An individual column within the kanban board.

| Prop | Type | Default | Description |
|---|---|---|---|
| `value` | `string` | `-` | Required. The unique identifier for the column. |
| `className` | `string` | `-` | Additional CSS classes for the column. |

### KanbanColumnHandle

The drag handle for a column (if columns are sortable).

| Prop | Type | Default | Description |
|---|---|---|---|
| `className` | `string` | `-` | Additional CSS classes for the handle. |

### KanbanColumnContent

The scrollable area within a column that holds the items.

| Prop | Type | Default | Description |
|---|---|---|---|
| `value` | `string` | `-` | Required. The identifier of the column this content belongs to. |
| `className` | `string` | `-` | Additional CSS classes for the content area. |

### KanbanItem

An individual draggable item within a column.

| Prop | Type | Default | Description |
|---|---|---|---|
| `value` | `string` | `-` | Required. The unique identifier for the item. |
| `disabled` | `boolean` | `false` | Whether the item is draggable. |
| `className` | `string` | `-` | Additional CSS classes for the item. |

### KanbanItemHandle

The drag handle for an individual item.

| Prop | Type | Default | Description |
|---|---|---|---|
| `className` | `string` | `-` | Additional CSS classes for the handle. |

### KanbanOverlay

The ghost element displayed during a drag operation.

| Prop | Type | Default | Description |
|---|---|---|---|
| `className` | `string` | `-` | Additional CSS classes for the overlay. |

## Base UI vs Radix UI

Installation command and import path are unchanged between builds (`@reui/kanban`,
`@/components/reui/kanban`), and the full API Reference table above is identical. The only real
difference is in how `KanbanColumnHandle` composes a custom trigger element in the example code:

- Base UI: uses the `render` prop with a function child —
  `<KanbanColumnHandle render={(props) => (<Button {...props} size="icon-xs" variant="ghost"><GripVerticalIcon /></Button>)} />`
- Radix UI: uses `asChild` with a plain child element —
  `<KanbanColumnHandle asChild><Button size="icon-xs" variant="ghost"><GripVerticalIcon /></Button></KanbanColumnHandle>`

This mirrors the Base UI `render`-prop vs. Radix UI `asChild` composition pattern seen across other
ReUI primitives (Stepper, Badge, Icon Tile). `KanbanColumnHandle` itself is not documented with a
`render`/`asChild` row in the upstream API Reference table for either build — the prop is attested
only by its use in example code, not by an upstream description or default.

To tell which build a project is on, check `components.json`: `style: "base-nova"` means Base UI
(`render` composition), `style: "radix-nova"` means Radix UI (`asChild` composition).

## Source

- Base UI: `docs/components/base/kanban` — mirror captured 2026-09-04.
- Radix UI: `docs/components/radix/kanban` — mirror captured 2026-09-04.
