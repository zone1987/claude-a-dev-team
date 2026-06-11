# sw-text-field-deprecated

> **Deprecated in 6.7** — Use `mt-text-field` instead. Will be removed in 6.8.
> See [mt-text-field](mt-text-field.md) for the replacement.

## Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-text-field>` | `<mt-text-field>` |

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | no |  |
| placeholder | `any` | `''` | no |  |
| copyable | `any` | `false` | no |  |
| copyableTooltip | `any` | `false` | no |  |
| idSuffix | `any` | — | no |  |
| ariaLabel | `any` | — | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| prefix | — | |
| suffix | — | |
| label | — | |
| hint | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |
| inheritance-restore | — | |
| inheritance-remove | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onChange` | |
| `onInput` | |
| `restoreInheritance` | |
| `createInputId` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `hasPrefix` | |
| `hasSuffix` | |
| `filteredInputAttributes` | |

## Examples

### Basic Usage
```twig
<sw-text-field-deprecated>
    <!-- content -->
</sw-text-field-deprecated>
```
