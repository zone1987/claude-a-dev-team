# API Reference

reka-ui API: https://reka-ui.com/docs/components/slider#api-reference

## Sub-Komponenten

The `Slider` component wraps `SliderRoot`, `SliderTrack`, `SliderRange`,
and `SliderThumb` internally. Only `Slider` is exported.

## Slider Props

Extends `SliderRootProps` from reka-ui plus:

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `modelValue` | `number[]` | — | Controlled value (array of numbers) |
| `defaultValue` | `number[]` | — | Uncontrolled initial value |
| `min` | `number` | `0` | Minimum value |
| `max` | `number` | `100` | Maximum value |
| `step` | `number` | `1` | Step interval |
| `orientation` | `'horizontal' \| 'vertical'` | `'horizontal'` | Slider orientation |
| `disabled` | `boolean` | `false` | Disables interaction |
| `minStepsBetweenThumbs` | `number` | `0` | Min steps between thumbs |
| `class` | `string` | — | Additional CSS classes |

## Emits

| Event | Payload | Description |
|-------|---------|-------------|
| `update:modelValue` | `number[]` | Emitted when value changes |
| `valueCommit` | `number[]` | Emitted on pointer-up / keyboard end |

## Slots

The component renders thumbs internally via `v-for` over `modelValue`.
No default slot is exposed.

## Data Attributes (reka-ui)

| Attribute | Values |
|-----------|--------|
| `data-disabled` | Present when disabled |
| `data-orientation` | `horizontal` \| `vertical` |
