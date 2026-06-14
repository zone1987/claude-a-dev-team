# Menubar — Beispiele

## Beispiel 1: Basic Menubar (MenubarBasic.vue)

File- und Edit-Menu mit Shortcuts und Separator.

```vue
<script setup lang="ts">
import {
  Menubar,
  MenubarContent,
  MenubarGroup,
  MenubarItem,
  MenubarMenu,
  MenubarSeparator,
  MenubarShortcut,
  MenubarTrigger,
} from "@/components/ui/menubar"
</script>

<template>
  <Menubar>
    <MenubarMenu>
      <MenubarTrigger>File</MenubarTrigger>
      <MenubarContent>
        <MenubarGroup>
          <MenubarItem>
            New Tab <MenubarShortcut>⌘T</MenubarShortcut>
          </MenubarItem>
          <MenubarItem>
            New Window <MenubarShortcut>⌘N</MenubarShortcut>
          </MenubarItem>
          <MenubarItem :disabled="true">
            New Incognito Window
          </MenubarItem>
        </MenubarGroup>
        <MenubarSeparator />
        <MenubarGroup>
          <MenubarItem>
            Print... <MenubarShortcut>⌘P</MenubarShortcut>
          </MenubarItem>
        </MenubarGroup>
      </MenubarContent>
    </MenubarMenu>
    <MenubarMenu>
      <MenubarTrigger>Edit</MenubarTrigger>
      <MenubarContent>
        <MenubarGroup>
          <MenubarItem>
            Undo <MenubarShortcut>⌘Z</MenubarShortcut>
          </MenubarItem>
          <MenubarItem>
            Redo <MenubarShortcut>⇧⌘Z</MenubarShortcut>
          </MenubarItem>
        </MenubarGroup>
        <MenubarSeparator />
        <MenubarGroup>
          <MenubarItem>Cut</MenubarItem>
          <MenubarItem>Copy</MenubarItem>
          <MenubarItem>Paste</MenubarItem>
        </MenubarGroup>
      </MenubarContent>
    </MenubarMenu>
  </Menubar>
</template>
```

---

## Beispiel 2: Menubar with Submenu (MenubarWithSubmenu.vue)

Untermenus mit `MenubarSub`, `MenubarSubTrigger`, `MenubarSubContent`.

```vue
<script setup lang="ts">
import {
  Menubar,
  MenubarContent,
  MenubarGroup,
  MenubarItem,
  MenubarMenu,
  MenubarSeparator,
  MenubarShortcut,
  MenubarSub,
  MenubarSubContent,
  MenubarSubTrigger,
  MenubarTrigger,
} from "@/components/ui/menubar"
</script>

<template>
  <Menubar>
    <MenubarMenu>
      <MenubarTrigger>File</MenubarTrigger>
      <MenubarContent>
        <MenubarSub>
          <MenubarSubTrigger>Share</MenubarSubTrigger>
          <MenubarSubContent>
            <MenubarGroup>
              <MenubarItem>Email link</MenubarItem>
              <MenubarItem>Messages</MenubarItem>
              <MenubarItem>Notes</MenubarItem>
            </MenubarGroup>
          </MenubarSubContent>
        </MenubarSub>
        <MenubarSeparator />
        <MenubarGroup>
          <MenubarItem>
            Print... <MenubarShortcut>⌘P</MenubarShortcut>
          </MenubarItem>
        </MenubarGroup>
      </MenubarContent>
    </MenubarMenu>
    <MenubarMenu>
      <MenubarTrigger>Edit</MenubarTrigger>
      <MenubarContent>
        <MenubarGroup>
          <MenubarItem>
            Undo <MenubarShortcut>⌘Z</MenubarShortcut>
          </MenubarItem>
          <MenubarItem>
            Redo <MenubarShortcut>⇧⌘Z</MenubarShortcut>
          </MenubarItem>
        </MenubarGroup>
        <MenubarSeparator />
        <MenubarSub>
          <MenubarSubTrigger>Find</MenubarSubTrigger>
          <MenubarSubContent>
            <MenubarGroup>
              <MenubarItem>Find...</MenubarItem>
              <MenubarItem>Find Next</MenubarItem>
              <MenubarItem>Find Previous</MenubarItem>
            </MenubarGroup>
          </MenubarSubContent>
        </MenubarSub>
        <MenubarSeparator />
        <MenubarGroup>
          <MenubarItem>Cut</MenubarItem>
          <MenubarItem>Copy</MenubarItem>
          <MenubarItem>Paste</MenubarItem>
        </MenubarGroup>
      </MenubarContent>
    </MenubarMenu>
  </Menubar>
</template>
```

