# Popover — Examples

## Contents

- [Example 1: Basic Popover (PopoverBasic.vue)](#example-1-basic-popover-popoverbasicvue)
- [Example 2: Popover with Form (PopoverWithForm.vue)](#example-2-popover-with-form-popoverwithformvue)
- [Example 3: Popover Alignments (PopoverAlignments.vue)](#example-3-popover-alignments-popoveralignmentsvue)
- [Example 4: Popover in Dialog (PopoverInDialog.vue)](#example-4-popover-in-dialog-popoverindialogvue)
- [Sources](#sources)

## Example 1: Basic Popover (PopoverBasic.vue)

Simple popover with a trigger button.

```vue
<script setup lang="ts">
import { Button } from "@/components/ui/button"
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"
</script>

<template>
  <Popover>
    <PopoverTrigger :as-child="true">
      <Button variant="outline">
        Open Popover
      </Button>
    </PopoverTrigger>
    <PopoverContent align="start">
      <div class="grid gap-4">
        <div class="space-y-2">
          <h4 class="font-medium leading-none">Dimensions</h4>
          <p class="text-sm text-muted-foreground">
            Set the dimensions for the layer.
          </p>
        </div>
      </div>
    </PopoverContent>
  </Popover>
</template>
```

---

## Example 2: Popover with Form (PopoverWithForm.vue)

Popover with form fields (Width/Height).

```vue
<script setup lang="ts">
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"
</script>

<template>
  <Popover>
    <PopoverTrigger :as-child="true">
      <Button variant="outline">
        Open Popover
      </Button>
    </PopoverTrigger>
    <PopoverContent class="w-64" align="start">
      <div class="grid gap-4">
        <div class="space-y-2">
          <h4 class="font-medium leading-none">Dimensions</h4>
          <p class="text-sm text-muted-foreground">
            Set the dimensions for the layer.
          </p>
        </div>
        <div class="grid gap-2">
          <div class="flex items-center gap-4">
            <Label html-for="width" class="w-1/2">Width</Label>
            <Input id="width" default-value="100%" />
          </div>
          <div class="flex items-center gap-4">
            <Label html-for="height" class="w-1/2">Height</Label>
            <Input id="height" default-value="25px" />
          </div>
        </div>
      </div>
    </PopoverContent>
  </Popover>
</template>
```

---

## Example 3: Popover Alignments (PopoverAlignments.vue)

Three alignment variants: `start`, `center`, `end`.

```vue
<script setup lang="ts">
import { Button } from "@/components/ui/button"
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"
</script>

<template>
  <div class="flex gap-6">
    <Popover>
      <PopoverTrigger :as-child="true">
        <Button variant="outline" size="sm">Start</Button>
      </PopoverTrigger>
      <PopoverContent align="start" class="w-40">
        Aligned to start
      </PopoverContent>
    </Popover>
    <Popover>
      <PopoverTrigger :as-child="true">
        <Button variant="outline" size="sm">Center</Button>
      </PopoverTrigger>
      <PopoverContent align="center" class="w-40">
        Aligned to center
      </PopoverContent>
    </Popover>
    <Popover>
      <PopoverTrigger :as-child="true">
        <Button variant="outline" size="sm">End</Button>
      </PopoverTrigger>
      <PopoverContent align="end" class="w-40">
        Aligned to end
      </PopoverContent>
    </Popover>
  </div>
</template>
```

---

## Example 4: Popover in Dialog (PopoverInDialog.vue)

Nested popover inside a dialog.

```vue
<script setup lang="ts">
import { Button } from "@/components/ui/button"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"
</script>

<template>
  <Dialog>
    <DialogTrigger :as-child="true">
      <Button variant="outline">
        Open Dialog
      </Button>
    </DialogTrigger>
    <DialogContent>
      <DialogHeader>
        <DialogTitle>Popover Example</DialogTitle>
        <DialogDescription>
          Click the button below to see the popover.
        </DialogDescription>
      </DialogHeader>
      <Popover>
        <PopoverTrigger :as-child="true">
          <Button variant="outline" class="w-fit">
            Open Popover
          </Button>
        </PopoverTrigger>
        <PopoverContent align="start">
          <div class="space-y-2">
            <h4 class="font-medium leading-none">Popover in Dialog</h4>
            <p class="text-sm text-muted-foreground">
              This popover appears inside a dialog.
            </p>
          </div>
        </PopoverContent>
      </Popover>
    </DialogContent>
  </Dialog>
</template>
```

---

## Sources
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/popover/PopoverBasic.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/popover/PopoverWithForm.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/popover/PopoverAlignments.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/popover/PopoverInDialog.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/popover/PopoverExample.vue`
