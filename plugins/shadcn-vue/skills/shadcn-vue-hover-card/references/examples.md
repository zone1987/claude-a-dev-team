# HoverCard — Beispiele

Quellen: `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/hover-card/`

## Alle Seiten (HoverCardSides.vue)

Hover Card auf allen vier Seiten.

```vue
<script setup lang="ts">
import { Button } from "@/registry/bases/reka/ui/button"
import {
  HoverCard,
  HoverCardContent,
  HoverCardTrigger,
} from "@/registry/bases/reka/ui/hover-card"

const HOVER_CARD_SIDES = ["top", "right", "bottom", "left"] as const
</script>

<template>
  <div class="flex flex-wrap items-center justify-center gap-4">
    <HoverCard
      v-for="side in HOVER_CARD_SIDES"
      :key="side"
      :open-delay="100"
      :close-delay="100"
    >
      <HoverCardTrigger :as-child="true">
        <Button variant="outline" class="capitalize">
          {{ side }}
        </Button>
      </HoverCardTrigger>
      <HoverCardContent :side="side" class="w-64">
        <div class="flex flex-col gap-2">
          <h4 class="font-medium">Hover Card</h4>
          <p>
            This hover card appears on the {{ side }} side of the trigger.
          </p>
        </div>
      </HoverCardContent>
    </HoverCard>
  </div>
</template>
```

## In einem Dialog (HoverCardInDialog.vue)

HoverCard innerhalb eines Dialogs.

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
import {
  HoverCard,
  HoverCardContent,
  HoverCardTrigger,
} from "@/registry/bases/reka/ui/hover-card"
</script>

<template>
  <Dialog>
    <DialogTrigger :as-child="true">
      <Button variant="outline">Open Dialog</Button>
    </DialogTrigger>
    <DialogContent>
      <DialogHeader>
        <DialogTitle>Hover Card Example</DialogTitle>
        <DialogDescription>
          Hover over the button below to see the hover card.
        </DialogDescription>
      </DialogHeader>
      <HoverCard :open-delay="100" :close-delay="100">
        <HoverCardTrigger :as-child="true">
          <Button variant="outline" class="w-fit">Hover me</Button>
        </HoverCardTrigger>
        <HoverCardContent class="w-64">
          <div class="flex flex-col gap-2">
            <h4 class="font-medium">Hover Card</h4>
            <p>
              This hover card appears inside a dialog.
            </p>
          </div>
        </HoverCardContent>
      </HoverCard>
    </DialogContent>
  </Dialog>
</template>
```

Quellen:
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/hover-card/HoverCardSides.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/hover-card/HoverCardInDialog.vue`
- `/tmp/shadcn-vue-repo/apps/v4/content/docs/components/hover-card.md`