---

## Beispiel 3: Menubar with Checkboxes (MenubarWithCheckboxes.vue)

`MenubarCheckboxItem` fur umschaltbare Optionen.

```vue
<script setup lang="ts">
import {
  Menubar,
  MenubarCheckboxItem,
  MenubarContent,
  MenubarGroup,
  MenubarItem,
  MenubarMenu,
  MenubarSeparator,
  MenubarShortcut,
  MenubarTrigger,
} from "@/components/ui/menubar"
</script>

<template>
  <Menubar>
    <MenubarMenu>
      <MenubarTrigger>View</MenubarTrigger>
      <MenubarContent class="w-64">
        <MenubarGroup>
          <MenubarCheckboxItem>
            Always Show Bookmarks Bar
          </MenubarCheckboxItem>
          <MenubarCheckboxItem :checked="true">
            Always Show Full URLs
          </MenubarCheckboxItem>
        </MenubarGroup>
        <MenubarSeparator />
        <MenubarGroup>
          <MenubarItem :inset="true">
            Reload <MenubarShortcut>⌘R</MenubarShortcut>
          </MenubarItem>
          <MenubarItem :disabled="true" :inset="true">
            Force Reload <MenubarShortcut>⇧⌘R</MenubarShortcut>
          </MenubarItem>
        </MenubarGroup>
      </MenubarContent>
    </MenubarMenu>
    <MenubarMenu>
      <MenubarTrigger>Format</MenubarTrigger>
      <MenubarContent>
        <MenubarCheckboxItem :checked="true">
          Strikethrough
        </MenubarCheckboxItem>
        <MenubarCheckboxItem>Code</MenubarCheckboxItem>
        <MenubarCheckboxItem>Superscript</MenubarCheckboxItem>
      </MenubarContent>
    </MenubarMenu>
  </Menubar>
</template>
```

---

## Beispiel 4: Menubar with Radio Groups (MenubarWithRadio.vue)

`MenubarRadioGroup` + `MenubarRadioItem` mit `v-model`.

```vue
<script setup lang="ts">
import { ref } from "vue"
import {
  Menubar,
  MenubarContent,
  MenubarGroup,
  MenubarItem,
  MenubarMenu,
  MenubarRadioGroup,
  MenubarRadioItem,
  MenubarSeparator,
  MenubarTrigger,
} from "@/components/ui/menubar"

const user = ref("benoit")
const theme = ref("system")
</script>

<template>
  <Menubar>
    <MenubarMenu>
      <MenubarTrigger>Profiles</MenubarTrigger>
      <MenubarContent>
        <MenubarRadioGroup v-model="user">
          <MenubarRadioItem value="andy">Andy</MenubarRadioItem>
          <MenubarRadioItem value="benoit">Benoit</MenubarRadioItem>
          <MenubarRadioItem value="luis">Luis</MenubarRadioItem>
        </MenubarRadioGroup>
        <MenubarSeparator />
        <MenubarGroup>
          <MenubarItem inset>Edit...</MenubarItem>
          <MenubarItem inset>Add Profile...</MenubarItem>
        </MenubarGroup>
      </MenubarContent>
    </MenubarMenu>
    <MenubarMenu>
      <MenubarTrigger>Theme</MenubarTrigger>
      <MenubarContent>
        <MenubarRadioGroup v-model="theme">
          <MenubarRadioItem value="light">Light</MenubarRadioItem>
          <MenubarRadioItem value="dark">Dark</MenubarRadioItem>
          <MenubarRadioItem value="system">System</MenubarRadioItem>
        </MenubarRadioGroup>
      </MenubarContent>
    </MenubarMenu>
  </Menubar>
</template>
```

---

## Quellen
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/menubar/MenubarBasic.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/menubar/MenubarWithSubmenu.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/menubar/MenubarWithCheckboxes.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/menubar/MenubarWithRadio.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/menubar/MenubarWithIcons.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/menubar/MenubarExample.vue`
