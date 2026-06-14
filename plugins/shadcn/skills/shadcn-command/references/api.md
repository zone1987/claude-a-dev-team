# Command — API Reference

## Composition

```text
Command
├── CommandInput
└── CommandList
    ├── CommandEmpty
    ├── CommandGroup
    │   ├── CommandItem
    │   └── CommandItem
    ├── CommandSeparator
    └── CommandGroup
        ├── CommandItem
        └── CommandItem
```

## Usage

```tsx
import {
  Command,
  CommandDialog,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
  CommandSeparator,
  CommandShortcut,
} from "@/components/ui/command"
```

```tsx
<Command className="max-w-sm rounded-lg border">
  <CommandInput placeholder="Type a command or search..." />
  <CommandList>
    <CommandEmpty>No results found.</CommandEmpty>
    <CommandGroup heading="Suggestions">
      <CommandItem>Calendar</CommandItem>
      <CommandItem>Search Emoji</CommandItem>
      <CommandItem>Calculator</CommandItem>
    </CommandGroup>
    <CommandSeparator />
    <CommandGroup heading="Settings">
      <CommandItem>Profile</CommandItem>
      <CommandItem>Billing</CommandItem>
      <CommandItem>Settings</CommandItem>
    </CommandGroup>
  </CommandList>
</Command>
```

## Sub-Component Props

### Command (Root)

Wraps `cmdk` `Command` primitive.

| Prop        | Type      | Default | Description                              |
| ----------- | --------- | ------- | ---------------------------------------- |
| `label`     | `string`  | -       | Accessible label for the command menu    |
| `filter`    | `function`| -       | Custom filter function for items         |
| `shouldFilter` | `boolean` | `true` | Whether to filter items on input change |
| `value`     | `string`  | -       | Controlled selected value                |
| `onValueChange` | `function` | -  | Callback when selected value changes    |
| `className` | `string`  | -       |                                          |

### CommandDialog

Wraps `Command` inside a `Dialog`. Accepts all `Dialog` props plus:

| Prop              | Type      | Default                  | Description                        |
| ----------------- | --------- | ------------------------ | ---------------------------------- |
| `title`           | `string`  | `"Command Palette"`      | Screen-reader dialog title         |
| `description`     | `string`  | `"Search for a command to run..."` | Screen-reader description |
| `showCloseButton` | `boolean` | `true`                   | Show the X close button            |
| `className`       | `string`  | -                        | Applied to `DialogContent`         |

### CommandInput

Text input with a search icon.

| Prop          | Type     | Default | Description          |
| ------------- | -------- | ------- | -------------------- |
| `placeholder` | `string` | -       | Placeholder text     |
| `value`       | `string` | -       | Controlled value     |
| `onValueChange` | `function` | -   | Input change callback |
| `className`   | `string` | -       |                      |

### CommandList

Scrollable container for command results. Max height 300px by default.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### CommandEmpty

Shown when the filtered list is empty.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### CommandGroup

Groups related items with an optional heading.

| Prop        | Type     | Default | Description                     |
| ----------- | -------- | ------- | ------------------------------- |
| `heading`   | `string` | -       | Group heading text              |
| `className` | `string` | -       |                                 |

### CommandItem

A single selectable command item.

| Prop        | Type       | Default | Description                              |
| ----------- | ---------- | ------- | ---------------------------------------- |
| `value`     | `string`   | -       | Value used for filtering                 |
| `onSelect`  | `function` | -       | Callback when item is selected           |
| `disabled`  | `boolean`  | `false` | Prevent selection                        |
| `keywords`  | `string[]` | -       | Additional search keywords               |
| `className` | `string`   | -       |                                          |

### CommandShortcut

Renders a keyboard shortcut hint aligned to the right of an item.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### CommandSeparator

A horizontal divider between groups.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

## CommandDialog Pattern

Open/close via keyboard shortcut:

```tsx
"use client"

import * as React from "react"
import { CommandDialog, CommandEmpty, CommandGroup, CommandInput, CommandItem, CommandList } from "@/components/ui/command"

export function CommandMenu() {
  const [open, setOpen] = React.useState(false)

  React.useEffect(() => {
    const down = (e: KeyboardEvent) => {
      if (e.key === "k" && (e.metaKey || e.ctrlKey)) {
        e.preventDefault()
        setOpen((open) => !open)
      }
    }
    document.addEventListener("keydown", down)
    return () => document.removeEventListener("keydown", down)
  }, [])

  return (
    <CommandDialog open={open} onOpenChange={setOpen}>
      <CommandInput placeholder="Type a command or search..." />
      <CommandList>
        <CommandEmpty>No results found.</CommandEmpty>
        <CommandGroup heading="Suggestions">
          <CommandItem>Calendar</CommandItem>
          <CommandItem>Search Emoji</CommandItem>
        </CommandGroup>
      </CommandList>
    </CommandDialog>
  )
}
```

---

_Source: `/tmp/shadcn-repo/apps/v4/content/docs/components/radix/command.mdx`_
