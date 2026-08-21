# Toggle — Examples

## Contents

- [Basic (Icons)](#basic-icons)
- [Outline Variant](#outline-variant)
- [Sizes](#sizes)
- [Disabled](#disabled)
- [With Text (Button Text comparison)](#with-text-button-text-comparison)
- [With Icon (Button Icon comparison)](#with-icon-button-icon-comparison)
- [With Icon + Text (Button comparison)](#with-icon-text-button-comparison)
- [Filled Icon on Active State](#filled-icon-on-active-state)

## Basic (Icons)

Three icon toggles for bold, italic, underline formatting. The first is pre-pressed via `:default-pressed="true"`.

```vue
<script setup lang="ts">
import { Toggle } from "@/components/ui/toggle"
import { BoldIcon, ItalicIcon, UnderlineIcon } from "lucide-vue-next"
</script>

<template>
  <div class="flex flex-wrap items-center gap-2">
    <Toggle aria-label="Toggle bold" :default-pressed="true">
      <BoldIcon />
    </Toggle>
    <Toggle aria-label="Toggle italic">
      <ItalicIcon />
    </Toggle>
    <Toggle aria-label="Toggle underline">
      <UnderlineIcon />
    </Toggle>
  </div>
</template>
```

Source: `registry/bases/reka/examples/toggle/ToggleBasic.vue`

---

## Outline Variant

Outline-bordered toggle with icon and label.

```vue
<script setup lang="ts">
import { Toggle } from "@/components/ui/toggle"
import { ItalicIcon, BoldIcon } from "lucide-vue-next"
</script>

<template>
  <div class="flex flex-wrap items-center gap-2">
    <Toggle variant="outline" aria-label="Toggle italic">
      <ItalicIcon />
      Italic
    </Toggle>
    <Toggle variant="outline" aria-label="Toggle bold">
      <BoldIcon />
      Bold
    </Toggle>
  </div>
</template>
```

Source: `registry/bases/reka/examples/toggle/ToggleOutline.vue`

---

## Sizes

All three size presets side by side.

```vue
<script setup lang="ts">
import { Toggle } from "@/components/ui/toggle"
</script>

<template>
  <div class="flex flex-wrap items-center gap-2">
    <Toggle variant="outline" aria-label="Toggle small" size="sm">
      Small
    </Toggle>
    <Toggle variant="outline" aria-label="Toggle default" size="default">
      Default
    </Toggle>
    <Toggle variant="outline" aria-label="Toggle large" size="lg">
      Large
    </Toggle>
  </div>
</template>
```

Source: `registry/bases/reka/examples/toggle/ToggleSizes.vue`

---

## Disabled

Both `default` and `outline` variants in disabled state.

```vue
<script setup lang="ts">
import { Toggle } from "@/components/ui/toggle"
</script>

<template>
  <div class="flex flex-wrap items-center gap-2">
    <Toggle aria-label="Toggle disabled" :disabled="true">
      Disabled
    </Toggle>
    <Toggle variant="outline" aria-label="Toggle disabled outline" :disabled="true">
      Disabled
    </Toggle>
  </div>
</template>
```

Source: `registry/bases/reka/examples/toggle/ToggleDisabled.vue`

---

## With Text (Button Text comparison)

Demonstrates how Toggle aligns with Button sizes across sm/default/lg.

```vue
<script setup lang="ts">
import { Button } from "@/components/ui/button"
import { Toggle } from "@/components/ui/toggle"
</script>

<template>
  <div class="flex flex-col gap-4">
    <div class="flex items-center gap-2">
      <Button size="sm" variant="outline">Button</Button>
      <Toggle variant="outline" aria-label="Toggle sm" size="sm">Toggle</Toggle>
    </div>
    <div class="flex items-center gap-2">
      <Button size="default" variant="outline">Button</Button>
      <Toggle variant="outline" aria-label="Toggle default" size="default">Toggle</Toggle>
    </div>
    <div class="flex items-center gap-2">
      <Button size="lg" variant="outline">Button</Button>
      <Toggle variant="outline" aria-label="Toggle lg" size="lg">Toggle</Toggle>
    </div>
  </div>
</template>
```

Source: `registry/bases/reka/examples/toggle/ToggleWithButtonText.vue`

---

## With Icon (Button Icon comparison)

Compares icon-only Button and Toggle at each size.

```vue
<script setup lang="ts">
import { Button } from "@/components/ui/button"
import { Toggle } from "@/components/ui/toggle"
import { BoldIcon, ItalicIcon, UnderlineIcon } from "lucide-vue-next"
</script>

<template>
  <div class="flex flex-col gap-4">
    <div class="flex items-center gap-2">
      <Button variant="outline" size="icon-sm"><BoldIcon /></Button>
      <Toggle variant="outline" aria-label="Toggle sm icon" size="sm"><BoldIcon /></Toggle>
    </div>
    <div class="flex items-center gap-2">
      <Button variant="outline" size="icon"><ItalicIcon /></Button>
      <Toggle variant="outline" aria-label="Toggle default icon" size="default"><ItalicIcon /></Toggle>
    </div>
    <div class="flex items-center gap-2">
      <Button variant="outline" size="icon-lg"><UnderlineIcon /></Button>
      <Toggle variant="outline" aria-label="Toggle lg icon" size="lg"><UnderlineIcon /></Toggle>
    </div>
  </div>
</template>
```

Source: `registry/bases/reka/examples/toggle/ToggleWithButtonIcon.vue`

---

## With Icon + Text (Button comparison)

Compares Button and Toggle with icon + text at each size.

```vue
<script setup lang="ts">
import { Button } from "@/components/ui/button"
import { Toggle } from "@/components/ui/toggle"
import { BoldIcon, ItalicIcon, UnderlineIcon } from "lucide-vue-next"
</script>

<template>
  <div class="flex flex-col gap-4">
    <div class="flex items-center gap-2">
      <Button size="sm" variant="outline"><BoldIcon />Button</Button>
      <Toggle variant="outline" aria-label="Toggle sm icon text" size="sm"><BoldIcon />Toggle</Toggle>
    </div>
    <div class="flex items-center gap-2">
      <Button size="default" variant="outline"><ItalicIcon />Button</Button>
      <Toggle variant="outline" aria-label="Toggle default icon text" size="default"><ItalicIcon />Toggle</Toggle>
    </div>
    <div class="flex items-center gap-2">
      <Button size="lg" variant="outline"><UnderlineIcon />Button</Button>
      <Toggle variant="outline" aria-label="Toggle lg icon text" size="lg"><UnderlineIcon />Toggle</Toggle>
    </div>
  </div>
</template>
```

Source: `registry/bases/reka/examples/toggle/ToggleWithButtonIconText.vue`

---

## Filled Icon on Active State

Uses `group-data-[state=on]/toggle:fill-accent-foreground` to fill the icon SVG when toggled on.

```vue
<script setup lang="ts">
import { Toggle } from "@/components/ui/toggle"
import { BookmarkIcon } from "lucide-vue-next"
</script>

<template>
  <div class="flex flex-wrap items-center gap-2">
    <Toggle aria-label="Toggle bookmark" :default-pressed="true">
      <BookmarkIcon class="group-data-[state=on]/toggle:fill-accent-foreground" />
    </Toggle>
    <Toggle variant="outline" aria-label="Toggle bookmark outline">
      <BookmarkIcon class="group-data-[state=on]/toggle:fill-accent-foreground" />
      Bookmark
    </Toggle>
  </div>
</template>
```

Source: `registry/bases/reka/examples/toggle/ToggleWithIcon.vue`
