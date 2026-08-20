# Carousel — Installation

## CLI (recommended)

```bash
npx shadcn-vue@latest add carousel
```

This installs the component files and the `embla-carousel-vue` dependency automatically.

## Manual Installation

### 1. Install peer dependency

```bash
npm install embla-carousel-vue
```

### 2. Copy source files

Copy all files from `registry/new-york-v4/ui/carousel/` (or `registry/bases/reka/ui/carousel/`) into your project's component folder, e.g. `src/components/ui/carousel/`:

- `Carousel.vue`
- `CarouselContent.vue`
- `CarouselItem.vue`
- `CarouselNext.vue`
- `CarouselPrevious.vue`
- `interface.ts`
- `useCarousel.ts`
- `index.ts`

### 3. Update import paths

Adjust all `@/lib/utils` and `@/registry/new-york-v4/ui/button` imports to match your project's alias structure.

### 4. Optional: Autoplay plugin

```bash
npm install embla-carousel-autoplay
```

Usage:

```vue
<script setup lang="ts">
import Autoplay from "embla-carousel-autoplay"
</script>

<template>
  <Carousel :plugins="[Autoplay({ delay: 2000 })]">
    ...
  </Carousel>
</template>
```

## Dependencies

| Package | Purpose |
|---------|---------|
| `embla-carousel-vue` | Core carousel engine |
| `@vueuse/core` | `createInjectionState` for context sharing |
| `@lucide/vue` | Arrow icons for Prev/Next buttons |
| shadcn-vue `Button` | Base for `CarouselPrevious` / `CarouselNext` |
