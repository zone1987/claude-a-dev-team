# sw-password-field

> **Migration wrapper** — Delegates to `mt-password-field` by default. The deprecated implementation is available via the `deprecated` prop.
> See [mt-password-field](mt-password-field.md) for the new component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | no |  |
| modelValue | `any` | — | no |  |
| placeholder | `any` | `''` | no |  |
| deprecated | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| name | — | |

## Methods

| Method | Description |
|--------|-------------|
| `getSlots` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `realValue` | |

## Examples

### Basic Usage
```twig
<sw-password-field>
    <!-- content -->
</sw-password-field>
```
