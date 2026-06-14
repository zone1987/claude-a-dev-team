# PinInput — Beispiele

## Beispiel 1: Basic Pin Input (PinInputBasic.vue)

4-stelliger PIN ohne Separator.

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

## Beispiel 2: Pin Input with Separator (PinInputWithSeparator.vue)

Zwei Gruppen mit Trennzeichen (z. B. fur Anmeldecodes wie 123-456).

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

## Beispiel 3: Masked Pin Input (PinInputMasked.vue)

6-stelliger maskierter PIN (Eingabe wird als Punkte angezeigt).

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

## Quellen
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/pin-input/PinInputBasic.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/pin-input/PinInputWithSeparator.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/pin-input/PinInputMasked.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/pin-input/PinInputExample.vue`
