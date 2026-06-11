# sw-password-field-deprecated

> **Deprecated in 6.7** — Use `mt-password-field` instead. Will be removed in 6.8.
> See [mt-password-field](mt-password-field.md) for the replacement.

## Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-password-field>` | `<mt-password-field>` |

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| passwordToggleAble | `any` | `true` | no |  |
| placeholderIsPassword | `any` | `false` | no |  |
| autocomplete | `any` | `null` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| label | — | |
| hint | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| inheritance-restore | — | |
| inheritance-remove | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onTogglePasswordVisibility` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `typeFieldClass` | |
| `passwordPlaceholder` | |

## Examples

### Basic Usage
```twig
<sw-password-field-deprecated>
    <!-- content -->
</sw-password-field-deprecated>
```
