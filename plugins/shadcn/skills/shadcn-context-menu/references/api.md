# ContextMenu — API Reference

## Composition

```text
ContextMenu
├── ContextMenuTrigger
└── ContextMenuContent
    ├── ContextMenuGroup
    │   ├── ContextMenuLabel
    │   ├── ContextMenuItem
    │   └── ContextMenuItem
    ├── ContextMenuSeparator
    ├── ContextMenuGroup
    │   ├── ContextMenuLabel
    │   ├── ContextMenuCheckboxItem
    │   └── ContextMenuCheckboxItem
    ├── ContextMenuSeparator
    ├── ContextMenuGroup
    │   ├── ContextMenuLabel
    │   └── ContextMenuRadioGroup
    │       ├── ContextMenuRadioItem
    │       └── ContextMenuRadioItem
    └── ContextMenuSub
        ├── ContextMenuSubTrigger
        └── ContextMenuSubContent
            └── ContextMenuGroup
                ├── ContextMenuItem
                └── ContextMenuItem
```

## Usage

```tsx
import {
  ContextMenu,
  ContextMenuContent,
  ContextMenuItem,
  ContextMenuTrigger,
} from "@/components/ui/context-menu"
```

```tsx
<ContextMenu>
  <ContextMenuTrigger>Right click here</ContextMenuTrigger>
  <ContextMenuContent>
    <ContextMenuItem>Profile</ContextMenuItem>
    <ContextMenuItem>Billing</ContextMenuItem>
    <ContextMenuItem>Team</ContextMenuItem>
    <ContextMenuItem>Subscription</ContextMenuItem>
  </ContextMenuContent>
</ContextMenu>
```

## Sub-Component Props

### ContextMenu (Root)

| Prop           | Type                      | Default | Description                        |
| -------------- | ------------------------- | ------- | ---------------------------------- |
| `onOpenChange` | `(open: boolean) => void` | -       | Callback when open state changes   |

### ContextMenuTrigger

The element that opens the menu on right-click.

| Prop        | Type      | Default | Description                            |
| ----------- | --------- | ------- | -------------------------------------- |
| `asChild`   | `boolean` | `false` | Merge props onto immediate child       |
| `disabled`  | `boolean` | `false` | Prevent opening                        |
| `className` | `string`  | -       |                                        |

### ContextMenuContent

The menu popup container.

| Prop        | Type     | Default | Description                           |
| ----------- | -------- | ------- | ------------------------------------- |
| `className` | `string` | -       |                                       |

### ContextMenuItem

A basic menu item.

| Prop        | Type                        | Default     | Description                          |
| ----------- | --------------------------- | ----------- | ------------------------------------ |
| `inset`     | `boolean`                   | `false`     | Add left padding to align with items that have an icon |
| `variant`   | `"default" \| "destructive"` | `"default"` | Style variant                        |
| `disabled`  | `boolean`                   | `false`     | Prevent interaction                  |
| `onSelect`  | `function`                  | -           | Callback when item is selected       |
| `className` | `string`                    | -           |                                      |

### ContextMenuCheckboxItem

A menu item with a checkbox indicator.

| Prop           | Type                                        | Default | Description                       |
| -------------- | ------------------------------------------- | ------- | --------------------------------- |
| `checked`      | `boolean \| "indeterminate"`                | -       | Controlled checked state          |
| `onCheckedChange` | `(checked: boolean) => void`             | -       | Callback on change                |
| `disabled`     | `boolean`                                   | `false` | Prevent interaction               |
| `className`    | `string`                                    | -       |                                   |

### ContextMenuRadioGroup / ContextMenuRadioItem

Group radio items; only one item can be checked at a time.

`ContextMenuRadioGroup`:

| Prop            | Type                      | Default | Description                    |
| --------------- | ------------------------- | ------- | ------------------------------ |
| `value`         | `string`                  | -       | Controlled selected value      |
| `onValueChange` | `(value: string) => void` | -       | Callback on change             |

`ContextMenuRadioItem`:

| Prop        | Type      | Default | Description            |
| ----------- | --------- | ------- | ---------------------- |
| `value`     | `string`  | required | Item value            |
| `disabled`  | `boolean` | `false`  | Prevent interaction   |
| `className` | `string`  | -        |                       |

### ContextMenuSub / ContextMenuSubTrigger / ContextMenuSubContent

For nested submenus.

`ContextMenuSubTrigger`:

| Prop        | Type      | Default | Description                      |
| ----------- | --------- | ------- | -------------------------------- |
| `inset`     | `boolean` | `false` | Add left padding                 |
| `className` | `string`  | -       |                                  |

### ContextMenuLabel

Non-interactive section heading.

| Prop        | Type      | Default | Description      |
| ----------- | --------- | ------- | ---------------- |
| `inset`     | `boolean` | `false` | Add left padding |
| `className` | `string`  | -       |                  |

### ContextMenuSeparator

Horizontal divider between groups.

### ContextMenuShortcut

Keyboard shortcut hint, rendered right-aligned inside an item.

## Radix UI API Reference

See https://www.radix-ui.com/docs/primitives/components/context-menu#api-reference for the complete API.

---

_Source: `/tmp/shadcn-repo/apps/v4/content/docs/components/radix/context-menu.mdx`_
