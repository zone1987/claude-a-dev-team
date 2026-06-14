# Context Menu — Examples

Source: `registry/bases/reka/examples/context-menu/`

---

## 1. ContextMenuBasic

Simple 3-item context menu triggered by right-clicking an area.

```vue
<script setup lang="ts">
import {
  ContextMenu,
  ContextMenuContent,
  ContextMenuItem,
  ContextMenuTrigger,
} from "@/components/ui/context-menu"
</script>

<template>
  <ContextMenu>
    <ContextMenuTrigger class="flex h-[150px] w-[300px] items-center justify-center rounded-md border border-dashed text-sm">
      Right click here
    </ContextMenuTrigger>
    <ContextMenuContent class="w-64">
      <ContextMenuItem>Back</ContextMenuItem>
      <ContextMenuItem>Forward</ContextMenuItem>
      <ContextMenuItem>Reload</ContextMenuItem>
    </ContextMenuContent>
  </ContextMenu>
</template>
```

---

## 2. ContextMenuWithShortcuts

Items with keyboard shortcut hints.

```vue
<script setup lang="ts">
import {
  ContextMenu,
  ContextMenuContent,
  ContextMenuItem,
  ContextMenuShortcut,
  ContextMenuTrigger,
} from "@/components/ui/context-menu"
</script>

<template>
  <ContextMenu>
    <ContextMenuTrigger class="flex h-[150px] w-[300px] items-center justify-center rounded-md border border-dashed text-sm">
      Right click here
    </ContextMenuTrigger>
    <ContextMenuContent class="w-64">
      <ContextMenuItem>
        Back
        <ContextMenuShortcut>⌘[</ContextMenuShortcut>
      </ContextMenuItem>
      <ContextMenuItem>
        Forward
        <ContextMenuShortcut>⌘]</ContextMenuShortcut>
      </ContextMenuItem>
      <ContextMenuItem>
        Reload
        <ContextMenuShortcut>⌘R</ContextMenuShortcut>
      </ContextMenuItem>
      <ContextMenuItem>
        Save As...
        <ContextMenuShortcut>⌘S</ContextMenuShortcut>
      </ContextMenuItem>
      <ContextMenuItem>
        Print...
        <ContextMenuShortcut>⌘P</ContextMenuShortcut>
      </ContextMenuItem>
    </ContextMenuContent>
  </ContextMenu>
</template>
```

---

## 3. ContextMenuWithSubmenu

Nested submenu using `ContextMenuSub`, `ContextMenuSubTrigger`, and `ContextMenuSubContent`.

```vue
<script setup lang="ts">
import {
  ContextMenu,
  ContextMenuContent,
  ContextMenuItem,
  ContextMenuSeparator,
  ContextMenuShortcut,
  ContextMenuSub,
  ContextMenuSubContent,
  ContextMenuSubTrigger,
  ContextMenuTrigger,
} from "@/components/ui/context-menu"
</script>

<template>
  <ContextMenu>
    <ContextMenuTrigger class="flex h-[150px] w-[300px] items-center justify-center rounded-md border border-dashed text-sm">
      Right click here
    </ContextMenuTrigger>
    <ContextMenuContent class="w-64">
      <ContextMenuItem>
        Back
        <ContextMenuShortcut>⌘[</ContextMenuShortcut>
      </ContextMenuItem>
      <ContextMenuItem>
        Forward
        <ContextMenuShortcut>⌘]</ContextMenuShortcut>
      </ContextMenuItem>
      <ContextMenuItem>
        Reload
        <ContextMenuShortcut>⌘R</ContextMenuShortcut>
      </ContextMenuItem>
      <ContextMenuSub>
        <ContextMenuSubTrigger>More Tools</ContextMenuSubTrigger>
        <ContextMenuSubContent class="w-48">
          <ContextMenuItem>
            Save Page As...
            <ContextMenuShortcut>⌘S</ContextMenuShortcut>
          </ContextMenuItem>
          <ContextMenuItem>Create Shortcut...</ContextMenuItem>
          <ContextMenuItem>Name Window...</ContextMenuItem>
          <ContextMenuSeparator />
          <ContextMenuItem>Developer Tools</ContextMenuItem>
        </ContextMenuSubContent>
      </ContextMenuSub>
      <ContextMenuSeparator />
      <ContextMenuItem>Print...</ContextMenuItem>
    </ContextMenuContent>
  </ContextMenu>
</template>
```

---

## 4. ContextMenuWithGroups

Multiple groups using `ContextMenuGroup`, `ContextMenuLabel`, and `ContextMenuSeparator`.

