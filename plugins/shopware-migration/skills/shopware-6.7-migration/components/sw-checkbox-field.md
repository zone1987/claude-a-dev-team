# sw-checkbox-field

> **Migration wrapper** — Delegates to `mt-checkbox` by default. The deprecated implementation is available via the `deprecated` prop.
> See [mt-checkbox](mt-checkbox.md) for the new component.

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
| `handleUpdateChecked` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `compatValue` | |

## Examples

### Basic Usage
```twig
<sw-checkbox-field>
    <!-- content -->
</sw-checkbox-field>
```
