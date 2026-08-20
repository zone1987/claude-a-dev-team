# Drawer — Examples

Sources: `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/drawer/`

## Drawer with all sides (DrawerWithSides.vue)

Shows drawers for all four directions (top/right/bottom/left).

```vue
<script setup lang="ts">
import { Button } from "@/registry/bases/reka/ui/button"
import {
  Drawer,
  DrawerClose,
  DrawerContent,
  DrawerDescription,
  DrawerFooter,
  DrawerHeader,
  DrawerTitle,
  DrawerTrigger,
} from "@/registry/bases/reka/ui/drawer"

const DRAWER_SIDES = ["top", "right", "bottom", "left"] as const
</script>

<template>
  <div class="flex flex-wrap gap-2">
    <Drawer
      v-for="side in DRAWER_SIDES"
      :key="side"
      :direction="side === 'bottom' ? undefined : (side as 'top' | 'right' | 'left')"
    >
      <DrawerTrigger :as-child="true">
        <Button variant="outline" class="capitalize">
          {{ side }}
        </Button>
      </DrawerTrigger>
      <DrawerContent class="data-[vaul-drawer-direction=bottom]:max-h-[50vh] data-[vaul-drawer-direction=top]:max-h-[50vh]">
        <DrawerHeader>
          <DrawerTitle>Move Goal</DrawerTitle>
          <DrawerDescription>
            Set your daily activity goal.
          </DrawerDescription>
        </DrawerHeader>
        <div class="overflow-y-auto px-4">
          <p v-for="index in 10" :key="index" class="mb-4">
            Lorem ipsum dolor sit amet...
          </p>
        </div>
        <DrawerFooter>
          <Button>Submit</Button>
          <DrawerClose :as-child="true">
            <Button variant="outline">Cancel</Button>
          </DrawerClose>
        </DrawerFooter>
      </DrawerContent>
    </Drawer>
  </div>
</template>
```

## Drawer with scrollable content (DrawerScrollableContent.vue)

Drawer from the right with a scrollable content area.

```vue
<script setup lang="ts">
import { Button } from "@/registry/bases/reka/ui/button"
import {
  Drawer,
  DrawerClose,
  DrawerContent,
  DrawerDescription,
  DrawerFooter,
  DrawerHeader,
  DrawerTitle,
  DrawerTrigger,
} from "@/registry/bases/reka/ui/drawer"
</script>

<template>
  <Drawer direction="right">
    <DrawerTrigger :as-child="true">
      <Button variant="outline">
        Scrollable Content
      </Button>
    </DrawerTrigger>
    <DrawerContent>
      <DrawerHeader>
        <DrawerTitle>Move Goal</DrawerTitle>
        <DrawerDescription>Set your daily activity goal.</DrawerDescription>
      </DrawerHeader>
      <div class="no-scrollbar overflow-y-auto px-4">
        <p v-for="index in 10" :key="index" class="mb-4 leading-normal">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua...
        </p>
      </div>
      <DrawerFooter>
        <Button>Submit</Button>
        <DrawerClose :as-child="true">
          <Button variant="outline">
            Cancel
          </Button>
        </DrawerClose>
      </DrawerFooter>
    </DrawerContent>
  </Drawer>
</template>
```

Sources:
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/drawer/DrawerWithSides.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/drawer/DrawerScrollableContent.vue`
- `/tmp/shadcn-vue-repo/apps/v4/content/docs/components/drawer.md`
