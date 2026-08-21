# Separator — Examples

## Contents

- [SeparatorHorizontal.vue (Horizontal)](#separatorhorizontalvue-horizontal)
- [SeparatorVertical.vue (Vertical)](#separatorverticalvue-vertical)
- [SeparatorVerticalMenu.vue (Vertical Menu)](#separatorverticalmenuvue-vertical-menu)
- [SeparatorInList.vue (In List)](#separatorinlistvue-in-list)

## SeparatorHorizontal.vue (Horizontal)

```vue
<script setup lang="ts">
import { Example } from "@/registry/bases/reka/components/example"
import { Separator } from "@/registry/bases/reka/ui/separator"
</script>

<template>
  <Example title="Horizontal">
    <div class="style-lyra:text-xs/relaxed flex flex-col gap-4 text-sm">
      <div class="flex flex-col gap-1">
        <div class="font-medium leading-none">
          shadcn/ui
        </div>
        <div class="text-muted-foreground">
          The Foundation for your Design System
        </div>
      </div>
      <Separator />
      <div>
        A set of beautifully designed components that you can customize,
        extend, and build on.
      </div>
    </div>
  </Example>
</template>
```

## SeparatorVertical.vue (Vertical)

```vue
<script setup lang="ts">
import { Example } from "@/registry/bases/reka/components/example"
import { Separator } from "@/registry/bases/reka/ui/separator"
</script>

<template>
  <Example title="Vertical">
    <div class="style-lyra:text-xs/relaxed flex h-5 items-center gap-4 text-sm">
      <div>Blog</div>
      <Separator orientation="vertical" />
      <div>Docs</div>
      <Separator orientation="vertical" />
      <div>Source</div>
    </div>
  </Example>
</template>
```

## SeparatorVerticalMenu.vue (Vertical Menu)

```vue
<script setup lang="ts">
import { Example } from "@/registry/bases/reka/components/example"
import { Separator } from "@/registry/bases/reka/ui/separator"
</script>

<template>
  <Example title="Vertical Menu">
    <div class="style-lyra:text-xs/relaxed flex items-center gap-2 text-sm md:gap-4">
      <div class="flex flex-col gap-1">
        <span class="font-medium">Settings</span>
        <span class="text-xs text-muted-foreground">
          Manage preferences
        </span>
      </div>
      <Separator orientation="vertical" />
      <div class="flex flex-col gap-1">
        <span class="font-medium">Account</span>
        <span class="text-xs text-muted-foreground">
          Profile & security
        </span>
      </div>
      <Separator orientation="vertical" />
      <div class="flex flex-col gap-1">
        <span class="font-medium">Help</span>
        <span class="text-xs text-muted-foreground">Support & docs</span>
      </div>
    </div>
  </Example>
</template>
```

## SeparatorInList.vue (In List)

```vue
<script setup lang="ts">
import { Example } from "@/registry/bases/reka/components/example"
import { Separator } from "@/registry/bases/reka/ui/separator"
</script>

<template>
  <Example title="In List">
    <div class="style-lyra:text-xs/relaxed flex flex-col gap-2 text-sm">
      <dl class="flex items-center justify-between">
        <dt>Item 1</dt>
        <dd class="text-muted-foreground">
          Value 1
        </dd>
      </dl>
      <Separator />
      <dl class="flex items-center justify-between">
        <dt>Item 2</dt>
        <dd class="text-muted-foreground">
          Value 2
        </dd>
      </dl>
      <Separator />
      <dl class="flex items-center justify-between">
        <dt>Item 3</dt>
        <dd class="text-muted-foreground">
          Value 3
        </dd>
      </dl>
    </div>
  </Example>
</template>
```
