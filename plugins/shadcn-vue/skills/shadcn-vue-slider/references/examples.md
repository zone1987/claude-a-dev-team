# Examples

## Basic

Single thumb, default value 50.

```vue
<!-- SliderBasic.vue -->
<script setup lang="ts">
import { Slider } from "@/components/ui/slider"
</script>

<template>
  <Slider :default-value="[50]" :max="100" :step="1" />
</template>
```

## Range

Two thumbs defining a range.

```vue
<!-- SliderRange.vue -->
<script setup lang="ts">
import { Slider } from "@/components/ui/slider"
</script>

<template>
  <Slider :default-value="[25, 50]" :max="100" :step="5" />
</template>
```

## Multiple Thumbs

Three thumbs on the same track.

```vue
<!-- SliderMultiple.vue -->
<script setup lang="ts">
import { Slider } from "@/components/ui/slider"
</script>

<template>
  <Slider :default-value="[10, 20, 70]" :max="100" :step="10" />
</template>
```

## Vertical

Vertical orientation with custom height.

```vue
<!-- SliderVertical.vue -->
<script setup lang="ts">
import { Slider } from "@/components/ui/slider"
</script>

<template>
  <div class="flex items-center gap-6">
    <Slider
      :default-value="[50]"
      :max="100"
      :step="1"
      orientation="vertical"
      class="h-40"
    />
    <Slider
      :default-value="[25]"
      :max="100"
      :step="1"
      orientation="vertical"
      class="h-40"
    />
  </div>
</template>
```

## Controlled

Reactive value with label display.

```vue
<!-- SliderControlled.vue -->
<script setup lang="ts">
import { ref } from "vue"
import { Label } from "@/components/ui/label"
import { Slider } from "@/components/ui/slider"

const value = ref([0.3, 0.7])
</script>

<template>
  <div class="grid w-full gap-3">
    <div class="flex items-center justify-between gap-2">
      <Label html-for="slider-demo-temperature">Temperature</Label>
      <span class="text-muted-foreground text-sm">
        {{ value.join(", ") }}
      </span>
    </div>
    <Slider
      id="slider-demo-temperature"
      v-model="value"
      :min="0"
      :max="1"
      :step="0.1"
    />
  </div>
</template>
```

## Disabled

Slider in disabled state.

```vue
<!-- SliderDisabled.vue -->
<script setup lang="ts">
import { Slider } from "@/components/ui/slider"
</script>

<template>
  <Slider :default-value="[50]" :max="100" :step="1" :disabled="true" />
</template>
```

Sources:
- `registry/bases/reka/examples/slider/SliderBasic.vue`
- `registry/bases/reka/examples/slider/SliderRange.vue`
- `registry/bases/reka/examples/slider/SliderMultiple.vue`
- `registry/bases/reka/examples/slider/SliderVertical.vue`
- `registry/bases/reka/examples/slider/SliderControlled.vue`
- `registry/bases/reka/examples/slider/SliderDisabled.vue`
