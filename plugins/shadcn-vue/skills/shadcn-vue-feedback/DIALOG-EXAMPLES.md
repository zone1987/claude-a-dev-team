# Dialog — Beispiele

Quellen: `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/dialog/`

## Contents

- [Dialog mit Formular (DialogWithForm.vue)](#dialog-mit-formular-dialogwithformvue)
- [Dialog ohne Close-Button (DialogNoCloseButton.vue)](#dialog-ohne-close-button-dialognoclosebuttonvue)
- [Scrollbarer Inhalt (DialogScrollableContent.vue)](#scrollbarer-inhalt-dialogscrollablecontentvue)
- [Dialog mit Sticky Footer (DialogWithStickyFooter.vue)](#dialog-mit-sticky-footer-dialogwithstickyfootervue)
- [Chat-Settings Dialog (DialogChatSettings.vue)](#chat-settings-dialog-dialogchatsettingsvue)
- [Hinweis: Dialog in ContextMenu/DropdownMenu](#hinweis-dialog-in-contextmenudropdownmenu)

## Dialog mit Formular (DialogWithForm.vue)

Dialog mit Profil-Bearbeitungs-Formular. Felder werden im Dialog behalten.

```vue
<script setup lang="ts">
import { Button } from "@/registry/bases/reka/ui/button"
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/registry/bases/reka/ui/dialog"
import { Field, FieldGroup, FieldLabel } from "@/registry/bases/reka/ui/field"
import { Input } from "@/registry/bases/reka/ui/input"
</script>

<template>
  <Dialog>
    <form>
      <DialogTrigger :as-child="true">
        <Button variant="outline">
          Edit Profile
        </Button>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Edit profile</DialogTitle>
          <DialogDescription>
            Make changes to your profile here. Click save when you're
            done. Your profile will be updated immediately.
          </DialogDescription>
        </DialogHeader>
        <FieldGroup>
          <Field>
            <FieldLabel html-for="name-1">
              Name
            </FieldLabel>
            <Input id="name-1" name="name" default-value="Pedro Duarte" />
          </Field>
          <Field>
            <FieldLabel html-for="username-1">
              Username
            </FieldLabel>
            <Input
              id="username-1"
              name="username"
              default-value="@peduarte"
            />
          </Field>
        </FieldGroup>
        <DialogFooter>
          <DialogClose :as-child="true">
            <Button variant="outline">
              Cancel
            </Button>
          </DialogClose>
          <Button type="submit">
            Save changes
          </Button>
        </DialogFooter>
      </DialogContent>
    </form>
  </Dialog>
</template>
```

## Dialog ohne Close-Button (DialogNoCloseButton.vue)

`:show-close-button="false"` entfernt das X oben rechts. Stattdessen schliessen via DialogClose im Footer.

```vue
<script setup lang="ts">
import { Button } from "@/registry/bases/reka/ui/button"
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/registry/bases/reka/ui/dialog"
</script>

<template>
  <Dialog>
    <DialogTrigger :as-child="true">
      <Button variant="outline">
        No Close Button
      </Button>
    </DialogTrigger>
    <DialogContent :show-close-button="false">
      <DialogHeader>
        <DialogTitle>No Close Button</DialogTitle>
        <DialogDescription>
          This dialog doesn't have a close button in the top-right
          corner.
        </DialogDescription>
      </DialogHeader>
      <DialogFooter>
        <DialogClose :as-child="true">
          <Button variant="outline">
            Close
          </Button>
        </DialogClose>
      </DialogFooter>
    </DialogContent>
  </Dialog>
</template>
```

## Scrollbarer Inhalt (DialogScrollableContent.vue)

Langer Inhalt mit `max-h-[70vh] overflow-y-auto` innerhalb des Dialogs.

```vue
<script setup lang="ts">
import { Button } from "@/registry/bases/reka/ui/button"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/registry/bases/reka/ui/dialog"
</script>

<template>
  <Dialog>
    <DialogTrigger :as-child="true">
      <Button variant="outline">
        Scrollable Content
      </Button>
    </DialogTrigger>
    <DialogContent>
      <DialogHeader>
        <DialogTitle>Scrollable Content</DialogTitle>
        <DialogDescription>
          This is a dialog with scrollable content.
        </DialogDescription>
      </DialogHeader>
      <div class="max-h-[70vh] overflow-y-auto">
        <p v-for="index in 10" :key="index" class="mb-4 leading-normal">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit...
        </p>
      </div>
    </DialogContent>
  </Dialog>
</template>
```

## Dialog mit Sticky Footer (DialogWithStickyFooter.vue)

Footer bleibt sichtbar, waehrend Inhalt scrollt.

```vue
<script setup lang="ts">
import { Button } from "@/registry/bases/reka/ui/button"
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/registry/bases/reka/ui/dialog"
</script>

<template>
  <Dialog>
    <DialogTrigger :as-child="true">
      <Button variant="outline">Sticky Footer</Button>
    </DialogTrigger>
    <DialogContent>
      <DialogHeader>
        <DialogTitle>Scrollable Content</DialogTitle>
        <DialogDescription>Dialog with scrollable content.</DialogDescription>
      </DialogHeader>
      <div class="max-h-[70vh] overflow-y-auto">
        <p v-for="index in 10" :key="index" class="mb-4">Lorem ipsum...</p>
      </div>
      <DialogFooter>
        <DialogClose :as-child="true">
          <Button variant="outline">Close</Button>
        </DialogClose>
      </DialogFooter>
    </DialogContent>
  </Dialog>
</template>
```

## Chat-Settings Dialog (DialogChatSettings.vue)

Komplexes Dialog-Beispiel mit Tabs, NativeSelect, Switch, InputGroup und mehr.

```vue
<script setup lang="ts">
import { ref } from "vue"
import { Button } from "@/registry/bases/reka/ui/button"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/registry/bases/reka/ui/dialog"
import {
  Field, FieldContent, FieldDescription, FieldGroup, FieldLabel, FieldSeparator,
  FieldSet, FieldTitle,
} from "@/registry/bases/reka/ui/field"
import {
  InputGroup, InputGroupAddon, InputGroupButton, InputGroupInput,
} from "@/registry/bases/reka/ui/input-group"
import {
  Select, SelectContent, SelectItem, SelectSeparator, SelectTrigger, SelectValue,
} from "@/registry/bases/reka/ui/select"
import { Switch } from "@/registry/bases/reka/ui/switch"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/registry/bases/reka/ui/tabs"

const tab = ref("general")
</script>

<template>
  <Dialog>
    <DialogTrigger :as-child="true">
      <Button variant="outline">Chat Settings</Button>
    </DialogTrigger>
    <DialogContent class="min-w-md">
      <DialogHeader>
        <DialogTitle>Chat Settings</DialogTitle>
        <DialogDescription>
          Customize your chat settings.
        </DialogDescription>
      </DialogHeader>
      <Tabs v-model="tab">
        <TabsList class="hidden w-full md:flex">
          <TabsTrigger value="general">General</TabsTrigger>
          <TabsTrigger value="notifications">Notifications</TabsTrigger>
          <TabsTrigger value="security">Security</TabsTrigger>
        </TabsList>
        <!-- TabsContent slots ... -->
      </Tabs>
    </DialogContent>
  </Dialog>
</template>
```

## Hinweis: Dialog in ContextMenu/DropdownMenu

Um einen Dialog innerhalb eines Context- oder Dropdown-Menus zu verwenden, muss der Dialog das Menu ummanteln:

```vue
<template>
  <Dialog>
    <ContextMenu>
      <ContextMenuTrigger>Right click</ContextMenuTrigger>
      <ContextMenuContent>
        <DialogTrigger as-child>
          <ContextMenuItem>Delete</ContextMenuItem>
        </DialogTrigger>
      </ContextMenuContent>
    </ContextMenu>
    <DialogContent>
      <DialogHeader>
        <DialogTitle>Are you absolutely sure?</DialogTitle>
      </DialogHeader>
      <DialogFooter>
        <Button type="submit">Confirm</Button>
      </DialogFooter>
    </DialogContent>
  </Dialog>
</template>
```

Quellen:
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/dialog/DialogWithForm.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/dialog/DialogNoCloseButton.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/dialog/DialogScrollableContent.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/dialog/DialogWithStickyFooter.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/dialog/DialogChatSettings.vue`
- `/tmp/shadcn-vue-repo/apps/v4/content/docs/components/dialog.md`
