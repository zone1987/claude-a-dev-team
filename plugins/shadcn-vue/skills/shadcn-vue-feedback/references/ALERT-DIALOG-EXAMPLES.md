# AlertDialog — Examples

## Contents

- [1. Basic Confirmation Dialog](#1-basic-confirmation-dialog)
- [2. Small Dialog](#2-small-dialog)
- [3. Destructive Action Dialog](#3-destructive-action-dialog)
- [4. AlertDialog Inside a Dialog](#4-alertdialog-inside-a-dialog)

## 1. Basic Confirmation Dialog

Standard two-button confirm dialog triggered by a button.

```vue
<script setup lang="ts">
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog"
import { Button } from "@/components/ui/button"
</script>

<template>
  <AlertDialog>
    <AlertDialogTrigger as-child>
      <Button variant="outline">Show Dialog</Button>
    </AlertDialogTrigger>
    <AlertDialogContent>
      <AlertDialogHeader>
        <AlertDialogTitle>Are you absolutely sure?</AlertDialogTitle>
        <AlertDialogDescription>
          This action cannot be undone. This will permanently delete your account
          and remove your data from our servers.
        </AlertDialogDescription>
      </AlertDialogHeader>
      <AlertDialogFooter>
        <AlertDialogCancel>Cancel</AlertDialogCancel>
        <AlertDialogAction>Continue</AlertDialogAction>
      </AlertDialogFooter>
    </AlertDialogContent>
  </AlertDialog>
</template>
```

---

## 2. Small Dialog

Uses `sm:max-w-sm` on the content to render a narrower dialog, useful for short messages.

```vue
<script setup lang="ts">
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog"
import { Button } from "@/components/ui/button"
</script>

<template>
  <AlertDialog>
    <AlertDialogTrigger as-child>
      <Button variant="outline">Small Dialog</Button>
    </AlertDialogTrigger>
    <AlertDialogContent class="sm:max-w-sm">
      <AlertDialogHeader>
        <AlertDialogTitle>Save changes?</AlertDialogTitle>
        <AlertDialogDescription>
          Your unsaved changes will be lost if you leave now.
        </AlertDialogDescription>
      </AlertDialogHeader>
      <AlertDialogFooter>
        <AlertDialogCancel>Discard</AlertDialogCancel>
        <AlertDialogAction>Save</AlertDialogAction>
      </AlertDialogFooter>
    </AlertDialogContent>
  </AlertDialog>
</template>
```

---

## 3. Destructive Action Dialog

Delete confirmation with a warning icon area and a destructive-styled action button.

```vue
<script setup lang="ts">
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog"
import { Button } from "@/components/ui/button"
import { Trash2 } from "lucide-vue-next"

function handleDelete() {
  // perform delete action
}
</script>

<template>
  <AlertDialog>
    <AlertDialogTrigger as-child>
      <Button variant="destructive">
        <Trash2 class="mr-2 h-4 w-4" />
        Delete Account
      </Button>
    </AlertDialogTrigger>
    <AlertDialogContent>
      <AlertDialogHeader>
        <div class="mx-auto mb-2 flex h-12 w-12 items-center justify-center rounded-full bg-destructive/10 sm:mx-0">
          <Trash2 class="h-6 w-6 text-destructive" />
        </div>
        <AlertDialogTitle>Delete account permanently?</AlertDialogTitle>
        <AlertDialogDescription>
          This will permanently delete your account, all your projects, and remove
          all associated data. This action <strong>cannot be undone</strong>.
        </AlertDialogDescription>
      </AlertDialogHeader>
      <AlertDialogFooter>
        <AlertDialogCancel>Keep account</AlertDialogCancel>
        <AlertDialogAction
          class="bg-destructive text-white hover:bg-destructive/90"
          @click="handleDelete"
        >
          Yes, delete account
        </AlertDialogAction>
      </AlertDialogFooter>
    </AlertDialogContent>
  </AlertDialog>
</template>
```

---

## 4. AlertDialog Inside a Dialog

An AlertDialog nested within a Dialog — useful for secondary confirmation inside a larger form/workflow.

```vue
<script setup lang="ts">
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
</script>

<template>
  <!-- Outer Dialog -->
  <Dialog>
    <DialogTrigger as-child>
      <Button variant="outline">Edit Profile</Button>
    </DialogTrigger>
    <DialogContent class="sm:max-w-[425px]">
      <DialogHeader>
        <DialogTitle>Edit profile</DialogTitle>
        <DialogDescription>
          Make changes to your profile here. Click save when you're done.
        </DialogDescription>
      </DialogHeader>

      <div class="grid gap-4 py-4">
        <div class="grid grid-cols-4 items-center gap-4">
          <Label for="name" class="text-right">Name</Label>
          <Input id="name" default-value="Pedro Duarte" class="col-span-3" />
        </div>
      </div>

      <DialogFooter class="gap-2">
        <!-- Inner AlertDialog for discarding changes -->
        <AlertDialog>
          <AlertDialogTrigger as-child>
            <Button variant="outline">Discard changes</Button>
          </AlertDialogTrigger>
          <AlertDialogContent>
            <AlertDialogHeader>
              <AlertDialogTitle>Discard changes?</AlertDialogTitle>
              <AlertDialogDescription>
                Any unsaved changes will be permanently lost.
              </AlertDialogDescription>
            </AlertDialogHeader>
            <AlertDialogFooter>
              <AlertDialogCancel>Keep editing</AlertDialogCancel>
              <AlertDialogAction>Discard</AlertDialogAction>
            </AlertDialogFooter>
          </AlertDialogContent>
        </AlertDialog>

        <Button type="submit">Save changes</Button>
      </DialogFooter>
    </DialogContent>
  </Dialog>
</template>
```
