# DropdownMenu — API Reference

## Composition Tree

```text
DropdownMenu
├── DropdownMenuTrigger
└── DropdownMenuContent
    ├── DropdownMenuGroup
    │   ├── DropdownMenuLabel
    │   ├── DropdownMenuItem
    │   └── DropdownMenuItem
    ├── DropdownMenuSeparator
    ├── DropdownMenuGroup
    │   ├── DropdownMenuLabel
    │   ├── DropdownMenuCheckboxItem
    │   └── DropdownMenuCheckboxItem
    ├── DropdownMenuSeparator
    ├── DropdownMenuGroup
    │   ├── DropdownMenuLabel
    │   └── DropdownMenuRadioGroup
    │       ├── DropdownMenuRadioItem
    │       └── DropdownMenuRadioItem
    └── DropdownMenuSub
        ├── DropdownMenuSubTrigger
        └── DropdownMenuSubContent
            └── DropdownMenuGroup
                ├── DropdownMenuLabel
                ├── DropdownMenuItem
                └── DropdownMenuItem
```

## Basic Usage

```tsx
import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"

<DropdownMenu>
  <DropdownMenuTrigger render={<Button variant="outline" />}>
    Open
  </DropdownMenuTrigger>
  <DropdownMenuContent>
    <DropdownMenuGroup>
      <DropdownMenuLabel>My Account</DropdownMenuLabel>
      <DropdownMenuItem>Profile</DropdownMenuItem>
      <DropdownMenuItem>Billing</DropdownMenuItem>
    </DropdownMenuGroup>
    <DropdownMenuSeparator />
    <DropdownMenuGroup>
      <DropdownMenuItem>Team</DropdownMenuItem>
      <DropdownMenuItem>Subscription</DropdownMenuItem>
    </DropdownMenuGroup>
  </DropdownMenuContent>
</DropdownMenu>
```

## Sub-component Props

### DropdownMenu

| Prop           | Type                      | Default | Description                             |
| -------------- | ------------------------- | ------- | --------------------------------------- |
| `open`         | `boolean`                 | –       | Controlled open state                   |
| `defaultOpen`  | `boolean`                 | `false` | Uncontrolled default                    |
| `onOpenChange` | `(open: boolean) => void` | –       | Called when open state changes          |
| `modal`        | `boolean`                 | `true`  | Set `false` to allow Dialog to open from item |

### DropdownMenuTrigger

| Prop      | Type      | Default | Description             |
| --------- | --------- | ------- | ----------------------- |
| `asChild` | `boolean` | `false` | Render as child element |

### DropdownMenuContent

| Prop         | Type                                           | Default | Description              |
| ------------ | ---------------------------------------------- | ------- | ------------------------ |
| `sideOffset` | `number`                                       | `4`     | Offset from trigger      |
| `align`      | `"start" \| "center" \| "end"`                | –       | Horizontal alignment     |
| `side`       | `"top" \| "right" \| "bottom" \| "left"`      | –       | Preferred side           |
| `className`  | `string`                                       | –       | Additional CSS classes   |

### DropdownMenuItem

| Prop        | Type                          | Default     | Description                         |
| ----------- | ----------------------------- | ----------- | ----------------------------------- |
| `inset`     | `boolean`                     | `false`     | Adds left padding (aligns with checkbox/radio items) |
| `variant`   | `"default" \| "destructive"` | `"default"` | Red color for destructive actions   |
| `disabled`  | `boolean`                     | `false`     | Disables the item                   |
| `onSelect`  | `(event: Event) => void`      | –           | Called when item is selected        |
| `className` | `string`                      | –           | Additional CSS classes              |

### DropdownMenuCheckboxItem

| Prop              | Type                                         | Default | Description                    |
| ----------------- | -------------------------------------------- | ------- | ------------------------------ |
| `checked`         | `boolean \| "indeterminate"`                 | –       | Controlled checked state       |
| `onCheckedChange` | `(checked: boolean) => void`                 | –       | Called on state change         |
| `disabled`        | `boolean`                                    | `false` | Disables the item              |

### DropdownMenuRadioGroup

| Prop          | Type                      | Default | Description              |
| ------------- | ------------------------- | ------- | ------------------------ |
| `value`       | `string`                  | –       | Selected value           |
| `onValueChange` | `(value: string) => void` | –     | Called when value changes |

### DropdownMenuRadioItem

| Prop       | Type      | Default | Description             |
| ---------- | --------- | ------- | ----------------------- |
| `value`    | `string`  | –       | Item value (required)   |
| `disabled` | `boolean` | `false` | Disables the item       |

### DropdownMenuLabel

| Prop        | Type      | Default | Description                         |
| ----------- | --------- | ------- | ----------------------------------- |
| `inset`     | `boolean` | `false` | Adds left padding to align with items |
| `className` | `string`  | –       | Additional CSS classes              |

### DropdownMenuShortcut

Plain `<span>` with `ml-auto` — displays keyboard shortcuts right-aligned.

```tsx
<DropdownMenuItem>
  Profile <DropdownMenuShortcut>⇧⌘P</DropdownMenuShortcut>
</DropdownMenuItem>
```

### DropdownMenuSub / SubTrigger / SubContent

Nests a secondary menu. `DropdownMenuSubTrigger` automatically adds the chevron icon.

---

_Source: `apps/v4/content/docs/components/base/dropdown-menu.mdx`, `apps/v4/registry/new-york-v4/ui/dropdown-menu.tsx`_
