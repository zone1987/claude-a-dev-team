# Badge — Examples

## Contents

- [1. All variants](#1-all-variants)
- [2. Badge with icon on the left](#2-badge-with-icon-on-the-left)
- [3. Badge with icon on the right](#3-badge-with-icon-on-the-right)
- [4. Badge as a link (asChild)](#4-badge-as-a-link-aschild)
- [5. Custom colors](#5-custom-colors)
- [Bonus: Using `badgeVariants` without the component](#bonus-using-badgevariants-without-the-component)

## 1. All variants

```vue
<script setup lang="ts">
import { Badge } from "@/components/ui/badge"
</script>

<template>
  <div class="flex flex-wrap gap-2">
    <Badge variant="default">Default</Badge>
    <Badge variant="secondary">Secondary</Badge>
    <Badge variant="destructive">Destructive</Badge>
    <Badge variant="outline">Outline</Badge>
  </div>
</template>
```

## 2. Badge with icon on the left

SVG children are automatically sized to `size-3` (12px) and spaced with `gap-1`.

```vue
<script setup lang="ts">
import { Badge } from "@/components/ui/badge"
</script>

<template>
  <Badge variant="default">
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
      aria-hidden="true"
    >
      <circle cx="12" cy="12" r="10" />
      <polyline points="12 6 12 12 16 14" />
    </svg>
    In Progress
  </Badge>
</template>
```

With a Lucide icon (if `lucide-vue-next` is installed):

```vue
<script setup lang="ts">
import { Badge } from "@/components/ui/badge"
import { CheckCircle } from "lucide-vue-next"
</script>

<template>
  <Badge variant="default">
    <CheckCircle />
    Completed
  </Badge>
</template>
```

## 3. Badge with icon on the right

```vue
<script setup lang="ts">
import { Badge } from "@/components/ui/badge"
import { X } from "lucide-vue-next"
</script>

<template>
  <Badge variant="secondary">
    TypeScript
    <X />
  </Badge>
</template>
```

## 4. Badge as a link (asChild)

Use `asChild` to render the badge as a real `<a>` element. This activates the `[a&]:hover:*` styles and makes the badge fully accessible as a link.

```vue
<script setup lang="ts">
import { Badge } from "@/components/ui/badge"
</script>

<template>
  <!-- Renders as <a href="..."> with full badge styling -->
  <Badge asChild variant="outline">
    <a href="/changelog">v2.4.0</a>
  </Badge>
</template>
```

With Vue Router's `RouterLink`:

```vue
<script setup lang="ts">
import { Badge } from "@/components/ui/badge"
import { RouterLink } from "vue-router"
</script>

<template>
  <Badge asChild variant="default">
    <RouterLink to="/new-features">What's new</RouterLink>
  </Badge>
</template>
```

## 5. Custom colors

Override the variant styles with additional Tailwind classes via the `class` prop. The `cn()` utility inside the component merges them with `tailwind-merge`, so conflicting classes are resolved correctly.

```vue
<script setup lang="ts">
import { Badge } from "@/components/ui/badge"
</script>

<template>
  <div class="flex flex-wrap gap-2">
    <!-- Success green -->
    <Badge class="bg-green-500 text-white border-transparent hover:bg-green-600">
      Published
    </Badge>

    <!-- Warning amber -->
    <Badge class="bg-amber-400 text-amber-900 border-transparent">
      Pending review
    </Badge>

    <!-- Brand purple (outline style) -->
    <Badge variant="outline" class="border-purple-500 text-purple-600">
      Premium
    </Badge>

    <!-- Dark surface -->
    <Badge class="bg-zinc-900 text-zinc-100 border-transparent">
      Beta
    </Badge>
  </div>
</template>
```

## Bonus: Using `badgeVariants` without the component

Apply badge styles to arbitrary elements by importing the CVA function directly:

```vue
<script setup lang="ts">
import { badgeVariants } from "@/components/ui/badge"
import { cn } from "@/lib/utils"

const tags = ["Vue", "TypeScript", "Tailwind"]
</script>

<template>
  <ul class="flex flex-wrap gap-2 list-none p-0">
    <li
      v-for="tag in tags"
      :key="tag"
      :class="cn(badgeVariants({ variant: 'secondary' }))"
    >
      {{ tag }}
    </li>
  </ul>
</template>
```
