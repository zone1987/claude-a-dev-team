# Command — API Reference

## Sub-components Overview

| Component | Description |
|---|---|
| `Command` | Root container. Wraps `ListboxRoot` from reka-ui. Manages filter state and item/group registry via context. |
| `CommandDialog` | Dialog wrapper around `Command`. Uses shadcn `Dialog` + `DialogContent` with `Command` inside. |
| `CommandInput` | Search input field. Uses `ListboxFilter` and binds to the shared `filterState.search`. Renders a `Search` icon. |
| `CommandList` | Scrollable list container. Uses `ListboxContent`. Max height 300px. |
| `CommandEmpty` | Shown only when `filterState.search` is set and `filterState.filtered.count === 0`. |
| `CommandGroup` | Groups items under an optional heading. Uses `ListboxGroup`. Hidden when filtered out. |
| `CommandItem` | Individual selectable item. Uses `ListboxItem`. Registers itself in the item registry on mount. Clears search on select. |
| `CommandSeparator` | Visual horizontal rule between groups. Uses reka-ui `Separator`. |
| `CommandShortcut` | Display-only span for keyboard shortcut hints (e.g. `⌘P`). Aligned to the right. |

---

## Command (Root)

Extends `ListboxRootProps` plus `class`.

Default `modelValue` is `""`.

Provides command context to all descendants:

```ts
provideCommandContext({
  allItems,    // Ref<Map<string, string>> — id → text content
  allGroups,   // Ref<Map<string, Set<string>>> — groupId → Set of item ids
  filterState, // reactive { search, filtered: { count, items, groups } }
})
```

---

## CommandDialog

Props:

| Prop | Type | Default | Description |
|---|---|---|---|
| `title` | `string` | `"Command Palette"` | Accessible dialog title (sr-only) |
| `description` | `string` | `"Search for a command to run..."` | Accessible dialog description (sr-only) |
| + all `DialogRootProps` | — | — | `open`, `defaultOpen`, `onUpdate:open`, etc. |

Usage pattern: bind `v-model:open` for controlled open state. The `Command` root is rendered inside the dialog automatically — do NOT wrap with another `Command`.

```vue
<CommandDialog v-model:open="open">
  <CommandInput placeholder="..." />
  <CommandList>
    ...
  </CommandList>
</CommandDialog>
```

---

## CommandGroup

Props:

| Prop | Type | Description |
|---|---|---|
| `heading` | `string?` | Optional group label text |
| `class` | `string?` | Additional CSS classes |
| + all `ListboxGroupProps` | — | reka-ui ListboxGroup props |

Groups register themselves in `allGroups` on mount and are automatically hidden when all their items are filtered out.

---

## CommandItem

Extends `ListboxItemProps` plus `class`.

Registers its text content in `allItems` on mount (uses `textContent` of the rendered element, or `props.value?.toString()`).

Automatically clears `filterState.search` on `@select`.

Visibility is computed from `filterState.filtered.items` score.

---

## CommandEmpty

Renders only when:
- `filterState.search` is non-empty, AND
- `filterState.filtered.count === 0`

---

## CommandShortcut

Pure display component. Renders a `<span>` with right-aligned, small, muted text.

```vue
<CommandItem value="profile">
  Profile
  <CommandShortcut>⌘P</CommandShortcut>
</CommandItem>
```

---

## Context

Exported composables for advanced use:

```ts
import { useCommand, useCommandGroup } from "@/components/ui/command"

// In a child component:
const { filterState, allItems, allGroups } = useCommand()
const groupContext = useCommandGroup() // may be undefined if not inside a group
```

---

## reka-ui API Reference

- Combobox/Listbox: https://reka-ui.com/docs/components/combobox#api-reference
- ListboxRoot props: https://reka-ui.com/docs/components/listbox
