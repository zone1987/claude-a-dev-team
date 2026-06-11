# sw-number-field

> **Migration wrapper** — Delegates to `mt-number-field` by default. The deprecated implementation is available via the `deprecated` prop.
> See [mt-number-field](mt-number-field.md) for the new component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | `null` | no |  |
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
<sw-number-field>
    <!-- content -->
</sw-number-field>
```
