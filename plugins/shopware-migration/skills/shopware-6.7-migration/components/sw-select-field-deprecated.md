# sw-select-field-deprecated

> **Deprecated in 6.7** — Use `mt-select` instead. Will be removed in 6.8.
> See [mt-select](mt-select.md) for the replacement.

## Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-select-field>` | `<mt-select>` |

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | `null` | no |  |
| placeholder | `any` | `null` | no |  |
| options | `any` | `null` | no |  |
| aside | `any` | `false` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| label | — | |
| hint | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

## Methods

| Method | Description |
|--------|-------------|
| `getOptionName` | |
| `onChange` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `locale` | |
| `fallbackLocale` | |
| `swFieldSelectClasses` | |
| `hasOptions` | |

## Examples

### Basic Usage
```twig
<sw-select-field-deprecated>
    <!-- content -->
</sw-select-field-deprecated>
```
