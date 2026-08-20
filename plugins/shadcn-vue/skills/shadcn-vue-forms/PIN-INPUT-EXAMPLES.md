# PinInput — Examples

## Example 1: Basic Pin Input (PinInputBasic.vue)

4-digit PIN without a separator.

```vue
<script setup lang="ts">
import {
  PinInput,
  PinInputGroup,
  PinInputSlot,
} from "@/components/ui/pin-input"
</script>

<template>
  <PinInput>
    <PinInputGroup>
      <PinInputSlot v-for="(id, index) in 4" :key="id" :index="index" />
    </PinInputGroup>
  </PinInput>
</template>
```

---

## Example 2: Pin Input with Separator (PinInputWithSeparator.vue)

Two groups with a separator (e.g. for login codes like 123-456).

```vue
<script setup lang="ts">
import {
  PinInput,
  PinInputGroup,
  PinInputSeparator,
  PinInputSlot,
} from "@/components/ui/pin-input"
</script>

<template>
  <PinInput>
    <PinInputGroup>
      <PinInputSlot v-for="(id, index) in 3" :key="id" :index="index" />
    </PinInputGroup>
    <PinInputSeparator />
    <PinInputGroup>
      <PinInputSlot v-for="(id, index) in 3" :key="id" :index="index + 3" />
    </PinInputGroup>
  </PinInput>
</template>
```

---

## Example 3: Masked Pin Input (PinInputMasked.vue)

6-digit masked PIN (input is displayed as dots).

```vue
<script setup lang="ts">
import {
  PinInput,
  PinInputGroup,
  PinInputSlot,
} from "@/components/ui/pin-input"
</script>

<template>
  <PinInput :mask="true" type="text">
    <PinInputGroup>
      <PinInputSlot v-for="(id, index) in 6" :key="id" :index="index" />
    </PinInputGroup>
  </PinInput>
</template>
```

---

## Sources
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/pin-input/PinInputBasic.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/pin-input/PinInputWithSeparator.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/pin-input/PinInputMasked.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/pin-input/PinInputExample.vue`
