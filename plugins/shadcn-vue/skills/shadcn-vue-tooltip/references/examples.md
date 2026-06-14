# Tooltip — Examples

## Basic

Tooltip on a button trigger using `asChild`.

```vue
<script setup lang="ts">
import { Button } from "@/components/ui/button"
import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip"
</script>

<template>
  <Tooltip>
    <TooltipTrigger :as-child="true">
      <Button variant="outline" class="w-fit">
        Show Tooltip
      </Button>
    </TooltipTrigger>
    <TooltipContent>
      <p>Add to library</p>
    </TooltipContent>
  </Tooltip>
</template>
```

Source: `registry/bases/reka/examples/tooltip/TooltipBasic.vue`

---

## All Four Sides

Demonstrates `side` prop with top, right, bottom, left variants.

```vue
<script setup lang="ts">
import { Button } from "@/components/ui/button"
import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip"

const sides = ["top", "right", "bottom", "left"] as const
</script>

<template>
  <div class="flex flex-wrap gap-2">
    <Tooltip v-for="side in sides" :key="side">
      <TooltipTrigger :as-child="true">
        <Button variant="outline" class="w-fit capitalize">
          {{ side }}
        </Button>
      </TooltipTrigger>
      <TooltipContent :side="side">
        <p>Add to library</p>
      </TooltipContent>
    </Tooltip>
  </div>
</template>
```

Source: `registry/bases/reka/examples/tooltip/TooltipSides.vue`

---

## With Icon Trigger

Icon-only button as trigger; `sr-only` span for screen readers.

```vue
<script setup lang="ts">
import { Button } from "@/components/ui/button"
import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip"
import { InfoIcon } from "lucide-vue-next"
</script>

<template>
  <Tooltip>
    <TooltipTrigger :as-child="true">
      <Button variant="ghost" size="icon">
        <InfoIcon />
        <span class="sr-only">Info</span>
      </Button>
    </TooltipTrigger>
    <TooltipContent>
      <p>Additional information</p>
    </TooltipContent>
  </Tooltip>
</template>
```

Source: `registry/bases/reka/examples/tooltip/TooltipWithIcon.vue`

---

## Long Content

Multi-sentence tooltip — content wraps via `text-balance`.

```vue
<script setup lang="ts">
import { Button } from "@/components/ui/button"
import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip"
</script>

<template>
  <Tooltip>
    <TooltipTrigger :as-child="true">
      <Button variant="outline" class="w-fit">Show Tooltip</Button>
    </TooltipTrigger>
    <TooltipContent>
      To learn more about how this works, check out the docs. If you have
      any questions, please reach out to us.
    </TooltipContent>
  </Tooltip>
</template>
```

Source: `registry/bases/reka/examples/tooltip/TooltipLongContent.vue`

---

## On a Disabled Element

Wrap the disabled button in a `<span>` to capture pointer events.

```vue
<script setup lang="ts">
import { Button } from "@/components/ui/button"
import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip"
</script>

<template>
  <Tooltip>
    <TooltipTrigger :as-child="true">
      <span class="inline-block w-fit">
        <Button variant="outline" disabled>Disabled</Button>
      </span>
    </TooltipTrigger>
    <TooltipContent>
      <p>This feature is currently unavailable</p>
    </TooltipContent>
  </Tooltip>
</template>
```

Source: `registry/bases/reka/examples/tooltip/TooltipDisabled.vue`

---

## With Keyboard Shortcut

Tooltip content with a `<Kbd>` component showing a keyboard shortcut.

```vue
<script setup lang="ts">
import { Button } from "@/components/ui/button"
import { Kbd } from "@/components/ui/kbd"
import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip"
import { SaveIcon } from "lucide-vue-next"
</script>

<template>
  <Tooltip>
    <TooltipTrigger :as-child="true">
      <Button variant="outline" size="icon-sm">
        <SaveIcon />
      </Button>
    </TooltipTrigger>
    <TooltipContent class="pr-1.5">
      <div class="flex items-center gap-2">
        Save Changes <Kbd>S</Kbd>
      </div>
    </TooltipContent>
  </Tooltip>
</template>
```

Source: `registry/bases/reka/examples/tooltip/TooltipWithKeyboard.vue`

---

## On a Link

`asChild` on an `<a>` element — tooltip triggers on a text link.

```vue
<script setup lang="ts">
import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip"
</script>

<template>
  <Tooltip>
    <TooltipTrigger :as-child="true">
      <a
        href="#"
        class="w-fit text-sm text-primary underline-offset-4 hover:underline"
        @click.prevent
      >
        Learn more
      </a>
    </TooltipTrigger>
    <TooltipContent>
      <p>Click to read the documentation</p>
    </TooltipContent>
  </Tooltip>
</template>
```

Source: `registry/bases/reka/examples/tooltip/TooltipOnLink.vue`

---

## Formatted Content

Multi-line structured content inside the tooltip (title + subtitle).

```vue
<script setup lang="ts">
import { Button } from "@/components/ui/button"
import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip"
</script>

<template>
  <Tooltip>
    <TooltipTrigger :as-child="true">
      <Button variant="outline" class="w-fit">Status</Button>
    </TooltipTrigger>
    <TooltipContent>
      <div class="flex flex-col gap-1">
        <p class="font-semibold">Active</p>
        <p class="text-xs opacity-80">Last updated 2 hours ago</p>
      </div>
    </TooltipContent>
  </Tooltip>
</template>
```

Source: `registry/bases/reka/examples/tooltip/TooltipFormatted.vue`
