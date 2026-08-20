# Label — Beispiele

## Beispiel 1: Label with Input (LabelWithInput.vue)

Einfache Verknupfung von Label und Input via `html-for`.

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

## Beispiel 2: Label with Checkbox (LabelWithCheckbox.vue)

Horizontale Ausrichtung mit Checkbox.

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

## Beispiel 3: Disabled (LabelDisabled.vue)

Disabled-Zustand uber das `data-disabled`-Group-Pattern.

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

## Beispiel 4: Label with Textarea (LabelWithTextarea.vue)

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

## Quellen
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/label/LabelWithInput.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/label/LabelWithCheckbox.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/label/LabelDisabled.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/label/LabelWithTextarea.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/label/LabelExample.vue`
