# sw-colorpicker

> **Migration wrapper** — Delegates to `mt-colorpicker` by default. The deprecated implementation is available via the `deprecated` prop.
> See [mt-colorpicker](mt-colorpicker.md) for the new component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `null \| null` | `null` | no |  |
| modelValue | `any` | — | no |  |
| deprecated | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| name | — | |

## Methods

| Method | Description |
|--------|-------------|
| `getSlots` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `currentValue` | |

## Examples

### Basic Usage
```twig
<sw-colorpicker>
    <!-- content -->
</sw-colorpicker>
```
