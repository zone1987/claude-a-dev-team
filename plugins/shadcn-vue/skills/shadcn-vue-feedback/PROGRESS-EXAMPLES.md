# Examples

Source: `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/progress/`

---

## Contents

- [Progress Bar](#progress-bar)
- [With Label](#with-label)
- [Controlled](#controlled)
- [File Upload List](#file-upload-list)

## Progress Bar

`ProgressValues.vue` — demonstrates the full range of static progress values.

```vue
<script setup lang="ts">
import { Example } from "@/registry/bases/reka/components/example"
import { Progress } from "@/registry/bases/reka/ui/progress"
</script>

<template>
  <Example title="Progress Bar">
    <div class="flex w-full flex-col gap-4">
      <Progress :model-value="0" />
      <Progress :model-value="25" class="w-full" />
      <Progress :model-value="50" />
      <Progress :model-value="75" />
      <Progress :model-value="100" />
    </div>
  </Example>
</template>
```

---

## With Label

`ProgressWithLabel.vue` — combines a `Field` / `FieldLabel` wrapper with the
progress bar to show a title and the current percentage side by side.

```vue
<script setup lang="ts">
import { Example } from "@/registry/bases/reka/components/example"
import { Field, FieldLabel } from "@/registry/bases/reka/ui/field"
import { Progress } from "@/registry/bases/reka/ui/progress"
</script>

<template>
  <Example title="With Label">
    <Field>
      <FieldLabel html-for="progress-upload">
        <span>Upload progress</span>
        <span class="ml-auto">66%</span>
      </FieldLabel>
      <Progress id="progress-upload" :model-value="66" class="w-full" />
    </Field>
  </Example>
</template>
```

---

## Controlled

`ProgressControlled.vue` — the progress value is driven by a `Slider` so the
user can drag to change it in real time.

```vue
<script setup lang="ts">
import { ref } from "vue"
import { Example } from "@/registry/bases/reka/components/example"
import { Progress } from "@/registry/bases/reka/ui/progress"
import { Slider } from "@/registry/bases/reka/ui/slider"

const value = ref([50])
</script>

<template>
  <Example title="Controlled">
    <div class="flex w-full flex-col gap-4">
      <Progress :model-value="value[0]" class="w-full" />
      <Slider
        v-model="value"
        :min="0"
        :max="100"
        :step="1"
      />
    </div>
  </Example>
</template>
```

---

## File Upload List

`FileUploadList.vue` — an `ItemGroup` list that shows per-file progress bars
alongside file names and time-remaining labels.

```vue
<script setup lang="ts">
import { computed } from "vue"
import IconPlaceholder from "@/components/IconPlaceholder.vue"
import { Example } from "@/registry/bases/reka/components/example"
import {
  Item,
  ItemActions,
  ItemContent,
  ItemGroup,
  ItemMedia,
  ItemTitle,
} from "@/registry/bases/reka/ui/item"
import { Progress } from "@/registry/bases/reka/ui/progress"

const files = computed(() => [
  {
    id: "1",
    name: "document.pdf",
    progress: 45,
    timeRemaining: "2m 30s",
  },
  {
    id: "2",
    name: "presentation.pptx",
    progress: 78,
    timeRemaining: "45s",
  },
  {
    id: "3",
    name: "spreadsheet.xlsx",
    progress: 12,
    timeRemaining: "5m 12s",
  },
  {
    id: "4",
    name: "image.jpg",
    progress: 100,
    timeRemaining: "Complete",
  },
])
</script>

<template>
  <Example title="File Upload List">
    <ItemGroup>
      <Item
        v-for="file in files"
        :key="file.id"
        size="xs"
        class="px-0"
      >
        <ItemMedia variant="icon">
          <IconPlaceholder
            lucide="FileIcon"
            tabler="IconFile"
            hugeicons="FileIcon"
            phosphor="FileIcon"
            remixicon="RiFileLine"
            class="size-5"
          />
        </ItemMedia>
        <ItemContent class="inline-block truncate">
          <ItemTitle class="inline">
            {{ file.name }}
          </ItemTitle>
        </ItemContent>
        <ItemContent>
          <Progress :model-value="file.progress" class="w-32" />
        </ItemContent>
        <ItemActions class="w-16 justify-end">
          <span class="text-sm text-muted-foreground">
            {{ file.timeRemaining }}
          </span>
        </ItemActions>
      </Item>
    </ItemGroup>
  </Example>
</template>
```
