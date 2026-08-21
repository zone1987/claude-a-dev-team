# AspectRatio — Examples

## 16:9 (Landscape / Video)

```vue
<script setup lang="ts">
import { AspectRatio } from "@/components/ui/aspect-ratio"
</script>

<template>
  <AspectRatio :ratio="16 / 9" class="bg-muted rounded-lg">
    <img
      src="https://avatar.vercel.sh/shadcn1"
      alt="Photo"
      class="h-full w-full rounded-lg object-cover"
    >
  </AspectRatio>
</template>
```

## 21:9 (Ultrawide / Cinema)

```vue
<script setup lang="ts">
import { AspectRatio } from "@/components/ui/aspect-ratio"
</script>

<template>
  <AspectRatio :ratio="21 / 9" class="bg-muted rounded-lg">
    <img
      src="https://avatar.vercel.sh/shadcn1"
      alt="Photo"
      class="h-full w-full rounded-lg object-cover"
    >
  </AspectRatio>
</template>
```

## 1:1 (Square / Avatar)

```vue
<script setup lang="ts">
import { AspectRatio } from "@/components/ui/aspect-ratio"
</script>

<template>
  <AspectRatio :ratio="1 / 1" class="bg-muted rounded-lg">
    <img
      src="https://avatar.vercel.sh/shadcn1"
      alt="Photo"
      class="h-full w-full rounded-lg object-cover"
    >
  </AspectRatio>
</template>
```

## 9:16 (Portrait / Story)

```vue
<script setup lang="ts">
import { AspectRatio } from "@/components/ui/aspect-ratio"
</script>

<template>
  <AspectRatio :ratio="9 / 16" class="bg-muted rounded-lg">
    <img
      src="https://avatar.vercel.sh/shadcn1"
      alt="Photo"
      class="h-full w-full rounded-lg object-cover"
    >
  </AspectRatio>
</template>
```
