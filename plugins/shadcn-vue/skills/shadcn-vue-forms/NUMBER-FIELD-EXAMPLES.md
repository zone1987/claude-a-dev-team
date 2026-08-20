# NumberField — Beispiele

## Contents

- [Beispiel 1: Basic Number Field (NumberFieldBasic.vue)](#beispiel-1-basic-number-field-numberfieldbasicvue)
- [Beispiel 2: Number Field with Label (NumberFieldWithLabel.vue)](#beispiel-2-number-field-with-label-numberfieldwithlabelvue)
- [Beispiel 3: Disabled Number Field (NumberFieldDisabled.vue)](#beispiel-3-disabled-number-field-numberfielddisabledvue)
- [Quellen](#quellen)

## Beispiel 1: Basic Number Field (NumberFieldBasic.vue)

Einfaches Zahlenfeld mit Min/Max und Custom-Icons.

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

## Beispiel 2: Number Field with Label (NumberFieldWithLabel.vue)

Kombination mit `Label` und `id`-Prop fur Barrierefreiheit.

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

## Beispiel 3: Disabled Number Field (NumberFieldDisabled.vue)

Deaktiviertes Feld — alle Controls werden deaktiviert.

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

## Quellen
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/number-field/NumberFieldBasic.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/number-field/NumberFieldWithLabel.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/number-field/NumberFieldDisabled.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/number-field/NumberFieldExample.vue`
