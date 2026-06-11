# sw-url-field

> **Migration wrapper** — Delegates to `mt-url-field` by default. The deprecated implementation is available via the `deprecated` prop.
> See [mt-url-field](mt-url-field.md) for the new component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| placeholder | `any` | — | no |  |
| value | `any` | — | no |  |
| modelValue | `any` | — | no |  |
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
<sw-url-field>
    <!-- content -->
</sw-url-field>
```