```vue
<script setup lang="ts">
import {
  ContextMenu,
  ContextMenuContent,
  ContextMenuGroup,
  ContextMenuItem,
  ContextMenuLabel,
  ContextMenuSeparator,
  ContextMenuShortcut,
  ContextMenuSub,
  ContextMenuSubContent,
  ContextMenuSubTrigger,
  ContextMenuTrigger,
} from "@/components/ui/context-menu"
</script>

<template>
  <ContextMenu>
    <ContextMenuTrigger class="flex h-[150px] w-[300px] items-center justify-center rounded-md border border-dashed text-sm">
      Right click here
    </ContextMenuTrigger>
    <ContextMenuContent class="w-64">
      <ContextMenuGroup>
        <ContextMenuLabel>Navigation</ContextMenuLabel>
        <ContextMenuItem>
          Back
          <ContextMenuShortcut>⌘[</ContextMenuShortcut>
        </ContextMenuItem>
        <ContextMenuItem>
          Forward
          <ContextMenuShortcut>⌘]</ContextMenuShortcut>
        </ContextMenuItem>
        <ContextMenuItem>
          Reload
          <ContextMenuShortcut>⌘R</ContextMenuShortcut>
        </ContextMenuItem>
      </ContextMenuGroup>
      <ContextMenuSeparator />
      <ContextMenuGroup>
        <ContextMenuLabel>Tools</ContextMenuLabel>
        <ContextMenuSub>
          <ContextMenuSubTrigger>More Tools</ContextMenuSubTrigger>
          <ContextMenuSubContent class="w-48">
            <ContextMenuItem>
              Save Page As...
              <ContextMenuShortcut>⌘S</ContextMenuShortcut>
            </ContextMenuItem>
            <ContextMenuItem>Create Shortcut...</ContextMenuItem>
            <ContextMenuItem>Name Window...</ContextMenuItem>
            <ContextMenuSeparator />
            <ContextMenuItem>Developer Tools</ContextMenuItem>
          </ContextMenuSubContent>
        </ContextMenuSub>
        <ContextMenuItem>
          Print...
          <ContextMenuShortcut>⌘P</ContextMenuShortcut>
        </ContextMenuItem>
      </ContextMenuGroup>
    </ContextMenuContent>
  </ContextMenu>
</template>
```

---

## 5. ContextMenuWithCheckboxes

Items that can be toggled on/off independently.

```vue
<script setup lang="ts">
import { ref } from "vue"
import {
  ContextMenu,
  ContextMenuCheckboxItem,
  ContextMenuContent,
  ContextMenuItem,
  ContextMenuSeparator,
  ContextMenuTrigger,
} from "@/components/ui/context-menu"

const showBookmarks = ref(true)
const showFullUrls = ref(false)
</script>

<template>
  <ContextMenu>
    <ContextMenuTrigger class="flex h-[150px] w-[300px] items-center justify-center rounded-md border border-dashed text-sm">
      Right click here
    </ContextMenuTrigger>
    <ContextMenuContent class="w-64">
      <ContextMenuItem>Back</ContextMenuItem>
      <ContextMenuItem>Forward</ContextMenuItem>
      <ContextMenuItem>Reload</ContextMenuItem>
      <ContextMenuSeparator />
      <ContextMenuCheckboxItem v-model:checked="showBookmarks">
        Show Bookmarks Bar
      </ContextMenuCheckboxItem>
      <ContextMenuCheckboxItem v-model:checked="showFullUrls">
        Show Full URLs
      </ContextMenuCheckboxItem>
    </ContextMenuContent>
  </ContextMenu>
</template>
```

---

## 6. ContextMenuWithRadio

Mutually exclusive selection using `ContextMenuRadioGroup` and `ContextMenuRadioItem`.

```vue
<script setup lang="ts">
import { ref } from "vue"
import {
  ContextMenu,
  ContextMenuContent,
  ContextMenuItem,
  ContextMenuLabel,
  ContextMenuRadioGroup,
  ContextMenuRadioItem,
  ContextMenuSeparator,
  ContextMenuTrigger,
} from "@/components/ui/context-menu"

const position = ref("bottom")
</script>

<template>
  <ContextMenu>
    <ContextMenuTrigger class="flex h-[150px] w-[300px] items-center justify-center rounded-md border border-dashed text-sm">
      Right click here
    </ContextMenuTrigger>
    <ContextMenuContent class="w-64">
      <ContextMenuItem>Back</ContextMenuItem>
      <ContextMenuItem>Forward</ContextMenuItem>
      <ContextMenuSeparator />
      <ContextMenuLabel>Panel Position</ContextMenuLabel>
      <ContextMenuRadioGroup v-model="position">
        <ContextMenuRadioItem value="top">Top</ContextMenuRadioItem>
        <ContextMenuRadioItem value="bottom">Bottom</ContextMenuRadioItem>
        <ContextMenuRadioItem value="right">Right</ContextMenuRadioItem>
      </ContextMenuRadioGroup>
    </ContextMenuContent>
  </ContextMenu>
</template>
```

---

## Notes

- `ContextMenuTrigger` wraps the right-clickable area. It does not add any visual styling by default — style it yourself.
- `ContextMenuContent` is rendered in a portal (appended to `<body>`) to avoid z-index and overflow clipping issues.
- `ContextMenuSubTrigger` automatically adds a `ChevronRight` icon at the end.
- `ContextMenuCheckboxItem` uses `v-model:checked` (bound to a `boolean` ref).
- `ContextMenuRadioGroup` uses `v-model` (bound to the selected `value` string); `ContextMenuRadioItem` requires a `value` prop.
- Use `ContextMenuSeparator` between logical groups or between sections of distinct item types (e.g. normal items vs. checkboxes).
- `variant="destructive"` on `ContextMenuItem` renders the item in red to indicate destructive actions.
