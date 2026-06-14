# Examples

## Basic

Tags with v-model, render tag chips with delete buttons.

```vue
<!-- TagsInputBasic.vue -->
<script setup lang="ts">
import { ref } from "vue"
import { XIcon } from "@lucide/vue"
import {
  TagsInput,
  TagsInputInput,
  TagsInputItem,
  TagsInputItemDelete,
  TagsInputItemText,
} from "@/components/ui/tags-input"

const tags = ref(["Vue", "React", "Angular"])
</script>

<template>
  <TagsInput v-model="tags" class="w-full max-w-sm">
    <TagsInputItem v-for="tag in tags" :key="tag" :value="tag">
      <TagsInputItemText />
      <TagsInputItemDelete>
        <XIcon class="w-4 h-4" />
      </TagsInputItemDelete>
    </TagsInputItem>
    <TagsInputInput placeholder="Add tag..." />
  </TagsInput>
</template>
```

## With Label

Tags input inside a labeled field.

```vue
<!-- TagsInputWithLabel.vue -->
<script setup lang="ts">
import { ref } from "vue"
import { XIcon } from "@lucide/vue"
import { Label } from "@/components/ui/label"
import {
  TagsInput,
  TagsInputInput,
  TagsInputItem,
  TagsInputItemDelete,
  TagsInputItemText,
} from "@/components/ui/tags-input"

const tags = ref(["TypeScript", "JavaScript", "Python"])
</script>

<template>
  <div class="grid w-full max-w-sm items-center gap-1.5">
    <Label html-for="skills">Skills</Label>
    <TagsInput id="skills" v-model="tags">
      <TagsInputItem v-for="tag in tags" :key="tag" :value="tag">
        <TagsInputItemText />
        <TagsInputItemDelete>
          <XIcon class="w-4 h-4" />
        </TagsInputItemDelete>
      </TagsInputItem>
      <TagsInputInput placeholder="Add skill..." />
    </TagsInput>
  </div>
</template>
```

Sources:
- `registry/bases/reka/examples/tags-input/TagsInputBasic.vue`
- `registry/bases/reka/examples/tags-input/TagsInputWithLabel.vue`
