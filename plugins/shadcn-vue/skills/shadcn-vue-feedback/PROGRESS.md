# shadcn-vue Progress

The Progress component displays a progress bar that indicates the completion
status of a task. It is built on top of the `ProgressRoot` and
`ProgressIndicator` primitives from reka-ui and styled with Tailwind v4.

## Contents

- [Sub-components](#sub-components)
- [Props](#props)
- [Usage patterns](#usage-patterns)
- [Styling](#styling)
- [Accessibility](#accessibility)
- [Files](#files)
- [References](#references)

## Sub-components

### ProgressRoot (via `<Progress>`)

The root container. Renders a `<div>` with `role="progressbar"` and the
appropriate ARIA attributes (`aria-valuemin`, `aria-valuemax`,
`aria-valuenow`). Accepts all `ProgressRootProps` from reka-ui plus an
optional `class` prop.

### ProgressIndicator (internal)

The inner bar that moves to reflect the current value. Its horizontal
position is calculated with a CSS `transform: translateX(-N%)` where N equals
`100 - modelValue`. This keeps the visual state in sync with the numeric
value without requiring JavaScript-driven width changes.

## Props

| Prop            | Type                                 | Default | Description                              |
|-----------------|--------------------------------------|---------|------------------------------------------|
| `modelValue`    | `number`                             | `0`     | Current progress value (0 to `max`).     |
| `max`           | `number`                             | `100`   | Maximum progress value.                  |
| `getValueLabel` | `(value: number, max: number) => string` | —   | Custom accessibility label for the value.|
| `class`         | `string`                             | —       | Additional CSS classes on the root.      |

All remaining `ProgressRootProps` from reka-ui are forwarded to `ProgressRoot`
via `reactiveOmit` / `v-bind`.

## Usage patterns

### Controlled value

Bind `:model-value` to a reactive number (0–100) to keep the bar in sync with
application state:

```vue
<script setup lang="ts">
import { ref } from "vue"
import { Progress } from "@/components/ui/progress"

const uploadProgress = ref(0)
</script>

<template>
  <Progress :model-value="uploadProgress" />
</template>
```

### With a label

Combine with the `Field` / `FieldLabel` components for accessible labelling:

```vue
<template>
  <Field>
    <FieldLabel html-for="upload">
      <span>Uploading...</span>
      <span class="ml-auto">{{ progress }}%</span>
    </FieldLabel>
    <Progress id="upload" :model-value="progress" />
  </Field>
</template>
```

### Custom max value

When your domain uses a value range other than 0–100, pass `max` explicitly:

```vue
<Progress :model-value="3" :max="5" />
```

## Styling

The root element carries `data-slot="progress"` and the indicator carries
`data-slot="progress-indicator"`. Use these data-attributes for CSS
overrides without relying on class names:

```css
[data-slot="progress"] {
  height: 0.5rem;
}
[data-slot="progress-indicator"] {
  background: theme(colors.green.500);
}
```

## Accessibility

- The component renders with `role="progressbar"`.
- `aria-valuemin` defaults to `0`, `aria-valuemax` to `max`.
- `aria-valuenow` reflects `modelValue`.
- Use `getValueLabel` to provide a human-readable label, e.g.
  `(v, m) => \`${v} of ${m} steps complete\``.

## Files

- `src/components/ui/progress/Progress.vue` — main component
- `src/components/ui/progress/index.ts` — barrel export

## References

- Installation: `PROGRESS-INSTALLATION.md`
- Source code: `PROGRESS-SOURCE.md`
- API reference: `PROGRESS-API.md`
- Usage examples: `PROGRESS-EXAMPLES.md`
- reka-ui docs: https://reka-ui.com/docs/components/progress
