---
name: shadcn-vue-skeleton
description: >
  shadcn-vue Skeleton component (animate-pulse placeholder, Tailwind v4 Vue SFC).
  Triggers: "shadcn-vue skeleton", "skeleton loader vue", "ladeplatzhalter vue",
  "skeleton component vue", "placeholder loading vue", "skeleton vue shadcn"
---

# shadcn-vue Skeleton Component

## Overview

The `Skeleton` component is a simple loading placeholder that uses a pulsing animation
(`animate-pulse`) to indicate that content is being loaded. It is a pure CSS component
with no reka-ui dependency — just a styled `div` with `bg-primary/10` background.

## Usage

```vue
<script setup lang="ts">
import { Skeleton } from '@/components/ui/skeleton'
</script>

<template>
  <Skeleton class="w-[100px] h-[20px] rounded-full" />
</template>
```

## Common Patterns

### Avatar with Text

```vue
<div class="flex items-center gap-4">
  <Skeleton class="size-10 rounded-full" />
  <div class="grid gap-2">
    <Skeleton class="h-4 w-[150px]" />
    <Skeleton class="h-4 w-[100px]" />
  </div>
</div>
```

### Card

```vue
<Card>
  <CardHeader>
    <Skeleton class="h-4 w-2/3" />
    <Skeleton class="h-4 w-1/2" />
  </CardHeader>
  <CardContent>
    <Skeleton class="aspect-square w-full" />
  </CardContent>
</Card>
```

### Table rows

```vue
<div class="flex w-full flex-col gap-2">
  <div class="flex gap-4">
    <Skeleton class="h-4 flex-1" />
    <Skeleton class="h-4 w-24" />
    <Skeleton class="h-4 w-20" />
  </div>
</div>
```

## Styling Tips

- Use `rounded-full` for circular skeletons (avatars)
- Use `rounded-md` for card/block skeletons
- Combine multiple Skeleton elements to mimic the actual layout
- Match widths and heights to approximate the real content dimensions
