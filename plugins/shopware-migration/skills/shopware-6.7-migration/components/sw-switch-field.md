# sw-switch-field

> **Migration wrapper** — Delegates to `mt-switch` by default. The deprecated implementation is available via the `deprecated` prop.
> See [mt-switch](mt-switch.md) for the new component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | no |  |
| checked | `any` | — | no |  |
| deprecated | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onChangeHandler` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `checkedValue` | |

## Examples

### Basic Usage
```twig
<sw-switch-field>
    <!-- content -->
</sw-switch-field>
```
