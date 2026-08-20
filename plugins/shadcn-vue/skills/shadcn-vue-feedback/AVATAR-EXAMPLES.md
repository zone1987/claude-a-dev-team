# Avatar — Examples

## Contents

- [1. Basic avatar with image and fallback](#1-basic-avatar-with-image-and-fallback)
- [2. Multiple sizes via class override](#2-multiple-sizes-via-class-override)
- [3. Avatar group (overlapping layout)](#3-avatar-group-overlapping-layout)
- [4. Avatar with custom fallback styling](#4-avatar-with-custom-fallback-styling)

## 1. Basic avatar with image and fallback

The most common usage: show a profile photo with two-letter initials as fallback.

```vue
<script setup lang="ts">
import { Avatar, AvatarImage, AvatarFallback } from "@/components/ui/avatar"
</script>

<template>
  <Avatar>
    <AvatarImage src="https://github.com/shadcn.png" alt="@shadcn" />
    <AvatarFallback>SC</AvatarFallback>
  </Avatar>
</template>
```

`AvatarFallback` is only visible until the image loads. Once the image is ready, it hides automatically.

---

## 2. Multiple sizes via class override

The default size is `size-8` (32 px). Pass a Tailwind class to `Avatar` to override it.

```vue
<script setup lang="ts">
import { Avatar, AvatarImage, AvatarFallback } from "@/components/ui/avatar"
</script>

<template>
  <div class="flex items-center gap-4">
    <!-- Small: 24 px -->
    <Avatar class="size-6">
      <AvatarImage src="https://github.com/shadcn.png" alt="@shadcn" />
      <AvatarFallback class="text-xs">SC</AvatarFallback>
    </Avatar>

    <!-- Default: 32 px -->
    <Avatar>
      <AvatarImage src="https://github.com/shadcn.png" alt="@shadcn" />
      <AvatarFallback>SC</AvatarFallback>
    </Avatar>

    <!-- Large: 48 px -->
    <Avatar class="size-12">
      <AvatarImage src="https://github.com/shadcn.png" alt="@shadcn" />
      <AvatarFallback>SC</AvatarFallback>
    </Avatar>

    <!-- Extra large: 64 px -->
    <Avatar class="size-16">
      <AvatarImage src="https://github.com/shadcn.png" alt="@shadcn" />
      <AvatarFallback class="text-xl">SC</AvatarFallback>
    </Avatar>
  </div>
</template>
```

> Note: The extended `size` prop shown in some shadcn-vue example pages (e.g. `AvatarSizes`) comes from the `AvatarGroup` / new-york-v4 extension layer and is not part of the base `Avatar` component.

---

## 3. Avatar group (overlapping layout)

A stacked group of avatars using a negative margin trick — no extra component needed.

```vue
<script setup lang="ts">
import { Avatar, AvatarImage, AvatarFallback } from "@/components/ui/avatar"

const users = [
  { src: "https://github.com/shadcn.png",   alt: "@shadcn",   initials: "SC" },
  { src: "https://github.com/radix-ui.png", alt: "@radix",    initials: "RX" },
  { src: "",                                 alt: "@unknown",  initials: "UN" },
  { src: "https://github.com/vercel.png",   alt: "@vercel",   initials: "VC" },
]
</script>

<template>
  <!-- Each avatar overlaps the previous one by half its width (-ml-3) -->
  <div class="flex items-center">
    <Avatar
      v-for="(user, i) in users"
      :key="i"
      class="ring-2 ring-background"
      :class="{ '-ml-3': i > 0 }"
    >
      <AvatarImage :src="user.src" :alt="user.alt" />
      <AvatarFallback>{{ user.initials }}</AvatarFallback>
    </Avatar>
  </div>
</template>
```

`ring-2 ring-background` adds a white ring around each avatar so the overlap looks clean. Adjust `-ml-3` (−12 px) relative to your chosen avatar size.

> For a built-in `AvatarGroup` component with count overflow (e.g. `+3 more`), see the `AvatarGroup` / `AvatarGroupCount` extensions from the reka/new-york-v4 layer — those are not part of the base install.

---

## 4. Avatar with custom fallback styling

Combine an icon and custom background colour in the fallback slot.

```vue
<script setup lang="ts">
import { Avatar, AvatarImage, AvatarFallback } from "@/components/ui/avatar"
// Any icon library — example uses lucide-vue-next
import { UserIcon } from "lucide-vue-next"
</script>

<template>
  <div class="flex items-center gap-4">
    <!-- Coloured initial -->
    <Avatar class="size-10">
      <AvatarImage src="" alt="No image" />
      <AvatarFallback class="bg-blue-500 text-white font-semibold">
        AG
      </AvatarFallback>
    </Avatar>

    <!-- Icon fallback -->
    <Avatar class="size-10">
      <AvatarImage src="" alt="No image" />
      <AvatarFallback class="bg-muted text-muted-foreground">
        <UserIcon class="size-5" />
      </AvatarFallback>
    </Avatar>

    <!-- Delayed fallback — avoids flash on fast connections -->
    <Avatar class="size-10">
      <AvatarImage src="https://github.com/shadcn.png" alt="@shadcn" />
      <AvatarFallback :delay-ms="600">SC</AvatarFallback>
    </Avatar>
  </div>
</template>
```

The `delayMs` prop on `AvatarFallback` suppresses the fallback for the given number of milliseconds, preventing a brief flash when the image loads quickly.
