# Label — Examples

## Example 1: Label with Input (LabelWithInput.vue)

Simple association of Label and Input via `html-for`.

```vue
<script setup lang="ts">
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
</script>

<template>
  <div class="grid gap-2">
    <Label html-for="label-demo-username">Username</Label>
    <Input id="label-demo-username" placeholder="Username" />
  </div>
</template>
```

---

## Example 2: Label with Checkbox (LabelWithCheckbox.vue)

Horizontal alignment with a Checkbox.

```vue
<script setup lang="ts">
import { Checkbox } from "@/components/ui/checkbox"
import { Label } from "@/components/ui/label"
</script>

<template>
  <div class="flex flex-row items-center gap-2">
    <Checkbox id="label-demo-terms" />
    <Label html-for="label-demo-terms">
      Accept terms and conditions
    </Label>
  </div>
</template>
```

---

## Example 3: Disabled (LabelDisabled.vue)

Disabled state via the `data-disabled` group pattern.

```vue
<script setup lang="ts">
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
</script>

<template>
  <div :data-disabled="true" class="group grid gap-2">
    <Label html-for="label-demo-disabled">
      Disabled
    </Label>
    <Input id="label-demo-disabled" placeholder="Disabled" disabled />
  </div>
</template>
```

---

## Example 4: Label with Textarea (LabelWithTextarea.vue)

```vue
<script setup lang="ts">
import { Label } from "@/components/ui/label"
import { Textarea } from "@/components/ui/textarea"
</script>

<template>
  <div class="grid gap-2">
    <Label html-for="label-demo-message">
      Message
    </Label>
    <Textarea id="label-demo-message" placeholder="Message" />
  </div>
</template>
```

---

## Sources
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/label/LabelWithInput.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/label/LabelWithCheckbox.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/label/LabelDisabled.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/label/LabelWithTextarea.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/label/LabelExample.vue`
