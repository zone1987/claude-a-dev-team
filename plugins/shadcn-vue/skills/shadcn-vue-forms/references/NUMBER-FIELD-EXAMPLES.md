# NumberField — Examples

## Contents

- [Example 1: Basic Number Field (NumberFieldBasic.vue)](#example-1-basic-number-field-numberfieldbasicvue)
- [Example 2: Number Field with Label (NumberFieldWithLabel.vue)](#example-2-number-field-with-label-numberfieldwithlabelvue)
- [Example 3: Disabled Number Field (NumberFieldDisabled.vue)](#example-3-disabled-number-field-numberfielddisabledvue)
- [Sources](#sources)

## Example 1: Basic Number Field (NumberFieldBasic.vue)

Simple number field with min/max and custom icons.

```vue
<script setup lang="ts">
import { MinusIcon, PlusIcon } from "@lucide/vue"
import {
  NumberField,
  NumberFieldContent,
  NumberFieldDecrement,
  NumberFieldIncrement,
  NumberFieldInput,
} from "@/components/ui/number-field"
</script>

<template>
  <NumberField :default-value="10" :min="0" :max="100">
    <NumberFieldContent>
      <NumberFieldDecrement>
        <MinusIcon />
      </NumberFieldDecrement>
      <NumberFieldInput />
      <NumberFieldIncrement>
        <PlusIcon />
      </NumberFieldIncrement>
    </NumberFieldContent>
  </NumberField>
</template>
```

---

## Example 2: Number Field with Label (NumberFieldWithLabel.vue)

Combined with `Label` and the `id` prop for accessibility.

```vue
<script setup lang="ts">
import { MinusIcon, PlusIcon } from "@lucide/vue"
import { Label } from "@/components/ui/label"
import {
  NumberField,
  NumberFieldContent,
  NumberFieldDecrement,
  NumberFieldIncrement,
  NumberFieldInput,
} from "@/components/ui/number-field"
</script>

<template>
  <div class="grid w-full max-w-sm items-center gap-1.5">
    <Label html-for="quantity">Quantity</Label>
    <NumberField id="quantity" :default-value="5" :min="1" :max="50">
      <NumberFieldContent>
        <NumberFieldDecrement>
          <MinusIcon />
        </NumberFieldDecrement>
        <NumberFieldInput />
        <NumberFieldIncrement>
          <PlusIcon />
        </NumberFieldIncrement>
      </NumberFieldContent>
    </NumberField>
  </div>
</template>
```

---

## Example 3: Disabled Number Field (NumberFieldDisabled.vue)

Disabled field — all controls are disabled.

```vue
<script setup lang="ts">
import { MinusIcon, PlusIcon } from "@lucide/vue"
import {
  NumberField,
  NumberFieldContent,
  NumberFieldDecrement,
  NumberFieldIncrement,
  NumberFieldInput,
} from "@/components/ui/number-field"
</script>

<template>
  <NumberField :default-value="10" :min="0" :max="100" :disabled="true">
    <NumberFieldContent>
      <NumberFieldDecrement>
        <MinusIcon />
      </NumberFieldDecrement>
      <NumberFieldInput />
      <NumberFieldIncrement>
        <PlusIcon />
      </NumberFieldIncrement>
    </NumberFieldContent>
  </NumberField>
</template>
```

---

## Sources
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/number-field/NumberFieldBasic.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/number-field/NumberFieldWithLabel.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/number-field/NumberFieldDisabled.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/number-field/NumberFieldExample.vue`
