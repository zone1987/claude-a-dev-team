# shadcn-vue AspectRatio

The `AspectRatio` component displays content within a desired, fixed aspect ratio. It is a thin wrapper around the `AspectRatio` primitive from **reka-ui** and is a single-file Vue component.

## Overview

- Maintains a fixed width-to-height ratio regardless of container width
- Responsive by default — stretches to fill available width
- Accepts any slotted content (images, videos, iframes, etc.)
- Passes all props through to reka-ui's `AspectRatio`

## Component

`AspectRatio` is a single SFC (`AspectRatio.vue`) that re-exports the reka-ui primitive with a `data-slot="aspect-ratio"` attribute for Tailwind/CSS targeting.

### Key Prop

| Prop    | Type     | Default | Description                                      |
|---------|----------|---------|--------------------------------------------------|
| `ratio` | `number` | `1`     | Width / height ratio (e.g. `16/9`, `4/3`, `1`)  |

### Basic Usage

```vue
<script setup lang="ts">
import { AspectRatio } from '@/components/ui/aspect-ratio'
</script>

<template>
  <AspectRatio :ratio="16 / 9">
    <img src="..." alt="Image" class="rounded-md object-cover">
  </AspectRatio>
</template>
```

### Common Ratios

| Expression  | Ratio    | Use case              |
|-------------|----------|-----------------------|
| `16 / 9`    | Landscape | Video, wide banners  |
| `21 / 9`    | Ultrawide | Cinema banners       |
| `1 / 1`     | Square   | Avatars, thumbnails  |
| `9 / 16`    | Portrait | Mobile/story cards   |
| `4 / 3`     | Classic  | Legacy video/photos  |

## Reference Files

| File                            | Purpose                          |
|---------------------------------|----------------------------------|
| `ASPECT-RATIO-INSTALLATION.md`   | CLI and manual installation      |
| `ASPECT-RATIO-SOURCE.md`         | Complete source of both files    |
| `ASPECT-RATIO-API.md`            | Props API table                  |
| `ASPECT-RATIO-EXAMPLES.md`       | Four ratio examples (Vue SFCs)   |
