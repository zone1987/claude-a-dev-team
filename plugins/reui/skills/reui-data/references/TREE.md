# Tree

Custom Shadcn Tree for React and Tailwind CSS. A customizable tree component for React, built on
`@headless-tree/core` and `@headless-tree/react`.

Free component — no licence key required.

## Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Examples](#examples)
- [Base UI vs Radix UI](#base-ui-vs-radix-ui)
- [Source](#source)

## Installation

```
pnpm dlx shadcn@latest add @reui/tree
```

(npm/yarn/bun equivalents: `npx shadcn@latest add @reui/tree`, `yarn dlx shadcn@latest add @reui/tree`,
`bunx shadcn@latest add @reui/tree`.)

## Usage

```tsx
import { Tree, TreeItem, TreeItemLabel } from "@/components/reui/tree"
```

Basic shape:

```tsx
<Tree tree={tree}>
  {tree.getItems().map((item) => (
    <TreeItem key={item.getId()} item={item}>
      <TreeItemLabel />
    </TreeItem>
  ))}
</Tree>
```

`Tree` is a styled shell: it takes a `@headless-tree/core` tree instance via the `tree` prop, NOT
`data`/`items` props directly. Build the instance with `useTree` from `@headless-tree/react`.

## API Reference

### Tree

The root component that provides context for the tree structure.

| Prop | Type | Default | Description |
|---|---|---|---|
| `tree` | `any` | — | Required. The tree instance from `@headless-tree/core`. |
| `indent` | `number` | `20` | Pixel value for each level of indentation. |
| `toggleIconType` | `"chevron" \| "plus-minus"` | `"chevron"` | The type of icon used for expanding/collapsing folders. |
| `className` | `string` | — | Additional CSS classes for the tree container. |

### TreeItem

A component representing a single item (node) in the tree.

| Prop | Type | Default | Description |
|---|---|---|---|
| `item` | `ItemInstance` | — | Required. The instance of the current tree item. |
| `indent` | `number` | — | Custom indentation for this specific item (overrides Tree indent). |
| `className` | `string` | — | Additional CSS classes for the item container. |

### TreeItemLabel

The component that displays the label and toggle icon for a tree item.

| Prop | Type | Default | Description |
|---|---|---|---|
| `item` | `ItemInstance` | — | Optional item instance (uses context if not provided). |
| `className` | `string` | — | Additional CSS classes for the label. |

### TreeDragLine

The visual indicator shown during drag-and-drop operations.

| Prop | Type | Default | Description |
|---|---|---|---|
| `className` | `string` | — | Additional CSS classes for the drag line. |

## Examples

The docs page lists 3 named example variants (in addition to the API-reference default), each a
complete, standalone `Pattern()` component. All four share the same `items` data (a CRM tree: crm ->
leads/accounts/activities/support, each with further children) and the same `indent = 20`, built with:

```tsx
const tree = useTree<Item>({
  initialState: {
    expandedItems: ["leads", "accounts", "activities"],
  },
  indent,
  rootItemId: "crm",
  getItemName: (item) => item.getItemData().name,
  isItemFolder: (item) => (item.getItemData()?.children?.length ?? 0) > 0,
  dataLoader: {
    getItem: (itemId) => items[itemId],
    getChildren: (itemId) => items[itemId].children ?? [],
  },
  features: [syncDataLoaderFeature, hotkeysCoreFeature],
})
```

Full `items` record (shared by every example):

```tsx
interface Item {
  name: string
  children?: string[]
}

const items: Record<string, Item> = {
  crm: { name: "CRM", children: ["leads", "accounts", "activities", "support"] },
  leads: { name: "Leads", children: ["new-lead", "contacted-lead", "qualified-lead"] },
  "new-lead": { name: "New Lead" },
  "contacted-lead": { name: "Contacted Lead" },
  "qualified-lead": { name: "Qualified Lead" },
  accounts: { name: "Accounts", children: ["acme-corp", "globex-inc"] },
  "acme-corp": { name: "Acme Corp", children: ["acme-contacts", "acme-opportunities"] },
  "acme-contacts": { name: "Contacts", children: ["john-smith", "jane-doe"] },
  "john-smith": { name: "John Smith" },
  "jane-doe": { name: "Jane Doe" },
  "acme-opportunities": { name: "Opportunities", children: ["website-redesign", "annual-maintenance"] },
  "website-redesign": { name: "Website Redesign" },
  "annual-maintenance": { name: "Annual Maintenance" },
  "globex-inc": { name: "Globex Inc", children: ["globex-contacts", "globex-opportunities"] },
  "globex-contacts": { name: "Contacts", children: ["alice-johnson"] },
  "alice-johnson": { name: "Alice Johnson" },
  "globex-opportunities": { name: "Opportunities", children: ["cloud-migration"] },
  "cloud-migration": { name: "Cloud Migration" },
  activities: { name: "Activities", children: ["calls", "meetings", "emails"] },
  calls: { name: "Calls" },
  meetings: { name: "Meetings" },
  emails: { name: "Emails" },
  support: { name: "Support", children: ["open-tickets", "closed-tickets"] },
  "open-tickets": { name: "Open Tickets" },
  "closed-tickets": { name: "Closed Tickets" },
}
```

### With line

Adds a vertical guide line per indent level via a `before:` pseudo-element on `Tree`, driven by the
`--tree-indent` CSS variable:

```tsx
<Tree
  className="relative before:absolute before:inset-0 before:-ms-1 before:bg-[repeating-linear-gradient(to_right,transparent_0,transparent_calc(var(--tree-indent)-1px),var(--border)_calc(var(--tree-indent)-1px),var(--border)_calc(var(--tree-indent)))]"
  indent={indent}
  tree={tree}
>
  {tree.getItems().map((item) => (
    <TreeItem key={item.getId()} item={item}>
      <TreeItemLabel />
    </TreeItem>
  ))}
</Tree>
```

### With Icon

Adds folder/file icons from `lucide-react` (`FileIcon`, `FolderIcon`, `FolderOpenIcon`), switching
open/closed folder icon based on `item.isFolder()` / `item.isExpanded()`, plus a background patch on
the label so the guide line doesn't show through selected/hovered rows:

```tsx
<TreeItemLabel className="before:bg-background relative before:absolute before:inset-x-0 before:-inset-y-0.5 before:-z-10">
  <span className="flex items-center gap-2">
    {item.isFolder() ? (
      item.isExpanded() ? (
        <FolderOpenIcon className="text-muted-foreground pointer-events-none size-4" />
      ) : (
        <FolderIcon className="text-muted-foreground pointer-events-none size-4" />
      )
    ) : (
      <FileIcon className="text-muted-foreground pointer-events-none size-4" />
    )}
    {item.getItemName()}
  </span>
</TreeItemLabel>
```

### With Plus and Minus Icons

Same as "With Icon" but sets `toggleIconType="plus-minus"` on `Tree` (in place of the default chevron)
and nudges the label content with `ms-1`:

```tsx
<Tree
  className="relative before:absolute before:inset-0 before:-ms-1.25 before:bg-[repeating-linear-gradient(to_right,transparent_0,transparent_calc(var(--tree-indent)-1px),var(--border)_calc(var(--tree-indent)-1px),var(--border)_calc(var(--tree-indent)))]"
  indent={indent}
  tree={tree}
  toggleIconType="plus-minus"
>
  {tree.getItems().map((item) => (
    <TreeItem key={item.getId()} item={item}>
      <TreeItemLabel className="before:bg-background relative before:absolute before:inset-x-0 before:-inset-y-0.5 before:-z-10">
        <span className="ms-1 flex items-center gap-2">
          {item.isFolder() ? (
            item.isExpanded() ? (
              <FolderOpenIcon className="text-muted-foreground pointer-events-none size-4" />
            ) : (
              <FolderIcon className="text-muted-foreground pointer-events-none size-4" />
            )
          ) : (
            <FileIcon className="text-muted-foreground pointer-events-none size-4" />
          )}
          {item.getItemName()}
        </span>
      </TreeItemLabel>
    </TreeItem>
  ))}
</Tree>
```

Full source for each example is the shared `Pattern()` function above with the `Tree`/`TreeItemLabel`
JSX block swapped for the variant shown.

## Base UI vs Radix UI

Detect your build from `components.json` -> `style`: `base-nova` -> Base UI (this file's default),
`radix-nova` -> Radix UI.

The upstream page states no prop, behaviour, or API difference between the two builds for Tree — the
only differences are the install/import identifiers:

| | Base UI | Radix UI |
|---|---|---|
| Install | `pnpm dlx shadcn@latest add @reui/tree` | `pnpm dlx shadcn@latest add @reui/r-tree` |
| Import path | `@/components/reui/tree` | `@/components/reui/r-tree` |

The Radix UI page describes its examples as following "the Radix UI implementation with accessible
primitives from the Radix stack"; the Base UI page describes its examples as using "Base UI primitives
from @base-ui/react". The API Reference tables (Tree, TreeItem, TreeItemLabel, TreeDragLine) are
identical between builds.

## Source

- https://reui.io/docs/components/base/tree (Base UI)
- https://reui.io/docs/components/radix/tree (Radix UI)
- Mirrored 2026-09-04.
