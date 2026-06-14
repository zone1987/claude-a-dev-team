# Examples

## Basic

Switch with a label using the `Field` component.

```vue
<!-- SwitchBasic.vue -->
<script setup lang="ts">
import { Field, FieldLabel } from "@/components/ui/field"
import { Switch } from "@/components/ui/switch"
</script>

<template>
  <Field orientation="horizontal">
    <Switch id="switch-basic" />
    <FieldLabel html-for="switch-basic">
      Airplane Mode
    </FieldLabel>
  </Field>
</template>
```

## With Description

Switch with title and description text.

```vue
<!-- SwitchWithDescription.vue -->
<script setup lang="ts">
import {
  Field,
  FieldContent,
  FieldDescription,
  FieldLabel,
  FieldTitle,
} from "@/components/ui/field"
import { Switch } from "@/components/ui/switch"
</script>

<template>
  <FieldLabel html-for="switch-focus-mode">
    <Field orientation="horizontal">
      <FieldContent>
        <FieldTitle>Share across devices</FieldTitle>
        <FieldDescription>
          Focus is shared across devices, and turns off when you leave the
          app.
        </FieldDescription>
      </FieldContent>
      <Switch id="switch-focus-mode" />
    </Field>
  </FieldLabel>
</template>
```

## Disabled

Disabled in unchecked and checked states.

```vue
<!-- SwitchDisabled.vue -->
<script setup lang="ts">
import { Label } from "@/components/ui/label"
import { Switch } from "@/components/ui/switch"
</script>

<template>
  <div class="flex flex-col gap-12">
    <div class="flex items-center gap-2">
      <Switch id="switch-disabled-unchecked" :disabled="true" />
      <Label html-for="switch-disabled-unchecked">
        Disabled (Unchecked)
      </Label>
    </div>
    <div class="flex items-center gap-2">
      <Switch id="switch-disabled-checked" :default-checked="true" :disabled="true" />
      <Label html-for="switch-disabled-checked">
        Disabled (Checked)
      </Label>
    </div>
  </div>
</template>
```

## Sizes

Small and default size variants.

```vue
<!-- SwitchSizes.vue -->
<script setup lang="ts">
import { Label } from "@/components/ui/label"
import { Switch } from "@/components/ui/switch"
</script>

<template>
  <div class="flex flex-col gap-12">
    <div class="flex items-center gap-2">
      <Switch id="switch-size-sm" size="sm" />
      <Label html-for="switch-size-sm">Small</Label>
    </div>
    <div class="flex items-center gap-2">
      <Switch id="switch-size-default" size="default" />
      <Label html-for="switch-size-default">Default</Label>
    </div>
  </div>
</template>
```

Sources:
- `registry/bases/reka/examples/switch/SwitchBasic.vue`
- `registry/bases/reka/examples/switch/SwitchWithDescription.vue`
- `registry/bases/reka/examples/switch/SwitchDisabled.vue`
- `registry/bases/reka/examples/switch/SwitchSizes.vue`
