# sw-switch-field-deprecated

> **Deprecated in 6.7** — Use `mt-switch` instead. Will be removed in 6.8.
> See [mt-switch](mt-switch.md) for the replacement.

## Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-switch-field>` | `<mt-switch>` |

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| noMarginTop | `any` | `false` | no |  |
| size | `any` | `'default'` | no | Valid: `small`, `medium`, `default` |
| ariaLabel | `any` | — | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| label | — | |
| hint | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| inheritance-remove | — | |
| inheritance-restore | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onInheritanceRestore` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `swSwitchFieldClasses` | |

## Examples

### Basic Usage
```twig
<sw-switch-field-deprecated>
    <!-- content -->
</sw-switch-field-deprecated>
```
