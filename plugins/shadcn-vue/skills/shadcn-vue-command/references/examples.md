# Command — Examples

Source: `registry/bases/reka/examples/command/`

---

## 1. Inline Command (no dialog)

The simplest usage — an always-visible command menu embedded directly in the page.

```vue
<script setup lang="ts">
import {
  Command,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
  CommandSeparator,
  CommandShortcut,
} from '@/components/ui/command'
</script>

<template>
  <Command>
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
</template>
```

---

## 2. CommandBasic (dialog-based)

Open a command palette in a dialog via a button.

```vue
<script setup lang="ts">
import { ref } from "vue"
import { Example } from "@/registry/bases/reka/components/example"
import { Button } from "@/registry/bases/reka/ui/button"
import {
  Command,
  CommandDialog,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
} from "@/registry/bases/reka/ui/command"

const open = ref(false)
</script>

<template>
  <Example title="Basic">
    <div class="flex flex-col gap-4">
      <Button variant="outline" class="w-fit" @click="open = true">
        Open Menu
      </Button>
      <CommandDialog v-model:open="open">
        <Command>
          <CommandInput placeholder="Type a command or search..." />
          <CommandList>
            <CommandEmpty>No results found.</CommandEmpty>
            <CommandGroup heading="Suggestions">
              <CommandItem value="calendar">Calendar</CommandItem>
              <CommandItem value="search-emoji">Search Emoji</CommandItem>
              <CommandItem value="calculator">Calculator</CommandItem>
            </CommandGroup>
          </CommandList>
        </Command>
      </CommandDialog>
    </div>
  </Example>
</template>
```

---

## 3. CommandWithShortcuts

Items with keyboard shortcut hints displayed on the right.

```vue
<script setup lang="ts">
import { ref } from "vue"
import { Example } from "@/registry/bases/reka/components/example"
import { Button } from "@/registry/bases/reka/ui/button"
import {
  Command,
  CommandDialog,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
  CommandShortcut,
} from "@/registry/bases/reka/ui/command"

const open = ref(false)
</script>

<template>
  <Example title="With Shortcuts">
    <div class="flex flex-col gap-4">
      <Button variant="outline" class="w-fit" @click="open = true">Open Menu</Button>
      <CommandDialog v-model:open="open">
        <Command>
          <CommandInput placeholder="Type a command or search..." />
          <CommandList>
            <CommandEmpty>No results found.</CommandEmpty>
            <CommandGroup heading="Settings">
              <CommandItem value="profile">
                <span>Profile</span>
                <CommandShortcut>⌘P</CommandShortcut>
              </CommandItem>
              <CommandItem value="billing">
                <span>Billing</span>
                <CommandShortcut>⌘B</CommandShortcut>
              </CommandItem>
              <CommandItem value="settings">
                <span>Settings</span>
                <CommandShortcut>⌘S</CommandShortcut>
              </CommandItem>
            </CommandGroup>
          </CommandList>
        </Command>
      </CommandDialog>
    </div>
  </Example>
</template>
```

---

## 4. CommandWithGroups

Multiple groups separated by a `CommandSeparator`, with shortcuts.

```vue
<script setup lang="ts">
import { ref } from "vue"
import { Example } from "@/registry/bases/reka/components/example"
import { Button } from "@/registry/bases/reka/ui/button"
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
} from "@/registry/bases/reka/ui/command"

const open = ref(false)
</script>

<template>
  <Example title="With Groups">
    <div class="flex flex-col gap-4">
      <Button variant="outline" class="w-fit" @click="open = true">Open Menu</Button>
      <CommandDialog v-model:open="open">
        <Command>
          <CommandInput placeholder="Type a command or search..." />
          <CommandList>
            <CommandEmpty>No results found.</CommandEmpty>
            <CommandGroup heading="Suggestions">
              <CommandItem value="calendar">
                <span>Calendar</span>
              </CommandItem>
              <CommandItem value="search-emoji">
                <span>Search Emoji</span>
              </CommandItem>
              <CommandItem value="calculator">
                <span>Calculator</span>
              </CommandItem>
            </CommandGroup>
            <CommandSeparator />
            <CommandGroup heading="Settings">
              <CommandItem value="profile">
                <span>Profile</span>
                <CommandShortcut>⌘P</CommandShortcut>
              </CommandItem>
              <CommandItem value="billing">
                <span>Billing</span>
                <CommandShortcut>⌘B</CommandShortcut>
              </CommandItem>
              <CommandItem value="settings">
                <span>Settings</span>
                <CommandShortcut>⌘S</CommandShortcut>
              </CommandItem>
            </CommandGroup>
          </CommandList>
        </Command>
      </CommandDialog>
    </div>
  </Example>
</template>
```

---

## Notes

- `CommandDialog` already renders `Command` internally. Do NOT nest `<Command>` inside `<CommandDialog>` in production code — it is already included. The examples above that wrap `Command` inside `CommandDialog` are from the shadcn-vue registry demo format and may double-wrap; in your own usage, simply put `CommandInput` + `CommandList` directly inside `CommandDialog`.
- `CommandItem` requires a unique `value` prop to identify items in the filter state.
- The `filterState.search` is automatically cleared when a `CommandItem` is selected (`@select` handler).
- `CommandEmpty` is only rendered when search is non-empty and no items match — never on initial render.
