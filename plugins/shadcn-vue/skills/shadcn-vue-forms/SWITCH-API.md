# API Reference

reka-ui API: https://reka-ui.com/docs/components/switch#api-reference

## Switch Props

Extends `SwitchRootProps` from reka-ui:

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `modelValue` | `boolean` | — | Controlled checked state |
| `defaultChecked` | `boolean` | `false` | Uncontrolled initial state |
| `checked` | `boolean` | — | Alternative controlled prop |
| `disabled` | `boolean` | `false` | Disables the switch |
| `required` | `boolean` | `false` | Required in a form |
| `name` | `string` | — | Form field name |
| `value` | `string` | `'on'` | Value submitted with forms |
| `class` | `string` | — | Additional CSS classes |

## Switch Emits

| Event | Payload | Description |
|-------|---------|-------------|
| `update:modelValue` | `boolean` | Emitted when checked state changes |
| `update:checked` | `boolean` | Alternative checked event |

## Slots

| Slot | Slot Props | Description |
|------|-----------|-------------|
| `#thumb` | `{ checked }` | Custom content inside the thumb |

## Data Attributes (reka-ui)

| Attribute | Values | Description |
|-----------|--------|-------------|
| `data-state` | `checked \| unchecked` | Current state |
| `data-disabled` | present | Switch is disabled |

## Usage with Label

```vue
<script setup lang="ts">
import { Label } from "@/components/ui/label"
import { Switch } from "@/components/ui/switch"
</script>

<template>
  <div class="flex items-center gap-2">
    <Switch id="airplane-mode" />
    <Label html-for="airplane-mode">Airplane Mode</Label>
  </div>
</template>
```
