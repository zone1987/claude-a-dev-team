# sw-text-field

> **Migration wrapper** — Delegates to `mt-text-field` by default. The deprecated implementation is available via the `deprecated` prop.
> See [mt-text-field](mt-text-field.md) for the new component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| modelValue | `any` | `null` | no |  |
| value | `any` | `null` | no |  |
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
| `handleUpdateModelValue` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `compatValue` | |

## Examples

### Basic Usage
```twig
<sw-text-field>
    <!-- content -->
</sw-text-field>
```
