# DropdownMenu — Examples

Sources: `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/dropdown-menu/`

## Contents

- [Basic (DropdownMenuBasic.vue)](#basic-dropdownmenubasicvue)
- [With checkboxes (DropdownMenuWithCheckboxes)](#with-checkboxes-dropdownmenuwithcheckboxes)
- [With radio group (DropdownMenuWithRadio)](#with-radio-group-dropdownmenuwithradio)
- [With shortcuts and submenu](#with-shortcuts-and-submenu)
- [In a dialog (DropdownMenuInDialog)](#in-a-dialog-dropdownmenuindialog)

## Basic (DropdownMenuBasic.vue)

```vue
<script setup lang="ts">
import { Button } from "@/registry/bases/reka/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/registry/bases/reka/ui/dropdown-menu"
</script>

<template>
  <DropdownMenu>
    <DropdownMenuTrigger :as-child="true">
      <Button variant="outline" class="w-fit">
        Open
      </Button>
    </DropdownMenuTrigger>
    <DropdownMenuContent>
      <DropdownMenuGroup>
        <DropdownMenuLabel>My Account</DropdownMenuLabel>
        <DropdownMenuItem>Profile</DropdownMenuItem>
        <DropdownMenuItem>Billing</DropdownMenuItem>
        <DropdownMenuItem>Settings</DropdownMenuItem>
      </DropdownMenuGroup>
      <DropdownMenuSeparator />
      <DropdownMenuGroup>
        <DropdownMenuItem>GitHub</DropdownMenuItem>
        <DropdownMenuItem>Support</DropdownMenuItem>
        <DropdownMenuItem :disabled="true">
          API
        </DropdownMenuItem>
      </DropdownMenuGroup>
    </DropdownMenuContent>
  </DropdownMenu>
</template>
```

## With checkboxes (DropdownMenuWithCheckboxes)

```vue
<script setup lang="ts">
import { ref } from "vue"
import { Button } from "@/registry/bases/reka/ui/button"
import {
  DropdownMenu,
  DropdownMenuCheckboxItem,
  DropdownMenuContent,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/registry/bases/reka/ui/dropdown-menu"

const notifications = ref({
  email: true,
  sms: false,
  push: true,
})
</script>

<template>
  <DropdownMenu>
    <DropdownMenuTrigger :as-child="true">
      <Button variant="outline">Notifications</Button>
    </DropdownMenuTrigger>
    <DropdownMenuContent>
      <DropdownMenuLabel>Notifications</DropdownMenuLabel>
      <DropdownMenuSeparator />
      <DropdownMenuCheckboxItem v-model:checked="notifications.email">
        Email
      </DropdownMenuCheckboxItem>
      <DropdownMenuCheckboxItem v-model:checked="notifications.sms">
        SMS
      </DropdownMenuCheckboxItem>
      <DropdownMenuCheckboxItem v-model:checked="notifications.push">
        Push
      </DropdownMenuCheckboxItem>
    </DropdownMenuContent>
  </DropdownMenu>
</template>
```

## With radio group (DropdownMenuWithRadio)

```vue
<script setup lang="ts">
import { ref } from "vue"
import { Button } from "@/registry/bases/reka/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuLabel,
  DropdownMenuRadioGroup,
  DropdownMenuRadioItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/registry/bases/reka/ui/dropdown-menu"

const theme = ref("light")
</script>

<template>
  <DropdownMenu>
    <DropdownMenuTrigger :as-child="true">
      <Button variant="outline">Theme</Button>
    </DropdownMenuTrigger>
    <DropdownMenuContent>
      <DropdownMenuLabel>Theme</DropdownMenuLabel>
      <DropdownMenuSeparator />
      <DropdownMenuRadioGroup v-model="theme">
        <DropdownMenuRadioItem value="light">Light</DropdownMenuRadioItem>
        <DropdownMenuRadioItem value="dark">Dark</DropdownMenuRadioItem>
        <DropdownMenuRadioItem value="system">System</DropdownMenuRadioItem>
      </DropdownMenuRadioGroup>
    </DropdownMenuContent>
  </DropdownMenu>
</template>
```

## With shortcuts and submenu

```vue
<script setup lang="ts">
import { Button } from "@/registry/bases/reka/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuShortcut,
  DropdownMenuSub,
  DropdownMenuSubContent,
  DropdownMenuSubTrigger,
  DropdownMenuTrigger,
} from "@/registry/bases/reka/ui/dropdown-menu"
</script>

<template>
  <DropdownMenu>
    <DropdownMenuTrigger :as-child="true">
      <Button variant="outline">File</Button>
    </DropdownMenuTrigger>
    <DropdownMenuContent>
      <DropdownMenuGroup>
        <DropdownMenuLabel>File</DropdownMenuLabel>
        <DropdownMenuItem>
          New File
          <DropdownMenuShortcut>⌘N</DropdownMenuShortcut>
        </DropdownMenuItem>
        <DropdownMenuSub>
          <DropdownMenuSubTrigger>Open Recent</DropdownMenuSubTrigger>
          <DropdownMenuSubContent>
            <DropdownMenuItem>Project Alpha</DropdownMenuItem>
            <DropdownMenuItem>Project Beta</DropdownMenuItem>
          </DropdownMenuSubContent>
        </DropdownMenuSub>
        <DropdownMenuSeparator />
        <DropdownMenuItem>
          Save
          <DropdownMenuShortcut>⌘S</DropdownMenuShortcut>
        </DropdownMenuItem>
      </DropdownMenuGroup>
      <DropdownMenuSeparator />
      <DropdownMenuItem variant="destructive">
        Sign Out
        <DropdownMenuShortcut>⇧⌘Q</DropdownMenuShortcut>
      </DropdownMenuItem>
    </DropdownMenuContent>
  </DropdownMenu>
</template>
```

## In a dialog (DropdownMenuInDialog)

The dialog must wrap the DropdownMenu:

```vue
<template>
  <Dialog>
    <DropdownMenu>
      <DropdownMenuTrigger :as-child="true">
        <Button variant="outline">Open Menu</Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent>
        <DropdownMenuGroup>
          <DropdownMenuLabel>Actions</DropdownMenuLabel>
          <DropdownMenuItem>Action 1</DropdownMenuItem>
          <DialogTrigger as-child>
            <DropdownMenuItem>Open Dialog</DropdownMenuItem>
          </DialogTrigger>
        </DropdownMenuGroup>
      </DropdownMenuContent>
    </DropdownMenu>
    <DialogContent>
      <DialogHeader>
        <DialogTitle>From Dropdown</DialogTitle>
      </DialogHeader>
    </DialogContent>
  </Dialog>
</template>
```

Sources:
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/dropdown-menu/`
- `/tmp/shadcn-vue-repo/apps/v4/content/docs/components/dropdown-menu.md`
