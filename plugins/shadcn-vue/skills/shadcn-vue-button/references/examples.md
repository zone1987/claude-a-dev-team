# Button — Examples

## 1. All Variants

```vue
<script setup lang="ts">
import { Button } from "@/components/ui/button"
</script>

<template>
  <div class="flex flex-wrap gap-4">
    <Button variant="default">Default</Button>
    <Button variant="destructive">Destructive</Button>
    <Button variant="outline">Outline</Button>
    <Button variant="secondary">Secondary</Button>
    <Button variant="ghost">Ghost</Button>
    <Button variant="link">Link</Button>
  </div>
</template>
```

## 2. All Sizes

```vue
<script setup lang="ts">
import { Button } from "@/components/ui/button"
</script>

<template>
  <div class="flex flex-wrap items-center gap-4">
    <Button size="sm">Small</Button>
    <Button size="default">Default</Button>
    <Button size="lg">Large</Button>
  </div>
</template>
```

## 3. Icon-Only Buttons

Use `size="icon"`, `size="icon-sm"`, or `size="icon-lg"` for square icon buttons. Always add an `aria-label` for accessibility.

```vue
<script setup lang="ts">
import { Button } from "@/components/ui/button"
import { Trash2, Settings, Plus } from "lucide-vue-next"
</script>

<template>
  <div class="flex items-center gap-4">
    <Button size="icon-sm" variant="outline" aria-label="Settings">
      <Settings />
    </Button>
    <Button size="icon" variant="default" aria-label="Add">
      <Plus />
    </Button>
    <Button size="icon-lg" variant="destructive" aria-label="Delete">
      <Trash2 />
    </Button>
  </div>
</template>
```

SVGs without an explicit `size-*` class are auto-sized to 16px via the base class `[&_svg:not([class*='size-'])]:size-4`.

## 4. Button with Icon Left / Right

```vue
<script setup lang="ts">
import { Button } from "@/components/ui/button"
import { Mail, ArrowRight, Loader2 } from "lucide-vue-next"
</script>

<template>
  <div class="flex flex-wrap gap-4">
    <!-- Icon on the left -->
    <Button>
      <Mail />
      Send Email
    </Button>

    <!-- Icon on the right -->
    <Button variant="outline">
      Continue
      <ArrowRight />
    </Button>

    <!-- Loading spinner (disabled state) -->
    <Button disabled>
      <Loader2 class="animate-spin" />
      Please wait
    </Button>
  </div>
</template>
```

The `gap-2` in the base class automatically spaces icon and text. Icon padding adapts via `has-[>svg]:px-3` (default) / `has-[>svg]:px-2.5` (sm) / `has-[>svg]:px-4` (lg).

## 5. asChild — Render as Link

Use `as-child` to render the button styles on a child element (e.g. `<a>`, `<RouterLink>`). The child receives all button classes and event handlers.

```vue
<script setup lang="ts">
import { Button } from "@/components/ui/button"
</script>

<template>
  <!-- Native anchor -->
  <Button as-child>
    <a href="/login">Login</a>
  </Button>

  <!-- Vue Router link -->
  <Button as-child variant="outline">
    <RouterLink to="/dashboard">Dashboard</RouterLink>
  </Button>

  <!-- External link -->
  <Button as-child variant="ghost" size="sm">
    <a href="https://example.com" target="_blank" rel="noopener noreferrer">
      External
    </a>
  </Button>
</template>
```

Alternatively, use the exported `buttonVariants` helper directly on a `<RouterLink>` without `asChild`:

```vue
<script setup lang="ts">
import { buttonVariants } from "@/components/ui/button"
</script>

<template>
  <RouterLink :class="buttonVariants({ variant: 'default', size: 'sm' })" to="/settings">
    Settings
  </RouterLink>
</template>
```
